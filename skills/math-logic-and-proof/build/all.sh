#!/bin/sh
# Full capsule build + validation.  Run from anywhere.
set -eu
cd "$(dirname "$0")/.."
echo "== graph + tsort =="
sh build/build-tree.sh
python3 build/check-edge-evidence.py    # edge TRUTH: node text vs the graph
sh validation/mutation-check.sh        # do the graph checks still catch a broken graph?
python3 build/check-lean-cores.py         # lean TRUTH: the machine-verification claims
sh validation/lean-mutation-check.sh     # do those lean checks still catch a sorry?
echo
echo "== node-page step-7 audit =="
python3 build/audit-pages.py
echo
echo "== discovery views =="
sh build/gen-indexes.sh
sh build/gen-symbol-index.sh
python3 build/gen-validation-md.py
echo
echo "== Lean proof-core checks =="
lean validation/proof-checks.lean && echo "lean: ok (exit 0, no sorry)"
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
echo "== result YAML <-> graph consistency =="
python3 build/check-yaml.py
echo
echo "ALL OK"
