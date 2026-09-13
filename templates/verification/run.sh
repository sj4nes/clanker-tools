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
# Two INDEPENDENT failure signals, both checked:
#   1. the OUTPUT -- a `*** FAIL` marker, plus the pass banner. Names the claim.
#   2. the EXIT STATUS -- checks.bc forces a nonzero exit on failure via a
#      deliberate 1/0. This also catches a BROKEN file for free: bc exits 2 on
#      a syntax error, 3 on an undefined function, 4 on a missing file.
#
# bc reports interpreter errors but never a false claim, so signal 1 is the
# one that catches wrong arithmetic; signal 2 is the backstop.
#
# The `-F` on the marker grep is LOAD-BEARING.  `'*** FAIL'` as a regex is a
# leading repetition operator applied to nothing: ugrep (installed as `grep`
# here) exits 2 with `repetition-operator operand invalid`, and shell `if`
# reads 2 as false -- so the clause never fires.  That broke this signal in 8
# of 9 harnesses before 2026-09-13.  Test it in ISOLATION: plant a `*** FAIL`
# marker with the `fails` counter untouched (banner still printed, exit still
# 0) and confirm run.sh exits 1.
#
# Capture the status EXPLICITLY. Two traps here:
#   - under `set -e`, a failing `$( )` assignment aborts before the diagnostics
#     are printed, so the useful output is lost;
#   - a pipe (`bc f.bc | tail`) replaces bc's status with the last command's.
# See docs/bc-verification-audit.md.
bcout=$(bc -lq checks.bc 2>&1) && bcstatus=0 || bcstatus=$?
printf '%s\n' "$bcout"
if [ "$bcstatus" -ne 0 ] \
   || ! printf '%s\n' "$bcout" | grep -q "ALL BC CHECKS PASSED" \
   || printf '%s\n' "$bcout" | grep -qF '*** FAIL'; then
    echo "bc checks FAILED (exit status $bcstatus)" >&2
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
