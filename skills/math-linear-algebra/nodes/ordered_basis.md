# ordered_basis

## Type
definition

## Statement
An ordered basis B = (b_1,...,b_n) of an n-dimensional V determines the coordinate map [.]_B : V -> F^n sending v to the column of its unique coefficients. It is a linear bijection.

## Symbols
- `[v]_B` — the coordinate column of v, type: element of F^n
- `B` — an ORDERED basis, type: finite sequence, not a set

## Epistemic status
definition  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
basis, basis_unique_representation, dimension

## Hypotheses
V finite-dimensional, B an ordered basis
## Type / well-formedness check
Well-formed by basis_unique_representation (coordinates exist and are unique) plus the index_convention (they are assembled as a COLUMN). Ordering is essential: permuting B permutes the coordinates.

## Specialization / boundary cases
- V = F^n with the standard ordered basis: [v]_B = v, the identity
- V = polynomials of degree <= 2 with B = (1, t, t^2): [3 + 5t^2]_B = (3, 0, 5)^T

## Hypothesis-dropped counterexamples
- **orderedness**: an unordered basis gives coordinates only up to permutation, so no well-defined map to F^n and no well-defined matrix of a linear map

## Common misuse
- writing [v] without recording which basis -- almost every sign and transposition error in applied linear algebra is a dropped basis label

## Related nodes (non-prerequisite)
- required_by: coordinate_isomorphism, matrix_of_linear_map

## Sources
hoffman_kunze_2e
