# matrix

## Type
definition

## Statement
A in F^{m x n} is a function {1..m} x {1..n} -> F, displayed as a rectangular array with m rows and n columns.

## Symbols
- `A` — the matrix, type: element of F^{m x n}
- `m, n` — the shape, type: positive integers

## Epistemic status
definition  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
field, index_convention, set

## Hypotheses
(none — unconditional within scope)
## Type / well-formedness check
Well-formed. A matrix is data, not a map: it BECOMES a map only after the index_convention fixes that Ax means the column combination sum_j x_j A_{.j}, and the same array represents different maps under different bases.

## Specialization / boundary cases
- m = n: a square matrix, the only shape for which eigenvalues, determinant, and trace are defined
- n = 1: a column vector; m = 1: a row vector
- m = n = 1: a scalar, under which every matrix identity in the capsule degenerates to field arithmetic

## Hypothesis-dropped counterexamples
- **none_all_hypotheses_essential**: a definition. The trap is identifying the array with a map without naming the bases -- see matrix_of_linear_map

## Common misuse
- speaking of THE eigenvalues of a rectangular matrix (use singular_values)
- treating a matrix as basis-independent: similarity classes, not matrices, correspond to operators

## Related nodes (non-prerequisite)
- required_by: matrix_multiplication, determinant

## Sources
hoffman_kunze_2e, strang_5e
