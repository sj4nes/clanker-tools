#!/bin/sh
# Full capsule build + validation.  Run from the capsule root.
set -eu
cd "$(dirname "$0")/.."
echo "== graph + tsort =="
sh build/build-tree.sh
python3 build/check-edge-evidence.py    # edge TRUTH: node text vs the graph
sh validation/mutation-check.sh        # do the graph checks still catch a broken graph?
python3 build/check-lean-cores.py         # lean TRUTH: the machine-verification claims
sh validation/lean-mutation-check.sh     # do those lean checks still catch a sorry?
echo
echo "== result entries + node pages =="
python3 build/gen-results.py
python3 build/gen-validation-md.py
python3 build/check-consistency.py
echo
echo "== views =="
sh build/gen-hypothesis-index.sh
sh build/gen-status-index.sh
sh build/gen-prereq-paths.sh
sh build/gen-counterexample-index.sh
sh build/gen-symbol-index.sh
echo
echo "== Lean proof-core checks =="
lean validation/proof-checks.lean && echo "lean: ok (exit 0)"
echo
echo "== bc instance checks =="
# `bc`'s `quit` ALWAYS exits 0, so `&& echo ok` reports success even when every
# check failed -- the OUTPUT must be inspected.  Grep for the marker `*** FAIL`,
# never the bare word, which appears legitimately in descriptive text.
# See docs/bc-verification-audit.md.
bc -q -l validation/instance-checks.bc > build/instance-checks.out 2>&1
if grep -q "ALL BC CHECKS PASSED" build/instance-checks.out && ! grep -q '\*\*\* FAIL' build/instance-checks.out; then
  echo "bc: ok ($(grep -c '\*\*\* FAIL' build/instance-checks.out | tr -d ' ') failures; see build/instance-checks.out)"
else
  echo "bc: FAILED -- see build/instance-checks.out" >&2
  grep '\*\*\* FAIL' build/instance-checks.out >&2 || echo "  (no pass banner: the file did not run to completion)" >&2
  exit 1
fi
echo
echo "ALL OK"
