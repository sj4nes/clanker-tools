# What the Lean kernel actually verified

`validation/proof-checks.lean` is **Mathlib-free** (Lean 4.33 core only) and
exits 0 with **no `sorry`, no `axiom`, and no warnings**. This file records, per
node, the split between *what the kernel checked* and *what remains cited* —
and is deliberately written so the two are impossible to confuse.

## The honesty vocabulary

| status | meaning | count |
|---|---|---|
| `core` | the **general** statement is proved | 13 |
| `dim_core` | **universal in the matrix entries, at a fixed dimension** (n = 2, sometimes 3) | 19 |
| `instance` | `decide`d at fixed numbers — a check, never a proof | 8 |
| `partial` | part of the argument formalised | 1 |
| `cited` | proved elsewhere | 110 |
| `stated_not_proved` | boundary node | 2 |

`dim_core` is this capsule's addition to the sibling capsules' vocabulary, and
it carries real information. `det(AB) = det(A) det(B)` at n = 2 is proved with
all eight entries as bound variables — that is a genuine proof of the n = 2
case, not a numeric spot-check. It is *not* a proof of the theorem, which
quantifies over n. Calling it `core` would overclaim; calling it `instance`
would underclaim.

## Why the general statements are not reachable here

Mathlib-free Lean has no `Matrix`, no `Module`, no `Real`, no `ring`, no
`linarith`. Consequently:

- **No quantification over dimension.** Every matrix result is proved at a fixed
  n via an explicit `structure M2`. Building an n-indexed matrix library is a
  project in itself and is out of scope for Release 0.1.
- **No real numbers.** Everything is over `Int`. Square roots, limits,
  compactness, and the extreme value theorem are unavailable, so
  `spectral_theorem_symmetric`, `singular_value_decomposition`,
  `cholesky_factorisation`, `gram_schmidt`, and the general `cauchy_schwarz`
  are **cited** at full generality — with their Int-coefficient / fixed-dimension
  shadows proved below.
- **`Int` division truncates.** Half-factors are never written as `/ 2`;
  `polarisation_real` is stated as `4 * <u,v> = ...`, which has the pleasant
  side effect of making its `char ≠ 2` dependence explicit in the statement.

## `core` — the general statement is proved (13 nodes)

These are the arithmetic and abstract-algebraic cores whose full generality
fits in Lean core.

| node | declaration | what is proved |
|---|---|---|
| `vector_space_basic_consequences` | `smul_zero_eq_zero`, `zero_smul_vec`, `neg_one_smul`, `no_zero_smul_divisors` | `0v = 0`, `a0 = 0`, `(-1)v = -v`, and `av = 0 ⟹ a = 0 ∨ v = 0` — the last via `Int.mul_eq_zero`, the one place field structure is used |
| `dimension_well_defined` | `basis_card_eq` | two Steinitz bounds give equality (`omega`) |
| `rank_nullity` | `rank_nullity` | `dim V = rank + nullity` bounds both summands |
| `injective_surjective_equivalence` | `inj_iff_surj_of_dim_eq` | `nullity = 0 ↔ rank = dim W`, given equal finite dimensions |
| `dimension_formula_sum` | `dim_sum_inter` | the Grassmann formula as Nat arithmetic |
| `quotient_dimension` | `dim_quotient` | `dim U + (dim V − dim U) = dim V`, guarded by `dim U ≤ dim V` |
| `four_subspaces` | `four_subspace_dims` | the four dimensions sum correctly in both ambient spaces |
| `algebraic_geometric_multiplicity` | `geom_le_alg` | `1 ≤ geom ≤ alg`, with the gap made explicit |
| `distinct_eigenvalues_independent` | `distinct_eig_indep_step` | the induction step: `a(λᵢ − λₖ) = 0` with `λᵢ ≠ λₖ` forces `a = 0` |
| `orthogonal_implies_independent` | `orthogonal_indep_core` | a positive squared norm forces the coefficient to vanish |
| `rank_inequalities` | `rank_bounds_consistent` | the upper bounds and Sylvester's lower bound are consistent |
| `condition_number` | `condition_ge_one` | `κ ≥ 1` always |
| `invertible_matrix` | `inv_unique`, `inv_mul_rev` | uniqueness of the inverse and `(XY)⁻¹ = Y⁻¹X⁻¹` — **monoid arguments**, using only associativity and a two-sided identity, so genuinely general |

## `dim_core` — universal in the entries, fixed dimension (19 nodes)

Every matrix entry is a bound variable. These prove the n = 2 (or n = 3) case.

| node | declaration(s) | dimension |
|---|---|---|
| `matrix_mult_is_composition` | `mul_assoc2`, `mul_one2` | 2 |
| `transpose` | `transpose_mul_rev`, `transpose_involutive` | 2 |
| `trace_cyclic` | `trace_mul_comm` | 2 |
| `determinant_multiplicative` | `det_mul` | 2 |
| `determinant_transpose` | `det_transpose` | 2 |
| `determinant_row_operations` | `det_row_op_R1`/`R2`/`R3`, `det_smul` | 2 |
| `determinant_triangular` | `det_triangular` | 2 |
| `adjugate` | `adjugate_identity` | 2 |
| `cayley_hamilton` | `cayley_hamilton_2` | 2 |
| `characteristic_polynomial` | `charpoly_2` | 2, universal in `t` |
| `char_poly_coefficients` | `charpoly_2` | 2 |
| `cauchy_schwarz` | `lagrange_identity2`/`3`, `cauchy_schwarz2`/`3` | 2 and 3 |
| `parallelogram_law` | `parallelogram` | 2 |
| `polarisation_identity` | `polarisation_real` | 2 |
| `pythagorean_theorem` | `pythagoras` | 2 |
| `induced_norm` | `nrm2_nonneg` | 2 |
| `gram_matrix` | `gram_psd`, `gram_psd_nonneg`, `gram_symmetric` | 2 |
| `self_adjoint_real_eigenvalues` | `symmetric_discriminant_nonneg` | 2 |
| `psd_characterisations` | `psd_2x2_complete_square` | 2 |
| `least_squares` | `normal_equations_residual_orthogonal` | 2 |

Four of these deserve comment because the Lean statement is sharper than the
prose one:

- **`det_smul`** proves `det(kX) = k² det X` at n = 2 — the `det(kA) = k det A`
  trap, machine-checked rather than merely warned about.
- **`adjugate_identity`** is proved for **every** `X`, including singular ones;
  no invertibility hypothesis appears.
- **`cayley_hamilton_2`** is proved by computation. The familiar pseudo-proof
  ("substitute `t = X` into `det(tI − X)`") is ill-typed, and the node page says
  so; this declaration is what the real argument reduces to at n = 2.
- **`lagrange_identity2`/`3`** exhibit the Cauchy–Schwarz **defect** as an
  explicit sum of squares, so the *equality case* (linear dependence) is visible
  in the statement, not just the inequality.

## `instance` — `decide` at fixed numbers (8 nodes)

Checks, not proofs. Several are deliberately **paired** so that a positive case
and its dropped-hypothesis counterexample are checked side by side.

| node | declaration | what it witnesses |
|---|---|---|
| `matrix_mult_noncommutative` | `ab_ne_ba`, `noncomm_but_trace_and_det_agree` | `AB ≠ BA`, **yet** trace and determinant still agree — so neither detects noncommutativity |
| `non_diagonalisable_counterexample` | `jordan_block_defective` | `J = (1 1; 0 1)` is defective and `Jᵏ = (1 k; 0 1)` grows **linearly** despite `\|λ\| = 1` |
| `projection_matrix_characterisation` | `proj_orth_idem_and_symmetric` **vs** `proj_oblique_idem_not_symmetric` | the paired witness that idempotence alone gives an *oblique* projection; symmetry is a necessary second condition |
| `hat_matrix` | `idempotent_trace_eq_rank_both` | `tr P = rank P` holds for the **oblique** projection too — so the trace identity does **not** certify orthogonality |
| `spectral_theorem_symmetric` | `sym_spectral_instance` | `(2 1; 1 2)` diagonalised explicitly, eigenvectors orthogonal |
| `sylvester_law_of_inertia`, `congruence` | `congruence_not_similarity` | `diag(1,−1) ~_c diag(4,−9)` with **different** trace and determinant — congruence is not similarity |
| `similar_invariants` | `charpoly_not_complete_invariant` | `I` and `J` share a characteristic polynomial and are not similar |

The paired entries are the point. A capsule that checked only the positive case
would let a reader conclude that idempotence implies orthogonal projection, or
that `tr P = rank P` implies symmetry. Both pairs are in the kernel.

## `partial` (1 node)

- **`basis_existence_finite`** — `list_induction_skeleton` formalises the
  termination skeleton that both halves of the theorem run (strip a redundant
  vector; adjoin a vector outside the span). The `dependence_lemma` step itself
  is **not** formalised. The node is `partial`, not `core`.

## Cited only — not formalised here (110 nodes)

Everything else. The load-bearing ones, with the reason:

| node | why it is cited |
|---|---|
| `spectral_theorem_symmetric` (general) | the Rayleigh/compactness existence step needs real analysis |
| `singular_value_decomposition`, `singular_values` | need nonnegative square roots |
| `cholesky_factorisation` | needs square roots over an ordered field |
| `gram_schmidt`, `qr_factorisation` | need normalisation, hence square roots |
| `cauchy_schwarz` (real coefficients) | the `Int` case is proved; the real case needs `Real` |
| `basis_existence_general` | needs Zorn's lemma — cited from `math-sets-functions-cardinality` |
| `rref_uniqueness`, `gaussian_elimination` | need an n-indexed matrix representation |
| `determinant_existence_uniqueness`, `leibniz_formula` | quantify over `S_n` for arbitrary n |
| `schur_triangularisation`, `spectral_theorem_normal` | need `C` and the cited fundamental theorem of algebra |
| `jordan_normal_form`, `smith_normal_form_boundary` | `stated_not_proved` boundary nodes (see `scope.md`) |
| `permutation_sign` | the parity well-definedness argument needs `S_n` for arbitrary n |

## How overclaiming is prevented

Three mechanisms, all wired into `build/all.sh`:

1. **`build/leanmap.py`** is the single authoritative `lean_status` / `lean_ref`
   table. `build/nodespec.py` applies it *over* whatever a spec module claims.
2. **A node absent from that map is forced to `cited` with no ref.** The default
   is the weakest status; every upgrade must name a declaration.
3. **`build/check-lean-refs.py`** verifies that every `LinAlg.*` named in a
   `lean_ref` exists in the `.lean` file, that every non-cited node names at
   least one, and that no `cited` node names any. It currently resolves **55
   references against 87 declarations**.

The `lean_status` drift that `math-logic-and-proof` and `math-probability` had
to be audited for retrospectively (see `BACKLOG.md`) is structurally impossible
here: the refs and the kernel cannot disagree and still build.

## The standing limitation

A `dim_core` proof at n = 2 is evidence, not a theorem. A `decide` instance is a
spot-check. `bc` instances (`validation/instance-checks.md`) are sanity checks
and counterexample hunts, never proofs. Every result in this capsule remains
conditional on its stated hypotheses, on the foundational stance in
`conventions.md`, and on its cited source.
