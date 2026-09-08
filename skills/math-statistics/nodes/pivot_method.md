# pivot_method

## Type
algorithm

## Statement
Given a pivot Q(X, theta) with known distribution, pick constants a, b with P(a <= Q(X, theta) <= b) = 1 - alpha, then C(X) = { theta : a <= Q(X, theta) <= b } is an exact 1 - alpha confidence set.

## Symbols
- `a, b` — quantiles of the pivot's known distribution (e.g. +- t_{n-1, 1-alpha/2})
- `'invert the pivot'` — solve the double inequality in theta

## Epistemic status
constructive_result  ·  regime: exact

## Prerequisites (tsort edges into this node)
confidence_set, pivotal_quantity

## Hypotheses
pivotal_quantity

## Proof provenance
technique: event identity { theta in C(X) } = { a <= Q(X, theta) <= b }; take P_theta of both sides; the right side has probability 1 - alpha independent of theta
derives_from: pivotal_quantity
lean_status: core — the event-identity / probability-transfer step is proof-checks.lean Stat.pivot_coverage -- P{theta in C} = P{a <= Q <= b} = 1 - alpha

## Type / well-formedness check
An exact construction: coverage is 1 - alpha BY CONSTRUCTION because {theta in C(X)} = {a <= Q(X, theta) <= b} as events, and the latter has probability 1 - alpha for every theta (pivotality). The set is an interval iff Q is monotone in theta.

## Specialization / boundary cases
- normal mean, sigma known: invert -z <= sqrt(n)(Xbar - mu)/sigma <= z  =>  Xbar +- z sigma/sqrt(n)
- normal variance: invert chi^2_{lo} <= (n-1)S^2/sigma^2 <= chi^2_{hi}  =>  ( (n-1)S^2/chi^2_{hi}, (n-1)S^2/chi^2_{lo} ) -- asymmetric
- the choice of (a, b) is free; equal-tailed is conventional, shortest-interval is an alternative

## Hypothesis-dropped counterexamples
- **pivotal_quantity**: with only an asymptotic pivot the coverage is 1 - alpha + O(n^{-1/2}) -- the method still 'works' but is no longer exact
- **monotone_in_theta**: if Q is not monotone in theta the inverted set can be a union of intervals or empty

## Common misuse
- inverting an asymptotic pivot and calling the interval 'exact'
- always using equal-tailed quantiles when the pivot's distribution is very skewed (chi^2 with small df) -- the equal-tailed interval is far from shortest

## Related nodes (non-prerequisite)
- required_by: normal_mean_ci_known_variance, normal_mean_ci_unknown_variance, normal_variance_ci
- uses: pivotal_quantity

## Sources
casella_berger_2e
