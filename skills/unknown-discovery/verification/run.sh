#!/bin/sh
# Verification run for the `unknown-discovery` skill: exercises the prescribed
# quantitative methods on cases with known answers.
#
#   1. value-of-information / EVPI on a two-action decision                 (bc)
#   2. calibration: calibrated Brier -> p(1-p) floor, overconfident worse   (py)
#   3. competing hypotheses: diagnostic vs non-diagnostic evidence          (py)
#   4. residual analysis: a hidden regime shift the aggregate mean hides    (py)
#   5. triage score P = I*U*(1-R)*D: monotonicity + component retention     (py)
set -e
cd "$(dirname "$0")"

echo "=== 1. value of information / EVPI (bc) ==="
# `bc`'s `quit` ALWAYS exits 0, so neither $? nor `set -e` can catch a failed
# check -- the OUTPUT must be inspected.  Both conditions below are needed:
# the banner alone would be satisfied by a file that never reached its later
# sections, the absence of FAIL alone by one that crashed before printing.
# See docs/bc-verification-audit.md.
bcout=$(bc -q -l checks.bc)
printf '%s\n' "$bcout"
if ! printf '%s\n' "$bcout" | grep -q "ALL BC CHECKS PASSED" \
   || printf '%s\n' "$bcout" | grep -qF '*** FAIL'; then
    echo "bc checks FAILED" >&2
    exit 1
fi
echo

echo "=== 2-5. method checks (python, stdlib only) ==="
python3 discovery.py
