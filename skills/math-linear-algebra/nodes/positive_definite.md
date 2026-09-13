# positive_definite

## Type
definition

## Statement
A real SYMMETRIC A is positive definite (A > 0) if x^T A x > 0 for every x != 0, and positive SEMIdefinite (A >= 0) if x^TAx >= 0 for all x. Negative (semi)definite by reversing; INDEFINITE otherwise.

## Symbols
- `A > 0, A >= 0` — the Loewner ordering notation; A >= B means A - B >= 0

## Epistemic status
definition  ·  field_scope: ordered_field

## Prerequisites (tsort edges into this node)
ordered_field_hyp, quadratic_form, real_number, self_adjoint

## Hypotheses
A symmetric, F ordered (F = R here)
## Type / well-formedness check
Well-formed only over an ORDERED field (to say '> 0') and conventionally only for SYMMETRIC A (so that x^TAx captures all of A -- see quadratic_form). Both restrictions are why the node carries edges to ordered_field_hyp and self_adjoint.

## Specialization / boundary cases
- A = I: positive definite
- A = 0: positive semidefinite but not definite
- any Gram matrix is PSD, and definite iff the vectors are independent (gram_matrix)
- a covariance matrix is PSD, and definite iff no linear combination of the variables is degenerate

## Hypothesis-dropped counterexamples
- **symmetry**: for a NON-symmetric A the condition x^TAx > 0 depends only on (A+A^T)/2, so it cannot characterise A. [[1,-3],[3,1]] satisfies x^TAx = ||x||^2 > 0 yet has complex eigenvalues -- 'positive definite' in the eigenvalue sense fails while the quadratic-form condition holds. The two notions agree ONLY for symmetric A, which is why symmetry is built into the definition
- **the_ordered_field**: over C, x^TAx is complex; the Hermitian form x^*Ax is real exactly when A is Hermitian, and that is the correct complex definition
- **definite_versus_semidefinite**: diag(1,0) is PSD, singular, and NOT positive definite -- the distinction is exactly invertibility

## Common misuse
- calling a non-symmetric matrix positive definite without saying which sense
- assuming positive entries means positive definite: [[1,2],[2,1]] has all positive entries and eigenvalues 3, -1 -- INDEFINITE. Conversely [[2,-1],[-1,2]] has negative entries and is positive definite

## In the wild
- covariance matrices, Hessians at a minimum, kernel matrices in SVMs and Gaussian processes, and the mass and stiffness matrices of a stable structure
- the Fisher information matrix in math-statistics is PSD, which is what makes the Cramer-Rao bound meaningful

## Related nodes (non-prerequisite)
- required_by: psd_characterisations, cholesky_factorisation, gram_matrix, singular_values

## Sources
horn_johnson_2e, boyd_vandenberghe
