# mean_squared_error

## Type
definition

## Statement
The mean squared error of theta_hat at theta is MSE(theta) = E_theta[(theta_hat - theta)^2] (for a vector, E_theta||theta_hat - theta||^2).

## Symbols
- `MSE(theta)` — mean squared error, type: nonnegative function of theta

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
estimator, prob_expectation

## Hypotheses
(none — unconditional within scope)
## Well-definedness
Defined wherever theta_hat has a finite second moment.

## Type / well-formedness check
The risk function under squared-error loss L(theta, a) = (a - theta)^2. Requires a finite second moment of theta_hat. Decomposes as variance plus squared bias (next node).

## Specialization / boundary cases
- MSE of Xbar for a population mean: sigma^2 / n (unbiased, so MSE = variance)
- MSE of a shrinkage estimator c Xbar: c^2 sigma^2/n + (1-c)^2 mu^2 -- minimized at c < 1, beating Xbar at that mu
- root-MSE is the natural scale; it has the units of theta

## Hypothesis-dropped counterexamples
- **finite_second_moment**: estimators with infinite variance (Cauchy-scale MLE at small n, ratio estimators near a zero denominator) have infinite MSE though they may be perfectly usable (finite median absolute error)

## Common misuse
- comparing MSE across estimands on different scales without standardizing
- using MSE when the loss is genuinely asymmetric (over- vs under-estimating a dose) -- then a tailored loss and its Bayes rule are right

## Related nodes (non-prerequisite)
- required_by: mse_bias_variance_decomposition, james_stein
- special_case_of: risk_function

## Sources
casella_berger_2e, lehmann_casella_tpe
