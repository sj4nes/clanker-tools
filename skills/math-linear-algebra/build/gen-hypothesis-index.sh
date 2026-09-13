#!/bin/sh
set -eu
cd "$(dirname "$0")/.."
out=indexes/hypothesis-index.md
echo "# Hypothesis / axiom index (generated)" > $out
echo >> $out
echo "Every result reachable *from* each hypothesis or axiom node, i.e. every" >> $out
echo "node that has it as a (possibly indirect) prerequisite." >> $out
echo >> $out
awk -F '\t' 'NR>1 && ($2=="hypothesis" || $2=="axiom" || $2=="structure" || $2=="primitive") { print $1 }' nodes/nodes.tsv | sort | while read h; do
  echo "## $h" >> $out
  awk -v h="$h" '
    { dep[$2]=dep[$2] " " $1 }
    END {
      # BFS over reverse edges from h
      queue[0]=h; n=1; seen[h]=1
      for (i=0; i<n; i++) {
        cur=queue[i]
        for (j in radj) {}
      }
    }' build/dependencies.sorted.edges >/dev/null 2>&1
  # simple transitive closure with awk
  awk -v start="$h" '
    { radj[$1]=radj[$1] SUBSEP $2 }
    END {
      split("", stack); si=0; stack[si++]=start
      while (si>0) {
        cur=stack[--si]
        m=split(radj[cur], outs, SUBSEP)
        for (k=1;k<=m;k++) { t=outs[k]; if (t!="" && !(t in seen)) { seen[t]=1; stack[si++]=t } }
      }
      nkeys=0; for (t in seen) nkeys++
      for (t in seen) print "- " t
    }' build/dependencies.sorted.edges | sort >> $out
  echo >> $out
done
echo "gen-hypothesis-index: ok"
