# dimension_of_subspace

## Type
proposition

## Statement
If U is a subspace of a finite-dimensional V then U is finite-dimensional, dim U <= dim V, and dim U = dim V if and only if U = V.

## Symbols
- `U` — a subspace of V

## Epistemic status
proposition  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
basis_existence_finite, dimension

## Hypotheses
V finite-dimensional, U a subspace of V

## Proof provenance
technique: a basis of U is independent in V so has at most dim V elements (Steinitz); if dim U = dim V, a basis of U is a maximal independent family in V hence spans V
derives_from: steinitz_exchange
lean_status: cited

## Type / well-formedness check
Well-formed. The equality clause is the workhorse: it converts a dimension count into a set equality, which is how most 'these two subspaces coincide' arguments in the capsule are closed.

## Specialization / boundary cases
- U = {0}: dimension 0 <= dim V
- dim U = dim V - 1: a hyperplane, the kernel of a nonzero functional (see annihilator)

## Hypothesis-dropped counterexamples
- **finite_dimensionality_of_V**: in F[t] the subspace of polynomials with zero constant term is a PROPER subspace with the same (infinite) dimension -- the equality clause fails outright. This is the same phenomenon as the infinite-dimensional failure of injective_surjective_equivalence

## Common misuse
- applying the equality clause without checking dim V is finite

## Sources
axler_lada_4e
