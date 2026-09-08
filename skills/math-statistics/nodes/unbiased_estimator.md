# unbiased_estimator

## Type
definition

## Statement
theta_hat is unbiased for g(theta) if E_theta[theta_hat] = g(theta) for every theta in Theta.

## Symbols
- `g(theta)` — the estimand (often theta itself)

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
bias

## Hypotheses
(none — unconditional within scope)
## Well-definedness
Requires a finite mean at every theta.

## Type / well-formedness check
A statement holding for ALL theta simultaneously. Unbiasedness is a convenient constraint that makes 'minimum variance' a well-posed optimality target, but it is not sacred (it can force large variance or absurd estimates).

## Specialization / boundary cases
- Xbar unbiased for the mean; S^2 (n-1 divisor) unbiased for the variance
- there is NO unbiased estimator of 1/p in Bernoulli sampling (any function of the sufficient statistic is a polynomial in the count, of bounded degree)
- the unique unbiased estimator of e^{-2 lambda} in Poisson sampling is (-1)^X -- unbiased but absurd (it is +-1)

## Hypothesis-dropped counterexamples
- **exists_at_all**: e^{-2 lambda} Poisson: the (-1)^X estimator shows unbiasedness can pick out a ridiculous rule; the MLE e^{-2 Xbar} is biased but sensible

## Common misuse
- insisting on unbiasedness when it forces a nonsensical or high-variance estimator
- assuming an unbiased estimator exists -- for many g(theta) none does

## Related nodes (non-prerequisite)
- required_by: umvue, cramer_rao_lower_bound, rao_blackwell_theorem, gauss_markov_theorem

## Sources
casella_berger_2e, lehmann_casella_tpe
