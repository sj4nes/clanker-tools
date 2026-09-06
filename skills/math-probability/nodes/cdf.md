# cdf

## Type
definition

## Statement
The cumulative distribution function of X is F_X(x) = P(X <= x) = P_X((-inf, x]).

## Symbols
- `F_X` — the CDF, type: R -> [0,1]
- `x` — a real threshold, type: real

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
distribution_pushforward, random_variable

## Hypotheses
(none — unconditional within scope)

## Well-definedness
F_X is well-defined for every random variable (the half-lines are Borel); its four characterizing properties are cdf_properties.

## Type / well-formedness check
F_X evaluates the law on the half-lines, which form a pi-system generating B(R) -- hence F_X determines P_X (cdf_determines_law). Right-continuity (not left) is the convention, from { X <= x } = bigcap_n { X <= x + 1/n }.

## Specialization / boundary cases
- X ~ Uniform(0,1): F_X(x) = x on [0,1]
- X = c: F_X = step at c (0 below, 1 from c on)
- F_X has an atom at x iff P(X = x) = F_X(x) - F_X(x^-) > 0

## Hypothesis-dropped counterexamples
- **none_defined_for_every_rv**: F_X always exists; the content is in cdf_properties (which functions are CDFs) and cdf_determines_law

## Common misuse
- using P(X < x) (left-continuous) and P(X <= x) interchangeably -- they differ exactly at atoms
- assuming F_X is continuous (it is only right-continuous in general)

## Related nodes (non-prerequisite)
- equivalent_to: the law P_X
- used_by: quantile_function, convergence_in_distribution, probability_integral_transform

## Sources
billingsley_probability_measure, durrett_pte
