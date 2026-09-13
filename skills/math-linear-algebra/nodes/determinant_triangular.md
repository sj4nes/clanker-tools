# determinant_triangular

## Type
proposition

## Statement
The determinant of a triangular matrix is the product of its diagonal entries.

## Symbols
- `A_{ii}` — the diagonal entries

## Epistemic status
proposition  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
determinant, leibniz_formula, triangular_matrix

## Hypotheses
A triangular

## Proof provenance
technique: in the Leibniz sum, a permutation other than the identity must pick an entry above the diagonal in some column and below it in another; triangularity makes one of these zero
derives_from: leibniz_formula
lean_status: dim_core — LinAlg.det_triangular (n = 2)

## Type / well-formedness check
Well-formed for upper or lower triangular A, and in particular for diagonal A.

## Specialization / boundary cases
- A = I: det = 1, recovering the normalisation
- combined with determinant_row_operations, this is the O(n^3) algorithm: eliminate to triangular, multiply the diagonal, correct for swaps and scalings

## Hypothesis-dropped counterexamples
- **triangularity**: a general matrix's determinant is NOT the product of its diagonal: [[0,1],[1,0]] has diagonal product 0 but determinant -1
- **block_version**: for a BLOCK triangular matrix det is the product of the DIAGONAL BLOCKS' determinants -- but only when the off-diagonal block is on one side; see schur_complement for the general case

## Common misuse
- reading the diagonal of a general matrix as its eigenvalues (true only for triangular matrices)

## Related nodes (non-prerequisite)
- required_by: determinant_invertible_iff, characteristic_polynomial

## Sources
hoffman_kunze_2e
