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
# See docs/verifying-skills.md for the shared contract and portability rules.
set -e
cd "$(dirname "$0")"
PY=python3

echo "=== 1. <name> (bc) ==="
bc -lq checks.bc
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
