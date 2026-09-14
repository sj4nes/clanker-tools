#!/bin/sh
# Shared capsule graph check: node-registry hygiene, edge hygiene, endpoint
# cross-check, deterministic sorted edge list.  Invoked through each capsule's
# validation/graph-check.sh shim (math, physics and chemistry capsules alike --
# the physics-formula-tree shims re-export this file).
#
#   Usage: sh graph-check.sh <capsule-root>
#
# CANONICAL SOURCE.  Keep in sync with references/package-layout.md.  See
# docs/verifying-skills.md §5 for the BSD/GNU rules this encodes (tsort cycle
# handling lives in build-tree.sh) and for the rubric this half implements:
# everything here is HYGIENE (is the graph well-formed?), never TRUTH (are the
# edges the right edges?).  Edge truth is check-edge-evidence.py's job.
set -eu
cd "${1:?usage: graph-check.sh <capsule-root>}"
mkdir -p build

# 1. node registry: 7 tab fields, non-empty ids, no duplicates
awk -F '\t' '
  NR == 1 { next }
  NF < 7   { print "nodes.tsv line " NR ": expected 7 fields, got " NF > "/dev/stderr"; bad=1 }
  $1 == "" { print "nodes.tsv line " NR ": empty id" > "/dev/stderr"; bad=1 }
  seen[$1]++ { print "nodes.tsv: duplicate id " $1 > "/dev/stderr"; bad=1 }
  END { exit bad+0 }
' nodes/nodes.tsv

# 2. strip full-line comments, then trailing "# evidence" comments, then blanks
grep -Ev '^[[:space:]]*(#|$)' edges/dependencies.plan \
  | sed -E 's/[[:space:]]*#.*$//; s/[[:space:]]+$//' \
  | grep -Ev '^[[:space:]]*$' > edges/dependencies.edges

# 3. exactly two fields per edge, no self-edges
awk 'NF != 2 { print "edge line " NR ": expected 2 fields, got " NF > "/dev/stderr"; bad=1 }
     $1 == $2 { print "edge line " NR ": self-edge " $1 > "/dev/stderr"; bad=1 }
     END { exit bad+0 }' edges/dependencies.edges

# 4. every edge endpoint is a registered node
awk -F '\t' 'NR>1 { print $1 }' nodes/nodes.tsv | LC_ALL=C sort -u > build/node-ids.txt
awk '{ print $1; print $2 }' edges/dependencies.edges | LC_ALL=C sort -u > build/edge-node-ids.txt
LC_ALL=C comm -23 build/edge-node-ids.txt build/node-ids.txt > build/unknown-edge-nodes.txt
if [ -s build/unknown-edge-nodes.txt ]; then
  echo "edges reference unregistered nodes:" >&2; cat build/unknown-edge-nodes.txt >&2; exit 1; fi

# 5. deterministic, de-duplicated edge file (never sorts WITHIN a pair)
LC_ALL=C sort -u edges/dependencies.edges > build/dependencies.sorted.edges

echo "graph-check: ok ($(wc -l < build/dependencies.sorted.edges | tr -d ' ') edges, $(wc -l < build/node-ids.txt | tr -d ' ') nodes)"
