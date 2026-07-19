"""Text and format tools (ntk text ...)."""
import sys, os, json, csv, base64, binascii, urllib.parse, re, difflib, html, io, unicodedata
from xml.dom import minidom
from html.parser import HTMLParser
from . import util

def _read(args):
    if not args:return sys.stdin.read()
    p=os.path.expanduser(args[0])
    if os.path.isfile(p):
        with open(p,encoding="utf-8",errors="replace") as f:return f.read()
    return " ".join(args)
def _json(args, compact=False):
    try: print(json.dumps(json.loads(_read(args)),ensure_ascii=False,separators=(",",":") if compact else None,indent=None if compact else 2)); return 0
    except Exception as e: util.err(str(e)); return 1
def json_format(args): return _json(args)
def json_minify(args): return _json(args,True)
def xml_format(args):
    try: print(minidom.parseString(_read(args)).toprettyxml(indent="  ").strip()); return 0
    except Exception as e: util.err(str(e)); return 1
def csv_to_json(args):
    try: print(json.dumps(list(csv.DictReader(io.StringIO(_read(args)))),ensure_ascii=False,indent=2)); return 0
    except Exception as e: util.err(str(e)); return 1
def json_to_csv(args):
    try:
        rows=json.loads(_read(args)); fields=sorted({k for r in rows for k in r}); out=io.StringIO(); w=csv.DictWriter(out,fieldnames=fields); w.writeheader(); w.writerows(rows); print(out.getvalue(),end=""); return 0
    except Exception as e: util.err(str(e)); return 1
def base64_enc(args): print(base64.b64encode(_read(args).encode()).decode()); return 0
def base64_dec(args):
    try: print(base64.b64decode(_read(args)).decode(errors="replace")); return 0
    except Exception as e: util.err(str(e)); return 1
def hex_dump(args):
    b=_read(args).encode();
    for i in range(0,len(b),16): print(f"{i:08x}  "+" ".join(f"{x:02x}" for x in b[i:i+16]));
    return 0
def url_enc(args): print(urllib.parse.quote(_read(args))); return 0
def url_dec(args): print(urllib.parse.unquote(_read(args))); return 0
def md_preview(args):
    s=_read(args)
    for line in s.splitlines():
        line=re.sub(r"^#{1,6}\s*", "",line); line=re.sub(r"\[([^]]+)\]\([^)]*\)",r"\1",line); print(re.sub(r"[*_`]", "",line))
    return 0
def regex(args):
    if len(args)<2: util.err("usage: ntk text regex <pattern> <text>"); return 2
    try:
        for m in re.finditer(args[0]," ".join(args[1:])): print(m.group(0))
        return 0
    except re.error as e: util.err(str(e)); return 1
def diff(args):
    if len(args)<2: util.err("usage: ntk text diff <a> <b>"); return 2
    a=_read([args[0]]); b=_read([args[1]]); print("".join(difflib.unified_diff(a.splitlines(True),b.splitlines(True),fromfile=args[0],tofile=args[1])),end=""); return 0
def grep(args):
    if not args: util.err("usage: ntk text grep <pattern> [file]"); return 2
    p=args[0]; s=_read(args[1:])
    try:
        for i,l in enumerate(s.splitlines(),1):
            if re.search(p,l): print(f"{i}:{l}")
        return 0
    except re.error as e: util.err(str(e)); return 1
def wc(args):
    s=_read(args); print(f"{len(s.split()):7} {len(s.splitlines()):7} {len(s):7}"); return 0
def replace(args):
    if len(args)<3: util.err("usage: ntk text replace <old> <new> <text|file>"); return 2
    print(_read(args[2:]).replace(args[0],args[1]),end=""); return 0
def sort_text(args): print("\n".join(sorted(_read(args).splitlines()))); return 0
def unique(args):
    seen=set()
    for l in _read(args).splitlines():
        if l not in seen: print(l); seen.add(l)
    return 0
def upper(args): print(_read(args).upper(),end=""); return 0
def lower(args): print(_read(args).lower(),end=""); return 0
def slugify(args):
    s=unicodedata.normalize("NFKD",_read(args)).encode("ascii","ignore").decode().lower(); print(re.sub(r"-+","-",re.sub(r"[^a-z0-9]+","-",s)).strip("-")); return 0
def titlecase(args): print(_read(args).title(),end=""); return 0
class _Strip(HTMLParser):
    def __init__(self):super().__init__();self.out=[]
    def handle_data(self,d):self.out.append(d)
def strip_html(args):
    p=_Strip(); p.feed(_read(args)); print("".join(p.out),end=""); return 0
def yaml_to_json(args):
    try:
        import yaml
    except ImportError: util.warn("needs yaml: pip install pyyaml"); return 1
    try: print(json.dumps(yaml.safe_load(_read(args)),ensure_ascii=False,indent=2)); return 0
    except Exception as e: util.err(str(e)); return 1
def json_to_yaml(args):
    try: import yaml
    except ImportError: util.warn("needs yaml: pip install pyyaml"); return 1
    try: print(yaml.safe_dump(json.loads(_read(args)),sort_keys=False,allow_unicode=True),end=""); return 0
    except Exception as e: util.err(str(e)); return 1
def html_format(args):
    s=_read(args); s=re.sub(r">\s*<", ">\n<", s); print(s); return 0
MORSE={**dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..".split())),**dict(zip("0123456789","----- .---- ..--- ...-- ....- ..... -.... --... ---.. ----.".split()))}
def morse(args):
    s=_read(args).strip(); inv={v:k for k,v in MORSE.items()}
    if set(s)<=set(".- /") and (" " in s or "/" in s): print(" ".join("".join(inv.get(x,"?") for x in w.split()) for w in s.split("/")))
    else: print(" ".join(MORSE.get(c,"/") for c in s.upper()))
    return 0
def binary(args):
    s=_read(args).strip()
    try:
        if re.fullmatch(r"[01 ]+",s) and any(len(x)==8 for x in s.split()): print(bytes(int(x,2) for x in s.split()).decode(errors="replace"))
        else: print(" ".join(f"{b:08b}" for b in s.encode()))
        return 0
    except Exception as e: util.err(str(e)); return 1
COMMANDS={"json-format":json_format,"json-minify":json_minify,"xml-format":xml_format,"csv-to-json":csv_to_json,"json-to-csv":json_to_csv,"base64-enc":base64_enc,"base64-dec":base64_dec,"hex-dump":hex_dump,"url-enc":url_enc,"url-dec":url_dec,"md-preview":md_preview,"regex":regex,"diff":diff,"grep":grep,"wc":wc,"replace":replace,"sort":sort_text,"unique":unique,"upper":upper,"lower":lower,"slugify":slugify,"titlecase":titlecase,"strip-html":strip_html,"yaml-to-json":yaml_to_json,"json-to-yaml":json_to_yaml,"html-format":html_format,"morse":morse,"binary":binary}
