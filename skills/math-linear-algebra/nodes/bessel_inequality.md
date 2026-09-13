# bessel_inequality

## Type
proposition

## Statement
For any orthonormal set (e_1,...,e_k) and any v: sum_{i=1}^k |<v,e_i>|^2 <= ||v||^2.

## Symbols
- `<v,e_i>` — the i-th Fourier coefficient of v

## Epistemic status
proposition  ·  field_scope: real_or_complex

## Prerequisites (tsort edges into this node)
induced_norm, orthogonality, orthonormal_basis, pythagorean_theorem

## Hypotheses
(e_i) orthonormal

## Proof provenance
technique: write v = P v + (v - P v) with P the projection onto span(e_i); Pythagoras gives ||v||^2 = ||Pv||^2 + ||v - Pv||^2 >= ||Pv||^2 = sum |<v,e_i>|^2
derives_from: pythagorean_theorem
lean_status: cited

## Type / well-formedness check
Well-formed for any orthonormal set, whether or not it is a basis. This is the point: Bessel needs no completeness, Parseval does.

## Specialization / boundary cases
- k = 1: |<v,e>|^2 <= ||v||^2, which is Cauchy-Schwarz for a unit vector
- (e_i) a BASIS: equality, which is parseval_identity
- the deficit ||v||^2 - sum |<v,e_i>|^2 is exactly the squared distance from v to the span

## Hypothesis-dropped counterexamples
- **orthonormality**: for a general independent set the sum of squared coefficients can EXCEED ||v||^2 -- take two nearly-parallel unit vectors in R^2 and v along their common direction
- **equality_requires_a_basis**: an orthonormal set that misses a direction leaves a strictly positive deficit

## Common misuse
- assuming equality without checking that the orthonormal set spans

## Related nodes (non-prerequisite)
- required_by: parseval_identity

## Sources
axler_lada_4e
