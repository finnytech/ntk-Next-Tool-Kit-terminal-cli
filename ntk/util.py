"""Shared helpers for NTK commands: colored output, tables, formatting, safe subprocess."""
import os
import sys
import shutil
import subprocess

# ---- ANSI color support (auto-enable on Windows 10+ terminals) ----
_COLOR = True


def _enable_windows_ansi():
    if os.name != "nt":
        return
    try:
        import ctypes
        kernel32 = ctypes.windll.kernel32
        # ENABLE_VIRTUAL_TERMINAL_PROCESSING = 0x0004
        for handle_id in (-11, -12):  # stdout, stderr
            handle = kernel32.GetStdHandle(handle_id)
            mode = ctypes.c_uint32()
            if kernel32.GetConsoleMode(handle, ctypes.byref(mode)):
                kernel32.SetConsoleMode(handle, mode.value | 0x0004)
    except Exception:
        pass


_enable_windows_ansi()

if os.environ.get("NO_COLOR") or not sys.stdout.isatty():
    _COLOR = False


class C:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    GRAY = "\033[90m"


def col(text, color):
    if not _COLOR:
        return str(text)
    return f"{color}{text}{C.RESET}"


def ok(msg):
    print(col("[OK] ", C.GREEN) + str(msg))


def err(msg):
    print(col("[ERR] ", C.RED) + str(msg), file=sys.stderr)


def warn(msg):
    print(col("[!] ", C.YELLOW) + str(msg))


def info(msg):
    print(col("[i] ", C.CYAN) + str(msg))


def header(title):
    line = "-" * max(4, len(title) + 4)
    print(col(line, C.GRAY))
    print(col("  " + title, C.BOLD + C.CYAN))
    print(col(line, C.GRAY))


def kv(key, value, width=18):
    print(f"  {col(str(key).ljust(width), C.CYAN)} {value}")


def table(rows, headers=None):
    """Simple auto-sized text table. rows = list of tuples/lists."""
    rows = [[str(c) for c in r] for r in rows]
    if not rows and not headers:
        return
    ncols = len(headers) if headers else (len(rows[0]) if rows else 0)
    widths = [0] * ncols
    all_rows = ([list(map(str, headers))] if headers else []) + rows
    for r in all_rows:
        for i in range(min(ncols, len(r))):
            widths[i] = max(widths[i], len(str(r[i])))
    if headers:
        line = "  " + "  ".join(col(str(h).ljust(widths[i]), C.BOLD + C.CYAN) for i, h in enumerate(headers))
        print(line)
        print("  " + "  ".join(col("-" * widths[i], C.GRAY) for i in range(ncols)))
    for r in rows:
        cells = []
        for i in range(ncols):
            v = r[i] if i < len(r) else ""
            cells.append(str(v).ljust(widths[i]))
        print("  " + "  ".join(cells))


def run(cmd, shell=False, timeout=None, check=False):
    """Run a subprocess and return (rc, stdout, stderr)."""
    try:
        p = subprocess.run(
            cmd, shell=shell, timeout=timeout,
            capture_output=True, text=True, encoding="utf-8", errors="replace",
        )
        if check and p.returncode != 0:
            raise subprocess.CalledProcessError(p.returncode, cmd, p.stdout, p.stderr)
        return p.returncode, p.stdout or "", p.stderr or ""
    except FileNotFoundError:
        return 127, "", f"command not found: {cmd if isinstance(cmd, str) else cmd[0]}"
    except subprocess.TimeoutExpired:
        return 124, "", "timeout"


def which(name):
    return shutil.which(name)


def human_bytes(n):
    n = float(n)
    for unit in ["B", "KB", "MB", "GB", "TB", "PB"]:
        if abs(n) < 1024.0:
            return f"{n:3.1f} {unit}"
        n /= 1024.0
    return f"{n:.1f} EB"


def bar(fraction, width=30):
    fraction = max(0.0, min(1.0, fraction))
    filled = int(round(fraction * width))
    color = C.GREEN if fraction < 0.7 else (C.YELLOW if fraction < 0.9 else C.RED)
    return col("█" * filled, color) + col("░" * (width - filled), C.GRAY)


def need(module_name, pip_name=None):
    """Try import an optional dependency; return module or None with a friendly note."""
    try:
        return __import__(module_name)
    except ImportError:
        return None


IS_WINDOWS = os.name == "nt"
