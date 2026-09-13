# row_equivalence

## Type
definition

## Statement
A ~_r B if B = EA for some product E of elementary matrices (equivalently, B arises from A by a finite sequence of row operations). An equivalence relation that PRESERVES the row space and the null space, but NOT the column space.

## Symbols
- `~_r` — row equivalence, type: equivalence relation on F^{m x n}

## Epistemic status
definition  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
elementary_matrix, equivalence_relation

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: preservation: Ax = 0 iff EAx = 0 since E is invertible, giving null(A) = null(B); rows of EA are combinations of rows of A and conversely
derives_from: elementary_matrix
lean_status: cited

## Type / well-formedness check
Well-formed as an equivalence relation precisely because each elementary operation is invertible (reflexive via the empty product, symmetric via E^{-1}, transitive via composition).

## Specialization / boundary cases
- E = I: A ~_r A

## Hypothesis-dropped counterexamples
- **column_space_is_NOT_preserved**: A = [[1],[1]] and its RREF [[1],[0]] have different column spaces (the diagonal line versus the x-axis in F^2). What IS preserved is the DIMENSION of the column space and WHICH columns are pivot columns -- this distinction is the whole subtlety of row_rank_equals_column_rank
- **invertibility_of_E**: a singular E gives a relation that is not symmetric

## Common misuse
- reading a basis of the column space off the RREF's columns: read off WHICH columns are pivots, then take the CORRESPONDING columns of the ORIGINAL A

## Related nodes (non-prerequisite)
- required_by: rref_uniqueness

## Sources
hoffman_kunze_2e, strang_5e
