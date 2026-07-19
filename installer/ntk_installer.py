#!/usr/bin/env python3
"""
NTK Installer (Windows) - runs as Administrator.

- Copies the bundled ntk.exe to C:\\Program Files\\NTK
- Adds that folder to the SYSTEM PATH (CMD + PowerShell)
- Registers App Paths + uninstall info in the Registry
- Broadcasts environment change so open shells can pick it up

Built as a standalone .exe with PyInstaller (--uac-admin). The payload
ntk.exe is bundled via --add-data and extracted at runtime.
"""
import os
import sys
import shutil
import ctypes
import subprocess

APP_NAME = "NTK"
INSTALL_DIR = os.path.join(os.environ.get("ProgramFiles", r"C:\Program Files"), "NTK")
EXE_NAME = "ntk.exe"
UPDATER_NAME = "ntk-updater.exe"  # optional, bundled if present


def _c(text, color=""):
    return text


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except Exception:
        return False


def elevate():
    """Relaunch self elevated via UAC."""
    params = " ".join(f'"{a}"' for a in sys.argv[1:])
    rc = ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, params, None, 1)
    return rc > 32


def resource_path(rel):
    """Locate a bundled resource (PyInstaller onefile puts them in _MEIPASS)."""
    base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, rel)


def broadcast_env_change():
    """Tell running processes the environment changed."""
    HWND_BROADCAST = 0xFFFF
    WM_SETTINGCHANGE = 0x1A
    SMTO_ABORTIFHUNG = 0x0002
    res = ctypes.c_long()
    ctypes.windll.user32.SendMessageTimeoutW(
        HWND_BROADCAST, WM_SETTINGCHANGE, 0,
        ctypes.c_wchar_p("Environment"), SMTO_ABORTIFHUNG, 5000,
        ctypes.byref(res))


def add_to_system_path(new_dir):
    """Append new_dir to the SYSTEM (machine) PATH via the Registry."""
    import winreg
    key_path = r"SYSTEM\CurrentControlSet\Control\Session Manager\Environment"
    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0,
                        winreg.KEY_READ | winreg.KEY_WRITE) as key:
        try:
            cur, vtype = winreg.QueryValueEx(key, "Path")
        except FileNotFoundError:
            cur, vtype = "", winreg.REG_EXPAND_SZ
        parts = [p for p in cur.split(";") if p.strip()]
        if any(os.path.normcase(p.rstrip("\\")) == os.path.normcase(new_dir.rstrip("\\"))
               for p in parts):
            return False  # already present
        parts.append(new_dir)
        winreg.SetValueEx(key, "Path", 0, winreg.REG_EXPAND_SZ, ";".join(parts))
    return True


def register_app(exe_path):
    """Register App Paths + uninstall entry in the Registry."""
    import winreg
    # App Paths -> lets 'start ntk' and Run dialog find it
    ap = r"SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\ntk.exe"
    with winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, ap) as k:
        winreg.SetValueEx(k, "", 0, winreg.REG_SZ, exe_path)
        winreg.SetValueEx(k, "Path", 0, winreg.REG_SZ, os.path.dirname(exe_path))
    # Uninstall entry
    un = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\NTK"
    with winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, un) as k:
        winreg.SetValueEx(k, "DisplayName", 0, winreg.REG_SZ, "NTK - Next Tool Kit")
        winreg.SetValueEx(k, "DisplayVersion", 0, winreg.REG_SZ, "1.0.0")
        winreg.SetValueEx(k, "Publisher", 0, winreg.REG_SZ, "finnytech")
        winreg.SetValueEx(k, "InstallLocation", 0, winreg.REG_SZ, os.path.dirname(exe_path))
        winreg.SetValueEx(k, "DisplayIcon", 0, winreg.REG_SZ, exe_path)
        winreg.SetValueEx(k, "NoModify", 0, winreg.REG_DWORD, 1)
        winreg.SetValueEx(k, "NoRepair", 0, winreg.REG_DWORD, 1)
    # Product record
    pr = r"SOFTWARE\NTK"
    with winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, pr) as k:
        winreg.SetValueEx(k, "InstallDir", 0, winreg.REG_SZ, os.path.dirname(exe_path))
        winreg.SetValueEx(k, "Version", 0, winreg.REG_SZ, "1.0.0")


def main():
    print("=" * 52)
    print("   NTK - Next Tool Kit  |  Installer v1.0.0")
    print("=" * 52)
    print()

    if not is_admin():
        print("[i] Administrator rights required - requesting elevation...")
        if elevate():
            return 0
        print("[!] Could not elevate. Right-click -> Run as administrator.")
        input("Press Enter to exit...")
        return 1

    src = resource_path(EXE_NAME)
    if not os.path.exists(src):
        print(f"[!] Bundled {EXE_NAME} not found at {src}")
        input("Press Enter to exit...")
        return 1

    try:
        print(f"[*] Installing to: {INSTALL_DIR}")
        os.makedirs(INSTALL_DIR, exist_ok=True)
        dst = os.path.join(INSTALL_DIR, EXE_NAME)
        shutil.copy2(src, dst)
        print(f"[+] Copied {EXE_NAME}")

        # Bundle the updater too, if it was packaged with the installer
        upd_src = resource_path(UPDATER_NAME)
        if os.path.exists(upd_src):
            shutil.copy2(upd_src, os.path.join(INSTALL_DIR, UPDATER_NAME))
            print(f"[+] Copied {UPDATER_NAME} (run 'ntk-updater' to update later)")

        print("[*] Updating SYSTEM PATH (CMD + PowerShell)...")
        added = add_to_system_path(INSTALL_DIR)
        print("[+] PATH updated" if added else "[=] PATH already contained the folder")

        print("[*] Writing Registry entries...")
        register_app(dst)
        print("[+] Registry: App Paths + Uninstall + Product key written")

        print("[*] Broadcasting environment change...")
        broadcast_env_change()
        print("[+] Done")

        print()
        print("-" * 52)
        print("  NTK installed successfully!")
        print("  Open a NEW terminal (CMD or PowerShell) and run:")
        print("      ntk --help")
        print("      ntk-sys-info")
        print("      ntk crypto password 24")
        print("-" * 52)
        print()
        print("  Note: open shells need a restart to see the new PATH.")
    except PermissionError as e:
        print(f"[!] Permission error: {e}")
        input("Press Enter to exit...")
        return 1
    except Exception as e:
        print(f"[!] Install failed: {e}")
        input("Press Enter to exit...")
        return 1

    input("Press Enter to finish...")
    return 0


if __name__ == "__main__":
    sys.exit(main())
