# truth_lemma_fol

## Type
proved_lemma  (epistemic status: `proved_lemma`; `constructive_grade:
needs_LEM` — the `¬`/`∨` clauses use classical completeness of the Henkin
theory)

## Statement
Let `T*` be a maximal consistent Henkin theory over `ℒ⁺` and `𝔐` its term model
(`term_model`). Then for **every** `ℒ⁺`-sentence `σ`:

    𝔐 ⊨ σ   ⟺   σ ∈ T*.

In particular `𝔐 ⊨ T*`, and (reducting to `ℒ`) `𝔐 ⊨ T` for the original theory.

## Symbols
- `T*`: the Henkin theory; `𝔐`: its term model.
- `σ`: any `ℒ⁺`-sentence; the proof runs by induction on all `ℒ⁺`-formulas
  (with an assignment sending each free variable to the class of a closed term).

## Prerequisites (tsort edges into this node)
`henkin_theory`, `term_model`, `tarski_satisfaction`, `structural_induction_wff`,
`quantifier_negation`.

## Proof (by `structural_induction_wff` on `σ`)
- **atomic `R t₁…tₙ`**: `𝔐 ⊨ R t₁…tₙ` ⟺ `([t₁],…,[tₙ]) ∈ R^𝔐` ⟺ `R t₁…tₙ ∈ T*`
  (definition of `R^𝔐`); equality atoms by definition of `≈`. Uses the
  `term_model` evaluation lemma `t^𝔐 = [t]`.
- **`¬σ`**: `𝔐 ⊨ ¬σ` ⟺ not `𝔐 ⊨ σ` ⟺ (IH) `σ ∉ T*` ⟺ `¬σ ∈ T*` (maximality +
  consistency). **Classical step.**
- **`σ ∧ τ`**, **`σ ∨ τ`**: from IH + `T*` deductively closed and complete. The
  `∨` case uses `σ ∨ τ ∈ T* ⇒ σ ∈ T* or τ ∈ T*`, which needs maximality
  (`quantifier_negation`-style reasoning). **Classical step.**
- **`∃x φ`**: `𝔐 ⊨ ∃x φ` ⟺ some `[t]` satisfies `φ` ⟺ (IH, on the sentence
  `φ(t/x)`) `φ(t/x) ∈ T*` for some closed `t` ⟺ `∃x φ ∈ T*` — the `⟸` direction
  is the **witness property** of `henkin_theory`; the `⟹` uses that every domain
  element is `[t]` for some closed term (`term_model`).
- **`∀x φ`**: `∀x φ ≡ ¬∃x ¬φ`, reduce to the above (`exists_forall_duality`).

## Constructive grade
`needs_LEM`. The `¬` and `∨` clauses rest on `T*` being **complete**
(`σ ∈ T*` or `¬σ ∈ T*`) — a classical property established by
`lindenbaum_lemma_fol`. The atomic and `∧` and (witness-property direction of)
`∃` clauses are constructive.

## Lean status
`lean_status: cited`. Mathlib proves the analogous statement in its completeness
development. `validation/proof-checks.lean` proves the **propositional**
analogue's shape via `soundness` machinery but not this.

## Type / well-formedness check
`well_formed`. The induction is over **all formulas** (with an assignment), not
just sentences — the `∃`/`∀` clauses strip a quantifier and produce a formula
with one more free variable, handled by substituting a closed term
(`free_for` is automatic for closed terms). Requires the `term_model` evaluation
lemma and the congruence property already discharged.

## Specialization / boundary cases
- **propositional analogue** (`truth_lemma_prop`): `v ⊨ σ ⟺ σ ∈ Δ` for a
  maximal consistent `Δ`, `v(atom) = [atom ∈ Δ]`; no quantifier clauses, no
  Henkin witnesses.
- `T*` = Henkinised theory of a real structure `𝔄`: the term model is
  elementarily equivalent to `𝔄` (and elementarily embeds).
- if `T*` decides `∀x (x = c)` positively: term model is a single point and the
  lemma still holds.

## Hypothesis-dropped counterexamples
- **`T*` not maximal**: `¬` clause fails — `σ ∉ T*` no longer gives `¬σ ∈ T*`.
- **`T*` not Henkin**: `∃` clause fails — `∃x φ ∈ T*` with no term witness means
  `𝔐 ⊭ ∃x φ` while `∃x φ ∈ T*`.
- **term model built without equality congruence**: atomic clause ill-defined.
- **constructive metatheory**: no complete `T*` (Lindenbaum fails), so no truth
  lemma — completeness genuinely fails constructively.

## Common misuse
Proving only `T* ⊆ Th(𝔐)` (one direction) and claiming the model; skipping the
`∃` witness-property step; forgetting the assignment in the quantifier cases;
treating `𝔐 ⊨ σ` as decidable (it is, *here*, because every element is named —
but that is a special feature of term models, not general).

## Related nodes (non-prerequisite)
- `specialises`: `truth_lemma_prop`.
- `immediately_gives`: `godel_completeness_theorem` (model existence).
- `uses`: `henkin_theory` (witness property), `term_model` (evaluation +
  congruence), `quantifier_negation` (`∨`/`¬` clauses).

## Sources
[enderton_logic_2e] §2.5 (Lemma 25A); [chiswell_hodges] §5.3;
[vandalen_5e] §3.1 (the "model existence lemma").
