# nd_derivation

## Type
definition  (epistemic status: `definition`; `constructive_grade: split` —
the object is neutral; classicality enters only via the `RAA` rule)

## Statement
A **natural-deduction derivation** of `φ` from `Γ` is a finite tree whose nodes
are wffs, whose leaves are members of `Γ` or **discharged assumptions**, whose
each internal step is an instance of a rule of `nd_rules_propositional`, and
whose root is `φ`. Written `Γ ⊢_ND φ`. (Gentzen trees and Fitch boxes are the
same object in different notation.)

## Symbols
- `Γ`: the **open** assumptions (a finite set of wffs).
- discharged assumptions: leaves closed off by an `→I`, `∨E`, `¬I`, or `RAA`
  step — no longer counted in `Γ`.
- the tree: a `finite_sequence`/tree of rule instances, generated inductively
  (`inductive_definition`).

## Prerequisites (tsort edges into this node)
`finite_sequence`, `wff_syntax`, `nd_rules_propositional`, `inductive_definition`.

## Content
The derivation is the **object** the metatheorems talk about: `soundness_prop`
inducts on its structure; `deduction_theorem` / `nd_hilbert_equivalence`
transform it; `compactness_prop` uses that it mentions only **finitely many**
premises. "`Γ ⊢ φ`" (`derivability`) abstracts away *which* derivation.

Because it is an `inductive_definition`, it comes with **rule induction**
(`structural_induction` specialised): to prove a property of all derivations,
check it for `ax` and for each rule assuming it of the sub-derivations.

## Constructive grade
`split` — the tree data structure is neutral. A derivation using no `RAA` step
is an **intuitionistic** derivation (and, via Curry–Howard, a typed λ-term);
one using `RAA` is classical.

## Lean status
`lean_status: core` (fragment). `validation/proof-checks.lean`
`inductive Deriv : Ctx → Wff → Prop` **is** `⊢_ND` for the fragment; the
`soundness` theorem is `Deriv Γ p → Entails Γ p` by `induction d`. Derived
rules (`Deriv.cut`, `Deriv.and_comm`, `Deriv.explosion`) are short compositions.

## Type / well-formedness check
`well_formed`. Bookkeeping obligations (`objects.md`): every leaf is in `Γ` or
gets discharged; a discharge closes **exactly** its assumption; each step
matches a rule schema. An "open" assumption left undischarged **belongs in
`Γ`** — a derivation of `φ` from `Γ` with a stray open `ψ` is really a
derivation from `Γ ∪ {ψ}`.

## Specialization / boundary cases
- `Γ = ∅`: `⊢_ND φ` — `φ` is a **theorem** (a tautology, by
  `soundness_prop` + `post_completeness_theorem`).
- a one-node tree: `φ ⊢_ND φ` (`ax`).
- Fitch vs Gentzen: presentation only; same derivability.
- **first-order**: `nd_derivation` extends with `nd_rules_quantifier` and the
  `eigenvariable_condition` — a separate edge into `derivability_fol`.

## Hypothesis-dropped counterexamples
- **infinitely deep / infinite tree**: not a derivation — finiteness is
  definitional and is what `compactness_prop` relies on.
- **undischarged assumption not counted in `Γ`**: "proves" `Γ ⊢ φ` when only
  `Γ ∪ {ψ} ⊢ φ` holds.
- **step not matching any rule**: not a derivation.

## Common misuse
Leaving an assumption open and forgetting to add it to `Γ`; discharging an
assumption that was never made; discharging the wrong assumption in `RAA`;
treating a Fitch proof and a Gentzen proof as different systems; assuming a
derivation gives a *decision procedure* (finding one is search;
`tautology_decidable` gives a semantic one).

## Related nodes (non-prerequisite)
- `equivalent_to`: `hilbert_derivation` (`nd_hilbert_equivalence`).
- `built_from`: `nd_rules_propositional`.
- `abstracted_by`: `derivability`.
- `mentioned_alternative`: sequent calculus derivations; semantic tableaux.
- `related`: Curry–Howard (normal derivations ↔ normal λ-terms).

## Sources
[vandalen_5e] ch. 2; [chiswell_hodges] ch. 4; [enderton_logic_2e] §2.4;
Prawitz (1965); Gentzen (1935).
