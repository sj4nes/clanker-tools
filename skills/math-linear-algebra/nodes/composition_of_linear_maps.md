# composition_of_linear_maps

## Type
proposition

## Statement
The composite of linear maps is linear; composition is associative, and bilinear in each argument: (S_1 + S_2)T = S_1T + S_2T, S(T_1 + T_2) = ST_1 + ST_2, (aS)T = S(aT) = a(ST).

## Symbols
- `S o T` — written ST, type: linear map V -> X when T: V -> W and S: W -> X

## Epistemic status
proposition  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
linear_map, space_of_linear_maps

## Hypotheses
shapes conformable

## Proof provenance
technique: direct substitution; associativity is inherited from composition of functions
derives_from: linear_map
lean_status: cited

## Type / well-formedness check
Well-formed only when the shapes conform (codomain of T equals domain of S); this conformability is the abstract source of the matrix shape rule.

## Specialization / boundary cases
- V = W = X: L(V) becomes an associative unital algebra, the setting for minimal_polynomial and cayley_hamilton

## Hypothesis-dropped counterexamples
- **conformability**: composing non-conformable maps is not a false statement but an ill-typed one -- the type check is the whole content
- **commutativity_is_NOT_available**: ST != TS in general; see matrix_mult_noncommutative

## Common misuse
- cancelling: ST = SU does not give T = U unless S is injective

## Related nodes (non-prerequisite)
- required_by: linear_operator, matrix_mult_is_composition, dual_map

## Sources
axler_lada_4e
