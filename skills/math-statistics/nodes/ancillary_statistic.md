# ancillary_statistic

## Type
definition

## Statement
A statistic A is ancillary for theta if its distribution does not depend on theta.

## Symbols
- `A(X)` — the ancillary statistic, type: statistic with a theta-free law

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
prob_cdf, statistic

## Hypotheses
(none — unconditional within scope)
## Well-definedness
A property of the statistic's marginal law under the model.

## Type / well-formedness check
A statistic carrying no MARGINAL information about theta. It can still carry information about the PRECISION of an estimate (an ancillary configuration statistic) -- the basis of conditional inference.

## Specialization / boundary cases
- location family f(x - theta): the residuals (X_i - Xbar), or the range X_(n) - X_(1), are ancillary
- N(mu, 1): S^2 is ancillary for mu
- the sample size n itself, if random but theta-free, is ancillary

## Hypothesis-dropped counterexamples
- **theta_free_law**: S^2 is NOT ancillary for sigma^2 in N(mu, sigma^2) -- its law (scaled chi-squared) depends on sigma^2. Ancillarity is always relative to a specified parameter.

## Common misuse
- conditioning on a statistic that is only APPROXIMATELY ancillary and ignoring the approximation error
- treating an ancillary statistic as ignorable -- it should often be conditioned on (conditionality principle)

## Related nodes (non-prerequisite)
- required_by: basu_theorem, conditionality_principle
- dual_of: sufficiency

## Sources
cox_hinkley_theoretical_statistics, casella_berger_2e
