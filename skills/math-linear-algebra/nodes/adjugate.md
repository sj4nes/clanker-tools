# adjugate

## Type
construction

## Statement
adj(A)_{ij} = C_{ji} = (-1)^{i+j} M_{ji} (the TRANSPOSED cofactor matrix). Then A adj(A) = adj(A) A = det(A) I, so A^{-1} = adj(A)/det(A) whenever det A != 0.

## Symbols
- `adj(A)` — the adjugate (classical adjoint), type: element of F^{n x n}

## Epistemic status
constructive_result  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
determinant_invertible_iff, invertible_matrix, laplace_expansion

## Hypotheses
A square

## Proof provenance
technique: the (i,i) entry of A adj(A) is the Laplace expansion along row i; an off-diagonal entry is the expansion of a matrix with two equal rows, hence 0
derives_from: laplace_expansion
lean_status: dim_core — LinAlg.adjugate_identity (n = 2, singular X included)

## Type / well-formedness check
Well-formed. The TRANSPOSE in the definition is essential and is the usual slip. Note the identity A adj(A) = det(A) I holds for EVERY square A, including singular ones -- no invertibility is assumed.

## Specialization / boundary cases
- n = 2: adj([[a,b],[c,d]]) = [[d,-b],[-c,a]], the familiar swap-and-negate rule
- A singular: A adj(A) = 0, and adj(A) has rank at most 1 when rank A = n-1
- over Z: adj(A) has INTEGER entries, so A^{-1} is integral exactly when det A = +-1 -- the ring statement determinant_invertible_iff needs

## Hypothesis-dropped counterexamples
- **the_transpose**: omitting it gives the cofactor matrix, for which the identity is false already at n = 2 unless the matrix is symmetric
- **cost**: computing A^{-1} via the adjugate costs O(n!) or at best O(n^4); elimination costs O(n^3)

## Common misuse
- using the adjugate formula as a numerical inverse
- confusing adj(A) (classical adjoint) with A^* (the Hermitian adjoint) -- unrelated objects sharing an unfortunate name

## In the wild
- Cramer's rule and the integrality criterion above; the adjugate is also how cayley_hamilton is proved in this release

## Related nodes (non-prerequisite)
- required_by: cramers_rule, cayley_hamilton

## Sources
hoffman_kunze_2e
