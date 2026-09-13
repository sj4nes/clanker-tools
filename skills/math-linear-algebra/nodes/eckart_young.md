# eckart_young

## Type
theorem

## Statement
The best rank-k approximation to A in BOTH the spectral and the Frobenius norm is the truncated SVD A_k = sum_{i=1}^k sigma_i u_i v_i^*, with errors ||A - A_k||_2 = sigma_{k+1} and ||A - A_k||_F = sqrt(sum_{i>k} sigma_i^2).

## Symbols
- `A_k` — the rank-k truncation of the SVD
- `sigma_{k+1}` — the first discarded singular value

## Epistemic status
proved_theorem  ·  field_scope: real_or_complex

## Prerequisites (tsort edges into this node)
courant_fischer, matrix_norms, matrix_rank, singular_value_decomposition

## Hypotheses
k < rank A, F = R or C

## Proof provenance
technique: the error value by direct computation. Optimality: any B of rank <= k has a null space of dimension >= n-k, which must intersect span(v_1..v_{k+1}) nontrivially; on that intersection ||(A-B)x|| = ||Ax|| >= sigma_{k+1}||x|| by courant_fischer
derives_from: singular_value_decomposition
lean_status: cited

## Type / well-formedness check
Well-formed. The remarkable content is that the SAME truncation is optimal for two quite different norms -- and in fact for every unitarily invariant norm (Mirsky's theorem, cited).

## Specialization / boundary cases
- k = rank A: zero error
- k = 0: the error is ||A||_2 = sigma_1, correctly
- A = diag(3,2): the best rank-1 approximation is diag(3,0) with spectral error 2

## Hypothesis-dropped counterexamples
- **the_norm_being_unitarily_invariant**: under the ENTRYWISE max norm the truncated SVD is NOT optimal -- optimality is specific to unitarily invariant norms, and this is exactly Mirsky's generalisation
- **uniqueness**: if sigma_k = sigma_{k+1} the optimal A_k is not unique, because the truncation can be taken in different directions within the tied subspace
- **structure_is_not_preserved**: the truncated SVD of a nonnegative matrix generally has negative entries, and of a sparse matrix is dense. Structured low-rank approximation (NMF, sparse PCA) is a different and much harder problem with no closed form

## Common misuse
- assuming the truncated SVD is the best STRUCTURED approximation (nonnegative, sparse, Hankel) -- it is the best unconstrained one
- reporting a unique answer when singular values are tied

## In the wild
- PCA's dimension reduction is exactly this theorem: retaining the top k components is optimal in mean squared error
- image and model compression, latent semantic indexing, and the theoretical justification of spectral methods generally

## Related nodes (non-prerequisite)
- approximates: singular_value_decomposition

## Sources
eckart_young_1936, trefethen_bau
