#!/bin/sh
# Shared capsule graph build: runs graph-check, then tsort with a stderr cycle
# guard (BSD tsort exits 0 on a cycle), an order-violation check, a node-coverage
# diff, and the reverse-dependencies / isolated-nodes / per-node incoming-edge
# views.  Invoked through each capsule's build/build-tree.sh shim.
#
#   Usage: sh build-tree.sh <capsule-root>
#
# CANONICAL SOURCE.  Keep in sync with references/package-layout.md.
#
# SCOPE (docs/verifying-skills.md §5): every check below is a HYGIENE or
# INTERNAL-CONSISTENCY check -- the emitted order is checked against the edge
# list it was built from.  A spurious edge and a missing edge both pass here;
# mutation testing (validation/mutation-check.sh) proves exactly that.  Edge
# TRUTH is build/check-edge-evidence.py's job.
set -eu
lib=$(cd "$(dirname "$0")" && pwd)
cd "${1:?usage: build-tree.sh <capsule-root>}"
mkdir -p build indexes validation

sh "$lib/graph-check.sh" "$PWD"

# BSD tsort exits 0 on a cycle and writes "cycle in data" to stderr, then emits a
# meaningless order.  GNU tsort exits non-zero.  Check BOTH.
: > validation/tsort-errors.txt
tsort build/dependencies.sorted.edges > indexes/tsort-order.txt 2> validation/tsort-errors.txt || true
if [ -s validation/tsort-errors.txt ]; then
  echo "tsort reported a problem (cycle?):" >&2; cat validation/tsort-errors.txt >&2; exit 1; fi

# every supplied edge must be respected by the emitted order
awk 'NR==FNR { pos[$1]=NR; next }
     { if (!($1 in pos) || !($2 in pos) || pos[$1] >= pos[$2]) {
         print "order violation: " $1 " must precede " $2 > "/dev/stderr"; bad=1 } }
     END { exit bad+0 }' indexes/tsort-order.txt build/dependencies.sorted.edges

# node coverage: the order must contain exactly the graph's nodes, once each
LC_ALL=C sort indexes/tsort-order.txt > build/order-nodes.txt
if awk 'seen[$0]++ { print "duplicated in tsort order: " $0 > "/dev/stderr"; bad=1 }
        END { exit bad+0 }' build/order-nodes.txt; then :; else exit 1; fi
LC_ALL=C sort -u build/order-nodes.txt > build/order-nodes.u.txt
if ! diff -u build/edge-node-ids.txt build/order-nodes.u.txt > build/coverage.diff; then
  echo "node coverage mismatch between edges and tsort order:" >&2
  cat build/coverage.diff >&2; exit 1; fi
rm -f build/coverage.diff build/order-nodes.u.txt

# reverse dependencies: node -> everything that requires it
awk '{ u[$1] = u[$1] " " $2 } END { for (n in u) print n ":" u[n] }' \
  build/dependencies.sorted.edges | LC_ALL=C sort > indexes/reverse-dependencies.txt

# registered nodes that appear in no edge are roots/isolated -- list, don't fail
LC_ALL=C comm -23 build/node-ids.txt build/edge-node-ids.txt > build/isolated-nodes.txt

# per-node incoming-edge list -- the authoritative dependency source for
# build/gen-results.py, build/check-consistency.py and check-edge-evidence.py
awk '{ d[$2] = d[$2] ", " $1 }
     END { for (n in d) print n ": [" substr(d[n], 3) "]" }' \
  build/dependencies.sorted.edges | LC_ALL=C sort > build/node-deps.txt

echo "build-tree: ok ($(wc -l < indexes/tsort-order.txt | tr -d ' ') ordered nodes; $(wc -l < build/isolated-nodes.txt | tr -d ' ') isolated)"
