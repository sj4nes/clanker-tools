# transformation_univariate

## Type
theorem

## Statement
If X has density f_X and g is strictly monotone and C^1 on the range of X, then Y = g(X) has density f_Y(y) = f_X(g^{-1}(y)) |d/dy g^{-1}(y)| on g(range).

## Symbols
- `g` — the transformation, type: strictly monotone C^1 function
- `Y` — g(X), type: Omega -> R

## Epistemic status
proved_theorem

## Prerequisites (tsort edges into this node)
cdf, pdf, real_field

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: F_Y(y) = P(g(X) <= y); for increasing g this is F_X(g^{-1}(y)), differentiate via the chain rule; for decreasing g, 1 - F_X(g^{-1}(y)); combine with |.|
derives_from: pdf
lean_status: cited — Durrett; Grimmett-Stirzaker 4.7

## Type / well-formedness check
derived by differentiating the CDF relation F_Y(y) = F_X(g^{-1}(y)) (increasing g) or 1 - F_X(g^{-1}(y)) (decreasing g); the absolute value handles both.

## Specialization / boundary cases
- g(x) = a x + b, a != 0: f_Y(y) = f_X((y-b)/a) / |a| -- affine rescaling
- g(x) = e^x on a normal X: Y is lognormal
- g(x) = x^2 (NOT monotone on R): split into x > 0 and x < 0 and add the two branches -- f_Y(y) = [f_X(sqrt y) + f_X(-sqrt y)] / (2 sqrt y)

## Hypothesis-dropped counterexamples
- **monotonicity_of_g**: g(x) = x^2 with X ~ N(0,1): the naive one-branch formula gives half the correct density; Y ~ chi-squared_1 requires summing both preimages
- **g_is_C1_with_nonzero_derivative**: if g'(x_0) = 0 the change of variables blows up; the density of Y develops a singularity there

## Common misuse
- forgetting the |Jacobian| factor
- applying the single-branch formula to a non-injective g
- using it when X has no density

## Related nodes (non-prerequisite)
- generalizes_to: jacobian_transformation
- special_case: the CDF method

## Sources
grimmett_stirzaker, durrett_pte
