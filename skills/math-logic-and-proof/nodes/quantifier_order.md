# quantifier_order

## Type
notation_convention  (also a `proposition`; `constructive_grade: intuitionistic`
for the valid direction)

## Statement
`∃y ∀x φ  ⊨  ∀x ∃y φ`, and the **converse is not valid**: a *uniform* witness
gives a *pointwise* witness, never conversely. Unlike quantifiers, adjacent
**unlike** quantifiers may **not** be swapped.

## Symbols
- `φ`: a formula with `x`, `y` (distinct) possibly free.

## Prerequisites (tsort edges into this node)
`logical_equivalence_fol`, `tarski_satisfaction`.

## Content
A `notation_convention` node because the entire capsule (and all of analysis)
depends on **never silently swapping** `∀x∃y` and `∃y∀x`. `∃y∀x` ("there is one
`y` that works for every `x`") is the strictly stronger **uniform** form.
Same-kind quantifiers **do** commute: `∀x∀y φ ≡ ∀y∀x φ`, `∃x∃y φ ≡ ∃y∃x φ`.

## Constructive grade
`intuitionistic` — `∃y∀x φ → ∀x∃y φ` is `fun ⟨y, hy⟩ x => ⟨y, hy x⟩`. (Getting
a uniform `y` *from* `∀x∃y`, when it did hold, would be a choice-flavoured move —
but the point is that it does not hold.)

## Lean status
`lean_status: core`. `validation/proof-checks.lean`:
`forall_exists_of_exists_forall : (∃ y, ∀ x, r x y) → (∀ x, ∃ y, r x y)`
(one line); `exists_forall_not_converse` — on `Bool` with `r x y := x ≠ y`,
`∀x∃y` holds and `∃y∀x` fails, both by `decide`. `bc validation/instance-checks.bc`
runs the same on a 4-element cyclic-successor relation.

## Type / well-formedness check
`well_formed`. `x`, `y` **distinct**; the entailment is stated for formulas
(free variables allowed) evaluated under an assignment.

## Specialization / boundary cases
- `φ = (x < y)` over `(ℕ, <)`: `∀x∃y (x < y)` TRUE (`y = x+1`);
  `∃y∀x (x < y)` FALSE — the standard witness.
- **continuity vs uniform continuity**: `∀x∀ε∃δ …` (continuous) vs
  `∀ε∃δ∀x …` (uniformly continuous) — swapping `δ` outward is exactly this, and
  is invalid; `f(x) = x²` on `ℝ` and `1/x` on `(0,1)` are the counterexamples.
- **one-element domain**: the two orders coincide.
- `¬∀x∃y φ ≡ ∃x∀y ¬φ` — the negation flips each quantifier but **preserves the
  order** (`quantifier_negation`).

## Hypothesis-dropped counterexamples
- **swap to `∃y∀x` from `∀x∃y`**: `f` continuous but not uniformly continuous —
  a `δ` for each `(x, ε)` but no `δ` uniform in `x`.
- **`x = y`**: the statement is malformed.

## Common misuse
Swapping adjacent unlike quantifiers in a proof; reading "for every `x` there is
a `y`" as providing one `y`; the pointwise/uniform confusion throughout analysis
(convergence, continuity, boundedness, equicontinuity).

## Related nodes (non-prerequisite)
- `strengthens`: `∃y∀x` is the uniform form of `∀x∃y`.
- `interacts_with`: `quantifier_negation` (negation preserves order).
- `used_by`: the `uniform_convergence` / `uniform_continuity` nodes of
  `math-real-analysis` — this is the `quantifier_order` primitive that capsule
  cites.

## Sources
[enderton_logic_2e] §2.2; [velleman_3e] §2.x; [vandalen_5e] §3.1.
