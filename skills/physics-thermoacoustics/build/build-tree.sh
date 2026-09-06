#!/bin/sh
# Topologically sort the prerequisite graph and generate views.
set -eu
cd "$(dirname "$0")/.."
sh validation/graph-check.sh

# BSD/macOS tsort exits 0 on a cycle and writes "cycle in data" to stderr, then
# emits a meaningless order. GNU tsort exits non-zero. Check BOTH.
: > validation/tsort-errors.txt
tsort build/dependencies.sorted.edges > indexes/tsort-order.txt 2> validation/tsort-errors.txt || true
if [ -s validation/tsort-errors.txt ]; then
  echo "tsort reported a problem (cycle?):" >&2
  cat validation/tsort-errors.txt >&2
  exit 1
fi

# every supplied edge must be respected by the emitted order
awk '
  NR==FNR { pos[$1]=NR; next }
  { if (!($1 in pos) || !($2 in pos) || pos[$1] >= pos[$2]) {
      print "order violation: " $1 " must precede " $2 > "/dev/stderr"; bad=1 } }
  END { exit bad+0 }
' indexes/tsort-order.txt build/dependencies.sorted.edges

# node coverage: order must contain exactly the graph nodes
LC_ALL=C sort -u indexes/tsort-order.txt > build/order-nodes.txt
if ! diff -u build/edge-node-ids.txt build/order-nodes.txt > build/coverage.diff; then
  echo "node coverage mismatch between edges and tsort order:" >&2
  cat build/coverage.diff >&2
  exit 1
fi

# registered nodes that appear in no edge (roots kept separate, not forced in)
comm -23 build/node-ids.txt build/edge-node-ids.txt > build/isolated-nodes.txt

# reverse dependencies: node -> everything that requires it
awk '{ u[$1] = u[$1] " " $2 } END { for (n in u) print n ":" u[n] }' \
  build/dependencies.sorted.edges | LC_ALL=C sort > indexes/reverse-dependencies.txt

n_order=$(wc -l < indexes/tsort-order.txt | tr -d ' ')
n_iso=$(wc -l < build/isolated-nodes.txt | tr -d ' ')
echo "build-tree: ok ($n_order ordered nodes, $n_iso isolated/root-only nodes)"
