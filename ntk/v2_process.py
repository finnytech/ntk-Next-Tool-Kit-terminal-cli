"""NTK v2 process tools."""
import os
import time
from . import util

def list(args):
    """list tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("list:", value)
        else:
            print("list: available")
        return 0
    except Exception:
        util.err("usage: ntk process list [value]")
        return 2

def list_by_cpu(args):
    """list-by-cpu tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("list-by-cpu:", value)
        else:
            print("list-by-cpu: available")
        return 0
    except Exception:
        util.err("usage: ntk process list-by-cpu [value]")
        return 2

def list_by_mem(args):
    """list-by-mem tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("list-by-mem:", value)
        else:
            print("list-by-mem: available")
        return 0
    except Exception:
        util.err("usage: ntk process list-by-mem [value]")
        return 2

def find(args):
    """find tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("find:", value)
        else:
            print("find: available")
        return 0
    except Exception:
        util.err("usage: ntk process find [value]")
        return 2

def kill(args):
    """kill tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("kill:", value)
        else:
            print("kill: available")
        return 0
    except Exception:
        util.err("usage: ntk process kill [value]")
        return 2

def kill_name(args):
    """kill-name tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("kill-name:", value)
        else:
            print("kill-name: available")
        return 0
    except Exception:
        util.err("usage: ntk process kill-name [value]")
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
        util.err("usage: ntk process tree [value]")
        return 2

def info(args):
    """info tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("info:", value)
        else:
            print("info: available")
        return 0
    except Exception:
        util.err("usage: ntk process info [value]")
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
        util.err("usage: ntk process count [value]")
        return 2

def threads(args):
    """threads tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("threads:", value)
        else:
            print("threads: available")
        return 0
    except Exception:
        util.err("usage: ntk process threads [value]")
        return 2

def open_files(args):
    """open-files tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("open-files:", value)
        else:
            print("open-files: available")
        return 0
    except Exception:
        util.err("usage: ntk process open-files [value]")
        return 2

def connections(args):
    """connections tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("connections:", value)
        else:
            print("connections: available")
        return 0
    except Exception:
        util.err("usage: ntk process connections [value]")
        return 2

def children(args):
    """children tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("children:", value)
        else:
            print("children: available")
        return 0
    except Exception:
        util.err("usage: ntk process children [value]")
        return 2

def parent(args):
    """parent tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("parent:", value)
        else:
            print("parent: available")
        return 0
    except Exception:
        util.err("usage: ntk process parent [value]")
        return 2

def priority(args):
    """priority tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("priority:", value)
        else:
            print("priority: available")
        return 0
    except Exception:
        util.err("usage: ntk process priority [value]")
        return 2

def set_priority(args):
    """set-priority tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("set-priority:", value)
        else:
            print("set-priority: available")
        return 0
    except Exception:
        util.err("usage: ntk process set-priority [value]")
        return 2

def kill_port(args):
    """kill-port tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("kill-port:", value)
        else:
            print("kill-port: available")
        return 0
    except Exception:
        util.err("usage: ntk process kill-port [value]")
        return 2

def port_owner(args):
    """port-owner tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("port-owner:", value)
        else:
            print("port-owner: available")
        return 0
    except Exception:
        util.err("usage: ntk process port-owner [value]")
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
        util.err("usage: ntk process oldest [value]")
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
        util.err("usage: ntk process newest [value]")
        return 2

def top(args):
    """top tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("top:", value)
        else:
            print("top: available")
        return 0
    except Exception:
        util.err("usage: ntk process top [value]")
        return 2

def cpu_of(args):
    """cpu-of tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("cpu-of:", value)
        else:
            print("cpu-of: available")
        return 0
    except Exception:
        util.err("usage: ntk process cpu-of [value]")
        return 2

def mem_of(args):
    """mem-of tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("mem-of:", value)
        else:
            print("mem-of: available")
        return 0
    except Exception:
        util.err("usage: ntk process mem-of [value]")
        return 2

def cmdline(args):
    """cmdline tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("cmdline:", value)
        else:
            print("cmdline: available")
        return 0
    except Exception:
        util.err("usage: ntk process cmdline [value]")
        return 2

def cwd_of(args):
    """cwd-of tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("cwd-of:", value)
        else:
            print("cwd-of: available")
        return 0
    except Exception:
        util.err("usage: ntk process cwd-of [value]")
        return 2

def status(args):
    """status tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("status:", value)
        else:
            print("status: available")
        return 0
    except Exception:
        util.err("usage: ntk process status [value]")
        return 2

def suspend(args):
    """suspend tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("suspend:", value)
        else:
            print("suspend: available")
        return 0
    except Exception:
        util.err("usage: ntk process suspend [value]")
        return 2

def resume(args):
    """resume tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("resume:", value)
        else:
            print("resume: available")
        return 0
    except Exception:
        util.err("usage: ntk process resume [value]")
        return 2

def running_count(args):
    """running-count tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("running-count:", value)
        else:
            print("running-count: available")
        return 0
    except Exception:
        util.err("usage: ntk process running-count [value]")
        return 2

def user_processes(args):
    """user-processes tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("user-processes:", value)
        else:
            print("user-processes: available")
        return 0
    except Exception:
        util.err("usage: ntk process user-processes [value]")
        return 2

def exe_of(args):
    """exe-of tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("exe-of:", value)
        else:
            print("exe-of: available")
        return 0
    except Exception:
        util.err("usage: ntk process exe-of [value]")
        return 2

def create_time(args):
    """create-time tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("create-time:", value)
        else:
            print("create-time: available")
        return 0
    except Exception:
        util.err("usage: ntk process create-time [value]")
        return 2

COMMANDS = {
    'list': list,
    'list-by-cpu': list_by_cpu,
    'list-by-mem': list_by_mem,
    'find': find,
    'kill': kill,
    'kill-name': kill_name,
    'tree': tree,
    'info': info,
    'count': count,
    'threads': threads,
    'open-files': open_files,
    'connections': connections,
    'children': children,
    'parent': parent,
    'priority': priority,
    'set-priority': set_priority,
    'kill-port': kill_port,
    'port-owner': port_owner,
    'oldest': oldest,
    'newest': newest,
    'top': top,
    'cpu-of': cpu_of,
    'mem-of': mem_of,
    'cmdline': cmdline,
    'cwd-of': cwd_of,
    'status': status,
    'suspend': suspend,
    'resume': resume,
    'running-count': running_count,
    'user-processes': user_processes,
    'exe-of': exe_of,
    'create-time': create_time,
}
