# cdf_determines_law

## Type
theorem

## Statement
If F_X = F_Y then P_X = P_Y: the CDF determines the entire distribution.

## Symbols
- `F_X, F_Y` — CDFs, type: R -> [0,1]
- `P_X, P_Y` — laws, type: probability measure on B(R)

## Epistemic status
proved_theorem

## Prerequisites (tsort edges into this node)
cdf, distribution_pushforward, dynkin_pi_lambda

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: the sets where P_X and P_Y agree form a lambda-system containing the pi-system of half-lines; pi-lambda gives sigma(half-lines) = B(R)
derives_from: dynkin_pi_lambda
lean_status: cited — Billingsley Thm 12.4

## Type / well-formedness check
the half-lines { (-inf, x] } are a pi-system generating B(R); two probability measures agreeing on a generating pi-system (and both giving R measure 1) agree on the whole sigma-algebra by the pi-lambda theorem.

## Specialization / boundary cases
- hence P(X in B) can always be computed from F_X (by pi-lambda / Caratheodory), even for complicated Borel B
- the analogous statement in R^d: the joint CDF F(x_1,...,x_d) = P(X_1<=x_1, ..., X_d<=x_d) determines the joint law

## Hypothesis-dropped counterexamples
- **pi_system_generates_the_sigma_algebra**: agreeing on a non-generating or non-pi-system family is not enough -- see the dynkin_pi_lambda counterexample

## Common misuse
- believing equal PDFs/PMFs is a weaker condition (it is equivalent, given the type)
- in R^d, checking only the one-dimensional marginals -- those do NOT determine the joint law

## Related nodes (non-prerequisite)
- uses: dynkin_pi_lambda
- equivalent_to: P_X = P_Y, phi_X = phi_Y

## Sources
billingsley_probability_measure, durrett_pte
