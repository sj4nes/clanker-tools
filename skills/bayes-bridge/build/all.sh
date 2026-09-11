#!/bin/sh
set -eu
cd "$(dirname "$0")/.."

echo "== graph + tsort =="
sh build/build-tree.sh

echo ""
echo "== bc instance checks =="
bc -q -l validation/instance-checks.bc > build/instance-checks.out
echo "bc: ok ($(wc -l < build/instance-checks.out | tr -d ' ') lines -> build/instance-checks.out)"

echo ""
echo "ALL OK"
