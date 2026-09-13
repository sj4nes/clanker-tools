# algebraic_geometric_multiplicity

## Type
definition

## Statement
The ALGEBRAIC multiplicity of lambda is its multiplicity as a root of p_A; the GEOMETRIC multiplicity is dim E_lambda. Always 1 <= geometric <= algebraic, and the gap is exactly the obstruction to diagonalisability.

## Symbols
- `alg(lambda), geom(lambda)` — type: positive integers

## Epistemic status
definition  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
char_poly_roots_are_eigenvalues, characteristic_polynomial, dimension, eigenspace

## Hypotheses
lambda an eigenvalue of A

## Proof provenance
technique: extend a basis of E_lambda to a basis of V; in that basis A is block triangular with lambda I_g in the top-left block, so (t - lambda)^g divides p_A
derives_from: characteristic_polynomial
lean_status: core — LinAlg.geom_le_alg

## Type / well-formedness check
Well-formed. The inequality is the substantive content and requires proof; that geom >= 1 is just the definition of an eigenvalue.

## Specialization / boundary cases
- A diagonalisable: geom = alg for every eigenvalue (diagonalisability_criterion)
- A = [[1,1],[0,1]]: alg(1) = 2, geom(1) = 1 -- the minimal defective example
- lambda a SIMPLE root (alg = 1): then geom = 1 forced, so simple eigenvalues never cause defectiveness

## Hypothesis-dropped counterexamples
- **the_inequality_is_strict_in_general**: the Jordan block above; the deficiency alg - geom counts the number of Jordan blocks beyond the first
- **the_reverse_inequality_is_false**: geom > alg never happens, but assuming geom = alg is exactly the diagonalisability assumption

## Common misuse
- counting eigenvalues 'with multiplicity' without saying WHICH multiplicity -- p_A uses algebraic, eigenspace dimensions use geometric
- assuming a repeated eigenvalue means non-diagonalisable

## Related nodes (non-prerequisite)
- contrasts_with: diagonalisability_criterion
- required_by: generalised_eigenspace

## Sources
horn_johnson_2e, hoffman_kunze_2e
