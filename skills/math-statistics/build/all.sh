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
sh build/gen-regime-index.sh
echo
echo "== Lean proof-core checks =="
if [ -f validation/proof-checks.lean ]; then lean validation/proof-checks.lean && echo "lean: ok (exit 0)"; else echo "lean: SKIP (validation/proof-checks.lean not written yet -- Stage 3)"; fi
echo
echo "== bc instance checks =="
if [ -f validation/instance-checks.bc ]; then bc -q -l validation/instance-checks.bc > build/instance-checks.out 2>&1 && echo "bc: ok"; else echo "bc: SKIP (validation/instance-checks.bc not written yet -- Stage 4)"; fi
echo
echo "ALL OK"
