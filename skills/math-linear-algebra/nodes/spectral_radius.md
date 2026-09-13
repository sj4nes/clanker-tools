# spectral_radius

## Type
definition

## Statement
rho(A) = max_i |lambda_i| over the eigenvalues of A. It satisfies rho(A) <= ||A|| for EVERY submultiplicative norm, with equality for NORMAL A in the spectral norm, and Gelfand's formula rho(A) = lim_k ||A^k||^{1/k}.

## Symbols
- `rho(A)` — type: nonnegative real

## Epistemic status
definition  ·  field_scope: real_or_complex

## Prerequisites (tsort edges into this node)
eigenvalue, matrix_norms, normal_matrix

## Hypotheses
eigenvalues taken over C

## Proof provenance
technique: rho <= ||A|| because ||Av|| = |lambda| ||v|| for an eigenvector; equality for normal A from spectral_theorem_normal, since the singular values are then the |lambda_i|. Gelfand's formula is CITED
derives_from: matrix_norms
lean_status: cited

## Type / well-formedness check
Well-formed over an algebraically closed field (or by passing to C for a real matrix). Note rho is NOT a norm: it vanishes on nonzero nilpotent matrices and is not subadditive.

## Specialization / boundary cases
- A normal: rho(A) = ||A||_2
- A^k -> 0 if and only if rho(A) < 1 -- the fundamental stability criterion for linear iterations and discrete dynamical systems
- A a stochastic matrix: rho(A) = 1, attained at the stationary distribution

## Hypothesis-dropped counterexamples
- **rho_is_not_a_norm**: the nilpotent [[0,1],[0,0]] has rho = 0 while A != 0, so rho(A) = 0 does not imply A = 0. It also fails subadditivity: rho(A+B) can exceed rho(A) + rho(B)
- **rho_does_not_bound_finite_powers**: with J = [[1,1],[0,1]], rho(J) = 1 but ||J^k||_2 grows LINEARLY in k. rho governs only the ASYMPTOTIC growth rate (Gelfand), not any individual power. Transient growth before eventual decay is a real and often decisive phenomenon in non-normal dynamics
- **normality_for_equality**: for non-normal A the gap ||A||_2 - rho(A) can be arbitrarily large

## Common misuse
- concluding from rho(A) < 1 that ||A^k|| decreases monotonically -- it can grow substantially first (transient growth), which matters in fluid stability and in iterative solver convergence
- using rho as a norm in a perturbation bound

## In the wild
- convergence of stationary iterative methods (Jacobi, Gauss-Seidel) is exactly rho of the iteration matrix being < 1; stability of discrete linear dynamical systems and of Markov chain mixing

## Related nodes (non-prerequisite)
- contrasts_with: matrix_norms

## Sources
horn_johnson_2e, trefethen_bau
