"""Search tools."""
import os, re, hashlib, time
from . import util


def _files(path='.'):
    out=[]
    for root, dirs, files in os.walk(path):
        dirs[:] = [d for d in dirs if d not in {'.git','node_modules','__pycache__'}]
        if len(out)>100000: break
        for name in files:
            p=os.path.join(root,name)
            try:
                if os.path.isfile(p): out.append(p)
            except OSError: pass
    return out

def _args(args, n=1):
    if len(args)<n: raise ValueError('arguments')
    return args

def _read(p):
    with open(p,'r',encoding='utf-8',errors='replace') as f: return f.read()

def _print(paths):
    for p in paths: print(p)

def files(a):
    try:
        pat=' '.join(a[:-1]) if len(a)>1 else '*'; path=a[-1] if a else '.'
        import fnmatch; _print([p for p in _files(path) if fnmatch.fnmatch(os.path.basename(p),pat)]); return 0
    except Exception: util.err('usage: files <pattern> [path]'); return 2

def text(a): return _grep(a, False)
def regex(a): return _grep(a, True)
def _grep(a, rx):
    try:
        if len(a)<2: raise ValueError()
        pat=a[0]; path=a[1]; rg=re.compile(pat) if rx else None
        for p in _files(path):
            try:
                for i,line in enumerate(_read(p).splitlines(),1):
                    if (rg.search(line) if rg else pat.lower() in line.lower()): print(f'{p}:{i}:{line}')
            except (OSError,UnicodeError): pass
        return 0
    except Exception: util.err('usage: grep <word/pattern> <path>'); return 2

def name(a):
    try: _print([p for p in _files(a[1] if len(a)>1 else '.') if a[0].lower() in os.path.basename(p).lower()]); return 0
    except Exception: util.err('usage: name <substring> [path]'); return 2

def ext(a):
    try: _print([p for p in _files(a[1] if len(a)>1 else '.') if os.path.splitext(p)[1].lower()==('.'+a[0].lstrip('.').lower())]); return 0
    except Exception: util.err('usage: ext <extension> [path]'); return 2

def _size(a, bigger):
    try:
        mb=float(a[0]); ps=_files(a[1] if len(a)>1 else '.'); _print([p for p in ps if (os.path.getsize(p)/1048576 >= mb)==bigger]); return 0
    except Exception: util.err('usage: size <MB> [path]'); return 2

def bigger(a): return _size(a,True)
def smaller(a): return _size(a,False)
def _age(a, older):
    try:
        d=float(a[0]); cutoff=time.time()-d*86400; _print([p for p in _files(a[1] if len(a)>1 else '.') if (os.path.getmtime(p)<cutoff)==older]); return 0
    except Exception: util.err('usage: age <days> [path]'); return 2

def newer(a): return _age(a,False)
def older(a): return _age(a,True)
def empty(a):
    try: _print([p for p in _files(a[0] if a else '.') if os.path.getsize(p)==0]); return 0
    except Exception: util.err('usage: empty-files [path]'); return 2
def content(a): return text(a)
def count(a):
    try:
        w,path=a[0],a[1]; print(sum(_read(p).lower().count(w.lower()) for p in _files(path))); return 0
    except Exception: util.err('usage: count-matches <word> <path>'); return 2
def replace_preview(a):
    try:
        old,new,path=a[0],a[1],a[2]
        for p in _files(path):
            s=_read(p); n=s.count(old)
            if n: print(f'{p}: {n} replacements')
        return 0
    except Exception: util.err('usage: replace-preview <old> <new> <path>'); return 2
def dupes(a):
    try:
        d={}
        for p in _files(a[0] if a else '.'):
            k=(os.path.getsize(p),hashlib.sha256(open(p,'rb').read()).hexdigest()); d.setdefault(k,[]).append(p)
        for v in d.values():
            if len(v)>1: print('\n'.join(v)); print()
        return 0
    except Exception: util.err('usage: dupes [path]'); return 2
def by_date(a):
    try: _print([p for p in _files(a[1] if len(a)>1 else '.') if time.strftime('%Y-%m-%d',time.localtime(os.path.getmtime(p)))==a[0]]); return 0
    except Exception: util.err('usage: by-date <YYYY-MM-DD> [path]'); return 2
def hidden(a):
    try: _print([p for p in _files(a[0] if a else '.') if os.path.basename(p).startswith('.')]); return 0
    except Exception: return 2
def executable(a):
    try: _print([p for p in _files(a[0] if a else '.') if os.access(p,os.X_OK)]); return 0
    except Exception: return 2
def symlinks(a):
    try: _print([os.path.join(r,n) for r,ds,fs in os.walk(a[0] if a else '.') for n in ds+fs if os.path.islink(os.path.join(r,n))]); return 0
    except Exception: return 2
def broken(a):
    try: _print([p for p in [os.path.join(r,n) for r,ds,fs in os.walk(a[0] if a else '.') for n in ds+fs if os.path.islink(os.path.join(r,n))] if not os.path.exists(p)]); return 0
    except Exception: return 2
def largest(a): return _rank(a,True)
def recent(a): return _rank(a,False)
def _rank(a, size):
    try:
        n=int(a[0]); ps=_files(a[1] if len(a)>1 else '.'); ps.sort(key=os.path.getsize if size else os.path.getmtime, reverse=True); _print(ps[:n]); return 0
    except Exception: util.err('usage: largest/recent <n> [path]'); return 2
def in_file(a): return _grep([a[0],a[1]],False)
def lines_with(a): return _grep([a[0],a[1]],False)
def file_type(a): return ext(a)
def grep_recursive(a): return text(a)
def match_any(a):
    try:
        words=a[0].split(','); path=a[1]
        for p in _files(path):
            for i,l in enumerate(_read(p).splitlines(),1):
                if any(w.lower() in l.lower() for w in words): print(f'{p}:{i}:{l}')
        return 0
    except Exception: util.err('usage: match-any <words,csv> <path>'); return 2
def fuzzy_name(a): return name(a)
def first_match(a):
    try:
        for p in _files(a[1]):
            for i,l in enumerate(_read(p).splitlines(),1):
                if a[0].lower() in l.lower(): print(f'{p}:{i}:{l}'); return 0
        return 0
    except Exception: return 2
def nth_line(a):
    try: print(_read(a[1]).splitlines()[int(a[0])-1]); return 0
    except Exception: util.err('usage: nth-line <n> <file>'); return 2
def find_dir(a):
    try:
        for r,ds,_ in os.walk(a[1] if len(a)>1 else '.'): _print([os.path.join(r,d) for d in ds if a[0].lower() in d.lower()])
        return 0
    except Exception: return 2

COMMANDS={'files':files,'text':text,'regex':regex,'name':name,'ext':ext,'bigger-than':bigger,'smaller-than':smaller,'newer-than':newer,'older-than':older,'empty-files':empty,'content':content,'count-matches':count,'replace-preview':replace_preview,'dupes':dupes,'by-date':by_date,'hidden':hidden,'executable':executable,'symlinks':symlinks,'broken-symlinks':broken,'largest':largest,'recent':recent,'in-file':in_file,'lines-with':lines_with,'file-type':file_type,'grep-recursive':grep_recursive,'match-any':match_any,'fuzzy-name':fuzzy_name,'first-match':first_match,'nth-line':nth_line,'find-dir':find_dir}
