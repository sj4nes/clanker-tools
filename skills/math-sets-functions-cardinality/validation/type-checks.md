# Type / well-formedness checks — headline nodes

Decided against `objects.md`. The traps this pass exists to catch: an unbounded
`{x : φ}` (proper class), an `⋂` over an empty family, a "function" that is not
total, a quantifier swap, and a use of choice that is not acknowledged.

## `quantifier_negation`
- `¬(∀x P) ⟺ ∃x ¬P` is stated over a domain; the `¬∀ → ∃¬` direction is
  **classical** (recorded — see `conventions.md`).
- The inner `¬P` must itself be pushed through: `¬(A⟹B) ⟺ A∧¬B`,
  `¬(∀ε∃δ…) ⟺ ∃ε∀δ¬…`. A stopped negation is the standing error (rule 6).
- **Status: well_formed.** Lean §5 checks both directions.

## `axiom_of_choice`
- Quantifies over an arbitrary indexed family `{A_i}`. The conclusion asserts a
  **function** `c` (total on `I`, `c(i) ∈ A_i`).
- A **definable** selector (least element of a well-order, the element of a
  singleton, a canonical representative) is *not* a use of AC — rule 7, recorded
  on the node and on every downstream result via `choice_grade`.
- **Status: well_formed.**

## `preimage_algebra`
- `f⁻¹[·]` is the **preimage operator**, total for every `f` (rule 3) — not the
  inverse function.
- `⋃_i`, `⋂_i` are over an index set `i ∈ I`; the intersection identity needs
  `I ≠ ∅` (rule 2) — recorded.
- **Status: well_formed.** Lean §1: the three identities are `rfl` when sets are
  predicates — genuine and universal.

## `image_algebra`
- `f[·]` is the image. `f[⋃] = ⋃f[·]` is an equality; `f[⋂] ⊆ ⋂f[·]` is only an
  inclusion — the type check flags that the reverse **fails** without
  injectivity (Lean §2: `img_inter_sub` proves only `→`).
- **Status: well_formed.**

## `equivalence_partition_correspondence`
- Forward: the classes `{[x]}` must be shown **nonempty** (`x ∈ [x]`),
  **pairwise disjoint** (`[x] ∩ [y] ≠ ∅ ⟹ [x] = [y]`), and **covering**. All
  three are genuine clauses (rule for `partition`).
- **Status: well_formed.** Lean §6: `cls_eq_iff` is the disjointness core.

## `well_defined_on_quotient`
- The rule `[x] ↦ h(x)` is a **function** only after `x∼x' ⟹ h(x)=h(x')` is
  discharged (rule 1). Stating "`f : X/∼ → Z` defined by …" without the check is
  ill-formed.
- **Status: well_formed.**

## `zorn_lemma` / `well_ordering_theorem`
- `zorn_lemma`: "every chain has an upper bound" — **every** chain, including
  the empty one (whose bound witnesses `P ≠ ∅`). The conclusion is **maximal**,
  not maximum (rule for `maximal_element`).
- `well_ordering_theorem`: the conclusion is `∃` a well-order — a total order
  with the least-element property. `uses_choice: true`, `choice_grade:
  needs_full_AC` — both edged to `axiom_of_choice`.
- **Status: well_formed.**

## `omega_construction` / `peano_holds_in_omega` / `recursion_theorem`
- `ω` is carved out of an Infinity-witness `I_0` by **Separation**
  (`ω = {x ∈ I_0 : ∀ inductive I, x ∈ I}`) — not a bare `{x : φ}` (rule 1).
- `peano_holds_in_omega`: `S` injective uses Foundation (`x ∉ x`); induction
  uses `ω` **minimal**. Both recorded.
- `recursion_theorem`: stated for an **arbitrary** target `A` — no arithmetic
  symbol appears (the recursion-vs-arithmetic cycle, `edges/cycles.md`).
- **Status: well_formed** (all three).

## `cantor_theorem` / `cantor_diagonal`
- The proof must **exhibit** the missing set `D = {x : x ∉ f(x)}` (rule 8) — a
  Separation instance bounded by `X`. `cantor_diagonal` gives the explicit
  flipped sequence `d(n) = 1 − s(n)(n)`.
- `cantor_diagonal` over `{0,1}` avoids the `0.999…` decimal ambiguity by
  construction (recorded).
- **Status: well_formed.** Lean §4: `cantor`, genuine, no Mathlib.

## `cantor_schroeder_bernstein`
- Inputs: two **injections**. Output: a **bijection**. The type check records
  that this is `choice_free` — a frequent misconception is that it needs AC
  (rule 7 / `choice_grade`).
- **Status: well_formed.**

## `countable_closure_properties`
- "countable" = injection into `ω`. The **countable-union** clause selects one
  enumeration per piece — `countable_choice`, edged. The other clauses (subset,
  image, finite product) are `choice_free`. `choice_grade:
  needs_countable_choice` with the note that a *given* enumeration removes the
  dependence.
- **Status: well_formed.**

## `continuum_hypothesis`
- `∄ κ, ℵ₀ < κ < 2^ℵ₀`. Well-formed as a statement. Its **status** is
  `independent_of_ZFC` — the one node that is neither proved nor an axiom
  (recorded prominently; the independence proofs are out of scope).
- **Status: well_formed.**

## Summary

All 14 headline nodes: **well_formed**. Recurring obligations forced into the
entries: (1) every `{x : φ}` is bounded or Replacement-justified; (2) `⋂` over a
family carries `I ≠ ∅`; (3) every "function" is total with a fixed codomain;
(4) every "∀…∃…" records whether the witness is uniform; (5) **every use of
choice is graded and edged** (`choice_free` / `needs_countable_choice` /
`needs_full_AC`), and CSB / Cantor / Hartogs / finite-pigeonhole are explicitly
flagged choice-free.
