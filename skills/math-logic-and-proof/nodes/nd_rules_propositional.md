# nd_rules_propositional

## Type
definition  (epistemic status: `definition`; `constructive_grade: split` —
the intro/elim rules are `intuitionistic`, the classical rule `RAA` is
`needs_DNE`)

## Statement
The inference rules of propositional **natural deduction**: for each connective
an **introduction** rule (how to conclude a formula with that connective as
principal) and an **elimination** rule (how to use one), plus `⊥`-elimination
and the classical rule.

| connective | introduction | elimination |
|---|---|---|
| `∧` | `φ, ψ ⟹ φ ∧ ψ` | `φ ∧ ψ ⟹ φ` ; `φ ∧ ψ ⟹ ψ` |
| `∨` | `φ ⟹ φ ∨ ψ` ; `ψ ⟹ φ ∨ ψ` | `φ ∨ ψ`, `[φ]…χ`, `[ψ]…χ ⟹ χ` |
| `→` | `[φ]…ψ ⟹ φ → ψ`  (discharge `φ`) | `φ, φ → ψ ⟹ ψ`  (MP) |
| `¬` | `[φ]…⊥ ⟹ ¬φ` | `φ, ¬φ ⟹ ⊥` |
| `⊥` | — | `⊥ ⟹ φ`  (ex falso) |
| classical | — | `[¬φ]…⊥ ⟹ φ`  (`RAA`) |

`↔` is treated via `biconditional_as_conjunction`. `[φ]` marks a **discharged
assumption** (`assumption_discharge`).

## Symbols
- `φ`, `ψ`, `χ`: wffs.
- `[φ]…χ`: a sub-derivation of `χ` under the temporary assumption `φ`.

## Prerequisites (tsort edges into this node)
`wff_syntax`.

## Content
Natural deduction is this capsule's **primary calculus** (the "ND primary"
decision). Its rules pair with the connective meanings: `→I` internalises the
deduction theorem as a rule; `∨E` is `proof_by_cases`; `RAA` is
`proof_by_contradiction`. Dropping `RAA` (and `⊥E`? no — `⊥E` stays) gives
**intuitionistic** ND; dropping `⊥E` too gives **minimal** logic.

## Constructive grade
`split`. All intro/elim rules and `⊥E` are **`intuitionistic`**. `RAA`
(equivalently `¬¬φ → φ`) is the sole **`needs_DNE`** rule and is what makes the
calculus classical. Per-rule grade is what lets the constructive grade of every
downstream law be read off.

## Lean status
`lean_status: core` (a representative fragment). `validation/proof-checks.lean`
`inductive Deriv` has `ax`, `impI` (`→I`), `impE` (`→E`/MP), `andI`, `andEl`,
`andEr`, `falseE` (`⊥E`), `raa` (`RAA`). The `∨` rules and `¬I` are omitted (they
add nothing to the `soundness` argument, which inducts over these constructors).

## Type / well-formedness check
`well_formed`. Each rule schema must be instantiated with wffs of one language;
a discharge (`→I`, `∨E`, `¬I`, `RAA`) must close **exactly** the marked
assumption; an elimination's major premise must have the right principal
connective. The eigenvariable conditions are a **first-order** matter
(`nd_rules_quantifier`) — none here.

## Specialization / boundary cases
- intuitionistic fragment: drop `RAA`; `⊥E` stays; `¬¬φ → φ` and `φ ∨ ¬φ` no
  longer derivable.
- minimal fragment: drop `RAA` and `⊥E`; even `⊥ → φ` fails.
- the `∧`, `→` fragment alone: the "implicational–conjunctive" calculus,
  Curry–Howard-corresponds to simply-typed λ-calculus with products.
- **normalisation**: every ND derivation reduces to a normal form (no
  introduction immediately followed by its elimination) — the proof-theoretic
  analogue of cut elimination, out of scope.

## Hypothesis-dropped counterexamples
- **drop `→I` (discharge)**: cannot prove `φ → φ` or any `→`-conclusion from no
  premises — the calculus loses all conditional reasoning.
- **`∨E` without discharging in both branches**: unsound (you could smuggle an
  undischarged assumption).
- **`RAA` with the wrong assumption discharged**: discharging `¬φ'` "proves"
  `φ'`, not `φ`.
- **add an unsound rule** (`φ ∨ ψ ⟹ φ`): breaks `soundness_prop`.

## Common misuse
Forgetting to discharge in `→I`/`∨E`/`RAA`; using `RAA` where `¬I` (constructive)
suffices; treating `⊥E` as classical (it is intuitionistic); confusing `¬E`
(`φ, ¬φ ⟹ ⊥`, intuitionistic) with `RAA`.

## Related nodes (non-prerequisite)
- `builds`: `nd_derivation`.
- `contains`: `modus_ponens` (`→E`), `assumption_discharge` (`→I`),
  `raa_rule`, `explosion_ex_falso` (`⊥E`).
- `equivalent_to` (extensionally): `hilbert_system_prop` (`nd_hilbert_equivalence`).
- `mentioned_alternative`: sequent calculus `LK`/`LJ`.

## Sources
[vandalen_5e] ch. 2; [chiswell_hodges] ch. 4; [enderton_logic_2e] §2.4;
Prawitz, *Natural Deduction* (1965).
