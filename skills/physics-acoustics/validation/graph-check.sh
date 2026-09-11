#!/bin/sh
set -eu
cd "$(dirname "$0")/.."
mkdir -p build

grep -Ev '^[[:space:]]*(#|$)' edges/dependencies.plan > edges/dependencies.edges

awk 'NF != 2 { print "line " NR ": expected 2 fields, got " NF > "/dev/stderr"; bad=1 }
     $1 == $2 { print "line " NR ": self-edge " $1 > "/dev/stderr"; bad=1 }
     END { exit bad+0 }' edges/dependencies.edges

awk -F '\t' 'NR>1 { print $1 }' nodes/nodes.tsv | LC_ALL=C sort -u > build/node-ids.txt
awk '{ print $1; print $2 }' edges/dependencies.edges | LC_ALL=C sort -u > build/edge-node-ids.txt
LC_ALL=C comm -23 build/edge-node-ids.txt build/node-ids.txt > build/unknown-edge-nodes.txt
if [ -s build/unknown-edge-nodes.txt ]; then
  echo "edges reference unregistered nodes:" >&2
  cat build/unknown-edge-nodes.txt >&2
  exit 1
fi

LC_ALL=C comm -23 build/node-ids.txt build/edge-node-ids.txt > build/isolated-nodes.txt
echo "graph-check: ok ($(wc -l < edges/dependencies.edges | tr -d ' ') edges, $(wc -l < build/node-ids.txt | tr -d ' ') nodes, $(wc -l < build/isolated-nodes.txt | tr -d ' ') isolated)"
if [ -s build/isolated-nodes.txt ]; then
  echo "isolated nodes:" >&2
  cat build/isolated-nodes.txt >&2
fi
