# signature

## Type
definition  (epistemic status: `definition`; `constructive_grade: intuitionistic`)

## Statement
A **signature** (first-order language, similarity type) `ℒ` is a set of
**non-logical symbols**, each with an **arity** (a metatheoretic natural
number):
- **constant symbols** `c, d, …` (arity 0);
- **function symbols** `f, g, …` of arity `≥ 1`;
- **relation (predicate) symbols** `R, S, …` of arity `≥ 1`.

The logical symbols (`¬ ∧ ∨ → ↔ ∀ ∃`, `=`, `(`, `)`, `,`, variables) are
**fixed** and not part of `ℒ`. Equality `=` is logical
(`first_order_logic_with_equality`).

## Symbols
- `ℒ`: the signature; `|ℒ|`: its cardinality (controls
  `lowenheim_skolem_down`).

## Prerequisites (tsort edges into this node)
`symbol`, `inductive_definition`, `metatheoretic_induction`.

## Content
`ℒ` fixes what can be *said*; a `structure` fixes what the symbols *mean*.
Examples: `ℒ_group = {·, e, ⁻¹}` (arities 2, 0, 1); `ℒ_order = {<}` (arity 2);
`ℒ_arith = {0, S, +, ·, <}`; `ℒ_ring`, `ℒ_ZFC = {∈}` (arity 2). Arities are
metatheoretic naturals — hence `metatheoretic_induction` as a prerequisite (to
recurse over argument lists).

## Constructive grade
`intuitionistic` — a set of symbols with a decidable arity function.

## Lean status
`lean_status: cited`. `validation/proof-checks.lean` is propositional (no
signature). Mathlib's `FirstOrder.Language` is a pair of arity-indexed symbol
families (`Functions : ℕ → Type`, `Relations : ℕ → Type`) — the reference model.

## Type / well-formedness check
`well_formed`. Each symbol has **exactly one** arity; the three classes
(constant/function/relation) are disjoint. `|ℒ| ≤ ℵ₀` is the **countable
language** assumption used by `lowenheim_skolem_down` and the choice-free
Lindenbaum; relaxed for `lowenheim_skolem_up`. A constant is a 0-ary function
(some treatments fold them together).

## Specialization / boundary cases
- `ℒ = ∅`: the language of **pure equality** — sentences can only count the
  domain ("there are exactly `n` elements", `∃`-`∀` with `=`).
- **relational** signature (no function/constant symbols): every substructure is
  a structure; the term model's domain is just constants.
- **expansions / reducts**: `ℒ ⊆ ℒ⁺` (add symbols); `henkin_constants` expands
  by witness constants.
- **many-sorted** signatures (sorts + typed symbols): a generalisation, out of
  scope; single-sorted here.

## Hypothesis-dropped counterexamples
- **a symbol with two arities**: `term_syntax` / `atomic_formula` formation is
  ambiguous.
- **`=` as non-logical** (in `ℒ`): then `=` need not be identity — "FOL without
  equality"; a legitimate variant, but this capsule fixes `=` logical.
- **uncountable `ℒ`**: no downward LS to `ℵ₀` in general; Lindenbaum needs choice.

## Common misuse
Putting `=` or the connectives in `ℒ`; forgetting arities; comparing formulas
across different signatures (`Γ ⊢ φ` needs one language); assuming a reduct of a
model is still a model of the full theory.

## Related nodes (non-prerequisite)
- `interpreted_by`: `structure`.
- `builds`: `term_syntax`, `atomic_formula`, `first_order_wff`.
- `expanded_by`: `henkin_constants` (witness constants), `equality_axioms`.
- `related`: many-sorted / typed signatures; `|ℒ|` in the LS cardinality bounds.

## Sources
[enderton_logic_2e] §2.1; [chiswell_hodges] ch. 5; [hodges_shorter] §1.1.
