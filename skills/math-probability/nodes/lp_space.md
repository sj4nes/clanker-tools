# lp_space

## Type
definition

## Statement
L^p(P) = { X : E[|X|^p] < inf } for p >= 1, a normed vector space with ||X||_p = E[|X|^p]^{1/p} (identifying X = Y a.s.). It is complete (a Banach space); L^2 is a Hilbert space.

## Symbols
- `X` — a random variable, type: Omega -> R
- `p` — an exponent, type: real >= 1

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
convex_function, expectation, moment

## Hypotheses
(none — unconditional within scope)

## Well-definedness
||.||_p is a genuine norm on the quotient by a.s.-equality (||X||_p = 0 iff X = 0 a.s., by expectation_monotonicity); Minkowski gives the triangle inequality.

## Type / well-formedness check
elements are a.s.-equivalence classes, not functions. The triangle inequality is Minkowski; completeness (Riesz-Fischer) is cited. On a PROBABILITY space the L^p are nested (moment_ladder), unlike on infinite measure spaces.

## Specialization / boundary cases
- p = 1: integrable variables, E[X] defined
- p = 2: finite variance, the Hilbert space where E[X|G] is a projection
- p = inf: ||X||_inf = ess sup |X|, the a.s.-bounded variables

## Hypothesis-dropped counterexamples
- **probability_space_for_nesting**: on (R, lambda), 1/x is in L^2(1, inf) but not L^1(1, inf) -- the nesting L^p subset L^q (p > q) needs a FINITE measure

## Common misuse
- treating L^p elements as functions with pointwise values
- assuming L^p nesting on a general measure space

## Related nodes (non-prerequisite)
- ordered_by: moment_ladder
- normed_by: holder_inequality, minkowski
- used_by: conditional_expectation_l2_projection, convergence_in_lp

## Sources
folland_real_analysis, williams_probability_martingales
