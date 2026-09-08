# mle_asymptotic_normality

## Type
theorem

## Statement
Under identifiability, theta_0 interior, log f in C^3 with a dominated third derivative, and I(theta_0) positive definite, the MLE satisfies sqrt(n)(theta_hat_n - theta_0) -> N(0, I(theta_0)^{-1}) in distribution; the MLE is asymptotically efficient.

## Symbols
- `I(theta_0)^{-1}` — the inverse per-observation Fisher information -- the Cramer-Rao asymptotic variance
- `the sample version` — n(theta_hat - theta_0) approx N(0, (n I)^{-1}); SE_j = sqrt((n I(theta_hat))^{-1}_jj)

## Epistemic status
proved_theorem  ·  regime: asymptotic

## Prerequisites (tsort edges into this node)
fisher_information_positive_definite, information_equality, log_likelihood_smooth, mle_consistency, mle_score_equation, prob_clt, prob_slutsky, ra_mean_value_theorem, ra_taylor_theorem, true_parameter_interior

## Hypotheses
true_parameter_interior, fisher_information_positive_definite, log_likelihood_smooth, identifiability

## Proof provenance
technique: Taylor-expand the score equation about theta_0; CLT for the score, LLN for the observed information, Slutsky
derives_from: prob_clt
lean_status: cited — CITED -- Cramer 1946; van der Vaart Thm 5.39. The Slutsky assembly N(0, A^{-1} B A^{-1}) with A = B = I is proof-checks.lean Stat.sandwich_reduces_when_info_equality; the deep CLT-for-the-score step is cited.

## Type / well-formedness check
An asymptotic distributional result. Proof: Taylor-expand 0 = U(theta_hat) about theta_0: 0 = U(theta_0) + U'(theta_bar)(theta_hat - theta_0). Then sqrt(n)(theta_hat - theta_0) = [-(1/n) U'(theta_bar)]^{-1} [(1/n^{1/2}) U(theta_0)]. Numerator -> N(0, I(theta_0)) by the CLT (score identity + information equality give mean 0, variance I). Denominator -> I(theta_0) by the LLN. Slutsky assembles N(0, I^{-1} I I^{-1}) = N(0, I^{-1}).

## Specialization / boundary cases
- Bernoulli: sqrt(n)(p_hat - p) -> N(0, p(1-p)) -- the de Moivre-Laplace / normal approximation to the binomial proportion
- N(mu, sigma^2): sqrt(n)((mu_hat, sigma^2_hat) - (mu, sigma^2)) -> N(0, diag(sigma^2, 2 sigma^4)) -- mu_hat and sigma^2_hat asymptotically independent
- logistic regression: sqrt(n)(beta_hat - beta) -> N(0, (E[p(1-p) x x^T])^{-1}) -- the basis of the reported z-values

## Hypothesis-dropped counterexamples
- **log_likelihood_smooth**: Laplace location: the MLE (sample median) IS sqrt(n)-normal but with variance 1 (= 1/(4 f(0)^2)), reached by a non-Taylor argument -- the C^3 route fails though the conclusion's SHAPE survives
- **support_independent_of_theta**: uniform(0, theta): n(theta - theta_hat) -> Exponential -- rate n, non-normal limit; the theorem's conclusion is simply false
- **true_parameter_interior**: one-sided boundary (variance component = 0): the limit is a half-normal, not a normal
- **fisher_information_positive_definite**: non-identified direction: I singular, I^{-1} undefined, no sqrt(n)-normal limit along the flat direction

## Common misuse
- using I(theta_0)^{-1}/n as an EXACT finite-sample variance -- it is a limit; at small n the sampling distribution of a nonlinear MLE is skewed
- trusting Wald intervals theta_hat +- z SE for a near-boundary parameter (a proportion near 0/1) -- the score or LR interval is far better there
- applying it to non-regular models

## In the wild
- the source of every 'estimate +- standard error' and z-/p-value in the output of a fitted GLM, survival model, or structural equation model
- the delta method (this + a smooth transform) delivers the SE of any function of the fitted parameters -- odds ratios, predicted probabilities, EC50s

## Related nodes (non-prerequisite)
- strengthens: mle_consistency
- required_by: wald_test, wilks_theorem, large_sample_wald_interval, bernstein_von_mises
- uses: information_equality

## Sources
cramer_1946, van_der_vaart_asymptotic, lehmann_casella_tpe
