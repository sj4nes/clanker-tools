# index_convention

## Type
notation_convention

## Statement
Vectors are COLUMNS. A in F^{m x n} has m rows and n columns; A_{ij} is the entry in row i and column j; indices start at 1. A row vector is written x^T.

## Symbols
- `A_{ij}` — the (i,j) entry, type: element of F
- `e_i` — the i-th standard basis column of F^n, type: element of F^n

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
(root — cited, see conventions.md)

## Hypotheses
(none — unconditional within scope)
## Type / well-formedness check
A convention, so there is nothing to prove -- but it is load-bearing: it fixes that Ax is a column, that the matrix of a map has the IMAGES of basis vectors as its columns (matrix_of_linear_map), and hence that [S o T] = [S][T] rather than the reverse.

## Specialization / boundary cases
- under the opposite (row-vector) convention the composition rule becomes [S o T] = [T][S] and every matrix identity in this capsule transposes

## Hypothesis-dropped counterexamples
- **none_all_hypotheses_essential**: a convention has no hypotheses; the failure mode is INCONSISTENCY, not falsity -- mixing conventions mid-derivation silently transposes results

## Common misuse
- reading x^T A x with x a row vector: the shapes then do not conform
- 0-based indexing when quoting the Leibniz formula or the cofactor sign (-1)^{i+j}, which shifts every sign

## Sources
hoffman_kunze_2e, strang_5e
