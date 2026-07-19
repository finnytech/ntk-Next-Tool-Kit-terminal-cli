"""Developer productivity tools (ntk dev ...)."""
import ast, datetime, hashlib, http.server, json, math as _math, os, random, re, secrets, socket, subprocess, time as _time, urllib.parse, urllib.request
from pathlib import Path
from . import util
from .util import col, C, run, IS_WINDOWS

def git_clean(args):
    """Show untracked files and build artifacts."""
    rc,out,err=run(['git','status','--short','--untracked-files=all']); print(out or err); return rc

def git_stats(args):
    """Show git history statistics."""
    rc,out,err=run(['git','log','--oneline','--stat','-n',str(args[0] if args and args[0].isdigit() else 10)]); print(out or err); return rc

def time_cmd(args):
    """Measure a command's runtime."""
    if not args: util.err('usage: ntk dev time <command> [args]'); return 2
    start=_time.perf_counter(); rc,out,err=run(args); elapsed=_time.perf_counter()-start; print(out,end=''); print(err,end=''); util.kv('Exit',rc); util.kv('Elapsed',f'{elapsed:.3f}s'); return rc

def color(args):
    """Convert HEX, RGB and HSL colors."""
    if not args: util.err('usage: ntk dev color <#rgb|r,g,b|h,s%,l%>'); return 2
    s=args[0].strip().lower()
    try:
        if s.startswith('#'):
            h=s[1:]; h=''.join(c*2 for c in h) if len(h)==3 else h; r,g,b=[int(h[i:i+2],16) for i in (0,2,4)]; hsl=_rgb_hsl(r,g,b); util.kv('RGB',f'{r},{g},{b}'); util.kv('HSL',f'{hsl[0]:.1f},{hsl[1]:.1f}%,{hsl[2]:.1f}%'); print('#%02x%02x%02x'%(r,g,b))
        elif ',' in s:
            vals=[float(x.strip().rstrip('%')) for x in s.split(',')];
            if max(vals)>100: r,g,b=map(int,vals); print('#%02x%02x%02x'%(r,g,b)); util.kv('HSL',str(_rgb_hsl(r,g,b)))
            else:
                h,sl,l=vals; r,g,b=_hsl_rgb(h,sl,l); print('#%02x%02x%02x'%(r,g,b)); util.kv('RGB',f'{r},{g},{b}')
        else: raise ValueError
        return 0
    except (ValueError,IndexError): util.err('invalid color'); return 2

def _rgb_hsl(r,g,b):
    import colorsys; h,l,s=colorsys.rgb_to_hls(r/255,g/255,b/255); return h*360,s*100,l*100
def _hsl_rgb(h,s,l):
    import colorsys; r,g,b=colorsys.hls_to_rgb((h%360)/360,l/100,s/100); return round(r*255),round(g*255),round(b*255)

def lorem(args):
    """Generate lorem ipsum text."""
    n=int(args[0]) if args and args[0].isdigit() else 3; words='lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua'.split(); out=[]
    for _ in range(n): out.append(' '.join(random.choice(words) for _ in range(12)).capitalize()+'.')
    print(' '.join(out)); return 0

def mock_user(args):
    """Generate a fake user record."""
    first=random.choice('Alex Sam Jordan Taylor Casey Morgan Riley Jamie'.split()); last=random.choice('Smith Lee Brown Davis Wilson'.split()); print(json.dumps({'name':f'{first} {last}','email':f'{first.lower()}.{last.lower()}@example.test','id':secrets.token_hex(4)},indent=2)); return 0

def mock_db(args):
    """Generate fake JSON database records."""
    n=int(args[0]) if args and args[0].isdigit() else 5; print(json.dumps([{'id':i,'name':f'User {i}','active':bool(random.getrandbits(1))} for i in range(1,n+1)],indent=2)); return 0

def port_scan(args):
    """Scan TCP ports on a host."""
    if not args: util.err('usage: ntk dev port-scan <host> [start-end]'); return 2
    host=args[0]; spec=args[1] if len(args)>1 else '1-1024'; a,b=(map(int,spec.split('-',1)) if '-' in spec else (int(spec),int(spec))); rows=[]
    for p in range(a,min(b,65535)+1):
        s=socket.socket(); s.settimeout(.05)
        try:
            if s.connect_ex((host,p))==0: rows.append((p,'open'))
        finally: s.close()
    util.table(rows,headers=['Port','State']); return 0

def _serve(args, api=False):
    """Serve a directory or JSON file over HTTP."""
    port=int(args[1]) if len(args)>1 else 8000; root=args[0] if args else os.getcwd()
    if api:
        data=json.load(open(root,encoding='utf-8'))
        class H(http.server.BaseHTTPRequestHandler):
            def do_GET(self): self.send_response(200); self.send_header('Content-Type','application/json'); self.end_headers(); self.wfile.write(json.dumps(data).encode())
            def log_message(self,*x): pass
        server=http.server.HTTPServer(('',port),H)
    else: os.chdir(root); server=http.server.ThreadingHTTPServer(('',port),http.server.SimpleHTTPRequestHandler)
    util.info(f'http://127.0.0.1:{port} (Ctrl+C to stop)')
    try: server.serve_forever()
    except KeyboardInterrupt: pass
    return 0

def api_serve(args): """Serve a JSON file as an API."""; return _serve(args,True)
def static_serve(args): """Serve static files over HTTP."""; return _serve(args)
def markdown_pdf(args):
    """Convert Markdown to PDF when supported."""
    if len(args)<1: util.err('usage: ntk dev markdown-pdf <file> [output]'); return 2
    try: import markdown; from weasyprint import HTML
    except ImportError: util.warn('needs markdown and weasyprint: pip install markdown weasyprint'); return 1
    out=args[1] if len(args)>1 else str(Path(args[0]).with_suffix('.pdf')); HTML(string=markdown.markdown(Path(args[0]).read_text())).write_pdf(out); print(out); return 0

def readme_gen(args): """Generate a README template."""; Path(args[0] if args else 'README.md').write_text('# Project\n\n## Installation\n\n## Usage\n'); return 0
def license_gen(args):
    """Generate a short open-source license."""
    kind=args[0].lower() if args else 'mit'; year=str(datetime.date.today().year); name=args[1] if len(args)>1 else 'Copyright holder'; templates={'mit':f'MIT License\n\nCopyright (c) {year} {name}\n\nPermission is hereby granted, free of charge, to any person obtaining a copy of this software...','apache-2.0':'Apache License 2.0\n\nLicensed under the Apache License, Version 2.0.','gpl-3.0':'GNU GENERAL PUBLIC LICENSE\nVersion 3, 29 June 2007'}; print(templates.get(kind,templates['mit'])); return 0

def gitignore_gen(args):
    """Fetch or print a language gitignore."""
    if not args: util.err('usage: ntk dev gitignore-gen <language>'); return 2
    lang=args[0].lower(); fallback={'python':'__pycache__/\n*.pyc\n.venv/\n','node':'node_modules/\n.env\n','java':'target/\n*.class\n'}
    try: text=urllib.request.urlopen(f'https://www.toptal.com/developers/gitignore/api/{urllib.parse.quote(lang)}',timeout=5).read().decode()
    except Exception: text=fallback.get(lang,'# Add project-specific ignores here\n')
    print(text); return 0

def semver(args):
    """Parse, compare or bump semantic versions."""
    if not args: util.err('usage: ntk dev semver <version> [bump]'); return 2
    m=re.match(r'v?(\d+)\.(\d+)\.(\d+)',args[0]);
    if not m: util.err('invalid semver'); return 2
    v=list(map(int,m.groups()));
    if len(args)>1:
        i={'major':0,'minor':1,'patch':2}.get(args[1]);
        if i is None: util.err('bump must be major, minor or patch'); return 2
        v[i]+=1
        for j in range(i+1,3): v[j]=0
    print('.'.join(map(str,v))); return 0

def cron_parse(args):
    """Explain a five-field cron expression."""
    if len(args)!=1 or len(args[0].split())!=5: util.err('usage: ntk dev cron-parse "m h dom mon dow"'); return 2
    names=['minute','hour','day of month','month','day of week']; util.table(list(zip(names,args[0].split())),headers=['Field','Value']); return 0

def changelog(args):
    """Create a changelog entry from git commits."""; rc,out,err=run(['git','log','--pretty=format:- %s','-n','20']); print('# Changelog\n\n'+out); return rc
def todo(args):
    """Scan source files for TODO and FIXME."""
    root=Path(args[0]) if args else Path('.'); rows=[]
    for p in root.rglob('*'):
        if p.is_file() and p.suffix not in {'.pyc','.png','.jpg','.gif'}:
            try:
                for i,line in enumerate(p.read_text(errors='ignore').splitlines(),1):
                    if re.search(r'\b(TODO|FIXME)\b',line): rows.append((str(p),i,line.strip()))
            except OSError: pass
    util.table(rows,headers=['File','Line','Text']); return 0
def dependency_check(args):
    """Check Python imports listed in requirements."""
    fn=args[0] if args else 'requirements.txt'; missing=[]
    try: lines=Path(fn).read_text().splitlines()
    except OSError as e: util.err(str(e)); return 1
    for x in lines:
        name=re.split(r'[<>=!~]',x.strip())[0].strip()
        if name and not name.startswith('#'):
            try: __import__(name.replace('-','_'))
            except ImportError: missing.append(name)
    print('missing: '+(', '.join(missing) if missing else 'none')); return 1 if missing else 0

def _pil(args, convert=False):
    try: from PIL import Image
    except ImportError: util.warn('needs Pillow: pip install Pillow'); return 1
    if len(args)<2: util.err('usage: ntk dev image-resize <in> <out> [width height]'); return 2
    try:
        im=Image.open(args[0]);
        if not convert: im=im.resize((int(args[2]),int(args[3])) if len(args)>3 else (int(im.width/2),int(im.height/2)))
        im.save(args[1]); print(args[1]); return 0
    except Exception as e: util.err(str(e)); return 1
def image_resize(args): """Resize an image with Pillow."""; return _pil(args)
def image_convert(args): """Convert an image format with Pillow."""; return _pil(args,True)
def svg_minify(args): """Minify an SVG file."""; return _minify(args,True)
def minify(args): """Naively minify text or JSON whitespace."""; return _minify(args)
def _minify(args,svg=False):
    if not args: util.err('usage: ntk dev minify <file> [output]'); return 2
    try: s=Path(args[0]).read_text(); s=re.sub(r'<!--.*?-->','',s,flags=re.S); s=re.sub(r'>\s+<','><',s); s=re.sub(r'\s+',' ',s).strip(); out=args[1] if len(args)>1 else args[0]+'.min'; Path(out).write_text(s); print(out); return 0
    except OSError as e: util.err(str(e)); return 1
def timestamp(args): """Print a Unix timestamp or convert one."""; print(datetime.datetime.fromtimestamp(float(args[0])) if args else int(_time.time())); return 0
def math(args):
    """Safely evaluate arithmetic."""
    if not args: util.err('usage: ntk dev math <expression>'); return 2
    try: print(_safe_eval(' '.join(args))); return 0
    except Exception as e: util.err(str(e)); return 1
def _safe_eval(s):
    tree=ast.parse(s,mode='eval'); allowed=(ast.Expression,ast.Constant,ast.BinOp,ast.UnaryOp,ast.Add,ast.Sub,ast.Mult,ast.Div,ast.FloorDiv,ast.Mod,ast.Pow,ast.USub,ast.UAdd)
    if any(not isinstance(n,allowed) for n in ast.walk(tree)): raise ValueError('only arithmetic is allowed')
    return eval(compile(tree,'<math>','eval'),{'__builtins__':{}},{})

COMMANDS={'git-clean':git_clean,'git-stats':git_stats,'time':time_cmd,'color':color,'lorem':lorem,'mock-user':mock_user,'mock-db':mock_db,'port-scan':port_scan,'api-serve':api_serve,'static-serve':static_serve,'markdown-pdf':markdown_pdf,'readme-gen':readme_gen,'license-gen':license_gen,'gitignore-gen':gitignore_gen,'semver':semver,'cron-parse':cron_parse,'changelog':changelog,'todo':todo,'dependency-check':dependency_check,'image-resize':image_resize,'image-convert':image_convert,'svg-minify':svg_minify,'timestamp':timestamp,'math':math,'minify':minify}
