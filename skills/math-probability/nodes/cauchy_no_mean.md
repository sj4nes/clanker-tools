# cauchy_no_mean

## Type
counterexample

## Statement
X ~ Cauchy: density f_X(x) = 1/(pi(1 + x^2)) on R. E[|X|] = inf, so E[X] does not exist and Var is undefined. The sample mean of n iid Cauchy variables is again Cauchy(0,1) -- it does not concentrate. The LLN and CLT both fail.

## Symbols
- `X` — a standard Cauchy variable, type: Omega -> R
- `f_X` — its density, type: R -> (0, inf)

## Epistemic status
counterexample

## Prerequisites (tsort edges into this node)
abstract_integral, expectation, pdf

## Hypotheses
(none — unconditional within scope)

## Well-definedness
f_X integrates to 1 (arctan), so Cauchy is a bona fide probability law; it is E[X] that fails to exist, not the distribution.

## Type / well-formedness check
the canonical finite-density law with no mean: the tails decay only like 1/x^2, so integral |x| f_X(x) dx = (2/pi) integral_0^inf x/(1+x^2) dx = inf. Its characteristic function phi_X(t) = e^{-|t|} exists (and is non-differentiable at 0, consistent with the missing mean).

## Specialization / boundary cases
- ratio Z_1/Z_2 of independent standard normals is standard Cauchy
- the sample mean stays Cauchy(0,1) (phi_{Xbar}(t) = phi_X(t/n)^n = e^{-|t|}) -- averaging does not help
- the sample MEDIAN of n iid Cauchy DOES concentrate (median is well-defined) and is asymptotically normal

## Hypothesis-dropped counterexamples
- **this_IS_the_counterexample**: it shows the finite-mean hypothesis of the WLLN/SLLN and the finite-variance hypothesis of the CLT are not removable

## Common misuse
- applying the LLN or CLT to ratios, or to data with power-law tails of index <= 1 (no mean) or <= 2 (no variance)
- reporting a sample mean and its standard error for heavy-tailed data (both are meaningless)
- assuming a symmetric unimodal density implies a mean exists

## Related nodes (non-prerequisite)
- breaks: weak_law_large_numbers, strong_law_large_numbers, central_limit_theorem
- stable_law: index 1
- arises_as: ratio of normals, tan of a uniform angle

## Sources
durrett_pte, grimmett_stirzaker
