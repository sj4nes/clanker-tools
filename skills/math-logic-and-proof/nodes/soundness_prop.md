# soundness_prop

## Type
metatheorem  (epistemic status: `metatheorem`; `constructive_grade: needs_DNE`
— the `RAA` case; the rest is intuitionistic)

## Statement
If `Γ ⊢ φ` (propositional) then `Γ ⊨ φ`: every derivable consequence is a
semantic consequence. Contrapositive: a wff with a countermodel is not
derivable. Corollary: a **satisfiable** set is **consistent**.

## Symbols
- `Γ`: a set of wffs; `φ`: a wff.

## Prerequisites (tsort edges into this node)
`derivability`, `semantic_consequence`, `nd_rules_propositional`,
`structural_induction_wff`.

## Proof
Induction on the derivation (`structural_induction_wff` applied to the
`nd_derivation` inductive type — "rule induction"). Show each rule **preserves**
the property "every assignment satisfying the open assumptions satisfies the
conclusion":
- `ax`: trivial; `→I`: discharges an assumption, handled by the `→` truth
  clause; `→E` (MP): from `⟦φ⟧_v = T` and `⟦φ → ψ⟧_v = T`; `∧I`/`∧E`: the `∧`
  clause; `⊥E`: vacuous (no `v` satisfies `⊥`); `RAA`: if every `v` satisfying
  `Γ, ¬φ` yields a contradiction then every `v` satisfying `Γ` satisfies `φ`
  (**classical** metatheory step).

## Constructive grade
`needs_DNE` — the `RAA` case uses double-negation elimination in the metatheory,
matching the classical object rule. Soundness of the **intuitionistic** fragment
(drop `RAA`) is fully constructive.

## Lean status
`lean_status: core`. `validation/proof-checks.lean`:
`theorem soundness {Γ p} (d : Deriv Γ p) : Entails Γ p := by induction d with …`
— genuine, universal, `#print axioms soundness` → `[propext]` only. Every rule
case (`ax`, `impI`, `impE`, `andI`, `andEl`, `andEr`, `falseE`, `raa`) is
discharged.

## Type / well-formedness check
`well_formed`. `Γ`, `φ` one language; `Entails Γ φ := ∀ v, (v ⊨ Γ) → v ⊨ φ`.
The induction is over the **derivation**, not the formula.

## Specialization / boundary cases
- `Γ = ∅`: `⊢ φ` ⟹ `φ` is a `tautology`.
- **contrapositive** — a formula with a countermodel is **not a theorem**: how
  you prove unprovability (`p → q` is not a theorem; `p = T, q = F`).
- `φ = ⊥`: `Γ ⊢ ⊥` ⟹ `Γ` unsatisfiable, i.e. **satisfiable ⟹ consistent**.

## Hypothesis-dropped counterexamples
- **add an unsound rule** (`φ ∨ ψ ⟹ φ`): then `{p ∨ q} ⊢ p` but `{p ∨ q} ⊭ p`
  (`p = F, q = T`) — soundness fails. Soundness is exactly the guarantee the
  rule set is not like this.
- **misstate a truth clause** (e.g. `⟦φ → ψ⟧_v = T` iff `⟦φ⟧_v = T`): the `→E`
  case breaks.

## Common misuse
Confusing soundness (`⊢ ⟹ ⊨`) with completeness (`⊨ ⟹ ⊢`); assuming soundness
is automatic (it is checked rule by rule); using it to conclude *provability*
(that is completeness); forgetting the `RAA` case is where the metatheory goes
classical.

## Related nodes (non-prerequisite)
- `converse_is`: `post_completeness_theorem`.
- `first_order_twin`: `soundness_fol`.
- `feeds`: `post_completeness_theorem`, `compactness_prop`, and every
  "unprovability" argument.

## Sources
[enderton_logic_2e] §1.7 / §2.5; [vandalen_5e] §1.4; [chiswell_hodges] §2.5.
