# wald_interval

## Type
definition

## Statement
A Wald confidence interval for a scalar theta is theta_hat +- z_{1-alpha/2} se(theta_hat), where theta_hat is asymptotically normal and se(theta_hat) is a consistent estimate of its standard deviation (typically from the inverse observed information). Coverage -> 1 - alpha as n -> inf.

## Symbols
- `se(theta_hat)` — estimated standard error, e.g. 1/sqrt(n I(theta_hat)) or a diagonal of the inverse observed information
- `z_{1-alpha/2}` — normal quantile (t_{n-p} in the regression case for a finite-sample refinement)

## Epistemic status
definition  ·  regime: asymptotic

## Prerequisites (tsort edges into this node)
asymptotic_normality_estimator, confidence_set, fisher_information, prob_standard_normal

## Hypotheses
fisher_information_positive_definite

## Proof provenance
technique: theta_hat asymptotically N(theta, se^2) + se consistent => (theta_hat - theta)/se -> N(0,1) (Slutsky); invert
derives_from: asymptotic_normality_estimator
lean_status: cited

## Type / well-formedness check
An ASYMPTOTIC interval. Its coverage is 1 - alpha only in the limit; it is symmetric by construction, which is its main weakness near a parameter boundary or for a skew-sampling-distribution estimator.

## Specialization / boundary cases
- MLE: theta_hat +- z / sqrt(n I(theta_hat)) (large_sample_wald_interval)
- binomial proportion: p_hat +- z sqrt(p_hat(1-p_hat)/n) -- the notorious Wald interval for p, which undercovers near 0 and 1
- a transformed parameter g(theta): use the delta-method se |g'(theta_hat)| se(theta_hat) (delta_method_standard_error), or better, build the interval on the scale where normality is best and back-transform

## Hypothesis-dropped counterexamples
- **fisher_information_positive_definite**: near a boundary (p near 0/1, a variance component near 0) the sampling distribution is skewed and one-sided; the symmetric Wald interval can extend outside the parameter space and badly undercover -- the score (Wilson) or LR interval is the fix
- **sqrt_n_normality**: for a non-sqrt(n) estimator (uniform endpoint) the Wald recipe is simply invalid

## Common misuse
- using the Wald interval for a proportion with small np or p near 0/1 (use Wilson or Clopper-Pearson)
- reporting a Wald CI that includes impossible values (negative variance, probability > 1) without reconsidering the scale
- trusting its coverage at the n you have rather than in the limit

## In the wild
- the default CI reported next to every coefficient in a fitted GLM / Cox model / SEM
- its poor small-sample behaviour for proportions is why epidemiology moved to Wilson score intervals

## Related nodes (non-prerequisite)
- uses: asymptotic_normality_estimator, fisher_information
- approximated_by: 
- approximates_from: normal_mean_ci_unknown_variance
- required_by: delta_method_standard_error, large_sample_wald_interval

## Sources
casella_berger_2e, brown_cai_dasgupta_2001
