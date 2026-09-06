#!/bin/sh
set -eu
cd "$(dirname "$0")/.."
out=indexes/status-index.md
echo "# Result index by node type (generated)" > $out
echo >> $out
for t in primitive notation_convention definition axiom structure hypothesis principle_law mathematical_identity proposition theorem; do
  echo "## $t" >> $out
  awk -F '\t' -v t="$t" 'NR>1 && $2==t { printf "- **%s** (%s) — %s\n", $1, $4, $7 }' nodes/nodes.tsv >> $out
  echo >> $out
done
echo "gen-status-index: ok"
