"""Admin tools (ntk admin ...). Read-only by default; destructive ops need --yes."""
import os
import sys
import getpass
from . import util
from .util import col, C, run, which, IS_WINDOWS


def _yes(args):
    return "--yes" in args or "-y" in args


def is_admin(args):
    """Check if running with admin/root rights."""
    if IS_WINDOWS:
        try:
            import ctypes
            adm = ctypes.windll.shell32.IsUserAnAdmin() != 0
        except Exception:
            adm = False
    else:
        adm = (os.geteuid() == 0)
    util.kv("Admin/root", "yes" if adm else "no")
    return 0


def current_user(args):
    """Show the current user name."""
    util.kv("User", getpass.getuser())
    return 0


def users_list(args):
    """List local user accounts."""
    if IS_WINDOWS:
        rc, out, e = run(["net", "user"], timeout=10)
        print(out or e)
        return rc
    try:
        with open("/etc/passwd") as f:
            users = [l.split(":")[0] for l in f if l.strip()]
        util.header("Users")
        for u in users:
            print("  " + u)
        return 0
    except OSError as e:
        util.err(str(e))
        return 1


def user_info(args):
    """Show info about a user: <name>."""
    if not args:
        util.err("usage: ntk admin user-info <name>")
        return 2
    if IS_WINDOWS:
        rc, out, e = run(["net", "user", args[0]], timeout=10)
        print(out or e)
        return rc
    rc, out, e = run(["id", args[0]], timeout=10)
    print(out or e)
    return rc


def groups_list(args):
    """List groups."""
    if IS_WINDOWS:
        rc, out, e = run(["net", "localgroup"], timeout=10)
        print(out or e)
        return rc
    try:
        with open("/etc/group") as f:
            for l in f:
                if l.strip():
                    print("  " + l.split(":")[0])
        return 0
    except OSError as e:
        util.err(str(e))
        return 1


def current_privileges(args):
    """Show current user privileges/groups."""
    if IS_WINDOWS:
        rc, out, e = run(["whoami", "/priv"], timeout=10)
        print(out or e)
        return rc
    rc, out, e = run(["id"], timeout=10)
    print(out or e)
    return rc


def hostname(args):
    """Show the machine hostname."""
    import socket
    util.kv("Hostname", socket.gethostname())
    return 0


def firewall_status(args):
    """Show firewall status."""
    if IS_WINDOWS:
        rc, out, e = run(["netsh", "advfirewall", "show", "allprofiles", "state"], timeout=12)
        print(out or e)
        return rc
    if which("ufw"):
        rc, out, e = run(["ufw", "status"], timeout=10)
        print(out or e)
        return rc
    util.warn("no supported firewall tool found (ufw).")
    return 1


def firewall_rules_count(args):
    """Count firewall rules."""
    if IS_WINDOWS:
        rc, out, _ = run(["netsh", "advfirewall", "firewall", "show", "rule", "name=all"], timeout=20)
        n = out.count("Rule Name:")
        util.kv("Firewall rules", n)
        return 0
    if which("iptables"):
        rc, out, _ = run(["iptables", "-S"], timeout=10)
        util.kv("iptables rules", len(out.splitlines()))
        return 0
    util.warn("need admin/iptables to count rules.")
    return 1


def hosts_file(args):
    """Show the hosts file."""
    path = r"C:\Windows\System32\drivers\etc\hosts" if IS_WINDOWS else "/etc/hosts"
    try:
        with open(path) as f:
            print(f.read())
        return 0
    except (OSError, PermissionError) as e:
        util.err(str(e))
        return 1


def services_list(args):
    """List running services."""
    if IS_WINDOWS:
        rc, out, e = run(["net", "start"], timeout=12)
        print(out or e)
        return rc
    if which("systemctl"):
        rc, out, e = run(["systemctl", "list-units", "--type=service",
                          "--state=running", "--no-pager", "--no-legend"], timeout=12)
        print(out or e)
        return rc
    util.warn("systemctl not available")
    return 1


def scheduled_tasks(args):
    """List scheduled tasks / cron jobs."""
    if IS_WINDOWS:
        rc, out, e = run(["schtasks", "/query", "/fo", "LIST"], timeout=20)
        print((out or e)[:4000])
        return rc
    rc, out, e = run(["crontab", "-l"], timeout=10)
    print(out or "(no crontab)")
    return 0


def startup_programs(args):
    """List startup programs."""
    if IS_WINDOWS:
        rc, out, e = run(["wmic", "startup", "get", "Caption,Command"], timeout=12)
        print(out or e)
        return rc
    import glob
    entries = glob.glob(os.path.expanduser("~/.config/autostart/*.desktop"))
    for p in entries:
        print("  " + os.path.basename(p))
    if not entries:
        util.info("no user autostart entries")
    return 0


def network_shares(args):
    """List network shares."""
    if IS_WINDOWS:
        rc, out, e = run(["net", "share"], timeout=10)
        print(out or e)
        return rc
    if which("smbstatus"):
        rc, out, e = run(["smbstatus", "--shares"], timeout=10)
        print(out or e)
        return rc
    util.warn("no SMB share info available")
    return 1


def password_policy(args):
    """Show password policy (Windows)."""
    if IS_WINDOWS:
        rc, out, e = run(["net", "accounts"], timeout=10)
        print(out or e)
        return rc
    util.info("On Linux, check /etc/login.defs and PAM config.")
    return 0


def last_boot(args):
    """Show last boot time."""
    try:
        import psutil
        import time
        util.kv("Last boot", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(psutil.boot_time())))
        return 0
    except ImportError:
        if IS_WINDOWS:
            rc, out, e = run(["net", "statistics", "workstation"], timeout=10)
            print(out or e)
            return rc
        rc, out, e = run(["uptime", "-s"], timeout=10)
        print(out or e)
        return 0


def event_log_tail(args):
    """Show recent system log entries."""
    if IS_WINDOWS:
        rc, out, e = run(["wevtutil", "qe", "System", "/c:10", "/rd:true", "/f:text"], timeout=20)
        print((out or e)[:4000])
        return rc
    if which("journalctl"):
        rc, out, e = run(["journalctl", "-n", "20", "--no-pager"], timeout=12)
        print(out or e)
        return rc
    try:
        with open("/var/log/syslog") as f:
            lines = f.readlines()[-20:]
        print("".join(lines))
        return 0
    except (OSError, PermissionError):
        util.warn("no readable system log")
        return 1


def failed_logins(args):
    """Show failed login attempts (best-effort)."""
    if IS_WINDOWS:
        util.info("Check Event Viewer > Security (Event ID 4625).")
        return 0
    for cmd in (["lastb", "-n", "10"], ["journalctl", "-n", "20", "-g", "Failed"]):
        if which(cmd[0]):
            rc, out, e = run(cmd, timeout=12)
            print(out or "(none)")
            return 0
    util.warn("no failed-login source available (need root).")
    return 1


def uac_status(args):
    """Show UAC status (Windows)."""
    if not IS_WINDOWS:
        util.info("UAC is Windows-only.")
        return 0
    try:
        import winreg
        key = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System"
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key) as k:
            v, _ = winreg.QueryValueEx(k, "EnableLUA")
        util.kv("UAC enabled", "yes" if v else "no")
        return 0
    except Exception as e:
        util.err(str(e))
        return 1


def ssh_keys_list(args):
    """List SSH keys in ~/.ssh."""
    d = os.path.expanduser("~/.ssh")
    if not os.path.isdir(d):
        util.info("no ~/.ssh directory")
        return 0
    util.header("SSH keys")
    for f in sorted(os.listdir(d)):
        if f.endswith(".pub") or f in ("id_rsa", "id_ed25519", "id_ecdsa"):
            util.kv(f, "present")
    return 0


def cron_list(args):
    """List cron jobs (Linux)."""
    if IS_WINDOWS:
        util.info("Windows uses Task Scheduler: ntk admin scheduled-tasks")
        return 0
    rc, out, e = run(["crontab", "-l"], timeout=10)
    print(out or "(no crontab entries)")
    return 0


def sudoers_check(args):
    """Show sudo access (Linux)."""
    if IS_WINDOWS:
        util.info("Windows: check group membership with 'ntk admin current-privileges'.")
        return 0
    rc, out, e = run(["sudo", "-n", "-l"], timeout=10)
    print(out or e or "(cannot determine without password)")
    return 0


def env_system(args):
    """Show important system environment variables."""
    keys = ["PATH", "HOME", "USER", "USERNAME", "COMPUTERNAME", "OS",
            "SHELL", "TEMP", "SystemRoot", "ProgramFiles"]
    util.header("System environment")
    for k in keys:
        v = os.environ.get(k)
        if v:
            util.kv(k, v if len(v) < 80 else v[:77] + "...")
    return 0


def open_ports(args):
    """List listening ports (admin view)."""
    if IS_WINDOWS:
        rc, out, e = run(["netstat", "-ano"], timeout=15)
    else:
        rc, out, e = run(["ss", "-tuln"], timeout=10)
        if rc != 0:
            rc, out, e = run(["netstat", "-tuln"], timeout=10)
    listening = [l for l in (out or "").splitlines() if "LISTEN" in l.upper()]
    print("\n".join(listening[:60]) or (out or "(none)")[:2000])
    return 0


def logged_in(args):
    """Show currently logged-in users."""
    if IS_WINDOWS:
        rc, out, e = run(["query", "user"], timeout=10)
        print(out or e or "(none)")
        return 0
    rc, out, e = run(["who"], timeout=10)
    print(out or "(none)")
    return 0


def disk_permissions(args):
    """Show permissions of a path: <path>."""
    path = args[0] if args else "."
    try:
        st = os.stat(path)
        util.kv("Path", os.path.abspath(path))
        util.kv("Mode", oct(st.st_mode & 0o777))
        util.kv("UID", st.st_uid)
        util.kv("GID", st.st_gid)
        return 0
    except OSError as e:
        util.err(str(e))
        return 1


def reboot(args):
    """Reboot the machine (requires --yes)."""
    if not _yes(args):
        util.warn("this will REBOOT. Re-run with --yes to confirm.")
        return 2
    if IS_WINDOWS:
        return run(["shutdown", "/r", "/t", "5"], timeout=10)[0]
    return run(["shutdown", "-r", "+1"], timeout=10)[0]


def shutdown(args):
    """Shut down the machine (requires --yes)."""
    if not _yes(args):
        util.warn("this will SHUT DOWN. Re-run with --yes to confirm.")
        return 2
    if IS_WINDOWS:
        return run(["shutdown", "/s", "/t", "5"], timeout=10)[0]
    return run(["shutdown", "-h", "+1"], timeout=10)[0]


def lock_screen(args):
    """Lock the screen."""
    if IS_WINDOWS:
        import ctypes
        ctypes.windll.user32.LockWorkStation()
        util.ok("locked")
        return 0
    for cmd in (["loginctl", "lock-session"], ["xdg-screensaver", "lock"]):
        if which(cmd[0]):
            run(cmd, timeout=8)
            util.ok("locked")
            return 0
    util.warn("no lock command available")
    return 1


def hostname_info(args):
    """Show full hostname/domain info."""
    import socket
    util.kv("Hostname", socket.gethostname())
    try:
        util.kv("FQDN", socket.getfqdn())
    except Exception:
        pass
    return 0


def installed_count(args):
    """Count installed programs (best-effort)."""
    if IS_WINDOWS:
        rc, out, _ = run(["wmic", "product", "get", "Name"], timeout=30)
        n = max(0, len([l for l in out.splitlines() if l.strip()]) - 1)
        util.kv("Installed products", n)
        return 0
    if which("dpkg"):
        rc, out, _ = run(["dpkg", "--get-selections"], timeout=15)
        util.kv("dpkg packages", len(out.splitlines()))
        return 0
    util.warn("no package manager info")
    return 1


COMMANDS = {
    "is-admin": is_admin,
    "current-user": current_user,
    "users-list": users_list,
    "user-info": user_info,
    "groups-list": groups_list,
    "current-privileges": current_privileges,
    "hostname": hostname,
    "hostname-info": hostname_info,
    "firewall-status": firewall_status,
    "firewall-rules-count": firewall_rules_count,
    "hosts-file": hosts_file,
    "services-list": services_list,
    "scheduled-tasks": scheduled_tasks,
    "startup-programs": startup_programs,
    "network-shares": network_shares,
    "password-policy": password_policy,
    "last-boot": last_boot,
    "event-log-tail": event_log_tail,
    "failed-logins": failed_logins,
    "uac-status": uac_status,
    "ssh-keys-list": ssh_keys_list,
    "cron-list": cron_list,
    "sudoers-check": sudoers_check,
    "env-system": env_system,
    "open-ports": open_ports,
    "logged-in": logged_in,
    "disk-permissions": disk_permissions,
    "installed-count": installed_count,
    "reboot": reboot,
    "shutdown": shutdown,
    "lock-screen": lock_screen,
}
