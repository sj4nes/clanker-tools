#!/bin/sh
# Full capsule build + validation.  Run from the capsule root.
set -eu
cd "$(dirname "$0")/.."
echo "== graph + tsort =="
sh build/build-tree.sh
echo
echo "== result entries + node pages =="
python3 build/gen-results.py
python3 build/gen-validation-md.py
python3 build/check-consistency.py
python3 build/check-lean-refs.py
echo
echo "== views =="
sh build/gen-hypothesis-index.sh
sh build/gen-status-index.sh
sh build/gen-prereq-paths.sh
sh build/gen-counterexample-index.sh
sh build/gen-symbol-index.sh
sh build/gen-field-scope-index.sh
echo
echo "== Lean proof-core checks =="
if [ -f validation/proof-checks.lean ]; then lean validation/proof-checks.lean && echo "lean: ok (exit 0)"; else echo "lean: SKIP (validation/proof-checks.lean not written yet -- Stage 3)"; fi
echo
echo "== bc instance checks =="
# NOTE: bc's `quit` always exits 0, so a failed CHECK cannot be detected from
# the exit status -- the output must be inspected.  (The sibling capsules'
# all.sh scripts rely on the exit code alone and would pass a broken run.)
if [ -f validation/instance-checks.bc ]; then
  bc -q -l validation/instance-checks.bc > build/instance-checks.out 2>&1
  if grep -q "ALL INSTANCE CHECKS PASSED" build/instance-checks.out \
     && ! grep -q "FAIL" build/instance-checks.out; then
    echo "bc: ok ($(grep -c '^ *[0-9]*\. ' build/instance-checks.out) sections, no FAIL lines)"
  else
    echo "bc: FAILED -- see build/instance-checks.out" >&2
    grep "FAIL" build/instance-checks.out >&2 || true
    exit 1
  fi
else
  echo "bc: SKIP (validation/instance-checks.bc not written yet)"
fi
echo
echo "ALL OK"
