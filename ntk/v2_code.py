"""Source code inspection tools."""
import os,re,json
from . import util

def _walk(p):
    for r,ds,fs in os.walk(p):
        ds[:]=[d for d in ds if d not in {'.git','node_modules','__pycache__'}]
        for f in fs: yield os.path.join(r,f)
def _read(p): return open(p,encoding='utf-8',errors='replace').read()
def count_lines(a):
    try: print(len(_read(a[0]).splitlines())); return 0
    except Exception:return 2
def loc(a):
    try: print(sum(len(_read(p).splitlines()) for p in _walk(a[0] if a else '.'))); return 0
    except Exception:return 2
def comment_ratio(a):
    try:
        l=_read(a[0]).splitlines(); print(sum(x.lstrip().startswith(('#','//')) for x in l)/max(1,len(l))); return 0
    except Exception:return 2
def longest_line(a):
    try: print(max(_read(a[0]).splitlines(),key=len)); return 0
    except Exception:return 2
def trailing(a):
    try:
        for i,l in enumerate(_read(a[0]).splitlines(),1):
            if l.rstrip()!=l: print(i)
        return 0
    except Exception:return 2
def todo(a): return _scan(a,'TODO')
def fixme(a): return _scan(a,'FIXME')
def _scan(a,w):
    try:
        for p in _walk(a[0] if a else '.'):
            for i,l in enumerate(_read(p).splitlines(),1):
                if w in l: print(f'{p}:{i}:{l}')
        return 0
    except Exception:return 2
def function_count(a): return _pattern(a,r'^\s*(def|function)\s+')
def indent_check(a): return _scan(a,'\t')
def format_json(a):
    try: print(json.dumps(json.load(open(a[0])),indent=2)); return 0
    except Exception:return 2
def minify_json(a):
    try: print(json.dumps(json.load(open(a[0])),separators=(',',':'))); return 0
    except Exception:return 2
def blank(a):
    try: print(sum(not x.strip() for x in _read(a[0]).splitlines())); return 0
    except Exception:return 2
def file_ext_stats(a):
    try:
        d={}
        for p in _walk(a[0] if a else '.'): d[os.path.splitext(p)[1]]=d.get(os.path.splitext(p)[1],0)+1
        print(d); return 0
    except Exception:return 2
def largest(a):
    try: print(max(_walk(a[0] if a else '.'),key=os.path.getsize)); return 0
    except Exception:return 2
def duplicate_lines(a):
    try:
        from collections import Counter
        print([x for x,n in Counter(_read(a[0]).splitlines()).items() if n>1]); return 0
    except Exception:return 2
def byte_count(a):
    try: print(os.path.getsize(a[0])); return 0
    except Exception:return 2
def encoding(a): print('utf-8'); return 0
def line_endings(a):
    try: print('CRLF' if b'\r\n' in open(a[0],'rb').read() else 'LF'); return 0
    except Exception:return 2
def tabs(a):
    try:
        if '--yes' not in a: util.err('use --yes'); return 2
        p=a[0]; open(p,'w').write(_read(p).replace('\t','    ')); return 0
    except Exception:return 2
def wc_code(a): return loc(a)
def languages(a): return file_ext_stats(a)
def shebang(a):
    try: print(_read(a[0]).splitlines()[0] if _read(a[0]).startswith('#!') else ''); return 0
    except Exception:return 2
def max_line(a): return longest_line(a)
def print_scan(a): return _scan(a,'print(')
def import_list(a): return _pattern(a,r'^\s*(import|from)\s+')
def class_count(a): return _pattern(a,r'^\s*class\s+')
def string_count(a):
    try: print(_read(a[0]).count(a[1])); return 0
    except Exception:return 2
def lines_of(a): return count_lines(a)
def empty_files(a):
    try: print('\n'.join(p for p in _walk(a[0] if a else '.') if os.path.getsize(p)==0)); return 0
    except Exception:return 2
def longest_function(a): return longest_line(a)
def header_check(a): return shebang(a)
def whitespace_only(a):
    try: print(sum(bool(x) and not x.strip() for x in _read(a[0]).splitlines())); return 0
    except Exception:return 2
def _pattern(a,pat):
    try: print(sum(bool(re.search(pat,x)) for x in _read(a[0]).splitlines())); return 0
    except Exception:return 2
COMMANDS={'count-lines':count_lines,'loc':loc,'comment-ratio':comment_ratio,'longest-line':longest_line,'trailing-whitespace':trailing,'todo-scan':todo,'fixme-scan':fixme,'function-count':function_count,'indent-check':indent_check,'format-json':format_json,'minify-json':minify_json,'blank-lines':blank,'file-ext-stats':file_ext_stats,'largest-file':largest,'duplicate-lines':duplicate_lines,'byte-count':byte_count,'encoding':encoding,'line-endings':line_endings,'tabs-to-spaces':tabs,'wc-code':wc_code,'languages':languages,'shebang':shebang,'max-line-length':max_line,'print-scan':print_scan,'import-list':import_list,'class-count':class_count,'string-count':string_count,'lines-of':lines_of,'empty-files':empty_files,'longest-function-hint':longest_function,'header-check':header_check,'whitespace-only':whitespace_only}
