# dual_space

## Type
definition

## Statement
V^* = L(V, F), the space of linear FUNCTIONALS on V (linear maps into the scalar field).

## Symbols
- `f` — a functional, type: element of V^*
- `V^*` — type: vector space over F

## Epistemic status
definition  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
field, space_of_linear_maps

## Hypotheses
(none — unconditional within scope)
## Type / well-formedness check
Well-formed as a special case of L(V,W) with W = F, which is a one-dimensional F-space.

## Specialization / boundary cases
- V = F^n: V^* is the space of row vectors, f(x) = a^T x -- the transpose convention made concrete
- V = polynomials of degree <= d: evaluation at a point, and integration over an interval, are functionals

## Hypothesis-dropped counterexamples
- **finite_dimensionality**: dim V^* = dim V only in finite dimension (dual_basis). For infinite-dimensional V the ALGEBRAIC dual is strictly larger in cardinality, which is why double_dual fails there

## Common misuse
- identifying V with V^* without an inner product: the identification requires a choice of basis and is NOT canonical. With an inner product it becomes canonical (the Riesz correspondence), which is why the inner-product half of the capsule can use A^T freely

## Related nodes (non-prerequisite)
- required_by: dual_basis, dual_map, annihilator

## Sources
hoffman_kunze_2e, axler_lada_4e
