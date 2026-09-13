# diagonalisability_criterion

## Type
theorem

## Statement
T is diagonalisable if and only if p_T SPLITS over F and geom(lambda) = alg(lambda) for every eigenvalue; equivalently V is the DIRECT SUM of the eigenspaces; equivalently sum of the geometric multiplicities = dim V.

## Symbols
- `(+)` — direct sum over the distinct eigenvalues

## Epistemic status
proved_theorem  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
algebraic_geometric_multiplicity, diagonalisable, dimension_formula_sum, direct_sum, distinct_eigenvalues_diagonalisable, eigenspace

## Hypotheses
V finite-dimensional

## Proof provenance
technique: the eigenspaces for distinct eigenvalues form a direct sum by distinct_eigenvalues_independent; that sum is all of V iff the dimensions add to dim V, which by geom <= alg and sum alg = deg p_T = dim V (needs splitting) happens iff geom = alg throughout
derives_from: algebraic_geometric_multiplicity
lean_status: cited

## Type / well-formedness check
Well-formed. Two conditions, BOTH necessary: splitting (which fails for the real rotation) and multiplicity equality (which fails for the Jordan block). They are logically independent.

## Specialization / boundary cases
- n distinct eigenvalues: every alg = 1 forces geom = 1, so diagonalisable
- T = lambda I: one eigenvalue with alg = geom = n

## Hypothesis-dropped counterexamples
- **splitting**: [[0,-1],[1,0]] over R: geom = alg vacuously (no eigenvalues) but p_T does not split, and it is not diagonalisable. So the multiplicity condition alone is insufficient
- **multiplicity_equality**: [[1,1],[0,1]]: p splits completely, but geom(1) = 1 < 2 = alg(1). So splitting alone is insufficient. The two counterexamples together show the conditions are independent

## Common misuse
- checking only one of the two conditions
- assuming a matrix over C is diagonalisable because p always splits there -- splitting is automatic over C, the MULTIPLICITY condition is what can fail

## Related nodes (non-prerequisite)
- equivalent_to: minimal_polynomial_diagonalisable

## Sources
hoffman_kunze_2e, axler_lada_4e
