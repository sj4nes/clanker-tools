# hilbert_system_prop

## Type
definition  (epistemic status: `definition`; `constructive_grade: needs_DNE`
as shipped — the third schema is classical)

## Statement
A **Hilbert (axiomatic) calculus** for classical propositional logic:
**axiom schemas**
1. `φ → (ψ → φ)`
2. `(φ → (ψ → χ)) → ((φ → ψ) → (φ → χ))`
3. `(¬ψ → ¬φ) → (φ → ψ)`   *(classical; the intuitionistic version replaces
   this with `⊥`-axioms and adds `∧`/`∨` schemas)*

and the single **rule** modus ponens (`modus_ponens`). All connectives beyond
`¬`, `→` are defined (`∧`, `∨`, `↔` via `implication_as_disjunction`,
`de_morgan_prop`, `biconditional_as_conjunction`).

## Symbols
- `φ`, `ψ`, `χ`: wffs (schema instances).

## Prerequisites (tsort edges into this node)
`wff_syntax`, `modus_ponens`.

## Content
This capsule's **secondary calculus** (ND is primary). Its virtues: a *tiny*
rule set (one rule), which makes **induction on derivations** short; the
**deduction theorem** (`deduction_theorem`) is a genuine metatheorem here (there
is no discharge rule to make it trivial). `nd_hilbert_equivalence` proves it
derives exactly the same wffs as `nd_derivation`, so no downstream result
depends on the choice.

Many equivalent axiomatisations exist (Łukasiewicz's 3 axioms with a single
schema, Frege's, Mendelson's, Hilbert–Ackermann's) — this is Mendelson's `¬`/`→`
set.

## Constructive grade
`needs_DNE` **as shipped** — schema 3 (`(¬ψ → ¬φ) → (φ → ψ)`) is
`contraposition`'s classical direction and yields `¬¬φ → φ`. The
**intuitionistic** Hilbert calculus drops schema 3, keeps 1–2, and adds
`φ → (ψ → φ ∧ ψ)`, `φ ∧ ψ → φ`, …, `⊥ → φ` — then it coincides with
intuitionistic ND.

## Lean status
`lean_status: core` (the `→`-fragment). `validation/proof-checks.lean`
`inductive H` has `k`, `s` (schemas 1, 2) and `mp`; `H.self` proves
`⊢ φ → φ` from them; the `deduction` theorem is proved by induction on `H`.
Schema 3 and the classical round-trip with `Deriv` are **not** in the file.

## Type / well-formedness check
`well_formed`. Each schema is a **template** — every substitution instance is an
axiom (infinitely many). A Hilbert derivation (`hilbert_derivation`) must cite
the *instance*, not the schema. Same language throughout.

## Specialization / boundary cases
- `Γ = ∅`, schemas 1–2 + MP: exactly the theorems of the `{→}`-fragment of
  **intuitionistic** logic (the "positive implicational calculus" is 1–2; adding
  Peirce's law `((φ→ψ)→φ)→φ` gives the classical `{→}`-fragment).
- adding schema 3 (or Peirce, or `¬¬φ → φ` as a schema): full classical
  propositional logic.
- **combinatory logic**: schemas 1, 2 are the types of the **K** and **S**
  combinators — Curry–Howard for the axiomatic style.

## Hypothesis-dropped counterexamples
- **schema 2 dropped**: the deduction theorem fails — its MP case needs exactly
  schema 2 (`deduction_theorem` counterexample note).
- **schema 1 dropped**: cannot even prove `φ → φ`.
- **only schema 1 + MP**: proves `φ → φ`? no — needs 2. Proves very little.
- **MP dropped**: only axiom instances are derivable; no `φ → φ` for atomic
  `φ` beyond instances.

## Common misuse
Citing a schema instead of its instance in a derivation; assuming the deduction
theorem is "obvious" here (it is the substantive metatheorem); thinking a
different axiomatisation is a different logic (they are equivalent); using the
classical schema 3 when an intuitionistic result is wanted.

## Related nodes (non-prerequisite)
- `equivalent_to` (extensionally): `nd_rules_propositional` /
  `nd_derivation` (`nd_hilbert_equivalence`).
- `builds`: `hilbert_derivation`.
- `needs`: `deduction_theorem` (to be usable in practice).
- `curry_howard`: **K**, **S** combinators.
- `mentioned_alternative`: Łukasiewicz / Frege / Hilbert–Ackermann
  axiomatisations.

## Sources
[mendelson_6e] ch. 1; [enderton_logic_2e] §2.4; [shoenfield] ch. 2;
[chiswell_hodges] §3.2.
