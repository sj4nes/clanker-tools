#!/bin/sh
# Verification run for the `<SKILL>` skill: exercises the prescribed workflow on
# <KNOWN-ANSWER CASE> and confirms each prescribed check behaves as claimed.
#
# The skill is methodology-only (no bespoke CLI), so verification means:
# re-solve a case with a closed form using the skill's own workflow, and assert
# each prescribed step -- including each negative-contrast guardrail -- fires.
#
#   1. <exact arithmetic: formulas / bounds / identities>            (bc)
#   2. <workflow check with a known answer>                          (py)
#   3. <negative contrast: guardrail must trip>                      (py)
#
# NEGATIVE-CONTRAST TEST THIS HARNESS BEFORE SHIPPING IT: corrupt one value,
# confirm this script exits nonzero, revert.  An assertion that has never been
# seen to fail is not known to be an assertion.
#
# See docs/verifying-skills.md for the shared contract and portability rules,
# and docs/bc-verification-audit.md for the bc exit-status trap.
set -e
cd "$(dirname "$0")"
PY=python3

echo "=== 1. <name> (bc) ==="
# `bc`'s `quit` ALWAYS EXITS 0 -- the exit status can never signal failure and
# `set -e` gives no protection.  The OUTPUT must be inspected.  Both conditions
# below are needed: the banner alone would be satisfied by a file that never
# reached its later sections, and the absence of FAIL alone by one that crashed
# before printing anything.  See docs/bc-verification-audit.md.
bcout=$(bc -lq checks.bc)
printf '%s\n' "$bcout"
if ! printf '%s\n' "$bcout" | grep -q "ALL BC CHECKS PASSED" \
   || printf '%s\n' "$bcout" | grep -q '*** FAIL'; then
    echo "bc checks FAILED" >&2
    exit 1
fi
echo

echo "=== 2-N. workflow checks (python, stdlib only) ==="
$PY - <<'EOF'
from sim import example_check   # keep sim.py importable: guard main, no side effects

fail = 0

got = example_check(seed=20260906)
want = 1.0
ok = abs(got - want) < 0.02
print(f"2. example: got={got:.3f}  want={want:.3f}  {'PASS' if ok else 'FAIL'}")
fail += (not ok)

# negative contrast: the guardrail the skill prescribes must visibly trip here
# ok = <the wrong method undercovers / diverges / inflates the error rate>
# print(f"3. guardrail: ... {'PASS' if ok else 'FAIL'}")
# fail += (not ok)

print()
print("ALL CHECKS PASS" if fail == 0 else f"{fail} CHECK(S) FAILED")
raise SystemExit(1 if fail else 0)
EOF
