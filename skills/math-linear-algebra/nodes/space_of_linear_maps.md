# space_of_linear_maps

## Type
structure

## Statement
L(V,W) is the set of linear maps V -> W, a vector space under (S+T)(v) = S(v) + T(v) and (aT)(v) = aT(v). If dim V = n and dim W = m are finite then dim L(V,W) = mn.

## Symbols
- `L(V,W)` — type: vector space over F
- `L(V)` — abbreviation for L(V,V)

## Epistemic status
definition  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
dimension, linear_map, linear_map_determined_by_basis, vector_space

## Hypotheses
V, W over the same field F

## Proof provenance
technique: the dimension count follows from linear_map_determined_by_basis: a map is freely specified by the n images, each with m coordinates
derives_from: linear_map_determined_by_basis
lean_status: cited

## Type / well-formedness check
Well-formed: the pointwise operations land in L(V,W) because a sum and a scalar multiple of linear maps is linear.

## Specialization / boundary cases
- W = F: L(V,F) = V^*, the dual space, of dimension n
- V = W = F^n: L(V) is isomorphic to F^{n x n}, of dimension n^2

## Hypothesis-dropped counterexamples
- **finite_dimensionality**: for infinite-dimensional V the algebraic dual and hence L(V,W) is strictly larger than V in cardinality, and dim L(V,F) > dim V -- which is exactly why double_dual fails

## Common misuse
- assuming L(V) is commutative: composition is not (matrix_mult_noncommutative)

## Related nodes (non-prerequisite)
- required_by: dual_space, minimal_polynomial

## Sources
axler_lada_4e, hoffman_kunze_2e
