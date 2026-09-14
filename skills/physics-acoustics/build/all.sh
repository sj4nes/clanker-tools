#!/bin/sh
set -eu
cd "$(dirname "$0")/.."

echo "== graph + tsort =="
sh build/build-tree.sh

python3 build/check-edge-evidence.py    # edge TRUTH: node text vs the graph
sh validation/mutation-check.sh        # do the graph checks still catch a broken graph?
echo ""
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
echo "bc: ok ($(wc -l < build/instance-checks.out | tr -d ' ') lines -> build/instance-checks.out)"

echo ""
echo "ALL OK"
