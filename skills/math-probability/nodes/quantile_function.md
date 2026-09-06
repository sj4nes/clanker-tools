# quantile_function

## Type
definition

## Statement
The quantile function (generalized inverse CDF) is F_X^{-1}(u) = inf { x : F_X(x) >= u } for u in (0,1).

## Symbols
- `F_X^{-1}` — the quantile function, type: (0,1) -> R
- `u` — a probability level, type: real in (0,1)

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
cdf, real_field

## Hypotheses
(none — unconditional within scope)

## Well-definedness
{ x : F_X(x) >= u } is nonempty (F_X -> 1) and bounded below (F_X -> 0), and closed to the right (F_X right-continuous), so the inf is attained and finite for u in (0,1).

## Type / well-formedness check
defined for every CDF, including discrete ones (where it is a step function) -- the inf makes it left-continuous and well-defined even where F_X jumps or is flat. F_X^{-1}(u) <= x iff u <= F_X(x), the Galois connection that powers the probability integral transform.

## Specialization / boundary cases
- F_X continuous and strictly increasing: F_X^{-1} is the ordinary inverse
- median = F_X^{-1}(1/2); quartiles at u = 1/4, 3/4
- discrete X: F_X^{-1} is a step function taking values in the support

## Hypothesis-dropped counterexamples
- **u_in_open_interval**: at u = 0 the inf is over all of R (gives -inf or the essential infimum); at u = 1 it may be +inf -- the transform is stated for u in (0,1)

## Common misuse
- assuming F_X^{-1}(F_X(x)) = x (fails where F_X is flat) or F_X(F_X^{-1}(u)) = u (fails where F_X jumps)
- using the right-continuous version inconsistently

## Related nodes (non-prerequisite)
- used_by: probability_integral_transform
- dual_of: the CDF (Galois connection)

## Sources
durrett_pte, grimmett_stirzaker
