# schur_complement

## Type
construction

## Statement
For M = [[A,B],[C,D]] with A invertible, the Schur complement of A is M/A = D - C A^{-1} B. Then det M = det(A) det(M/A), M is invertible iff M/A is, and for symmetric M, M is positive definite iff A and M/A both are.

## Symbols
- `M/A` — the Schur complement, type: matrix of the same shape as D

## Epistemic status
constructive_result  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
block_matrix, invertible_matrix

## Hypotheses
A invertible

## Proof provenance
technique: the block factorisation above, then determinant multiplicativity on block triangular factors
derives_from: block_matrix
lean_status: cited

## Type / well-formedness check
Well-formed when A is invertible. It arises from the block elimination M = [[I,0],[CA^{-1},I]] [[A,0],[0,M/A]] [[I,A^{-1}B],[0,I]], which is block LU.

## Specialization / boundary cases
- A = [a] a 1x1 scalar: M/A = D - cb/a, the ordinary elimination step
- C = B^T and M symmetric: the positive-definiteness criterion, which is exactly how conditional covariance matrices in statistics are shown to be PSD

## Hypothesis-dropped counterexamples
- **invertibility_of_A**: if A is singular the Schur complement is undefined; a generalised Schur complement using the pseudoinverse recovers part of the theory (see moore_penrose_pseudoinverse)

## Common misuse
- assuming the determinant identity without A invertible

## In the wild
- the conditional covariance of a Gaussian: Var(X|Y) is exactly the Schur complement of the Y-block, which is why conditional covariances are automatically PSD
- block elimination in interior-point and KKT solvers

## Related nodes (non-prerequisite)
- generalizes: determinant_triangular
- required_by: psd_characterisations

## Sources
horn_johnson_2e, boyd_vandenberghe
