"""NTK router: parses `ntk <category> <tool> [args...]` and dispatches to handlers.

Categories are lazy-loaded so startup stays fast even with 300 commands.
"""
import sys
import importlib
from . import util
from .util import col, C

# category key -> (module name, short description)
CATEGORIES = {
    "sys":    ("cmd_sys",    "System & OS monitoring/control"),
    "net":    ("cmd_net",    "Network & HTTP tools"),
    "file":   ("cmd_file",   "Filesystem & storage"),
    "text":   ("cmd_text",   "Text & data processing"),
    "format": ("cmd_text",   "Text/data formatters (alias of text)"),
    "crypto": ("cmd_crypto", "Cryptography & security"),
    "dev":    ("cmd_dev",    "Developer workflow & IDE utils"),
    "auto":   ("cmd_auto",   "Automation & helpers"),
    "docker": ("cmd_docker", "Docker & containers"),
    "db":     ("cmd_db",     "Database tools"),
    "web":    ("cmd_web",    "Advanced web & API tools"),
    "media":  ("cmd_media",  "Media & asset tools"),
    "ai":     ("cmd_ai",     "AI & LLM integrations"),
    "sec":    ("cmd_sec",    "System security & audit"),
    "cloud":  ("cmd_cloud",  "DevOps & cloud management"),
    "util":   ("cmd_util",   "General utilities & terminal games"),
}

BANNER = r"""
   _   _ _____ _  __
  | \ | |_   _| |/ /   Next Tool Kit
  |  \| | | | | ' /    300 tools, one CLI
  | |\  | | | | . \    Win10 / Win11 - CMD & PowerShell
  |_| \_| |_| |_|\_\
"""


ISSUES_URL = "https://github.com/finnytech/ntk-Next-Tool-Kit-terminal-cli/issues"


def _load(cat):
    mod_name = CATEGORIES[cat][0]
    return importlib.import_module(f".{mod_name}", package="ntk")


def print_top_help():
    from . import __version__
    print(col(BANNER, C.CYAN))
    print(col(f"  ntk v{__version__}", C.DIM) + col("  -  https://github.com/finnytech/ntk", C.GRAY))
    print()
    print(col("Usage:", C.BOLD) + " ntk <category> <tool> [args...]")
    print()
    print(col("Categories:", C.BOLD))
    for key, (_, desc) in CATEGORIES.items():
        if key == "format":
            continue
        print(f"  {col(key.ljust(8), C.CYAN)} {desc}")
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

    cat = argv[0].lower()
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
        if head in CATEGORIES:
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
