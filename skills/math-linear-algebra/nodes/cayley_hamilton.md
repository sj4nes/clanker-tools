# cayley_hamilton

## Type
theorem

## Statement
Every square matrix satisfies its own characteristic polynomial: p_A(A) = 0. Consequently m_A divides p_A, and A^n is a combination of I, A, ..., A^{n-1}.

## Symbols
- `p_A(A)` — the polynomial p_A evaluated AT THE MATRIX A, type: element of F^{n x n}

## Epistemic status
proved_theorem  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
adjugate, characteristic_polynomial, linear_operator, polynomial_ring

## Hypotheses
A square

## Proof provenance
technique: the adjugate route: over F[t], adj(tI - A)(tI - A) = p_A(t) I. Write adj(tI - A) = sum_k B_k t^k with B_k in F^{n x n}, expand, match coefficients of each power of t, then multiply the k-th relation on the right by A^k and sum -- the left side telescopes to 0
derives_from: adjugate
lean_status: dim_core — LinAlg.cayley_hamilton_2 (n = 2)

## Type / well-formedness check
Well-formed, and the type check is the whole subtlety: p_A(t) = det(tI - A) is a scalar polynomial, and p_A(A) means substituting the MATRIX A for t, which is a different operation from evaluating the determinant at t = A. The pseudo-proof 'p_A(A) = det(AI - A) = det(0) = 0' is ill-typed nonsense -- det(AI - A) is a scalar, not a matrix.

## Specialization / boundary cases
- n = 1: p(t) = t - a and p(A) = A - aI = 0
- n = 2: A^2 - tr(A) A + det(A) I = 0 -- the identity used to compute A^{-1} = (tr(A) I - A)/det(A) and every 2x2 matrix power
- A diagonalisable: immediate, since p_A kills each eigenvector

## Hypothesis-dropped counterexamples
- **the_ill_typed_pseudo_proof**: 'substitute t = A into det(tI - A)' is not a proof: det(tI - A) is computed in F[t] with t a SCALAR indeterminate, and substituting a matrix for a scalar inside a determinant is undefined. The adjugate argument is needed precisely because the shortcut is invalid
- **squareness**: no characteristic polynomial otherwise

## Common misuse
- citing the pseudo-proof above
- concluding m_A = p_A: the theorem gives divisibility only

## In the wild
- reducing any polynomial in A to degree < n, which is how matrix functions (exp, powers) are computed for small n
- the basis of the Faddeev-LeVerrier algorithm for the characteristic polynomial and the inverse

## Related nodes (non-prerequisite)
- required_by: minimal_polynomial_diagonalisable

## Sources
hoffman_kunze_2e, horn_johnson_2e
