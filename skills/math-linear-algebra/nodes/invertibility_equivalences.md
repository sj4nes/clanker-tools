# invertibility_equivalences

## Type
theorem

## Statement
For square A in F^{n x n} the following are equivalent: A is invertible; rank A = n; null(A) = {0}; col(A) = F^n; rref(A) = I; A is a product of elementary matrices; det A != 0; 0 is not an eigenvalue of A; the columns are a basis of F^n; Ax = b has a unique solution for every b.

## Symbols
- `A` — a SQUARE matrix over a field

## Epistemic status
proved_theorem  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
char_poly_roots_are_eigenvalues, determinant_invertible_iff, elementary_matrix, invertible_matrix, matrix_rank, null_space, rank_nullity, rref_uniqueness

## Hypotheses
A square, F a field

## Proof provenance
technique: a cycle of implications: rank n => rref I (elimination) => product of elementaries => invertible => null trivial => rank n (rank_nullity); det A != 0 <=> invertible from determinant_invertible_iff; 0 not an eigenvalue <=> null trivial from the eigenvalue definition
derives_from: determinant_invertible_iff
lean_status: cited

## Type / well-formedness check
Well-formed for square A only. Each clause is proved where it is introduced; this node is the omnibus statement and therefore sits downstream of all of them -- which is why it takes an edge from char_poly_roots_are_eigenvalues.

## Specialization / boundary cases
- n = 1: [a] invertible iff a != 0 iff det != 0 iff 0 is not the eigenvalue a
- A diagonal: all clauses reduce to 'no zero on the diagonal'

## Hypothesis-dropped counterexamples
- **squareness**: for rectangular A the clauses split apart: full column rank gives injectivity and a left inverse only; full row rank gives surjectivity and a right inverse only; no clause gives two-sided invertibility
- **finite_dimensionality**: the operator analogue fails on F[t] -- see one_sided_inverse_square
- **F_a_field**: over Z, A = [[2]] has det 2 != 0 but no inverse IN Z. The clause 'det != 0 implies invertible' needs the determinant to be a UNIT, which over a field is automatic and over a ring is not

## Common misuse
- applying det != 0 as an invertibility test over a ring (see above)
- reading 'det A is small' as 'nearly singular' -- scaling A by c scales det by c^n while leaving the condition number unchanged

## Related nodes (non-prerequisite)
- equivalent_to: determinant_invertible_iff
- contrasts_with: condition_number

## Sources
strang_5e, hoffman_kunze_2e
