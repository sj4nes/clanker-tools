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

echo "build-tree: ok ($n_nodes ordered nodes; $n_isolated isolated)"
