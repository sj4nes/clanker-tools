# induction_equivalence

## Type
proved_theorem  (epistemic status: `proved_theorem`; `constructive_grade:
needs_DNE` for the well-ordering leg with arbitrary predicates, `intuitionistic`
for the weak ⟺ strong core; **headline** of the proof-methods block)

## Statement
Over `ℕ` (with `0`, successor, `<`, and the other Peano axioms), the three
principles

    weak_induction   ⟺   strong_induction   ⟺   well_ordering_principle

are pairwise equivalent: each is derivable from any other. Taking any one as the
axiom yields the same theorems.

## Symbols
- `P`: an arbitrary predicate on `ℕ`.
- the carrier: `(ℕ, 0, S, <)` with `S` injective and `0` not a successor.

## Prerequisites (tsort edges into this node)
`weak_induction`, `strong_induction`, `well_ordering_principle`.

## Proof
- **weak → strong**: apply `weak_induction` to `Q(n) := ∀k < n, P(k)`.
  (`strong_of_weak` in `validation/proof-checks.lean`.)
- **strong → well-ordering**: contrapositive — if `S ⊆ ℕ` has no least element,
  strong-induct to get `∀n, n ∉ S`, so `S = ∅`. (`well_ordering` in the Lean
  file.)
- **well-ordering → weak**: given `P(0)` and `∀n (P(n) → P(n+1))`, suppose `P`
  fails somewhere; `{n : ¬P(n)}` is nonempty, take its least `m`; `m ≠ 0` (base),
  so `m − 1` exists with `P(m−1)`, hence `P(m)` (step) — contradiction.

## Constructive grade
- weak ⟺ strong: **`intuitionistic`** — both from `Nat`-recursion, zero axioms
  (`#print axioms strong_of_weak`).
- the legs involving `well_ordering_principle` for **arbitrary** `P` use
  `proof_by_contradiction`: **`needs_DNE`**. For **decidable** `P` all three are
  intuitionistically equivalent.

## Lean status
`lean_status: core`. `strong_of_weak` and `well_ordering` in
`validation/proof-checks.lean` give two of the three implications as genuine
plain-Lean proofs; the third (well-ordering → weak) is the same
least-counterexample argument. `#print axioms strong_of_weak` → none;
`well_ordering` pulls `Classical`.

## Type / well-formedness check
`well_formed`. The equivalence is stated **relative to the Peano structure** —
`S` injective, `0` not a successor, `<` the associated well-founded order. Drop
those and the principles come apart (see below). "Over `ℕ`" is doing real work.

## Specialization / boundary cases
- **decidable `P`**: all three intuitionistically equivalent; the least element
  is computable (`Nat.find`).
- **structural induction** on any inductive type: the weak-induction analogue;
  well-foundedness of the subterm order is the well-ordering analogue.
- **transfinite**: on the ordinals, "every nonempty class has a least element"
  ⟺ transfinite induction (`math-sets-functions-cardinality`).

## Hypothesis-dropped counterexamples
- **drop `S` injective / `0` not a successor** (e.g. `ℤ/6ℤ` with `+1` as
  "successor"): weak induction from `0` still reaches every element, but
  `well_ordering_principle` **fails** — the cyclic order has no least element.
  The principles are no longer equivalent.
- **carrier `ℤ`** (no least element): `well_ordering_principle` fails outright;
  "downward" induction also fails; only a two-way induction schema survives.
- **carrier `ℚ≥0` under `<`** (dense, no immediate successor): the "`m − 1`
  exists" step of well-ordering → weak has no analogue; weak induction is not
  even statable.
- **arbitrary `P`, constructive metatheory**: well-ordering → weak needs
  `proof_by_contradiction`; without `DNE` the equivalence with the well-ordering
  principle breaks (weak ⟺ strong survives).

## Common misuse
Assuming `strong_induction` is strictly stronger (it proves exactly the same
theorems); using `well_ordering_principle` on non-well-founded carriers by
analogy; forgetting the equivalence is Peano-structure-relative; treating the
decidable and arbitrary-`P` cases as the same constructively.

## Related nodes (non-prerequisite)
- `equivalent_to` (the content): `weak_induction`, `strong_induction`,
  `well_ordering_principle`.
- `generalised_by`: well-founded induction; `transfinite_induction`
  (`math-sets-functions-cardinality`).
- `underpins`: every inductive proof in the capsule stack.

## Sources
[velleman_3e] §6.4; [enderton_logic_2e] §3.3; [hammack_bop] ch. 10.
