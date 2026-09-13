# null_space

## Type
definition

## Statement
null(A) = {x in F^n : Ax = 0}, the kernel of x -> Ax, a subspace of F^n. Invariant under row equivalence.

## Symbols
- `null(A)` — type: subspace of F^n

## Epistemic status
definition  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
kernel, matrix

## Hypotheses
(none — unconditional within scope)
## Type / well-formedness check
Well-formed as the kernel of a linear map; the invariance under row equivalence is the reason elimination solves homogeneous systems.

## Specialization / boundary cases
- A invertible: null(A) = {0}
- dim null(A) = n - rank A by rank_nullity, so the free columns count the dimension

## Hypothesis-dropped counterexamples
- **none_all_hypotheses_essential**: a definition

## Common misuse
- confusing null(A) with null(A^T) (the left null space), which lives in F^m and is what makes a system INCONSISTENT rather than underdetermined

## Related nodes (non-prerequisite)
- dual_of: left_null_space
- required_by: four_subspaces, linear_system

## Sources
strang_5e
