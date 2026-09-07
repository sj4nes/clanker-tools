#!/bin/sh
# test.sh -- verification battery for ste-check.awk.
#
# Runs the checker against fixtures/ with known expected findings and asserts
# each tag fires where it should and stays silent where it should not. No
# network, no dependencies beyond POSIX awk + sh. Exit 0 if all pass.

set -u

here=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
awkf="$here/ste-check.awk"
fix="$here/fixtures"
pass=0
fail=0

# run <fixture> [extra awk -v args...] -> output on stdout
run() {
  f="$1"; shift
  awk "$@" -f "$awkf" "$fix/$f"
}

# expect_count <label> <expected-n> <pattern> <output>
expect_count() {
  label="$1"; want="$2"; pat="$3"; out="$4"
  got=$(printf '%s\n' "$out" | grep -c -- "$pat" || true)
  if [ "$got" -eq "$want" ]; then
    pass=$((pass + 1)); echo "PASS  $label  ($pat x$got)"
  else
    fail=$((fail + 1)); echo "FAIL  $label  expected $want of [$pat], got $got"
    printf '%s\n' "$out" | sed 's/^/      /'
  fi
}

# expect_exit <label> <expected-rc> <fixture> [awk args...]
expect_exit() {
  label="$1"; want="$2"; f="$3"; shift 3
  awk "$@" -f "$awkf" "$fix/$f" >/dev/null 2>&1
  got=$?
  if [ "$got" -eq "$want" ]; then
    pass=$((pass + 1)); echo "PASS  $label  (exit $got)"
  else
    fail=$((fail + 1)); echo "FAIL  $label  expected exit $want, got $got"
  fi
}

echo "== ste-check.awk verification battery =="

# --- clean.md: zero findings, code-fence content ignored --------------------
out=$(run clean.md)
expect_count "clean/no-findings"        0 "\[" "$out"
expect_count "clean/code-fence-ignored" 0 "PASSIVE" "$out"

# --- length.md ------------------------------------------------------------------
out=$(run length.md)
expect_count "length/long-sentence"  1 "\[LENGTH\]" "$out"

# --- vague.md ----------------------------------------------------------------
out=$(run vague.md)
expect_count "vague/handle"   1 '"handle"'   "$out"
expect_count "vague/ensure"   1 '"ensure"'   "$out"
expect_count "vague/leverage" 1 '"leverage"' "$out"
expect_count "vague/total"    3 "\[VAGUE-VERB\]" "$out"

# --- passive.md ------------------------------------------------------------------
out=$(run passive.md)
expect_count "passive/detected"    2 "\[PASSIVE?\]" "$out"

# --- multi-action.md -------------------------------------------------------------
out=$(run multi-action.md)
expect_count "multi-action/joined" 1 "\[MULTI-ACTION?\]" "$out"

# --- condition.md --------------------------------------------------------------
out=$(run condition.md)
expect_count "condition/trailing"  2 "\[CONDITION-LAST\]" "$out"

# --- synonym-drift.md ----------------------------------------------------------
out=$(run synonym-drift.md)
expect_count "drift/doc-summary"   1 "same operation written 3 ways" "$out"

out=$(run synonym-drift.md -v canon=verify)
expect_count "drift/canon-check"   1 '"check"'   "$out"
expect_count "drift/canon-confirm" 1 '"confirm"' "$out"
expect_count "drift/canon-not-verify" 0 'SYNONYM-DRIFT]  "verify"' "$out"

# --- synonym-consistent.md: one verb, no drift -------------------------------
out=$(run synonym-consistent.md)
expect_count "consistent/no-drift" 0 "SYNONYM-DRIFT" "$out"

# --- exit codes -------------------------------------------------------------
expect_exit "exit/clean-strict-0"  0 clean.md        -v strict=1
expect_exit "exit/vague-strict-1"  1 vague.md        -v strict=1
expect_exit "exit/vague-default-0" 0 vague.md

echo
echo "== $pass passed, $fail failed =="
[ "$fail" -eq 0 ]
