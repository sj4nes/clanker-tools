# explosion_ex_falso

## Type
theorem  (epistemic status: `proved_theorem`; `constructive_grade: intuitionistic`)

## Statement
**Ex falso quodlibet** (`⊥E`, the principle of explosion): from `⊥`, derive any
wff `φ`. Equivalently `⊥ ⊨ φ` for every `φ`; equivalently `¬φ, φ ⊢ ψ` for every
`ψ`.

## Symbols
- `φ`: an arbitrary wff (the conclusion).

## Prerequisites (tsort edges into this node)
`true_false_constants`, `nd_rules_propositional`.

## Content
`⊥E` is a **primitive rule** of full and intuitionistic natural deduction (it is
what separates **intuitionistic** logic from **minimal** logic, which lacks it).
Semantically trivial: no assignment satisfies `⊥`, so `⊥ ⊨ φ` **vacuously**
(`semantic_consequence`). Proof-theoretically it is the statement that an
inconsistent theory is trivial — `Γ ⊢ ⊥ ⟹ Γ ⊢ φ` for all `φ` (`consistency`).

## Constructive grade
`intuitionistic` — accepted by Brouwer/Heyting: a proof of `⊥` is impossible, so
the rule is never actually invoked on a closed proof; it lets you *locally*
finish a case that has been shown absurd. **Minimal logic** (Johansson) rejects
it; **relevance logic** rejects it (as an irrelevant inference). Classical logic
has it (and `RAA` on top).

## Lean status
`lean_status: core`. `Deriv.falseE : Deriv Γ Wff.fls → Deriv Γ p` is a
constructor in `validation/proof-checks.lean`; `Deriv.explosion` is its named
form; the `falseE` case of `soundness` closes by `Bool.noConfusion` on
`false = true`. In Lean's own logic it is `False.elim` / `absurd`.

## Type / well-formedness check
`well_formed`. `φ` is genuinely arbitrary — no constraint. The premise must be
an actually-derived `⊥` (or `γ ∧ ¬γ` with `γ` derived), not an assumed one left
open.

## Specialization / boundary cases
- `φ = ⊥`: trivial (`⊥ ⊢ ⊥`).
- inside a `proof_by_cases`: a case shown contradictory is closed by `⊥E` to the
  common goal.
- `¬φ, φ ⊢ ⊥` (`¬E`) then `⊥E` to any `ψ`: the standard "from a contradiction,
  anything".
- **paraconsistent logics** (LP, relevance): drop `⊥E` precisely so that
  `{φ, ¬φ}` does not entail everything — out of scope, noted as the boundary.

## Hypothesis-dropped counterexamples
- **minimal logic** (no `⊥E`): `⊥ → φ` is **not** derivable for `φ` other than
  `⊥` and negations; `{p, ¬p} ⊬ q`. This is the exact content of dropping the
  rule.
- **relevance logic**: `p ∧ ¬p ⊬ q` (no shared propositional variable ⟹ no
  entailment).
- the rule cannot be dropped from **classical** logic while keeping `RAA` and
  soundness — `RAA` + `¬E` already give explosion.

## Common misuse
Believing explosion is a *classical* principle (it is intuitionistic; `RAA` is
the classical one); using it from an **assumed** `⊥` without having derived the
contradiction; expecting it in a paraconsistent setting; reading `⊥ ⊨ φ` as
saying something about `φ` (it says something about `⊥`).

## Related nodes (non-prerequisite)
- `is`: the `⊥E` rule of `nd_rules_propositional`.
- `separates`: intuitionistic logic from minimal logic.
- `feeds`: `consistency` ("inconsistent ⟹ trivial"), the `p = ⊥` case of
  `implication_as_disjunction` / `vacuous_trivial_proof`.
- `rejected_by`: minimal, relevance, paraconsistent logics (out of scope).

## Sources
[vandalen_5e] §2.3, ch. 5; [chiswell_hodges] ch. 4;
Johansson (1937) (minimal logic); Priest, *In Contradiction* (paraconsistency).
