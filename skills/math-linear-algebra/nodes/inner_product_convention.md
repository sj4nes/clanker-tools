# inner_product_convention

## Type
notation_convention

## Statement
The complex inner product is LINEAR IN THE FIRST argument and conjugate-linear in the second: <ax, y> = a<x,y>, <x, ay> = conj(a)<x,y>, <y,x> = conj(<x,y>). The mathematician's convention (Axler, Hoffman-Kunze), NOT the physicist's.

## Symbols
- `<x,y>` — the inner product, type: V x V -> F with F in {R, C}

## Epistemic status
definition  ·  field_scope: real_or_complex

## Prerequisites (tsort edges into this node)
(root — cited, see conventions.md)

## Hypotheses
(none — unconditional within scope)
## Type / well-formedness check
A convention, but conjugate-symmetry is FORCED, not chosen: without it <x,x> need not be real and 'positive definite' is meaningless. What is conventional is only WHICH slot is conjugated.

## Specialization / boundary cases
- over R conjugation is the identity and the form is simply bilinear and symmetric
- the standard inner product on C^n under this convention is <x,y> = sum_i x_i conj(y_i) = y^* x

## Hypothesis-dropped counterexamples
- **conjugate_symmetry**: the plain bilinear form sum_i x_i y_i on C^n is NOT positive definite: x = (1, i) gives sum x_i^2 = 1 + (-1) = 0 with x != 0. Every norm, projection, and spectral result in the inner-product half of the capsule collapses without the conjugation

## Common misuse
- mixing this with the physicist's convention mid-proof, which swaps a with conj(a) and turns the adjoint identity <Tv,w> = <v,T^*w> into its conjugate
- reading <x,y> = y^* x as y^T x over C

## Sources
axler_lada_4e, hoffman_kunze_2e
