# convolution_formula

## Type
theorem

## Statement
If X, Y are independent with densities f_X, f_Y, then X + Y has density (f_X * f_Y)(z) = integral_R f_X(x) f_Y(z - x) dx. Discrete analogue: p_{X+Y}(k) = sum_j p_X(j) p_Y(k - j).

## Symbols
- `f_X, f_Y` — the marginal densities, type: R -> [0, inf)
- `*` — convolution, type: binary operation on densities

## Epistemic status
proved_theorem

## Prerequisites (tsort edges into this node)
abstract_integral, fubini_tonelli, independence_random_variables, pdf

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: push (x, y) -> (x, x + y) through the product density via jacobian_transformation (Jacobian 1), then integrate out x
derives_from: fubini_tonelli
lean_status: cited — Grimmett-Stirzaker 4.8; Durrett Thm 2.1.10

## Type / well-formedness check
P(X + Y <= z) = integral integral_{x + y <= z} f_X(x) f_Y(y) dy dx (product law, Fubini); differentiate in z. Convolution is commutative and associative, matching X + Y = Y + X and sums of three.

## Specialization / boundary cases
- Exponential(lambda) * Exponential(lambda) = Gamma(2, 1/lambda) -- sum of two iid exponentials
- N(0, s_1^2) * N(0, s_2^2) = N(0, s_1^2 + s_2^2)
- Poisson(a) * Poisson(b) = Poisson(a + b) (discrete convolution of the pmfs)

## Hypothesis-dropped counterexamples
- **independence**: for dependent X, Y the density of X + Y involves the joint density and is not a convolution -- e.g. Y = -X gives X + Y = 0, a point mass
- **existence_of_densities**: if X is discrete and Y continuous, X + Y has a density (a mixture of shifted f_Y), but the pure convolution-of-densities formula does not apply directly

## Common misuse
- convolving marginals of dependent variables
- sign error in f_Y(z - x) vs f_Y(x - z) (equal only if f_Y symmetric)

## Related nodes (non-prerequisite)
- requires: independence_random_variables
- cf_shortcut: phi_{X+Y} = phi_X phi_Y (often easier)
- used_by: gamma_distribution, normal_affine_closure

## Sources
grimmett_stirzaker, durrett_pte
