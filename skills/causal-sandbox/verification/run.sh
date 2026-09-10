#!/bin/sh
# Verification run for the `causal-sandbox` skill: builds a small authored-rule
# sandbox and confirms each prescribed mechanism behaves as claimed, including
# the negative contrasts the guardrails exist to prevent.
#
#   1. inventory arithmetic: the reorder-crossing step and the zero-hit step
#      that the engine trace must reproduce                          (bc)
#   2. forward run: the causal graph shows reorder fired BECAUSE the last
#      consume dropped stock below threshold (last-writer edge)      (py)
#   3. backward query: 'stock hit zero' -> the 1-change fix is raise-the-
#      threshold; 'skip the consume' is not in the candidate space   (py)
#   4. confluence: grant_default/revoke_all on one user is flagged, two
#      independent grants are not                                    (py)
#   5. a causal claim on the non-confluent slice flips with firing order (py)
#   6. degenerate cases (frozen / empty-write / replay) and read/write-set
#      enforcement                                                   (py)
#
# See docs/verifying-skills.md for the shared contract.
set -e
cd "$(dirname "$0")"
PY=python3

echo "=== 1. inventory arithmetic (bc) ==="
out=$(bc -q checks.bc)
echo "$out"
if echo "$out" | grep -q FAIL; then
    echo "bc checks failed" >&2
    exit 1
fi
echo

echo "=== 2-6. engine mechanisms (python, stdlib only) ==="
$PY sandbox.py
echo
echo "verification OK"
