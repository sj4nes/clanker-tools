# invariant_subspace

## Type
definition

## Statement
U is T-invariant if T(U) is contained in U. Then T restricts to an operator T|_U on U, and m_{T|_U} divides m_T.

## Symbols
- `T|_U` — the restriction, type: element of L(U)

## Epistemic status
definition  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
linear_operator, minimal_polynomial, subspace

## Hypotheses
U a subspace with T(U) subset U

## Proof provenance
technique: divisibility because m_T(T) = 0 on all of V, hence on U
derives_from: minimal_polynomial
lean_status: cited

## Type / well-formedness check
Well-formed; the restriction is an OPERATOR on U (not merely a map into V) precisely because of invariance, which is what makes eigenvalue language applicable to it.

## Specialization / boundary cases
- {0} and V are always invariant
- every eigenspace E_lambda is invariant
- ker p(T) and im p(T) are invariant for any polynomial p, since they commute with T
- U^perp is T-invariant when U is and T is SELF-ADJOINT -- the induction step of spectral_theorem_symmetric

## Hypothesis-dropped counterexamples
- **invariance_of_the_complement**: for a general T, U invariant does NOT make a complement invariant: for J = [[1,1],[0,1]], the x-axis is invariant but no complementary line is. This is exactly why J fails to decompose and hence fails to diagonalise
- **self_adjointness_for_the_orthogonal_complement**: U^perp is T-invariant when U is only if T^* preserves... precisely, U T-invariant implies U^perp T^*-invariant. For self-adjoint T these coincide, which is the whole mechanism of the spectral theorem

## Common misuse
- assuming an invariant subspace has an invariant complement -- that is the semisimplicity assumption and it fails for defective operators

## Related nodes (non-prerequisite)
- required_by: schur_triangularisation, primary_decomposition, spectral_theorem_symmetric

## Sources
axler_lada_4e, hoffman_kunze_2e
