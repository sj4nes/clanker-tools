# elementary_matrix

## Type
construction

## Statement
Each elementary row operation on A equals left multiplication EA, where E is the result of applying that operation to I. Every elementary matrix is invertible, with an elementary inverse of the same type.

## Symbols
- `E` — an elementary matrix, type: invertible element of F^{m x m}

## Epistemic status
constructive_result  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
elementary_row_operation, identity_matrix, invertible_matrix, matrix_multiplication

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: compute EA row by row; invertibility because each operation is reversible by an operation of the same type
derives_from: elementary_row_operation
lean_status: cited

## Type / well-formedness check
Well-formed. Left multiplication acts on rows and right multiplication on columns -- a consequence of the index_convention, not a separate fact.

## Specialization / boundary cases
- E for R2 with factor c has inverse the R2 matrix with factor c^{-1}
- E for R3 with factor c has inverse the R3 matrix with factor -c
- E for R1 is its own inverse

## Hypothesis-dropped counterexamples
- **invertibility_of_each_operation**: an 'operation' multiplying a row by 0 has a singular E and generates no equivalence relation

## Common misuse
- forgetting that applying row operations to A means LEFT-multiplying, so a recorded sequence composes in reverse order: A -> E_k...E_1 A

## Related nodes (non-prerequisite)
- required_by: row_equivalence, determinant_multiplicative, lu_factorisation

## Sources
hoffman_kunze_2e
