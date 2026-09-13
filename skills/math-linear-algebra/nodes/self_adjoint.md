# self_adjoint

## Type
definition

## Statement
T is self-adjoint (Hermitian) if T = T^*; over R this reads A = A^T (symmetric). Equivalently <Tv,w> = <v,Tw> for all v, w, and over C equivalently <Tv,v> is REAL for every v.

## Symbols
- `T^*` — the adjoint

## Epistemic status
definition  ·  field_scope: real_or_complex

## Prerequisites (tsort edges into this node)
adjoint_operator, conjugate_transpose, transpose_convention

## Hypotheses
T in L(V), V an inner product space

## Proof provenance
technique: the equivalences from the defining property of the adjoint; the complex real-form criterion by polarisation
derives_from: adjoint_operator
lean_status: cited

## Type / well-formedness check
Well-formed for an OPERATOR (T^* has the same domain and codomain only then). The 'real quadratic form' characterisation is a COMPLEX phenomenon: over R, <Tv,v> is automatically real for every T, so that criterion is vacuous there.

## Specialization / boundary cases
- orthogonal projections are self-adjoint (projection_matrix_characterisation)
- covariance matrices and Gram matrices are real symmetric
- a real DIAGONAL matrix is self-adjoint

## Hypothesis-dropped counterexamples
- **the_complex_criterion_is_complex_only**: over R, <Av,v> is real for EVERY A, so it cannot detect symmetry. Indeed [[0,-1],[1,0]] has <Av,v> = 0 for all v and is not symmetric. Over C the criterion is genuinely equivalent -- an asymmetry worth remembering
- **complex_symmetric_is_not_Hermitian**: A^T = A over C is a different, badly behaved class: [[1,i],[i,-1]] is complex symmetric, has p(t) = t^2, and is NILPOTENT -- nothing like a Hermitian matrix

## Common misuse
- defining Hermitian as A^T = A over C
- using the 'real quadratic form' test over R, where it is vacuous

## Related nodes (non-prerequisite)
- required_by: spectral_theorem_symmetric, positive_definite, normal_matrix, rayleigh_quotient

## Sources
axler_lada_4e, horn_johnson_2e
