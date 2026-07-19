#!/usr/bin/env python3
"""
NTK Manager - lightweight local web UI.

Starts a localhost HTTP server and opens the default browser. The UI lets you:
  - browse all 1000+ tools by category
  - search across every command + description
  - read each command's help / usage
  - copy any command to the clipboard (one click)
  - update NTK (runs ntk-updater)
  - uninstall NTK (runs ntk-uninstall / ntk uninstall)

No heavy GUI toolkit - just the Python stdlib http.server + a single HTML page.
Packaged as a standalone .exe with PyInstaller. The command catalog is pulled
live from the installed `ntk` binary (via `ntk --json-commands`); if that isn't
on PATH we fall back to a catalog bundled at build time.
"""
import json
import os
import sys
import shutil
import socket
import threading
import subprocess
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

VERSION = "2.0.0"
IS_WINDOWS = os.name == "nt"


# ---------------------------------------------------------------- catalog ----
def _find_ntk():
    name = "ntk.exe" if IS_WINDOWS else "ntk"
    exe = shutil.which("ntk") or shutil.which(name)
    if exe:
        return exe
    # look next to this manager (install dir)
    here = os.path.dirname(os.path.abspath(
        sys.executable if getattr(sys, "frozen", False) else __file__))
    cand = os.path.join(here, name)
    return cand if os.path.exists(cand) else None


def _bundled_catalog():
    """Catalog packaged with the manager at build time (fallback)."""
    base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    for p in (os.path.join(base, "catalog.json"),
              os.path.join(os.path.dirname(os.path.abspath(__file__)), "catalog.json")):
        try:
            with open(p, encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            continue
    return {}


def load_catalog():
    exe = _find_ntk()
    if exe:
        try:
            out = subprocess.check_output([exe, "--json-commands"],
                                          stderr=subprocess.DEVNULL, timeout=30)
            data = json.loads(out.decode("utf-8", "replace"))
            if data:
                return data
        except Exception:
            pass
    return _bundled_catalog()


def tool_help(cat, tool):
    exe = _find_ntk()
    if not exe:
        return "(ntk not found on this system)"
    try:
        out = subprocess.run([exe, cat, tool, "-h"],
                             capture_output=True, timeout=20)
        txt = (out.stdout or b"").decode("utf-8", "replace")
        txt += (out.stderr or b"").decode("utf-8", "replace")
        # strip ANSI colour codes
        import re
        txt = re.sub(r"\x1b\[[0-9;]*m", "", txt)
        return txt.strip() or "(no help text)"
    except Exception as e:
        return f"(could not fetch help: {e})"


def run_updater():
    exe = _find_ntk()
    if exe:
        try:
            subprocess.Popen([exe, "update"])
            return "Update started - watch the new console window."
        except Exception as e:
            return f"Could not start update: {e}"
    return "ntk not found."


def run_uninstall():
    # Prefer the standalone uninstaller (own console, can self-elevate).
    name = "ntk-uninstall.exe" if IS_WINDOWS else "ntk-uninstall"
    here = os.path.dirname(os.path.abspath(
        sys.executable if getattr(sys, "frozen", False) else __file__))
    cand = shutil.which("ntk-uninstall") or os.path.join(here, name)
    try:
        if os.path.exists(cand):
            subprocess.Popen([cand])
            return "Uninstaller launched in a new window."
        exe = _find_ntk()
        if exe:
            subprocess.Popen([exe, "uninstall"])
            return "Uninstall started via 'ntk uninstall'."
    except Exception as e:
        return f"Could not start uninstaller: {e}"
    return "No uninstaller found."


# ------------------------------------------------------------------- page ----
PAGE = r"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>NTK Manager</title>
<style>
:root{--bg:#0d1117;--panel:#161b22;--border:#30363d;--fg:#e6edf3;
--muted:#8b949e;--accent:#58a6ff;--accent2:#3fb950;--chip:#21262d;}
*{box-sizing:border-box}
body{margin:0;font:14px/1.5 -apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;
background:var(--bg);color:var(--fg)}
header{display:flex;align-items:center;gap:14px;padding:14px 20px;
border-bottom:1px solid var(--border);background:var(--panel);position:sticky;top:0;z-index:5}
.logo{font-weight:800;font-size:20px;letter-spacing:1px;color:var(--accent)}
.tag{color:var(--muted);font-size:12px}
.spacer{flex:1}
button{background:var(--chip);color:var(--fg);border:1px solid var(--border);
border-radius:7px;padding:7px 12px;cursor:pointer;font-size:13px}
button:hover{border-color:var(--accent)}
button.primary{background:var(--accent);color:#0d1117;border-color:var(--accent);font-weight:600}
button.danger:hover{border-color:#f85149;color:#f85149}
.wrap{display:flex;height:calc(100vh - 59px)}
.side{width:240px;border-right:1px solid var(--border);overflow:auto;padding:10px;background:var(--panel)}
.cat{padding:7px 10px;border-radius:6px;cursor:pointer;color:var(--muted);
display:flex;justify-content:space-between;gap:8px}
.cat:hover{background:var(--chip);color:var(--fg)}
.cat.active{background:var(--chip);color:var(--accent);font-weight:600}
.cat .n{font-size:11px;color:var(--muted)}
.main{flex:1;overflow:auto;padding:18px 22px}
.search{width:100%;padding:11px 13px;border-radius:9px;border:1px solid var(--border);
background:var(--panel);color:var(--fg);font-size:14px;margin-bottom:16px}
.search:focus{outline:none;border-color:var(--accent)}
.tool{border:1px solid var(--border);border-radius:10px;padding:12px 14px;margin-bottom:10px;background:var(--panel)}
.tool h3{margin:0 0 4px;font-size:15px}
.tool .cmd{font-family:ui-monospace,Consolas,monospace;color:var(--accent2);font-size:13px}
.tool .desc{color:var(--muted);margin:5px 0 8px}
.tool .row{display:flex;gap:8px;flex-wrap:wrap}
.badge{font-size:11px;color:var(--muted);background:var(--chip);border:1px solid var(--border);
border-radius:20px;padding:2px 9px}
.help{white-space:pre-wrap;font-family:ui-monospace,Consolas,monospace;font-size:12px;
background:#0b0f14;border:1px solid var(--border);border-radius:8px;padding:10px;margin-top:8px;display:none}
.toast{position:fixed;bottom:20px;left:50%;transform:translateX(-50%);
background:var(--accent2);color:#04140a;padding:10px 18px;border-radius:8px;
font-weight:600;opacity:0;transition:.25s;pointer-events:none}
.toast.show{opacity:1}
.count{color:var(--muted);font-size:12px;margin-bottom:8px}
</style></head><body>
<header>
  <span class="logo">NTK</span><span class="tag">Manager v__VER__ &middot; 1000+ tools, one CLI</span>
  <span class="spacer"></span>
  <button class="primary" onclick="doUpdate()">&#8635; Update NTK</button>
  <button class="danger" onclick="doUninstall()">&#128465; Uninstall</button>
</header>
<div class="wrap">
  <div class="side" id="side"></div>
  <div class="main">
    <input class="search" id="q" placeholder="Search 1000+ commands...  (e.g. 'free ram', 'password', 'ping')" oninput="render()">
    <div class="count" id="count"></div>
    <div id="list"></div>
  </div>
</div>
<div class="toast" id="toast"></div>
<script>
let CAT={}, active="ALL";
function copy(t){navigator.clipboard.writeText(t).then(()=>toast("Copied: "+t));}
function toast(m){let e=document.getElementById('toast');e.textContent=m;e.classList.add('show');
  clearTimeout(window._tt);window._tt=setTimeout(()=>e.classList.remove('show'),1400);}
function doUpdate(){fetch('/action/update',{method:'POST'}).then(r=>r.text()).then(toast);}
function doUninstall(){if(confirm('Uninstall NTK from this computer?'))
  fetch('/action/uninstall',{method:'POST'}).then(r=>r.text()).then(toast);}
function help(cat,tool,el){
  let box=el.parentElement.parentElement.querySelector('.help');
  if(box.style.display==='block'){box.style.display='none';return;}
  box.textContent='loading...';box.style.display='block';
  fetch('/help?cat='+cat+'&tool='+encodeURIComponent(tool)).then(r=>r.text()).then(t=>box.textContent=t);
}
function sidebar(){
  let s=document.getElementById('side');let tot=0;
  for(const c in CAT)tot+=Object.keys(CAT[c].tools).length;
  let h='<div class="cat '+(active==='ALL'?'active':'')+'" onclick="pick(\'ALL\')">'
    +'<span>All</span><span class="n">'+tot+'</span></div>';
  for(const c of Object.keys(CAT).sort()){
    h+='<div class="cat '+(active===c?'active':'')+'" onclick="pick(\''+c+'\')">'
      +'<span>'+c+'</span><span class="n">'+Object.keys(CAT[c].tools).length+'</span></div>';}
  s.innerHTML=h;
}
function pick(c){active=c;sidebar();render();}
function render(){
  let q=document.getElementById('q').value.toLowerCase().trim();
  let list=document.getElementById('list');let rows=[];let n=0;
  for(const c of Object.keys(CAT).sort()){
    if(active!=='ALL'&&active!==c)continue;
    for(const t of Object.keys(CAT[c].tools).sort()){
      let d=CAT[c].tools[t]||'';
      let hay=(c+' '+t+' '+d).toLowerCase();
      if(q&&!q.split(/\s+/).every(w=>hay.includes(w)))continue;
      n++;
      let full='ntk '+c+' '+t, hy='ntk-'+c+'-'+t;
      rows.push('<div class="tool"><h3>'+t+' <span class="badge">'+c+'</span></h3>'
        +'<div class="cmd">'+full+'</div>'
        +(d?'<div class="desc">'+esc(d)+'</div>':'')
        +'<div class="row">'
        +'<button onclick="copy(\''+full.replace(/'/g,"\\'")+'\')">Copy</button>'
        +'<button onclick="copy(\''+hy.replace(/'/g,"\\'")+'\')">Copy '+hy+'</button>'
        +'<button onclick="help(\''+c+'\',\''+t.replace(/'/g,"\\'")+'\',this)">Help</button>'
        +'</div><div class="help"></div></div>');
    }
  }
  document.getElementById('count').textContent=n+' command'+(n===1?'':'s');
  list.innerHTML=rows.join('')||'<p style="color:var(--muted)">No matches.</p>';
}
function esc(s){return s.replace(/[&<>]/g,m=>({'&':'&amp;','<':'&lt;','>':'&gt;'}[m]));}
fetch('/catalog').then(r=>r.json()).then(d=>{CAT=d;sidebar();render();});
</script></body></html>"""


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def _send(self, code, body, ctype="text/html; charset=utf-8"):
        if isinstance(body, str):
            body = body.encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        try:
            self.wfile.write(body)
        except Exception:
            pass

    def do_GET(self):
        from urllib.parse import urlparse, parse_qs
        u = urlparse(self.path)
        if u.path in ("/", "/index.html"):
            return self._send(200, PAGE.replace("__VER__", VERSION))
        if u.path == "/catalog":
            return self._send(200, json.dumps(load_catalog()),
                              "application/json; charset=utf-8")
        if u.path == "/help":
            q = parse_qs(u.query)
            cat = (q.get("cat") or [""])[0]
            tool = (q.get("tool") or [""])[0]
            return self._send(200, tool_help(cat, tool),
                              "text/plain; charset=utf-8")
        return self._send(404, "not found", "text/plain")

    def do_POST(self):
        if self.path == "/action/update":
            return self._send(200, run_updater(), "text/plain")
        if self.path == "/action/uninstall":
            return self._send(200, run_uninstall(), "text/plain")
        return self._send(404, "not found", "text/plain")


def _free_port():
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    p = s.getsockname()[1]
    s.close()
    return p


def main():
    port = _free_port()
    httpd = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    url = f"http://127.0.0.1:{port}/"
    print("=" * 52)
    print(f"   NTK Manager v{VERSION}")
    print("=" * 52)
    print(f"[+] Serving UI at {url}")
    print("[i] Close this window (or Ctrl+C) to stop the manager.")
    threading.Timer(0.6, lambda: webbrowser.open(url)).start()
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[i] Stopping.")
    finally:
        httpd.shutdown()
    return 0


if __name__ == "__main__":
    sys.exit(main())
