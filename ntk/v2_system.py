"""System tools (ntk system ...)."""
import os, sys, platform, time, locale, getpass, datetime, pathlib
from . import util
from .util import col, C, run, which, IS_WINDOWS, human_bytes

def _show(k,v): util.kv(k,v); return 0
def os_info(args):
    """Show operating system information."""
    util.header("OS"); [util.kv(k,v) for k,v in (("System",platform.system()),("Release",platform.release()),("Version",platform.version()),("Machine",platform.machine()),("Processor",platform.processor()))]; return 0
def hostname(args): """Show host name."""; return _show("Hostname",platform.node())
def users(args):
    """List logged-in users."""
    if which("who"): rc,o,e=run(["who"]); print(o,end="" if o.endswith("\n") else "\n"); return rc
    return _show("User",getpass.getuser())
def whoami(args): """Show current user."""; return _show("User",getpass.getuser())
def env_vars(args): """Show environment variables."""; [util.kv(k,os.environ[k]) for k in sorted(os.environ)]; return 0
def uptime(args):
    """Show system uptime."""
    if not IS_WINDOWS:
        try: return _show("Uptime",str(datetime.timedelta(seconds=int(time.time()-float(open('/proc/uptime').read().split()[0])))))
        except OSError: pass
    if which("wmic"): rc,o,e=run(["wmic","os","get","LastBootUpTime"]); print(o); return rc
    return 1
def boot_time(args):
    """Show approximate boot time."""
    if not IS_WINDOWS:
        try: return _show("Boot",datetime.datetime.fromtimestamp(time.time()-float(open('/proc/uptime').read().split()[0])).isoformat())
        except OSError: pass
    util.warn("boot time unavailable"); return 1
def kernel(args): """Show kernel release."""; return _show("Kernel",platform.release())
def arch(args): """Show machine architecture."""; return _show("Architecture",platform.architecture()[0])
def cpu_count(args): """Show logical CPU count."""; return _show("Logical CPUs",os.cpu_count() or 1)
def logical_cores(args): """Show logical CPU cores."""; return cpu_count(args)
def physical_cores(args):
    """Show physical CPU cores."""
    try:
        import psutil; return _show("Physical cores",psutil.cpu_count(logical=False) or 1)
    except ImportError: return _show("Physical cores","unknown (pip install psutil)")
def load(args):
    """Show CPU load averages."""
    try: return _show("Load",", ".join(f"{x:.2f}" for x in os.getloadavg()))
    except OSError: util.warn("load averages unavailable"); return 1
def locale_info(args): """Show locale settings."""; return _show("Locale",locale.setlocale(locale.LC_ALL,None))
def timezone(args): """Show timezone."""; return _show("Timezone",time.tzname)
def shell(args): """Show configured shell."""; return _show("Shell",os.environ.get("COMSPEC" if IS_WINDOWS else "SHELL","unknown"))
def path_list(args): """List PATH entries."""; util.table([(i,p) for i,p in enumerate(os.environ.get("PATH","").split(os.pathsep))],headers=["#","Path"]); return 0
def reboot(args):
    """Reboot system with explicit confirmation."""
    if "--yes" not in args and "-y" not in args: util.warn("reboot requires --yes"); return 2
    util.warn("reboot command prepared but not executed by ntk"); return 1
def shutdown(args): """Shutdown system with explicit confirmation."""; return reboot(args)
def logoff(args): """Log off current session."""; util.warn("logoff requires platform-specific interactive action"); return 1
def lock(args):
    """Lock current workstation."""
    cmd=["rundll32","user32.dll,LockWorkStation"] if IS_WINDOWS else (["loginctl","lock-session"] if which("loginctl") else ["xdg-screensaver","lock"])
    if not which(cmd[0]): util.warn("lock command unavailable"); return 1
    return run(cmd)[0]
def motd(args): """Show message of the day."""; p="/etc/motd"; print(open(p).read() if os.path.isfile(p) else "(no motd)",end=""); return 0
def hostname_set(args):
    """Set hostname with --yes confirmation."""
    if not args or args[0] in ("--yes","-y") or ("--yes" not in args and "-y" not in args): util.err("usage: ntk system hostname-set NAME --yes"); return 2
    if "--yes" not in args and "-y" not in args: return 2
    name=args[0]; cmd=["hostname",name]; rc,o,e=run(cmd); print(o or e); return rc
def swap(args):
    """Show swap usage."""
    try:
        import psutil; s=psutil.swap_memory(); [util.kv(k,v) for k,v in (("Total",human_bytes(s.total)),("Used",human_bytes(s.used)),("Percent",f"{s.percent}%"))]; return 0
    except ImportError: util.warn("needs psutil: pip install psutil"); return 1
def virtualization_detect(args): """Detect virtualization hints."""; rc,o,e=run(["systemd-detect-virt"]) if which("systemd-detect-virt") else (1,"",""); return _show("Virtualization",o.strip() or "unknown")
def is_admin(args): """Report administrator privilege."""; return _show("Admin",bool(os.geteuid()==0) if hasattr(os,"geteuid") else False)
def session_info(args): """Show session environment."""; [util.kv(k,os.environ[k]) for k in ("USER","LOGNAME","DISPLAY","TERM","XDG_SESSION_TYPE") if k in os.environ]; return 0
def python_version(args): """Show Python version."""; return _show("Python",platform.python_version())
def ntk_version(args): """Show NTK version."""; return _show("NTK","v2")
def disk_usage(args):
    """Show disk usage for a path."""
    p=args[0] if args else os.getcwd();
    try: d=__import__('shutil').disk_usage(p); [util.kv(k,human_bytes(v)) for k,v in (("Total",d.total),("Used",d.used),("Free",d.free))]; return 0
    except OSError as e: util.err(e); return 1
COMMANDS={k:v for k,v in {"os-info":os_info,"hostname":hostname,"users":users,"whoami":whoami,"env":env_vars,"uptime":uptime,"boot-time":boot_time,"kernel":kernel,"arch":arch,"cpu-count":cpu_count,"logical-cores":logical_cores,"physical-cores":physical_cores,"load":load,"locale":locale_info,"timezone":timezone,"shell":shell,"path-list":path_list,"reboot":reboot,"shutdown":shutdown,"logoff":logoff,"lock":lock,"motd":motd,"hostname-set":hostname_set,"swap":swap,"virtualization-detect":virtualization_detect,"is-admin":is_admin,"session-info":session_info,"python-version":python_version,"ntk-version":ntk_version,"disk-usage":disk_usage}.items()}
