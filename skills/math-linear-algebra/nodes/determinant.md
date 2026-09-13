# determinant

## Type
definition

## Statement
det: F^{n x n} -> F is THE unique normalised alternating multilinear function of the columns. Defined with no reference to eigenvalues (edges/cycles.md, cycle 1) and with no reference to minors, so rank stays determinant-free (cycle 3).

## Symbols
- `det A` — type: element of F
- `|A|` — alternative notation, avoided here to prevent confusion with norms

## Epistemic status
definition  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
determinant_existence_uniqueness, multilinear_alternating_form

## Hypotheses
A square
## Type / well-formedness check
Well-formed as a definite description ONLY because determinant_existence_uniqueness precedes it.

## Specialization / boundary cases
- n = 1: det[a] = a
- n = 2: det = ad - bc
- n = 3: the six-term Sarrus expansion -- valid ONLY for n = 3 and not a general pattern

## Hypothesis-dropped counterexamples
- **squareness**: there is no determinant of a rectangular matrix; the nearest analogues are the Gram determinant det(A^TA) and the singular values
- **commutativity_of_F**: over a noncommutative division ring no function with these properties exists (the Dieudonne determinant lands in an abelianisation instead)

## Common misuse
- extending Sarrus' rule to n >= 4, where it is simply wrong
- reading det as a measure of how invertible A is: det != 0 is a yes/no test, and magnitude is not conditioning (condition_number)

## In the wild
- the Jacobian determinant as the local volume-change factor in the change-of-variables formula
- the normalising constant of the multivariate normal density involves det(Sigma)

## Related nodes (non-prerequisite)
- required_by: leibniz_formula, determinant_multiplicative, characteristic_polynomial

## Sources
hoffman_kunze_2e, axler_lada_4e
