# soundness_fol

## Type
metatheorem  (epistemic status: `metatheorem`; `constructive_grade: needs_DNE`
— the classical-rule case; the quantifier-rule core is constructive)

## Statement
For a first-order language `ℒ` with equality: if `Γ ⊢ φ` in the calculus
(`derivability_fol`) then `Γ ⊨ φ` (`semantic_consequence_fol`) — every provable
consequence is a genuine semantic consequence. Equivalently: a **satisfiable**
theory is **consistent**.

## Symbols
- `Γ`: a set of `ℒ`-formulas; `φ`: an `ℒ`-formula.
- the derivation: a finite object (`nd_derivation` / `hilbert_derivation`),
  calculus-independent by `nd_hilbert_equivalence`.

## Prerequisites (tsort edges into this node)
`derivability_fol`, `semantic_consequence_fol`, `substitution_lemma_semantic`,
`coincidence_lemma`, `eigenvariable_condition`, `structural_induction_wff`.

## Proof (induction on the derivation)
Show every rule **preserves the property** "every model of `Γ` under every
assignment satisfying the open assumptions satisfies the conclusion".
- **propositional rules**: as `soundness_prop` (truth-table clauses; the
  classical rule needs `needs_DNE` in the metatheory).
- **`∀E`** (`∀x φ ⊢ φ(t/x)`): from `𝔄 ⊨ ∀x φ[s]` and
  `substitution_lemma_semantic` (needs `t` **free for `x`**), `𝔄 ⊨ φ(t/x)[s]`.
- **`∃I`** (`φ(t/x) ⊢ ∃x φ`): the converse direction of the same lemma.
- **`∀I`** (`φ ⊢ ∀x φ`, `x` not free in `Γ`): the **eigenvariable condition**
  makes `x` genuinely arbitrary; `coincidence_lemma` discharges "`x` not free in
  the open assumptions", so `𝔄 ⊨ φ[s(x↦a)]` for every `a`.
- **`∃E`**: dual, same eigenvariable condition.
- **equality axioms**: valid because `=` is interpreted as identity
  (`first_order_logic_with_equality`).

## Constructive grade
`needs_DNE` overall (the classical propositional rule). The **quantifier and
equality** cases are constructive. A soundness proof for the intuitionistic
first-order calculus (Kripke semantics) is fully constructive.

## Lean status
`lean_status: partial`. The propositional core (`soundness` in
`validation/proof-checks.lean`) is a genuine kernel proof on `propext`. The
quantifier cases are `stated` (they need the FOL `satisfaction` and
`substitution_lemma_semantic` formalised, which without Mathlib is not done);
`validation/proof-checks.md` records the split.

## Type / well-formedness check
`well_formed`. `Γ` and `φ` in the same language; the delicate obligations are
**`free_for`** (for `∀E`/`∃I`) and the **`eigenvariable_condition`** (for
`∀I`/`∃E`) — a derivation violating either is not a derivation, and soundness is
exactly the guarantee that respecting them yields truth-preservation.

## Specialization / boundary cases
- `Γ = ∅`: `⊢ φ` ⟹ `φ` is **valid** (true in every structure).
- **contrapositive** — a formula with a **countermodel** is **not derivable**:
  the standard way to prove non-theorems (e.g. `∃x P x → ∀x P x` has a 2-element
  countermodel, so it is unprovable).
- propositional reduct: recovers `soundness_prop`.
- `Γ` finite: `⊢ (⋀Γ → φ)` ⟹ `⊨ (⋀Γ → φ)`.

## Hypothesis-dropped counterexamples
- **drop the eigenvariable condition on `∀I`**: from `P(x)` derive `∀x P(x)`, so
  `{P(x)} ⊢ ∀x P(x)`; but `{P(x)} ⊭ ∀x P(x)` in a structure where `P` holds of
  `s(x)` only. **Soundness fails.**
- **drop `free_for` on `∀E`**: from `∀x ∃y (y ≠ x)` derive `∃y (y ≠ y)` — valid
  premise, contradictory conclusion (`free_for.md` capture bug).
- **misinterpret `=`** (not as identity): `x = x ⊢ …` reasoning breaks; equality
  axioms become unsound.

## Common misuse
Confusing with `godel_completeness_theorem` (the converse); assuming FOL
soundness follows from propositional soundness (the quantifier/equality rules
need their own cases); skipping the eigenvariable check "because it usually
works out"; using it to conclude provability.

## Related nodes (non-prerequisite)
- `converse_is`: `godel_completeness_theorem`.
- `specialises`: `soundness_prop`.
- `feeds`: `godel_completeness_theorem` (the "`Γ ⊨ φ` and `Γ ⊬ φ` ⟹
  `Γ ∪ {¬φ}` consistent" reduction), `compactness_fol`.
- `guarded_by`: `free_for`, `eigenvariable_condition`.

## Sources
[enderton_logic_2e] §2.5 (Soundness Theorem); [vandalen_5e] §3.1;
[chiswell_hodges] §5.2.
