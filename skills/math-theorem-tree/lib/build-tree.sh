#!/bin/sh
# Shared capsule graph build: runs graph-check, then tsort with a stderr cycle
# guard (BSD tsort exits 0 on a cycle), an order-violation check, and the
# reverse-dependencies / isolated-nodes / per-node incoming-edge views.
# Invoked through each capsule's build/build-tree.sh shim.
#
#   Usage: sh build-tree.sh <capsule-root>
#
# Canonical source; keep in sync with references/package-layout.md.
set -eu
lib=$(cd "$(dirname "$0")" && pwd)
cd "${1:?usage: build-tree.sh <capsule-root>}"

sh "$lib/graph-check.sh" "$PWD"

# BSD tsort exits 0 on a cycle and prints to stderr -- check both.
tsort build/dependencies.sorted.edges > indexes/tsort-order.txt 2> validation/tsort-errors.txt || true
if [ -s validation/tsort-errors.txt ]; then
  echo "tsort reported a problem (cycle?):" >&2; cat validation/tsort-errors.txt >&2; exit 1; fi

# every supplied edge must be respected by the emitted order
awk 'NR==FNR { pos[$1]=NR; next }
     { if (!($1 in pos) || !($2 in pos) || pos[$1] >= pos[$2]) {
         print "order violation: " $1 " must precede " $2 > "/dev/stderr"; bad=1 } }
     END { exit bad+0 }' indexes/tsort-order.txt build/dependencies.sorted.edges

# reverse dependencies
awk '{ u[$1] = u[$1] " " $2 } END { for (n in u) print n ":" u[n] }' \
  build/dependencies.sorted.edges | LC_ALL=C sort > indexes/reverse-dependencies.txt

# node coverage: registered nodes with no edge are roots/isolated, list them
awk '{ print $1; print $2 }' build/dependencies.sorted.edges | LC_ALL=C sort -u > build/edge-node-ids.txt
comm -23 build/node-ids.txt build/edge-node-ids.txt > build/isolated-nodes.txt

# per-node incoming-edge list -- the authoritative dependency source for
# build/gen-results.py and build/check-consistency.py
awk '{ d[$2] = d[$2] ", " $1 }
     END { for (n in d) print n ": [" substr(d[n], 3) "]" }' \
  build/dependencies.sorted.edges | LC_ALL=C sort > build/node-deps.txt

echo "build-tree: ok ($(wc -l < indexes/tsort-order.txt | tr -d ' ') ordered nodes; $(wc -l < build/isolated-nodes.txt | tr -d ' ') isolated)"
