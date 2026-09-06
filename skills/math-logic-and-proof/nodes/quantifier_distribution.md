# quantifier_distribution

## Type
mathematical_identity  (epistemic status: `mathematical_identity` / mixed —
some are equivalences, some one-directional; `constructive_grade: intuitionistic`
for the valid directions)

## Statement
- `∀x (φ ∧ ψ) ≡ (∀x φ) ∧ (∀x ψ)`   — **equivalence** (∀ distributes over ∧)
- `∃x (φ ∨ ψ) ≡ (∃x φ) ∨ (∃x ψ)`   — **equivalence** (∃ distributes over ∨)
- `(∀x φ) ∨ (∀x ψ)  ⊨  ∀x (φ ∨ ψ)` — **one direction only** (converse fails)
- `∃x (φ ∧ ψ)  ⊨  (∃x φ) ∧ (∃x ψ)` — **one direction only** (converse fails)
- If `x ∉ FV(ψ)`: `∀x (φ ∨ ψ) ≡ (∀x φ) ∨ ψ` and `∃x (φ ∧ ψ) ≡ (∃x φ) ∧ ψ`
  (pull the `ψ` out) — used in `prenex_normal_form`.

## Symbols
- `φ`, `ψ`: formulas; `x`: the quantified variable.

## Prerequisites (tsort edges into this node)
`logical_equivalence_fol`, `tarski_satisfaction`.

## Content
`∀` behaves like an infinite `∧`, `∃` like an infinite `∨` — so `∀` distributes
over `∧` and `∃` over `∨` (both directions), but the "cross" combinations are
**one-directional** (the same asymmetry as `distributivity_prop`'s quantified
analogue).

## Constructive grade
`intuitionistic` for all the **valid** directions (they are BHK-provable term
constructions). The failing directions fail *semantically*, not for want of
LEM.

## Lean status
`lean_status: cited`. The valid directions are one-line Lean terms
(`fun h => ⟨fun x => (h x).1, fun x => (h x).2⟩` for `∀`-over-`∧`); not named in
`validation/proof-checks.lean`. `bc validation/instance-checks.bc` can exhibit a
failing case on a finite domain.

## Type / well-formedness check
`well_formed`. The "pull `ψ` out" equivalences **require `x ∉ FV(ψ)`** — omit
that and you capture. Nonempty domain for the `∀`/`∃` interplay.

## Specialization / boundary cases
- domain **finite** `{a₁, …, aₙ}`: all four become finite `distributivity_prop`
  instances, and the one-directional ones are then genuine non-equivalences
  visible in 2 elements.
- `x ∉ FV(φ) ∪ FV(ψ)`: both quantifiers vacuous, everything trivial.
- `prenex_normal_form` uses the `x ∉ FV(ψ)` pull-out rules (after α-renaming to
  ensure the side condition).

## Hypothesis-dropped counterexamples
- **`∀x (φ ∨ ψ) ⟹ (∀x φ) ∨ (∀x ψ)`**: FALSE. Domain `{0, 1}`,
  `φ(x) := (x = 0)`, `ψ(x) := (x = 1)`: `∀x (x=0 ∨ x=1)` is true, but neither
  `∀x (x=0)` nor `∀x (x=1)`.
- **`(∃x φ) ∧ (∃x ψ) ⟹ ∃x (φ ∧ ψ)`**: FALSE, same structure — `∃x (x=0)` and
  `∃x (x=1)` both hold, but no `x` is both.
- **pull `ψ` out with `x ∈ FV(ψ)`**: `∀x (φ(x) ∨ ψ(x)) ≢ (∀x φ(x)) ∨ ψ(x)` —
  the free `x` on the right is unbound/captured.

## Common misuse
Distributing `∀` over `∨` or `∃` over `∧` as an equivalence; pulling a formula
past a quantifier whose variable it contains; assuming the failures are
constructive rather than semantic; forgetting the `x ∉ FV(ψ)` side condition in
prenexing.

## Related nodes (non-prerequisite)
- `analogue`: `distributivity_prop` (the propositional / finite case).
- `used_by`: `prenex_normal_form` (the pull-out rules).
- `related`: `∀` as infinite `∧`, `∃` as infinite `∨`.

## Sources
[enderton_logic_2e] §2.2; [vandalen_5e] §3.1; [chiswell_hodges] ch. 7.
