# polarisation_identity

## Type
identity

## Statement
Over R: <u,v> = (||u+v||^2 - ||u-v||^2)/4. Over C: <u,v> = (1/4) sum_{k=0}^3 i^k ||u + i^k v||^2. The inner product is RECOVERABLE from the norm; the factor 1/4 is why characteristic 2 is excluded.

## Symbols
- `i^k` — the four fourth roots of unity, k = 0,1,2,3

## Epistemic status
mathematical_identity  ·  field_scope: char_not_2

## Prerequisites (tsort edges into this node)
characteristic_not_two, induced_norm, inner_product, parallelogram_law

## Hypotheses
char F != 2, F = R or C

## Proof provenance
technique: expand each squared norm and collect; over C the four terms isolate the real and imaginary parts of <u,v> separately
derives_from: parallelogram_law
lean_status: dim_core — LinAlg.polarisation_real (n = 2, stated as 4*<u,v> = ... so the char != 2 dependence is explicit)

## Type / well-formedness check
Well-formed over R and C. The division by 4 requires 2 to be invertible -- hence the characteristic_not_two edge. Over a field of characteristic 2 no polarisation exists and symmetric bilinear forms are not determined by their quadratic forms.

## Specialization / boundary cases
- u = v over R: (||2u||^2 - 0)/4 = ||u||^2, correct
- the real formula applied to a COMPLEX inner product recovers only Re<u,v>, which is why the complex version needs four terms

## Hypothesis-dropped counterexamples
- **characteristic_not_two**: over F_2 the map q(x) = x^T A x satisfies q(u+v) = q(u) + q(v) (all cross terms double to zero), so q is ADDITIVE and carries none of the bilinear information. Symmetric and alternating forms become indistinguishable -- the single sharpest consequence of char 2 in this capsule
- **using_the_real_formula_over_C**: gives Re<u,v> only, losing the imaginary part entirely

## Common misuse
- applying the real polarisation formula in a complex space
- symmetrising a matrix as (A + A^T)/2 over a field of characteristic 2

## Related nodes (non-prerequisite)
- required_by: isometry_characterisation, quadratic_form

## Sources
axler_lada_4e
