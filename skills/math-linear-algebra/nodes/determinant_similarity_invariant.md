# determinant_similarity_invariant

## Type
corollary

## Statement
det(P^{-1}AP) = det(A). The determinant depends only on the operator, not on the basis, and is therefore a similarity invariant.

## Symbols
- `P` — invertible

## Epistemic status
corollary  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
determinant_invertible_iff, determinant_multiplicative, similarity

## Hypotheses
P invertible

## Proof provenance
technique: multiplicativity: det(P^{-1})det(A)det(P) = det(A) since det(P^{-1}) = 1/det(P) and F is commutative
derives_from: determinant_multiplicative
lean_status: cited

## Type / well-formedness check
Well-formed. This is what licenses defining det(T) for an OPERATOR T, by taking the determinant of its matrix in any basis.

## Specialization / boundary cases
- P orthogonal: det(P) = +-1, so det is also a CONGRUENCE invariant in that special case
- but for general congruence det(P^TAP) = det(P)^2 det(A), which is NOT invariant -- only its SIGN is (see sylvester_law_of_inertia)

## Hypothesis-dropped counterexamples
- **similarity_versus_congruence**: under congruence the determinant scales by det(P)^2 > 0 over R. So congruence preserves the SIGN of det but not its value -- which is exactly the one-dimensional shadow of Sylvester's law

## Common misuse
- assuming det is a congruence invariant

## Related nodes (non-prerequisite)
- required_by: characteristic_polynomial, similar_invariants

## Sources
hoffman_kunze_2e
