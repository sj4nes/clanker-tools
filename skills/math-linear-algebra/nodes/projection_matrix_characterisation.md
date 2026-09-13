# projection_matrix_characterisation

## Type
theorem

## Statement
Over R, a matrix P represents the ORTHOGONAL projection onto col(P) if and only if P^2 = P and P^T = P. (Over C: P^2 = P and P^* = P.) Idempotence alone gives only an oblique projection.

## Symbols
- `P` — type: element of R^{n x n}
- `tr P` — equals rank P for such a P

## Epistemic status
proved_theorem  ·  field_scope: real_or_complex

## Prerequisites (tsort edges into this node)
column_space, matrix_of_linear_map, orthogonal_decomposition, orthogonal_projection, real_number, transpose

## Hypotheses
F = R (or C with ^*)

## Proof provenance
technique: forward from orthogonal_projection. Conversely, P^2 = P gives V = im P (+) ker P; P^T = P gives ker P = (im P)^perp by adjoint_kernel_image, so the decomposition is orthogonal
derives_from: orthogonal_decomposition
lean_status: instance — LinAlg.proj_orth_idem_and_symmetric vs LinAlg.proj_oblique_idem_not_symmetric

## Type / well-formedness check
Well-formed. TWO conditions, both necessary: idempotence makes it a projection, self-adjointness makes it orthogonal. This is the theorem `math-statistics` uses for the hat matrix.

## Specialization / boundary cases
- P = I and P = 0: the trivial projections
- the hat matrix H = X(X^TX)^{-1}X^T: symmetric and idempotent, hence orthogonal projection onto col(X)
- tr P = rank P, since the eigenvalues of such a P are all 0 or 1 -- the identity behind residual degrees of freedom

## Hypothesis-dropped counterexamples
- **symmetry**: P = [[1,1],[0,0]] satisfies P^2 = P and is a projection onto the x-axis, but ALONG the line x + y = 0, not along its orthogonal complement. It is oblique: P^T != P. In regression this is the difference between OLS and a general weighted or instrumental-variables fit
- **idempotence**: a symmetric non-idempotent matrix is not a projection at all

## Common misuse
- calling any idempotent matrix a projection matrix in a least-squares context, where the orthogonality is what gives the normal equations
- using tr P = rank P for an oblique projection (it still holds for idempotents, but the geometric reading does not)

## In the wild
- the hat matrix and the residual-maker I - H in linear regression; Cochran's theorem in ANOVA, which decomposes I into orthogonal idempotents

## Related nodes (non-prerequisite)
- equivalent_to: orthogonal_projection
- required_by: hat_matrix, spectral_decomposition

## Sources
strang_5e, rao_linear_statistical_inference
