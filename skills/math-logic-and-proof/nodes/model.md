# model

## Type
definition  (epistemic status: `definition`; `constructive_grade: n/a`)

## Statement
A structure `𝔄` is a **model** of a sentence `σ` if `𝔄 ⊨ σ`; a model of a set of
sentences `Γ` (a theory) if `𝔄 ⊨ σ` for every `σ ∈ Γ`. `Mod(Γ)` is the **class**
of all models of `Γ`.

## Symbols
- `𝔄 ⊨ Γ`: `𝔄` models `Γ`; `Mod(Γ)`: the (proper) class of models.

## Prerequisites (tsort edges into this node)
`sentence`, `tarski_satisfaction`, `structure`.

## Content
The bridge from a **theory** (syntax) to its **semantics**. `T` is
**satisfiable** iff `Mod(T) ≠ ∅`; `T ⊨ φ` iff `Mod(T) ⊆ Mod({φ})`
(`semantic_consequence_fol`); `T` **complete** iff all its models are
elementarily equivalent. `godel_completeness_theorem` (model-existence form):
`T` consistent ⟹ `Mod(T) ≠ ∅`.

## Constructive grade
`n/a` — `Mod(Γ)` is a `naive_collection` (a proper class in ZFC).

## Lean status
`lean_status: cited`. Mathlib: `T.Model` / `T.IsSatisfiable` (a model is a
`Type` + `Structure` + a proof it satisfies `T`).

## Type / well-formedness check
`well_formed`. `Γ` a set of **sentences** (not open formulas — else "model"
needs a closure convention). `Mod(Γ)` is a **proper class** (there are
arbitrarily large models by `lowenheim_skolem_up`) — statements quantifying over
it use reflection / set-sized approximations. A model of `Γ` is a model of every
`σ ∈ Γ` **simultaneously** (one structure).

## Specialization / boundary cases
- `Γ = ∅`: `Mod(∅)` = all structures.
- `Γ` = a **complete** consistent theory: `Mod(Γ)` is a single elementary-
  equivalence class (but many isomorphism types — `non_categoricity`).
- `Γ` inconsistent: `Mod(Γ) = ∅`.
- **`Δ`-elementary classes**: `Mod(Γ)` for a set `Γ` — closed under
  isomorphism, elementary equivalence, ultraproducts (`compactness_fol`); an
  **elementary class** `Mod(σ)` for a single `σ` is additionally closed under
  ultrapowers and their inverses.

## Hypothesis-dropped counterexamples
- **"model" of open formulas without a closure convention**: ambiguous.
- **a structure satisfying each `σ ∈ Γ` under a *different* assignment**: not a
  model — one structure must work for all.
- **treat `Mod(Γ)` as a set**: Russell-style issues; it is a proper class.

## Common misuse
Using open formulas as theory members without closure; a per-sentence structure;
treating `Mod(Γ)` as a set; assuming a complete theory is categorical (models
agree on *sentences*, not up to isomorphism).

## Related nodes (non-prerequisite)
- `defined_from`: `tarski_satisfaction`, `sentence`.
- `feeds`: `validity`, `semantic_consequence_fol`, `godel_completeness_theorem`
  (model existence), `compactness_fol`, `lowenheim_skolem_*`, `non_categoricity`.
- `related`: elementary class, elementary equivalence, `Th(𝔄)`.

## Sources
[enderton_logic_2e] §2.2; [chiswell_hodges] ch. 5; [hodges_shorter] §1.2.
