# score_test

## Type
definition

## Statement
The score (Rao / Lagrange-multiplier) test of H0: theta = theta_0 rejects when U(theta_0)^T [n I(theta_0)]^{-1} U(theta_0) exceeds chi^2_{d, 1-alpha}. It uses ONLY the null fit -- no need to estimate the alternative model.

## Symbols
- `U(theta_0)` — the score evaluated at the hypothesized value -- large in magnitude => theta_0 is a poor fit
- `everything evaluated at theta_0` — the practical advantage: only fit the restricted model

## Epistemic status
definition  ·  regime: asymptotic

## Prerequisites (tsort edges into this node)
chi_squared_distribution, fisher_information, information_equality, score_function

## Hypotheses
fisher_information_positive_definite

## Proof provenance
technique: score identity: E_{theta_0}[U(theta_0)] = 0; CLT: (1/sqrt n) U(theta_0) -> N(0, I(theta_0)); standardize and apply continuous mapping to get chi^2_d
derives_from: information_equality
lean_status: cited

## Type / well-formedness check
An asymptotic test. Under H0, (1/sqrt n) U(theta_0) -> N(0, I(theta_0)) (score identity + information equality), so the standardized quadratic form -> chi^2_d. Invariant to reparametrization. Ideal when the alternative model is hard to fit (many nuisance parameters) or when scanning many candidate additions.

## Specialization / boundary cases
- Pearson's chi-squared goodness-of-fit statistic IS the score test for the multinomial (pearson_chi_squared_gof)
- the Breusch-Pagan test for heteroskedasticity and the Breusch-Godfrey test for autocorrelation are score (LM) tests
- testing whether to add a variable to a regression: the score test needs only the model WITHOUT it -- efficient for variable screening

## Hypothesis-dropped counterexamples
- **fisher_information_positive_definite**: singular I(theta_0) (a redundant restriction) makes the inverse undefined
- **H0_regular**: if theta_0 is on the boundary the score does not have mean 0 in the two-sided sense and the chi^2 calibration fails

## Common misuse
- using the observed information at theta_0 vs the expected information inconsistently -- they differ and the choice affects small-sample behaviour
- treating the score test as exact -- it is asymptotic like Wald and Wilks

## In the wild
- variable-selection screening in high-dimensional regression (score tests for each candidate, no refit)
- the score test underlies the 'modification indices' in structural equation modeling

## Related nodes (non-prerequisite)
- uses: score_function, information_equality, chi_squared_distribution
- required_by: three_tests_asymptotically_equivalent, pearson_chi_squared_gof

## Sources
rao_1948, casella_berger_2e
