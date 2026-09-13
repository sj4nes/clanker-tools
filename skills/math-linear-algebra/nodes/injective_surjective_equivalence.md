# injective_surjective_equivalence

## Type
corollary

## Statement
If dim V = dim W < infinity then for T: V -> W the conditions injective, surjective, and bijective are EQUIVALENT.

## Symbols
- `T` — a linear map between spaces of equal finite dimension

## Epistemic status
corollary  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
dimension_of_subspace, finite_dimensional, injective_iff_trivial_kernel, rank_nullity

## Hypotheses
dim V = dim W, V finite-dimensional

## Proof provenance
technique: injective gives nullity 0, so rank = dim V = dim W, so im T = W by dimension_of_subspace; conversely surjective gives rank = dim W = dim V, so nullity 0
derives_from: rank_nullity
lean_status: core — LinAlg.inj_iff_surj_of_dim_eq

## Type / well-formedness check
Well-formed. Both the equality of dimensions AND their finiteness are needed; the node carries edges to finite_dimensional for exactly this reason.

## Specialization / boundary cases
- V = W = F^n: a square matrix is injective iff surjective iff invertible -- one clause of invertibility_equivalences
- the finite-field analogue of the pigeonhole principle for linear maps

## Hypothesis-dropped counterexamples
- **finite_dimensionality**: on F[t], multiplication by t is injective but not surjective (nothing maps to the constant 1); formal differentiation is surjective but not injective. Both live on the SAME space, so equality of dimensions holds trivially and it is finiteness alone that fails
- **equal_dimensions**: F^2 -> F^3 can be injective and never surjective; F^3 -> F^2 can be surjective and never injective

## Common misuse
- applying it to operators on function spaces, where it is exactly false and is the reason Fredholm theory exists
- applying it to a non-square matrix

## Related nodes (non-prerequisite)
- illustrated_by: infinite_dimensional_boundary

## Sources
axler_lada_4e
