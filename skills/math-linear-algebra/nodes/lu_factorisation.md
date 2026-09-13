# lu_factorisation

## Type
construction

## Statement
A = LU with L unit lower triangular and U upper triangular, recording Gaussian elimination without row swaps. In general PA = LU with P a permutation. Solving then costs two triangular solves, ~n^2 each, after the ~(2/3)n^3 factorisation.

## Symbols
- `L` — unit lower triangular (1s on the diagonal)
- `U` — upper triangular
- `P` — a permutation matrix

## Epistemic status
constructive_result  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
elementary_matrix, gaussian_elimination, triangular_matrix

## Hypotheses
every leading principal minor nonzero, for the unpivoted form

## Proof provenance
technique: each elimination step is left multiplication by a unit lower triangular elementary matrix; the product and the inverse of such matrices are again unit lower triangular
derives_from: gaussian_elimination
lean_status: cited

## Type / well-formedness check
Well-formed; the L factor is exactly the record of the R3 multipliers, and unit-triangularity makes the factorisation unique when it exists.

## Specialization / boundary cases
- A symmetric positive definite: L can be taken with U = L^T scaled, which is cholesky_factorisation
- A already upper triangular: L = I

## Hypothesis-dropped counterexamples
- **nonvanishing_leading_minors**: A = [[0,1],[1,0]] admits NO unpivoted LU: the first pivot is 0. Yet it is perfectly invertible -- existence of LU is strictly stronger than invertibility, which is precisely why P is needed
- **exact_arithmetic**: even when LU exists, a tiny pivot makes it numerically useless (lu_pivoting_regime)

## Common misuse
- reusing an LU factorisation after modifying A: it must be recomputed (or updated by a rank-one update formula)
- assuming LU always exists for invertible A

## In the wild
- the standard dense direct solver: factor once, solve for many right-hand sides; the basis of LAPACK's dgesv

## Related nodes (non-prerequisite)
- special_case_of: 
- required_by: lu_pivoting_regime, cholesky_factorisation

## Sources
golub_van_loan_4e, strang_5e
