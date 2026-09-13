# linear_isomorphism

## Type
definition

## Statement
An isomorphism is a bijective linear map. Its set-theoretic inverse is AUTOMATICALLY linear, so 'isomorphism' needs no separate condition on the inverse.

## Symbols
- `T^{-1}` — the inverse map, type: linear map W -> V

## Epistemic status
definition  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
bijection, coordinate_isomorphism, linear_map

## Hypotheses
T linear and bijective

## Proof provenance
technique: apply T to both sides of the claimed linearity of T^{-1} and use injectivity
derives_from: bijection
lean_status: cited

## Type / well-formedness check
Well-formed. The automatic linearity of the inverse is genuine content: T^{-1}(aw_1 + bw_2) = T^{-1}(aT(v_1) + bT(v_2)) = T^{-1}(T(av_1 + bv_2)) = av_1 + bv_2.

## Specialization / boundary cases
- the coordinate map [.]_B is an isomorphism V -> F^n (coordinate_isomorphism)
- V isomorphic to W iff dim V = dim W, for finite-dimensional spaces over the same field

## Hypothesis-dropped counterexamples
- **bijectivity**: an injective non-surjective linear map has a left inverse but no two-sided one
- **linearity_of_T**: a nonlinear bijection has a nonlinear inverse, and none of the structure transfers

## Common misuse
- requiring separately that the inverse be linear -- it is free here, unlike for continuous maps (a continuous bijection need not have continuous inverse) or smooth maps

## Related nodes (non-prerequisite)
- required_by: invertible_operator, first_isomorphism_theorem

## Sources
axler_lada_4e
