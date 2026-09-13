# conjugate_transpose

## Type
definition

## Statement
(A^*)_{ij} = conj(A_{ji}), the Hermitian adjoint. Over R it equals A^T. It satisfies (AB)^* = B^* A^*, (A^*)^* = A, and (aA)^* = conj(a) A^*.

## Symbols
- `A^*` — type: element of C^{n x m}
- `conj` — complex conjugation

## Epistemic status
definition  ·  field_scope: real_or_complex

## Prerequisites (tsort edges into this node)
complex_number, transpose, transpose_convention

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: entrywise, combining transpose with the ring homomorphism property of conjugation
derives_from: transpose
lean_status: cited

## Type / well-formedness check
Well-formed. Note A -> A^* is conjugate-linear, not linear -- the scalar comes out conjugated, so A^* is not a linear function of A over C.

## Specialization / boundary cases
- A real: A^* = A^T, which is why the whole statistics-facing half of the capsule can be written with T
- A^*A is always positive SEMIdefinite with (A^*A)^* = A^*A -- the fact singular_values rests on

## Hypothesis-dropped counterexamples
- **conjugation**: with A = [[1, i]] (1x2), A^T A = [[1, i],[i, -1]] has determinant 0 and is singular, while A^* A = [[1, -i],[i, 1]] is positive semidefinite of rank 1. Dropping the conjugate destroys positive semidefiniteness, hence the SVD and every least-squares argument over C

## Common misuse
- defining Hermitian as A^T = A over C: that is complex-symmetric, a genuinely different and far worse-behaved class (complex symmetric matrices need not be diagonalisable)

## Related nodes (non-prerequisite)
- required_by: adjoint_operator, self_adjoint, singular_values

## Sources
horn_johnson_2e
