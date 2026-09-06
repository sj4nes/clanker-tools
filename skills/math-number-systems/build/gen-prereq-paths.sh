#!/bin/sh
set -eu
cd "$(dirname "$0")/.."
out=indexes/prerequisite-paths.md
echo "# Minimal prerequisite paths for headline results (generated)" > $out
echo >> $out
echo "Each list is the transitive prerequisite set of the node, printed in" >> $out
echo "\`tsort\` order. It is the set the graph forces to precede the node, not a" >> $out
echo "shortest teaching path. Derived from graph structure, not the flat order." >> $out
echo >> $out
for n in recursion_theorem nat_division_with_remainder integer integer_is_ordered_integral_domain rational_number rational_is_ordered_field sqrt2_irrational rational_incomplete_lub dedekind_cut real_number real_is_ordered_field lub_property real_archimedean rational_dense_in_real nth_root_exists real_uniqueness nat_pairing_bijection rational_countable cantor_diagonal_argument real_uncountable; do
  echo "## $n" >> $out
  awk -v start="$n" '
    { adj[$2]=adj[$2] SUBSEP $1 }
    END { si=0; stack[si++]=start
      while (si>0) { cur=stack[--si]
        m=split(adj[cur], ins, SUBSEP)
        for (k=1;k<=m;k++){ p=ins[k]; if(p!="" && !(p in seen)){ seen[p]=1; stack[si++]=p } } }
      for (p in seen) print p }' build/dependencies.sorted.edges > build/_pp.$$
  cnt=$(grep -Fxf build/_pp.$$ indexes/tsort-order.txt | wc -l | tr -d ' ')
  echo "_($cnt prerequisites)_" >> $out
  echo >> $out
  grep -Fxf build/_pp.$$ indexes/tsort-order.txt | sed 's/^/- /' >> $out
  rm -f build/_pp.$$
  echo >> $out
done
echo "gen-prereq-paths: ok"
