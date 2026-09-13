# determinant_row_operations

## Type
proposition

## Statement
Under R1 (swap) det negates; under R2 (scale a row by c) det scales by c; under R3 (add a multiple of one row to another) det is UNCHANGED. Hence elimination computes det in O(n^3).

## Symbols
- `c` — the scaling factor in R2

## Epistemic status
proposition  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
determinant, elementary_row_operation, multilinear_alternating_form

## Hypotheses
A square

## Proof provenance
technique: R2 from multilinearity, R1 from antisymmetry, R3 by splitting the modified row by multilinearity: the extra term has two equal rows and so vanishes by alternation
derives_from: multilinear_alternating_form
lean_status: dim_core — LinAlg.det_row_op_R1/R2/R3 and LinAlg.det_smul (the det(kX) = k^2 det X trap), n = 2

## Type / well-formedness check
Well-formed. Stated for ROWS; the column versions follow from determinant_transpose, and the alternating property is a column property by definition -- so this proposition is where rows and columns are first tied together.

## Specialization / boundary cases
- A with two equal rows: repeated R3 produces a zero row, so det = 0
- A with a zero row: det = 0 by R2 with c = 0

## Hypothesis-dropped counterexamples
- **R3_requires_distinct_rows**: r_i -> r_i + c r_i is R2 in disguise and DOES change det by (1+c); the i != j condition in elementary_row_operation is what makes R3 determinant-preserving
- **R2_scales_ONE_row**: scaling the whole matrix by c scales det by c^n, not by c -- det(cA) = c^n det(A) is the single most common determinant error

## Common misuse
- writing det(cA) = c det(A)
- writing det(A + B) = det A + det B: the determinant is multilinear in COLUMNS, not linear in the matrix

## Related nodes (non-prerequisite)
- required_by: determinant_multiplicative, determinant_invertible_iff

## Sources
hoffman_kunze_2e, strang_5e
