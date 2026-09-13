# trace

## Type
definition

## Statement
tr(A) = sum_{i=1}^n A_{ii} for square A. It is a LINEAR functional on F^{n x n}: tr(aA + bB) = a tr(A) + b tr(B).

## Symbols
- `tr(A)` — type: element of F

## Epistemic status
definition  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
field, index_convention, matrix

## Hypotheses
A square
## Type / well-formedness check
Well-formed for SQUARE A only. Linearity is immediate; what is not immediate is that it is similarity-invariant (trace_cyclic), which is what makes it an operator invariant.

## Specialization / boundary cases
- tr(I_n) = n -- which over F_p can be 0, a genuine trap in finite characteristic
- tr of a projection equals its rank (hat_matrix), the identity behind residual degrees of freedom

## Hypothesis-dropped counterexamples
- **squareness**: undefined otherwise
- **characteristic**: over F_p, tr(I_p) = p = 0, so 'the trace of a rank-r projection is r' must be read mod p

## Common misuse
- assuming tr(AB) = tr(A)tr(B): false in general (take A = B = I_2, giving 2 versus 4)

## Related nodes (non-prerequisite)
- required_by: trace_cyclic, char_poly_coefficients, matrix_norms

## Sources
hoffman_kunze_2e
