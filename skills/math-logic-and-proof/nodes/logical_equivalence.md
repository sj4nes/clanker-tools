# logical_equivalence

## Type
definition  (epistemic status: `definition`; `constructive_grade: intuitionistic`
as a definition)

## Statement
Two wffs `φ`, `ψ` are **logically equivalent**, `φ ⊨⊨ ψ` (also `φ ≡ ψ`), iff
they have the same truth value under every assignment: `∀v, ⟦φ⟧_v = ⟦ψ⟧_v`.
Equivalently `φ ⊨ ψ` **and** `ψ ⊨ φ`; equivalently `⊨ (φ ↔ ψ)`.

## Symbols
- `φ`, `ψ`: wffs (over the union of their atom sets).
- `⊨⊨` / `≡`: the equivalence relation on wffs.

## Prerequisites (tsort edges into this node)
`semantic_consequence`, `satisfaction`.

## Content
An **equivalence relation** on `Wff` (reflexive, symmetric, transitive); the
quotient `Wff / ⊨⊨` is the **Lindenbaum–Tarski Boolean algebra** of the
language. It is a **congruence** for the connectives (`substitution_of_equivalents`):
`φ ≡ φ'` ⟹ `¬φ ≡ ¬φ'`, `φ ∧ ψ ≡ φ' ∧ ψ`, etc. — so you may rewrite a subformula
by an equivalent one anywhere.

The entire `prop_laws` catalogue (`double_negation`, `de_morgan_prop`,
`distributivity_prop`, …) consists of instances of `⊨⊨`.

Not to be confused with the meta-level `⊨` between `Γ` and `φ`, nor with the
object connective `↔` — though `φ ≡ ψ` iff `⊨ (φ ↔ ψ)`.

## Constructive grade
`intuitionistic` as a definition. A given equivalence may be `needs_LEM` /
`needs_DNE` to establish (the `prop_laws` split nodes) — but that is about the
*proof of the equivalence*, not the relation itself.

## Lean status
`lean_status: core`. `validation/proof-checks.lean`:
`Wff.Equiv a b := ∀ v, eval v a = eval v b`, with `equiv_refl`, `equiv_symm`,
`equiv_trans` and the connective congruences `equiv_neg`, `equiv_conj`,
`equiv_disj`, `equiv_impl` — the substance of `substitution_of_equivalents`.
The `Prop`-level catalogue lemmas (`not_or_iff`, `impl_iff_or`, …) are the
schematic versions.

## Type / well-formedness check
`well_formed`. `∀v` ranges over assignments to `atoms(φ) ∪ atoms(ψ)` — comparing
over only one formula's atoms can give a false "equivalence" (e.g. `p` vs
`p ∧ (q ∨ ¬q)` are equivalent, but only when `q` is in the assignment domain).
`⊨⊨` is a metastatement, not a wff.

## Specialization / boundary cases
- `φ ≡ φ` always.
- all tautologies are mutually equivalent (to `⊤`); all contradictions to `⊥`.
- `φ ≡ ψ` iff `¬φ ≡ ¬ψ` (congruence).
- equivalence classes = elements of the free Boolean algebra on the atoms
  (finitely many atoms ⟹ finitely many classes: `2^(2ⁿ)`).
- **substitution instances**: `φ ≡ ψ` schematic ⟹ every substitution instance
  is an equivalence.

## Hypothesis-dropped counterexamples
- **compare over mismatched atom sets**: `p` and `p ∨ (q ∧ ¬q)` "look" equal on
  `{p}` but the comparison must include `q`.
- **confuse `⊨⊨` with `↔`**: `φ ↔ ψ` is a wff that can be true under some `v` and
  false under others; `φ ≡ ψ` says the biconditional is a *tautology*.
- **rewrite inside a non-truth-functional context**: substitution of equivalents
  **fails** inside quotation, provability, or modal operators (`□φ` vs `□ψ` for
  `φ ≡ ψ` — not valid). Classical propositional logic has no such contexts, so
  it is always safe *here*.

## Common misuse
Treating `⊨⊨` as the object connective `↔`; comparing over one formula's atoms;
assuming an equivalence proved classically is constructively usable as a rewrite
in an intuitionistic proof; rewriting inside opaque contexts.

## Related nodes (non-prerequisite)
- `is_a`: equivalence relation / congruence on `Wff`.
- `quotient_gives`: the Lindenbaum–Tarski Boolean algebra.
- `instances`: the entire `prop_laws` block.
- `enables`: `substitution_of_equivalents`, `duality_principle`,
  normal-form theorems.

## Sources
[enderton_logic_2e] §1.2; [vandalen_5e] §1.2; [chiswell_hodges] §2.4;
[halmos_boolean] (the algebra).
