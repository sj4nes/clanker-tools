#!/bin/sh
# Validate the node registry and prerequisite edge list before tsort.
set -eu
cd "$(dirname "$0")/.."
mkdir -p build

# 1. node registry: header + >=7 fields, unique ids
awk -F '\t' '
  NR == 1 { next }
  NF < 7 { print "nodes.tsv line " NR ": expected 7 fields, got " NF > "/dev/stderr"; bad=1 }
  $1 == "" { print "nodes.tsv line " NR ": empty id" > "/dev/stderr"; bad=1 }
  seen[$1]++ { print "nodes.tsv: duplicate id " $1 > "/dev/stderr"; bad=1 }
  END { exit bad+0 }
' nodes/nodes.tsv

# 2. strip comments/blanks to a clean edge file
grep -Ev '^[[:space:]]*(#|$)' edges/dependencies.plan > edges/dependencies.edges

# 3. exactly two fields per edge, no self-edges
awk '
  NF != 2 { print "edge line " NR ": expected 2 fields, got " NF > "/dev/stderr"; bad=1 }
  $1 == $2 { print "edge line " NR ": self-edge " $1 > "/dev/stderr"; bad=1 }
  END { exit bad+0 }
' edges/dependencies.edges

# 4. every edge endpoint is a registered node
awk -F '\t' 'NR>1 { print $1 }' nodes/nodes.tsv | LC_ALL=C sort -u > build/node-ids.txt
awk '{ print $1; print $2 }' edges/dependencies.edges | LC_ALL=C sort -u > build/edge-node-ids.txt
comm -23 build/edge-node-ids.txt build/node-ids.txt > build/unknown-edge-nodes.txt
if [ -s build/unknown-edge-nodes.txt ]; then
  echo "edges reference unregistered nodes:" >&2
  cat build/unknown-edge-nodes.txt >&2
  exit 1
fi

# 5. deterministic, de-duplicated edge file (never sorts within a pair)
LC_ALL=C sort -u edges/dependencies.edges > build/dependencies.sorted.edges

echo "graph-check: ok ($(wc -l < build/node-ids.txt) nodes, $(wc -l < build/dependencies.sorted.edges) edges)"
