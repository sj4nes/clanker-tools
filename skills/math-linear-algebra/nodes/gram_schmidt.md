# gram_schmidt

## Type
algorithm

## Statement
Given an independent list (v_1,...,v_k), define e_j recursively as (v_j - P_{span(e_1..e_{j-1})} v_j) normalised. The result is orthonormal with span(e_1..e_j) = span(v_1..v_j) for every j. Hence EVERY finite-dimensional inner product space has an orthonormal basis.

## Symbols
- `w_j` — the un-normalised residual
- `e_j` — the j-th orthonormal vector

## Epistemic status
constructive_result  ·  field_scope: real_or_complex

## Prerequisites (tsort edges into this node)
induction_principle, linear_independence, orthogonal_projection, orthonormal_basis, span

## Hypotheses
(v_i) linearly independent

## Proof provenance
technique: induction on j: orthogonality of e_j to earlier e_i by construction (the residual of a projection is orthogonal to the subspace); the span equality because each e_j is a combination of v_1..v_j with nonzero v_j-coefficient and conversely
derives_from: orthogonal_projection
lean_status: cited

## Type / well-formedness check
Well-formed: w_j != 0 at every step BECAUSE the v's are independent (v_j is not in the span of the earlier ones), so the division by ||w_j|| is legitimate. Independence is exactly the non-degeneracy condition the algorithm needs.

## Specialization / boundary cases
- k = 1: e_1 = v_1/||v_1||
- the v's already orthogonal: Gram-Schmidt only normalises
- recording the coefficients gives exactly qr_factorisation, with R upper triangular because e_j uses only v_1..v_j

## Hypothesis-dropped counterexamples
- **independence**: applied to a dependent list, some w_j = 0 and the normalisation divides by zero. The MODIFIED algorithm skips such j and produces an orthonormal basis of the span -- but the span-matching property is then lost for that index
- **numerical_stability**: CLASSICAL Gram-Schmidt loses orthogonality catastrophically in floating point; MODIFIED Gram-Schmidt (subtract projections one at a time, updating as you go) is far better, and Householder reflections better still. This is a numerical-analysis fact, CITED, not established here

## Common misuse
- implementing classical Gram-Schmidt for an ill-conditioned matrix and trusting the resulting Q to be orthogonal
- applying it to a dependent list without handling the zero residual

## In the wild
- QR factorisation and hence the standard least-squares solver; the construction of orthogonal polynomial families (Legendre, Hermite) by Gram-Schmidt on 1, t, t^2, ... in an L^2 inner product

## Related nodes (non-prerequisite)
- required_by: qr_factorisation, orthogonal_decomposition, schur_triangularisation, singular_value_decomposition

## Sources
axler_lada_4e, trefethen_bau
