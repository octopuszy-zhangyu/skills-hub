#!/usr/bin/env python3
"""
ctyun PPT Replicator - Environment Validator

Check that the bundled skill can run its Python-based PPT generation helpers.

Usage:
    python scripts/validate_environment.py

Examples:
    python scripts/validate_environment.py

Dependencies:
    Pillow, python-pptx
"""

from __future__ import annotations

import importlib.util
import sys


REQUIRED_MODULES = {
    "PIL": "Pillow",
    "pptx": "python-pptx",
}


def main() -> int:
    missing = []
    for module_name, package_name in REQUIRED_MODULES.items():
        if importlib.util.find_spec(module_name) is None:
            missing.append(package_name)

    print(f"Python: {sys.version.split()[0]}")
    if missing:
        print("Missing packages: " + ", ".join(missing), file=sys.stderr)
        print("Install with: python -m pip install -r requirements.txt", file=sys.stderr)
        return 1

    print("Environment OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
