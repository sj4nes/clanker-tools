# nd_hilbert_equivalence

## Type
proved_lemma  (epistemic status: `proved_lemma`; `constructive_grade: needs_DNE`
for the classical calculi as shipped — the intuitionistic fragments coincide
intuitionistically)

## Statement
For every finite `Γ` and wff `φ`:

    Γ ⊢_ND φ   ⟺   Γ ⊢_H φ

The natural-deduction calculus (`nd_derivation` + `nd_rules_propositional` +
`raa_rule`) and the Hilbert calculus (`hilbert_system_prop`: axiom schemas
`P→(Q→P)`, `(P→(Q→R))→((P→Q)→(P→R))`, `(¬Q→¬P)→(P→Q)`, plus modus ponens)
derive exactly the same consequences.

Consequence: `derivability` (`Γ ⊢ φ`) is **calculus-independent**; no downstream
metatheorem depends on which calculus is used.

## Symbols
- `Γ`: a finite set of wffs (`Context`).
- `⊢_ND`, `⊢_H`: derivability in each calculus.

## Prerequisites (tsort edges into this node)
`nd_derivation`, `hilbert_derivation`, `deduction_theorem`, `assumption_discharge`.

## Proof
**(⇐) Hilbert ⟹ ND.** Each Hilbert axiom schema is an ND theorem (short
derivations); modus ponens is `→E`. Induction on the Hilbert derivation
(`metatheoretic_induction`).

**(⇒) ND ⟹ Hilbert.** Induction on the structure of the ND derivation
(`inductive_definition` of `nd_derivation`). The only non-routine case is
`→I` (discharge): an ND derivation of `ψ` from `Γ, φ` becomes, by IH, a Hilbert
derivation of `ψ` from `Γ ∪ {φ}`; the **deduction theorem** (`deduction_theorem`)
converts it to a Hilbert derivation of `φ → ψ` from `Γ`. `∨E`, `¬I`, `RAA` use
the corresponding Hilbert-provable schemas.

## Constructive grade
As shipped, both calculi are **classical** (ND includes `raa_rule`; Hilbert
includes the contraposition axiom `(¬Q→¬P)→(P→Q)`), so the lemma is
`needs_DNE`. Restricting ND to `{∧,∨,→,⊥}`-intro/elim + `⊥E` and Hilbert to the
first two schema groups + `⊥E` gives **intuitionistic** calculi that coincide
**intuitionistically** — recorded, because it is what lets the constructive
grade of every downstream law be read off either calculus.

## Lean status
`lean_status: core`. `validation/proof-checks.lean` (§5–5b) defines `Deriv` (the
ND fragment) and `H` (a classical Hilbert calculus matching it rule for rule:
`K`, `S`, MP, the three `∧` schemas, ex falso `⊥→φ`, and the classical reductio
axiom `(¬φ→⊥)→φ`; `¬` is primitive and enters only through that axiom, exactly
as in `Deriv`) as **separate** inductive predicates over `Wff`, then proves the
**full round trip** `deriv_iff_H : Deriv Γ φ ↔ H Γ φ`, both directions genuine
and universal:

- **`H_of_deriv`** (`Deriv ⇒ H`): induction on the ND derivation; the `→I`
  (discharge) case *is* the **deduction theorem** (`theorem deduction`, proved
  by induction on `H`), and the `∧I`/`∧E`/`⊥E`/`RAA` cases are one `H.mp` each
  against the matching schema.
- **`deriv_of_H`** (`H ⇒ Deriv`): induction on the Hilbert derivation; each
  axiom schema is a short `impI`-built ND theorem (generic in `Γ`), MP is `→E`.
- **`Deriv.weaken`**: context monotone under `⊆` — the weakening lemma, proved
  by induction (`impI`/`raa` push the extra context under the discharged
  assumption).

`#print axioms deriv_iff_H` → `propext` only: the meta-level proof is
constructive even though both calculi are classical. Recorded in
`validation/proof-checks.md`.

## Type / well-formedness check
`well_formed`. Both sides range over the **same** `Wff` type and the **same**
finite `Γ`. The deduction theorem used in the proof needs no `free_for`
condition (propositional). Discharged-assumption bookkeeping in `nd_derivation`
is part of the object, checked in `objects.md`.

## Specialization / boundary cases
- `Γ = ∅`: `⊢_ND φ ⟺ ⊢_H φ` — the theorems coincide.
- adding a third calculus (a **sequent calculus** `LK`): `⊢_LK` coincides too
  (`edges/relations.tsv`: `mentioned_alternative`), so "provable" is robust —
  but `LK`'s cut-elimination proof theory is out of scope.
- **first-order**: the analogous `derivability_fol` equivalence holds (ND with
  eigenvariable conditions ⟺ Hilbert with generalisation); it is a separate
  edge into `derivability_fol`.

## Hypothesis-dropped counterexamples
- **drop the deduction theorem** (i.e. try to prove ⟹ directly): the `→I` case
  has no route — a Hilbert system *without* the deduction theorem as a
  meta-result cannot simulate discharge, and the naive translation blows up.
  The deduction theorem is not droppable.
- **mismatch the axiom set**: Hilbert with only `P→(Q→P)` and MP proves strictly
  fewer wffs (no `→` distributivity), so the equivalence needs the full schema
  list.
- **infinite `Γ`**: the statement still holds, but "finite" is the case that
  matters for `compactness_prop` (a derivation uses finitely many premises
  regardless).

## Common misuse
Assuming a metatheorem proved for one calculus must be re-proved for the other;
treating Fitch-style and Gentzen-tree ND as different systems (same object,
different notation); forgetting that the *classical* rule (`raa_rule` /
contraposition axiom) is what makes them classical — dropping it on one side
only breaks the equivalence.

## Related nodes (non-prerequisite)
- `equivalent_to`: `nd_derivation` ↔ `hilbert_derivation` (this lemma *is* that
  relation, made a proved node).
- `mentioned_alternative`: sequent calculus, semantic tableaux.
- `enables`: every downstream `⊢` statement (`soundness_prop`,
  `post_completeness_theorem`, `derived_rules`, …) to be read calculus-free.

## Sources
[mendelson_6e] ch. 1 (Hilbert + deduction theorem); [vandalen_5e] ch. 2 (ND);
[enderton_logic_2e] §2.4.
