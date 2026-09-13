# determinant_invertible_iff

## Type
theorem

## Statement
A square matrix over a FIELD is invertible if and only if det A != 0, and then det(A^{-1}) = 1/det(A).

## Symbols
- `det A` — an element of F, tested against 0

## Epistemic status
proved_theorem  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
determinant, determinant_multiplicative, determinant_row_operations, invertible_matrix, rref_uniqueness

## Hypotheses
A square, F a field

## Proof provenance
technique: if A is invertible, multiplicativity on AA^{-1} = I gives det(A)det(A^{-1}) = 1 so det A != 0. Conversely, if A is singular its columns are dependent, so an R3 sequence produces a zero column and det A = 0
derives_from: determinant_multiplicative
lean_status: cited

## Type / well-formedness check
Well-formed over a field. Over a commutative RING the correct statement is 'invertible iff det A is a UNIT', which over Z means det = +-1, not merely nonzero.

## Specialization / boundary cases
- n = 1: [a] invertible iff a != 0
- A triangular: invertible iff no diagonal entry is 0, combining this with determinant_triangular

## Hypothesis-dropped counterexamples
- **F_a_field**: over Z, det[[2]] = 2 != 0 but [[2]] has no inverse with integer entries. The correct ring statement requires det to be a unit
- **exact_arithmetic**: in floating point, det A != 0 is not a usable invertibility test: a matrix with det = 10^{-300} may be perfectly well conditioned and one with det = 1 may be numerically singular. Use the condition number

## Common misuse
- testing numerical singularity by the determinant (see above) -- this is the single most common misuse of the determinant in computation
- applying it over a ring

## Related nodes (non-prerequisite)
- equivalent_to: invertibility_equivalences
- contrasts_with: condition_number

## Sources
hoffman_kunze_2e, higham_asna_2e
