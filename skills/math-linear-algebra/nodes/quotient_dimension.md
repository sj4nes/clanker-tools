# quotient_dimension

## Type
proposition

## Statement
For a finite-dimensional V and a subspace U, dim(V/U) = dim V - dim U. The number dim(V/U) is the CODIMENSION of U in V.

## Symbols
- `codim U` — = dim(V/U), type: natural number

## Epistemic status
proposition  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
basis_existence_finite, dimension, finite_dimensional, quotient_space

## Hypotheses
V finite-dimensional, U a subspace

## Proof provenance
technique: extend a basis of U to a basis of V; the images of the added vectors form a basis of V/U
derives_from: basis_existence_finite
lean_status: core — LinAlg.dim_quotient

## Type / well-formedness check
Well-formed; the subtraction is legitimate because dim U <= dim V by dimension_of_subspace.

## Specialization / boundary cases
- U = {0}: dim(V/U) = dim V
- U a hyperplane: codimension 1, and V/U is one-dimensional -- the setting of a single linear functional

## Hypothesis-dropped counterexamples
- **finite_dimensionality**: codimension can be finite while both dimensions are infinite (the polynomials with zero constant term have codimension 1 in F[t]), so the SUBTRACTION is meaningless even though the quotient is fine. Codimension, not dimension, is the robust notion

## Common misuse
- computing codimension as dim V - dim U when V is infinite-dimensional: define it as dim(V/U) directly

## Related nodes (non-prerequisite)
- required_by: first_isomorphism_theorem

## Sources
hoffman_kunze_2e
