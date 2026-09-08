# asymptotic_normality_estimator

## Type
definition

## Statement
theta_hat_n is asymptotically normal with rate sqrt(n) if sqrt(n)(theta_hat_n - theta) -> N(0, Sigma(theta)) in distribution, for every theta.

## Symbols
- `Sigma(theta)` — the asymptotic covariance, type: PSD matrix depending on theta
- `-->^d` — convergence in distribution (prob_conv_d)

## Epistemic status
definition  ·  regime: asymptotic

## Prerequisites (tsort edges into this node)
estimator, prob_conv_d, prob_standard_normal

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: delta method / Taylor expansion of an estimating equation, then the CLT for the sum of iid influence-function terms
derives_from: prob_clt
lean_status: cited

## Type / well-formedness check
An asymptotic distributional statement. The centering is the true theta and the scaling is sqrt(n); other rates (n for uniform(0,theta), n^{1/3} for a mode / isotonic estimator) give non-normal limits and are excluded from 'asymptotically normal'.

## Specialization / boundary cases
- Xbar: sqrt(n)(Xbar - mu) -> N(0, sigma^2) whenever sigma^2 < inf (CLT)
- the MLE under regularity: Sigma(theta) = I(theta)^{-1} (efficient)
- a method-of-moments estimator: Sigma from the delta method applied to the moment map

## Hypothesis-dropped counterexamples
- **sqrt_n_rate**: uniform(0, theta): n(theta - X_(n)) -> Exponential(1/theta), NOT a sqrt(n) normal limit -- 'asymptotic normality' as defined here simply does not hold

## Common misuse
- quoting a symmetric Wald interval when the true rate or limit law is not sqrt(n)-normal
- using the asymptotic variance at a sample size where the sampling distribution is visibly skewed

## Related nodes (non-prerequisite)
- required_by: asymptotic_variance, wald_interval
- strengthens: consistency

## Sources
van_der_vaart_asymptotic
