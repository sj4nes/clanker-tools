#!/bin/sh
# Verification run for the `formula-tree-tutorial` skill: checks that every
# tutorial shipped in this repository carries the beats the skill prescribes,
# and that each of those checks can actually fail.
#
#   1. beats present in all 24 shipped tutorials      (python)
#   2. both skills still defer to the shared contract (python)
#   3. every guard breaks on its own mutant           (python)
set -e
cd "$(dirname "$0")"
PY=python3

echo "=== 1. prescribed beats, every shipped tutorial (python) ==="
# Structural, not stylistic: each beat below is one that
# references/document-structure.md states. Exits non-zero on any missing beat.
$PY check_beats.py
echo

echo "=== 2. the shared contract is single-source (python) ==="
# docs/capsule-tutorial-contract.md exists because the skeleton was maintained
# twice and drifted. Single-sourcing helps only while both skills point at it.
$PY check_contract.py
echo

echo "=== 3. mutation check: can each guard fail? (python) ==="
# A checker only ever run against conforming documents has demonstrated
# nothing. One mutant per guard, in isolation; a guard whose mutant still
# passes is reported DEAD and fails this run.
$PY mutation_check.py
