# alpha_equivalence

## Type
definition  (epistemic status: `definition`; `constructive_grade: intuitionistic`)

## Statement
Two wffs are **α-equivalent** (`φ ≡_α ψ`) if one is obtained from the other by
**renaming bound variables** — replacing `∀x φ` by `∀y (φ[y/x])` (and likewise
`∃`) where `y` does not occur free in `φ` and `y` is free for `x` in `φ`.
α-equivalent wffs are logically interchangeable: `𝔄 ⊨ φ [s] ⟺ 𝔄 ⊨ ψ [s]`.

## Symbols
- `≡_α`: the α-renaming equivalence relation on wffs.

## Prerequisites (tsort edges into this node)
`free_bound_variables`, `substitution`, `free_for`.

## Content
The device that makes `free_for` never a real obstruction: if `t` is **not**
free for `x` in `φ`, α-rename the offending bound variables of `φ` to fresh
ones, obtaining `φ' ≡_α φ` in which `t` **is** free for `x`. Used in
`prenex_normal_form` (pull quantifiers out without clashes) and in the Henkin
construction (`godel_completeness_theorem` — nested witness substitutions stay
capture-free).

Working "modulo α" (Barendregt's variable convention; or de Bruijn indices)
lets one ignore bound-variable names entirely — Mathlib's approach.

## Constructive grade
`intuitionistic` — a computable equivalence; renaming is effective.

## Lean status
`lean_status: cited` / `n/a`. In a **de Bruijn** representation (Mathlib) there
are no bound-variable names, so α-equivalence is **syntactic identity** — the
node's content is discharged by the representation choice. Named treatments
carry it explicitly.

## Type / well-formedness check
`well_formed`. The fresh variable `y` must **not occur free in `φ`** (else it
gets captured) **and** be free for `x` in `φ` (usually automatic for a truly
fresh `y`). α-renaming changes **names**, not `FV(φ)` and not the truth value.
`≡_α` is finer than `logical_equivalence_fol` (`≡_α ⊆ ≡`): α-equivalent wffs are
logically equivalent, not conversely.

## Specialization / boundary cases
- `φ` closed under the "no clashes" convention (all bound variables distinct
  from each other and from free variables): α-renaming is rarely needed.
- **capture-avoiding substitution** is defined *as* "α-rename then substitute
  naively".
- de Bruijn indices: `≡_α` collapses to `=`.
- `∀x P(x) ≡_α ∀y P(y)` but `∀x P(x) ≢_α ∀x Q(x)` (renaming ≠ replacing the
  matrix).

## Hypothesis-dropped counterexamples
- **rename to a variable free in `φ`**: `∀x (x < z)` "renamed" to `∀z (z < z)` —
  captures `z`, changes the meaning.
- **rename to a variable already bound elsewhere in scope**: shadowing bugs.
- **treat `≡_α` as `≡`**: `p ∨ ¬p ≡ ⊤` but they are not α-equivalent (α only
  renames binders).

## Common misuse
Renaming to a non-fresh variable (capture); thinking α-renaming can change a
formula's logical content; conflating `≡_α` with `≡`; forgetting that
substitution is *defined* to be capture-avoiding via α-renaming.

## Related nodes (non-prerequisite)
- `discharges`: `free_for` obstructions.
- `uses`: `substitution`, `free_bound_variables`.
- `feeds`: `prenex_normal_form`, `godel_completeness_theorem` (Henkin).
- `trivialised_by`: de Bruijn indices.

## Sources
[chiswell_hodges] §7.1; [enderton_logic_2e] §2.1; Barendregt, *The Lambda
Calculus* (the variable convention).
