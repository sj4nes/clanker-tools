# semantic_consequence

## Type
definition  (epistemic status: `definition`; `constructive_grade: intuitionistic`
as a definition)

## Statement
`Γ ⊨ φ` ("`Γ` semantically entails / logically implies `φ`") iff **every** truth
assignment that satisfies all of `Γ` also satisfies `φ`:

    Γ ⊨ φ   :⟺   ∀v, (v ⊨ Γ) → v ⊨ φ.

## Symbols
- `Γ`: a set of wffs (premises); `φ`: a wff (conclusion).
- `Γ ⊨ φ`: a **metastatement** (a `Prop` about assignments), not a wff.

## Prerequisites (tsort edges into this node)
`satisfaction`, `truth_assignment`.

## Content
The semantic counterpart of `derivability` (`Γ ⊢ φ`). `soundness_prop` says
`⊢` ⊆ `⊨`; `post_completeness_theorem` says `⊨` ⊆ `⊢`; together `Γ ⊨ φ ⟺ Γ ⊢ φ`.

Equivalent forms:
- `Γ ⊨ φ` iff `Γ ∪ {¬φ}` is unsatisfiable (`contradiction_unsat`);
- for finite `Γ = {γ₁,…,γₙ}`: `Γ ⊨ φ` iff `⊨ (γ₁ ∧ … ∧ γₙ → φ)` (a
  `tautology`) — the **semantic deduction theorem**;
- `∅ ⊨ φ` iff `φ` is a `tautology`.

## Constructive grade
`intuitionistic` as a definition. As a *fact to establish*: for finite `Γ`,
decidable (`truth_table`); the `∅ ⊨ p ∨ ¬p` kind of instance is a classical
tautology with no intuitionistic proof of the corresponding `⊢`.

## Lean status
`lean_status: core`. `validation/proof-checks.lean`:
`Entails Γ p := ∀ v, (∀ q ∈ Γ, eval v q = true) → eval v p = true` — this **is**
`semantic_consequence`; the `soundness` theorem concludes `Entails Γ p` from
`Deriv Γ p`.

## Type / well-formedness check
`well_formed`. `Γ` and `φ` in the same language. `Γ ⊨ φ` is **not** a wff — it
cannot be nested inside connectives or quantified; it is a statement in the
metatheory. Confusing `Γ ⊨ φ` with the object wff `(⋀Γ) → φ` is the classic
"use–mention" slip (they are related by the semantic deduction theorem, for
**finite** `Γ`).

## Specialization / boundary cases
- `Γ = ∅`: `⊨ φ` — tautologyhood.
- `Γ = {φ}`: `φ ⊨ φ` always (reflexivity).
- `φ ∈ Γ`: `Γ ⊨ φ` trivially.
- **monotone**: `Γ ⊨ φ` and `Γ ⊆ Δ` ⟹ `Δ ⊨ φ` (adding premises never loses
  consequences — classical logic is monotone; non-monotonic logics drop this,
  out of scope).
- **cut / transitivity**: `Γ ⊨ ψ` for each `ψ ∈ Δ` and `Δ ⊨ φ` ⟹ `Γ ⊨ φ`.

## Hypothesis-dropped counterexamples
- **check assignments satisfying `φ` instead of `Γ`**: reverses the implication
  — `p ⊨ p ∨ q` holds, `p ∨ q ⊨ p` does not.
- **`Γ` unsatisfiable**: then `Γ ⊨ φ` for **every** `φ` (vacuously — no `v`
  satisfies `Γ`); the "explosion" at the semantic level.
- **infinite `Γ` and the deduction-theorem form**: `⊨ (⋀Γ → φ)` is not
  well-formed for infinite `Γ` (`⋀Γ` is not a wff); the equivalence needs
  `compactness_prop` (`Γ ⊨ φ` ⟹ some finite `Γ₀ ⊨ φ`).

## Common misuse
Writing `Γ ⊨ φ` as if it were the wff `⋀Γ → φ`; nesting `⊨` inside connectives;
checking the wrong side of the implication; forgetting the vacuous case when `Γ`
is unsatisfiable; assuming the deduction-theorem form for infinite `Γ` without
compactness.

## Related nodes (non-prerequisite)
- `syntactic_counterpart`: `derivability` (`Γ ⊢ φ`).
- `related`: `soundness_prop`, `post_completeness_theorem` (the two inclusions),
  `compactness_prop` (finite character).
- `special_case`: `tautology` (`Γ = ∅`), `logical_equivalence` (mutual
  `⊨` of two singletons).

## Sources
[enderton_logic_2e] §1.2; [vandalen_5e] §1.3; [chiswell_hodges] §2.3.
