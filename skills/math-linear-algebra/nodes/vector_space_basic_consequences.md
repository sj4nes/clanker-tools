# vector_space_basic_consequences

## Type
proposition

## Statement
In any vector space: 0v = 0, a0 = 0, (-1)v = -v, and av = 0 implies a = 0 or v = 0.

## Symbols
- `0` — context-dependent: the zero scalar on the left of 0v, the zero vector elsewhere

## Epistemic status
proposition  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
vector_space

## Hypotheses
V a vector space over a field F

## Proof provenance
technique: 0v = (0+0)v = 0v + 0v, then cancel in the abelian group; for the last clause, if a != 0 multiply by a^{-1}
derives_from: vector_space
lean_status: core — LinAlg.smul_zero_eq_zero, LinAlg.zero_smul_vec, LinAlg.neg_one_smul, LinAlg.no_zero_smul_divisors

## Type / well-formedness check
Well-formed. The last clause is the 'no zero divisors' statement and is exactly where the FIELD structure (invertibility of nonzero a) is used, not merely the ring axioms.

## Specialization / boundary cases
- in F^n these are the componentwise facts, but the proof uses only the axioms and so holds in every V

## Hypothesis-dropped counterexamples
- **invertibility_of_nonzero_scalars**: over the ring Z/6 as a module over itself, 2*3 = 0 with neither factor zero -- the no-zero-divisors clause genuinely needs F to be a field

## Common misuse
- treating 0v = 0 as an axiom: it is a consequence, and deriving it is the standard check that an axiom list is not redundant

## Sources
axler_lada_4e
