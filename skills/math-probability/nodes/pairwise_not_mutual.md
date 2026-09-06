# pairwise_not_mutual

## Type
counterexample

## Statement
Pairwise independence does not imply mutual independence. Example: X, Y independent fair +-1 variables, Z = XY. Then (X,Y), (X,Z), (Y,Z) are each independent pairs, but P(X = Y = Z = 1) = 1/4 != 1/8 = P(X=1)P(Y=1)P(Z=1).

## Symbols
- `X, Y` — iid Uniform{-1,1}, type: Omega -> {-1,1}
- `Z` — XY, type: Omega -> {-1,1}

## Epistemic status
counterexample

## Prerequisites (tsort edges into this node)
independence_events

## Hypotheses
(none — unconditional within scope)

## Well-definedness
all three variables are Uniform{-1,1}; the pair (X, Z) is independent because Z = XY with Y an independent fair sign 'rerandomizes' X. Yet Z is sigma(X,Y)-measurable.

## Type / well-formedness check
each of Z, X, Y is Uniform{-1,1} and any two are independent (checking the four sign combinations), but the three are functionally linked: XYZ = 1 always, so knowing two determines the third.

## Specialization / boundary cases
- the |S| = 2 factorization equations all hold; the |S| = 3 equation P(X=Y=Z=1) = P(X=1)P(Y=1)P(Z=1) fails
- consequence: E[XYZ] = E[1] = 1 != 0 = E[X]E[Y]E[Z], so 'expectation factors' can fail even when it holds for every pair

## Hypothesis-dropped counterexamples
- **this_IS_the_counterexample**: it shows the |S| >= 3 conditions in independence_events are not redundant

## Common misuse
- verifying independence by checking only pairs
- assuming pairwise-independent variables can be treated as a product for a union bound refinement or a CLT (pairwise independence IS enough for the L^2 WLLN, but not for the CLT or the SLLN)

## Related nodes (non-prerequisite)
- limits: independence_events
- constrasts: for the WLLN, pairwise uncorrelated suffices

## Sources
durrett_pte, grimmett_stirzaker
