# plug_in_estimator

## Type
definition

## Statement
The plug-in estimator of a statistical functional theta = T(P) is theta_hat = T(P_hat_n), obtained by applying the functional to the empirical distribution.

## Symbols
- `T` — the functional (mean, variance, quantile, correlation, a treatment-effect contrast, ...)
- `influence function IF(x)` — the Gateaux derivative of T at P -- governs the asymptotic variance E[IF^2] and the bias

## Epistemic status
definition  ·  regime: distribution_free

## Prerequisites (tsort edges into this node)
empirical_cdf, plug_in_principle

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: functional delta method: T(P_hat_n) = T(P) + (1/n) sum IF(X_i) + o_p(n^{-1/2}); CLT on the average of the influence-function terms
derives_from: glivenko_cantelli
lean_status: cited

## Type / well-formedness check
A construction. For a Hadamard-differentiable T, sqrt(n)(T(P_hat_n) - T(P)) -> N(0, E[IF(X)^2]) by the functional delta method, and E[IF^2]/n is the asymptotic variance (estimated by plugging in, or by the bootstrap / jackknife).

## Specialization / boundary cases
- T(P) = E_P[X] => plug-in Xbar, IF(x) = x - mu
- T(P) = Var_P(X) => plug-in the /n sample variance, IF(x) = (x - mu)^2 - sigma^2
- T(P) = median => plug-in sample median, IF(x) = (1/2 - 1{x <= m}) / f(m) -- note the density in the denominator

## Hypothesis-dropped counterexamples
- **Hadamard_differentiability**: T(P) = f_P(x_0) (a density value) or T(P) = number of modes: not a differentiable functional; the plug-in either does not exist (density of a discrete P_hat_n) or converges at a slower nonparametric rate
- **IF_has_finite_variance**: if E[IF(X)^2] = inf (heavy tails and a functional sensitive to them) the sqrt(n) normal limit fails

## Common misuse
- reporting the naive plug-in SE for a functional with an influence function that involves an unknown density (quantiles) -- use the bootstrap
- assuming every functional plugs in at sqrt(n) rate

## Related nodes (non-prerequisite)
- uses: plug_in_principle, empirical_cdf
- required_by: bootstrap

## Sources
van_der_vaart_asymptotic, hampel_robust_statistics
