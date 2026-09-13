# courant_fischer

## Type
theorem

## Statement
For real symmetric A with eigenvalues lambda_1 >= ... >= lambda_n: lambda_k = max over k-dimensional subspaces S of min_{x in S, x != 0} R_A(x), and dually lambda_k = min over (n-k+1)-dimensional S of the max. In particular lambda_1 = max R_A and lambda_n = min R_A.

## Symbols
- `S` — a subspace of the stated dimension
- `lambda_k` — the k-th largest eigenvalue

## Epistemic status
proved_theorem  ·  field_scope: real_or_complex

## Prerequisites (tsort edges into this node)
dimension_formula_sum, orthonormal_basis, quadratic_form, rayleigh_quotient, spectral_theorem_symmetric

## Hypotheses
A real symmetric

## Proof provenance
technique: diagonalise by the spectral theorem so R_A(x) = sum lambda_i |c_i|^2 / sum |c_i|^2, a weighted average of the eigenvalues; then a dimension-counting argument (S of dimension k must meet the span of the last n-k+1 eigenvectors nontrivially) gives both inequalities
derives_from: spectral_theorem_symmetric
lean_status: cited

## Type / well-formedness check
Well-formed given a real symmetric A and its ordered real spectrum (both supplied by spectral_theorem_symmetric). The characterisation is BASIS-FREE and does not mention eigenvectors, which is what makes it robust under perturbation.

## Specialization / boundary cases
- k = 1: lambda_1 = max R_A over the unit sphere, and k = n: lambda_n = min
- CAUCHY INTERLACING: deleting a row and the matching column of A gives B with lambda_k(A) >= lambda_k(B) >= lambda_{k+1}(A)
- WEYL: |lambda_k(A+E) - lambda_k(A)| <= ||E||_2, so symmetric eigenvalues are perfectly conditioned

## Hypothesis-dropped counterexamples
- **symmetry**: for a non-symmetric matrix the eigenvalues are not real, cannot be ordered, and are NOT well-conditioned: a Jordan block perturbed by epsilon in the corner has eigenvalues moving by epsilon^{1/n}. Everything in this node depends on symmetry
- **finite_dimensionality**: the min-max principle extends to compact self-adjoint operators, but not to general ones

## Common misuse
- applying eigenvalue-perturbation intuition from the symmetric case to a general matrix, where conditioning can be catastrophic
- using the min-max form with the wrong subspace dimension (the two forms use k and n-k+1)

## In the wild
- eigenvalue interlacing under adding a data point or a constraint; the stability of PCA directions under sampling noise
- the Eckart-Young bound and singular-value perturbation theory

## Related nodes (non-prerequisite)
- generalizes: rayleigh_quotient
- required_by: eckart_young

## Sources
horn_johnson_2e, trefethen_bau
