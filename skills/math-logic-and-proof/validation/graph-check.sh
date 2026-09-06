#!/bin/sh
set -eu
cd "$(dirname "$0")/.."
mkdir -p build
# strip full-line comments, then trailing "# evidence" comments, then blank lines
grep -Ev '^[[:space:]]*(#|$)' edges/dependencies.plan \
  | sed -E 's/[[:space:]]*#.*$//; s/[[:space:]]+$//' \
  | grep -Ev '^[[:space:]]*$' > edges/dependencies.edges
awk 'NF != 2 { print "line " NR ": expected 2 fields, got " NF > "/dev/stderr"; bad=1 }
     $1 == $2 { print "line " NR ": self-edge " $1 > "/dev/stderr"; bad=1 }
     END { exit bad+0 }' edges/dependencies.edges
awk -F '\t' 'NR>1 { print $1 }' nodes/nodes.tsv | LC_ALL=C sort -u > build/node-ids.txt
awk '{ print $1; print $2 }' edges/dependencies.edges | LC_ALL=C sort -u > build/edge-node-ids.txt
comm -23 build/edge-node-ids.txt build/node-ids.txt > build/unknown-edge-nodes.txt
if [ -s build/unknown-edge-nodes.txt ]; then
  echo "edges reference unregistered nodes:" >&2; cat build/unknown-edge-nodes.txt >&2; exit 1; fi
LC_ALL=C sort -u edges/dependencies.edges > build/dependencies.sorted.edges
echo "graph-check: ok ($(wc -l < build/dependencies.sorted.edges | tr -d ' ') edges, $(($(wc -l < nodes/nodes.tsv)-1)) nodes)"
