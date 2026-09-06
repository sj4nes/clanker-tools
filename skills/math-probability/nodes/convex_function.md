# convex_function

## Type
primitive

## Statement
phi: I -> R is convex if phi(t x + (1-t) y) <= t phi(x) + (1-t) phi(y) for all x,y in I and t in [0,1]; equivalently it lies above each of its tangent/supporting lines on the interior.

## Symbols
- `phi` — the function, type: I -> R with I an interval
- `supporting line at c` — an affine L with L(c)=phi(c), L<=phi, type: affine function

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
(root)

## Hypotheses
(none — unconditional within scope)

## Well-definedness
a convex function on an open interval is continuous and has one-sided derivatives everywhere; the supporting-line family is nonempty at every interior point.

## Type / well-formedness check
convexity is on an interval I; at an interior point c there is at least one supporting line phi(x) >= phi(c) + m (x - c). Jensen's inequality is exactly 'take x = X, c = E[X], then integrate'. Discharged from math-real-analysis.

## Specialization / boundary cases
- phi(x) = x^2, |x|, e^{tx} are convex on R -- the cases used for variance, Jensen, and the Chernoff/Hoeffding bounds
- phi affine: Jensen holds with equality

## Hypothesis-dropped counterexamples
- **convexity**: phi(x) = -x^2 (concave): Jensen reverses, phi(E[X]) >= E[phi(X)]

## Common misuse
- applying Jensen with the inequality the wrong way for a concave phi
- assuming strict inequality without strict convexity + a non-degenerate X

## Related nodes (non-prerequisite)
- developed_in: math-real-analysis
- dual_of: concave function

## Sources
rudin_principles, boucheron_lugosi_massart
