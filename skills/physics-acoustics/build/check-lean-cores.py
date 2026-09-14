#!/usr/bin/env python3
"""Thin shim -> shared implementation in the physics-formula-tree skill.
Canonical source: skills/math-theorem-tree/lib/check-lean-cores.py"""
import os, sys
here = os.path.dirname(os.path.abspath(__file__))
sys.argv = [sys.argv[0], os.path.dirname(here)] + sys.argv[1:]
exec(open(os.path.join(here, "..", "..", "physics-formula-tree", "lib", "check-lean-cores.py")).read())
