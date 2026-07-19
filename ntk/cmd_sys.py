"""System & OS tools (ntk sys ...)."""
import os
import sys
import platform
import getpass
import socket
import time
from . import util
from .util import col, C, run, IS_WINDOWS

try:
    import psutil
except ImportError:
    psutil = None


def _need_psutil():
    if psutil is None:
        util.warn("This tool needs 'psutil'. Install: pip install psutil")
        return False
    return True


def info(args):
    """OS, CPU, RAM, kernel and uptime at a glance."""
    util.header("System Info")
    util.kv("OS", f"{platform.system()} {platform.release()} ({platform.version()})")
    util.kv("Machine", platform.machine())
    util.kv("Hostname", socket.gethostname())
    util.kv("Python", platform.python_version())
    util.kv("Processor", platform.processor() or "n/a")
    if psutil:
        util.kv("CPU cores", f"{psutil.cpu_count(logical=False)} phys / {psutil.cpu_count()} logical")
        vm = psutil.virtual_memory()
        util.kv("RAM", f"{util.human_bytes(vm.used)} / {util.human_bytes(vm.total)} ({vm.percent}%)")
        boot = psutil.boot_time()
        up = time.time() - boot
        util.kv("Uptime", _fmt_dur(up))
    return 0


def _fmt_dur(seconds):
    seconds = int(seconds)
    d, seconds = divmod(seconds, 86400)
    h, seconds = divmod(seconds, 3600)
    m, s = divmod(seconds, 60)
    parts = []
    if d:
        parts.append(f"{d}d")
    if h or d:
        parts.append(f"{h}h")
    parts.append(f"{m}m")
    parts.append(f"{s}s")
    return " ".join(parts)


def cpu(args):
    """Detailed per-core CPU usage."""
    if not _need_psutil():
        return 1
    util.header("CPU Usage")
    per = psutil.cpu_percent(interval=0.6, percpu=True)
    for i, p in enumerate(per):
        print(f"  Core {str(i).rjust(2)} {util.bar(p/100)} {str(int(p)).rjust(3)}%")
    print()
    util.kv("Total", f"{psutil.cpu_percent()}%")
    try:
        freq = psutil.cpu_freq()
        if freq:
            util.kv("Frequency", f"{freq.current:.0f} MHz")
    except Exception:
        pass
    return 0


def ram(args):
    """Current RAM usage (total, free, cache)."""
    if not _need_psutil():
        return 1
    vm = psutil.virtual_memory()
    sw = psutil.swap_memory()
    util.header("Memory")
    print(f"  RAM  {util.bar(vm.percent/100)} {vm.percent}%")
    util.kv("Total", util.human_bytes(vm.total))
    util.kv("Used", util.human_bytes(vm.used))
    util.kv("Available", util.human_bytes(vm.available))
    util.kv("Swap", f"{util.human_bytes(sw.used)} / {util.human_bytes(sw.total)}")
    return 0


def disk(args):
    """Disk usage of all mounts."""
    if not _need_psutil():
        return 1
    util.header("Disk Usage")
    rows = []
    for part in psutil.disk_partitions(all=False):
        try:
            u = psutil.disk_usage(part.mountpoint)
        except (PermissionError, OSError):
            continue
        rows.append((part.device, util.human_bytes(u.total), util.human_bytes(u.used),
                     util.human_bytes(u.free), f"{u.percent}%"))
    util.table(rows, headers=["Device", "Total", "Used", "Free", "Use%"])
    return 0


def ps(args):
    """List/search processes (filter: ntk sys ps <name>)."""
    if not _need_psutil():
        return 1
    query = args[0].lower() if args else None
    procs = []
    for p in psutil.process_iter(["pid", "name", "cpu_percent", "memory_percent"]):
        try:
            n = p.info["name"] or ""
            if query and query not in n.lower():
                continue
            procs.append((p.info["pid"], n, f"{p.info.get('memory_percent') or 0:.1f}%"))
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    procs.sort(key=lambda r: r[0])
    util.header(f"Processes{' matching ' + repr(query) if query else ''} ({len(procs)})")
    util.table(procs[:60], headers=["PID", "Name", "Mem%"])
    if len(procs) > 60:
        print(col(f"  ... {len(procs)-60} more", C.DIM))
    return 0


def kill(args):
    """Kill a process by PID or name."""
    if not args:
        util.err("usage: ntk sys kill <pid|name>")
        return 2
    if not _need_psutil():
        return 1
    target = args[0]
    killed = 0
    if target.isdigit():
        try:
            psutil.Process(int(target)).terminate()
            killed += 1
        except Exception as e:
            util.err(e)
            return 1
    else:
        for p in psutil.process_iter(["pid", "name"]):
            try:
                if p.info["name"] and target.lower() in p.info["name"].lower():
                    p.terminate()
                    killed += 1
            except Exception:
                continue
    util.ok(f"terminated {killed} process(es)")
    return 0


def kill_port(args):
    """Kill the process holding a given port."""
    if not args:
        util.err("usage: ntk sys kill-port <port>")
        return 2
    if not _need_psutil():
        return 1
    port = int(args[0])
    killed = 0
    for c in psutil.net_connections():
        if c.laddr and c.laddr.port == port and c.pid:
            try:
                psutil.Process(c.pid).terminate()
                killed += 1
                util.ok(f"killed PID {c.pid} on port {port}")
            except Exception as e:
                util.err(e)
    if not killed:
        util.warn(f"no process found on port {port}")
    return 0


def env(args):
    """Show environment variables (filter: ntk sys env <substr>)."""
    q = args[0].lower() if args else None
    rows = []
    for k, v in sorted(os.environ.items()):
        if q and q not in k.lower():
            continue
        if len(v) > 80:
            v = v[:77] + "..."
        rows.append((k, v))
    util.table(rows, headers=["Variable", "Value"])
    return 0


def uptime(args):
    """System uptime since last boot."""
    if not _need_psutil():
        return 1
    up = time.time() - psutil.boot_time()
    util.kv("Uptime", _fmt_dur(up))
    util.kv("Booted", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(psutil.boot_time())))
    return 0


def temp(args):
    """Read hardware temperatures (CPU/GPU)."""
    if not _need_psutil():
        return 1
    fn = getattr(psutil, "sensors_temperatures", None)
    temps = fn() if fn else None
    if not temps:
        util.warn("no temperature sensors available on this platform")
        return 0
    for name, entries in temps.items():
        util.header(name)
        for e in entries:
            util.kv(e.label or "temp", f"{e.current}°C")
    return 0


def battery(args):
    """Battery status and remaining runtime (laptops)."""
    if not _need_psutil():
        return 1
    fn = getattr(psutil, "sensors_battery", None)
    b = fn() if fn else None
    if not b:
        util.warn("no battery detected")
        return 0
    util.header("Battery")
    print(f"  {util.bar(b.percent/100)} {b.percent:.0f}%")
    util.kv("Plugged in", "yes" if b.power_plugged else "no")
    if b.secsleft and b.secsleft > 0:
        util.kv("Time left", _fmt_dur(b.secsleft))
    return 0


def whoami(args):
    """Current user, groups and privilege level."""
    util.header("Identity")
    util.kv("User", getpass.getuser())
    util.kv("Home", os.path.expanduser("~"))
    if IS_WINDOWS:
        try:
            import ctypes
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        except Exception:
            is_admin = False
        util.kv("Admin", "yes" if is_admin else "no")
        util.kv("Domain", os.environ.get("USERDOMAIN", ""))
    else:
        util.kv("UID", os.getuid())
        util.kv("Root", "yes" if os.getuid() == 0 else "no")
    return 0


def history(args):
    """Searchable shell history with usage stats."""
    paths = []
    if IS_WINDOWS:
        appd = os.environ.get("APPDATA", "")
        paths.append(os.path.join(appd, "Microsoft", "Windows", "PowerShell",
                                  "PSReadLine", "ConsoleHost_history.txt"))
    else:
        paths += [os.path.expanduser("~/.bash_history"), os.path.expanduser("~/.zsh_history")]
    lines = []
    for p in paths:
        if os.path.exists(p):
            try:
                lines += open(p, encoding="utf-8", errors="replace").read().splitlines()
            except Exception:
                pass
    if not lines:
        util.warn("no shell history found")
        return 0
    q = args[0].lower() if args else None
    from collections import Counter
    counter = Counter(l.strip().split()[0] for l in lines if l.strip())
    util.header(f"History ({len(lines)} entries)")
    print(col("Top commands:", C.BOLD))
    for cmd, n in counter.most_common(10):
        print(f"  {str(n).rjust(4)}  {cmd}")
    if q:
        print()
        print(col(f"Matches for {q!r}:", C.BOLD))
        for l in lines:
            if q in l.lower():
                print("  " + l)
    return 0


def path(args):
    """Show the PATH variable line by line, de-duplicated."""
    sep = ";" if IS_WINDOWS else ":"
    entries = os.environ.get("PATH", "").split(sep)
    seen = set()
    util.header("PATH entries")
    for e in entries:
        if not e:
            continue
        exists = os.path.isdir(e)
        marker = col("✓", C.GREEN) if exists else col("✗", C.RED)
        dup = col(" (dup)", C.YELLOW) if e in seen else ""
        print(f"  {marker} {e}{dup}")
        seen.add(e)
    return 0


def services(args):
    """List system services and status."""
    if IS_WINDOWS:
        if psutil and hasattr(psutil, "win_service_iter"):
            rows = []
            for s in psutil.win_service_iter():
                try:
                    rows.append((s.name(), s.status()))
                except Exception:
                    continue
            q = args[0].lower() if args else None
            if q:
                rows = [r for r in rows if q in r[0].lower()]
            util.table(rows[:80], headers=["Service", "Status"])
        else:
            rc, out, _ = run(["sc", "query", "type=", "service", "state=", "all"])
            print(out)
    else:
        rc, out, e = run(["systemctl", "list-units", "--type=service", "--no-pager"])
        print(out or e)
    return 0


def service_start(args):
    """Start a service."""
    if not args:
        util.err("usage: ntk sys service-start <name>")
        return 2
    name = args[0]
    cmd = ["sc", "start", name] if IS_WINDOWS else ["systemctl", "start", name]
    rc, out, e = run(cmd)
    print(out or e)
    return rc


def service_stop(args):
    """Stop a service."""
    if not args:
        util.err("usage: ntk sys service-stop <name>")
        return 2
    name = args[0]
    cmd = ["sc", "stop", name] if IS_WINDOWS else ["systemctl", "stop", name]
    rc, out, e = run(cmd)
    print(out or e)
    return rc


def reboot(args):
    """Reboot the system (optional delay seconds)."""
    delay = int(args[0]) if args and args[0].isdigit() else 0
    if IS_WINDOWS:
        cmd = ["shutdown", "/r", "/t", str(delay)]
    else:
        cmd = ["shutdown", "-r", f"+{max(0, delay//60)}"]
    util.warn(f"rebooting in {delay}s ... (Ctrl+C won't cancel; use 'shutdown /a')")
    rc, out, e = run(cmd)
    print(out or e)
    return rc


def shutdown(args):
    """Shut down the system (optional delay seconds)."""
    delay = int(args[0]) if args and args[0].isdigit() else 0
    if IS_WINDOWS:
        cmd = ["shutdown", "/s", "/t", str(delay)]
    else:
        cmd = ["shutdown", "-h", f"+{max(0, delay//60)}"]
    util.warn(f"shutting down in {delay}s ...")
    rc, out, e = run(cmd)
    print(out or e)
    return rc


def log_sys(args):
    """Stream the last lines of system logs."""
    n = int(args[0]) if args and args[0].isdigit() else 40
    if IS_WINDOWS:
        rc, out, e = run(["powershell", "-NoProfile", "-Command",
                          f"Get-EventLog -LogName System -Newest {n} | Format-Table -AutoSize"])
        print(out or e)
    else:
        for p in ["/var/log/syslog", "/var/log/messages"]:
            if os.path.exists(p):
                lines = open(p, errors="replace").read().splitlines()[-n:]
                print("\n".join(lines))
                return 0
        rc, out, e = run(["journalctl", "-n", str(n), "--no-pager"])
        print(out or e)
    return 0


def hardware(args):
    """Detailed hardware specs (mainboard, RAM, GPU)."""
    util.header("Hardware")
    if IS_WINDOWS:
        rc, out, _ = run(["powershell", "-NoProfile", "-Command",
                          "Get-CimInstance Win32_ComputerSystem | Format-List Manufacturer,Model,TotalPhysicalMemory"])
        print(out)
        rc, out, _ = run(["powershell", "-NoProfile", "-Command",
                          "Get-CimInstance Win32_VideoController | Format-List Name,AdapterRAM,DriverVersion"])
        print(out)
    else:
        for f in ["/proc/cpuinfo"]:
            if os.path.exists(f):
                for line in open(f):
                    if "model name" in line:
                        util.kv("CPU", line.split(":", 1)[1].strip())
                        break
        rc, out, _ = run(["lspci"])
        for line in out.splitlines():
            if "VGA" in line or "3D" in line:
                util.kv("GPU", line.split(":", 2)[-1].strip())
    return 0


def shell(args):
    """Info about the current shell and version."""
    util.header("Shell")
    if IS_WINDOWS:
        util.kv("ComSpec", os.environ.get("ComSpec", ""))
        util.kv("PSModulePath?", "yes" if os.environ.get("PSModulePath") else "no")
        rc, out, _ = run(["powershell", "-NoProfile", "-Command", "$PSVersionTable.PSVersion.ToString()"])
        util.kv("PowerShell", out.strip())
    else:
        util.kv("SHELL", os.environ.get("SHELL", ""))
        rc, out, _ = run([os.environ.get("SHELL", "bash"), "--version"])
        print(out.splitlines()[0] if out else "")
    return 0


COMMANDS = {
    "info": info, "cpu": cpu, "ram": ram, "disk": disk, "ps": ps,
    "kill": kill, "kill-port": kill_port, "env": env, "uptime": uptime,
    "temp": temp, "battery": battery, "whoami": whoami, "history": history,
    "path": path, "services": services, "service-start": service_start,
    "service-stop": service_stop, "reboot": reboot, "shutdown": shutdown,
    "log-sys": log_sys, "hardware": hardware, "shell": shell,
}
