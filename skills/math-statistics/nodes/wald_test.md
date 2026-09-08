# wald_test

## Type
definition

## Statement
The Wald test of H0: theta = theta_0 rejects when W = (theta_hat - theta_0)^T [n I(theta_hat)] (theta_hat - theta_0) exceeds chi^2_{d, 1-alpha} (scalar case: (theta_hat - theta_0)^2 n I(theta_hat) > chi^2_{1,1-alpha}). It uses only the UNRESTRICTED fit.

## Symbols
- `theta_hat` — the unrestricted MLE
- `n I(theta_hat)` — estimated sample information (or observed information)
- `W -> chi^2_d under H0` — by mle_asymptotic_normality + continuous mapping

## Epistemic status
definition  ·  regime: asymptotic

## Prerequisites (tsort edges into this node)
chi_squared_distribution, fisher_information, mle_asymptotic_normality

## Hypotheses
true_parameter_interior, fisher_information_positive_definite

## Proof provenance
technique: mle_asymptotic_normality: sqrt(n)(theta_hat - theta_0) -> N(0, I^{-1}) under H0; the quadratic form with the inverse covariance -> chi^2_d (continuous mapping)
derives_from: mle_asymptotic_normality
lean_status: cited

## Type / well-formedness check
An asymptotic test; the quadratic form of a standardized N(0, I^{-1}) vector is chi^2_d. Needs only the alternative-model fit -- convenient, but NOT invariant to reparametrization (W changes if you test log theta vs theta), its worst practical flaw.

## Specialization / boundary cases
- scalar: W = (theta_hat - theta_0)^2 / se^2 = (z-statistic)^2 -- the squared 'estimate over standard error'
- the z-values printed next to GLM coefficients ARE Wald tests of H0: beta_j = 0
- for a linear model with normal errors the Wald test of several coefficients is exactly q F_{q, n-p} rescaled

## Hypothesis-dropped counterexamples
- **reparametrization**: testing H0: theta = 1 vs H0: log theta = 0 gives DIFFERENT Wald statistics and p-values though the hypotheses are identical -- the Wald test is not invariant. The LRT and score test are.
- **true_parameter_interior**: the 'Hauck-Donner effect': for a logistic coefficient far from 0 with a large SE, W can DECREASE as the effect grows, so the Wald test loses power exactly when the effect is large. Use the LRT.
- **fisher_information_positive_definite**: near-singular information (collinearity) makes W numerically unstable

## Common misuse
- preferring the Wald test for its convenience when the log-likelihood is asymmetric (small n, near-boundary) -- the LRT is more reliable
- reporting Wald p-values for a logistic model with near-separation (Hauck-Donner)

## Related nodes (non-prerequisite)
- uses: mle_asymptotic_normality, fisher_information, chi_squared_distribution
- required_by: three_tests_asymptotically_equivalent

## Sources
wald_1943, casella_berger_2e, hauck_donner_1977
