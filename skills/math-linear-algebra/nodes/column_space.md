# column_space

## Type
definition

## Statement
col(A) = span of the columns of A, a subspace of F^m. It equals the image of the map x -> Ax, so Ax = b is solvable exactly when b is in col(A).

## Symbols
- `A_{.j}` — the j-th column

## Epistemic status
definition  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
matrix, span

## Hypotheses
(none — unconditional within scope)
## Type / well-formedness check
Well-formed; the identification with the image is immediate from reading Ax as a combination of the columns, which is what the index_convention fixes.

## Specialization / boundary cases
- A a single column: col(A) is the line through it
- A invertible n x n: col(A) = F^n

## Hypothesis-dropped counterexamples
- **none_all_hypotheses_essential**: a definition. The trap is that column space is NOT preserved by row operations (see row_equivalence)

## Common misuse
- computing it from the RREF's columns rather than the original's pivot columns

## Related nodes (non-prerequisite)
- required_by: matrix_rank, least_squares, linear_system

## Sources
strang_5e
