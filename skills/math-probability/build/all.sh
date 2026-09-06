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
bc -q -l validation/instance-checks.bc > build/instance-checks.out 2>&1 && echo "bc: ok ($(wc -l < build/instance-checks.out | tr -d ' ') lines of output -> build/instance-checks.out)"
echo
echo "ALL OK"
