#!/bin/sh
# Verification run for the `temporal-data-modeling` skill: re-solves a
# known-answer case -- a 7-day active-membership + login log with one team
# merge, one coverage gap (d6), and one field of each semantics -- using the
# workflow SKILL.md prescribes, and confirms each prescribed check fires,
# including the negative contrast the guardrail exists to prevent.
#
#   1-3. persistent/cumulative/naive split; round-trip loss class;
#        gluing check + cut-point independence for an additive field   (bc)
#   4.   gluing check for a set-valued cumulative field                (py)
#   5.   coverage gap: `disappear` invents churn, `unobserved` does not (py)
#   6.   resolution collapse: week property at daily granularity        (py)
#
# See docs/verifying-skills.md for the shared contract and portability rules.
set -e
cd "$(dirname "$0")"
PY=python3

echo "=== 1-3. semantics split, round-trip class, gluing check (bc) ==="
out=$(bc -q checks.bc)
echo "$out"
if echo "$out" | grep -q FAIL; then
    echo "bc checks failed" >&2
    exit 1
fi
echo

echo "=== 4-6. operator checks (python, stdlib only) ==="
$PY tdm.py
