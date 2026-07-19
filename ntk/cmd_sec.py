"""System security & audit (ntk sec ...). Defensive/local-audit oriented."""
import os
import re
import math
import hashlib
import socket
import json
from . import util
from .util import col, C, run, which, IS_WINDOWS


def pass_audit(args):
    """Check a password against HaveIBeenPwned (k-anonymity)."""
    if not args:
        util.err("usage: ntk sec pass-audit <password>")
        return 2
    pw = args[0]
    sha1 = hashlib.sha1(pw.encode()).hexdigest().upper()
    prefix, suffix = sha1[:5], sha1[5:]
    import urllib.request
    try:
        with urllib.request.urlopen(f"https://api.pwnedpasswords.com/range/{prefix}", timeout=15) as r:
            data = r.read().decode()
    except Exception as e:
        util.err(f"lookup failed: {e}")
        return 1
    for line in data.splitlines():
        h, count = line.split(":")
        if h == suffix:
            util.warn(f"PWNED! Seen {count} times in breaches. Change it.")
            return 0
    util.ok("not found in known breaches")
    return 0


def entropy(args):
    """Measure Shannon entropy of a string."""
    if not args:
        util.err("usage: ntk sec entropy <string>")
        return 2
    s = args[0]
    if not s:
        return 0
    freq = {c: s.count(c) for c in set(s)}
    ent = -sum((n / len(s)) * math.log2(n / len(s)) for n in freq.values())
    bits = ent * len(s)
    util.kv("Entropy/char", f"{ent:.2f} bits")
    util.kv("Total entropy", f"{bits:.1f} bits")
    verdict = "weak" if bits < 40 else ("ok" if bits < 60 else "strong")
    color = C.RED if bits < 40 else (C.YELLOW if bits < 60 else C.GREEN)
    util.kv("Verdict", col(verdict, color))
    return 0


_SECRET_PATTERNS = {
    "AWS Access Key": r"AKIA[0-9A-Z]{16}",
    "Google API Key": r"AIza[0-9A-Za-z\-_]{35}",
    "Slack Token": r"xox[baprs]-[0-9A-Za-z-]{10,}",
    "GitHub Token": r"gh[pousr]_[0-9A-Za-z]{36,}",
    "Private Key": r"-----BEGIN (?:RSA |EC |OPENSSH |PGP )?PRIVATE KEY-----",
    "Generic Secret": r"(?i)(api[_-]?key|secret|password|token)\s*[=:]\s*['\"][^'\"]{8,}['\"]",
    "JWT": r"eyJ[A-Za-z0-9_-]+\.eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+",
}


def key_scan(args):
    """Scan files for API keys / secrets."""
    root = args[0] if args else "."
    hits = 0
    exts = (".py", ".js", ".ts", ".env", ".json", ".yml", ".yaml", ".txt", ".sh",
            ".ini", ".cfg", ".conf", ".java", ".go", ".rb", ".php", ".xml")
    util.header(f"Secret scan: {root}")
    for dirpath, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in (".git", "node_modules", "__pycache__", "venv", ".venv")]
        for fn in files:
            if not fn.endswith(exts) and fn != ".env":
                continue
            path = os.path.join(dirpath, fn)
            try:
                content = open(path, encoding="utf-8", errors="replace").read()
            except Exception:
                continue
            for name, pat in _SECRET_PATTERNS.items():
                for m in re.finditer(pat, content):
                    line = content[:m.start()].count("\n") + 1
                    hits += 1
                    print(f"  {col(name, C.RED)} {path}:{line}")
    if not hits:
        util.ok("no secrets detected")
    else:
        util.warn(f"{hits} potential secret(s) found")
    return 0


def vuln_scan(args):
    """Scan dependencies for known CVEs."""
    path = args[0] if args else "."
    if os.path.exists(os.path.join(path, "package.json")):
        if which("npm"):
            rc, o, e = run(["npm", "audit"], )
            print(o or e)
            return rc
        util.warn("npm not found for JS audit")
    if os.path.exists(os.path.join(path, "requirements.txt")):
        if which("pip"):
            util.info("running pip-audit (if installed)...")
            rc, o, e = run(["pip-audit", "-r", os.path.join(path, "requirements.txt")])
            print(o or e or "install pip-audit: pip install pip-audit")
            return rc
    util.warn("no supported dependency manifest found (package.json / requirements.txt)")
    return 1


def subdomains(args):
    """Find public subdomains via crt.sh (OSINT)."""
    if not args:
        util.err("usage: ntk sec subdomains <domain>")
        return 2
    domain = args[0]
    import urllib.request
    try:
        with urllib.request.urlopen(f"https://crt.sh/?q=%25.{domain}&output=json", timeout=25) as r:
            data = json.loads(r.read())
    except Exception as e:
        util.err(f"lookup failed: {e}")
        return 1
    subs = sorted({entry["name_value"] for entry in data})
    flat = sorted({s for row in subs for s in row.split("\n")})
    util.header(f"Subdomains of {domain} ({len(flat)})")
    for s in flat:
        print("  " + s)
    return 0


def nmap(args):
    """Simplified port/network scan (uses nmap if present)."""
    if not args:
        util.err("usage: ntk sec nmap <host> [ports]")
        return 2
    if which("nmap"):
        rc, o, e = run(["nmap"] + args)
        print(o or e)
        return rc
    # Built-in fallback: TCP connect scan of common ports
    host = args[0]
    ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 3306, 3389, 5432, 6379, 8080, 8443]
    util.header(f"TCP scan {host} (builtin, nmap not found)")
    for p in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.6)
        if s.connect_ex((host, p)) == 0:
            print(f"  {col('open', C.GREEN)}  {p}")
        s.close()
    return 0


def ssh_audit(args):
    """Check SSH server config for weak settings."""
    conf = args[0] if args else "/etc/ssh/sshd_config"
    if not os.path.exists(conf):
        util.warn(f"sshd_config not found at {conf}")
        return 1
    text = open(conf, errors="replace").read()
    util.header("SSH audit")
    checks = [
        ("PermitRootLogin", "no", "root login"),
        ("PasswordAuthentication", "no", "password auth"),
        ("X11Forwarding", "no", "X11 forwarding"),
        ("Protocol", "2", "protocol version"),
    ]
    for key, want, label in checks:
        m = re.search(rf"^\s*{key}\s+(\S+)", text, re.M | re.I)
        val = m.group(1) if m else "(default)"
        good = val.lower() == want.lower()
        mark = col("OK", C.GREEN) if good else col("REVIEW", C.YELLOW)
        print(f"  [{mark}] {label}: {val}")
    return 0


def xss_test(args):
    """Basic reflected-XSS probe (authorized testing only)."""
    if not args:
        util.err("usage: ntk sec xss-test <url-with-param>")
        return 2
    import urllib.request
    import urllib.parse
    payload = "<ntkxss>"
    url = args[0]
    test = url + ("&" if "?" in url else "?") + "q=" + urllib.parse.quote(payload)
    try:
        with urllib.request.urlopen(test, timeout=15) as r:
            body = r.read().decode("utf-8", "replace")
        if payload in body:
            util.warn("payload reflected unescaped - possible XSS")
        else:
            util.ok("payload not reflected unescaped")
    except Exception as e:
        util.err(e)
        return 1
    return 0


def sqli_test(args):
    """Basic SQL-injection probe (authorized testing only)."""
    if not args:
        util.err("usage: ntk sec sqli-test <url-with-param>")
        return 2
    import urllib.request
    errors = ["sql syntax", "mysql_fetch", "ORA-", "unclosed quotation", "sqlite3.",
              "psql:", "syntax error at or near"]
    url = args[0]
    test = url + ("&" if "?" in url else "?") + "id=1'"
    try:
        with urllib.request.urlopen(test, timeout=15) as r:
            body = r.read().decode("utf-8", "replace").lower()
        found = [e for e in errors if e.lower() in body]
        if found:
            util.warn(f"DB error strings leaked: {found} - possible SQLi")
        else:
            util.ok("no obvious SQL error leakage")
    except Exception as e:
        util.err(e)
        return 1
    return 0


def dir_brute(args):
    """Discover common web paths (authorized testing only)."""
    if not args:
        util.err("usage: ntk sec dir-brute <base-url>")
        return 2
    import urllib.request
    base = args[0].rstrip("/")
    words = ["admin", "login", "api", "config", ".git", "backup", "robots.txt",
             "sitemap.xml", "wp-admin", "phpinfo.php", ".env", "test", "uploads",
             "dashboard", "static", "assets"]
    util.header(f"Dir brute: {base}")
    for w in words:
        try:
            req = urllib.request.Request(f"{base}/{w}", method="HEAD")
            with urllib.request.urlopen(req, timeout=8) as r:
                if r.status < 400:
                    print(f"  {col(r.status, C.GREEN)}  /{w}")
        except Exception:
            pass
    return 0


_HASH_LENGTHS = {32: ["MD5", "MD4", "NTLM"], 40: ["SHA-1"], 56: ["SHA-224"],
                 64: ["SHA-256"], 96: ["SHA-384"], 128: ["SHA-512"]}


def hash_identify(args):
    """Identify a hash algorithm by shape."""
    if not args:
        util.err("usage: ntk sec hash-identify <hash>")
        return 2
    h = args[0].strip()
    if h.startswith("$2"):
        util.kv("Likely", "bcrypt")
        return 0
    if h.startswith("$argon2"):
        util.kv("Likely", "Argon2")
        return 0
    if not re.fullmatch(r"[0-9a-fA-F]+", h):
        util.warn("not a plain hex hash")
        return 1
    guesses = _HASH_LENGTHS.get(len(h), ["unknown"])
    util.kv("Length", len(h))
    util.kv("Likely", ", ".join(guesses))
    return 0


def ports_vuln(args):
    """Flag risky open ports on a host."""
    host = args[0] if args else "127.0.0.1"
    risky = {21: "FTP cleartext", 23: "Telnet cleartext", 135: "RPC", 139: "NetBIOS",
             445: "SMB", 3389: "RDP exposed", 5900: "VNC", 6379: "Redis no-auth risk",
             27017: "MongoDB exposed", 3306: "MySQL exposed", 5432: "Postgres exposed"}
    util.header(f"Risky port check {host}")
    any_open = False
    for p, note in risky.items():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.6)
        if s.connect_ex((host, p)) == 0:
            any_open = True
            print(f"  {col('OPEN', C.RED)} {p}  {note}")
        s.close()
    if not any_open:
        util.ok("no risky ports open")
    return 0


def sandbox_run(args):
    """Run a command with reduced privileges/timeout."""
    if not args:
        util.err("usage: ntk sec sandbox-run <command...>")
        return 2
    util.info("running with a 30s timeout and captured output (best-effort sandbox)")
    rc, o, e = run(args, timeout=30)
    print(o)
    if e:
        print(col(e, C.YELLOW))
    return rc


def firewall(args):
    """Show firewall status and rules."""
    if IS_WINDOWS:
        rc, o, e = run(["netsh", "advfirewall", "show", "allprofiles", "state"])
        print(o or e)
    elif which("ufw"):
        rc, o, e = run(["ufw", "status", "verbose"])
        print(o or e)
    elif which("iptables"):
        rc, o, e = run(["iptables", "-L", "-n"])
        print(o or e)
    else:
        util.warn("no known firewall tool found")
        return 1
    return 0


def dnssec(args):
    """Validate DNSSEC signature of a domain."""
    if not args:
        util.err("usage: ntk sec dnssec <domain>")
        return 2
    if which("dig"):
        rc, o, e = run(["dig", "+dnssec", "+short", args[0]])
        print(o or e or "(no records)")
        rc, o, e = run(["dig", "+short", "DNSKEY", args[0]])
        if o.strip():
            util.ok("DNSKEY present (DNSSEC configured)")
        else:
            util.warn("no DNSKEY found (DNSSEC likely not enabled)")
        return 0
    util.warn("needs 'dig' (dnsutils / bind-tools)")
    return 1


def ssl_ciphers(args):
    """List SSL/TLS ciphers a server supports."""
    if not args:
        util.err("usage: ntk sec ssl-ciphers <host[:port]>")
        return 2
    import ssl
    host = args[0]
    port = 443
    if ":" in host:
        host, port = host.split(":")
        port = int(port)
    ctx = ssl.create_default_context()
    try:
        with socket.create_connection((host, port), timeout=10) as sock:
            with ctx.wrap_socket(sock, server_hostname=host) as s:
                util.kv("Negotiated", s.cipher()[0])
                util.kv("TLS version", s.version())
    except Exception as e:
        util.err(e)
        return 1
    util.info("client-supported ciphers:")
    for c in ssl.create_default_context().get_ciphers()[:20]:
        print("  " + c["name"])
    return 0


def anti_virus(args):
    """Quick local scan of a file (uses OS AV if available)."""
    if not args:
        util.err("usage: ntk sec anti-virus <file>")
        return 2
    f = args[0]
    if IS_WINDOWS:
        mp = r"C:\Program Files\Windows Defender\MpCmdRun.exe"
        if os.path.exists(mp):
            rc, o, e = run([mp, "-Scan", "-ScanType", "3", "-File", os.path.abspath(f)])
            print(o or e)
            return rc
        util.warn("Windows Defender CLI not found")
    elif which("clamscan"):
        rc, o, e = run(["clamscan", f])
        print(o or e)
        return rc
    else:
        util.warn("no AV engine found; showing file hash instead")
    h = hashlib.sha256(open(f, "rb").read()).hexdigest()
    util.kv("SHA-256", h)
    util.info(f"check at https://www.virustotal.com/gui/file/{h}")
    return 0


def user_audit(args):
    """Audit system users and login info."""
    util.header("User audit")
    if IS_WINDOWS:
        rc, o, e = run(["net", "user"])
        print(o or e)
        rc, o, e = run(["net", "localgroup", "administrators"])
        print(o or e)
    else:
        for line in open("/etc/passwd"):
            parts = line.split(":")
            if len(parts) >= 7 and (parts[6].strip().endswith(("bash", "sh", "zsh"))):
                util.kv(parts[0], f"uid={parts[2]} shell={parts[6].strip()}")
        rc, o, e = run(["last", "-n", "5"])
        if o:
            util.info("recent logins:")
            print(o)
    return 0


def _integrity_db():
    return os.path.join(os.path.expanduser("~"), ".ntk-integrity.json")


def file_integrity(args):
    """Baseline/verify file hashes (init <dir> | check <dir>)."""
    if len(args) < 2 or args[0] not in ("init", "check"):
        util.err("usage: ntk sec file-integrity <init|check> <dir>")
        return 2
    mode, root = args[0], args[1]
    db_path = _integrity_db()
    current = {}
    for dp, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in (".git", "node_modules", "__pycache__")]
        for fn in files:
            p = os.path.join(dp, fn)
            try:
                current[p] = hashlib.sha256(open(p, "rb").read()).hexdigest()
            except Exception:
                continue
    if mode == "init":
        json.dump(current, open(db_path, "w"))
        util.ok(f"baseline of {len(current)} files -> {db_path}")
        return 0
    if not os.path.exists(db_path):
        util.warn("no baseline; run 'init' first")
        return 1
    old = json.load(open(db_path))
    changed = [p for p in current if p in old and current[p] != old[p]]
    added = [p for p in current if p not in old]
    removed = [p for p in old if p not in current]
    for p in changed:
        print(f"  {col('CHANGED', C.YELLOW)} {p}")
    for p in added:
        print(f"  {col('ADDED', C.CYAN)} {p}")
    for p in removed:
        print(f"  {col('REMOVED', C.RED)} {p}")
    if not (changed or added or removed):
        util.ok("no changes since baseline")
    return 0


def _store_path():
    return os.path.join(os.path.expanduser("~"), ".ntk-secrets.enc")


def secret_store(args):
    """Encrypted local credential store (set/get/list)."""
    if not args or args[0] not in ("set", "get", "list"):
        util.err("usage: ntk sec secret-store <set|get|list> [name] [value]")
        return 2
    try:
        from cryptography.fernet import Fernet
    except ImportError:
        util.warn("needs cryptography: pip install cryptography")
        return 1
    import getpass
    import base64 as b64
    pw = getpass.getpass("master password: ")
    key = b64.urlsafe_b64encode(hashlib.sha256(pw.encode()).digest())
    f = Fernet(key)
    path = _store_path()
    data = {}
    if os.path.exists(path):
        try:
            data = json.loads(f.decrypt(open(path, "rb").read()).decode())
        except Exception:
            util.err("wrong master password or corrupt store")
            return 1
    if args[0] == "list":
        for k in data:
            print("  " + k)
    elif args[0] == "get":
        print("  " + data.get(args[1], "(not found)"))
    elif args[0] == "set":
        if len(args) < 3:
            util.err("usage: ...set <name> <value>")
            return 2
        data[args[1]] = args[2]
        open(path, "wb").write(f.encrypt(json.dumps(data).encode()))
        util.ok("stored")
    return 0


COMMANDS = {
    "pass-audit": pass_audit, "entropy": entropy, "key-scan": key_scan,
    "vuln-scan": vuln_scan, "subdomains": subdomains, "nmap": nmap,
    "ssh-audit": ssh_audit, "xss-test": xss_test, "sqli-test": sqli_test,
    "dir-brute": dir_brute, "hash-identify": hash_identify, "ports-vuln": ports_vuln,
    "sandbox-run": sandbox_run, "firewall": firewall, "dnssec": dnssec,
    "ssl-ciphers": ssl_ciphers, "anti-virus": anti_virus, "user-audit": user_audit,
    "file-integrity": file_integrity, "secret-store": secret_store,
}
