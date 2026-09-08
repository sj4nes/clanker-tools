# cochran_theorem

## Type
theorem

## Statement
Let Z ~ N(0, I_n) and write Z^T Z = sum_{j=1}^m Q_j with each Q_j = Z^T A_j Z a quadratic form, A_j symmetric of rank r_j. If sum_j r_j = n, then each Q_j ~ chi^2_{r_j} and the Q_j are mutually independent (equivalently: the A_j are idempotent and A_j A_l = 0 for j != l).

## Symbols
- `A_j` — symmetric n x n matrices, type: real symmetric (projections onto orthogonal subspaces)
- `r_j = rank(A_j) = tr(A_j)` — the df of the j-th component

## Epistemic status
proved_theorem  ·  regime: exact

## Prerequisites (tsort edges into this node)
chi_squared_distribution, linear_algebra_background, prob_independence_rv, prob_standard_normal

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: the rank condition + sum A_j = I force each A_j idempotent with mutually orthogonal ranges; rotate to an eigenbasis where each Q_j is a sum of r_j distinct squared standard normals
derives_from: linear_algebra_background
lean_status: cited — the linear-algebra core (sum of idempotents = I with ranks summing to n => each idempotent, pairwise products 0) is proof-checks.lean Stat.cochran_idempotent for n <= 3 via decide on integer projection matrices

## Type / well-formedness check
A quadratic-forms decomposition theorem for the spherical Gaussian. Uses linear_algebra_background (idempotent = projection, rank = trace for idempotents, simultaneous diagonalization). The 'sum of ranks = n' condition forces each A_j to be an orthogonal projection and the images to be orthogonal.

## Specialization / boundary cases
- one-way ANOVA: Z^T Z = (between-groups SS) + (within-groups SS) with ranks (k - 1) + (n - k) = n - 1 after centering -- the F-test's numerator and denominator
- sample variance: I - (1/n) J has rank n - 1, (1/n) J has rank 1, sum = n -- gives scaled_sample_variance_chi_squared and Xbar _||_ S^2 in one stroke
- regression: fitted SS (rank p) + residual SS (rank n - p)

## Hypothesis-dropped counterexamples
- **sum_of_ranks_equals_n**: if sum r_j < n the components need not be chi^2 or independent (there is 'leftover' variation); if the A_j are not idempotent (a general quadratic form) the law is a weighted sum of chi^2_1's
- **Z_spherical**: for Z ~ N(0, Sigma), Sigma != I, apply to Sigma^{-1/2} Z; forgetting the whitening gives wrong df

## Common misuse
- decomposing a non-orthogonal (unbalanced, correlated-predictor) design's sums of squares and asserting independent chi^2 components -- Type I/II/III SS ambiguity comes exactly from this
- using it for a quadratic form whose matrix is not idempotent

## Related nodes (non-prerequisite)
- uses: chi_squared_additivity, linear_algebra_background
- required_by: scaled_sample_variance_chi_squared, one_way_anova_identity, overall_f_test, ols_distribution_under_normal_errors

## Sources
cochran_1934, rao_linear_statistical_inference, scheffe_analysis_of_variance
