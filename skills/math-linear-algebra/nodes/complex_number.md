# complex_number

## Type
bridge

## Statement
C = R[i] with i^2 = -1: a field of characteristic 0 carrying the conjugation a + bi -> a - bi, with |z|^2 = z conj(z) >= 0. Cited: NO capsule in this stack constructs C.

## Symbols
- `C` — the complex field, type: field of characteristic 0
- `conj(z)` — complex conjugation, type: field automorphism C -> C fixing R
- `|z|` — modulus, type: function C -> R_{>=0}

## Epistemic status
proved_theorem

## Prerequisites (tsort edges into this node)
(root — cited, see conventions.md)

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: cited from math-number-systems (R) plus the standard quadratic extension; the extension itself is NOT developed in this stack
lean_status: cited

## Type / well-formedness check
Cited. Well-formed as a quotient of the polynomial ring R[t] by the maximal ideal (t^2 + 1); the quotient is a field because that polynomial is irreducible over R.

## Specialization / boundary cases
- restricting conjugation to R gives the identity, which is why every real result is the b = 0 case of its complex counterpart

## Hypothesis-dropped counterexamples
- **positive_definiteness_of_the_form**: over C the bilinear form sum z_i w_i is NOT positive definite (take z = (1, i): sum z_i^2 = 0 with z != 0). This is exactly why the complex inner product must conjugate one slot -- see inner_product_convention

## Common misuse
- treating C as an ordered field -- it admits no order compatible with its arithmetic, which is why positive_definite is tagged ordered_field and stated over R

## Sources
hoffman_kunze_2e
