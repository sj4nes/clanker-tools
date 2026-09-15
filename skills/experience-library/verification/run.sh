#!/bin/sh
# Verification run for the `experience-library` skill: exercises the
# prescribed workflow on library dynamics whose true answer is known by
# construction, and confirms each prescribed check behaves as claimed.
#
#   1. exact arithmetic (bc): the coverage/retrieval drift curve and its
#      interior optimum (found by scan AND by the analytic crossover), the
#      over-retirement ordering, the paired-vs-unpaired variance ratio, and
#      the retention/activation/execution decomposition
#   2. Monte Carlo (python, stdlib only): the drift curve DRAWN rather than
#      computed (independent oracle), the three retention policies, the
#      admission gate on a useless-but-appealing candidate, and paired vs
#      unpaired power at an identical task budget
set -e
cd "$(dirname "$0")"
PY=python3

echo "=== 1. exact arithmetic (bc) ==="
# `bc`'s exit status reports INTERPRETER errors (2 syntax, 3 undefined function,
# 4 missing file, 1 math error), NOT whether your claims were true -- a false
# claim is a VALUE to a calculator, not an error, and `quit` takes no status.
# So `set -e` catches a broken file but never a wrong answer.  Inspect the OUTPUT.
bcout=$(bc -lq checks.bc 2>&1) && bcstatus=0 || bcstatus=$?
printf '%s\n' "$bcout"
if [ "$bcstatus" -ne 0 ] \
   || ! printf '%s\n' "$bcout" | grep -q "ALL BC CHECKS PASSED" \
   || printf '%s\n' "$bcout" | grep -qF '*** FAIL'; then   # -F is load-bearing
    echo "bc checks FAILED (exit status $bcstatus)" >&2; exit 1
fi
echo

echo "=== 2. Monte Carlo (python, stdlib only) ==="
$PY librarysim.py
