#!/usr/bin/env python3
"""
NTK Uninstaller (Windows) - runs as Administrator.

Cleanly removes everything the installer added:
- Removes C:\\Program Files\\NTK from the SYSTEM PATH
- Deletes App Paths + Uninstall + Product registry keys
- Deletes the C:\\Program Files\\NTK folder (schedules self-delete if running from there)
- Broadcasts environment change so open shells update

Also importable: `from ntk_uninstall import uninstall` and used by the
`ntk uninstall` CLI command (cross-platform).

Built standalone with PyInstaller (--uac-admin).
"""
import os
import sys
import shutil
import ctypes
import subprocess

APP_NAME = "NTK"
INSTALL_DIR = os.path.join(os.environ.get("ProgramFiles", r"C:\Program Files"), "NTK")


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except Exception:
        return False


def elevate():
    params = " ".join(f'"{a}"' for a in sys.argv[1:])
    rc = ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, params, None, 1)
    return rc > 32


def broadcast_env_change():
    HWND_BROADCAST = 0xFFFF
    WM_SETTINGCHANGE = 0x1A
    SMTO_ABORTIFHUNG = 0x0002
    res = ctypes.c_long()
    ctypes.windll.user32.SendMessageTimeoutW(
        HWND_BROADCAST, WM_SETTINGCHANGE, 0,
        ctypes.c_wchar_p("Environment"), SMTO_ABORTIFHUNG, 5000,
        ctypes.byref(res))


def remove_from_system_path(target_dir):
    """Remove target_dir from the SYSTEM PATH. Returns True if changed."""
    import winreg
    key_path = r"SYSTEM\CurrentControlSet\Control\Session Manager\Environment"
    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0,
                        winreg.KEY_READ | winreg.KEY_WRITE) as key:
        try:
            cur, _ = winreg.QueryValueEx(key, "Path")
        except FileNotFoundError:
            return False
        parts = [p for p in cur.split(";") if p.strip()]
        norm = os.path.normcase(target_dir.rstrip("\\"))
        new_parts = [p for p in parts if os.path.normcase(p.rstrip("\\")) != norm]
        if len(new_parts) == len(parts):
            return False
        winreg.SetValueEx(key, "Path", 0, winreg.REG_EXPAND_SZ, ";".join(new_parts))
    return True


def _del_key_tree(root, path):
    import winreg
    try:
        winreg.DeleteKey(root, path)
        return True
    except FileNotFoundError:
        return False
    except OSError:
        # key has subkeys; delete them first
        try:
            with winreg.OpenKey(root, path, 0, winreg.KEY_ALL_ACCESS) as k:
                while True:
                    try:
                        sub = winreg.EnumKey(k, 0)
                    except OSError:
                        break
                    _del_key_tree(root, path + "\\" + sub)
            winreg.DeleteKey(root, path)
            return True
        except Exception:
            return False


def unregister_app():
    import winreg
    removed = []
    for path in (
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\ntk.exe",
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\NTK",
        r"SOFTWARE\NTK",
    ):
        if _del_key_tree(winreg.HKEY_LOCAL_MACHINE, path):
            removed.append(path)
    return removed


def _schedule_dir_delete(path):
    """Delete a folder; if a file is locked (we're running from it), schedule via cmd."""
    try:
        shutil.rmtree(path, ignore_errors=False)
        return True
    except Exception:
        # Fallback: spawn a detached cmd that waits then removes the dir.
        try:
            subprocess.Popen(
                ["cmd", "/c", "ping 127.0.0.1 -n 3 >nul & rmdir /s /q \"%s\"" % path],
                creationflags=0x00000008 | 0x00000200,  # DETACHED | NEW_PROCESS_GROUP
            )
            return "scheduled"
        except Exception:
            return False


def uninstall(purge_user_data=False, quiet=False):
    """Cross-platform uninstall core. Returns dict of actions."""
    log = (lambda *a: None) if quiet else print
    actions = {}
    if os.name == "nt":
        try:
            actions["path"] = remove_from_system_path(INSTALL_DIR)
            log("[+] Removed from SYSTEM PATH" if actions["path"] else "[=] PATH entry not present")
        except Exception as e:
            log(f"[!] PATH removal failed: {e}")
        try:
            removed = unregister_app()
            actions["registry"] = removed
            log(f"[+] Removed {len(removed)} registry key(s)")
        except Exception as e:
            log(f"[!] Registry cleanup failed: {e}")
        try:
            if os.path.isdir(INSTALL_DIR):
                r = _schedule_dir_delete(INSTALL_DIR)
                actions["files"] = r
                if r == "scheduled":
                    log("[+] Install folder will be removed in a moment.")
                elif r:
                    log("[+] Removed install folder")
                else:
                    log("[!] Could not remove install folder (locked). Delete manually: " + INSTALL_DIR)
            else:
                log("[=] Install folder already gone")
        except Exception as e:
            log(f"[!] Folder removal failed: {e}")
        try:
            broadcast_env_change()
        except Exception:
            pass
    else:
        # Linux/mac: remove the binary from common locations
        removed = []
        for cand in ("/usr/local/bin/ntk", os.path.expanduser("~/.local/bin/ntk")):
            if os.path.exists(cand):
                try:
                    os.remove(cand)
                    removed.append(cand)
                    log(f"[+] Removed {cand}")
                except PermissionError:
                    log(f"[!] Need sudo to remove {cand}")
        actions["files"] = removed

    if purge_user_data:
        data = os.path.expanduser("~/.ntk")
        if os.path.isdir(data):
            shutil.rmtree(data, ignore_errors=True)
            actions["user_data"] = True
            log("[+] Removed ~/.ntk user data")
    return actions


def main():
    print("=" * 52)
    print("   NTK - Next Tool Kit  |  Uninstaller")
    print("=" * 52)
    print()

    purge = "--purge" in sys.argv or "--all" in sys.argv
    assume_yes = "--yes" in sys.argv or "-y" in sys.argv

    if os.name == "nt" and not is_admin():
        print("[i] Administrator rights required - requesting elevation...")
        if elevate():
            return 0
        print("[!] Could not elevate. Right-click -> Run as administrator.")
        input("Press Enter to exit...")
        return 1

    if not assume_yes:
        try:
            ans = input("This will remove NTK from this system. Continue? [y/N] ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print()
            return 1
        if ans not in ("y", "yes"):
            print("Cancelled.")
            return 0

    print("[*] Uninstalling NTK...")
    uninstall(purge_user_data=purge)
    print()
    print("-" * 52)
    print("  NTK has been uninstalled.")
    print("  Open a new terminal; 'ntk' should no longer be found.")
    if not purge:
        print("  (User notes/todos in ~/.ntk kept. Use --purge to remove them.)")
    print("-" * 52)
    if os.name == "nt":
        input("Press Enter to finish...")
    return 0


if __name__ == "__main__":
    sys.exit(main())
