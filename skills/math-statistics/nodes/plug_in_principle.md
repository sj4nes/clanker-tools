# plug_in_principle

## Type
definition

## Statement
The plug-in principle estimates a functional T(P) of the unknown law P by T(P_hat_n), where P_hat_n is the empirical distribution (mass 1/n at each observation).

## Symbols
- `T(.)` — a statistical functional, type: map from laws to R^k (the mean, a quantile, the variance, a correlation)
- `P_hat_n` — the empirical measure

## Epistemic status
definition  ·  regime: distribution_free

## Prerequisites (tsort edges into this node)
empirical_cdf, statistic

## Hypotheses
(none — unconditional within scope)
## Type / well-formedness check
Requires the estimand to be expressed as a functional of P. Consistency comes from P_hat_n -> P (Glivenko-Cantelli) plus continuity of T; asymptotic normality from the functional delta method when T is Hadamard-differentiable.

## Specialization / boundary cases
- T(P) = E_P[X] => plug-in is Xbar; T(P) = Var_P(X) => plug-in is the /n sample variance
- T(P) = F^{-1}(1/2) => plug-in is the sample median
- T(P) = P(X in A) => plug-in is the sample proportion

## Hypothesis-dropped counterexamples
- **T_continuous**: the density value f(x_0) is NOT a continuous functional of P in the sup metric -- there is no sqrt(n) plug-in estimator; density estimation is a genuinely nonparametric (slower-rate) problem (see kde_bias_variance_tradeoff)

## Common misuse
- plugging into a functional that is not smooth (a density, a mode, the number of modes) and expecting sqrt(n) behaviour
- forgetting the plug-in variance estimator (/n) is biased -- it is the MLE, not the UMVUE

## Related nodes (non-prerequisite)
- required_by: plug_in_estimator
- uses: empirical_cdf

## Sources
wasserman_all_of_statistics, van_der_vaart_asymptotic
