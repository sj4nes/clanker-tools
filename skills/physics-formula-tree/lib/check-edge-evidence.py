#!/usr/bin/env python3
"""Re-export of the canonical edge-evidence check, so physics and chemistry
capsules point at their own method skill's lib/.
Canonical source: skills/math-theorem-tree/lib/check-edge-evidence.py"""
import os
_here = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(_here, "..", "..", "math-theorem-tree", "lib", "check-edge-evidence.py")).read())
