# confidence_set

## Type
definition

## Statement
A 1 - alpha confidence set for theta is a data-dependent set C(X) subset Theta with P_theta( theta in C(X) ) >= 1 - alpha for every theta (an interval, in one dimension).

## Symbols
- `C(X)` — the confidence set, type: random subset of Theta
- `1 - alpha` — the confidence LEVEL (a property of the procedure, not of one realized interval)
- `coverage` — theta -> P_theta(theta in C(X)), which should be >= 1 - alpha throughout

## Epistemic status
definition  ·  regime: exact

## Prerequisites (tsort edges into this node)
parameter_space, prob_probability_space

## Hypotheses
(none — unconditional within scope)
## Type / well-formedness check
A frequentist coverage guarantee about the RANDOM set C(X), holding for all theta. A realized interval [l, u] either contains the fixed unknown theta or not -- the '95%' describes the long-run behaviour of the rule, not a probability about theta.

## Specialization / boundary cases
- exact: Xbar +- t_{n-1, 1-alpha/2} S/sqrt(n) for a normal mean -- coverage exactly 1 - alpha
- asymptotic: theta_hat +- z_{1-alpha/2} SE -- coverage -> 1 - alpha
- conservative: a Bonferroni-adjusted simultaneous set has coverage >= 1 - alpha, often strictly

## Hypothesis-dropped counterexamples
- **coverage_for_every_theta**: the Wald interval for a binomial p has coverage that DIPS well below 1 - alpha for p near 0 or 1 and small n (down to ~0.8 for a nominal 0.95) -- the Clopper-Pearson or Wilson interval fixes it
- **the_set_is_pre-specified**: choosing which parameter to bracket after seeing the data (selective inference) destroys the coverage guarantee

## Common misuse
- saying 'there is a 95% probability that theta is in [l, u]' for a realized interval -- theta is not random
- comparing two 95% intervals by whether they overlap as a test (the overlap test is conservative and low-powered)

## In the wild
- every reported '95% CI' in a clinical trial, poll, or physics measurement
- the CI is the dual of the hypothesis test (confidence_set_test_duality) -- reporting the interval subsumes the test

## Related nodes (non-prerequisite)
- required_by: coverage_probability, pivot_method, confidence_set_test_duality, wald_interval
- dual_of: test_function
- commonly_confused_with: credible_interval

## Sources
casella_berger_2e, neyman_1937
