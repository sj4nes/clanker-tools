# sylvester_law_of_inertia

## Type
theorem

## Statement
The numbers (n_+, n_-, n_0) of positive, negative, and zero eigenvalues of a real symmetric A -- its INERTIA -- are invariant under congruence. Two real quadratic forms are congruent iff they have the same inertia, so the signature is a COMPLETE invariant.

## Symbols
- `(n_+, n_-, n_0)` — the inertia
- `signature` — n_+ - n_-

## Epistemic status
proved_theorem  ·  field_scope: ordered_field

## Prerequisites (tsort edges into this node)
congruence, dimension_formula_sum, ordered_field_hyp, positive_definite, quadratic_form, spectral_theorem_symmetric

## Hypotheses
A real symmetric, F ordered

## Proof provenance
technique: the spectral theorem plus scaling gives the canonical form diag(I,-I,0), so every A is congruent to one. Invariance: if P^TAP = diag(I_{p},-I_{q},0) and also = diag(I_{p'},-I_{q'},0), a dimension count on the maximal subspace where the form is positive definite (which is congruence-invariant) forces p = p'
derives_from: congruence
lean_status: instance — LinAlg.congruence_not_similarity

## Type / well-formedness check
Well-formed over an ORDERED field (to classify signs). Over C every nondegenerate form is congruent to the identity, so the inertia carries no information -- the theorem is genuinely about real (or ordered-field) forms.

## Specialization / boundary cases
- A positive definite: inertia (n,0,0)
- A = diag(1,-1) and B = diag(4,-9): congruent (P = diag(2,3)) with the SAME inertia, though with completely different eigenvalues -- the sharpest illustration of similarity versus congruence
- the index n_- is the Morse index of a critical point

## Hypothesis-dropped counterexamples
- **the_ordered_field**: over C, diag(1,-1) = P^T I P with P = diag(1, i), so every nondegenerate complex symmetric form is congruent to I and the inertia is meaningless. Ordering is essential
- **eigenvalues_are_not_preserved**: only their SIGNS are, as the diag(4,-9) example shows. Quoting eigenvalues as form invariants is the standard error
- **symmetry**: no inertia is defined for a non-symmetric matrix

## Common misuse
- using eigenvalues rather than their signs to compare quadratic forms
- applying inertia over C

## In the wild
- the Morse index in optimisation and differential topology; the classification of conics and quadrics by signature
- the inertia of the KKT matrix is the standard test that an interior-point step is a descent direction

## Related nodes (non-prerequisite)
- contrasts_with: similar_invariants

## Sources
hoffman_kunze_2e, horn_johnson_2e
