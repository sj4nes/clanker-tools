# one_way_anova_identity

## Type
identity

## Statement
For data X_ij (group i = 1..k, observation j = 1..n_i, total N = sum n_i), the total sum of squares decomposes as SS_total = SS_between + SS_within: sum_ij (X_ij - Xbar_..)^2 = sum_i n_i (Xbar_i. - Xbar_..)^2 + sum_ij (X_ij - Xbar_i.)^2, with degrees of freedom (N - 1) = (k - 1) + (N - k).

## Symbols
- `Xbar_i.` — the i-th group mean
- `Xbar_..` — the grand mean
- `SS_between / SS_within` — explained / unexplained variation

## Epistemic status
mathematical_identity  ·  regime: exact

## Prerequisites (tsort edges into this node)
cochran_theorem, linear_algebra_background, sample_mean

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: expand (X_ij - Xbar_..) = (X_ij - Xbar_i.) + (Xbar_i. - Xbar_..); the cross-sum is 2 sum_i (Xbar_i. - Xbar_..) sum_j (X_ij - Xbar_i.) = 0
derives_from: chi_squared_additivity
lean_status: core — the vanishing cross term is proof-checks.lean Stat.anova_cross_term_zero -- sum_j (x_ij - xbar_i) = 0 kills it (Int arithmetic)

## Type / well-formedness check
An exact algebraic (Pythagorean) identity -- the cross term vanishes because sum_j (X_ij - Xbar_i.) = 0 within each group. Under N(mu_i, sigma^2) errors and H0: all mu_i equal, Cochran makes SS_between/sigma^2 ~ chi^2_{k-1} independent of SS_within/sigma^2 ~ chi^2_{N-k}, so the F-ratio [SS_between/(k-1)] / [SS_within/(N-k)] ~ F_{k-1, N-k}.

## Specialization / boundary cases
- k = 2 groups: the ANOVA F reduces to the square of the pooled two-sample t-statistic (F_{1, N-2} = t_{N-2}^2)
- one observation per group (n_i = 1): SS_within = 0, no error estimate -- the design is degenerate
- R^2 for the ANOVA = SS_between / SS_total = eta^2

## Hypothesis-dropped counterexamples
- **equal_group_variances**: if the groups have different sigma_i^2 the F-statistic is not F-distributed under H0 (the Behrens-Fisher problem); Welch's ANOVA adjusts the df
- **normality**: the identity is algebraic and always holds; the chi^2 / F distribution of the pieces needs normal errors (or large n_i via the CLT)

## Common misuse
- reading a significant overall F as telling you WHICH groups differ -- it does not; post-hoc comparisons with multiplicity control are needed
- applying one-way ANOVA to non-independent observations (repeated measures) without a within-subject error term

## Related nodes (non-prerequisite)
- uses: cochran_theorem, chi_squared_additivity
- special_case_of: overall_f_test

## Sources
scheffe_analysis_of_variance, casella_berger_2e, fisher_1925
