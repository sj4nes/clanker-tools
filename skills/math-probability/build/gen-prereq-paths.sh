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
for n in kolmogorov_axioms boole_inequality borel_cantelli_first bayes_theorem conditional_probability random_variable probability_integral_transform independence_events independence_random_variables expectation expectation_linearity lotus markov_inequality jensen_inequality chebyshev_inequality variance_computational hoeffding_inequality binomial_distribution normal_distribution convergence_implications weak_law_large_numbers strong_law_large_numbers central_limit_theorem levy_continuity_theorem tower_property law_of_total_variance conditional_expectation_l2_projection; do
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
