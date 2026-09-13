#!/bin/sh
set -eu
cd "$(dirname "$0")/.."
out=indexes/counterexample-index.md
echo "# Counterexample index (generated from results/*.yaml)" > $out
echo >> $out
echo "\`dropped hypothesis\`  ->  \`witnessing counterexample\`  (from which result)" >> $out
echo >> $out
for f in results/*.yaml; do
  node=$(awk '/^node:/{print $2}' "$f")
  awk -v node="$node" '
    /^counterexamples_when_dropped:/ {inb=1; next}
    inb && /^[a-z_]+:/ && !/^  / {inb=0}
    inb && /^  [a-z_]+:/ {
      line=$0; sub(/^  /,"",line);
      print "- **" node "** — " line
    }' "$f" >> $out
done
echo >> $out
echo "gen-counterexample-index: ok"
