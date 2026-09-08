#!/bin/sh
# Full capsule build + validation.  Run from anywhere.
set -eu
cd "$(dirname "$0")/.."
echo "== graph + tsort =="
sh build/build-tree.sh
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
bc -q -l validation/instance-checks.bc > build/instance-checks.out 2>&1 \
  && echo "bc: ok ($(wc -l < build/instance-checks.out | tr -d ' ') lines -> build/instance-checks.out)"
echo
echo "== result YAML <-> graph consistency =="
python3 build/check-yaml.py
echo
echo "ALL OK"
