# slutsky_theorem

## Type
theorem

## Statement
If X_n -> X in distribution and Y_n -> c in probability (c a constant), then X_n + Y_n -> X + c, X_n Y_n -> cX, and X_n / Y_n -> X / c (c != 0), all in distribution.

## Symbols
- `X_n` — sequence converging in distribution, type: N -> (Omega -> R)
- `Y_n` — sequence converging in probability to a constant c, type: N -> (Omega -> R)
- `c` — a constant, type: real

## Epistemic status
proved_theorem

## Prerequisites (tsort edges into this node)
continuous_mapping_theorem, convergence_in_distribution, convergence_in_probability, portmanteau_theorem

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: Y_n -> c in probability => (X_n, Y_n) -> (X, c) jointly in distribution (the constant limit removes the dependence problem), then continuous_mapping_theorem on +, x, /
derives_from: continuous_mapping_theorem
lean_status: cited — Durrett Thm 3.2.8 (Ex); Billingsley Thm 25.4

## Type / well-formedness check
the key asymmetry: one sequence may converge only in distribution, but the OTHER must converge in probability to a CONSTANT (not a random variable). Then (X_n, Y_n) -> (X, c) jointly in distribution and the continuous map applies.

## Specialization / boundary cases
- studentization: sqrt(n)(Xbar - mu)/S_n -> N(0,1), because sqrt(n)(Xbar - mu)/sigma -> N(0,1) and sigma/S_n -> 1 in probability
- if a_n -> a and b_n -> b (deterministic) and Z_n -> Z in distribution then a_n Z_n + b_n -> a Z + b

## Hypothesis-dropped counterexamples
- **the_limit_c_must_be_a_constant**: X_n = Z ~ N(0,1) for all n (so X_n -> Z in distribution), Y_n = -Z (so Y_n -> -Z in distribution, NOT to a constant): X_n + Y_n = 0, not N(0,1) + N(0,1). Slutsky needs Y_n -> constant.
- **convergence_in_probability_not_just_distribution_for_Y_n**: if Y_n -> c only in distribution (c constant) that is equivalent to in probability, so this is automatically fine -- but Y_n -> non-constant in distribution is not enough

## Common misuse
- applying it when both sequences converge only in distribution
- letting the 'constant' limit actually be a non-degenerate random variable

## Related nodes (non-prerequisite)
- special_case_of: continuous_mapping_theorem (joint)
- used_by: delta_method

## Sources
durrett_pte, billingsley_probability_measure
