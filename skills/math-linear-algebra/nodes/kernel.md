# kernel

## Type
definition

## Statement
ker T = {v in V : T(v) = 0}, the null space of T. It is a subspace of V.

## Symbols
- `ker T` — type: subspace of V (the DOMAIN)

## Epistemic status
definition  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
linear_map, subspace

## Hypotheses
T linear

## Proof provenance
technique: subspace by the criterion applied to linearity
derives_from: subspace_criterion
lean_status: cited

## Type / well-formedness check
Well-formed and a subspace: 0 is in it, and linearity gives closure -- T(au + bv) = aT(u) + bT(v) = 0.

## Specialization / boundary cases
- T = 0: ker T = V
- T injective: ker T = {0} (injective_iff_trivial_kernel)
- T = differentiation on polynomials: ker T = the constants, dimension 1

## Hypothesis-dropped counterexamples
- **linearity_of_T**: for a nonlinear f, f^{-1}(0) is generally not a subspace: the preimage of 0 under x -> x^2 - 1 on R is {-1, 1}
- **the_target_being_zero**: T^{-1}({w}) for w != 0 is an AFFINE subspace (a coset of ker T), not a subspace -- this is exactly the solution-set structure of linear_system

## Common misuse
- confusing ker T (in V) with the zero subspace of W
- computing 'the kernel' of a matrix without saying whether the matrix acts on the left or right -- null(A) and null(A^T) are different (left_null_space)

## Related nodes (non-prerequisite)
- required_by: rank_nullity, eigenspace, null_space

## Sources
axler_lada_4e
