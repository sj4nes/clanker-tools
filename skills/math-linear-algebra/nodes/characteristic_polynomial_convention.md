# characteristic_polynomial_convention

## Type
notation_convention

## Statement
p_A(t) = det(tI - A), which is MONIC of degree n. The common variant det(A - tI) equals (-1)^n p_A(t): same roots, opposite sign when n is odd, and a different constant term.

## Symbols
- `p_A` — the characteristic polynomial, type: monic element of F[t] of degree n
- `t` — the indeterminate, type: element of F[t]

## Epistemic status
definition  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
(root — cited, see conventions.md)

## Hypotheses
(none — unconditional within scope)
## Type / well-formedness check
A convention. Monicity is what makes 'the' characteristic polynomial a definite description and makes the coefficient identities (char_poly_coefficients) hold with the signs stated.

## Specialization / boundary cases
- n = 1: p_A(t) = t - A_{11} under this convention, versus A_{11} - t under the other
- n = 2: p_A(t) = t^2 - tr(A) t + det(A), the form used throughout the capsule's 2x2 instance checks

## Hypothesis-dropped counterexamples
- **none_all_hypotheses_essential**: a convention; the failure mode is a sign error. Under det(A - tI) the constant term is det(A), not (-1)^n det(A), and quoting char_poly_coefficients across conventions produces wrong signs for odd n

## Common misuse
- quoting 'the constant term is det A' without saying which convention -- true for det(A - tI), off by (-1)^n for det(tI - A)

## Sources
hoffman_kunze_2e, horn_johnson_2e
