# annihilator

## Type
definition

## Statement
For a subspace U of V, the annihilator is U^0 = {f in V^* : f(u) = 0 for all u in U}, a subspace of V^*. In finite dimension dim U + dim U^0 = dim V.

## Symbols
- `U^0` — type: subspace of V^*

## Epistemic status
definition  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
dual_basis, dual_space, subspace

## Hypotheses
V finite-dimensional for the dimension identity

## Proof provenance
technique: extend a basis of U to a basis of V; the dual functionals indexed by the ADDED vectors form a basis of U^0
derives_from: dual_basis
lean_status: cited

## Type / well-formedness check
Well-formed: the conditions f(u) = 0 are linear in f, so U^0 is an intersection of kernels of functionals on V^*, hence a subspace.

## Specialization / boundary cases
- U = {0}: U^0 = V^*
- U = V: U^0 = {0}
- U a hyperplane: U^0 is one-dimensional, spanned by any functional cutting it out

## Hypothesis-dropped counterexamples
- **finite_dimensionality**: the dimension identity fails in infinite dimension, where it must be replaced by a statement about codimension
- **no_inner_product_needed**: U^0 lives in V^*, NOT in V. The analogous object inside V is the orthogonal complement U^perp, which requires an inner product; conflating them is the standard error

## Common misuse
- writing U^0 as a subspace of V -- it is a subspace of the DUAL. The two coincide only after the Riesz identification supplied by an inner product

## Related nodes (non-prerequisite)
- dual_of: orthogonal_complement

## Sources
hoffman_kunze_2e
