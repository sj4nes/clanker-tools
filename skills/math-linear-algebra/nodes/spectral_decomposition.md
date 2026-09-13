# spectral_decomposition

## Type
corollary

## Statement
A self-adjoint A equals sum_i lambda_i P_i over its DISTINCT eigenvalues, where P_i is the orthogonal projection onto E_{lambda_i}. The P_i are self-adjoint idempotents with P_iP_j = 0 for i != j and sum_i P_i = I. Consequently f(A) = sum_i f(lambda_i) P_i for any function f on the spectrum.

## Symbols
- `P_i` — the spectral projections
- `f(A)` — the functional calculus

## Epistemic status
corollary  ·  field_scope: real_or_complex

## Prerequisites (tsort edges into this node)
direct_sum, eigenspace, orthogonal_projection, projection_matrix_characterisation, spectral_theorem_symmetric

## Hypotheses
A self-adjoint, finite-dimensional

## Proof provenance
technique: group the columns of Q in spectral_theorem_symmetric by eigenvalue; P_i = Q_iQ_i^T for the corresponding block
derives_from: spectral_theorem_symmetric
lean_status: cited

## Type / well-formedness check
Well-formed; the sum is over DISTINCT eigenvalues, so the number of terms is at most n and typically fewer. The functional calculus f(A) is well-defined because the P_i are a resolution of the identity.

## Specialization / boundary cases
- A with distinct eigenvalues: each P_i is a rank-one projection q_iq_i^T
- f(t) = t^k: recovers A^k = sum lambda_i^k P_i
- f(t) = 1/t on an invertible A: A^{-1} = sum (1/lambda_i) P_i
- f(t) = e^t: the matrix exponential in closed form

## Hypothesis-dropped counterexamples
- **self_adjointness**: for a general diagonalisable A the spectral projections are OBLIQUE (P_i = v_iw_i^* with w the LEFT eigenvectors) and are not self-adjoint; the resolution of the identity still holds but the geometry is skewed. For a defective A no such decomposition exists at all
- **distinctness_of_the_lambda_i**: summing over eigenvalues WITH multiplicity would double-count the projections

## Common misuse
- using f(A) = sum f(lambda_i)P_i for a defective matrix
- computing the matrix exponential this way for a non-diagonalisable A

## In the wild
- the matrix functional calculus: exp(At) for linear ODEs, A^{1/2} for whitening, and the matrix square root used to standardise a multivariate normal
- Cochran's theorem in statistics is exactly the spectral resolution of I into orthogonal idempotents

## Related nodes (non-prerequisite)
- special_case_of: spectral_theorem_symmetric

## Sources
horn_johnson_2e
