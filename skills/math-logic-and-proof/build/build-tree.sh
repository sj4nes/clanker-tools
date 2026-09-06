#!/bin/sh
set -eu
cd "$(dirname "$0")/.."
sh validation/graph-check.sh
tsort build/dependencies.sorted.edges > indexes/tsort-order.txt 2> validation/tsort-errors.txt || true
if [ -s validation/tsort-errors.txt ]; then
  echo "tsort reported a problem (cycle?):" >&2; cat validation/tsort-errors.txt >&2; exit 1; fi
awk 'NR==FNR { pos[$1]=NR; next }
     { if (!($1 in pos) || !($2 in pos) || pos[$1] >= pos[$2]) {
         print "order violation: " $1 " must precede " $2 > "/dev/stderr"; bad=1 } }
     END { exit bad+0 }' indexes/tsort-order.txt build/dependencies.sorted.edges
awk '{ u[$1] = u[$1] " " $2 } END { for (n in u) print n ":" u[n] }' \
  build/dependencies.sorted.edges | LC_ALL=C sort > indexes/reverse-dependencies.txt
awk '{ print $1; print $2 }' build/dependencies.sorted.edges | LC_ALL=C sort -u > build/edge-node-ids.txt
comm -23 build/node-ids.txt build/edge-node-ids.txt > build/isolated-nodes.txt
echo "build-tree: ok ($(wc -l < indexes/tsort-order.txt | tr -d ' ') ordered nodes; $(wc -l < build/isolated-nodes.txt | tr -d ' ') isolated)"
