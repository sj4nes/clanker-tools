# injective_iff_trivial_kernel

## Type
proposition

## Statement
A linear map T is injective if and only if ker T = {0}.

## Symbols
- `{0}` — the zero subspace of V

## Epistemic status
proposition  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
kernel, linear_map

## Hypotheses
T linear

## Proof provenance
technique: T(u) = T(v) iff T(u - v) = 0 iff u - v in ker T
derives_from: linear_map
lean_status: cited

## Type / well-formedness check
Well-formed. The reduction of a global condition (injectivity, a statement about all pairs) to a local one (a single subspace being trivial) is available ONLY for linear maps, and it is what makes injectivity computable by elimination.

## Specialization / boundary cases
- V = F^n: T injective iff Ax = 0 has only the trivial solution iff A has full column rank

## Hypothesis-dropped counterexamples
- **linearity**: for nonlinear f, f^{-1}(0) = {0} does not give injectivity: x -> x^2 on R has only 0 in its zero set but is not injective

## Common misuse
- applying the criterion to an affine map x -> Ax + b: injectivity is still governed by ker A, but the 'zero set' is not the kernel

## Related nodes (non-prerequisite)
- required_by: injective_surjective_equivalence

## Sources
axler_lada_4e
