#!/usr/bin/env python3
"""Plant the defect: ties round toward +infinity instead of away from zero.

Chosen for HEADROOM. It differs from the spec at negative ties and NOWHERE
else, so:

    5/2  -> 3   both      (positive tie: unchanged)
   -5/2  -> -2  planted, spec says -3
    7/3  -> 2   both      (non-tie: unchanged)

A harness that exercises positive ties and non-ties passes it. Catching it
requires testing a NEGATIVE tie, which is the discipline step the docstring
invites ("and -5/2 -> -3") and which a merely competent suite can skip.

The previous fixture's plant (half-even) differed at EVERY tie, which any
tie-aware suite catches -- no headroom for the instruction to matter.
"""
import pathlib
import sys

SRC = "    if 2 * rest >= denominator:\n        whole += 1\n    return -whole if negative else whole"
DST = ("    if 2 * rest >= denominator:\n"
       "        whole += 1\n"
       "    if negative and 2 * rest == denominator:\n"
       "        whole -= 1        # PLANTED: ties go toward +inf, not away from zero\n"
       "    return -whole if negative else whole")

p = pathlib.Path(sys.argv[1])
s = p.read_text()
assert SRC in s, "subject does not match the expected source"
p.write_text(s.replace(SRC, DST, 1))
