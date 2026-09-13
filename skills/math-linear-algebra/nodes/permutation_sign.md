# permutation_sign

## Type
definition

## Statement
S_n is the group of bijections of {1..n}. Every permutation is a product of transpositions, and the PARITY of the number of transpositions is well-defined; sgn: S_n -> {+1,-1} is the resulting group homomorphism.

## Symbols
- `S_n` — the symmetric group, type: group of order n!
- `sgn` — type: group homomorphism S_n -> {+1,-1}

## Epistemic status
definition  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
bijection, finite_set

## Hypotheses
n finite

## Proof provenance
technique: inversion-count argument; the homomorphism property then follows by concatenating decompositions
derives_from: bijection
lean_status: cited

## Well-definedness
Parity is independent of the decomposition because each transposition changes the inversion count by an odd number. Without this, 'sgn' would not be a function and the Leibniz formula would be meaningless.

## Type / well-formedness check
The type check IS the well-definedness check: a permutation has many decompositions into transpositions, and the claim is that their parities agree. Proved by tracking the number of inversions, which changes parity under each transposition.

## Specialization / boundary cases
- n = 2: S_2 = {id, swap} with signs +1 and -1
- a cycle of length k has sign (-1)^{k-1}
- over a field of characteristic 2, +1 = -1 and sgn is trivial -- which is why the determinant over F_2 is the PERMANENT

## Hypothesis-dropped counterexamples
- **well_definedness_of_parity**: if parity were decomposition-dependent, sgn would not exist and the alternating condition could not be expressed
- **characteristic_two**: over F_2 the alternating condition 'D = 0 when two columns are equal' is strictly stronger than 'D changes sign under a swap', because -1 = 1 makes the latter vacuous. This is why multilinear_alternating_form is defined by the VANISHING condition, not the sign-change condition

## Common misuse
- defining alternating as 'antisymmetric' (sign-changing) -- equivalent only when char F != 2

## Related nodes (non-prerequisite)
- required_by: determinant_existence_uniqueness, leibniz_formula

## Sources
hoffman_kunze_2e, dummit_foote_3e
