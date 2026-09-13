# distinct_eigenvalues_independent

## Type
theorem

## Statement
Eigenvectors belonging to PAIRWISE DISTINCT eigenvalues are linearly independent. Consequently an operator on an n-dimensional space has at most n distinct eigenvalues.

## Symbols
- `k` — the number of distinct eigenvalues, at most dim V

## Epistemic status
proved_theorem  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
eigenvalue, induction_principle, linear_independence

## Hypotheses
the eigenvalues pairwise distinct

## Proof provenance
technique: induction on k: apply (T - lambda_k I) to a vanishing combination, killing the last term and scaling the others by (lambda_i - lambda_k) != 0; the inductive hypothesis forces the remaining coefficients to vanish
derives_from: linear_independence
lean_status: core — LinAlg.distinct_eig_indep_step (the induction step)

## Type / well-formedness check
Well-formed. Note it takes ONE eigenvector per eigenvalue; the stronger statement that the eigenSPACES form a direct sum follows and is used by diagonalisability_criterion.

## Specialization / boundary cases
- k = 2: two eigenvectors for distinct eigenvalues cannot be proportional, since a proportional pair would satisfy both eigen-equations
- k = n: n eigenvectors for n distinct eigenvalues form a basis, giving distinct_eigenvalues_diagonalisable

## Hypothesis-dropped counterexamples
- **distinctness**: two eigenvectors for the SAME eigenvalue can certainly be dependent -- any two elements of a one-dimensional eigenspace are
- **nonzero_eigenvectors**: the zero vector satisfies every eigen-equation and would make any list dependent

## Common misuse
- concluding an operator with fewer than n distinct eigenvalues is not diagonalisable: repeated eigenvalues are fine provided the geometric multiplicities are full (I_n has one eigenvalue and is diagonal)

## Related nodes (non-prerequisite)
- required_by: distinct_eigenvalues_diagonalisable, diagonalisability_criterion

## Sources
axler_lada_4e
