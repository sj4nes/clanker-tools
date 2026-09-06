# derived_rules

## Type
proposition  (epistemic status: `proposition`; `constructive_grade` varies
per rule — noted below)

## Statement
Rules that are **not primitive** but **admissible** (adding them derives no new
theorems) or **derivable** (they abbreviate a fixed sub-derivation). Standard
ones:

| rule | form | grade |
|---|---|---|
| modus tollens | `φ → ψ`, `¬ψ ⟹ ¬φ` | `intuitionistic` |
| hypothetical syllogism | `φ → ψ`, `ψ → χ ⟹ φ → χ` | `intuitionistic` |
| disjunctive syllogism | `φ ∨ ψ`, `¬φ ⟹ ψ` | `intuitionistic` (via `∨E` + `⊥E`) |
| **cut** | `Γ ⊢ φ`, `Γ, φ ⊢ ψ ⟹ Γ ⊢ ψ` | `intuitionistic` |
| constructive dilemma | `φ → ψ`, `χ → ρ`, `φ ∨ χ ⟹ ψ ∨ ρ` | `intuitionistic` |
| double-negation intro | `φ ⟹ ¬¬φ` | `intuitionistic` |
| **double-negation elim** | `¬¬φ ⟹ φ` | `needs_DNE` |
| excluded middle | `⟹ φ ∨ ¬φ` | `needs_LEM` |
| Peirce's law | `⟹ ((φ → ψ) → φ) → φ` | `needs_LEM` |

## Symbols
- `φ`, `ψ`, `χ`, `ρ`: wffs; `Γ`: a premise set.

## Prerequisites (tsort edges into this node)
`derivability`, `raa_rule`, `modus_ponens`.

## Content
Derived rules are **conservative** shorthands: each is replaced, in principle,
by its defining sub-derivation. **Admissibility** (the rule can be added without
new theorems) is the precise notion; for a calculus already complete
(`post_completeness_theorem`) every truth-preserving rule is admissible. **Cut**
is the headline example — admissible in ND/Hilbert trivially, and *eliminable*
(Gentzen) in the sequent calculus `LK` with the subformula property as payoff
(out of scope).

## Constructive grade
Per rule (table above). The intuitionistically-derivable ones use only
intro/elim + `⊥E`; DNE / LEM / Peirce require `raa_rule`.

## Lean status
`lean_status: core` (the intuitionistic ones). `validation/proof-checks.lean`:
`Deriv.cut` (`→I` then `→E`), `Deriv.and_comm` (`∧E` twice then `∧I`),
`Deriv.explosion` (`⊥E`). `dni` / `dne` cover the double-negation pair;
`contrapose_weak` is modus tollens' shape. The rules requiring `¬I` (modus
tollens, disjunctive syllogism as *`Deriv`* theorems) are not built — the
fragment omits `¬I` — but their `Prop`-level analogues are in the catalogue.

## Type / well-formedness check
`well_formed` per rule. "Admissible" ≠ "derivable": a rule is **derivable** if a
uniform sub-derivation exists (schematic in the premises), **admissible** if
"whenever the premises are provable, so is the conclusion" — derivable ⟹
admissible, not conversely (e.g. in some weak systems a rule is admissible but
not derivable).

## Specialization / boundary cases
- **cut** in ND: `Deriv.cut` above — one line.
- **cut elimination** (sequent calculus): every `LK` proof reduces to a
  cut-free one; gives consistency and the subformula property. Not in scope.
- modus tollens = `contraposition` (`intuitionistic` half) + MP.
- disjunctive syllogism is **rejected by relevance logic** (it is
  interderivable with explosion given the other rules).

## Hypothesis-dropped counterexamples
- **use DNE / LEM / Peirce in an intuitionistic proof**: not admissible there —
  they are exactly the classical additions.
- **"admissible" assumed to mean "derivable"**: fails in some substructural
  systems.
- **disjunctive syllogism in a paraconsistent logic**: unsound (it would
  restore explosion).

## Common misuse
Treating DNE/LEM/Peirce as "just abbreviations" (they are classical);
conflating admissible with derivable; using cut freely while claiming a
subformula property (that needs cut *elimination*, not just admissibility);
importing relevance-invalid rules into a relevance setting.

## Related nodes (non-prerequisite)
- `derived_from`: `nd_rules_propositional` / `hilbert_system_prop` + primitive
  rules.
- `headline_example`: cut / cut elimination (sequent calculus, out of scope).
- `related`: `contraposition`, `double_negation`, `raa_rule`,
  `proof_by_cases`.

## Sources
[vandalen_5e] ch. 2, ch. 3 (sequent calculus, cut elimination);
[chiswell_hodges] ch. 4; [enderton_logic_2e] §2.4; Gentzen (1935).
