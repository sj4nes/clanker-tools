# free_for

## Type
definition  (epistemic status: `definition`; it is a **side condition**, the
capsule's `type_check` exemplar)

## Statement
A term `t` is **free for `x` in `φ`** when substituting `t` for the free
occurrences of `x` in `φ` captures no variable of `t` — i.e. for every variable
`y` occurring in `t`, no free occurrence of `x` in `φ` lies within the scope of
a quantifier `∀y` or `∃y`.

Recursively:
- `t` is free for `x` in an atomic `φ`: always.
- free for `x` in `¬φ` ⟺ free for `x` in `φ`; likewise `∧ ∨ → ↔` componentwise.
- free for `x` in `∀y φ` (resp. `∃y φ`) ⟺ **either** `x` is not free in `∀y φ`,
  **or** (`y` does not occur in `t` **and** `t` is free for `x` in `φ`).

## Symbols
- `t`: a term (`term_syntax`); `var(t)` its set of variables.
- `x`: the variable being substituted for.
- `φ`: a `first_order_wff`.

## Prerequisites (tsort edges into this node)
`free_bound_variables`, `quantifier_syntax`, `term_syntax`.
(**Not** `substitution` — the total operation `φ[t/x]` and this condition are
independent; see `edges/cycles.md` §1.)

## Why it exists — the failure it prevents
`φ[t/x]` as a raw string operation is always defined, but it is only **sound**
when `t` is free for `x` in `φ`. The canonical break:

    φ  =  ∃y (y > x)              (true in (ℕ,<) under any assignment: take y = x+1)
    t  =  y
    φ[y/x]  =  ∃y (y > y)        (FALSE in (ℕ,<))

The free `x` was under `∃y`, and `t = y` got **captured**. `∀E` concluding
`φ[t/x]` from `∀x φ`, and `∃I` concluding `∃x φ` from `φ[t/x]`, are **unsound**
without the condition — this is exactly why `nd_rules_quantifier` and
`hilbert_quantifier_axioms` carry a `requires free_for` edge.

## Discharging it — `alpha_equivalence`
If `t` is not free for `x` in `φ`, rename the offending bound variables of `φ`
(`alpha_equivalence`) to fresh ones; the result is logically interchangeable and
`t` is free for `x` in it. So the condition is never a real obstruction, only a
check — but skipping the check is a genuine bug.

## Lean status
`lean_status: core` (the mechanism), `mathlib_cited` (the general treatment).
In a de Bruijn representation capture is impossible by construction, so the
Lean model either uses named variables with an explicit `FreeFor` predicate
(checked by `decide` on examples) or cites Mathlib's substitution lemmas which
bake in the condition. `validation/proof-checks.md#free_for` records which.

## Type / well-formedness check
This node **is** the type check for every substitution-under-a-binder statement.
`type_check_status` on `substitution_lemma_semantic`, `nd_rules_quantifier`,
`hilbert_quantifier_axioms`, `prenex_normal_form`, and the Henkin axioms in
`godel_completeness_theorem` all reduce, in part, to "the `free_for` obligation
is discharged". A statement writing `φ[t/x]` without it is **ill-formed to use**
(`objects.md`).

## Specialization / boundary cases
- `t` a **constant** or a **closed term**: free for `x` in every `φ` (no
  variables to capture) — this is why the Henkin witnesses `c_ψ` need no
  renaming.
- `x` **not free** in `φ`: free for `x` vacuously (`φ[t/x] = φ`).
- `t = x`: always free for `x` in `φ` (`φ[x/x] = φ`).
- `φ` **quantifier-free**: always free.

## Hypothesis-dropped counterexamples (drop the condition, keep substituting)
- `∀E`: from `∀x ∃y (y > x)` infer `∃y (y > y)` — valid premise, false
  conclusion.
- `∃I`: from `∃y ¬(x = y)` (some element differs from `x`) infer
  `∃x ∃y ¬(x = y)` correctly, but from `P(x) → ∃y R(x,y)` one must not
  instantiate `x := y`.
- the **substitution lemma** `𝔄 ⊨ φ[t/x][s] ⟺ 𝔄 ⊨ φ[s(x ↦ s̄(t))]` fails on
  the nose in the capture case.

## Common misuse
Silently substituting in a proof "because the syntax allows it"; forgetting the
condition when the term is a compound like `f(y,z)` (any of `y`, `z` can be
captured); assuming a renaming changes the meaning.

## Related nodes (non-prerequisite)
- `discharged_by`: `alpha_equivalence`.
- `guards`: `nd_rules_quantifier`, `hilbert_quantifier_axioms`,
  `substitution_lemma_semantic`, `prenex_normal_form`.
- `commonly_confused_with`: `free_bound_variables` (that is about occurrences in
  `φ` alone; this is about `t` and `φ` together).

## Sources
[enderton_logic_2e] §2.1 (def. of "substitutable"); [vandalen_5e] §3.1;
[chiswell_hodges] §7.1.
