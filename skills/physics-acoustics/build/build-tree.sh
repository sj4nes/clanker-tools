#!/bin/sh
set -eu
cd "$(dirname "$0")/.."
mkdir -p build indexes

sh validation/graph-check.sh

TSORT_ERR=$(mktemp)
tsort edges/dependencies.edges > build/tsort-order.txt 2>"$TSORT_ERR"
if [ -s "$TSORT_ERR" ]; then
  echo "tsort reported a cycle:" >&2
  cat "$TSORT_ERR" >&2
  rm -f "$TSORT_ERR"
  exit 1
fi
rm -f "$TSORT_ERR"
cp build/tsort-order.txt indexes/tsort-order.txt

n_nodes=$(wc -l < build/node-ids.txt | tr -d ' ')
n_isolated=$(wc -l < build/isolated-nodes.txt | tr -d ' ')
awk '{print $2}' edges/dependencies.edges | LC_ALL=C sort -u > build/target-node-ids.txt
n_roots=$(LC_ALL=C comm -23 build/node-ids.txt build/target-node-ids.txt | wc -l | tr -d ' ')
echo "build-tree: ok ($n_nodes ordered nodes; $n_isolated isolated; $n_roots roots)"
