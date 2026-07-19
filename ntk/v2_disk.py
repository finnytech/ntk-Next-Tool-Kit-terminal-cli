"""NTK v2 disk tools."""
import os
import time
from . import util

def usage(args):
    """usage tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("usage:", value)
        else:
            print("usage: available")
        return 0
    except Exception:
        util.err("usage: ntk disk usage [value]")
        return 2

def tree(args):
    """tree tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("tree:", value)
        else:
            print("tree: available")
        return 0
    except Exception:
        util.err("usage: ntk disk tree [value]")
        return 2

def bigfiles(args):
    """bigfiles tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("bigfiles:", value)
        else:
            print("bigfiles: available")
        return 0
    except Exception:
        util.err("usage: ntk disk bigfiles [value]")
        return 2

def dupes(args):
    """dupes tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("dupes:", value)
        else:
            print("dupes: available")
        return 0
    except Exception:
        util.err("usage: ntk disk dupes [value]")
        return 2

def by_ext(args):
    """by-ext tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("by-ext:", value)
        else:
            print("by-ext: available")
        return 0
    except Exception:
        util.err("usage: ntk disk by-ext [value]")
        return 2

def empty_dirs(args):
    """empty-dirs tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("empty-dirs:", value)
        else:
            print("empty-dirs: available")
        return 0
    except Exception:
        util.err("usage: ntk disk empty-dirs [value]")
        return 2

def oldest(args):
    """oldest tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("oldest:", value)
        else:
            print("oldest: available")
        return 0
    except Exception:
        util.err("usage: ntk disk oldest [value]")
        return 2

def newest(args):
    """newest tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("newest:", value)
        else:
            print("newest: available")
        return 0
    except Exception:
        util.err("usage: ntk disk newest [value]")
        return 2

def count(args):
    """count tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("count:", value)
        else:
            print("count: available")
        return 0
    except Exception:
        util.err("usage: ntk disk count [value]")
        return 2

def du(args):
    """du tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("du:", value)
        else:
            print("du: available")
        return 0
    except Exception:
        util.err("usage: ntk disk du [value]")
        return 2

def free(args):
    """free tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("free:", value)
        else:
            print("free: available")
        return 0
    except Exception:
        util.err("usage: ntk disk free [value]")
        return 2

def partitions(args):
    """partitions tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("partitions:", value)
        else:
            print("partitions: available")
        return 0
    except Exception:
        util.err("usage: ntk disk partitions [value]")
        return 2

def mounts(args):
    """mounts tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("mounts:", value)
        else:
            print("mounts: available")
        return 0
    except Exception:
        util.err("usage: ntk disk mounts [value]")
        return 2

def largest_dir(args):
    """largest-dir tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("largest-dir:", value)
        else:
            print("largest-dir: available")
        return 0
    except Exception:
        util.err("usage: ntk disk largest-dir [value]")
        return 2

def file_types(args):
    """file-types tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("file-types:", value)
        else:
            print("file-types: available")
        return 0
    except Exception:
        util.err("usage: ntk disk file-types [value]")
        return 2

def size(args):
    """size tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("size:", value)
        else:
            print("size: available")
        return 0
    except Exception:
        util.err("usage: ntk disk size [value]")
        return 2

def find_large(args):
    """find-large tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("find-large:", value)
        else:
            print("find-large: available")
        return 0
    except Exception:
        util.err("usage: ntk disk find-large [value]")
        return 2

def find_old(args):
    """find-old tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("find-old:", value)
        else:
            print("find-old: available")
        return 0
    except Exception:
        util.err("usage: ntk disk find-old [value]")
        return 2

def extensions_stats(args):
    """extensions-stats tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("extensions-stats:", value)
        else:
            print("extensions-stats: available")
        return 0
    except Exception:
        util.err("usage: ntk disk extensions-stats [value]")
        return 2

def hidden_files(args):
    """hidden-files tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("hidden-files:", value)
        else:
            print("hidden-files: available")
        return 0
    except Exception:
        util.err("usage: ntk disk hidden-files [value]")
        return 2

def symlinks(args):
    """symlinks tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("symlinks:", value)
        else:
            print("symlinks: available")
        return 0
    except Exception:
        util.err("usage: ntk disk symlinks [value]")
        return 2

def zero_byte(args):
    """zero-byte tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("zero-byte:", value)
        else:
            print("zero-byte: available")
        return 0
    except Exception:
        util.err("usage: ntk disk zero-byte [value]")
        return 2

def readonly_files(args):
    """readonly-files tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("readonly-files:", value)
        else:
            print("readonly-files: available")
        return 0
    except Exception:
        util.err("usage: ntk disk readonly-files [value]")
        return 2

def permissions_summary(args):
    """permissions-summary tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("permissions-summary:", value)
        else:
            print("permissions-summary: available")
        return 0
    except Exception:
        util.err("usage: ntk disk permissions-summary [value]")
        return 2

def space_by_folder(args):
    """space-by-folder tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("space-by-folder:", value)
        else:
            print("space-by-folder: available")
        return 0
    except Exception:
        util.err("usage: ntk disk space-by-folder [value]")
        return 2

def recent_files(args):
    """recent-files tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("recent-files:", value)
        else:
            print("recent-files: available")
        return 0
    except Exception:
        util.err("usage: ntk disk recent-files [value]")
        return 2

def scan(args):
    """scan tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("scan:", value)
        else:
            print("scan: available")
        return 0
    except Exception:
        util.err("usage: ntk disk scan [value]")
        return 2

def depth(args):
    """depth tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("depth:", value)
        else:
            print("depth: available")
        return 0
    except Exception:
        util.err("usage: ntk disk depth [value]")
        return 2

def total_files(args):
    """total-files tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("total-files:", value)
        else:
            print("total-files: available")
        return 0
    except Exception:
        util.err("usage: ntk disk total-files [value]")
        return 2

def total_size(args):
    """total-size tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("total-size:", value)
        else:
            print("total-size: available")
        return 0
    except Exception:
        util.err("usage: ntk disk total-size [value]")
        return 2

COMMANDS = {
    'usage': usage,
    'tree': tree,
    'bigfiles': bigfiles,
    'dupes': dupes,
    'by-ext': by_ext,
    'empty-dirs': empty_dirs,
    'oldest': oldest,
    'newest': newest,
    'count': count,
    'du': du,
    'free': free,
    'partitions': partitions,
    'mounts': mounts,
    'largest-dir': largest_dir,
    'file-types': file_types,
    'size': size,
    'find-large': find_large,
    'find-old': find_old,
    'extensions-stats': extensions_stats,
    'hidden-files': hidden_files,
    'symlinks': symlinks,
    'zero-byte': zero_byte,
    'readonly-files': readonly_files,
    'permissions-summary': permissions_summary,
    'space-by-folder': space_by_folder,
    'recent-files': recent_files,
    'scan': scan,
    'depth': depth,
    'total-files': total_files,
    'total-size': total_size,
}
