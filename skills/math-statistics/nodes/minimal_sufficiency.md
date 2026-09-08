# minimal_sufficiency

## Type
definition

## Statement
A sufficient statistic T is minimal sufficient if it is a function of every other sufficient statistic: the coarsest sufficient reduction of the data.

## Symbols
- `T` — the minimal sufficient statistic (unique up to bijection)

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
sufficiency

## Hypotheses
(none — unconditional within scope)
## Well-definedness
Exists for the dominated models in scope; unique up to a one-to-one transformation.

## Type / well-formedness check
A minimality statement. Lehmann-Scheffe test: T(x) = T(y) iff the likelihood ratio f(x; theta)/f(y; theta) is constant in theta.

## Specialization / boundary cases
- exponential family (minimal representation): sum_i T(X_i) is minimal sufficient
- iid Cauchy(theta, 1): the full order statistic is minimal sufficient -- no finite-dimensional reduction
- uniform(theta, theta+1): (X_(1), X_(n)) is minimal sufficient, 2-dimensional for a 1-dim parameter

## Hypothesis-dropped counterexamples
- **minimality**: sum_i T(X_i) for a CURVED exponential family: still minimal sufficient but its dimension exceeds dim(theta) -- 'minimal' does not mean 'dimension = dim theta'

## Common misuse
- assuming minimal sufficient has the same dimension as the parameter
- confusing minimal sufficiency (coarsest sufficient) with completeness (a different property entirely)

## Related nodes (non-prerequisite)
- commonly_confused_with: completeness_statistic
- generalizes_from: sufficiency

## Sources
lehmann_casella_tpe, casella_berger_2e
