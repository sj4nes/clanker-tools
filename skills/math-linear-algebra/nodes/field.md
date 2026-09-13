# field

## Type
structure

## Statement
A field (F, +, *, 0, 1) is a commutative ring with 0 != 1 in which every nonzero element has a multiplicative inverse: (F,+) is an abelian group, (F\{0}, *) is an abelian group, and * distributes over +.

## Symbols
- `F` — the field, type: set with two binary operations
- `0, 1` — the additive and multiplicative identities, type: elements of F, required distinct
- `a^{-1}` — the multiplicative inverse of a != 0, type: element of F

## Epistemic status
definition  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
set

## Hypotheses
0 != 1 (excludes the zero ring)
## Type / well-formedness check
Well-formed. The exclusion of 0 from the multiplicative group is essential: 0 has no inverse in any ring with 0 != 1, since 0*x = 0 for all x.

## Specialization / boundary cases
- F = Q, R, C: the fields this capsule actually uses
- F = F_2 = {0,1}: the two-element field, where 1 + 1 = 0 -- the standing counterexample for every char_not_2 result
- F = F_p for p prime: finite fields, over which all the any_field results still hold

## Hypothesis-dropped counterexamples
- **existence_of_inverses**: Z is a commutative ring but not a field; over Z 'vector spaces' become modules, bases need not exist, and rank is replaced by invariant factors (smith_normal_form_boundary)
- **commutativity_of_multiplication**: over a division ring (the quaternions H) left and right vector spaces differ and the determinant theory breaks: det(AB) = det(A)det(B) has no direct analogue
- **zero_not_equal_one**: in the zero ring every module is trivial and dimension is meaningless

## Common misuse
- assuming char F = 0 -- half the hypothesis-dropped counterexamples in this capsule are at char 2
- assuming F is ordered: 'x^2 >= 0' is meaningless over C and false over F_p

## In the wild
- the scalars of every vector space in the capsule; coding theory and cryptography run the same linear algebra over F_2 and F_p
- F_2 linear algebra is the engine of linear block codes (Hamming, Reed-Muller) and of Gaussian elimination in SAT/XOR solvers

## Related nodes (non-prerequisite)
- generalizes: 

## Sources
hoffman_kunze_2e, dummit_foote_3e
