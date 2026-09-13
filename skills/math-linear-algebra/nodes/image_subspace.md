# image_subspace

## Type
definition

## Statement
im T = T(V) = {T(v) : v in V}, the range of T. It is a subspace of W.

## Symbols
- `im T` — type: subspace of W (the CODOMAIN)

## Epistemic status
definition  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
linear_map, subspace

## Hypotheses
T linear

## Proof provenance
technique: closure from linearity
derives_from: subspace_criterion
lean_status: cited

## Type / well-formedness check
Well-formed and a subspace: it contains T(0) = 0 and is closed because aT(u) + bT(v) = T(au + bv).

## Specialization / boundary cases
- T surjective: im T = W
- T = 0: im T = {0}
- T = x -> Ax: im T = col(A), the column space -- this identification is why column_space is defined as it is

## Hypothesis-dropped counterexamples
- **linearity**: the image of a nonlinear map is usually not a subspace: x -> x^2 maps R onto [0, infinity)

## Common misuse
- conflating the image (a subspace of W) with the codomain W: T is surjective exactly when they coincide, which is a theorem to prove, not a definition

## Related nodes (non-prerequisite)
- required_by: rank, first_isomorphism_theorem

## Sources
axler_lada_4e
