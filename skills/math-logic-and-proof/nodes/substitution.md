# substitution

## Type
definition  (epistemic status: `definition`; `constructive_grade: intuitionistic`)

## Statement
`φ[t/x]` — the result of replacing **every free occurrence** of the variable
`x` in the wff `φ` by the term `t`. By recursion (`recursion_on_wff`):

    (atomic)[t/x]     = replace x by t in the terms
    (¬φ)[t/x]         = ¬(φ[t/x]);   (φ ∘ ψ)[t/x] = φ[t/x] ∘ ψ[t/x]
    (∀y φ)[t/x]       = ∀y φ           if y = x
                      = ∀y (φ[t/x])    if y ≠ x
    (∃y φ)[t/x]       similarly.

Analogously for terms: `u[t/x]`.

## Symbols
- `φ[t/x]`: the substitution instance; `x`: the variable; `t`: the term.

## Prerequisites (tsort edges into this node)
`term_syntax`, `first_order_wff`, `free_bound_variables`, `recursion_on_wff`.

## Content
A **total syntactic operation** — always defined. It is only **sound to use**
(in `∀E`, `∃I`, `substitution_lemma_semantic`, the Henkin axioms) when `t` is
**free for `x` in `φ`** (`free_for`) — otherwise it captures. The operation and
the side condition are **independent** (`edges/cycles.md` §1): `substitution`
requires only `free_bound_variables` (+ term/wff syntax), not `free_for`.

## Constructive grade
`intuitionistic` — a computable recursion.

## Lean status
`lean_status: cited`. Mathlib's `BoundedFormula` substitution (de Bruijn) is
capture-free by construction; named treatments carry the recursion above +
`free_for` guards. `free_for.md` in this capsule and `free_for_matters` in
`validation/proof-checks.lean` demonstrate the capture bug.

## Type / well-formedness check
`well_formed` as an operation. Where a **lemma or rule** writes `φ[t/x]` and
draws a semantic/proof-theoretic conclusion, the `free_for(t, x, φ)` obligation
must be discharged (or `alpha_equivalence` used to arrange it) — a statement
using `φ[t/x]` without it is **ill-formed to use** (`objects.md`).

## Specialization / boundary cases
- `t = x`: `φ[x/x] = φ`.
- `x ∉ FV(φ)`: `φ[t/x] = φ`.
- `t` a **closed term** (constant, ground): free for `x` in every `φ` — no
  renaming needed (Henkin witnesses).
- **simultaneous** substitution `φ[t₁/x₁, …, tₙ/xₙ]`: not the same as iterated
  single substitution in general (order matters if the `xᵢ` occur in the `tⱼ`).
- **term substitution** in the term model: `[t]` classes.

## Hypothesis-dropped counterexamples
- **capture** (`free_for` violated): `φ = ∃y (y > x)`, `t = y` ⟹
  `φ[y/x] = ∃y (y > y)` — a truth turned into a falsehood; `∀E` becomes
  unsound (`free_for.md`).
- **substitute for bound occurrences**: `(∀x P(x))[t/x] = ∀x P(x)` (correct —
  bound `x` untouched); substituting them would be nonsense.
- **iterate simultaneous substitutions naively**: `φ[y/x][x/y] ≠ φ` in general.

## Common misuse
Substituting without checking `free_for`; hitting bound occurrences; assuming
simultaneous = iterated substitution; forgetting `alpha_equivalence` can always
re-establish `free_for`; confusing `φ[t/x]` (substitution) with `φ` under an
assignment `s(x ↦ a)` (the two are linked by `substitution_lemma_semantic`).

## Related nodes (non-prerequisite)
- `independent_of`: `free_for` (both need only `free_bound_variables`).
- `guarded_by`: `free_for` (for sound *use*).
- `feeds`: `alpha_equivalence`, `nd_rules_quantifier`,
  `hilbert_quantifier_axioms`, `substitution_lemma_semantic`,
  `prenex_normal_form`, `equality_axioms`.

## Sources
[enderton_logic_2e] §2.1; [chiswell_hodges] §7.1; [vandalen_5e] §3.1.
