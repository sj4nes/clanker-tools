# independence_factorization

## Type
theorem

## Statement
X, Y are independent iff F_{X,Y}(x, y) = F_X(x) F_Y(y) for all x, y; iff (when densities exist) f_{X,Y}(x, y) = f_X(x) f_Y(y) for a.e. (x, y); iff (discrete) p_{X,Y}(x,y) = p_X(x) p_Y(y).

## Symbols
- `F_{X,Y}, f_{X,Y}` — joint CDF / density, type: R^2 -> [0,1] / [0, inf)

## Epistemic status
proved_theorem

## Prerequisites (tsort edges into this node)
cdf, dynkin_pi_lambda, independence_random_variables, joint_distribution, pdf

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: factorization on the generating pi-system of rectangles + pi-lambda; for densities, integrate/differentiate the CDF statement
derives_from: dynkin_pi_lambda
lean_status: cited — Billingsley Thm 20.1; Durrett Thm 2.1.7

## Type / well-formedness check
the half-line rectangles (-inf, x] x (-inf, y] are a pi-system generating B(R^2); the factorization of the joint CDF there extends to full independence by the pi-lambda theorem.

## Specialization / boundary cases
- a joint density that is a product g(x) h(y) (even unnormalized) => X, Y independent with marginals proportional to g, h -- the 'factorization criterion'
- checking independence: it is enough that the SUPPORT is a product AND the density factors on it

## Hypothesis-dropped counterexamples
- **factorization_over_the_full_support**: f_{X,Y}(x,y) = 2 on the triangle 0 < x < y < 1: the density is 'constant' but the support is not a rectangle, so X, Y are NOT independent (Y | X = x is Uniform(x, 1))

## Common misuse
- reading a constant joint density as independence without checking the support is a product
- checking factorization at a few points rather than a.e.

## Related nodes (non-prerequisite)
- uses: dynkin_pi_lambda
- operationalizes: independence_random_variables

## Sources
billingsley_probability_measure, durrett_pte
