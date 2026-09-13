# characteristic_not_two

## Type
hypothesis

## Statement
char F != 2, i.e. 1 + 1 != 0 in F. Required wherever a factor of 1/2 is taken, and wherever a symmetric bilinear form must be recoverable from its quadratic form.

## Symbols
- `char F` — the characteristic: the least n > 0 with n*1 = 0, or 0 if none

## Epistemic status
definition  ·  field_scope: char_not_2

## Prerequisites (tsort edges into this node)
field

## Hypotheses
(none — unconditional within scope)
## Type / well-formedness check
Well-formed for any field. Note char F is either 0 or a prime.

## Specialization / boundary cases
- F = Q, R, C all have characteristic 0, so every char_not_2 result applies unconditionally there
- F = F_3: 1 + 1 = 2 != 0, so the hypothesis holds over odd finite fields too

## Hypothesis-dropped counterexamples
- **char_not_2**: over F_2 the polarisation identity fails: the map q(x) = x^T A x determines A only up to adding an alternating matrix, since q(x+y) - q(x) - q(y) = 2 x^T A y = 0. Symmetric and alternating forms cease to be distinguishable, and quadratic_form's uniqueness of the symmetric representative is false

## Common misuse
- writing (A + A^T)/2 to symmetrise a matrix without checking the characteristic

## Related nodes (non-prerequisite)
- required_by: polarisation_identity, quadratic_form

## Sources
hoffman_kunze_2e, lang_algebra_3e
