#!/usr/bin/env python3
"""
NTK Updater - pulls the latest release from GitHub and replaces the installed ntk.

- Queries the GitHub Releases API for the newest tag
- Compares it to the locally installed version (ntk --version)
- Downloads the right binary for the platform (ntk.exe on Windows, ntk-linux-x64 on Linux)
- Replaces the installed binary in place (self-elevates on Windows if needed)

Built as a standalone .exe (Windows) and binary (Linux) with PyInstaller.
"""
import os
import sys
import json
import ssl
import tempfile
import shutil
import subprocess
import urllib.request

REPO = "finnytech/ntk-Next-Tool-Kit-terminal-cli"
API_LATEST = f"https://api.github.com/repos/{REPO}/releases/latest"
API_ALL = f"https://api.github.com/repos/{REPO}/releases?per_page=30"
IS_WIN = os.name == "nt"
UA = "ntk-updater/1.0"

# Asset names per platform
ASSET_WIN = "ntk.exe"
ASSET_LINUX = "ntk-linux-x64"


def log(msg):
    print(msg, flush=True)


def http_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA,
                                               "Accept": "application/vnd.github+json"})
    ctx = ssl.create_default_context()
    with urllib.request.urlopen(req, timeout=30, context=ctx) as r:
        return json.loads(r.read().decode("utf-8"))


def get_latest_release():
    """Return the newest release. /releases/latest ignores prereleases, so
    fall back to the full list (which includes prereleases/betas)."""
    try:
        rel = http_json(API_LATEST)
        if rel and rel.get("tag_name"):
            return rel
    except Exception:
        pass
    # Fallback: list all, pick the first non-draft (API returns newest first)
    rels = http_json(API_ALL)
    for r in rels:
        if not r.get("draft"):
            return r
    return rels[0] if rels else None


def download(url, dest):
    req = urllib.request.Request(url, headers={"User-Agent": UA,
                                               "Accept": "application/octet-stream"})
    ctx = ssl.create_default_context()
    with urllib.request.urlopen(req, timeout=120, context=ctx) as r, open(dest, "wb") as f:
        total = int(r.headers.get("Content-Length", 0))
        done = 0
        chunk = 1024 * 64
        while True:
            buf = r.read(chunk)
            if not buf:
                break
            f.write(buf)
            done += len(buf)
            if total:
                pct = done * 100 // total
                bar = "#" * (pct // 4)
                print(f"\r  [{bar:<25}] {pct:3d}%  ({done//1024//1024}/{total//1024//1024} MB)",
                      end="", flush=True)
    print()


def installed_version(ntk_path):
    try:
        out = subprocess.run([ntk_path, "--version"], capture_output=True, text=True, timeout=15)
        # "ntk 1.0.0"
        parts = (out.stdout or out.stderr).strip().split()
        return parts[-1] if parts else None
    except Exception:
        return None


def find_installed_ntk():
    """Locate the currently installed ntk binary."""
    name = "ntk.exe" if IS_WIN else "ntk"
    # 1) PATH
    p = shutil.which(name) or shutil.which("ntk")
    if p and os.path.basename(p).lower() != os.path.basename(sys.argv[0]).lower():
        return p
    # 2) Default install dir (Windows)
    if IS_WIN:
        cand = os.path.join(os.environ.get("ProgramFiles", r"C:\Program Files"), "NTK", "ntk.exe")
        if os.path.exists(cand):
            return cand
    else:
        for cand in ("/usr/local/bin/ntk", "/usr/bin/ntk", os.path.expanduser("~/.local/bin/ntk")):
            if os.path.exists(cand):
                return cand
    return None


def is_admin_win():
    try:
        import ctypes
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except Exception:
        return False


def elevate_win():
    import ctypes
    params = " ".join(f'"{a}"' for a in sys.argv[1:])
    rc = ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, params, None, 1)
    return rc > 32


def replace_binary(target, new_file):
    """Replace target with new_file. On Windows a running/locked exe is renamed aside first."""
    if IS_WIN:
        # Can't overwrite a file that's in use; move the old one aside, then copy new in.
        old_bak = target + ".old"
        try:
            if os.path.exists(old_bak):
                os.remove(old_bak)
        except Exception:
            pass
        try:
            if os.path.exists(target):
                os.replace(target, old_bak)  # rename current out of the way
        except Exception:
            pass
        shutil.copy2(new_file, target)
        try:
            if os.path.exists(old_bak):
                os.remove(old_bak)
        except Exception:
            pass  # leftover .old is harmless; PATH still resolves to the new exe
    else:
        shutil.copy2(new_file, target)
        os.chmod(target, 0o755)


def main():
    print("=" * 52)
    print("   NTK Updater  |  pulls the latest release from GitHub")
    print("=" * 52)
    print()

    target = find_installed_ntk()
    if not target:
        log("[!] Could not find an installed 'ntk'. Install it first (run the installer).")
        if IS_WIN:
            input("Press Enter to exit...")
        return 1
    log(f"[*] Installed ntk: {target}")

    cur = installed_version(target)
    log(f"[*] Current version: {cur or 'unknown'}")

    log("[*] Checking GitHub for the latest release...")
    try:
        rel = get_latest_release()
        if not rel:
            raise RuntimeError("no releases found")
    except Exception as e:
        log(f"[!] Could not reach GitHub: {e}")
        if IS_WIN:
            input("Press Enter to exit...")
        return 1

    latest = (rel.get("tag_name") or "").lstrip("v")
    log(f"[*] Latest release: {latest or '?'}  ({rel.get('name','')})")

    force = "--force" in sys.argv or "-f" in sys.argv
    if cur and latest and cur == latest and not force:
        log("[=] You already have the latest version. Nothing to do.")
        log("    (use --force to re-download and reinstall anyway)")
        if IS_WIN:
            input("Press Enter to exit...")
        return 0

    want = ASSET_WIN if IS_WIN else ASSET_LINUX
    asset = next((a for a in rel.get("assets", []) if a.get("name") == want), None)
    if not asset:
        log(f"[!] Release has no asset named '{want}'.")
        if IS_WIN:
            input("Press Enter to exit...")
        return 1

    # On Windows, replacing a file in Program Files needs admin.
    if IS_WIN and not is_admin_win():
        instdir = os.path.dirname(target).lower()
        if "program files" in instdir:
            log("[i] Administrator rights required to update in Program Files - elevating...")
            if elevate_win():
                return 0
            log("[!] Could not elevate. Right-click -> Run as administrator.")
            input("Press Enter to exit...")
            return 1

    tmp = tempfile.mkdtemp(prefix="ntk_upd_")
    dl = os.path.join(tmp, want)
    log(f"[*] Downloading {want} ({asset.get('size',0)//1024//1024} MB)...")
    try:
        download(asset["browser_download_url"], dl)
    except Exception as e:
        log(f"[!] Download failed: {e}")
        if IS_WIN:
            input("Press Enter to exit...")
        return 1

    log("[*] Replacing installed binary...")
    try:
        replace_binary(target, dl)
    except PermissionError as e:
        log(f"[!] Permission denied: {e}")
        log("    Try running the updater as administrator.")
        if IS_WIN:
            input("Press Enter to exit...")
        return 1
    except Exception as e:
        log(f"[!] Replace failed: {e}")
        if IS_WIN:
            input("Press Enter to exit...")
        return 1
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    new = installed_version(target)
    print()
    print("-" * 52)
    log(f"[+] NTK updated successfully -> version {new or latest}")
    log("    Open a new terminal and run:  ntk --version")
    print("-" * 52)
    if IS_WIN:
        input("Press Enter to finish...")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\nCancelled.")
        sys.exit(130)
