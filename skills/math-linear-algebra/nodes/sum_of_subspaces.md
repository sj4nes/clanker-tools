# sum_of_subspaces

## Type
definition

## Statement
U + W = {u + w : u in U, w in W}, the smallest subspace of V containing both. More generally sum_i U_i is the set of finite sums of elements of the U_i.

## Symbols
- `U + W` — type: subspace of V

## Epistemic status
definition  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
span, subspace

## Hypotheses
(none — unconditional within scope)
## Type / well-formedness check
Well-formed, and equal to span(U union W) -- which is why the union itself (usually not a subspace, see subspace_intersection) is not the right object.

## Specialization / boundary cases
- U + {0} = U
- U + U = U
- in R^3, the sum of two distinct planes through the origin is all of R^3

## Hypothesis-dropped counterexamples
- **none_all_hypotheses_essential**: a definition; the trap is the union, which is generally not a subspace

## Common misuse
- writing U union W for the span of two subspaces
- assuming dim(U + W) = dim U + dim W without directness -- see dimension_formula_sum

## Related nodes (non-prerequisite)
- required_by: direct_sum, dimension_formula_sum

## Sources
axler_lada_4e
