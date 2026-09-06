# modus_ponens

## Type
definition  (epistemic status: `definition`; `constructive_grade: intuitionistic`)

## Statement
The inference rule **modus ponens** (`→E`, detachment): from `φ` and `φ → ψ`,
infer `ψ`.

    φ      φ → ψ
    ───────────────  (MP)
          ψ

## Symbols
- `φ`, `ψ`: wffs.

## Prerequisites (tsort edges into this node)
`wff_syntax`.

## Content
The one non-axiom rule of the Hilbert calculus (`hilbert_system_prop`): a
Hilbert derivation is a sequence in which each line is an axiom instance or
follows from two earlier lines by MP. In natural deduction it is the
**elimination rule for `→`** (`impE` in `nd_rules_propositional`). It is
**truth-preserving** (`soundness_prop`): if `v ⊨ φ` and `v ⊨ φ → ψ` then
`⟦φ → ψ⟧_v = T` forces `⟦ψ⟧_v = T`.

## Constructive grade
`intuitionistic` — `→E` is a rule of minimal logic; it is function application
under Curry–Howard (`(φ → ψ) applied to a proof of φ`).

## Lean status
`lean_status: core`. `Deriv.impE` in `validation/proof-checks.lean` is exactly
MP; `H.mp` is the Hilbert version. Its soundness is the `impE` case of the
`soundness` theorem. In Lean's own logic, MP is `h₁ h₂` (application).

## Type / well-formedness check
`well_formed`. The minor premise must be **exactly** the antecedent `φ` of the
major premise `φ → ψ` — not a variant, not `φ'` with `φ ≡ φ'` (unless you first
rewrite by `substitution_of_equivalents`). Both premises and the conclusion in
one language.

## Specialization / boundary cases
- iterated: `φ`, `φ → (ψ → χ)`, `ψ` ⊢ `χ` (MP twice).
- with the deduction theorem: `Γ, φ ⊢ ψ` ⟺ `Γ ⊢ φ → ψ` — MP is the "⟸"
  direction (`deduction_theorem`).
- `ψ = ⊥`: from `φ` and `φ → ⊥` (= `¬φ`) infer `⊥` — this is `¬E`.

## Hypothesis-dropped counterexamples
- **affirming the consequent** (`ψ`, `φ → ψ` ⊢ `φ`): invalid — `ψ = T`,
  `φ = F` satisfies both premises, not the "conclusion".
- **denying the antecedent** (`¬φ`, `φ → ψ` ⊢ `¬ψ`): invalid, same countermodel
  idea.
- **minor premise not the antecedent**: `φ'`, `φ → ψ` ⊢ `ψ` fails when
  `φ' ≠ φ`.

## Common misuse
Affirming the consequent / denying the antecedent (the two classic fallacies);
detaching on a premise that only *resembles* the antecedent; treating MP as
introducing `→` (that is `→I` / `assumption_discharge`).

## Related nodes (non-prerequisite)
- `is`: the `→E` rule of `nd_rules_propositional` / `impE` of `nd_derivation`.
- `paired_with`: `assumption_discharge` (`→I`).
- `feeds`: `hilbert_system_prop`, `deduction_theorem`, `derived_rules`.
- `related`: Curry–Howard (application); the "MP + generalisation" rule set of
  `hilbert_quantifier_axioms`.

## Sources
[mendelson_6e] ch. 1; [enderton_logic_2e] §2.4; [vandalen_5e] ch. 2.
