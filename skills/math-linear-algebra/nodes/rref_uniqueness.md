# rref_uniqueness

## Type
theorem

## Statement
Every matrix is row equivalent to EXACTLY ONE matrix in reduced row echelon form. RREF is therefore a canonical form for row equivalence.

## Symbols
- `R = rref(A)` — the canonical representative

## Epistemic status
proved_theorem  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
row_echelon_form, row_equivalence

## Hypotheses
F a field

## Proof provenance
technique: existence by Gaussian elimination. Uniqueness: row equivalence preserves null(A), and the RREF is determined by null(A) -- the pivot columns are those not expressible in terms of earlier columns, and the free columns' entries are exactly the coefficients of that expression
derives_from: row_equivalence
lean_status: cited

## Type / well-formedness check
Well-formed. Existence is the elimination algorithm; uniqueness is the substantive half and is what licenses defining rank and pivot columns from the RREF.

## Specialization / boundary cases
- A invertible: rref(A) = I, giving one clause of invertibility_equivalences
- A a single nonzero row: rref(A) has leading 1 in the first nonzero column

## Hypothesis-dropped counterexamples
- **reducedness**: non-reduced echelon forms are NOT unique: [[1,2],[0,1]] and [[1,0],[0,1]] are both REF for the same matrix. Only the RREF is canonical
- **F_a_field**: over Z one cannot scale a pivot to 1; the canonical form is instead Hermite (or Smith) normal form -- see smith_normal_form_boundary

## Common misuse
- assuming the intermediate echelon forms produced by different pivoting orders agree: only the final RREF does

## Related nodes (non-prerequisite)
- required_by: row_rank_equals_column_rank, invertibility_equivalences

## Sources
hoffman_kunze_2e
