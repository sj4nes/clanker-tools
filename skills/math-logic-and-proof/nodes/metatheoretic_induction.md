# metatheoretic_induction

## Type
primitive  (a root; `constructive_grade: intuitionistic`)

## Statement
Ordinary and strong **induction** and **recursion** on the metatheoretic natural
numbers `ℕ = {0, 1, 2, …}`:
- **weak induction**: `P(0)` and `∀n (P(n) → P(n+1))` ⟹ `∀n P(n)`;
- **strong induction**: `∀n ((∀k < n, P(k)) → P(n))` ⟹ `∀n P(n)`;
- **recursion**: a function `ℕ → A` is determined by `f(0)` and `f(n+1) =
  g(n, f(n))` (or course-of-values).

## Symbols
- `ℕ` (meta): the natural numbers used to index symbols, measure formula
  length / height / quantifier rank, count derivation steps, and enumerate.

## Prerequisites (tsort edges into this node)
none — **primitive**.

## Why primitive here, and NOT imported
`math-number-systems` *constructs* `ℕ` and proves things about it **using
logic** — its derivations are among the finite objects this capsule quantifies
over. Importing that `ℕ` would rest the floor on something two storeys up. So
the metatheoretic `ℕ` — used only for counting and induction on finite
syntactic structure — is declared primitive, with the Peano-style
induction/recursion rules bundled here. This is finitistic and uncontroversial;
it is **not** a claim that `ℕ` needs no construction.

`weak_induction`, `strong_induction`, `well_ordering_principle`,
`structural_induction` all draw on this node; `induction_equivalence` proves the
three `ℕ`-principles equivalent.

## Constructive grade
`intuitionistic` — `Nat.rec`; the recursor of an inductive type. Zero axioms
(`#print axioms strong_of_weak` in `validation/proof-checks.lean` → none).

## Lean status
`lean_status: core`. `induction n with | zero => … | succ n ih => …` and
`Nat`-recursion are primitive in Lean; `strong_of_weak` in
`validation/proof-checks.lean` derives strong induction from `Nat`-recursion
with **no axioms**.

## Type / well-formedness check
`well_formed`. The Peano properties assumed: `0` is not a successor; `succ` is
injective; induction. `<` is the associated well-founded order
(`well_ordering_principle`). "Metatheoretic" flags that this is reasoning *in
the metalanguage about* syntax, not an object theory.

## Specialization / boundary cases
- induction from a base `b`; two-step / `k`-step induction (really strong
  induction).
- **induction on `formula_complexity`** (degree, height, quantifier rank):
  `strong_induction` on `ℕ` via the measure — the standard way to induct on wffs
  when the IH must cover non-subformulas.
- **transfinite** induction/recursion (ordinals) is the `math-sets-...`
  generalisation; not needed here.

## Hypothesis-dropped counterexamples
- **carrier not well-founded** (`ℤ`, `ℚ`, a cycle `ℤ/nℤ`): the principles come
  apart (`induction_equivalence` counterexamples).
- **omit the base case**: `∀n (P(n) → P(n+1))` alone proves nothing.
- **step only for large `n`**: the "all horses same colour" failure is at
  `n = 1 → 2`.

## Common misuse
Verifying the induction step only for large `n`; using `P(n+1)` (the goal) in
the step; inducting on a non-well-founded quantity; importing constructed `ℕ`
into the metatheory (circular).

## Related nodes (non-prerequisite)
- `packages`: `weak_induction`, `strong_induction`, `well_ordering_principle`,
  `structural_induction` (as proof methods).
- `used_by`: `deduction_theorem`, `lindenbaum_lemma_prop` / `_fol`,
  `henkin_constants`, `formula_complexity`, every "induction on the length of a
  derivation".
- `generalised_by`: transfinite induction (`math-sets-functions-cardinality`).

## Sources
[enderton_logic_2e] §3.3; [vandalen_5e] §1.1; `conventions.md` (the stance).
