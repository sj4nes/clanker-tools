# congruence

## Type
definition

## Statement
A ~_c B if B = P^T A P for some invertible P. This is the transformation law of QUADRATIC FORMS under a change of variables x = Py, and it is DIFFERENT from similarity (P^{-1}AP) unless P is orthogonal.

## Symbols
- `~_c` — congruence, type: equivalence relation on symmetric matrices

## Epistemic status
definition  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
equivalence_relation, invertible_matrix, quadratic_form, transpose

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: equivalence-relation axioms; the change-of-variables reading by substituting x = Py into x^TAx
derives_from: quadratic_form
lean_status: instance — LinAlg.congruence_not_similarity

## Type / well-formedness check
Well-formed as an equivalence relation (reflexive with P = I, symmetric via P^{-1}, transitive by composition) and it preserves symmetry: (P^TAP)^T = P^TA^TP = P^TAP.

## Specialization / boundary cases
- P orthogonal: congruence and similarity COINCIDE, which is exactly why spectral_theorem_symmetric can be read either way
- P diagonal with entries 1/sqrt(|lambda_i|): brings a diagonalised form to a matrix of +-1s and 0s, the canonical form of sylvester_law_of_inertia

## Hypothesis-dropped counterexamples
- **congruence_is_not_similarity**: A = I_2 and B = diag(4,9) = P^T I P with P = diag(2,3) are CONGRUENT but not SIMILAR -- their eigenvalues differ entirely. So eigenvalues are NOT congruence invariants; only their SIGNS are (sylvester_law_of_inertia). Using similarity invariants (trace, determinant, eigenvalues) to compare quadratic forms is the standard error
- **invertibility_of_P**: a singular P can only degrade the form and gives no equivalence relation

## Common misuse
- quoting eigenvalues as invariants of a quadratic form
- diagonalising a quadratic form by similarity when the change of variables is not orthogonal

## Related nodes (non-prerequisite)
- contrasts_with: similarity
- required_by: sylvester_law_of_inertia, simultaneous_diagonalisation

## Sources
hoffman_kunze_2e, horn_johnson_2e
