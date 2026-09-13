# dual_map

## Type
definition

## Statement
For T: V -> W the dual (transpose) map T^t: W^* -> V^* is T^t(g) = g o T. It REVERSES direction, and (ST)^t = T^t S^t.

## Symbols
- `T^t` — the dual map, type: linear map W^* -> V^*
- `g` — a functional on W, type: element of W^*

## Epistemic status
definition  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
composition_of_linear_maps, dual_space

## Hypotheses
T linear

## Proof provenance
technique: linearity of T^t from bilinearity of composition; the contravariance from associativity
derives_from: composition_of_linear_maps
lean_status: cited

## Type / well-formedness check
Well-formed: g o T is a composite of linear maps V -> W -> F, hence an element of V^*. The direction reversal is forced by the types, and it is the abstract reason (AB)^T = B^T A^T.

## Specialization / boundary cases
- in dual bases, the matrix of T^t is the TRANSPOSE of the matrix of T -- the conceptual content of the transpose operation
- T = I: T^t = I

## Hypothesis-dropped counterexamples
- **none_all_hypotheses_essential**: the definition needs only linearity; it is the MATRIX statement that needs finite-dimensionality and a choice of dual bases

## Common misuse
- expecting T^t: V^* -> W^*: the arrow reverses. Every 'why is it B^T A^T and not A^T B^T' question is answered here
- confusing the dual map (no inner product needed) with the ADJOINT T^* (needs an inner product and conjugates over C) -- they agree over R under the Riesz identification only

## Related nodes (non-prerequisite)
- dual_of: transpose
- contrasts_with: adjoint_operator

## Sources
hoffman_kunze_2e, axler_lada_4e
