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
bc -q -l checks.bc
echo

echo "=== 2-5. method checks (python, stdlib only) ==="
python3 discovery.py
