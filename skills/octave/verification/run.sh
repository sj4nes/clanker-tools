#!/bin/sh
# Verification run for the `octave` skill.
#
# Re-solves real math-linear-algebra claims with the method SKILL.md prescribes
# (independent routes, derived tolerances, n large enough to have content) and
# asserts each, including the negative contrasts that must fail.
#
# Unlike the `bc` harnesses in this repo, NO output-grepping protocol is needed:
# Octave exits 1 on a failed assert or an uncaught error, so `set -e` is
# sufficient. That is the one place Octave is strictly better than bc as a check
# runner -- see docs/bc-verification-audit.md for why bc needs the grep.
#
# NEGATIVE-CONTRAST TESTED: corrupting any asserted value makes this exit 1.
set -e
cd "$(dirname "$0")"

command -v octave >/dev/null || { echo "FAIL: octave not on PATH"; exit 1; }

echo "=== math-linear-algebra claims, verified numerically (octave) ==="
octave --no-gui --quiet checks.m
echo
echo "ALL CHECKS PASS"
