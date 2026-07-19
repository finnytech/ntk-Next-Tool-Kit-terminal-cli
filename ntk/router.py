"""NTK router: parses `ntk <category> <tool> [args...]` and dispatches to handlers.

Categories are lazy-loaded so startup stays fast even with 300 commands.
"""
import os
import sys
import importlib
from . import util
from .util import col, C

# category key -> (module name, short description)
# v2.0: 33 universal categories, ~30 tools each (~1000 total).
CATEGORIES = {
    "system":       ("v2_system",       "System & OS info/control"),
    "performance":  ("v2_performance",  "Speed up: free RAM, clean disk, CPU/GPU optimize"),
    "network":      ("v2_network",      "Network, DNS, ports & connectivity"),
    "file":         ("v2_file",         "Files & folders"),
    "text":         ("v2_text",         "Text processing"),
    "data":         ("v2_data",         "JSON/CSV/YAML/XML convert & query"),
    "crypto":       ("v2_crypto",       "Hashing & encryption"),
    "security":     ("v2_security",     "Security audit & scanning"),
    "dev":          ("v2_dev",          "Developer workflow"),
    "git":          ("v2_git",          "Git helpers"),
    "web":          ("v2_web",          "Web, HTTP & API"),
    "media":        ("v2_media",        "Media info & simple ops"),
    "docker":       ("v2_docker",       "Docker & containers"),
    "cloud":        ("v2_cloud",        "Cloud & DevOps"),
    "database":     ("v2_database",     "Database tools"),
    "math":         ("v2_math",         "Math, stats & number tools"),
    "time":         ("v2_time",         "Date, time, timers & zones"),
    "convert":      ("v2_convert",      "Units & format conversion"),
    "generate":     ("v2_generate",     "Generators (passwords, UUID, QR, ...)"),
    "monitor":      ("v2_monitor",      "Live system monitors"),
    "benchmark":    ("v2_benchmark",    "Speed benchmarks"),
    "disk":         ("v2_disk",         "Disk & storage analysis"),
    "process":      ("v2_process",      "Process management"),
    "search":       ("v2_search",       "Search files, text & web"),
    "archive":      ("v2_archive",      "Archives & backups"),
    "image":        ("v2_image",        "Image editing"),
    "audio":        ("v2_audio",        "Audio tools"),
    "code":         ("v2_code",         "Code analysis & formatting"),
    "api":          ("v2_api",          "API testing & clients"),
    "os":           ("v2_os",           "OS settings, services & tasks"),
    "hardware":     ("v2_hardware",     "Hardware & sensors"),
    "productivity": ("v2_productivity", "Notes, todo, calc & fun"),
    "admin":        ("v2_admin",        "Admin: users, firewall, tasks"),
}

# Backward-compatible aliases from v1 category names.
ALIASES = {
    "sys": "system", "net": "network", "sec": "security",
    "db": "database", "util": "productivity", "format": "data",
    "auto": "productivity", "ai": "dev",
}

BANNER = r"""
   _   _ _____ _  __
  | \ | |_   _| |/ /   Next Tool Kit
  |  \| | | | | ' /    1000+ tools, one CLI
  | |\  | | | | . \    Win10 / Win11 / Linux - CMD, PowerShell & bash
  |_| \_| |_| |_|\_\
"""


ISSUES_URL = "https://github.com/finnytech/ntk-Next-Tool-Kit-terminal-cli/issues"


def _load(cat):
    mod_name = CATEGORIES[cat][0]
    return importlib.import_module(f".{mod_name}", package="ntk")


def _print_json_commands():
    """Emit the full command catalog as JSON (used by the manager UI)."""
    import json
    data = {}
    for cat, (mod, desc) in CATEGORIES.items():
        try:
            m = _load(cat)
            cmds = getattr(m, "COMMANDS", {})
            tools = {}
            for name, fn in cmds.items():
                doc = (fn.__doc__ or "").strip()
                tools[name] = doc.splitlines()[0] if doc else ""
            data[cat] = {"desc": desc, "tools": tools}
        except Exception:
            data[cat] = {"desc": desc, "tools": {}}
    print(json.dumps(data))
    return 0


def _run_uninstall(rest):
    """Uninstall NTK from this system."""
    try:
        import os as _os
        import sys as _sys
        _sys.path.insert(0, _os.path.join(_os.path.dirname(__file__), "..", "installer"))
        try:
            from installer import ntk_uninstall as un  # source layout
        except Exception:
            import ntk_uninstall as un  # bundled/flat layout
        purge = "--purge" in rest or "--all" in rest
        util.info("Uninstalling NTK...")
        un.uninstall(purge_user_data=purge)
        util.ok("NTK uninstalled. Open a new terminal.")
        return 0
    except Exception as e:
        util.err(f"uninstall failed: {e}")
        print(col("Tip: run the standalone ntk-uninstall(.exe) as Administrator.", C.DIM))
        return 1


def _run_updater(rest):
    """Launch the updater to pull the latest release."""
    import shutil as _sh
    import subprocess as _sp
    name = "ntk-updater.exe" if util.IS_WINDOWS else "ntk-updater"
    exe = _sh.which(name) or _sh.which("ntk-updater")
    if not exe:
        # look next to the running ntk
        here = os.path.dirname(os.path.abspath(sys.executable if getattr(sys, "frozen", False) else __file__))
        cand = os.path.join(here, name)
        exe = cand if os.path.exists(cand) else None
    if not exe:
        util.err("updater not found. Download ntk-updater from the releases page.")
        return 1
    try:
        return _sp.call([exe] + list(rest))
    except Exception as e:
        util.err(f"could not run updater: {e}")
        return 1


def print_top_help():
    from . import __version__
    print(col(BANNER, C.CYAN))
    print(col(f"  ntk v{__version__}", C.DIM) + col("  -  https://github.com/finnytech/ntk", C.GRAY))
    print()
    print(col("Usage:", C.BOLD) + " ntk <category> <tool> [args...]")
    print()
    print(col("Categories:", C.BOLD))
    for key, (_, desc) in CATEGORIES.items():
        print(f"  {col(key.ljust(12), C.CYAN)} {desc}")
    print()
    print(col("Examples:", C.BOLD))
    print("  ntk sys info")
    print("  ntk net ping google.com")
    print("  ntk crypto password 24")
    print("  ntk util calc \"2*(3+4)\"")
    print()
    print(col("Help:", C.BOLD) + " ntk <category>            list a category's tools")
    print("       ntk <category> <tool> -h  tool help")


def print_category_help(cat):
    if cat in ALIASES:
        cat = ALIASES[cat]
    mod = _load(cat)
    cmds = getattr(mod, "COMMANDS", {})
    util.header(f"ntk {cat}  -  {CATEGORIES[cat][1]}")
    rows = []
    for name in sorted(cmds):
        fn = cmds[name]
        doc = (fn.__doc__ or "").strip().splitlines()
        desc = doc[0] if doc else ""
        rows.append((name, desc))
    util.table(rows, headers=["tool", "description"])
    print()
    print(col(f"Run: ntk {cat} <tool> [args]", C.DIM))


def dispatch(argv):
    if not argv or argv[0] in ("-h", "--help", "help"):
        print_top_help()
        return 0
    if argv[0] in ("-v", "--version", "version"):
        from . import __version__
        print(f"ntk {__version__}")
        return 0
    if argv[0] == "--json-commands":
        return _print_json_commands()
    if argv[0] in ("uninstall", "--uninstall"):
        return _run_uninstall(argv[1:])
    if argv[0] in ("update", "--update", "upgrade"):
        return _run_updater(argv[1:])

    cat = argv[0].lower()
    if cat in ALIASES:
        cat = ALIASES[cat]
    if cat not in CATEGORIES:
        util.err(f"unknown category: {cat}")
        print(col("Run 'ntk --help' to see categories.", C.DIM))
        return 2

    if len(argv) == 1:
        print_category_help(cat)
        return 0

    tool = argv[1].lower()
    rest = argv[2:]

    try:
        mod = _load(cat)
    except Exception as e:  # pragma: no cover
        util.err(f"failed to load category '{cat}': {e}")
        return 1

    cmds = getattr(mod, "COMMANDS", {})
    if tool in ("-h", "--help", "help"):
        print_category_help(cat)
        return 0
    if tool not in cmds:
        util.err(f"unknown tool: ntk {cat} {tool}")
        print(col(f"Run 'ntk {cat}' to list tools.", C.DIM))
        return 2

    fn = cmds[tool]

    # Centralized per-tool help: intercept -h/--help BEFORE the tool tries to
    # parse it as an argument (prevents ugly 'invalid literal'/'unknown url' errors).
    if rest and rest[0] in ("-h", "--help"):
        doc = (fn.__doc__ or "").strip()
        desc = doc.splitlines()[0] if doc else ""
        util.header(f"ntk {cat} {tool}")
        if desc:
            print("  " + desc)
        if len(doc.splitlines()) > 1:
            print()
            print("\n".join("  " + ln for ln in doc.splitlines()[1:]))
        print()
        print(col(f"Usage: ntk {cat} {tool} [args...]   (or: ntk-{cat}-{tool} ...)", C.DIM))
        return 0

    try:
        rc = fn(rest)
        return rc if isinstance(rc, int) else 0
    except KeyboardInterrupt:
        print()
        return 130
    except (EOFError, BrokenPipeError):
        return 0
    except (FileNotFoundError, IsADirectoryError, NotADirectoryError) as e:
        util.err(f"{cat} {tool}: file/path not found or invalid: {getattr(e, 'filename', e)}")
        print(col(f"Try: ntk {cat} {tool} -h", C.DIM))
        return 1
    except PermissionError as e:
        util.err(f"{cat} {tool}: permission denied: {getattr(e, 'filename', e)}")
        print(col("Tip: run the terminal as Administrator/root if this needs elevated access.", C.DIM))
        return 1
    except (ValueError, TypeError) as e:
        util.err(f"{cat} {tool}: invalid argument: {e}")
        print(col(f"Try: ntk {cat} {tool} -h", C.DIM))
        return 2
    except (OSError,) as e:
        # network/socket/address errors, ports in use, etc.
        util.err(f"{cat} {tool}: {e}")
        return 1
    except Exception as e:
        util.err(f"{cat} {tool}: {type(e).__name__}: {e}")
        print(col(f"This looks like a bug. Please report it: {ISSUES_URL}", C.DIM))
        return 1


def _expand_hyphen_form(argv):
    """Support `ntk-sys-info` / `ntk sys-info` style: split a leading hyphenated
    token into category + tool so `ntk-<cat>-<tool>` works like `ntk <cat> <tool>`.
    """
    if not argv:
        return argv
    first = argv[0]
    # strip a leading 'ntk-' if the launcher passed the whole thing through
    if first.lower().startswith("ntk-"):
        first = first[4:]
    # If the first token itself contains a category prefix like 'sys-info'
    if "-" in first:
        head = first.split("-", 1)[0].lower()
        if head in CATEGORIES or head in ALIASES:
            cat, tool = first.split("-", 1)
            return [cat, tool] + list(argv[1:])
    return argv


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    try:
        argv = _expand_hyphen_form(argv)
        return dispatch(argv)
    except KeyboardInterrupt:
        print()
        return 130
    except (BrokenPipeError, EOFError):
        return 0
    except Exception as e:
        # Absolute last line of defense: never show a raw traceback to a user.
        try:
            util.err(f"unexpected error: {type(e).__name__}: {e}")
            print(col(f"Please report this: {ISSUES_URL}", C.DIM))
        except Exception:
            sys.stderr.write(f"ntk: unexpected error: {e}\n")
        return 1
