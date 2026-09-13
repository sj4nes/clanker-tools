# distinct_eigenvalues_diagonalisable

## Type
corollary

## Statement
If A in F^{n x n} has n DISTINCT eigenvalues in F then A is diagonalisable. SUFFICIENT, NOT NECESSARY.

## Symbols
- `n` — the size, equal to the number of distinct eigenvalues

## Epistemic status
corollary  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
diagonalisable, dimension, distinct_eigenvalues_independent

## Hypotheses
n distinct eigenvalues, all in F

## Proof provenance
technique: the n eigenvectors are independent by distinct_eigenvalues_independent, hence a basis by the dimension count
derives_from: distinct_eigenvalues_independent
lean_status: cited

## Type / well-formedness check
Well-formed. Note the eigenvalues must lie IN F: n distinct complex eigenvalues do not diagonalise a real matrix over R.

## Specialization / boundary cases
- n = 2 with tr^2 != 4 det over R: two distinct real roots, so diagonalisable
- generic matrices have distinct eigenvalues, which is why diagonalisability is 'typical' -- but not robust, since the defective matrices are exactly where numerical eigenvector computation becomes ill-conditioned

## Hypothesis-dropped counterexamples
- **necessity_fails**: I_n has one eigenvalue repeated n times and is diagonal. The converse is false and assuming it is the standard error
- **eigenvalues_in_F**: [[0,-1],[1,0]] has two distinct eigenvalues +-i, but not in R, and it is not diagonalisable over R

## Common misuse
- concluding non-diagonalisability from repeated eigenvalues

## Sources
axler_lada_4e
