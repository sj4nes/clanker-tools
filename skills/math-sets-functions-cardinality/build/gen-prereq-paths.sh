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
for n in preimage_algebra equivalence_partition_correspondence quotient_set well_defined_on_quotient universal_property_quotient inverse_iff_bijective powerset_iso_two_power pigeonhole_principle zorn_lemma well_ordering_theorem transfinite_recursion order_type_theorem omega_construction peano_holds_in_omega recursion_theorem cantor_schroeder_bernstein cantor_theorem cantor_diagonal countable_closure_properties cardinal_comparability hartogs_number infinite_cardinal_arithmetic continuum_hypothesis; do
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
