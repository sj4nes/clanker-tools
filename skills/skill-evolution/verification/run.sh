#!/bin/sh
# Verification run for the `skill-evolution` skill: re-computes the 4-round
# worked example from references/optimization-loop.md and confirms each
# prescribed mechanism behaves as claimed, including the negative contrasts
# the guardrails exist to prevent.
#
#   1. volatility EMA + edit budget: a volatile round shrinks the next
#      budget below b_base, the EMA keeps it suppressed for a calm round,
#      then it recovers                                            (bc)
#   2. acceptance gate: a candidate whose mean improves but whose
#      protected metric regresses is rejected; a flat primary carried
#      by an auxiliary target is accepted                          (py)
#   3. issue-tracker update: a recurring failure links to its existing
#      entry and is marked reopened, not duplicated                (py)
#   4. rejected-candidate log: a re-proposed dead-end patch is caught (py)
#
# See docs/verifying-skills.md for the shared contract.
set -e
cd "$(dirname "$0")"
PY=python3

echo "=== 1. volatility EMA + edit budget (bc) ==="
out=$(bc -q checks.bc)
echo "$out"
if echo "$out" | grep -q FAIL; then
    echo "bc checks failed" >&2
    exit 1
fi
echo

echo "=== 2-4. acceptance gate, issue tracker, rejected log (python, stdlib only) ==="
$PY evolve.py
echo
echo "verification OK"
