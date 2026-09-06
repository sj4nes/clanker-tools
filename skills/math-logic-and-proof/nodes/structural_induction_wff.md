# structural_induction_wff

## Type
theorem  (epistemic status: `proved_theorem` / induction principle;
`constructive_grade: intuitionistic`)

## Statement
To prove `∀φ, P(φ)` for wffs: prove `P` of every atom and of `⊥`, and prove that
each connective **preserves** `P` — `P(φ) ⟹ P(¬φ)`, and
`P(φ) ∧ P(ψ) ⟹ P(φ ∘ ψ)` for `∘ ∈ {∧, ∨, →, ↔}`. Then `P(φ)` holds for every
wff.

## Symbols
- `P`: a predicate on `Wff`.
- the cases: one per constructor of `wff_syntax`.

## Prerequisites (tsort edges into this node)
`wff_syntax`, `inductive_definition`, `wff_unique_readability`.

## Content
The **induction principle of the `wff_syntax` inductive definition** — `Wff` is
the *least* set closed under the clauses, so any `P`-closed class contains it.
It is the specialisation of `structural_induction` to `Wff`, and (via
`formula_complexity`) equivalent to `strong_induction` on formula degree.

It is the workhorse of propositional metatheory: `soundness_prop` (induction on
the *derivation*, a different inductive type, but same principle),
`truth_lemma_prop`, `substitution_of_equivalents`, the normal-form theorems, and
`wff_unique_readability` itself (the parenthesis lemma) are all proved by it.

## Constructive grade
`intuitionistic` — it is a recursor; no classical input. A proof by structural
induction computes.

## Lean status
`lean_status: core`. `induction φ with | atom n => … | fls => … | neg p ih => …
| conj p q ih1 ih2 => …` in `validation/proof-checks.lean` (used in `soundness`,
the `equiv_*` congruences, `taut_iff_neg_contra`, …). `#print axioms` on those
shows at most `propext` — the induction adds no axiom.

## Type / well-formedness check
`well_formed` **iff** every constructor gets a case and the IH offered is
exactly "`P` of the immediate subformulas" — no more (assuming `P` of a
non-subformula, e.g. a substitution instance, is unsound; use degree induction
instead), no less (skipping the `↔` or `⊥` case leaves a gap). Requires
`wff_unique_readability` so the cases are exhaustive and exclusive.

## Specialization / boundary cases
- `P` about **truth values**: `truth_value_recursion`'s truth-functionality.
- `P` about **derivations**: "rule induction" — the same principle for the
  `nd_derivation` / `hilbert_derivation` inductive types (one case per rule).
- **degree induction**: when the IH must range over *all* smaller formulas (post
  a substitution), induct on `formula_complexity` via `strong_induction`.
- first-order: `first_order_wff` adds `∀x`, `∃x` cases (the sub-formula there has
  one more free variable) — the pattern behind `coincidence_lemma`,
  `truth_lemma_fol`.

## Hypothesis-dropped counterexamples
- **omit a constructor case** (forget `↔` or `⊥`): the "proof" has a gap;
  `P` may fail on formulas using that connective.
- **use the IH on a non-subformula** (a substitution result, `∀x`-instance): not
  licensed — that formula is not structurally smaller.
- **`Wff` not the least fixed point** (add a "nothing else" violation, or make
  it coinductive): structural induction is **invalid** — for a coinductive
  "formula" type (infinite trees) you need coinduction.

## Common misuse
Skipping the base or a connective case; using the IH on a substitution instance;
treating a coinductively-defined syntax inductively; conflating induction on
*formula structure* with induction on *derivation structure* (both valid, both
this principle, different inductive types).

## Related nodes (non-prerequisite)
- `instance_of`: `structural_induction`.
- `equivalent_to` (via `formula_complexity`): `strong_induction` on degree.
- `licensed_by`: `wff_unique_readability`.
- `enables`: `recursion_on_wff`, `soundness_prop`, `truth_lemma_prop`, the
  normal-form theorems.

## Sources
[enderton_logic_2e] §1.4; [vandalen_5e] §1.1; [chiswell_hodges] ch. 2.
