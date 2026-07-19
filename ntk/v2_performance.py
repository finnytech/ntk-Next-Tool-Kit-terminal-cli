"""Performance tools (ntk performance ...). SAFE by default: never closes user apps,
never deletes personal files. Cleanup targets only temp/cache and asks confirmation."""
import os
import sys
import glob
import shutil
import tempfile
import ctypes
from . import util
from .util import col, C, run, which, IS_WINDOWS, human_bytes


# ---------------- helpers ----------------
def _confirm(prompt, args):
    if "--yes" in args or "-y" in args:
        return True
    if not sys.stdin or not sys.stdin.isatty():
        util.warn("non-interactive; re-run with --yes to actually apply.")
        return False
    try:
        return input(f"  {prompt} [y/N] ").strip().lower() in ("y", "yes")
    except (EOFError, KeyboardInterrupt):
        print()
        return False


def _dir_size(path):
    total = 0
    for root, _dirs, files in os.walk(path, topdown=True, onerror=lambda e: None):
        for f in files:
            try:
                total += os.path.getsize(os.path.join(root, f))
            except OSError:
                pass
    return total


def _safe_clean(path, dry=True):
    """Delete files inside a temp/cache dir. Returns (freed_bytes, removed_count)."""
    freed = 0
    removed = 0
    if not path or not os.path.isdir(path):
        return 0, 0
    for name in os.listdir(path):
        full = os.path.join(path, name)
        try:
            if os.path.isfile(full) or os.path.islink(full):
                sz = os.path.getsize(full) if os.path.isfile(full) else 0
                if not dry:
                    os.remove(full)
                freed += sz
                removed += 1
            elif os.path.isdir(full):
                sz = _dir_size(full)
                if not dry:
                    shutil.rmtree(full, ignore_errors=True)
                freed += sz
                removed += 1
        except (OSError, PermissionError):
            pass
    return freed, removed


def _temp_dirs():
    dirs = []
    dirs.append(tempfile.gettempdir())
    if IS_WINDOWS:
        for e in ("TEMP", "TMP"):
            v = os.environ.get(e)
            if v:
                dirs.append(v)
        win = os.environ.get("WINDIR", r"C:\Windows")
        dirs.append(os.path.join(win, "Temp"))
        la = os.environ.get("LOCALAPPDATA", "")
        if la:
            dirs.append(os.path.join(la, "Temp"))
    else:
        dirs += ["/tmp", "/var/tmp"]
    # unique + existing
    seen, out = set(), []
    for d in dirs:
        d = os.path.normpath(d)
        if d not in seen and os.path.isdir(d):
            seen.add(d)
            out.append(d)
    return out


def _psutil():
    try:
        import psutil
        return psutil
    except ImportError:
        return None


# ---------------- RAM ----------------
def ram_free(args):
    """Free RAM by trimming working sets/caches (SAFE: no apps closed)."""
    dry = not ("--yes" in args or "-y" in args)
    ps = _psutil()
    before = ps.virtual_memory().available if ps else None
    if IS_WINDOWS:
        util.info("Trimming process working sets (safe, non-critical processes only)...")
        trimmed = 0
        try:
            EmptyWorkingSet = ctypes.windll.psapi.EmptyWorkingSet
            OpenProcess = ctypes.windll.kernel32.OpenProcess
            CloseHandle = ctypes.windll.kernel32.CloseHandle
            PROTECTED = {"system", "smss.exe", "csrss.exe", "wininit.exe",
                         "winlogon.exe", "services.exe", "lsass.exe", "svchost.exe",
                         "registry", "memory compression"}
            if ps:
                for p in ps.process_iter(["pid", "name"]):
                    nm = (p.info.get("name") or "").lower()
                    if nm in PROTECTED or p.info["pid"] <= 4:
                        continue
                    if dry:
                        trimmed += 1
                        continue
                    h = OpenProcess(0x1F0FFF, False, p.info["pid"])
                    if h:
                        try:
                            if EmptyWorkingSet(h):
                                trimmed += 1
                        finally:
                            CloseHandle(h)
        except Exception as e:
            util.warn(f"working-set trim partly failed: {e}")
        action = "would trim" if dry else "trimmed"
        util.ok(f"{action} {trimmed} process working sets")
    else:
        util.info("Requesting kernel to drop clean caches (needs root)...")
        if dry:
            util.warn("dry run; re-run with --yes (and sudo) to apply.")
        else:
            rc, _o, _e = run(["sync"])
            try:
                with open("/proc/sys/vm/drop_caches", "w") as f:
                    f.write("3\n")
                util.ok("dropped pagecache/dentries/inodes")
            except PermissionError:
                util.err("need root: sudo ntk performance ram-free --yes")
                return 1
    if ps:
        after = ps.virtual_memory().available
        util.kv("Available before", human_bytes(before))
        util.kv("Available after", human_bytes(after))
        if after > before:
            util.kv("Freed", human_bytes(after - before))
    if dry:
        util.info("Dry run. Add --yes to actually apply.")
    return 0


def mem_report(args):
    """Detailed memory usage report."""
    ps = _psutil()
    if not ps:
        util.warn("needs psutil: pip install psutil")
        return 1
    vm = ps.virtual_memory()
    sm = ps.swap_memory()
    util.header("Memory Report")
    util.kv("Total", human_bytes(vm.total))
    util.kv("Used", human_bytes(vm.used))
    util.kv("Available", human_bytes(vm.available))
    util.kv("Percent", f"{vm.percent}%")
    print("  " + util.bar(vm.percent / 100.0))
    util.kv("Swap total", human_bytes(sm.total))
    util.kv("Swap used", human_bytes(sm.used))
    return 0


def top_memory(args):
    """Show top memory-consuming processes."""
    ps = _psutil()
    if not ps:
        util.warn("needs psutil: pip install psutil")
        return 1
    n = int(args[0]) if args and args[0].isdigit() else 10
    procs = []
    for p in ps.process_iter(["pid", "name", "memory_info"]):
        try:
            procs.append((p.info["memory_info"].rss, p.info["pid"], p.info["name"]))
        except Exception:
            pass
    procs.sort(reverse=True)
    util.header(f"Top {n} memory processes")
    util.table([(pid, name, human_bytes(rss)) for rss, pid, name in procs[:n]],
               headers=["PID", "Name", "RAM"])
    return 0


# ---------------- DISK CLEAN ----------------
def clean_disk(args):
    """Clean ONLY temp/cache (safe). Personal files untouched. Use --yes to apply."""
    dry = not ("--yes" in args or "-y" in args)
    targets = _temp_dirs()
    util.header("Disk Cleanup (safe: temp & caches only)")
    total_freed = 0
    rows = []
    for d in targets:
        freed, removed = _safe_clean(d, dry=True)  # measure first
        total_freed += freed
        rows.append((d, human_bytes(freed), removed))
    util.table(rows, headers=["Location", "Reclaimable", "Items"])
    util.kv("Total reclaimable", human_bytes(total_freed))
    if dry:
        util.info("Dry run. Re-run with --yes to actually delete temp/cache files.")
        return 0
    if not _confirm("Delete these temp/cache files now?", args):
        util.warn("cancelled.")
        return 0
    real_freed = 0
    for d in targets:
        f, _ = _safe_clean(d, dry=False)
        real_freed += f
    util.ok(f"Freed {human_bytes(real_freed)}")
    return 0


def temp_clean(args):
    """Clear temporary files only (alias of clean-disk, temp dirs)."""
    return clean_disk(args)


def cache_clean(args):
    """Clear common app/browser caches (safe)."""
    dry = not ("--yes" in args or "-y" in args)
    caches = []
    home = os.path.expanduser("~")
    if IS_WINDOWS:
        la = os.environ.get("LOCALAPPDATA", "")
        for sub in [r"Google\Chrome\User Data\Default\Cache",
                    r"Microsoft\Edge\User Data\Default\Cache",
                    r"Mozilla\Firefox\Profiles"]:
            if la:
                caches.append(os.path.join(la, sub))
    else:
        caches += [os.path.join(home, ".cache"),
                   os.path.join(home, ".mozilla")]
    util.header("Cache Cleanup")
    total = 0
    rows = []
    for c in caches:
        if os.path.isdir(c):
            sz = _dir_size(c)
            total += sz
            rows.append((c, human_bytes(sz)))
    util.table(rows, headers=["Cache", "Size"])
    util.kv("Total", human_bytes(total))
    if dry:
        util.info("Dry run. Add --yes to clear caches.")
        return 0
    if not _confirm("Clear these caches?", args):
        return 0
    freed = 0
    for c in caches:
        f, _ = _safe_clean(c, dry=False)
        freed += f
    util.ok(f"Freed {human_bytes(freed)}")
    return 0


def recycle_clean(args):
    """Empty the Recycle Bin / Trash (asks first)."""
    if not _confirm("Empty the Recycle Bin / Trash?", args):
        util.warn("cancelled (or use --yes).")
        return 0
    if IS_WINDOWS:
        try:
            SHEmptyRecycleBin = ctypes.windll.shell32.SHEmptyRecycleBinW
            # 0x7 = no confirmation, progress, or sound
            SHEmptyRecycleBin(None, None, 0x7)
            util.ok("Recycle Bin emptied.")
            return 0
        except Exception as e:
            util.err(f"failed: {e}")
            return 1
    else:
        trash = os.path.expanduser("~/.local/share/Trash/files")
        f, n = _safe_clean(trash, dry=False)
        util.ok(f"Trash emptied ({human_bytes(f)}, {n} items)")
        return 0


# ---------------- CPU ----------------
def cpu_optimize(args):
    """Report CPU hogs and lower priority of heavy background tasks (safe)."""
    ps = _psutil()
    if not ps:
        util.warn("needs psutil: pip install psutil")
        return 1
    dry = not ("--yes" in args or "-y" in args)
    util.info("Scanning CPU usage (2s sample)...")
    for p in ps.process_iter():
        try:
            p.cpu_percent(None)
        except Exception:
            pass
    import time
    time.sleep(2)
    procs = []
    for p in ps.process_iter(["pid", "name"]):
        try:
            procs.append((p.cpu_percent(None), p.info["pid"], p.info["name"], p))
        except Exception:
            pass
    procs.sort(reverse=True)
    util.header("Top CPU processes")
    util.table([(pid, name, f"{cpu:.1f}%") for cpu, pid, name, _ in procs[:10]],
               headers=["PID", "Name", "CPU"])
    lowered = 0
    PROTECT = {"system", "explorer.exe", "ntk.exe", "python.exe"}
    for cpu, pid, name, p in procs[:10]:
        if cpu < 15 or (name or "").lower() in PROTECT:
            continue
        if dry:
            lowered += 1
            continue
        try:
            if IS_WINDOWS:
                p.nice(ps.BELOW_NORMAL_PRIORITY_CLASS)
            else:
                p.nice(min(19, p.nice() + 5))
            lowered += 1
        except Exception:
            pass
    verb = "would lower" if dry else "lowered"
    util.ok(f"{verb} priority of {lowered} heavy background process(es)")
    if dry:
        util.info("Dry run. Add --yes to apply.")
    return 0


def cpu_info(args):
    """Show CPU model, cores and current load."""
    ps = _psutil()
    util.header("CPU")
    model = ""
    if IS_WINDOWS:
        rc, out, _ = run(["wmic", "cpu", "get", "name"], timeout=8)
        lines = [l.strip() for l in out.splitlines() if l.strip() and "Name" not in l]
        model = lines[0] if lines else ""
    else:
        try:
            with open("/proc/cpuinfo") as f:
                for line in f:
                    if "model name" in line:
                        model = line.split(":", 1)[1].strip()
                        break
        except OSError:
            pass
    util.kv("Model", model or "unknown")
    util.kv("Logical cores", os.cpu_count())
    if ps:
        util.kv("Load", f"{ps.cpu_percent(interval=1)}%")
    return 0


def cpu_throttle_check(args):
    """Check whether the CPU is being thermally/power throttled."""
    util.header("CPU Throttle Check")
    if IS_WINDOWS:
        rc, out, _ = run(["wmic", "cpu", "get", "CurrentClockSpeed,MaxClockSpeed"], timeout=8)
        print(out.strip() or "(no data)")
    else:
        paths = glob.glob("/sys/devices/system/cpu/cpu*/cpufreq/scaling_cur_freq")
        if paths:
            for p in paths[:4]:
                try:
                    khz = int(open(p).read().strip())
                    util.kv(p.split("/")[5], f"{khz/1000:.0f} MHz")
                except OSError:
                    pass
        else:
            util.warn("no cpufreq data available")
    return 0


# ---------------- GPU ----------------
def gpu_optimize(args):
    """Report GPU status and power/optimization hints."""
    return gpu_info(args)


def gpu_info(args):
    """Show GPU model, driver, memory and power mode."""
    util.header("GPU")
    if which("nvidia-smi"):
        rc, out, _ = run(["nvidia-smi",
                          "--query-gpu=name,driver_version,memory.total,memory.used,utilization.gpu,power.draw",
                          "--format=csv,noheader"], timeout=8)
        if rc == 0 and out.strip():
            for line in out.strip().splitlines():
                parts = [x.strip() for x in line.split(",")]
                keys = ["Name", "Driver", "Mem total", "Mem used", "Util", "Power"]
                for k, v in zip(keys, parts):
                    util.kv(k, v)
            return 0
    if IS_WINDOWS:
        rc, out, _ = run(["wmic", "path", "win32_VideoController", "get",
                          "Name,DriverVersion,AdapterRAM"], timeout=8)
        print(out.strip() or "(no GPU data)")
        return 0
    else:
        if which("lspci"):
            rc, out, _ = run(["lspci"], timeout=8)
            gpus = [l for l in out.splitlines() if "VGA" in l or "3D" in l or "Display" in l]
            print("\n".join("  " + g for g in gpus) or "  (no GPU found)")
        else:
            util.warn("install nvidia-smi or lspci for GPU details")
        return 0


# ---------------- BOOST / COMBO ----------------
def boost(args):
    """Safe all-in-one: report + free RAM + preview disk cleanup. --yes applies."""
    apply = "--yes" in args or "-y" in args
    util.header("NTK Performance Boost (safe mode)")
    mem_report([])
    print()
    ram_free(args if apply else [])
    print()
    clean_disk([])  # always dry preview here
    print()
    util.info("Boost complete." + ("" if apply else " Add --yes to also free RAM & clean disk."))
    return 0


def dns_flush(args):
    """Flush the DNS resolver cache."""
    if IS_WINDOWS:
        rc, out, e = run(["ipconfig", "/flushdns"], timeout=10)
        print(out or e)
        return rc
    for cmd in (["resolvectl", "flush-caches"], ["systemd-resolve", "--flush-caches"]):
        if which(cmd[0]):
            rc, out, e = run(cmd, timeout=10)
            util.ok("DNS cache flushed" if rc == 0 else (e or "failed"))
            return rc
    util.warn("no supported DNS flush tool found (systemd-resolved).")
    return 1


def power_plan(args):
    """Show or set the OS power plan (high-performance/balanced)."""
    if IS_WINDOWS:
        if args and args[0] in ("high", "performance"):
            run(["powercfg", "/setactive", "SCHEME_MIN"], timeout=8)
            util.ok("Set High performance power plan.")
            return 0
        if args and args[0] == "balanced":
            run(["powercfg", "/setactive", "SCHEME_BALANCED"], timeout=8)
            util.ok("Set Balanced power plan.")
            return 0
        rc, out, _ = run(["powercfg", "/getactivescheme"], timeout=8)
        print(out.strip() or "(unknown)")
        return 0
    else:
        gov = glob.glob("/sys/devices/system/cpu/cpu0/cpufreq/scaling_governor")
        if gov:
            util.kv("Governor", open(gov[0]).read().strip())
        else:
            util.warn("no cpufreq governor info")
        return 0


def startup_list(args):
    """List programs that run at startup (report-first)."""
    util.header("Startup Programs")
    if IS_WINDOWS:
        rc, out, _ = run(["wmic", "startup", "get", "Caption,Command"], timeout=10)
        print(out.strip() or "(none)")
    else:
        paths = glob.glob(os.path.expanduser("~/.config/autostart/*.desktop"))
        for p in paths:
            util.kv(os.path.basename(p), "autostart")
        if not paths:
            util.info("no user autostart entries")
    return 0


def services_list(args):
    """List running services (to spot trimmable ones)."""
    util.header("Services")
    if IS_WINDOWS:
        rc, out, _ = run(["net", "start"], timeout=10)
        print(out.strip())
    else:
        if which("systemctl"):
            rc, out, _ = run(["systemctl", "list-units", "--type=service",
                              "--state=running", "--no-pager", "--no-legend"], timeout=10)
            print(out.strip())
        else:
            util.warn("systemctl not available")
    return 0


def bloat_scan(args):
    """Scan for large caches, logs and temp taking up space."""
    util.header("Bloat Scan")
    targets = _temp_dirs()
    home = os.path.expanduser("~")
    extra = []
    if IS_WINDOWS:
        win = os.environ.get("WINDIR", r"C:\Windows")
        extra = [os.path.join(win, "SoftwareDistribution", "Download"),
                 os.path.join(win, "Logs")]
    else:
        extra = ["/var/log", os.path.join(home, ".cache")]
    rows = []
    for d in targets + extra:
        if os.path.isdir(d):
            rows.append((d, human_bytes(_dir_size(d))))
    rows.sort(key=lambda r: r[0])
    util.table(rows, headers=["Location", "Size"])
    return 0


def disk_usage(args):
    """Show disk usage summary for all drives."""
    util.header("Disk Usage")
    ps = _psutil()
    if ps:
        for part in ps.disk_partitions(all=False):
            try:
                u = ps.disk_usage(part.mountpoint)
                util.kv(part.device, f"{human_bytes(u.used)}/{human_bytes(u.total)} ({u.percent}%)")
                print("  " + util.bar(u.percent / 100.0))
            except (PermissionError, OSError):
                pass
    else:
        total, used, free = shutil.disk_usage(os.path.abspath(os.sep))
        util.kv("Used", f"{human_bytes(used)}/{human_bytes(total)}")
    return 0


def thermals(args):
    """Show temperature sensors if available."""
    ps = _psutil()
    util.header("Thermals")
    if ps and hasattr(ps, "sensors_temperatures"):
        temps = ps.sensors_temperatures()
        if temps:
            for chip, entries in temps.items():
                for e in entries:
                    util.kv(f"{chip}/{e.label or 'temp'}", f"{e.current}°C")
            return 0
    util.warn("no temperature sensors exposed on this system.")
    return 1


def uptime(args):
    """Show system uptime and boot time."""
    ps = _psutil()
    if not ps:
        util.warn("needs psutil: pip install psutil")
        return 1
    import time
    boot = ps.boot_time()
    up = time.time() - boot
    d, rem = divmod(int(up), 86400)
    h, rem = divmod(rem, 3600)
    m, _ = divmod(rem, 60)
    util.kv("Uptime", f"{d}d {h}h {m}m")
    util.kv("Booted", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(boot)))
    return 0


def battery(args):
    """Show battery percentage and time remaining."""
    ps = _psutil()
    if not ps or not hasattr(ps, "sensors_battery"):
        util.warn("needs psutil: pip install psutil")
        return 1
    b = ps.sensors_battery()
    if not b:
        util.info("no battery (desktop?)")
        return 0
    util.kv("Charge", f"{b.percent}%")
    util.kv("Plugged in", "yes" if b.power_plugged else "no")
    if b.secsleft and b.secsleft > 0:
        util.kv("Time left", f"{b.secsleft//3600}h {(b.secsleft%3600)//60}m")
    return 0


def network_boost(args):
    """Report network tweaks and flush DNS (safe)."""
    util.header("Network Boost")
    dns_flush([])
    if IS_WINDOWS:
        util.info("Tip: 'ntk performance power-plan high' can help sustained throughput.")
    return 0


def io_report(args):
    """Show disk I/O counters."""
    ps = _psutil()
    if not ps:
        util.warn("needs psutil: pip install psutil")
        return 1
    io = ps.disk_io_counters()
    if not io:
        util.warn("no disk I/O data")
        return 1
    util.kv("Read", human_bytes(io.read_bytes))
    util.kv("Write", human_bytes(io.write_bytes))
    util.kv("Read count", io.read_count)
    util.kv("Write count", io.write_count)
    return 0


def net_report(args):
    """Show network I/O counters per interface."""
    ps = _psutil()
    if not ps:
        util.warn("needs psutil: pip install psutil")
        return 1
    counters = ps.net_io_counters(pernic=True)
    rows = [(nic, human_bytes(c.bytes_sent), human_bytes(c.bytes_recv))
            for nic, c in counters.items()]
    util.table(rows, headers=["Interface", "Sent", "Recv"])
    return 0


def process_count(args):
    """Count running processes and threads."""
    ps = _psutil()
    if not ps:
        util.warn("needs psutil: pip install psutil")
        return 1
    procs = list(ps.process_iter())
    threads = 0
    for p in procs:
        try:
            threads += p.num_threads()
        except Exception:
            pass
    util.kv("Processes", len(procs))
    util.kv("Threads", threads)
    return 0


def health(args):
    """Overall performance health score (RAM/CPU/disk)."""
    ps = _psutil()
    if not ps:
        util.warn("needs psutil: pip install psutil")
        return 1
    vm = ps.virtual_memory()
    cpu = ps.cpu_percent(interval=1)
    disk = ps.disk_usage(os.path.abspath(os.sep)).percent
    score = 100 - (vm.percent * 0.4 + cpu * 0.3 + disk * 0.3)
    score = max(0, min(100, int(score)))
    util.header("System Health")
    util.kv("RAM used", f"{vm.percent}%")
    util.kv("CPU load", f"{cpu}%")
    util.kv("Disk used", f"{disk}%")
    util.kv("Health score", f"{score}/100")
    print("  " + util.bar(score / 100.0))
    return 0


def standby_clear(args):
    """Clear the standby memory list (Windows, needs admin)."""
    if not IS_WINDOWS:
        return ram_free(args)
    util.info("Standby list clearing requires admin rights and RAMMap/EmptyStandbyList.")
    if which("EmptyStandbyList.exe"):
        if not ("--yes" in args or "-y" in args):
            util.info("Add --yes to run EmptyStandbyList.")
            return 0
        rc, out, e = run(["EmptyStandbyList.exe", "standbylist"], timeout=15)
        util.ok("standby list cleared" if rc == 0 else (e or "failed"))
        return rc
    util.warn("EmptyStandbyList.exe not found on PATH; ram-free trims working sets instead.")
    return ram_free(args)


def prefetch_clean(args):
    """Clean Windows Prefetch (safe; rebuilt automatically)."""
    if not IS_WINDOWS:
        util.info("Prefetch is Windows-only.")
        return 0
    pf = os.path.join(os.environ.get("WINDIR", r"C:\Windows"), "Prefetch")
    if not os.path.isdir(pf):
        util.warn("Prefetch folder not found (need admin).")
        return 1
    freed, _ = _safe_clean(pf, dry=True)
    util.kv("Prefetch reclaimable", human_bytes(freed))
    if not ("--yes" in args or "-y" in args):
        util.info("Add --yes to clean (Windows rebuilds it automatically).")
        return 0
    f, n = _safe_clean(pf, dry=False)
    util.ok(f"cleaned {n} prefetch files ({human_bytes(f)})")
    return 0


def gpu_processes(args):
    """List processes using the GPU (nvidia only)."""
    if which("nvidia-smi"):
        rc, out, _ = run(["nvidia-smi",
                          "--query-compute-apps=pid,process_name,used_memory",
                          "--format=csv,noheader"], timeout=8)
        print(out.strip() or "  (no GPU processes)")
        return 0
    util.warn("nvidia-smi not found; GPU process list unavailable.")
    return 1


def swap_report(args):
    """Show swap/pagefile usage."""
    ps = _psutil()
    if not ps:
        util.warn("needs psutil: pip install psutil")
        return 1
    sm = ps.swap_memory()
    util.kv("Swap total", human_bytes(sm.total))
    util.kv("Swap used", human_bytes(sm.used))
    util.kv("Percent", f"{sm.percent}%")
    return 0


def quick_scan(args):
    """Fast overview: health + top RAM + top CPU."""
    health([])
    print()
    top_memory(["5"])
    return 0


COMMANDS = {
    "ram-free": ram_free,
    "mem-report": mem_report,
    "top-memory": top_memory,
    "clean-disk": clean_disk,
    "temp-clean": temp_clean,
    "cache-clean": cache_clean,
    "recycle-clean": recycle_clean,
    "cpu-optimize": cpu_optimize,
    "cpu-info": cpu_info,
    "cpu-throttle-check": cpu_throttle_check,
    "gpu-optimize": gpu_optimize,
    "gpu-info": gpu_info,
    "gpu-processes": gpu_processes,
    "boost": boost,
    "quick-scan": quick_scan,
    "dns-flush": dns_flush,
    "power-plan": power_plan,
    "startup-list": startup_list,
    "services-list": services_list,
    "bloat-scan": bloat_scan,
    "disk-usage": disk_usage,
    "thermals": thermals,
    "uptime": uptime,
    "battery": battery,
    "network-boost": network_boost,
    "net-report": net_report,
    "io-report": io_report,
    "process-count": process_count,
    "health": health,
    "standby-clear": standby_clear,
    "prefetch-clean": prefetch_clean,
    "swap-report": swap_report,
}
