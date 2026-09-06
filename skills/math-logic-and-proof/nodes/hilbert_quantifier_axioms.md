# hilbert_quantifier_axioms

## Type
definition  (epistemic status: `definition`; `constructive_grade: intuitionistic`)

## Statement
The Hilbert calculus for first-order logic adds to `hilbert_system_prop`:
- **∀-instantiation schema**: `∀x φ → φ[t/x]`, for `t` **free for `x`** in `φ`
  (`free_for`);
- **∀-distribution schema**: `∀x (φ → ψ) → (∀x φ → ∀x ψ)`;
- **vacuous-∀ schema**: `φ → ∀x φ` when `x ∉ FV(φ)`;
- the **generalisation rule**: from `⊢ φ` infer `⊢ ∀x φ` (with the restriction
  that `x` is not free in any premise still in play).

`∃x φ` is `¬∀x ¬φ` (or gets dual axioms). Equality is handled by
`equality_axioms`.

## Symbols
- `x`: bound variable; `t`: a term.

## Prerequisites (tsort edges into this node)
`hilbert_system_prop`, `quantifier_syntax`, `substitution`, `free_for`.

## Content
The axiomatic-style counterpart of `nd_rules_quantifier`. Generalisation plays
the role of `∀I`; the instantiation schema plays `∀E`. The **deduction theorem**
(`deduction_theorem`) needs its first-order side condition precisely because
generalisation can be applied to a variable free in an assumption.
`derivability_fol` is calculus-independent (`nd_hilbert_equivalence` extended).

## Constructive grade
`intuitionistic` — these schemas and generalisation are rules of intuitionistic
predicate logic; the classical strength comes only from
`hilbert_system_prop`'s schema 3.

## Lean status
`lean_status: cited`. Mathlib's first-order proof system; not in
`validation/proof-checks.lean` (propositional). Lean's own `∀`-elimination is
term application; generalisation is `fun y => …` under a fresh binder.

## Type / well-formedness check
`well_formed`. The instantiation schema requires **`free_for(t, x, φ)`** — an
instance without it is not an axiom. Generalisation requires `x` **not free in
premises** — otherwise it is unsound (the first-order deduction-theorem
counterexample). The vacuous-∀ schema requires `x ∉ FV(φ)`.

## Specialization / boundary cases
- instantiation with `t = x`: `∀x φ → φ`.
- generalisation of a **theorem** (`⊢ φ`, no premises): always allowed —
  `⊢ φ ⟹ ⊢ ∀x φ`.
- combined with the propositional axioms: exactly the valid first-order wffs
  (`godel_completeness_theorem`).
- **∃-instantiation** is *not* an axiom (it would be `∃E`, which discharges an
  assumption) — handled via `¬∀x ¬` + generalisation.

## Hypothesis-dropped counterexamples
- **instantiation without `free_for`**: `∀x ∃y (y ≠ x) → ∃y (y ≠ y)` — an
  "axiom" that is not valid.
- **generalise a variable free in a premise**: `P(x) ⊢ ∀x P(x)` (by
  generalisation), but `⊬ P(x) → ∀x P(x)` — soundness / the deduction theorem
  break.
- **vacuous-∀ when `x ∈ FV(φ)`**: `P(x) → ∀x P(x)` is not valid.

## Common misuse
Instantiating with a capturing term; generalising a variable that appears free
in a live assumption; treating `∃`-instantiation as an axiom; forgetting the
deduction theorem's first-order side condition.

## Related nodes (non-prerequisite)
- `nd_counterpart`: `nd_rules_quantifier` (`∀E` ↔ instantiation, `∀I` ↔
  generalisation).
- `requires`: `free_for`, and (generalisation) the not-free-in-premises
  restriction.
- `feeds`: `derivability_fol`.
- `constrains`: `deduction_theorem` (first-order form).

## Sources
[mendelson_6e] ch. 2; [enderton_logic_2e] §2.4; [shoenfield] ch. 3.
