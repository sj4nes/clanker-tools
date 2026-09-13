# orthogonal_matrix

## Type
definition

## Statement
Q in R^{n x n} is orthogonal if Q^TQ = QQ^T = I; U in C^{n x n} is unitary if U^*U = I. Equivalently the columns (and rows) are orthonormal, Q^{-1} = Q^T, and |det Q| = 1. The orthogonal matrices form a group O(n).

## Symbols
- `Q` — orthogonal
- `U` — unitary
- `O(n), U(n)` — the orthogonal and unitary groups

## Epistemic status
definition  ·  field_scope: real_or_complex

## Prerequisites (tsort edges into this node)
adjoint_operator, conjugate_transpose, invertible_matrix, orthonormal_basis

## Hypotheses
Q square for the two-sided identity

## Proof provenance
technique: Q^TQ = I says the (i,j) entry is <q_i, q_j> = delta_{ij}; the group property from (QR)^T(QR) = R^TQ^TQR = I
derives_from: orthonormal_basis
lean_status: cited

## Type / well-formedness check
Well-formed for SQUARE matrices, where Q^TQ = I and QQ^T = I are equivalent by one_sided_inverse_square. For rectangular Q with m > n only Q^TQ = I can hold -- QQ^T is then a rank-n projection, NOT the identity, which is exactly the reduced-QR situation.

## Specialization / boundary cases
- rotations and reflections in R^2; det = +1 for rotations, -1 for reflections
- permutation matrices are orthogonal
- the Q of a QR factorisation has orthonormal COLUMNS but is generally rectangular, so QQ^T is a projection

## Hypothesis-dropped counterexamples
- **squareness**: for Q in R^{m x n} with m > n and Q^TQ = I, QQ^T is the projection onto col(Q), not I. Treating a reduced-QR Q as 'orthogonal' in the two-sided sense is a standard error
- **det_pm_one_is_not_sufficient**: det = +-1 does NOT imply orthogonal: [[1,1],[0,1]] has det 1 and is not orthogonal. Orthogonality is a much stronger, metric condition

## Common misuse
- inferring orthogonality from det = 1
- assuming a rectangular Q with orthonormal columns satisfies QQ^T = I

## In the wild
- numerically stable factorisations (QR, SVD) use orthogonal transformations precisely because they preserve the 2-norm and hence do not amplify error
- rotations in graphics and robotics; the orthogonal design matrices of balanced experiments

## Related nodes (non-prerequisite)
- required_by: isometry_characterisation, spectral_theorem_symmetric, singular_value_decomposition

## Sources
horn_johnson_2e, trefethen_bau
