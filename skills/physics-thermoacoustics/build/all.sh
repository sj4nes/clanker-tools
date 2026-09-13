#!/bin/sh
# Full capsule build + validation.  Run from the capsule root:  sh build/all.sh
#
# Added 2026-09-13.  Before this, the capsule had NO build script: the commands
# below were listed in README.md for a human to run by hand, and the bc checks
# in particular were never executed by anything.  See docs/bc-verification-audit.md.
set -eu
cd "$(dirname "$0")/.."

echo "== graph + tsort =="
sh build/build-tree.sh

echo
echo "== views =="
sh build/gen-symbol-index.sh
sh build/gen-assumption-index.sh

echo
echo "== Lean derivation checks =="
if [ -f validation/derivation-checks.lean ]; then
  lean validation/derivation-checks.lean && echo "lean: ok (exit 0)"
else
  echo "lean: SKIP (no validation/derivation-checks.lean)"
fi

echo
echo "== bc dimensional / instance checks =="
# `bc`'s `quit` ALWAYS exits 0, so the exit status can never signal failure --
# the OUTPUT must be inspected.  Grep for the marker `*** FAIL`, never the bare
# word, which appears legitimately in descriptive text.  `< /dev/null` guards
# against a missing trailing `quit` leaving bc reading stdin.
bc -q -l validation/dimensional-checks.bc < /dev/null > build/bc-checks.out 2>&1
if grep -q "ALL BC CHECKS PASSED" build/bc-checks.out && ! grep -q '\*\*\* FAIL' build/bc-checks.out; then
  echo "bc: ok (see build/bc-checks.out)"
else
  echo "bc: FAILED -- see build/bc-checks.out" >&2
  grep '\*\*\* FAIL' build/bc-checks.out >&2 || echo "  (no pass banner: the file did not run to completion)" >&2
  exit 1
fi

echo
echo "ALL OK"
