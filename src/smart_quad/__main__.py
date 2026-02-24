"""
Package entry point.

This file is executed when you run:
    python -m smart_quad

Think of it as the "front door" of the package.
It should be tiny: parse CLI args (later), call the app runner, exit with a code.
"""

from __future__ import annotations

import sys
from smart_quad.app import run

def main(argv: list[str] | None = None) -> int:
    if argv is None:
        argv = sys.argv[1:]

    try:
        run()
        return 0
    except Exception as exc:
        print(f"[smart_quad] ERROR: {exc}", file = sys.stderr)
        return 1

if __name__ == "__main__":
    raise SystemExit(main())
