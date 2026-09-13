# singular_value_decomposition

## Type
theorem

## Statement
Every A in F^{m x n} factors as A = U Sigma V^* with U in F^{m x m} and V in F^{n x n} unitary and Sigma in R^{m x n} diagonal with entries sigma_1 >= ... >= sigma_p >= 0. Equivalently A = sum_{i=1}^r sigma_i u_i v_i^* with r = rank A. NO hypothesis on A whatsoever -- not square, not symmetric, not full rank.

## Symbols
- `u_i, v_i` — the left and right singular vectors
- `r` — rank A

## Epistemic status
proved_theorem  ·  field_scope: real_or_complex

## Prerequisites (tsort edges into this node)
gram_schmidt, matrix_rank, orthogonal_matrix, orthonormal_basis, singular_values, spectral_theorem_symmetric

## Hypotheses
F = R or C

## Proof provenance
technique: diagonalise the Hermitian PSD A^*A = V D V^* by spectral_theorem_symmetric; set sigma_i = sqrt(d_i) and u_i = Av_i/sigma_i for sigma_i > 0, which are orthonormal by construction; extend to an orthonormal basis of F^m by gram_schmidt
derives_from: singular_values
lean_status: cited

## Type / well-formedness check
Well-formed for EVERY matrix over R or C. The unqualified generality is the point: where the eigendecomposition needs diagonalisability and the spectral theorem needs symmetry, the SVD needs nothing.

## Specialization / boundary cases
- A symmetric PSD: U = V and the SVD is the eigendecomposition
- A orthogonal: Sigma = I
- A = uv^*: a single term, sigma_1 = ||u|| ||v||
- the geometric reading: every linear map is a rotation, then an axis-aligned scaling, then another rotation

## Hypothesis-dropped counterexamples
- **uniqueness_fails**: the singular VALUES are unique, but U and V are not: any repeated singular value allows rotating within its subspace, and even for distinct values each pair (u_i, v_i) can be multiplied by a common unit scalar. Claims of a 'unique SVD' are wrong
- **no_hypothesis_can_be_dropped_because_there_are_none**: the only requirement is F in {R, C}. Over a general field there is no SVD, because there is no notion of nonnegative square root

## Common misuse
- expecting a unique U and V
- interpreting singular vectors as eigenvectors of A

## In the wild
- principal component analysis (the SVD of the centred data matrix), latent semantic analysis, image compression, and every low-rank approximation method -- via eckart_young
- the numerically definitive way to compute rank, null space, range, and pseudoinverse of a matrix

## Related nodes (non-prerequisite)
- generalizes: spectral_theorem_symmetric
- required_by: svd_four_subspaces, moore_penrose_pseudoinverse, eckart_young

## Sources
trefethen_bau, golub_van_loan_4e
