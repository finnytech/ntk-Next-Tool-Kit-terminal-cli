#!/usr/bin/env python3
"""PyInstaller entry point for the standalone `ntk` executable.

The launcher accepts both spellings:
    ntk sys info
    ntk-sys-info        (when the shim passes 'ntk-sys-info' as argv[0]-like token)
    ntk sys-info
"""
import sys

# Ensure the bundled package is importable when frozen
try:
    from ntk.router import main
except Exception:
    import os
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from ntk.router import main


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
