# well_ordering_principle

## Type
theorem  (epistemic status: `proved_theorem`; `constructive_grade: needs_DNE`
for arbitrary predicates, `intuitionistic` for decidable ones; equivalent to
`weak_induction`)

## Statement
Every nonempty subset `S ⊆ ℕ` has a least element: `∃m ∈ S, ∀k ∈ S, m ≤ k`.
Equivalently, for every predicate `P` with a witness, there is a least `n` with
`P(n)`.

## Symbols
- `S`: a nonempty set of natural numbers (or `P : ℕ → Prop` with `∃n, P(n)`).
- `m`: the least element.

## Prerequisites (tsort edges into this node)
`weak_induction`, `metatheoretic_induction`.

## Content / proof
From `strong_induction` (contrapositive): if `S` had **no** least element, then
by strong induction `∀n, n ∉ S` (if every `k < n` is outside `S`, then `n` must
be too — else `n` would be least), so `S = ∅`, contradiction. This is
`well_ordering` in `validation/proof-checks.lean`. It is the "least
counterexample" / **infinite descent** engine.

## Constructive grade
- `S` **decidable** (the usual case — a set of naturals cut out by a decidable
  property): `intuitionistic`, the least element is found by bounded search
  (`bc validation/instance-checks.bc`, least `n` with `n² > 30`).
- `S` an **arbitrary** predicate: `needs_DNE` — the proof above uses
  `proof_by_contradiction`, and `well_ordering` in the Lean file goes through
  `Classical.byContradiction`.

## Lean status
`lean_status: core`. `well_ordering` derives it from `strong_of_weak`; core also
has `Nat.find` (for decidable `P` with a witness) which computes the least
element.

## Type / well-formedness check
`well_formed`. **Nonemptiness is essential** — `∅` has no least element and the
statement would be false. The order must be the standard `≤` on `ℕ` (a
well-order); the principle is *about* that order.

## Specialization / boundary cases
- `S` finite: has a least (and a greatest) element — provable without the full
  principle.
- `S = ℕ`: least element `0`.
- **infinite descent** (Fermat): to show no `n` has property `P`, show that any
  `n` with `P(n)` yields a strictly smaller `n' < n` with `P(n')` — impossible
  in a well-order.
- lifted to ordinals: every nonempty class of ordinals has a least element
  (`math-sets-functions-cardinality`, `ordinal`).

## Where it fails
- **`S = ∅`**: no least element; the "nonempty" hypothesis cannot be dropped.
- **`ℤ`, `ℚ`, `ℝ` under `<`**: not well-ordered — `ℤ` has no least element,
  `{q ∈ ℚ : q > 0}` has no least element, `(0,1) ⊆ ℝ` has no least element.
  Well-ordering these needs the Axiom of Choice
  (`math-sets-functions-cardinality`, `well_ordering_theorem`) and the resulting
  order is not `<`.
- **a set with no *decidable* membership** but classically nonempty: the least
  element exists but is not computable.

## Common misuse
Applying it to subsets of `ℚ` or `ℝ` "ordered as usual"; forgetting
nonemptiness; confusing this theorem (about `ℕ`, provable) with the
**well-ordering theorem** (every set can be well-ordered, needs AC); using it to
extract a *computable* least element from a non-decidable set.

## Related nodes (non-prerequisite)
- `equivalent_to`: `weak_induction`, `strong_induction` (`induction_equivalence`).
- `commonly_confused_with`: `well_ordering_theorem` (AC, `math-sets-...`).
- `enables`: infinite descent, the division algorithm, `induction_equivalence`.

## Sources
[velleman_3e] §6.4; [hammack_bop] ch. 10; [enderton_logic_2e] §3.3.
