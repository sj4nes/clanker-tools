#!/bin/sh
# Verification for `directed-verification`.
#
# Most of this skill is judgement and its SKILL.md says so. One behaviour --
# "suspect the test before the subject" -- leaves a trace, because a repository
# that records its own corrections records them in commit bodies.
set -e
cd "$(dirname "$0")/../../.."
D=skills/directed-verification/verification/detect_selfcorrection.py

echo "=== 1. the detector must be able to say NO ==="
python3 "$D" --self-test

echo
echo "=== 2. on the real history: find the admissions, reject the rest ==="
python3 "$D" --history

echo
echo "=== 3. behaviour 3's evidence, from this repo's history ==="
python3 "$D"

echo
echo "ALL DIRECTED-VERIFICATION CHECKS PASSED"
