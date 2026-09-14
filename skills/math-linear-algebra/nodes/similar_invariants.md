# similar_invariants

## Type
proposition

## Statement
Similar matrices share rank, trace, determinant, characteristic polynomial, minimal polynomial, and every eigenvalue multiplicity. NONE of these, nor all together short of the Jordan data, is a COMPLETE invariant.

## Symbols
- `~` — similarity

## Epistemic status
proposition  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
characteristic_polynomial, determinant_similarity_invariant, matrix_rank, minimal_polynomial, non_diagonalisable_counterexample, rank_inequalities, similarity, trace_cyclic

## Hypotheses
A ~ B

## Proof provenance
technique: rank because multiplication by invertibles preserves it (rank_inequalities); trace by trace_cyclic; determinant and characteristic polynomial by determinant_similarity_invariant; minimal polynomial because p(P^{-1}AP) = P^{-1}p(A)P
derives_from: similarity
lean_status: instance — LinAlg.charpoly_not_complete_invariant

## Type / well-formedness check
Well-formed. The proposition is a list of necessary conditions; its value is as much in the failure of sufficiency as in the invariances.

## Specialization / boundary cases
- A diagonalisable: the eigenvalue multiset IS complete among diagonalisable matrices
- p and m together are complete for n <= 3, but not for n >= 4

## Hypothesis-dropped counterexamples
- **completeness_fails_for_p_alone**: I_2 and [[1,1],[0,1]] share p(t) = (t-1)^2 and are not similar (they have different ranks of A - I)
- **completeness_fails_for_p_and_m_together_at_n_equals_4**: diag(J_2(0), J_2(0)) and diag(J_2(0), 0, 0) both have p = t^4 and m = t^2, yet have different numbers of blocks (2 versus 3) and hence different ranks -- they are not similar. This is the standard witness that p and m do not suffice
- **these_are_not_congruence_invariants**: trace and determinant are NOT preserved by congruence; only the inertia is (sylvester_law_of_inertia)

## Common misuse
- concluding similarity from equal characteristic polynomials
- using these invariants to compare matrices related by congruence rather than similarity

## Related nodes (non-prerequisite)
- contrasts_with: congruence

## Sources
horn_johnson_2e
