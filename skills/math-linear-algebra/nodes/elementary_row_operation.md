# elementary_row_operation

## Type
definition

## Statement
Three operations on the rows of a matrix: (R1) swap two rows; (R2) multiply a row by a NONZERO scalar; (R3) add a scalar multiple of one row to a DIFFERENT row. Each is reversible.

## Symbols
- `r_i` — the i-th row
- `c` — a scalar, required nonzero in R2

## Epistemic status
definition  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
field, matrix

## Hypotheses
c != 0 in R2, i != j in R3
## Type / well-formedness check
Well-formed. The two side conditions (c != 0 in R2, i != j in R3) are exactly what makes each operation invertible, hence what makes row_equivalence an equivalence relation.

## Specialization / boundary cases
- R3 with c = 0 is the identity operation, harmless but useless
- R1 is expressible via three R3's and one R2 over any field, so the swap is redundant in principle

## Hypothesis-dropped counterexamples
- **nonzero_scalar_in_R2**: multiplying a row by 0 destroys information irreversibly, changes the row space, and can turn a nonsingular matrix singular
- **distinct_rows_in_R3**: r_i -> r_i + c r_i is R2 with factor (1 + c), which is NOT invertible when c = -1 -- allowing i = j would break reversibility

## Common misuse
- applying COLUMN operations while tracking the null space: row operations preserve null(A), column operations preserve col(A), and mixing them preserves neither

## Related nodes (non-prerequisite)
- required_by: elementary_matrix, row_echelon_form

## Sources
hoffman_kunze_2e, strang_5e
