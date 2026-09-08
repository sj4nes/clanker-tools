# sufficiency

## Type
definition

## Statement
A statistic T is sufficient for theta if the conditional distribution of the sample X given T(X) = t does not depend on theta.

## Symbols
- `T` — the statistic, type: measurable map of the sample
- `P_theta(X in . | T = t)` — the conditional law of the data given the statistic

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
prob_conditional_distribution, statistic

## Hypotheses
(none — unconditional within scope)
## Well-definedness
Requires a regular conditional distribution to exist (it does for the models in scope). The full sample is trivially sufficient; the constant statistic is sufficient only if theta is known.

## Type / well-formedness check
A conditional-independence statement: given T, the data carry no further information about theta. Equivalent operational form: one could simulate a fresh sample with the same distribution from T alone.

## Specialization / boundary cases
- Bernoulli: the count sum X_i is sufficient; the order of the 0s and 1s is not informative
- N(mu, sigma^2): (Xbar, S^2) is sufficient
- uniform(0, theta): the maximum X_(n) is sufficient

## Hypothesis-dropped counterexamples
- **conditional_law_theta_free**: Xbar alone is NOT sufficient for (mu, sigma^2) in a normal sample: given Xbar, the spread of the residuals still depends on sigma^2. Discarding S^2 loses information about sigma^2.

## Common misuse
- reducing data to an insufficient statistic and then claiming no information was lost
- confusing 'sufficient' (loses nothing) with 'minimal sufficient' (the maximal reduction) or 'complete'

## In the wild
- the Rao-Blackwell recipe -- condition any estimator on a sufficient statistic to improve it -- is the basis of every UMVUE derivation
- in privacy / compression, a sufficient statistic is the minimal release that preserves inference about theta

## Related nodes (non-prerequisite)
- required_by: neyman_fisher_factorization, rao_blackwell_theorem, basu_theorem
- specializes_to: minimal_sufficiency

## Sources
casella_berger_2e, lehmann_casella_tpe
