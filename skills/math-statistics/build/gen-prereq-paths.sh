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
for n in likelihood_function score_function fisher_information score_identity information_equality exponential_family sufficiency neyman_fisher_factorization completeness_statistic estimator mse_bias_variance_decomposition consistency umvue cramer_rao_lower_bound rao_blackwell_theorem lehmann_scheffe_theorem maximum_likelihood_estimator mle_consistency mle_asymptotic_normality bayes_estimator credible_interval bernstein_von_mises risk_function admissibility bayes_rule_minimizes_bayes_risk james_stein chi_squared_distribution students_t_distribution sample_mean sample_variance bias_of_sample_variance normal_sample_mean_variance_independence scaled_sample_variance_chi_squared t_statistic_distribution confidence_set confidence_set_test_duality normal_mean_ci_unknown_variance wald_interval test_function size_of_test power_function neyman_pearson_lemma likelihood_ratio_test wilks_theorem p_value empirical_cdf glivenko_cantelli bootstrap linear_model ordinary_least_squares gauss_markov_theorem ols_distribution_under_normal_errors; do
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
