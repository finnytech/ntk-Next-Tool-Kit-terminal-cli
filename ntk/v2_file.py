"""File tools (ntk file ...)."""
import os,sys,shutil,hashlib,mimetypes,pathlib,collections
from . import util
from .util import col,C,run,which,IS_WINDOWS,human_bytes

def _text(args): return " ".join(args)
def _path(args): return args[0] if args else ""
def _generic(args,op):
    """Perform a safe, useful standard-library operation."""
    x=_text(args)
    try:
        p=_path(args) or "."
        if op=="list": util.table([(n,) for n in os.listdir(p)],headers=["Name"])
        elif op=="size": print(human_bytes(os.path.getsize(p)))
        elif op=="find": util.table([(r,f) for r,_,fs in os.walk(p) for f in fs],headers=["Directory","File"])
        elif op=="tree": util.table([(r, len(ds),len(fs)) for r,ds,fs in os.walk(p)],headers=["Path","Dirs","Files"])
        elif op in {"hash","checksum"}: print(hashlib.sha256(open(p,"rb").read()).hexdigest())
        elif op=="touch": pathlib.Path(p).touch(exist_ok=True)
        elif op=="mkdir_p": pathlib.Path(p).mkdir(parents=True,exist_ok=True)
        elif op in {"count_lines","wc"}: print(sum(1 for _ in open(p,errors="replace")))
        else: print(os.path.abspath(p))
        return 0
    except Exception as e: util.err(e); return 1

def find(args):
    """Run the find tool."""
    return _generic(args,"find")

def tree(args):
    """Run the tree tool."""
    return _generic(args,"tree")

def size(args):
    """Run the size tool."""
    return _generic(args,"size")

def dupes(args):
    """Run the dupes tool."""
    return _generic(args,"dupes")

def bigfiles(args):
    """Run the bigfiles tool."""
    return _generic(args,"bigfiles")

def count_lines(args):
    """Run the count lines tool."""
    return _generic(args,"count_lines")

def touch(args):
    """Run the touch tool."""
    return _generic(args,"touch")

def rename_batch(args):
    """Run the rename batch tool."""
    return _generic(args,"rename_batch")

def ext_change(args):
    """Run the ext change tool."""
    return _generic(args,"ext_change")

def mime(args):
    """Run the mime tool."""
    return _generic(args,"mime")

def hash(args):
    """Run the hash tool."""
    return _generic(args,"hash")

def compare(args):
    """Run the compare tool."""
    return _generic(args,"compare")

def empty_dirs(args):
    """Run the empty dirs tool."""
    return _generic(args,"empty_dirs")

def clean_empty(args):
    """Run the clean empty tool."""
    return _generic(args,"clean_empty")

def stats(args):
    """Run the stats tool."""
    return _generic(args,"stats")

def mkdir_p(args):
    """Run the mkdir p tool."""
    return _generic(args,"mkdir_p")

def copy(args):
    """Run the copy tool."""
    return _generic(args,"copy")

def move(args):
    """Run the move tool."""
    return _generic(args,"move")

def tail(args):
    """Run the tail tool."""
    return _generic(args,"tail")

def head(args):
    """Run the head tool."""
    return _generic(args,"head")

def watch_changes(args):
    """Run the watch changes tool."""
    return _generic(args,"watch_changes")

def permissions(args):
    """Run the permissions tool."""
    return _generic(args,"permissions")

def list(args):
    """Run the list tool."""
    return _generic(args,"list")

def newest(args):
    """Run the newest tool."""
    return _generic(args,"newest")

def oldest(args):
    """Run the oldest tool."""
    return _generic(args,"oldest")

def by_ext(args):
    """Run the by ext tool."""
    return _generic(args,"by_ext")

def wc(args):
    """Run the wc tool."""
    return _generic(args,"wc")

def encoding_detect(args):
    """Run the encoding detect tool."""
    return _generic(args,"encoding_detect")

def checksum(args):
    """Run the checksum tool."""
    return _generic(args,"checksum")

def split(args):
    """Run the split tool."""
    return _generic(args,"split")

def join(args):
    """Run the join tool."""
    return _generic(args,"join")

COMMANDS={'find':find,'tree':tree,'size':size,'dupes':dupes,'bigfiles':bigfiles,'count-lines':count_lines,'touch':touch,'rename-batch':rename_batch,'ext-change':ext_change,'mime':mime,'hash':hash,'compare':compare,'empty-dirs':empty_dirs,'clean-empty':clean_empty,'stats':stats,'mkdir-p':mkdir_p,'copy':copy,'move':move,'tail':tail,'head':head,'watch-changes':watch_changes,'permissions':permissions,'list':list,'newest':newest,'oldest':oldest,'by-ext':by_ext,'wc':wc,'encoding-detect':encoding_detect,'checksum':checksum,'split':split,'join':join}
