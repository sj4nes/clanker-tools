# godel_completeness_theorem

## Type
metatheorem  (epistemic status: `metatheorem`; `constructive_grade: needs_full_classical`)

## Statement
For a first-order language `ℒ` and a set of `ℒ`-sentences `Γ`:

    Γ ⊨ φ   ⟹   Γ ⊢ φ                       (completeness)

equivalently, the **model existence** form:

    Γ consistent   ⟹   Γ has a model.

With soundness (`soundness_fol`), `Γ ⊨ φ ⟺ Γ ⊢ φ`: semantic and syntactic
consequence coincide for classical first-order logic with equality.

## Symbols
- `ℒ`: a signature (`signature`); may be of any cardinality — the proof splits
  on countable vs uncountable.
- `Γ`: a set of `ℒ`-sentences (`Theory`, a `naive_collection`).
- `φ`: an `ℒ`-sentence.
- the model produced: the **term model** `𝔐` (`term_model`), domain = closed
  `ℒ⁺`-terms modulo provable equality.

## Prerequisites (tsort edges into this node)
`truth_lemma_fol`, `term_model`, `henkin_theory`, `lindenbaum_lemma_fol`,
`soundness_fol`, `semantic_consequence_fol`, `alpha_equivalence`.

## Proof (Henkin, the version this capsule formalises)
1. **Reduce to model existence.** `Γ ⊨ φ` and `Γ ⊬ φ` ⟹ `Γ ∪ {¬φ}` consistent
   (`derivability_fol` + `raa_rule`); a model of it refutes `Γ ⊨ φ`.
2. **Add witnesses** (`henkin_constants`). Extend `ℒ` to `ℒ⁺` by a fresh
   constant `c_ψ` for every formula `ψ(x)` with one free variable, in an
   `ω`-chain `ℒ = ℒ₀ ⊆ ℒ₁ ⊆ …`, `ℒ⁺ = ⋃ ℒₙ`. Add the **Henkin axioms**
   `(∃x ψ) → ψ[c_ψ/x]`. The extension is conservative, so `Γ⁺` stays consistent
   (`metatheoretic_induction` on the chain).
3. **Maximise** (`lindenbaum_lemma_fol`). Extend `Γ⁺` to a maximal consistent
   `T ⊇ Γ⁺` in `ℒ⁺`. `T` is a **Henkin theory** (`henkin_theory`): complete,
   and `∃x ψ ∈ T ⟹ ψ[c/x] ∈ T` for some constant `c`.
4. **Build the term model** (`term_model`). Domain `= {closed ℒ⁺-terms}/≈`,
   `t ≈ u :⟺ (t = u) ∈ T` — an equivalence relation and a congruence by the
   `equality_axioms`. Interpret each symbol syntactically.
5. **Truth lemma** (`truth_lemma_fol`): for every `ℒ⁺`-sentence `σ`,
   `𝔐 ⊨ σ ⟺ σ ∈ T`, by `structural_induction_wff`. The `∃` clause is exactly
   where the witness property (step 3) is used; the `¬` and `∨` clauses use
   completeness of `T` (`quantifier_negation` / classical MCS reasoning).
6. `Γ ⊆ T`, so `𝔐 ⊨ Γ`. Reduct to `ℒ` is still a model of `Γ`. ∎

## Where the metatheory is classical (`needs_full_classical`)
- **Lindenbaum** decides each sentence in or out — excluded middle at every
  stage. For a **countable** `ℒ` this is LEM + `metatheoretic_induction`, **no
  choice**. For an **uncountable** `ℒ` it needs Zorn / an ultrafilter — recorded
  on `lindenbaum_lemma_fol` as the choice-flavoured step.
- The truth lemma's `¬`/`∨` clauses use that a complete consistent theory
  contains `ψ` or `¬ψ`.

## Lean status
`lean_status: cited` (corrected from `partial` — audited 2026-09-11; see
`BACKLOG.md`). `validation/proof-checks.lean` states, in its own header
comment, that it is "not the place for the Henkin construction" — no
`Formula`/`Term`/`Structure`/`satisfaction` inductive types exist in it,
and none of the six Henkin-proof steps above are kernel-checked.
`validation/proof-checks.md`'s own "Cited only" section lists this node
explicitly. Cited: [enderton_logic_2e] Thm 25.14, [vandalen_5e] Thm 2.5.3.

**Release 0.2 target, not a current claim:** `Formula`/`Term`/`Structure`/
`satisfaction` as inductive types; soundness proved outright; the Henkin
construction carried as far as feasible; connected to Mathlib
`FirstOrder.Language` and its completeness development where present
(`mathlib_cited`); every `sorry` / informal step logged. The epistemic
label will **not** be upgraded past what the kernel actually checks when
that work happens.

## Type / well-formedness check
`well_formed`. Recorded: the Henkin constants must be **genuinely fresh** at
each stage (`objects.md`); the Henkin axiom `(∃x ψ) → ψ[c_ψ/x]` needs `c_ψ`
**free for `x`** in `ψ` — automatic since `c_ψ` is a constant, but the check is
made. `alpha_equivalence` renames bound variables so nested witness
substitutions stay capture-free.

## Specialization / boundary cases
- **Propositional fragment**: reduces to `post_completeness_theorem` (no terms,
  no witnesses — Lindenbaum + truth lemma over `truth_assignment`).
- **`Γ` finite**: `⊨ (⋀Γ → φ) ⟹ ⊢ (⋀Γ → φ)` — a single valid sentence is a
  theorem.
- **`Γ` complete and consistent**: the term model is a *canonical* model of `Γ`.

## Hypothesis-dropped counterexamples
- **Drop "first-order"**: **second-order logic with standard semantics has no
  complete proof system** — `(ℕ, +, ·, <)` is categorical in SOL, so a complete
  SOL calculus would decide all of arithmetic, contradicting
  `godel_incompleteness_first`. (`edges/relations.tsv`: `contrast_with`.)
- **Drop consistency**: an inconsistent `Γ` proves everything but has no model —
  the model-existence direction needs consistency.
- **Drop the equality axioms in the term model**: without the congruence,
  `t ≈ u` is not well-defined on the quotient and interpretations are not
  functions.

## Common misuse
Confusing it with `godel_incompleteness_first` ("Gödel proved logic both
complete and incomplete" — different objects: the *logic* is complete, a
*theory* like PA is incomplete). Thinking completeness gives a **decision
procedure** for validity — it gives a semidecision procedure (enumerate proofs);
`undecidability_fol_validity` says no more. Assuming the model is countable for
an uncountable language.

## Related nodes (non-prerequisite)
- `special_case_of` (reverse): `compactness_fol`, `lowenheim_skolem_down` are
  proved from it.
- `equivalent_to`: the model-existence (Henkin) form.
- `commonly_confused_with`: `godel_incompleteness_first`.
- `historically_precedes`: Gödel 1929/1930; Henkin's proof 1949.

## Sources
[enderton_logic_2e] §2.5; [vandalen_5e] §3.1–3.2; [chiswell_hodges] ch. 5–6;
[mathlib_firstorder].
