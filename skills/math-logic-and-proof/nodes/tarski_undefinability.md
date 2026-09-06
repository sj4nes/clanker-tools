# tarski_undefinability

## Type
theorem  (epistemic status: **`stated_not_proved`**; `constructive_grade: n/a`)

## Statement
**Arithmetical truth is not arithmetically definable.** There is no formula
`True(x)` in the language of arithmetic such that, for every sentence `σ`,

    ℕ ⊨ ( True(⌜σ⌝) ↔ σ ).

More generally: no sufficiently expressive, consistent theory can contain its
own truth predicate (Tarski 1933/1936).

## Symbols
- `True(x)`: a candidate truth predicate; `⌜σ⌝`: the Gödel number of `σ`.
- `ℕ`: the standard model of arithmetic.

## Prerequisites (tsort edges into this node)
`godel_incompleteness_first`, `tarski_satisfaction`.

## Proof (sketch — not in scope)
The **diagonal lemma** (shared with `godel_incompleteness_first`): for any
formula `ψ(x)` there is a sentence `λ` with `ℕ ⊨ (λ ↔ ψ(⌜λ⌝))`. Apply it to
`ψ(x) := ¬True(x)`: get `λ` with `ℕ ⊨ (λ ↔ ¬True(⌜λ⌝))`. But the truth schema
gives `ℕ ⊨ (True(⌜λ⌝) ↔ λ)`. Combining: `ℕ ⊨ (λ ↔ ¬λ)` — contradiction. So no
such `True` exists. (This is the **Liar paradox**, made rigorous.)

## Constructive grade
`n/a` — a negative result. The proof is effective (diagonalisation).

## Lean status
`lean_status: none`. Shares the diagonal-lemma machinery with
`godel_incompleteness_first`; out of scope to build.

## Type / well-formedness check
`well_formed`. "Arithmetically definable" = definable by a first-order formula in
the language of arithmetic, interpreted in `ℕ`. The result is about **truth**
(the semantic notion, `tarski_satisfaction` at `ℕ`); it does **not** say
truth is *incomprehensible* — only not capturable *within the same language*.

## Specialization / boundary cases
- **provability IS definable**: `Prov_T(x)` is a `Σ₁` arithmetical formula —
  the asymmetry that drives `godel_incompleteness_first` (provability is
  definable and, being weaker than truth, misses the Gödel sentence).
- **partial truth predicates**: for each `n`, `Σₙ`-truth *is* `Σₙ`-definable —
  the hierarchy of partial truth predicates (Tarski's own construction, going up
  a level).
- **a metalanguage** strictly stronger than the object language *can* define the
  object language's truth (`ℕ`-truth is definable in second-order arithmetic /
  in set theory).
- **Kripke's theory of truth**, revision theories, `KF` — attempts at
  self-applicable truth by weakening classical logic or the `T`-schema; out of
  scope.

## Relation to the boundary block
- **Tarski undefinability ⟹ Gödel I** (semantic version): if all theorems of a
  consistent, recursively axiomatised, sound arithmetic theory `T` were exactly
  the true sentences, then truth would be r.e., hence (with its complement, by
  completeness/consistency) decidable and definable — contradicting
  undefinability. So `T` is incomplete.
- both rest on the **diagonal lemma**.

## Hypothesis-dropped counterexamples / limits
- **restrict to `Σₙ`**: `Σₙ`-truth is definable (partial truth predicates).
- **move to a stronger metalanguage**: `ℕ`-truth is definable there.
- **weaken the `T`-schema or the logic**: self-applicable truth becomes possible
  (Kripke, `KF`) — at a cost.

## Common misuse
Reading it as "mathematical truth is unknowable" or "undefinable in any sense" —
it is undefinable *in the object language*; a stronger metalanguage suffices.
Confusing truth (undefinable) with provability (definable). Ignoring the partial
truth predicates.

## Related nodes (non-prerequisite)
- `shares_machinery_with`: `godel_incompleteness_first` (the diagonal lemma).
- `contrast`: provability is arithmetically definable (`Σ₁`).
- `related`: the Liar paradox, partial truth predicates, Kripke's theory of
  truth, revision theory.

## Sources
[bbj_5e] ch. 17; [smith_godel_2e]; Tarski (1933/1936); [enderton_logic_2e] §3.5.
