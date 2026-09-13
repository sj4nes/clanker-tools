# row_space

## Type
definition

## Statement
row(A) = span of the rows of A, a subspace of F^n. Invariant under row equivalence.

## Symbols
- `A_{i.}` — the i-th row of A, regarded as an element of F^n

## Epistemic status
definition  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
matrix, span

## Hypotheses
(none — unconditional within scope)
## Type / well-formedness check
Well-formed. Note row(A) lives in F^n (indexed by COLUMNS) while col(A) lives in F^m -- the two live in different spaces and cannot be compared as sets, only in dimension.

## Specialization / boundary cases
- row(A) = col(A^T), which is why every row statement has a transposed column counterpart

## Hypothesis-dropped counterexamples
- **none_all_hypotheses_essential**: a definition; the substance is its invariance under row_equivalence and its equality of dimension with col(A)

## Common misuse
- comparing row(A) and col(A) as subsets when m != n -- they are subspaces of different spaces

## Related nodes (non-prerequisite)
- dual_of: column_space
- required_by: four_subspaces, row_rank_equals_column_rank

## Sources
strang_5e
