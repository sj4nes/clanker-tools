# rank_nullity

## Type
theorem

## Statement
For T: V -> W with V finite-dimensional: dim V = rank T + nullity T.

## Symbols
- `dim V` — dimension of the DOMAIN -- not of W

## Epistemic status
proved_theorem  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
basis_existence_finite, finite_dimensional, nullity, rank

## Hypotheses
V finite-dimensional, T linear

## Proof provenance
technique: take a basis of ker T, extend it to a basis of V; the images of the added vectors are a basis of im T -- spanning by linearity, independent because a vanishing combination of images puts a combination of the added vectors into ker T
derives_from: basis_existence_finite
lean_status: core — LinAlg.rank_nullity (the Nat identity the basis count concludes with)

## Type / well-formedness check
Well-formed; note the theorem constrains the DOMAIN's dimension, so nothing follows about W. This is the most-misquoted point about it.

## Specialization / boundary cases
- T injective: rank T = dim V, so im T is a copy of V inside W
- T = 0: rank 0, nullity dim V
- A in F^{m x n}: n = rank A + dim null(A), the count that drives gaussian_elimination's free-variable bookkeeping

## Hypothesis-dropped counterexamples
- **finite_dimensionality_of_V**: the right shift S on F^infinity (sequences) is injective with nullity 0 but NOT surjective; and the left shift is surjective with nullity 1. Neither satisfies any finite count. Rank-nullity is the canonical casualty of dropping finite_dimensional
- **linearity**: for a nonlinear map neither side is defined

## Common misuse
- quoting it as dim W = rank + nullity -- it is dim V
- concluding surjectivity from full rank without knowing dim W = dim V (that is injective_surjective_equivalence, which needs the extra hypothesis)

## In the wild
- the degrees-of-freedom count in every linear model: n observations, p parameters, n - rank(X) residual degrees of freedom
- the constraint count in linear programming and in structural mechanics (Maxwell's rule for determinacy)

## Related nodes (non-prerequisite)
- required_by: injective_surjective_equivalence, four_subspaces

## Sources
axler_lada_4e, hoffman_kunze_2e
