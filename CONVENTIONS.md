# NTK command module conventions (READ FIRST)

All command modules live in `ntk-build/ntk/cmd_<category>.py`.

## Structure of every module
```python
"""<Category> tools (ntk <cat> ...)."""
import ...
from . import util
from .util import col, C, run, IS_WINDOWS

def toolname(args):
    """One-line description (shown in help)."""
    # args is a list[str] of everything after `ntk <cat> <tool>`
    ...
    return 0  # 0 = success, non-zero = error

COMMANDS = {
    "tool-name": toolname,   # dict key = CLI name (may contain hyphens)
    ...
}
```

## Rules
- Pure Python standard library first. Optional deps allowed: `psutil`, `requests`, `PIL` (Pillow).
  For optional deps, import in a try/except and if missing print `util.warn("needs X: pip install X")` and `return 1`.
- Cross-platform: must work on Windows 10/11 (primary), degrade gracefully on Linux.
- Never call `sys.exit()`. Return an int.
- Use `util.header(title)`, `util.kv(k,v)`, `util.table(rows, headers=[...])`,
  `util.ok/err/warn/info`, `util.bar(fraction)`, `util.human_bytes(n)`,
  `util.run(cmd_list) -> (rc, stdout, stderr)`, `util.which(name)`.
- Validate args; on bad usage print `util.err("usage: ntk <cat> <tool> ...")` and `return 2`.
- Keep each tool small and genuinely functional. No placeholder "not implemented".
- The first line of the docstring is the help description; keep it under ~60 chars.

## Colors
`col(text, C.CYAN)` etc. C has RED/GREEN/YELLOW/BLUE/MAGENTA/CYAN/GRAY/BOLD/DIM/RESET.

Every tool listed in the spec MUST appear as a key in COMMANDS with a working function.
