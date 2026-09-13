# self_adjoint_real_eigenvalues

## Type
proposition

## Statement
Every eigenvalue of a self-adjoint operator is REAL, and eigenvectors for distinct eigenvalues are ORTHOGONAL. (For a real symmetric matrix this means the complex eigenvalues guaranteed by FTA are in fact real.)

## Symbols
- `lambda` — an eigenvalue, a priori complex

## Epistemic status
proposition  ·  field_scope: real_or_complex

## Prerequisites (tsort edges into this node)
eigenvalue, inner_product, orthogonality, self_adjoint

## Hypotheses
T self-adjoint

## Proof provenance
technique: lambda <v,v> = <Tv,v> = <v,Tv> = conj(lambda)<v,v>, and <v,v> != 0 forces lambda = conj(lambda). Orthogonality: lambda<v,w> = <Tv,w> = <v,Tw> = conj(mu)<v,w> = mu<v,w> using realness, so (lambda - mu)<v,w> = 0
derives_from: self_adjoint
lean_status: dim_core — LinAlg.symmetric_discriminant_nonneg (n = 2: the discriminant is a sum of squares) with LinAlg.rotation_discriminant_negative as the dropped-hypothesis witness

## Type / well-formedness check
Well-formed. For a REAL symmetric matrix one must first pass to C to know an eigenvalue exists (eigenvalue_existence_closed over C); the proposition then says it is real. That two-step structure is why the real spectral theorem is not a triviality.

## Specialization / boundary cases
- A = [[a,b],[b,d]] real symmetric: discriminant (a-d)^2 + 4b^2 >= 0 always, so both roots are real -- the 2x2 case verified directly
- a covariance matrix has real (indeed nonnegative) eigenvalues, which is why PCA's variances are meaningful numbers

## Hypothesis-dropped counterexamples
- **self_adjointness**: [[0,-1],[1,0]] is real but NOT symmetric, and its eigenvalues +-i are not real. Symmetry, not realness of the entries, is what forces real eigenvalues
- **over_C_transpose_is_not_enough**: the complex-symmetric [[1,i],[i,-1]] has A^T = A but eigenvalues both 0 with a defective eigenspace -- it is nilpotent. Hermitian (A^* = A) is the correct hypothesis

## Common misuse
- assuming a real matrix has real eigenvalues
- using A^T = A as the criterion over C

## In the wild
- the real-valuedness of PCA variances, of the natural frequencies of a conservative mechanical system, and of quantum-mechanical observables

## Related nodes (non-prerequisite)
- required_by: spectral_theorem_symmetric

## Sources
axler_lada_4e, horn_johnson_2e
