#!/bin/sh
# Verification run for the `hypergraph-reasoning` skill: exercises the prescribed
# operators on cases with known answers and confirms each -- including each
# negative-contrast guardrail -- fires.
#
# The skill is methodology-only (no bespoke CLI), so verification means:
# re-solve a case using the skill's own operators, and assert the naive method
# the guardrail exists to prevent visibly fails.
#
#   1. retrieval score + precondition conjunction                   (bc)
#   2. context collapse: n-ary edge vs shattered binary edges       (py)
#   3. temporal scope: valid_time vs time-blind check               (py)
#   4. contradiction detection: role-typed vs role-blind            (py)
#   5. epistemic-status / provenance gating vs flat synthesis       (py)
#
# See docs/verifying-skills.md for the shared contract and portability rules.
set -e
cd "$(dirname "$0")"
PY=python3

echo "=== 1. retrieval score + precondition conjunction (bc) ==="
bc -lq checks.bc
echo

echo "=== 2-5. operator checks (python, stdlib only) ==="
$PY hypergraph.py
