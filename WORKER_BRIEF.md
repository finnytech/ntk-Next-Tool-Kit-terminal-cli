# NTK v2 Worker Brief — build category modules

You are building command modules for the NTK CLI. Work in the workspace at
`/home/openclaw/.openclaw/workspace/ntk-build/`. Write each module as
`ntk/v2_<category>.py`.

## HARD REQUIREMENTS (must follow exactly)
1. Each module starts with a docstring and these imports:
   ```python
   """<Category> tools (ntk <cat> ...)."""
   import os, sys, ...   # only what you use
   from . import util
   from .util import col, C, run, which, IS_WINDOWS, human_bytes
   ```
2. Each tool is a function `def toolname(args):` where `args` is `list[str]`
   (everything after `ntk <cat> <tool>`). First docstring line = help text (<60 chars).
   Return an int (0 = ok, non-zero = error). NEVER call sys.exit().
3. End each module with a `COMMANDS = { "hyphen-name": func, ... }` dict.
4. **EACH module must have AT LEAST 30 tools** that are genuinely functional.
5. Cross-platform: branch on `util.IS_WINDOWS`. Degrade gracefully on the other OS
   (print `util.warn(...)` + `return 1`, never crash).
6. Optional deps (`psutil`, `requests`, `PIL`) MUST be imported inside try/except;
   if missing: `util.warn("needs X: pip install X"); return 1`.
7. Validate args: on bad usage `util.err("usage: ntk <cat> <tool> ..."); return 2`.
8. Destructive actions (delete/kill/overwrite) require a `--yes`/`-y` flag OR an
   interactive confirm; SAFE by default. Never touch personal user files.
9. Do NOT block forever: interactive/TTY tools must check `sys.stdin.isatty()` and
   bail with return 2 if not a TTY. No infinite loops without Ctrl+C handling.
10. Use util helpers for output: `util.header/kv/table/ok/err/warn/info/bar`.

## Helpers available (ntk/util.py)
- `util.header(title)`, `util.kv(key,value)`, `util.table(rows, headers=[...])`
- `util.ok/err/warn/info(msg)`, `util.bar(fraction)`, `util.human_bytes(n)`
- `util.run(cmd_list, timeout=..) -> (rc, stdout, stderr)`  (never raises)
- `util.which(name)`, `util.IS_WINDOWS`, colors via `col(text, C.CYAN)`

## Quality bar
- Real, useful tools. No "not implemented" stubs. No duplicate logic across tools
  in the same module (each does something distinct).
- Keep functions small. Prefer stdlib. Wrap external CLIs (git, docker, ffmpeg, aws,
  kubectl) with `util.run` and a graceful "install X" message when `which(X)` is None.

## Validate before finishing
Run in the venv:
```
cd /home/openclaw/.openclaw/workspace/ntk-build && . .venv/bin/activate
PYTHONPATH=. python -c "import ntk.v2_<cat> as m; print('<cat>', len(m.COMMANDS))"
```
Every module must import cleanly and report >=30 tools.
