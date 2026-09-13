# svd_four_subspaces

## Type
corollary

## Statement
With r = rank A: u_1..u_r is an orthonormal basis of col(A), u_{r+1}..u_m of null(A^*); v_1..v_r of row(A) (i.e. col(A^*)), and v_{r+1}..v_n of null(A). The SVD delivers ORTHONORMAL bases for all four fundamental subspaces at once.

## Symbols
- `r` — rank A, = the number of nonzero singular values

## Epistemic status
corollary  ·  field_scope: real_or_complex

## Prerequisites (tsort edges into this node)
adjoint_kernel_image, four_subspaces, orthonormal_basis, singular_value_decomposition

## Hypotheses
A in F^{m x n}, F = R or C

## Proof provenance
technique: Av_i = sigma_i u_i shows Av_i = 0 exactly for i > r, giving the null space; the u_i for i <= r then span the image, and the orthogonal complements follow from adjoint_kernel_image
derives_from: singular_value_decomposition
lean_status: cited

## Type / well-formedness check
Well-formed. This upgrades four_subspaces (dimensions) and adjoint_kernel_image (orthogonality) to explicit orthonormal bases -- the strongest form of the four-subspace picture.

## Specialization / boundary cases
- A of full column rank: no v's left over, null(A) = {0}
- A square invertible: r = n = m and both null spaces are trivial

## Hypothesis-dropped counterexamples
- **numerical_rank**: deciding r requires a THRESHOLD on the singular values in floating point; 'rank' is not a computable property of a floating-point matrix, and the SVD makes this explicit (small nonzero sigma) where elimination hides it

## Common misuse
- reading r off exact zeros of Sigma in a numerical computation without a tolerance

## Related nodes (non-prerequisite)
- generalizes: four_subspaces
- required_by: moore_penrose_pseudoinverse

## Sources
strang_5e, trefethen_bau
