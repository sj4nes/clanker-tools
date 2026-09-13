# moore_penrose_pseudoinverse

## Type
construction

## Statement
A^+ = V Sigma^+ U^* where Sigma^+ inverts the nonzero singular values and transposes. It is the UNIQUE matrix satisfying the four Penrose conditions (AA^+A = A, A^+AA^+ = A^+, (AA^+)^* = AA^+, (A^+A)^* = A^+A). A^+b is the MINIMUM-NORM least-squares solution, and AA^+ is the orthogonal projection onto col(A).

## Symbols
- `A^+` — the pseudoinverse, type: element of F^{n x m}
- `Sigma^+` — diagonal with 1/sigma_i for sigma_i > 0, else 0

## Epistemic status
constructive_result  ·  field_scope: real_or_complex

## Prerequisites (tsort edges into this node)
least_squares, orthogonal_projection, singular_value_decomposition, svd_four_subspaces

## Hypotheses
F = R or C

## Proof provenance
technique: existence from the SVD by direct verification of the four conditions; uniqueness by a standard algebraic argument from them. The minimum-norm property because A^+b lies in row(A) = null(A)^perp, and any other minimiser adds an element of null(A), which by Pythagoras only increases the norm
derives_from: singular_value_decomposition
lean_status: cited

## Type / well-formedness check
Well-formed for EVERY A, including rank-deficient and rectangular. Uniqueness under the four conditions is what makes A^+ canonical rather than one generalised inverse among many.

## Specialization / boundary cases
- A invertible: A^+ = A^{-1}
- A of full column rank: A^+ = (A^*A)^{-1}A^*, the least-squares formula
- A of full row rank: A^+ = A^*(AA^*)^{-1}, the minimum-norm solution of an underdetermined system
- A = 0: A^+ = 0

## Hypothesis-dropped counterexamples
- **discontinuity_in_A**: A^+ is NOT a continuous function of A across a rank change: for A_eps = diag(1, eps), A_eps^+ = diag(1, 1/eps) blows up as eps -> 0, while A_0^+ = diag(1,0). This is the practical reason a truncated (regularised) pseudoinverse is used in practice, and the reason a rank tolerance is unavoidable
- **(AB)^+ != B^+A^+**: the reversal rule holds for inverses but FAILS for pseudoinverses in general -- a common and silent error

## Common misuse
- using the reversal rule for pseudoinverses
- applying A^+ numerically without truncating tiny singular values

## In the wild
- the canonical solution of rank-deficient least squares; ridge regression as a regularised pseudoinverse; the minimum-norm solution in underdetermined inverse problems and in over-parameterised model fitting

## Related nodes (non-prerequisite)
- generalizes: invertible_matrix

## Sources
golub_van_loan_4e, horn_johnson_2e
