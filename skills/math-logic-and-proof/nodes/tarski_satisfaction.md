# tarski_satisfaction

## Type
definition  (epistemic status: `definition`; `constructive_grade: intuitionistic`
as a definition — `metatheory: naive_collections`)

## Statement
`𝔄 ⊨ φ [s]` ("`𝔄` satisfies `φ` under assignment `s`"), by recursion on
`first_order_wff`:

    𝔄 ⊨ R t₁…tₙ [s]  ⟺  (s̄(t₁),…,s̄(tₙ)) ∈ R^𝔄
    𝔄 ⊨ (t₁ = t₂)[s] ⟺  s̄(t₁) = s̄(t₂)
    𝔄 ⊨ ¬φ [s]       ⟺  not 𝔄 ⊨ φ [s]
    𝔄 ⊨ (φ ∧ ψ)[s]   ⟺  𝔄 ⊨ φ [s] and 𝔄 ⊨ ψ [s]      (∨, →, ↔ similarly)
    𝔄 ⊨ ∀x φ [s]     ⟺  for every a ∈ |𝔄|, 𝔄 ⊨ φ [s(x ↦ a)]
    𝔄 ⊨ ∃x φ [s]     ⟺  for some  a ∈ |𝔄|, 𝔄 ⊨ φ [s(x ↦ a)]

## Symbols
- `𝔄`: a `structure`; `s`: an `assignment`; `φ`: a `first_order_wff`.

## Prerequisites (tsort edges into this node)
`first_order_wff`, `term_evaluation`, `assignment`, `structure`,
`recursion_on_wff`, `quantifier_syntax`.

## Content
**Tarski's definition of truth in a formalised language** (1933/1936) — the
foundation of model theory. The quantifier clauses are what make it more than a
propositional valuation: they range over the **domain** (a `naive_collection`),
and reduce satisfaction of `∀x φ` to satisfaction of the *strictly simpler* `φ`
under a modified assignment (well-founded on quantifier rank /
`formula_complexity`).

## Constructive grade
`intuitionistic` **as a definition**. Deciding `𝔄 ⊨ φ` in an **infinite**
structure is not effective (the `∀`-clause quantifies over `|𝔄|`) — a
decidability matter, not a constructivity-of-the-definition one.

## Lean status
`lean_status: cited`. Mathlib: `FirstOrder.Language.BoundedFormula.Realize`.
`validation/proof-checks.lean` builds the **propositional** analogue
(`Wff.eval`); the FOL definition is `cited`.

## Type / well-formedness check
`well_formed`. `metatheory: naive_collections` — depends on `naive_collection`
(the domain, the "for every `a ∈ |𝔄|`"). `s` must be defined on `FV(φ)`
(`coincidence_lemma`: only those matter). Recursion licensed by unique
readability of `first_order_wff`. Domain **nonempty** so the quantifier clauses
behave.

## Specialization / boundary cases
- **propositional reduct** (no quantifiers, 0-ary relations): recovers
  `satisfaction` / `truth_value_recursion`.
- **sentence**: `s`-independent — `𝔄 ⊨ σ`.
- **finite `𝔄`**: satisfaction is **decidable** (the `∀`/`∃` clauses are finite
  conjunctions/disjunctions) — this is what `bc validation/instance-checks.bc`
  exploits (`∀x∃y` vs `∃y∀x` on a 4-element domain).
- **the T-schema**: `𝔄 ⊨ "φ" ⟺ φ` — the disquotational reading Tarski
  formalised.

## Hypothesis-dropped counterexamples
- **empty domain**: `∀x φ` vacuously true, `∃x φ` false for all `φ` —
  `∃x (x = x)` false, breaking duality.
- **`s` undefined on a free variable**: `𝔄 ⊨ (x = y)[s]` meaningless.
- **read the `∀`-clause as ranging over syntax** rather than the domain: a
  common beginner error.
- **non-truth-functional operator** (modal `□`): no single-structure clause —
  needs a Kripke frame.

## Common misuse
Reading the quantifier clause over formulas not elements; treating every formula
as a sentence (forgetting `s`); conflating `𝔄 ⊨ φ` (semantic) with `⊢ φ`
(syntactic); assuming satisfaction is decidable in infinite structures.

## Related nodes (non-prerequisite)
- `refines`: `satisfaction` (propositional).
- `uses`: `term_evaluation`, `assignment`, `structure`.
- `feeds`: `model`, `validity`, `semantic_consequence_fol`, `coincidence_lemma`,
  `substitution_lemma_semantic`, `quantifier_negation`, `soundness_fol`,
  `truth_lemma_fol`.
- `named_for`: Tarski (1933/1936).

## Sources
[enderton_logic_2e] §2.2; [chiswell_hodges] ch. 5; [vandalen_5e] §3.1;
Tarski, *The Concept of Truth in Formalized Languages*.
