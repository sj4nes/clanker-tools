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
for n in vector_space subspace span linear_independence basis steinitz_exchange basis_existence_finite basis_existence_general dimension_well_defined dimension direct_sum dimension_formula_sum quotient_space linear_map rank_nullity injective_surjective_equivalence first_isomorphism_theorem dual_basis double_dual matrix_multiplication matrix_mult_is_composition rref_uniqueness gaussian_elimination row_rank_equals_column_rank four_subspaces matrix_rank rank_inequalities invertibility_equivalences linear_system lu_factorisation schur_complement trace_cyclic change_of_basis determinant_existence_uniqueness determinant leibniz_formula determinant_multiplicative determinant_invertible_iff laplace_expansion adjugate cramers_rule determinant_rank_minors determinant_volume eigenvalue characteristic_polynomial char_poly_roots_are_eigenvalues eigenvalue_existence_closed distinct_eigenvalues_independent diagonalisability_criterion minimal_polynomial cayley_hamilton minimal_polynomial_diagonalisable schur_triangularisation primary_decomposition jordan_normal_form inner_product cauchy_schwarz orthonormal_basis gram_schmidt parseval_identity orthogonal_decomposition orthogonal_projection projection_matrix_characterisation best_approximation least_squares hat_matrix qr_factorisation adjoint_operator adjoint_kernel_image self_adjoint orthogonal_matrix spectral_theorem_symmetric spectral_theorem_normal spectral_decomposition courant_fischer quadratic_form positive_definite psd_characterisations gram_matrix cholesky_factorisation sylvester_law_of_inertia simultaneous_diagonalisation singular_values singular_value_decomposition moore_penrose_pseudoinverse eckart_young matrix_norms condition_number spectral_radius; do
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
