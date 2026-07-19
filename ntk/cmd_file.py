"""File management tools (ntk file ...)."""
import os, shutil, hashlib, zipfile, tarfile, gzip, mimetypes, pathlib, filecmp, tempfile, time, difflib, fnmatch, stat
from . import util
from .util import run, IS_WINDOWS

def _path(args, usage):
    if not args: util.err("usage: "+usage); return None
    return os.path.expanduser(args[0])
def find(args):
    root=_path(args,"ntk file find <dir> [pattern] [grep]");
    if not root:return 2
    pat=args[1] if len(args)>1 else "*"; q=args[2] if len(args)>2 else None
    for d,_,fs in os.walk(root):
        for f in fs:
            if fnmatch.fnmatch(f,pat):
                p=os.path.join(d,f)
                if not q or q in open(p,errors="ignore").read(): print(p)
    return 0
def size(args):
    root=_path(args,"ntk file size <path>");
    if not root:return 2
    rows=[]
    for d,ds,fs in os.walk(root):
        total=0
        for f in fs:
            try: total+=os.path.getsize(os.path.join(d,f))
            except OSError: pass
        rows.append((total,d))
    if os.path.isfile(root): rows=[(os.path.getsize(root),root)]
    util.table([(util.human_bytes(s),p) for s,p in sorted(rows,reverse=True)[:20]],headers=["Size","Path"]); return 0
def tree(args):
    root=_path(args,"ntk file tree <dir> [depth]");
    if not root:return 2
    depth=int(args[1]) if len(args)>1 else 3
    def walk(p,lev):
        if lev>depth:return
        try: ents=sorted(os.scandir(p),key=lambda x:(not x.is_dir(),x.name.lower()))
        except OSError:return
        for e in ents:
            print("  "*lev+"└─ "+e.name)
            if e.is_dir():walk(e.path,lev+1)
    print(root); walk(root,1); return 0
def rename(args):
    if len(args)<2: util.err("usage: ntk file rename <source> <dest>"); return 2
    os.rename(os.path.expanduser(args[0]),os.path.expanduser(args[1])); util.ok("renamed"); return 0
def duplicates(args):
    root=_path(args,"ntk file duplicates <dir>");
    if not root:return 2
    groups={}
    for d,_,fs in os.walk(root):
        for f in fs:
            p=os.path.join(d,f)
            try:
                h=hashlib.md5(open(p,"rb").read()).hexdigest(); groups.setdefault((os.path.getsize(p),h),[]).append(p)
            except OSError: pass
    for ps in groups.values():
        if len(ps)>1: print("\n".join(ps)+"\n")
    return 0
def shred(args):
    p=_path(args,"ntk file shred <file> [passes]");
    if not p:return 2
    passes=int(args[1]) if len(args)>1 else 3
    try:
        n=os.path.getsize(p)
        with open(p,"r+b") as f:
            for i in range(passes): f.seek(0); f.write(os.urandom(n)); f.flush(); os.fsync(f.fileno())
        os.remove(p); util.ok("shredded"); return 0
    except OSError as e: util.err(str(e)); return 1
def compress(args):
    src=_path(args,"ntk file compress <source> [archive]");
    if not src:return 2
    out=args[1] if len(args)>1 else src.rstrip(os.sep)+".zip"
    with zipfile.ZipFile(out,"w",zipfile.ZIP_DEFLATED) as z:
        if os.path.isdir(src):
            for d,_,fs in os.walk(src):
                for f in fs:z.write(os.path.join(d,f),os.path.relpath(os.path.join(d,f),os.path.dirname(src)))
        else:z.write(src,os.path.basename(src))
    util.ok(out); return 0
def decompress(args):
    p=_path(args,"ntk file decompress <archive> [dest]");
    if not p:return 2
    dest=args[1] if len(args)>1 else os.path.splitext(p)[0]; os.makedirs(dest,exist_ok=True)
    try:
        if zipfile.is_zipfile(p): zipfile.ZipFile(p).extractall(dest)
        elif tarfile.is_tarfile(p): tarfile.open(p).extractall(dest)
        else: util.err("unsupported archive"); return 2
        util.ok(dest); return 0
    except Exception as e: util.err(str(e)); return 1
def mime(args):
    p=_path(args,"ntk file mime <file>");
    if not p:return 2
    util.kv("Type",mimetypes.guess_type(p)[0] or "application/octet-stream"); util.kv("Size",util.human_bytes(os.path.getsize(p))); return 0
def stats(args):
    p=_path(args,"ntk file stats <file>");
    if not p:return 2
    st=os.stat(p); util.kv("Size",util.human_bytes(st.st_size)); util.kv("Mode",oct(st.st_mode)); util.kv("Modified",time.ctime(st.st_mtime)); return 0
def chmod(args):
    if len(args)<2: util.err("usage: ntk file chmod <mode> <path>"); return 2
    os.chmod(args[1],int(args[0],8)); return 0
def chown(args):
    if len(args)<2: util.err("usage: ntk file chown <user> <path>"); return 2
    if IS_WINDOWS or not hasattr(os,"chown"): util.warn("chown unavailable on this platform"); return 1
    import pwd
    os.chown(args[1],pwd.getpwnam(args[0]).pw_uid,-1); return 0
def symlink(args):
    if len(args)<2: util.err("usage: ntk file symlink <target> <link>"); return 2
    os.symlink(args[0],args[1]); return 0
def empty(args):
    p=_path(args,"ntk file empty <file>");
    if not p:return 2
    open(p,"w").close(); return 0
def lines(args):
    p=_path(args,"ntk file lines <file>");
    if not p:return 2
    with open(p,errors="replace") as f: util.kv("Lines",sum(1 for _ in f)); return 0
def compare(args):
    if len(args)<2: util.err("usage: ntk file compare <a> <b>"); return 2
    a,b=args[:2]; same=filecmp.cmp(a,b,shallow=False); util.kv("Equal",same); return 0 if same else 1
def tail_f(args):
    p=_path(args,"ntk file tail-f <file> [lines]");
    if not p:return 2
    n=int(args[1]) if len(args)>1 else 10
    with open(p,errors="replace") as f:
        f.seek(0,2); print("".join(f.readlines()[-n:]),end="")
    return 0
def touch(args):
    p=_path(args,"ntk file touch <file>");
    if not p:return 2
    pathlib.Path(p).touch(); return 0
def temp_dir(args):
    p=tempfile.mkdtemp(prefix="ntk-"); print(p); return 0
def clean_temp(args):
    root=tempfile.gettempdir(); count=0
    for p in pathlib.Path(root).glob("ntk-*"):
        try: shutil.rmtree(p) if p.is_dir() else p.unlink(); count+=1
        except OSError: pass
    util.ok(f"removed {count}"); return 0
def sync(args):
    if len(args)<2: util.err("usage: ntk file sync <source> <dest>"); return 2
    src,dst=map(os.path.expanduser,args[:2]); os.makedirs(dst,exist_ok=True)
    for d,_,fs in os.walk(src):
        rel=os.path.relpath(d,src); out=os.path.join(dst,"" if rel=="." else rel); os.makedirs(out,exist_ok=True)
        for f in fs:
            a=os.path.join(d,f); b=os.path.join(out,f)
            if not os.path.exists(b) or os.path.getmtime(a)>os.path.getmtime(b): shutil.copy2(a,b)
    return 0
def disk_health(args):
    if not util.which("smartctl"): util.warn("smartctl not found"); return 1
    dev=_path(args,"ntk file disk-health <device>");
    if not dev:return 2
    rc,o,e=run(["smartctl","-H",dev]); print(o or e); return rc
COMMANDS={"find":find,"size":size,"tree":tree,"rename":rename,"duplicates":duplicates,"shred":shred,"compress":compress,"decompress":decompress,"mime":mime,"stats":stats,"chmod":chmod,"chown":chown,"symlink":symlink,"empty":empty,"lines":lines,"compare":compare,"tail-f":tail_f,"touch":touch,"temp-dir":temp_dir,"clean-temp":clean_temp,"sync":sync,"disk-health":disk_health}
