#!/usr/bin/env python3
"""Re-export of the canonical Lean-core check.
Canonical source: skills/math-theorem-tree/lib/check-lean-cores.py"""
import os
_here = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(_here, "..", "..", "math-theorem-tree", "lib", "check-lean-cores.py")).read())
