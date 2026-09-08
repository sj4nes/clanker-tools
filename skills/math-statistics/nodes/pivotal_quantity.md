# pivotal_quantity

## Type
definition

## Statement
A pivotal quantity is a function Q(X, theta) of the data and the parameter whose distribution is the same for every theta in Theta.

## Symbols
- `Q(X, theta)` — the pivot -- involves theta, so it is NOT a statistic
- `its (theta-free) distribution` — known, so its quantiles can be looked up

## Epistemic status
definition  ·  regime: exact

## Prerequisites (tsort edges into this node)
parameter_space, prob_cdf

## Hypotheses
(none — unconditional within scope)
## Type / well-formedness check
A pivot mixes data and parameter in a way that cancels theta's effect on the distribution. It is the engine for exact confidence sets: bracket Q by its known quantiles, then solve for theta.

## Specialization / boundary cases
- N(mu, sigma^2 known): Q = sqrt(n)(Xbar - mu)/sigma ~ N(0,1), pivotal
- N(mu, sigma^2): Q = sqrt(n)(Xbar - mu)/S ~ t_{n-1}, pivotal
- N(mu, sigma^2): Q = (n-1) S^2 / sigma^2 ~ chi^2_{n-1}, pivotal for sigma^2
- any continuous F_theta: Q = F_theta(X) ~ Uniform(0,1) -- the probability integral transform is a universal (if often intractable) pivot

## Hypothesis-dropped counterexamples
- **exactly_theta_free_law**: an ASYMPTOTIC pivot (theta_hat - theta)/SE -> N(0,1) is only approximately pivotal at finite n -- the resulting Wald interval has approximate coverage
- **Behrens-Fisher**: (Xbar - Ybar - delta) / sqrt(S_X^2/n + S_Y^2/m) is NOT exactly pivotal when sigma_X != sigma_Y -- its df depends on the unknown ratio (hence Welch's approximation)

## Common misuse
- treating a quantity as pivotal because it 'looks standardized' without checking its law is genuinely theta-free
- using a location-scale pivot when a nuisance parameter (an unknown correlation, an unknown shape) remains in its distribution

## Related nodes (non-prerequisite)
- required_by: pivot_method
- uses: 

## Sources
casella_berger_2e
