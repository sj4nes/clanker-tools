# conditional_expectation_abstract

## Type
definition

## Statement
For X in L^1(Omega, F, P) and a sub-sigma-algebra G subset F, E[X | G] is any random variable Z such that (i) Z is G-measurable and (ii) integral_A Z dP = integral_A X dP for every A in G. It is unique up to P-a.s. equality.

## Symbols
- `X` — an integrable random variable, type: L^1(P)
- `G` — a sub-sigma-algebra (the conditioning information), type: sigma-algebra subset F
- `Z` — the conditional expectation E[X | G], type: L^1(Omega, G, P)

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
abstract_integral, almost_sure, expectation, measurable_function, sigma_algebra

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: existence and uniqueness are conditional_expectation_existence (Radon-Nikodym or L^2 projection); this node is the DEFINITION via the two properties
lean_status: cited — Williams ch. 9; Durrett ch. 4

## Type / well-formedness check
the defining property is (i) measurability + (ii) matching integrals on G-sets; conditioning on a variable is E[X | sigma(Y)]. This handles conditioning on probability-zero events, which the elementary definition cannot.

## Specialization / boundary cases
- G = { empty, Omega }: E[X | G] = E[X] (a constant)
- G = F: E[X | G] = X
- X G-measurable: E[X | G] = X; X independent of G: E[X | G] = E[X]
- pull-out: E[Y X | G] = Y E[X | G] when Y is G-measurable and bounded

## Hypothesis-dropped counterexamples
- **integrability_of_X**: for X >= 0 not integrable one defines E[X | G] in [0, inf] by monotone approximation; for signed non-integrable X it need not exist
- **measurability_condition_(i)**: dropping (i) makes Z = X trivially satisfy (ii) -- the content is that Z is COARSER (G-measurable), a genuine projection / averaging

## Common misuse
- computing integral_A Z = integral_A X only for A generating G, without checking it is a pi-system (then pi-lambda is needed)
- treating E[X | G] as defined pointwise (it is an a.s. equivalence class)

## Related nodes (non-prerequisite)
- exists_by: conditional_expectation_existence
- generalizes: conditional_expectation_elementary, law_of_total_probability
- is_a: projection (conditional_expectation_l2_projection)

## Sources
williams_probability_martingales, durrett_pte
