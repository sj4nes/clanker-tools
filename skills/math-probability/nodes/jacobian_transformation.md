# jacobian_transformation

## Type
theorem

## Statement
If X is an R^n random vector with density f_X and g: R^n -> R^n is a diffeomorphism on an open set carrying P_X, then Y = g(X) has density f_Y(y) = f_X(g^{-1}(y)) |det J_{g^{-1}}(y)|.

## Symbols
- `g` — a diffeomorphism, type: R^n -> R^n, C^1 with C^1 inverse
- `J_{g^{-1}}` — the Jacobian matrix of g^{-1}, type: n x n matrix

## Epistemic status
proved_theorem

## Prerequisites (tsort edges into this node)
abstract_integral, pdf, transformation_univariate

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: change of variables in the Lebesgue integral (a cited real-analysis theorem) applied to the pushforward identity
derives_from: transformation_univariate
lean_status: cited — Folland; Billingsley Thm 17.2

## Type / well-formedness check
the multivariate change-of-variables formula for integrals, applied to P(Y in B) = P(X in g^{-1}(B)) = integral_{g^{-1}(B)} f_X = integral_B f_X(g^{-1}(y)) |det J_{g^{-1}}(y)| dy.

## Specialization / boundary cases
- polar coordinates on (X_1, X_2) ~ iid N(0,1): shows R^2 ~ Exponential and Theta ~ Uniform -- the Box-Muller method
- linear map Y = A X, A invertible: f_Y(y) = f_X(A^{-1} y) / |det A|
- sum-and-difference: (X+Y, X-Y) to get the distribution of a sum from a joint density

## Hypothesis-dropped counterexamples
- **g_a_diffeomorphism**: if g is not injective (e.g. (x_1,x_2) -> (x_1^2, x_2)) the preimage has multiple sheets and their Jacobian contributions must be summed
- **det_J_nonzero**: at a critical point det J_{g^{-1}} = inf and the transformed density is singular

## Common misuse
- using |det J_g| instead of |det J_{g^{-1}}| (they are reciprocals -- getting it backward inverts the density)
- applying to a non-injective map without summing sheets

## Related nodes (non-prerequisite)
- generalizes: transformation_univariate
- used_by: convolution_formula, simulation (Box-Muller)

## Sources
billingsley_probability_measure, grimmett_stirzaker
