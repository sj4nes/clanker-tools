# Cross-capsule relations — `discharges` (NOT a `tsort` edge in either capsule)

`math-statistics` Release 0.1 carries a single cited node,
`linear_algebra_background`, described in its own YAML as:

> Assumed without a capsule: vector spaces and subspaces, rank, transpose,
> inverse; symmetric and positive-(semi)definite matrices; the spectral theorem
> for real symmetric matrices; orthogonal projection onto a subspace and its
> idempotent symmetric projection matrix; trace; quadratic forms `x^T A x`.
> **FLAGGED for a future math-linear-algebra capsule.**

This capsule is that future capsule. Every item on the list is a developed node
here.

## Why this is metadata and not a graph edge

Each capsule's `validation/graph-check.sh` only knows its own `nodes.tsv`, and
the atlas-style separation of cross-capsule edges into their own layer is
deliberate — splicing `math-linear-algebra:*` ids into
`math-statistics/edges/dependencies.plan` would break that capsule's own build.
Same pattern as `math-sets-functions-cardinality` Release 0.2 (its logic
primitives against `math-logic-and-proof`) and `physics-thermoacoustics`
(its `small_amplitude` / `time_harmonic` roots against `physics-acoustics`).

Unlike the `math-sets` ↔ `math-logic` case, this discharge is **not** mutually
grounding: linear algebra does not presuppose statistics. The direction is
clean, so these are real dependencies recorded in a separate layer, not a
circularity being papered over.

## The discharge table

| `math-statistics` assumes | developed here as | node type |
|---|---|---|
| vector spaces and subspaces | `vector_space`, `subspace`, `subspace_criterion` | structure, definition |
| rank | `rank`, `matrix_rank`, `row_rank_equals_column_rank`, `rank_nullity` | definition, theorem |
| transpose | `transpose`, `transpose_convention`, `conjugate_transpose` | definition, convention |
| inverse | `invertible_matrix`, `invertibility_equivalences`, `one_sided_inverse_square` | definition, theorem |
| symmetric matrices | `self_adjoint` (real case: `A = A^T`) | definition |
| positive-(semi)definite matrices | `positive_definite`, `psd_characterisations`, `gram_matrix`, `cholesky_factorisation` | definition, theorem, construction |
| spectral theorem for real symmetric matrices | `spectral_theorem_symmetric`, `spectral_decomposition` | theorem, corollary |
| orthogonal projection onto a subspace | `orthogonal_projection`, `orthogonal_decomposition`, `best_approximation` | construction, theorem |
| its idempotent symmetric projection matrix | `projection_matrix_characterisation`, `hat_matrix` | theorem, construction |
| trace | `trace`, `trace_cyclic` | definition, proposition |
| quadratic forms `x^T A x` | `quadratic_form`, `congruence`, `sylvester_law_of_inertia` | definition, theorem |

**All 11 discharged.**

## Per-consumer check

`linear_algebra_background` has ten `tsort` consumers inside `math-statistics`.
Each is listed with the node here that actually supplies what it needs:

| `math-statistics` node | needs | supplied by |
|---|---|---|
| `fisher_information_matrix` | symmetric PSD matrices, matrix inverse | `positive_definite`, `psd_characterisations`, `invertible_matrix` |
| `normal_sample_mean_variance_independence` | orthogonal transformation preserving the standard normal | `orthogonal_matrix`, `isometry_characterisation` |
| `cochran_theorem` | idempotent symmetric matrices summing to `I`, with ranks summing to `n` | `spectral_decomposition`, `projection_matrix_characterisation` |
| `one_way_anova_identity` | orthogonal decomposition of `R^n` into centring and between-group parts | `orthogonal_decomposition`, `orthogonal_projection` |
| `linear_model` | column space, rank, full-column-rank identifiability | `column_space`, `matrix_rank`, `rank_nullity` |
| `normal_equations` | `A^T A x = A^T b` as the stationarity condition | `least_squares` |
| `ols_is_projection` | OLS fitted values are the projection onto `col(X)` | `hat_matrix`, `best_approximation` |
| `unbiased_error_variance_estimator` | `tr(I - H) = n - p` | `trace_cyclic`, `hat_matrix` |
| `gauss_markov_theorem` | PSD ordering of covariance matrices; the cross-term vanishing | `positive_definite`, `adjoint_kernel_image` |
| `ols_distribution_under_normal_errors` | `Var(Ax) = A Var(x) A^T`; quadratic forms in normals | `quadratic_form`, `spectral_theorem_symmetric` |

**All 10 consumers supplied.** No `math-statistics` use of
`linear_algebra_background` needs a linear-algebra fact this capsule does not
develop.

## What is NOT discharged

Two gaps, stated rather than hidden:

1. **`math-statistics` never needs `C`.** Its Gaussian theory is real. The
   complex half of this capsule (`spectral_theorem_normal`,
   `schur_triangularisation`, `conjugate_transpose`) is developed for the
   capsule's own coherence, not for the discharge.
2. **This capsule's own floor is not fully discharged.** `real_number`,
   `complex_number`, `polynomial_ring`, `compactness_cited`, and
   `extreme_value_cited` are cited roots. `real_number`, `compactness_cited`,
   and `extreme_value_cited` *are* developed in the stack
   (`math-number-systems`, `math-real-analysis`) and could be discharged the
   same way in a Release 0.2; `complex_number` and `polynomial_ring` are
   genuinely absent from the stack, as `fundamental_theorem_of_algebra` already
   records.

## Recommended edit to `math-statistics`

Mirror of the `physics-thermoacoustics` pattern — a metadata note, not a graph
change:

- `math-statistics/nodes/nodes.tsv`: annotate the `linear_algebra_background`
  row "discharged by math-linear-algebra (see its edges/cross-capsule.md)".
- `math-statistics/results/linear_algebra_background.yaml`: drop "FLAGGED for a
  future math-linear-algebra capsule" in favour of the citation.
- `math-statistics/scope.md`: point the "Release 0.2 territory" line at this
  capsule.

`math-statistics`'s own graph is unchanged by this and stays green.
