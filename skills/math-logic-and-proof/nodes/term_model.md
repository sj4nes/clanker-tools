# term_model

## Type
construction  (epistemic status: `constructive_result`; `constructive_grade:
intuitionistic` given a Henkin theory — the classicality is upstream in
`henkin_theory`)

## Statement
Given a maximal consistent Henkin theory `T*` over `ℒ⁺`, the **term model**
(canonical model, Henkin model) `𝔐` is the `ℒ⁺`-structure:
- **domain** `M = {closed ℒ⁺-terms} / ≈`, where `t ≈ u :⟺ (t = u) ∈ T*`;
- **constants** `c^𝔐 = [c]`;
- **functions** `f^𝔐([t₁], …, [tₙ]) = [f t₁ … tₙ]`;
- **relations** `([t₁], …, [tₙ]) ∈ R^𝔐 :⟺ R t₁ … tₙ ∈ T*`.

## Symbols
- `T*`: a Henkin theory (`henkin_theory`).
- `[t]`: the `≈`-class of the closed term `t`.
- `𝔐`: the resulting structure (`Structure` — depends on `naive_collection`).

## Prerequisites (tsort edges into this node)
`henkin_theory`, `term_evaluation`, `structure`, `equality_axioms`,
`first_order_logic_with_equality`.

## Well-definedness — the type check that carries the weight
- `≈` is an **equivalence relation**: reflexive/symmetric/transitive from the
  `equality_axioms` (`t = t`, and the substitution schema) being in `T*`
  (deductively closed).
- `≈` is a **congruence**: if `t₁ ≈ u₁, …, tₙ ≈ uₙ` then `f t₁… ≈ f u₁…` and
  `R t₁… ↔ R u₁…` in `T*` — again from the equality substitution schema. This is
  what makes `f^𝔐` and `R^𝔐` **well-defined on the quotient** (the same
  obligation as `well_defined_on_quotient` in `math-sets-functions-cardinality`).
- domain **nonempty**: `ℒ⁺` has closed terms (the Henkin constants), so
  `M ≠ ∅` — the standing convention (`objects.md`) is met without extra
  hypotheses.

## Evaluation lemma
For every closed `ℒ⁺`-term `t`: `t^𝔐 = [t]` (the term denotes its own class), by
induction on `t` (`term_evaluation`).

## Constructive grade
`intuitionistic` **relative to `T*`** — the quotient, the interpretations, and
the evaluation lemma use no classical principle beyond what built `T*`. All the
classicality sits in `lindenbaum_lemma_fol`.

## Lean status
`lean_status: cited`. Mathlib builds exactly this as
`FirstOrder.Language.Theory.Model` from a complete Henkin theory (the
"term model" / `CompleteType`-free canonical model). Not in
`validation/proof-checks.lean`.

## Type / well-formedness check
`well_formed` **iff** the congruence check passes — a `term_model` built without
the `equality_axioms` in `T*` has `f^𝔐`, `R^𝔐` that are not functions/relations
on `M` (representative-dependent). This is the single most important
well-formedness obligation in the completeness proof and mirrors the
quotient-construction discipline of the number-systems capsule.

## Specialization / boundary cases
- `ℒ⁺` **countable** ⇒ `M` countable (a quotient of a countable set) ⇒
  `lowenheim_skolem_down`.
- `ℒ` has **no function symbols**: `M` = equivalence classes of constants only.
- `T*` = the (Henkinised) theory of an actual structure `𝔄`: the term model
  embeds elementarily into `𝔄`.
- if `T*` proves `t = u` for all closed `t, u`: `M` is a **single point** (a
  one-element model) — legitimate, and the reason the domain-nonempty convention
  matters rather than domain-infinite.

## Hypothesis-dropped counterexamples
- **drop the equality axioms from `T*`**: `≈` need not be transitive or a
  congruence; `[t]` is ill-defined, interpretations are multivalued — no
  structure.
- **`T*` not Henkin**: the truth lemma's `∃` clause fails — `𝔐 ⊨ ∃x φ` requires
  a *term* witness, which only the witness property supplies.
- **`T*` not maximal**: `R^𝔐` is defined by `R t… ∈ T*`, but without maximality
  `R t… ∉ T*` does not give `¬R t… ∈ T*`, so the `¬` clause of the truth lemma
  breaks.

## Common misuse
Skipping the congruence check ("obviously well-defined"); forgetting the model
is over `ℒ⁺` (must reduct to `ℒ`); assuming the term model is the *intended*
model (it is syntactic — `√2` in a term model of real-closed-field theory is a
formal term, not the real number); thinking every element is named (true here —
that is special, it is an *atomic*/*prime* model).

## Related nodes (non-prerequisite)
- `built_from`: `henkin_theory`.
- `analogue_of`: `quotient_set` / `well_defined_on_quotient`
  (`math-sets-functions-cardinality`).
- `feeds`: `truth_lemma_fol`, `godel_completeness_theorem`,
  `lowenheim_skolem_down`.

## Sources
[enderton_logic_2e] §2.5; [chiswell_hodges] §5.3; [vandalen_5e] §3.1;
[hodges_shorter] §2.1 (canonical models).
