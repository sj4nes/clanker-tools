# large_sample_wald_interval

## Type
proposition

## Statement
From the MLE, theta_hat_MLE +- z_{1-alpha/2} / sqrt(n I(theta_hat_MLE)) (or using the observed information -d^2 ell(theta_hat)) is a confidence interval with coverage -> 1 - alpha.

## Symbols
- `n I(theta_hat)` — the estimated sample Fisher information -- or the observed information J(theta_hat) = -d^2 ell(theta_hat)
- `observed vs expected information` — the observed version has slightly better finite-sample properties (Efron-Hinkley 1978)

## Epistemic status
proposition  ·  regime: asymptotic

## Prerequisites (tsort edges into this node)
fisher_information, mle_asymptotic_normality, wald_interval

## Hypotheses
true_parameter_interior, fisher_information_positive_definite, log_likelihood_smooth

## Proof provenance
technique: mle_asymptotic_normality gives sqrt(n)(theta_hat - theta) -> N(0, I^{-1}); I(theta_hat) -> I(theta) consistently; Slutsky; invert
derives_from: mle_asymptotic_normality
lean_status: cited

## Type / well-formedness check
The Wald interval specialized to the MLE, using mle_asymptotic_normality's variance I(theta_0)^{-1}. Asymptotic; shares the Wald interval's boundary weaknesses.

## Specialization / boundary cases
- Poisson rate: lambda_hat +- z sqrt(lambda_hat / n) since I(lambda) = 1/lambda
- logistic regression coefficients: the standard reported CI, beta_hat_j +- z se_j with se_j from the inverse observed information
- prefer the profile-likelihood (LR) interval when the log-likelihood is visibly asymmetric

## Hypothesis-dropped counterexamples
- **true_parameter_interior**: near a boundary the interval extends past the parameter space and undercovers -- use the LR interval, which respects the likelihood's shape
- **log_likelihood_smooth**: non-regular model: the interval is invalid (wrong rate / wrong shape)

## Common misuse
- reporting it for a small sample where the log-likelihood is far from quadratic (use LR / profile intervals)
- using expected information I(theta_hat) when the model may be misspecified -- then the sandwich SE is right

## Related nodes (non-prerequisite)
- uses: mle_asymptotic_normality, wald_interval
- approximates: 

## Sources
casella_berger_2e, efron_hinkley_1978
