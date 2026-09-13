# cramers_rule

## Type
corollary

## Statement
For invertible A, the unique solution of Ax = b is x_i = det(A_i)/det(A), where A_i is A with its i-th COLUMN replaced by b.

## Symbols
- `A_i` — the modified matrix, type: element of F^{n x n}

## Epistemic status
corollary  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
adjugate, determinant_invertible_iff, linear_system

## Hypotheses
A square and invertible

## Proof provenance
technique: x = A^{-1}b = adj(A)b/det(A); the i-th entry of adj(A)b is the Laplace expansion of det(A_i)
derives_from: adjugate
lean_status: cited

## Type / well-formedness check
Well-formed when det A != 0. Note the substitution is into a COLUMN, matching the column-multilinearity of det.

## Specialization / boundary cases
- n = 2: x_1 = (b_1 d - b_2 b)/det, the two-equation formula from school algebra
- over Z with det A = +-1: the solution is automatically integral

## Hypothesis-dropped counterexamples
- **invertibility**: for singular A the formula divides by zero; a consistent singular system has infinitely many solutions and Cramer says nothing about them
- **cost**: n+1 determinants, so O(n * n^3) at best against O(n^3) for elimination -- Cramer is exponentially worse if the determinants are computed by expansion

## Common misuse
- using it to solve systems of any real size
- applying it to an underdetermined or inconsistent system

## In the wild
- still useful for SYMBOLIC 2x2 and 3x3 solves, and for proving that solutions depend rationally (hence smoothly) on the entries -- the implicit function theorem's linear core

## Related nodes (non-prerequisite)
- historically_precedes: gaussian_elimination

## Sources
hoffman_kunze_2e
