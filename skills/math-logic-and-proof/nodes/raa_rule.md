# raa_rule

## Type
definition  (epistemic status: `definition`; `constructive_grade: needs_DNE`)

## Statement
**Reductio ad absurdum** (the classical rule): from a sub-derivation of `⊥`
under the assumption `¬φ`, conclude `φ` (discharging `¬φ`).

    [¬φ]¹
      ⋮
      ⊥
    ─────  RAA, discharging ¹
      φ

This is the rule that makes propositional natural deduction **classical**.

## Symbols
- `φ`: the goal (a **positive** wff — see the `¬I` contrast).
- `[¬φ]`: the discharged assumption.

## Prerequisites (tsort edges into this node)
`nd_derivation`, `true_false_constants`, `double_negation`.

## Content — RAA vs `¬I`
Two distinct rules easily conflated:
- **`¬I`** (intuitionistic): `[φ]…⊥ ⟹ ¬φ`. To prove a **negation**. Always
  available; it is `→I` for `φ → ⊥`.
- **`RAA`** (classical): `[¬φ]…⊥ ⟹ φ`. To prove a **positive** goal by refuting
  its negation. `needs_DNE`.

`RAA` is interderivable with `double_negation` elimination (`¬¬φ → φ`), with
excluded middle, and with Peirce's law — adding any one to intuitionistic ND
gives classical ND (`edges/relations.tsv`: `raa_rule equivalent_to
double_negation`).

## Constructive grade
`needs_DNE`. `RAA` extracts positive content (`φ`) from a purely negative
hypothesis (`¬φ` leads to absurdity) — the move BHK semantics does not license.
An `RAA` proof of `∃x ψ` yields **no witness**.

## Lean status
`lean_status: core`. `Deriv.raa : Deriv (Wff.neg p :: Γ) Wff.fls → Deriv Γ p` in
`validation/proof-checks.lean`; its soundness (the `raa` case of `soundness`) is
where the metatheory does a classical `Bool` case-split. `dne` (=
`Classical.byContradiction ∘ …`) is the term-level counterpart; `#print axioms`
shows `Classical.choice`.

## Type / well-formedness check
`well_formed`. The discharged assumption must be **exactly** `¬φ` for the `φ`
concluded — discharging `¬φ'` gives `φ'`. The sub-derivation must actually reach
`⊥` (or a `γ ∧ ¬γ`); a sub-derivation that never uses `¬φ` signals a hidden
direct proof.

## Specialization / boundary cases
- goal `φ = ¬ψ`: `RAA` assumes `¬¬ψ`, derives `⊥`, concludes `¬ψ` — this is
  intuitionistically equivalent to `¬I` on `¬ψ` (proving a negation by
  contradiction is fine). So `RAA` is "really" classical only for **positive**
  goals.
- `φ` decidable: `RAA` is eliminable (case on `φ ∨ ¬φ`).
- Euclid's infinitude of primes, irrationality of `√2`, Cantor's diagonal — the
  classic genuine uses (each also has a direct rephrasing).

## Hypothesis-dropped counterexamples
- **drop `RAA` from ND**: `¬¬φ → φ`, `φ ∨ ¬φ`, Peirce's law
  `((φ → ψ) → φ) → φ`, and the classical direction of `de_morgan_prop` /
  `implication_as_disjunction` / `contraposition` all become underivable.
- **`RAA` for `∃x ψ`**: derivable classically, but yields no term — rejected in
  constructive foundations.

## Common misuse
Using `RAA` where `¬I` (constructive) suffices; discharging the wrong
assumption; a "reductio" that never uses `¬φ` (a disguised direct proof);
concluding `∃`-statements by `RAA` then speaking of "the" object; conflating
`RAA` with `¬E` (`φ, ¬φ ⟹ ⊥`, which is intuitionistic).

## Related nodes (non-prerequisite)
- `equivalent_to`: `double_negation` (over intuitionistic ND); excluded middle;
  Peirce's law.
- `is`: the classical rule of `nd_rules_propositional`.
- `feeds`: `proof_by_contradiction`, `derived_rules`.
- `contrast_with`: `¬I` (intuitionistic); intuitionistic logic
  (`edges/relations.tsv`).

## Sources
[vandalen_5e] §2.3 (the RAA/¬I distinction); [chiswell_hodges] ch. 4;
[enderton_logic_2e] §2.4.
