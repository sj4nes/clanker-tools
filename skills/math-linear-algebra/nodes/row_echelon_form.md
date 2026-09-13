# row_echelon_form

## Type
definition

## Statement
A is in row echelon form if all zero rows are at the bottom and each nonzero row's leading entry (pivot) is strictly to the right of the one above. REDUCED row echelon form additionally requires every pivot to be 1 and to be the only nonzero entry in its column.

## Symbols
- `pivot` — the leftmost nonzero entry of a nonzero row

## Epistemic status
definition  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
elementary_row_operation, matrix

## Hypotheses
(none — unconditional within scope)
## Type / well-formedness check
Well-formed. REF is not unique (any REF can be scaled); RREF is (rref_uniqueness), which is what makes it a canonical form.

## Specialization / boundary cases
- A invertible: its RREF is I
- A = 0: already in RREF with no pivots
- the number of pivots is the same for EVERY echelon form of A -- this is what matrix_rank is counting

## Hypothesis-dropped counterexamples
- **none_all_hypotheses_essential**: a definition; the substantive claim is uniqueness, stated separately

## Common misuse
- calling any upper-triangular matrix an echelon form -- the pivot positions must strictly increase, which a triangular matrix with a zero on the diagonal violates

## Related nodes (non-prerequisite)
- required_by: rref_uniqueness, gaussian_elimination, pivot_columns

## Sources
hoffman_kunze_2e, strang_5e
