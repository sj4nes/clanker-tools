# cholesky_factorisation

## Type
construction

## Statement
A real symmetric POSITIVE DEFINITE A factors UNIQUELY as A = LL^T with L lower triangular having strictly positive diagonal. Cost ~ (1/3)n^3, half that of LU, and NO PIVOTING is ever required.

## Symbols
- `L` — the Cholesky factor
- `L_{ii}` — required strictly positive, which fixes uniqueness

## Epistemic status
constructive_result  ·  field_scope: ordered_field

## Prerequisites (tsort edges into this node)
induction_principle, lu_factorisation, positive_definite, triangular_matrix

## Hypotheses
A symmetric positive definite

## Proof provenance
technique: induction on n: A = [[a, b^T],[b, A']] with a > 0 (since e_1^TAe_1 = a); factor out, and the remaining block is the Schur complement A' - bb^T/a, which is again positive definite (schur_complement)
derives_from: positive_definite
lean_status: cited

## Type / well-formedness check
Well-formed. Positive definiteness is what makes every square root taken in the algorithm a square root of a POSITIVE number, so the factorisation exists over R without ever leaving R.

## Specialization / boundary cases
- A = I: L = I
- n = 1: A = [a] with a > 0 gives L = [sqrt a]
- A = R^TR from qr_factorisation applied to the normal equations: the Cholesky factor of A^TA is exactly the R of the QR of A

## Hypothesis-dropped counterexamples
- **positive_definiteness**: A = [[0,1],[1,0]] is symmetric, invertible, and INDEFINITE: the algorithm's first step needs sqrt(0) then divides by it. Cholesky failing is in fact the standard NUMERICAL TEST for positive definiteness -- attempt the factorisation and see whether it completes
- **semidefinite_case**: a singular PSD A has a Cholesky-like factorisation with a zero on the diagonal, but it is no longer unique

## Common misuse
- applying Cholesky to a symmetric indefinite matrix (use LDL^T or Bunch-Kaufman instead)
- testing positive definiteness by computing all eigenvalues when attempting Cholesky is ~3x cheaper

## In the wild
- sampling from a multivariate normal: x = mu + L z with z standard normal has covariance LL^T = Sigma
- the standard solver for the normal equations and for every kernel-method linear system; Kalman filter covariance updates

## Related nodes (non-prerequisite)
- special_case_of: lu_factorisation
- required_by: psd_characterisations, simultaneous_diagonalisation

## Sources
golub_van_loan_4e, higham_asna_2e
