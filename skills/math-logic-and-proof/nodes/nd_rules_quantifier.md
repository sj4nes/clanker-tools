# nd_rules_quantifier

## Type
definition  (epistemic status: `definition`; `constructive_grade: intuitionistic`
— the rules are minimal-logic)

## Statement
The natural-deduction rules for `∀` and `∃`:

| rule | form | side condition |
|---|---|---|
| `∀I` | from `φ[y/x]` infer `∀x φ` | `y` **fresh** (`eigenvariable_condition`) |
| `∀E` | from `∀x φ` infer `φ[t/x]` | `t` **free for `x`** in `φ` (`free_for`) |
| `∃I` | from `φ[t/x]` infer `∃x φ` | `t` **free for `x`** in `φ` |
| `∃E` | from `∃x φ` and `[φ[y/x]] … ψ` infer `ψ` | `y` **fresh**; `y ∉ FV(ψ)` |

## Symbols
- `x`: bound variable; `y`: eigenvariable; `t`: a term.

## Prerequisites (tsort edges into this node)
`nd_rules_propositional`, `quantifier_syntax`, `substitution`, `free_for`,
`eigenvariable_condition`.

## Content
Extends `nd_rules_propositional` to first-order logic. The pairing:
`∀I` = "let `y` be arbitrary"; `∀E` = "instantiate"; `∃I` = "exhibit a witness"
(`existence_proof`, constructive branch); `∃E` = "choose a witness and reason
about it". The **two side conditions** — `free_for` (for the term rules) and
`eigenvariable_condition` (for the fresh-variable rules) — are exactly what
`soundness_fol` needs; dropping either breaks soundness.

## Constructive grade
`intuitionistic` — all four rules are rules of intuitionistic (indeed minimal)
predicate logic. Classicality enters only via `raa_rule` (propositional) and the
`quantifier_negation` law, not these rules.

## Lean status
`lean_status: cited`. Mathlib's proof system / Lean's own `intro` (`∀I`),
`⟨t, _⟩` (`∃I`), `apply`/`specialize` (`∀E`), `obtain ⟨y, hy⟩` (`∃E`) realise
them; `intro`/`obtain` enforce the eigenvariable condition by fresh-local
scoping. Not in `validation/proof-checks.lean` (propositional).

## Type / well-formedness check
`well_formed` per use: `∀E`/`∃I` require the `free_for` check (or
`alpha_equivalence` first); `∀I`/`∃E` require the freshness check on `y` against
the conclusion and open assumptions. `∃E` additionally: `y ∉ FV(ψ)`.

## Specialization / boundary cases
- `∀E` with `t = x`: `∀x φ ⊢ φ` (drop the quantifier).
- `∃I` from `φ[c/x]` for a constant `c`: `free_for` automatic.
- nested `∀I`: prove `φ(y, z)` for fresh `y, z`, conclude `∀x ∀w φ`.
- the **prenex** manipulations and the quantifier laws are *derived* from these
  rules + the propositional ones.

## Hypothesis-dropped counterexamples
- **`∀I` without freshness**: `{P(y)} ⊢ ∀x P(x)` — unsound.
- **`∀E` without `free_for`**: `∀x ∃y (y ≠ x) ⊢ ∃y (y ≠ y)` — valid premise,
  contradictory conclusion.
- **`∃E` letting `y` into `ψ`**: from `∃x P(x)` "conclude" `P(y)`.
- **`∃I` without `free_for`**: dually to `∀E`.

## Common misuse
Skipping either side condition; instantiating `∀E` with a term that captures;
generalising a constrained variable; letting the `∃E` witness leak; treating
`∃E` as "so let `y` be the object" (it is, but `y` cannot appear in the final
claim).

## Related nodes (non-prerequisite)
- `extends`: `nd_rules_propositional`.
- `requires`: `free_for`, `eigenvariable_condition`.
- `feeds`: `derivability_fol`, `soundness_fol`, `existence_proof`,
  `disproof_by_counterexample`.
- `hilbert_counterpart`: `hilbert_quantifier_axioms`.

## Sources
[vandalen_5e] ch. 3; [chiswell_hodges] ch. 4; [enderton_logic_2e] §2.4;
Prawitz (1965).
