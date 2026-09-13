#!/bin/sh
# Verification run for the `test-writing` skill.
#
# The skill is a nudge away from known testing failure modes, so verification
# means: plant a bug of each documented shape, write the test an agent writes
# by DEFAULT and the check the skill PRESCRIBES, and confirm the default misses
# the bug while the prescribed check catches it -- and does not false-alarm on
# the corrected code.
#
#   1. exact oracle + masking premise for subject A                     (bc)
#   2. detection matrix: 6 planted bugs x {prescribed, naive}           (py)
#   3. branch coverage: naive vs structured generator (subject D)       (py)
#
# NEGATIVE-CONTRAST TESTED: the whole point of this harness is that each check
# has been seen to fail (column 1 of the matrix IS the failure), and cell 2
# proves the check is not vacuously failing.  See README.md for the audit.
#
# See docs/verifying-skills.md for the shared contract and portability rules,
# and docs/bc-verification-audit.md for the bc exit-status trap.
set -e
cd "$(dirname "$0")"
PY=python3

echo "=== 1. exact rounding oracle and the masking premise (bc) ==="
# bc's exit status reports INTERPRETER errors, never a false claim, and `quit`
# always exits 0 -- so grep the output, and keep the status as a backstop only.
# Capture explicitly: under `set -e` a failing $( ) aborts before the
# diagnostics print, and a pipe would replace bc's status with the pipe's.
bcout=$(bc -lq checks.bc 2>&1) && bcstatus=0 || bcstatus=$?
printf '%s\n' "$bcout"
if [ "$bcstatus" -ne 0 ] \
   || ! printf '%s\n' "$bcout" | grep -q "ALL BC CHECKS PASSED" \
   || printf '%s\n' "$bcout" | grep -q '\*\*\* FAIL'; then
    echo "bc checks FAILED (exit status $bcstatus)" >&2
    exit 1
fi
echo

echo "=== 2. detection matrix: 6 planted bugs (python, stdlib only) ==="
$PY matrix.py
echo

echo "=== 3. branch coverage of the two generators, subject D (python) ==="
$PY - <<'EOF'
import naive_tests as N
import prescribed_tests as P

fail = 0

naive = N.naive_d_coverage()
structured = P.prescribed_d_coverage()

ok = naive == 0.0
print("naive (uniform random bytes):      %8.4f%% of inputs reach the "
      "repeated-key branch  %s" % (100 * naive, "PASS" if ok else "FAIL"))
print("   (claim: a fuzzer whose every input dies at the first guard tests "
      "the guard, not the code)")
fail += (not ok)

ok = structured >= 0.30
print("structured (grammar + steering):   %8.4f%% reach it                "
      "        %s" % (100 * structured, "PASS" if ok else "FAIL"))
print("   (claim: >= 30% -- the generator must steer toward interesting "
      "state, not merely be valid)")
fail += (not ok)

print()
print("ALL CHECKS PASS" if fail == 0 else "%d CHECK(S) FAILED" % fail)
raise SystemExit(1 if fail else 0)
EOF
echo
echo "=== test-writing verification: all sections passed ==="
