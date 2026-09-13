# non_diagonalisable_counterexample

## Type
counterexample

## Statement
J = [[1,1],[0,1]] has p_J(t) = (t-1)^2, so alg(1) = 2, but ker(J - I) is spanned by e_1 alone, so geom(1) = 1. J is NOT diagonalisable over any field. Its minimal polynomial is (t-1)^2, not (t-1).

## Symbols
- `J` — the 2x2 Jordan block for eigenvalue 1

## Epistemic status
counterexample  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
algebraic_geometric_multiplicity, characteristic_polynomial, diagonalisable

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: direct computation of ker(J - I) and of p_J
derives_from: algebraic_geometric_multiplicity
lean_status: instance — LinAlg.jordan_block_defective

## Type / well-formedness check
Well-formed over any field; the entries 0 and 1 make it a counterexample even in characteristic 2.

## Specialization / boundary cases
- J^k = [[1,k],[0,1]], which grows LINEARLY even though the only eigenvalue has modulus 1 -- the practical consequence of defectiveness
- J is similar to no diagonal matrix, though it shares its characteristic polynomial with I_2

## Hypothesis-dropped counterexamples
- **none_all_hypotheses_essential**: this IS the counterexample node. It witnesses: the converse of distinct_eigenvalues_diagonalisable, the multiplicity clause of diagonalisability_criterion, the incompleteness of p_A as a similarity invariant, and the necessity of (t-lambda) appearing to the first power in minimal_polynomial_diagonalisable

## Common misuse
- assuming |eigenvalues| <= 1 bounds ||A^k||: J shows it does not. The correct statement involves the spectral radius only ASYMPTOTICALLY (spectral_radius)

## Related nodes (non-prerequisite)
- illustrated_by: 

## Sources
horn_johnson_2e
