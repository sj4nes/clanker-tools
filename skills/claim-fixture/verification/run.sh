#!/bin/sh
# Verification for `claim-fixture`: run the pre-registration check over the two
# real case studies. ONE OF THEM FAILS, deliberately and permanently.
set -e
cd "$(dirname "$0")"
V=../../role-deck/verification

echo "=== case study 2: the ordering fixture ==="
sh check_preregistration.sh \
   "skills/role-deck/verification/ordering-fixture/score.sh" \
   "skills/role-deck/verification/ordering-fixture/RESULT.md" \
   && o=0 || o=1

echo
echo "=== case study 1: the premise fixture (expected to FAIL) ==="
sh check_preregistration.sh \
   "skills/role-deck/verification/premise-fixture/score.py" \
   "skills/role-deck/verification/premise-fixture/results/trial1.txt" \
   && p=0 || p=1

echo
if [ "$o" -eq 0 ] && [ "$p" -eq 1 ]; then
    echo "ALL CHECKS PASSED"
    echo "  The ordering fixture is provably pre-registered."
    echo "  The premise fixture is NOT, and that is the point: its scorer was"
    echo "  written first but committed alongside the results, so the record"
    echo "  cannot show it. Behaviour 4 says SEPARATE COMMIT for this reason."
    exit 0
fi
echo "*** unexpected: ordering=$o premise=$p (want 0 and 1)" >&2
exit 1
