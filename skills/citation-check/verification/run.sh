#!/bin/sh
# Verification run for the `citation-check` skill.
#
# The skill is methodology-only (no bespoke CLI), so verification means:
# exercise the prescribed workflow end-to-end against the REAL authoritative
# APIs on a battery of citations with known ground truth -- real, real-but-
# misstated, and deliberately broken -- and confirm each prescribed status,
# ladder, and API access pattern behaves as documented.
#
#   citecheck.py -- a minimal implementation of the SKILL.md pipeline
#   (parse/normalize -> route -> retrieve -> score -> calibrated status).
#
# Needs network. Tooling: Python 3 stdlib only. ~60-90 s wall (rate-limited).
set -e
cd "$(dirname "$0")"
python3 citecheck.py
