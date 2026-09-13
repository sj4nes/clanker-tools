"""AUTHORITATIVE lean_status / lean_ref map, reconciled against what
validation/proof-checks.lean ACTUALLY compiles.

Applied by nodespec.N at construction time, OVERRIDING whatever a spec module
claims.  A node absent from LEAN_MAP is forced to `cited` with no ref -- so a
spec cannot accidentally overclaim: the default is the weakest status, and
every upgrade has to name a declaration that `build/check-lean-refs.py`
confirms exists in the .lean file.

Status vocabulary (see conventions.md):
  core     -- the GENERAL statement is proved
  dim_core -- universal in the matrix entries at a FIXED dimension (n = 2 or 3)
  instance -- `decide` at fixed numbers; a check, not a proof
  cited    -- proved elsewhere, referenced here
"""

LEAN_MAP = {
  # --- core: the general statement is proved -------------------------------
  "vector_space_basic_consequences": ("core",
    "LinAlg.smul_zero_eq_zero, LinAlg.zero_smul_vec, LinAlg.neg_one_smul, LinAlg.no_zero_smul_divisors"),
  "dimension_well_defined": ("core", "LinAlg.basis_card_eq"),
  "rank_nullity": ("core", "LinAlg.rank_nullity (the Nat identity the basis count concludes with)"),
  "injective_surjective_equivalence": ("core", "LinAlg.inj_iff_surj_of_dim_eq"),
  "dimension_formula_sum": ("core", "LinAlg.dim_sum_inter"),
  "quotient_dimension": ("core", "LinAlg.dim_quotient"),
  "four_subspaces": ("core", "LinAlg.four_subspace_dims"),
  "algebraic_geometric_multiplicity": ("core", "LinAlg.geom_le_alg"),
  "distinct_eigenvalues_independent": ("core", "LinAlg.distinct_eig_indep_step (the induction step)"),
  "orthogonal_implies_independent": ("core", "LinAlg.orthogonal_indep_core"),
  "rank_inequalities": ("core", "LinAlg.rank_bounds_consistent"),
  "condition_number": ("core", "LinAlg.condition_ge_one"),
  "invertible_matrix": ("core",
    "LinAlg.inv_unique, LinAlg.inv_mul_rev (monoid arguments: associativity + two-sided identity only)"),
  "basis_existence_finite": ("partial",
    "LinAlg.list_induction_skeleton -- the termination skeleton only; the dependence-lemma step is not formalised"),

  # --- dim_core: universal in the entries, fixed dimension -----------------
  "matrix_mult_is_composition": ("dim_core", "LinAlg.mul_assoc2, LinAlg.mul_one2 (n = 2)"),
  "transpose": ("dim_core", "LinAlg.transpose_mul_rev, LinAlg.transpose_involutive (n = 2)"),
  "trace_cyclic": ("dim_core", "LinAlg.trace_mul_comm (n = 2)"),
  "determinant_multiplicative": ("dim_core", "LinAlg.det_mul (n = 2)"),
  "determinant_transpose": ("dim_core", "LinAlg.det_transpose (n = 2)"),
  "determinant_row_operations": ("dim_core",
    "LinAlg.det_row_op_R1/R2/R3 and LinAlg.det_smul (the det(kX) = k^2 det X trap), n = 2"),
  "determinant_triangular": ("dim_core", "LinAlg.det_triangular (n = 2)"),
  "adjugate": ("dim_core", "LinAlg.adjugate_identity (n = 2, singular X included)"),
  "cayley_hamilton": ("dim_core", "LinAlg.cayley_hamilton_2 (n = 2)"),
  "characteristic_polynomial": ("dim_core", "LinAlg.charpoly_2 (n = 2, universal in t)"),
  "char_poly_coefficients": ("dim_core", "LinAlg.charpoly_2 (n = 2: p(t) = t^2 - tr t + det)"),
  "cauchy_schwarz": ("dim_core",
    "LinAlg.lagrange_identity2/3 and LinAlg.cauchy_schwarz2/3 (Int coefficients, n = 2 and 3; the defect is exhibited as a sum of squares). The REAL-coefficient statement is cited"),
  "parallelogram_law": ("dim_core", "LinAlg.parallelogram (n = 2)"),
  "polarisation_identity": ("dim_core",
    "LinAlg.polarisation_real (n = 2, stated as 4*<u,v> = ... so the char != 2 dependence is explicit)"),
  "pythagorean_theorem": ("dim_core", "LinAlg.pythagoras (n = 2)"),
  "induced_norm": ("dim_core", "LinAlg.nrm2_nonneg (n = 2; what makes the sqrt well-typed)"),
  "gram_matrix": ("dim_core",
    "LinAlg.gram_psd, LinAlg.gram_psd_nonneg, LinAlg.gram_symmetric (n = 2)"),
  "self_adjoint_real_eigenvalues": ("dim_core",
    "LinAlg.symmetric_discriminant_nonneg (n = 2: the discriminant is a sum of squares) with LinAlg.rotation_discriminant_negative as the dropped-hypothesis witness"),
  "psd_characterisations": ("dim_core",
    "LinAlg.psd_2x2_complete_square with LinAlg.leading_minors_insufficient_for_psd (the leading-vs-all-principal-minors trap)"),
  "least_squares": ("dim_core", "LinAlg.normal_equations_residual_orthogonal (n = 2)"),

  # --- instance: decide at fixed numbers -----------------------------------
  "matrix_mult_noncommutative": ("instance",
    "LinAlg.ab_ne_ba, LinAlg.noncomm_but_trace_and_det_agree"),
  "non_diagonalisable_counterexample": ("instance", "LinAlg.jordan_block_defective"),
  "projection_matrix_characterisation": ("instance",
    "LinAlg.proj_orth_idem_and_symmetric vs LinAlg.proj_oblique_idem_not_symmetric"),
  "hat_matrix": ("instance", "LinAlg.idempotent_trace_eq_rank_both"),
  "spectral_theorem_symmetric": ("instance",
    "LinAlg.sym_spectral_instance (the 2x2 case worked explicitly). The general theorem is CITED: its Rayleigh/compactness step needs real analysis, unavailable Mathlib-free"),
  "sylvester_law_of_inertia": ("instance", "LinAlg.congruence_not_similarity"),
  "congruence": ("instance", "LinAlg.congruence_not_similarity"),
  "similar_invariants": ("instance", "LinAlg.charpoly_not_complete_invariant"),
}
