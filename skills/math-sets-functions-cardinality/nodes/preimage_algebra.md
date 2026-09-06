# preimage_algebra

## Type
theorem  (epistemic status: `proved_theorem`, `choice_free`)

## Statement
For **any** function `f : X → Y` and any family `{B_i}_{i∈I}` of subsets of `Y`:

    f⁻¹[⋃_i B_i] = ⋃_i f⁻¹[B_i]
    f⁻¹[⋂_i B_i] = ⋂_i f⁻¹[B_i]      (I ≠ ∅)
    f⁻¹[B^c]     = (f⁻¹[B])^c

## Symbols
- `f⁻¹[B] = { x ∈ X : f(x) ∈ B }` — the **preimage operator**, defined for
  every `f` (not the inverse function, which needs `f` bijective).

## Prerequisites (tsort edges into this node)
`preimage`, `indexed_union_intersection`, `relative_complement`,
`quantifier_negation`.

## Proof
Elementwise, and each step *is* a quantifier manipulation:

- `x ∈ f⁻¹[⋃_i B_i] ⟺ f(x) ∈ ⋃_i B_i ⟺ ∃i, f(x) ∈ B_i ⟺ ∃i, x ∈ f⁻¹[B_i]`.
- `x ∈ f⁻¹[⋂_i B_i] ⟺ ∀i, f(x) ∈ B_i ⟺ ∀i, x ∈ f⁻¹[B_i]`.
- `x ∈ f⁻¹[B^c] ⟺ f(x) ∉ B ⟺ ¬(x ∈ f⁻¹[B])` (`quantifier_negation` /
  double negation).

**Checked with Lean:** `validation/proof-checks.lean` §1 — `preim_iUnion`,
`preim_iInter`, `preim_compl` are `rfl` (genuine, universal) once a set is a
predicate `X → Prop` and `f⁻¹ B := fun x => B (f x)`.

## Why this node matters
It is the algebraic fact that **continuity and compactness proofs run on**:

- "`f` is continuous ⟺ the preimage of every open set is open" is well-posed
  *because* `f⁻¹` respects arbitrary unions and finite intersections (open sets
  are closed under exactly those).
- the compactness pullback — "pull an open cover of `f(K)` back through `f` to an
  open cover of `K`" — is this theorem plus continuity
  (`math-real-analysis` `continuous_image_of_compact`).
- `math-real-analysis`'s `intermediate_value_theorem` (topological route) and
  `continuous_image_of_connected` both use `f⁻¹` of a separation.

## Type / well-formedness check
`well_formed` (`validation/type-checks.md#preimage_algebra`). Recorded: `f⁻¹[·]`
is total for every `f`; the `⋂` identity carries `I ≠ ∅`.

## Contrast: the image does NOT behave this way
`f[⋃_i A_i] = ⋃_i f[A_i]` holds, but `f[⋂_i A_i] ⊆ ⋂_i f[A_i]` is only an
**inclusion**. Counterexample: `f(x) = x²`, `A = {−1}`, `B = {1}` ⇒
`f[A ∩ B] = f[∅] = ∅` while `f[A] ∩ f[B] = {1}`. Equality is restored iff `f` is
injective. (Lean §2: `img_union` is an equality; `img_inter_sub` proves only
`→`.)

## Specialization / boundary cases
- `f⁻¹[∅] = ∅`, `f⁻¹[Y] = X`.
- `f⁻¹[B ∖ C] = f⁻¹[B] ∖ f⁻¹[C]` (from union + complement).

## Common misuse
Assuming the image commutes with intersection; conflating the preimage operator
with the inverse function; forgetting `I ≠ ∅` for `⋂`.

## Related nodes (non-prerequisite)
- `contrasts_with`: `image_algebra`
- used by: `math-real-analysis` `continuity_at_point`,
  `continuous_image_of_compact`, the topological IVT route

## Sources
[munkres] §2; [enderton] ch. 3; [halmos] §§8–10.
