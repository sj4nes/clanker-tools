# first_isomorphism_theorem

## Type
theorem

## Statement
For linear T: V -> W, the map v + ker T -> T(v) is a well-defined isomorphism V/ker T -> im T.

## Symbols
- `V/ker T` — the quotient by the kernel
- `im T` — the image in W

## Epistemic status
proved_theorem  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
image_subspace, kernel, linear_isomorphism, quotient_space

## Hypotheses
T linear

## Proof provenance
technique: well-definedness as above; injectivity because T(v) = 0 puts v in ker T, i.e. the coset is zero; surjectivity onto im T by construction
derives_from: quotient_space
lean_status: cited

## Well-definedness
Independence of the coset representative is exactly the definition of ker T, so the map is well-defined for EVERY linear T with no extra hypothesis.

## Type / well-formedness check
The type check is the WELL-DEFINEDNESS check: if v + ker T = v' + ker T then v - v' is in ker T so T(v) = T(v'). This is the canonical instance of well_defined_on_quotient.

## Specialization / boundary cases
- T injective: V/{0} isomorphic to V, so T is an isomorphism onto its image
- taking dimensions recovers rank_nullity via quotient_dimension -- the two theorems are the same fact, one counted and one structural

## Hypothesis-dropped counterexamples
- **linearity**: for a nonlinear map the fibres are not cosets of a subspace and there is no quotient to form
- **none_all_hypotheses_essential**: no finite-dimensionality is needed: this is the structural statement that SURVIVES in infinite dimension while its dimension-counting shadow (rank_nullity) does not

## Common misuse
- treating V/ker T as a subspace of V: see quotient_space

## Related nodes (non-prerequisite)
- equivalent_to: 
- required_by: 

## Sources
hoffman_kunze_2e, axler_lada_4e
