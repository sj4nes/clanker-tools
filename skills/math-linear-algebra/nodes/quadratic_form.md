# quadratic_form

## Type
definition

## Statement
q(x) = x^T A x with A symmetric. When char F != 2 the symmetric A representing a given q is UNIQUE, and the associated bilinear form is recovered by polarisation: b(x,y) = (q(x+y) - q(x) - q(y))/2.

## Symbols
- `q` — type: function F^n -> F, homogeneous of degree 2
- `A` — the symmetric representing matrix

## Epistemic status
definition  ·  field_scope: char_not_2

## Prerequisites (tsort edges into this node)
characteristic_not_two, matrix, self_adjoint, transpose

## Hypotheses
A symmetric, char F != 2 for uniqueness

## Proof provenance
technique: x^TAx = x^T A^T x since both are 1x1, so x^TAx = x^T((A+A^T)/2)x; uniqueness by polarisation
derives_from: characteristic_not_two
lean_status: cited

## Type / well-formedness check
Well-formed. Uniqueness of the SYMMETRIC representative is the substantive claim: any A gives a form, but x^TAx = x^T((A+A^T)/2)x, so only the symmetric part matters -- and forming (A+A^T)/2 divides by 2.

## Specialization / boundary cases
- n = 1: q(x) = ax^2
- A = I: q(x) = ||x||^2
- the second-order term of a Taylor expansion, with A the Hessian -- symmetric by equality of mixed partials

## Hypothesis-dropped counterexamples
- **characteristic_not_two**: over F_2, q(x) = x_1x_2 comes from A = [[0,1],[0,0]] and from A = [[0,0],[1,0]] and from [[0,1],[1,0]] -- the symmetric representative is not unique, and worse, the polarisation b(x,y) = 2x^TAy = 0 vanishes identically. Quadratic forms in characteristic 2 are a genuinely separate theory
- **symmetry**: without restricting to symmetric A the representation is never unique in any characteristic

## Common misuse
- symmetrising as (A + A^T)/2 without checking the characteristic
- confusing the quadratic form's transformation law (congruence, P^TAP) with an operator's (similarity, P^{-1}AP) -- see congruence

## In the wild
- the second-derivative test in optimisation: the Hessian's definiteness classifies critical points
- variance of a linear combination: Var(a^TX) = a^T Sigma a is a quadratic form, PSD because Sigma is

## Related nodes (non-prerequisite)
- required_by: congruence, positive_definite, sylvester_law_of_inertia, courant_fischer

## Sources
hoffman_kunze_2e, horn_johnson_2e
