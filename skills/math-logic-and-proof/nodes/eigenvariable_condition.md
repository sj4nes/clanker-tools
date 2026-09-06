# eigenvariable_condition

## Type
hypothesis  (a first-class side condition; `constructive_grade: intuitionistic`)

## Statement
In the rules `∀I` (universal introduction) and `∃E` (existential elimination),
the **eigenvariable** (proper parameter) `y` — the variable generalised or the
fresh witness — must **not occur free** in:
- the conclusion of the rule, and
- any **open assumption** of the sub-derivation.

    ⋮                          [φ[y/x]]ⁱ
    φ[y/x]        (y fresh)       ⋮
    ─────── ∀I                    ψ           ∃x φ
    ∀x φ            ────────────────────────────── ∃E, discharging ¹  (y fresh)
                                  ψ

## Symbols
- `y`: the eigenvariable; `φ`, `ψ`: wffs; `Γ`: the open assumptions.

## Prerequisites (tsort edges into this node)
`free_bound_variables`, `quantifier_syntax`.

## Content
The condition that makes generalisation **sound**: `y` must be *genuinely
arbitrary* — nothing in `Γ` or the goal constrains it — so "`φ` holds of `y`"
really means "`φ` holds of everything". It is stated purely in terms of
`free_bound_variables` (a predicate on occurrences), **independently** of the
rules themselves (`edges/cycles.md` §2). `nd_rules_quantifier` then *requires*
it.

## Constructive grade
`intuitionistic` — a syntactic freshness check; `∀I`/`∃E` with it are minimal-
logic rules.

## Lean status
`lean_status: cited`. In a de Bruijn representation the eigenvariable condition
is automatic (the fresh variable is a new index). Named / Lean's own `∀`-intro
(`intro y`) enforces it by scoping: `y` is a fresh local not appearing in the
hypotheses.

## Type / well-formedness check
`well_formed`. The check is per **use** of the rule: enumerate the free
variables of the conclusion and of every open assumption; `y` must be in
neither. `alpha_equivalence` / choosing a truly fresh `y` always allows the
condition to be met.

## Specialization / boundary cases
- **`∀I`**: prove `φ(y)` for a fresh `y`, conclude `∀x φ(x)`. This is
  "let `y` be arbitrary" in ordinary mathematical prose.
- **`∃E`**: from `∃x φ` and a proof of `ψ` from a fresh `φ(y)`, conclude `ψ`
  (`ψ` must not mention `y`). This is "choose a witness `y` with `φ(y)`" — and
  the discipline that `y` cannot leak into the conclusion.
- **Hilbert generalisation** (`hilbert_quantifier_axioms`) has the analogous
  restriction as a side condition on the rule.

## Hypothesis-dropped counterexamples
- **`∀I` without freshness**: from `P(y)` (an open assumption) derive
  `∀x P(x)` — so `{P(y)} ⊢ ∀x P(x)`, but `{P(y)} ⊭ ∀x P(x)` (a structure where
  `P` holds of `s(y)` only). **Soundness fails** (`soundness_fol`).
- **`∃E` letting `y` into the conclusion**: from `∃x P(x)` "conclude" `P(y)` for
  the witness `y` — but `y` is not a real object, and `P(y)` can then be used
  where a *specific* claim is needed.
- the deduction theorem's first-order form fails for the same reason
  (`{P(x)} ⊢ ∀x P(x)` but `⊬ P(x) → ∀x P(x)`).

## Common misuse
Skipping the freshness check "because it usually works out"; letting the `∃E`
witness variable appear in the conclusion; generalising a variable that is
constrained by a hypothesis; confusing the eigenvariable with a Skolem constant.

## Related nodes (non-prerequisite)
- `guards`: `nd_rules_quantifier` (`∀I`, `∃E`), `hilbert_quantifier_axioms`
  (generalisation).
- `stated_via`: `free_bound_variables`.
- `related`: the free-variable side condition on the first-order deduction
  theorem; Skolemisation (the "opposite" move).

## Sources
[vandalen_5e] ch. 3; [chiswell_hodges] ch. 4; [enderton_logic_2e] §2.4;
Prawitz (1965).
