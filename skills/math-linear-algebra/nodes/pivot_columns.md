# pivot_columns

## Type
definition

## Statement
The pivot columns of A are the columns of A whose indices carry pivots in rref(A); the remaining columns are free. The PIVOT COLUMNS OF A (not of the RREF) form a basis of col(A); the free columns parameterise null(A).

## Symbols
- `A_{.j}` — the j-th column of the ORIGINAL matrix

## Epistemic status
definition  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
row_echelon_form, rref_uniqueness

## Hypotheses
rref(A) computed

## Proof provenance
technique: row operations preserve linear dependence relations among columns (they act on the left), so the original pivot columns are independent and the free ones are combinations of earlier pivot columns
derives_from: rref_uniqueness
lean_status: cited

## Type / well-formedness check
Well-formed by rref_uniqueness: the pivot INDEX SET is an invariant of A, even though the RREF's columns are not the original columns.

## Specialization / boundary cases
- A invertible: every column is a pivot column
- A = [[1,2],[2,4]]: one pivot, col(A) is spanned by (1,2)^T, and the second column is free

## Hypothesis-dropped counterexamples
- **using_A_not_its_RREF**: the RREF's pivot columns span a DIFFERENT subspace: for A = [[1],[1]], rref(A) = [[1],[0]] and col(rref A) is the x-axis, not the diagonal. The index set transfers; the columns do not. This is the single most common elimination error

## Common misuse
- reading a column-space basis off the RREF columns (see above)

## Related nodes (non-prerequisite)
- required_by: matrix_rank, row_rank_equals_column_rank

## Sources
strang_5e
