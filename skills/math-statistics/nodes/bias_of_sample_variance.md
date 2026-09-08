# bias_of_sample_variance

## Type
identity

## Statement
For any distribution with finite variance sigma^2, E[ sum_{i=1}^n (X_i - Xbar)^2 ] = (n - 1) sigma^2; hence S^2 = (n-1)^{-1} sum (X_i - Xbar)^2 is unbiased for sigma^2 (no normality needed).

## Symbols
- `the (n-1)` — the count of independent deviations -- n residuals constrained by sum (X_i - Xbar) = 0

## Epistemic status
mathematical_identity  ·  regime: exact

## Prerequisites (tsort edges into this node)
prob_covariance, prob_expectation_linearity, prob_independence_factorization, prob_variance, sample_variance

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: algebraic identity sum(X_i - Xbar)^2 = sum(X_i - mu)^2 - n(Xbar - mu)^2, then E[.] = n sigma^2 - n Var(Xbar) = n sigma^2 - sigma^2
derives_from: prob_expectation_linearity
lean_status: core — validation/proof-checks.lean Stat.bias_sample_var -- the identity sum(x_i - xbar)^2 = sum(x_i - m)^2 - n(xbar - m)^2 over Int, then E gives (n-1)sigma^2 (reuses the centid/variance algebra from math-probability)

## Type / well-formedness check
An exact identity for every finite-variance law. Proof: sum (X_i - Xbar)^2 = sum (X_i - mu)^2 - n(Xbar - mu)^2; take expectations: n sigma^2 - n . sigma^2/n = (n - 1) sigma^2.

## Specialization / boundary cases
- n = 1: sum (X_1 - X_1)^2 = 0 = 0 . sigma^2 -- consistent, and S^2 is undefined (0/0), matching 'you cannot estimate spread from one point'
- n = 2: E[(X_1 - X_2)^2 / 2] = sigma^2
- the divisor-n version has expectation (n-1)/n sigma^2 -- bias -sigma^2/n, vanishing as n -> inf

## Hypothesis-dropped counterexamples
- **finite_variance**: if sigma^2 = inf (Cauchy, t_2) the left side is infinite and 'unbiased for sigma^2' is vacuous -- S^2 estimates nothing

## Common misuse
- believing the n-1 correction requires normality -- it does not; it is a second-moment identity
- believing S (the sqrt) is unbiased for sigma -- E[S] < sigma strictly (Jensen), by a factor that itself depends on n

## In the wild
- the reason every calculator, spreadsheet, and stats package has a 'sample' (n-1) vs 'population' (n) standard-deviation button
- the n - p generalization is the unbiased error-variance estimator in regression (unbiased_error_variance_estimator)

## Related nodes (non-prerequisite)
- required_by: sample_variance, unbiased_error_variance_estimator
- uses: prob_variance, prob_independence_factorization

## Sources
casella_berger_2e
