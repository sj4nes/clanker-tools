#!/bin/sh
# gen-prereq-path.sh NODE  -> transitive prerequisite set of NODE, in tsort order
set -eu
cd "$(dirname "$0")/.."
target="$1"
awk -v start="$target" '
  { adj[$2]=adj[$2] SUBSEP $1 }
  END {
    si=0; stack[si++]=start
    while (si>0) { cur=stack[--si]
      m=split(adj[cur], ins, SUBSEP)
      for (k=1;k<=m;k++){ p=ins[k]; if(p!="" && !(p in seen)){ seen[p]=1; stack[si++]=p } } }
    for (p in seen) print p
  }' build/dependencies.sorted.edges > build/_prereq.$$
grep -Fxf build/_prereq.$$ indexes/tsort-order.txt
rm -f build/_prereq.$$
