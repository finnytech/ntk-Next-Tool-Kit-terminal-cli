"""Advanced web & API tools (ntk web ...)."""
import time
import json
import socket
import ssl
import urllib.request
import urllib.parse
import random
from html.parser import HTMLParser
from . import util
from .util import col, C, run, which

_UA = "Mozilla/5.0 (compatible; ntk/1.0)"


def _fetch(url, method="GET", timeout=15, headers=None, data=None):
    h = {"User-Agent": _UA}
    if headers:
        h.update(headers)
    req = urllib.request.Request(url, method=method, headers=h, data=data)
    return urllib.request.urlopen(req, timeout=timeout)


def headers(args):
    """Analyze HTTP security headers (CSP/HSTS/etc.)."""
    if not args:
        util.err("usage: ntk web headers <url>")
        return 2
    try:
        r = _fetch(args[0])
        hd = dict(r.headers)
    except Exception as e:
        util.err(e)
        return 1
    util.header("Security headers")
    checks = {
        "Content-Security-Policy": "CSP",
        "Strict-Transport-Security": "HSTS",
        "X-Frame-Options": "Clickjacking protection",
        "X-Content-Type-Options": "MIME sniffing protection",
        "Referrer-Policy": "Referrer policy",
        "Permissions-Policy": "Permissions policy",
    }
    for hk, label in checks.items():
        val = hd.get(hk)
        mark = col("SET", C.GREEN) if val else col("MISSING", C.RED)
        print(f"  [{mark}] {label}")
    return 0


def bench(args):
    """Load-test a URL (N requests, req/s)."""
    if not args:
        util.err("usage: ntk web bench <url> [count=20]")
        return 2
    n = int(args[1]) if len(args) > 1 else 20
    times = []
    ok_count = 0
    t_all = time.time()
    for _ in range(n):
        t0 = time.time()
        try:
            r = _fetch(args[0], timeout=20)
            r.read()
            ok_count += 1
            times.append((time.time() - t0) * 1000)
        except Exception:
            pass
    total = time.time() - t_all
    util.header("Benchmark")
    util.kv("Requests", f"{ok_count}/{n} ok")
    if times:
        util.kv("Avg", f"{sum(times)/len(times):.0f} ms")
        util.kv("Min/Max", f"{min(times):.0f} / {max(times):.0f} ms")
    util.kv("Throughput", f"{ok_count/total:.1f} req/s")
    return 0


class _LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for k, v in attrs:
                if k == "href" and v:
                    self.links.append(v)


def broken_links(args):
    """Find broken links (404s) on a page."""
    if not args:
        util.err("usage: ntk web broken-links <url>")
        return 2
    base = args[0]
    try:
        html = _fetch(base).read().decode("utf-8", "replace")
    except Exception as e:
        util.err(e)
        return 1
    p = _LinkParser()
    p.feed(html)
    util.header(f"Link check ({len(p.links)} links)")
    checked = set()
    for link in p.links:
        full = urllib.parse.urljoin(base, link)
        if full in checked or not full.startswith("http"):
            continue
        checked.add(full)
        try:
            r = _fetch(full, method="HEAD", timeout=8)
            if r.status >= 400:
                print(f"  {col(r.status, C.RED)} {full}")
        except urllib.error.HTTPError as e:
            print(f"  {col(e.code, C.RED)} {full}")
        except Exception:
            print(f"  {col('ERR', C.YELLOW)} {full}")
    util.ok("done")
    return 0


def sitemap(args):
    """List URLs from a sitemap.xml."""
    if not args:
        util.err("usage: ntk web sitemap <url>")
        return 2
    url = args[0]
    if not url.endswith(".xml"):
        url = url.rstrip("/") + "/sitemap.xml"
    try:
        data = _fetch(url).read().decode("utf-8", "replace")
    except Exception as e:
        util.err(e)
        return 1
    import re
    locs = re.findall(r"<loc>(.*?)</loc>", data)
    for l in locs:
        print("  " + l)
    util.info(f"{len(locs)} URLs")
    return 0


def robots(args):
    """Fetch and show robots.txt."""
    if not args:
        util.err("usage: ntk web robots <url>")
        return 2
    url = args[0].rstrip("/") + "/robots.txt"
    try:
        print(_fetch(url).read().decode("utf-8", "replace"))
    except Exception as e:
        util.err(e)
        return 1
    return 0


def cookie_chk(args):
    """Show cookies and check HttpOnly/Secure flags."""
    if not args:
        util.err("usage: ntk web cookie-chk <url>")
        return 2
    try:
        r = _fetch(args[0])
        cookies = r.headers.get_all("Set-Cookie") or []
    except Exception as e:
        util.err(e)
        return 1
    if not cookies:
        util.info("no cookies set")
        return 0
    for c in cookies:
        name = c.split("=")[0]
        http_only = "HttpOnly" in c
        secure = "Secure" in c
        print(f"  {name}: HttpOnly={col('Y' if http_only else 'N', C.GREEN if http_only else C.RED)}"
              f"  Secure={col('Y' if secure else 'N', C.GREEN if secure else C.RED)}")
    return 0


def ws_client(args):
    """Minimal WebSocket check (best-effort)."""
    if not args:
        util.err("usage: ntk web ws-client <ws-url>")
        return 2
    try:
        import websocket  # type: ignore
    except ImportError:
        util.warn("full WS needs 'websocket-client': pip install websocket-client")
        return 1
    try:
        ws = websocket.create_connection(args[0], timeout=10)
        if len(args) > 1:
            ws.send(args[1])
        util.ok("connected")
        ws.settimeout(3)
        try:
            print("  <- " + ws.recv())
        except Exception:
            pass
        ws.close()
    except Exception as e:
        util.err(e)
        return 1
    return 0


def sse_client(args):
    """Receive Server-Sent Events from an endpoint."""
    if not args:
        util.err("usage: ntk web sse-client <url>")
        return 2
    try:
        r = _fetch(args[0], headers={"Accept": "text/event-stream"}, timeout=60)
        util.info("streaming (Ctrl+C to stop)...")
        for line in r:
            line = line.decode("utf-8", "replace").rstrip()
            if line:
                print("  " + line)
    except KeyboardInterrupt:
        pass
    except Exception as e:
        util.err(e)
        return 1
    return 0


def graphql(args):
    """Run a GraphQL query against an endpoint."""
    if len(args) < 2:
        util.err('usage: ntk web graphql <url> "{ query }"')
        return 2
    body = json.dumps({"query": args[1]}).encode()
    try:
        r = _fetch(args[0], method="POST", headers={"Content-Type": "application/json"}, data=body)
        print(json.dumps(json.loads(r.read()), indent=2))
    except Exception as e:
        util.err(e)
        return 1
    return 0


def dns_propagation(args):
    """Check DNS across public resolvers."""
    if not args:
        util.err("usage: ntk web dns-propagation <domain>")
        return 2
    domain = args[0]
    resolvers = {"Google": "8.8.8.8", "Cloudflare": "1.1.1.1", "Quad9": "9.9.9.9",
                 "OpenDNS": "208.67.222.222"}
    util.header(f"DNS propagation: {domain}")
    if which("nslookup"):
        for name, ip in resolvers.items():
            rc, o, e = run(["nslookup", domain, ip], timeout=10)
            addrs = [l.split()[-1] for l in o.splitlines() if "Address" in l][1:]
            util.kv(name, ", ".join(addrs) or "(no answer)")
    else:
        try:
            util.kv("System resolver", socket.gethostbyname(domain))
        except Exception as e:
            util.err(e)
    return 0


def whois_expiry(args):
    """Check a domain's expiry date."""
    if not args:
        util.err("usage: ntk web whois-expiry <domain>")
        return 2
    if not which("whois"):
        util.warn("whois CLI not found")
        return 1
    rc, o, e = run(["whois", args[0]], timeout=20)
    import re
    m = re.search(r"(Expir\w*|Registry Expiry)[^\n:]*:\s*(.+)", o, re.I)
    if m:
        util.kv("Expiry", m.group(2).strip())
    else:
        util.warn("expiry date not found in whois output")
    return 0


def minify_html(args):
    """Minify HTML (input file or string)."""
    import re
    if not args:
        util.err("usage: ntk web minify-html <file|html>")
        return 2
    import os
    src = open(args[0], encoding="utf-8").read() if os.path.isfile(args[0]) else " ".join(args)
    out = re.sub(r"<!--.*?-->", "", src, flags=re.S)
    out = re.sub(r">\s+<", "><", out)
    out = re.sub(r"\s{2,}", " ", out)
    print(out.strip())
    return 0


def css_unused(args):
    """Find CSS classes not referenced in HTML files."""
    import os
    import re
    if len(args) < 2:
        util.err("usage: ntk web css-unused <style.css> <page.html> [more.html]")
        return 2
    css = open(args[0], encoding="utf-8").read()
    classes = set(re.findall(r"\.([a-zA-Z0-9_-]+)", css))
    used = set()
    for html_file in args[1:]:
        if os.path.isfile(html_file):
            content = open(html_file, encoding="utf-8").read()
            for m in re.findall(r'class=["\']([^"\']+)["\']', content):
                used.update(m.split())
    unused = sorted(classes - used)
    util.header(f"Unused CSS classes ({len(unused)})")
    for c in unused:
        print("  ." + c)
    return 0


def pagespeed(args):
    """Basic page performance metrics."""
    if not args:
        util.err("usage: ntk web pagespeed <url>")
        return 2
    t0 = time.time()
    try:
        r = _fetch(args[0], timeout=30)
        body = r.read()
    except Exception as e:
        util.err(e)
        return 1
    load = (time.time() - t0) * 1000
    util.header("Page metrics")
    util.kv("Load time", f"{load:.0f} ms")
    util.kv("Size", util.human_bytes(len(body)))
    util.kv("Status", r.status)
    util.kv("Server", r.headers.get("Server", "?"))
    return 0


def http2_chk(args):
    """Check if a site supports HTTP/2 (via curl)."""
    if not args:
        util.err("usage: ntk web http2-chk <url>")
        return 2
    if which("curl"):
        rc, o, e = run(["curl", "-sI", "--http2", args[0]])
        if "HTTP/2" in o:
            util.ok("HTTP/2 supported")
        else:
            util.warn("HTTP/2 not detected (HTTP/1.1?)")
        return 0
    util.warn("needs curl for reliable HTTP/2 detection")
    return 1


def cors_test(args):
    """Check if a server allows cross-origin requests."""
    if not args:
        util.err("usage: ntk web cors-test <url>")
        return 2
    try:
        r = _fetch(args[0], headers={"Origin": "https://example.com"})
        acao = r.headers.get("Access-Control-Allow-Origin")
    except Exception as e:
        util.err(e)
        return 1
    if acao == "*":
        util.warn("CORS wide open (Access-Control-Allow-Origin: *)")
    elif acao:
        util.kv("Allowed origin", acao)
    else:
        util.ok("no CORS header (same-origin only)")
    return 0


_UAS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64; rv:123.0) Gecko/20100101 Firefox/123.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 Mobile/15E148 Safari/604.1",
]


def user_agent(args):
    """Print a random User-Agent string."""
    print("  " + random.choice(_UAS))
    return 0


def url_shorten(args):
    """Shorten a URL via is.gd."""
    if not args:
        util.err("usage: ntk web url-shorten <url>")
        return 2
    api = "https://is.gd/create.php?format=simple&url=" + urllib.parse.quote(args[0])
    try:
        print("  " + _fetch(api).read().decode().strip())
    except Exception as e:
        util.err(e)
        return 1
    return 0


def ip_geo(args):
    """Geolocate an IP (country, ISP)."""
    ip = args[0] if args else ""
    try:
        data = json.loads(_fetch(f"http://ip-api.com/json/{ip}").read())
    except Exception as e:
        util.err(e)
        return 1
    if data.get("status") != "success":
        util.err(data.get("message", "lookup failed"))
        return 1
    util.header(f"IP geo: {data.get('query')}")
    for k in ("country", "regionName", "city", "isp", "org", "as", "timezone"):
        if data.get(k):
            util.kv(k, data[k])
    return 0


def mail_dns(args):
    """Validate MX / SPF / DMARC records."""
    if not args:
        util.err("usage: ntk web mail-dns <domain>")
        return 2
    domain = args[0]
    if not which("nslookup"):
        util.warn("needs nslookup/dig")
        return 1
    util.header(f"Mail DNS: {domain}")
    rc, o, _ = run(["nslookup", "-type=MX", domain], timeout=10)
    mx = [l for l in o.splitlines() if "mail exchanger" in l]
    util.kv("MX", "; ".join(m.split("=")[-1].strip() for m in mx) or "none")
    rc, o, _ = run(["nslookup", "-type=TXT", domain], timeout=10)
    spf = [l for l in o.splitlines() if "spf1" in l]
    util.kv("SPF", "yes" if spf else "MISSING")
    rc, o, _ = run(["nslookup", "-type=TXT", "_dmarc." + domain], timeout=10)
    util.kv("DMARC", "yes" if "DMARC1" in o else "MISSING")
    return 0


COMMANDS = {
    "headers": headers, "bench": bench, "broken-links": broken_links,
    "sitemap": sitemap, "robots": robots, "cookie-chk": cookie_chk,
    "ws-client": ws_client, "sse-client": sse_client, "graphql": graphql,
    "dns-propagation": dns_propagation, "whois-expiry": whois_expiry,
    "minify-html": minify_html, "css-unused": css_unused, "pagespeed": pagespeed,
    "http2-chk": http2_chk, "cors-test": cors_test, "user-agent": user_agent,
    "url-shorten": url_shorten, "ip-geo": ip_geo, "mail-dns": mail_dns,
}
