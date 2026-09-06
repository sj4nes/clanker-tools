# variance_of_sum

## Type
theorem

## Statement
Var(sum_{i=1}^n X_i) = sum_i Var(X_i) + 2 sum_{i<j} Cov(X_i, X_j). If the X_i are pairwise uncorrelated, Var(sum) = sum Var.

## Symbols
- `X_i` — random variables in L^2(P), type: L^2(P)
- `n` — a fixed positive integer, type: natural number

## Epistemic status
proved_theorem

## Prerequisites (tsort edges into this node)
covariance, covariance_bilinear, expectation_linearity, variance

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: bilinearity of covariance: Cov(sum_i X_i, sum_j X_j) = sum_{i,j} Cov(X_i, X_j), split diagonal from off-diagonal
derives_from: covariance_bilinear
lean_status: core — validation/proof-checks.lean Prob.var_of_sum_raw and Prob.cov_bilinear_raw (GENUINE raw-moment identities)

## Type / well-formedness check
expand Var(sum X_i) = Cov(sum X_i, sum X_j) by bilinearity; the diagonal terms are Var(X_i), the off-diagonal terms pair up.

## Specialization / boundary cases
- pairwise uncorrelated (in particular independent) X_i: Var(sum) = sum Var(X_i) -- 'variances add'
- iid X_i: Var(sum) = n Var(X_1), so Var(sample mean) = Var(X_1)/n -- the 1/n that drives the LLN and the sqrt(n) in the CLT
- X_i = X for all i: Var(nX) = n^2 Var(X) -- maximal positive correlation

## Hypothesis-dropped counterexamples
- **uncorrelatedness_for_the_clean_form**: X_1 ~ N(0,1), X_2 = -X_1: Var(X_1 + X_2) = Var(0) = 0, not Var(X_1) + Var(X_2) = 2 -- the -2 Cov term matters

## Common misuse
- assuming variances add without checking (pairwise) uncorrelatedness
- forgetting the factor 2 on the covariance sum

## Related nodes (non-prerequisite)
- derives_from: covariance_bilinear
- used_by: weak_law_large_numbers, binomial_distribution

## Sources
billingsley_probability_measure, durrett_pte
