# variance_affine

## Type
identity

## Statement
Var(aX + b) = a^2 Var(X). Standard deviation scales as |a|; adding a constant b does not change the variance.

## Symbols
- `a, b` — constants, type: real
- `X` — a random variable in L^2(P), type: L^2(P)

## Epistemic status
mathematical_identity

## Prerequisites (tsort edges into this node)
expectation_linearity, variance, variance_computational

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: substitute into the definition; the b cancels, a factors out squared
derives_from: expectation_linearity
lean_status: core — validation/proof-checks.lean Prob.var_affine (GENUINE: the 2ab.n.sx and b^2 n^2 terms cancel)

## Type / well-formedness check
E[aX + b] = a E[X] + b, so (aX + b) - E[aX + b] = a(X - E[X]); square and take expectations.

## Specialization / boundary cases
- standardization: Z = (X - mu)/sigma has Var(Z) = 1
- a = -1: Var(-X) = Var(X)

## Hypothesis-dropped counterexamples
- **none_holds_whenever_Var_X_is_finite**: unconditional given a finite second moment

## Common misuse
- writing Var(aX) = a Var(X) (missing the square)
- thinking b affects the spread

## Related nodes (non-prerequisite)
- derives_from: variance_computational
- used_by: standard_normal, central_limit_theorem

## Sources
billingsley_probability_measure, durrett_pte
