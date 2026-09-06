# structure

## Type
definition  (epistemic status: `definition`; `constructive_grade: n/a` —
depends on `naive_collection`)

## Statement
An **`ℒ`-structure** `𝔄` (model, interpretation) consists of:
- a **nonempty domain** (universe) `A = |𝔄|` — a `naive_collection`;
- for each constant symbol `c ∈ ℒ`: an element `c^𝔄 ∈ A`;
- for each `n`-ary function symbol `f ∈ ℒ`: a function `f^𝔄 : Aⁿ → A`;
- for each `n`-ary relation symbol `R ∈ ℒ`: a relation `R^𝔄 ⊆ Aⁿ`;
- equality is interpreted as identity on `A`
  (`first_order_logic_with_equality`).

## Symbols
- `𝔄`, `𝔅`: structures (fraktur); `A = |𝔄|`; `·^𝔄`: the interpretation map.

## Prerequisites (tsort edges into this node)
`naive_collection`, `signature`, `first_order_logic_with_equality`.

## Content
`ℒ` fixes syntax; `𝔄` supplies meaning. Every semantic notion is relative to
`𝔄`: `term_evaluation`, `tarski_satisfaction`, `model`, `validity`. This is the
propositional `truth_assignment` scaled up — a bit per atom becomes an
element/function/relation per symbol. **`metatheory: naive_collections`**: `A`
and the interpretations are set-theoretic objects the capsule does not build.

## Constructive grade
`n/a` — a structure is a `naive_collection`-level object; the classicality of
the semantic metatheorems sits in `lindenbaum_lemma_fol` / choice, not here.

## Lean status
`lean_status: cited`. Mathlib: `FirstOrder.Language.Structure` — a `Type`
domain + `funMap` / `RelMap` families. `validation/proof-checks.lean` is
propositional (no structures).

## Type / well-formedness check
`well_formed`. **Domain nonempty** (`objects.md`) — `∃x (x = x)` is valid here.
Every symbol of `ℒ` gets an interpretation of the **right arity**; `f^𝔄` is a
**total** function `Aⁿ → A`. A **reduct** `𝔄 ↾ ℒ₀` (forget interpretations of
`ℒ \ ℒ₀`) is an `ℒ₀`-structure; an **expansion** adds interpretations.

## Specialization / boundary cases
- `ℒ = ∅`: a structure is just a nonempty set.
- **one-element domain**: every `f^𝔄` is constant; the term model when a theory
  proves all closed terms equal.
- `(ℕ, 0, S, +, ·, <)` — the standard model of arithmetic; `(ℝ, +, ·, <)`;
  `(V, ∈)` — a model of set theory.
- **substructure** `𝔅 ⊆ 𝔄`: `|𝔅| ⊆ |𝔄|` closed under the functions, with
  restricted relations; **elementary** substructure `𝔅 ≼ 𝔄` if it agrees on all
  formulas with parameters (`lowenheim_skolem_down`).

## Hypothesis-dropped counterexamples
- **empty domain**: `∀x φ` vacuously true, `∃x φ` false — breaks quantifier
  duality and the standard axioms; free logic handles it, out of scope.
- **partial `f^𝔄`**: `term_evaluation` undefined somewhere.
- **`=` not identity**: `equality_congruence` fails, `term_model` breaks.
- **wrong arity interpretation**: satisfaction ill-defined.

## Common misuse
Allowing an empty domain; a partial function interpretation; forgetting a symbol
of `ℒ`; assuming a reduct of a model of `T` still models `T` (it need not, if
`T` mentions the forgotten symbols); confusing a structure (semantic) with a
theory (syntactic).

## Related nodes (non-prerequisite)
- `interprets`: `signature`.
- `depends_on`: `naive_collection`.
- `feeds`: `assignment`, `term_evaluation`, `tarski_satisfaction`, `model`.
- `propositional_shadow`: `truth_assignment`.
- `related`: substructure, elementary substructure, reduct, expansion.

## Sources
[enderton_logic_2e] §2.2; [chiswell_hodges] ch. 5; [hodges_shorter] §1.1.
