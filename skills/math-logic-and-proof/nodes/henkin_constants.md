# henkin_constants

## Type
construction  (epistemic status: `constructive_result`; `constructive_grade:
needs_LEM` — inherits from the consistency checks, but the language extension
itself is effective)

## Statement
Given a consistent `ℒ`-theory `T`, extend the language and theory so that every
existential claim has a **named witness**. For each `ℒ`-formula `φ(x)` with one
free variable, introduce a fresh constant symbol `c_φ` and the **Henkin axiom**

    (∃x φ(x)) → φ(c_φ / x).

Iterate: `ℒ = ℒ₀ ⊆ ℒ₁ ⊆ …`, `ℒₙ₊₁` adds a witness constant for every
`ℒₙ`-formula; `ℒ⁺ = ⋃ₙ ℒₙ`. Let `T⁺ = T ∪ {all Henkin axioms}` over `ℒ⁺`.

## Symbols
- `φ(x)`: an `ℒₙ`-formula, `x` its sole free variable.
- `c_φ`: a constant symbol not in `ℒₙ` (a `naive_collection` of them, one per
  formula — countably many if `ℒ` is countable).
- `T⁺`: the extended theory in `ℒ⁺`.

## Prerequisites (tsort edges into this node)
`signature`, `consistency_fol`, `metatheoretic_induction`, `derivability_fol`.

## Key lemma: the extension is conservative, so `T⁺` stays consistent
Adding one Henkin axiom `(∃x φ) → φ(c/x)` for a **fresh** `c` to a consistent
theory keeps it consistent: a derivation of `⊥` from `T ∪ {(∃x φ) → φ(c/x)}`
could be turned into one from `T` alone by generalising `c` back to a variable
(`c` fresh ⇒ eigenvariable condition holds) and using `∃E`. Iterate over the
`ω`-chain (`metatheoretic_induction`): each `Tₙ` consistent ⇒ `Tₙ₊₁` consistent
⇒ `T⁺ = ⋃ Tₙ` consistent (finite character).

## Why the `ω`-chain (not one round)
Adding constants creates **new** formulas `φ(x)` (now mentioning the new
constants) that also need witnesses — hence the iteration. After `ω` steps every
`ℒ⁺`-formula was an `ℒₙ`-formula for some `n` and got its constant at stage
`n+1`.

## Constructive grade
The language construction is **effective** (given an enumeration of formulas).
The consistency *proof* at each stage uses `needs_LEM` (via the Lindenbaum-style
reasoning it feeds into) — but the conservativity lemma above is itself
proof-theoretic and constructive. Graded `needs_LEM` for its role in the
completeness proof.

## Lean status
`lean_status: cited`. Mathlib's `FirstOrder.Language.language.withConstants` /
the `Henkinization` in its completeness development is the reference. Not built
in `validation/proof-checks.lean`.

## Type / well-formedness check
`well_formed`. Each `c_φ` must be **genuinely fresh** at its stage (not already
in `ℒₙ`); `φ(c_φ / x)` requires `c_φ` **free for `x`** in `φ` — automatic since
`c_φ` is a constant (no variables to capture), but the check is recorded
(`free_for`). The union `ℒ⁺` is a legitimate signature (countable union of
countable signatures is countable, when `ℒ` is).

## Specialization / boundary cases
- `ℒ` already has a witness for every existential (a **Henkin language**): the
  construction is idempotent, `T⁺ ≈ T`.
- `ℒ` countable ⇒ `ℒ⁺` countable ⇒ the eventual term model is countable
  (`lowenheim_skolem_down`).
- only sentences `∃x φ` with `φ` having exactly one free variable need
  witnesses; closed instances and multi-variable cases are handled by nesting.

## Hypothesis-dropped counterexamples
- **`c` not fresh**: adding `(∃x x≠d) → (d ≠ d)` for an **existing** constant
  `d` is inconsistent with `∃x x≠d` in any model with ≥ 2 elements — freshness
  is essential to conservativity.
- **stop after finitely many stages**: some `ℒ⁺`-existential still lacks a
  witness, and `henkin_theory` (hence `truth_lemma_fol`) fails at its `∃`
  clause.
- **drop consistency of `T`**: nothing to extend.

## Common misuse
Reusing a constant as a witness for two different formulas without checking
consistency; thinking one round of witness-adding suffices; treating `c_φ` as
denoting a *specific* pre-existing object rather than a formal symbol; forgetting
the Henkin axioms are added to `T`, not just the constants.

## Related nodes (non-prerequisite)
- `feeds`: `henkin_theory` (then Lindenbaum), `term_model`.
- `related`: Skolem functions / Skolemisation (a second-order-flavoured
  alternative; `henkin_constants` is the first-order, choice-free-in-the-
  countable-case route).
- `used_by`: `godel_completeness_theorem`.

## Sources
[enderton_logic_2e] §2.5 (the "add witnesses" step); [chiswell_hodges] §5.3;
Henkin, *The completeness of the first-order functional calculus* (1949).
