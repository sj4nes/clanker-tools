# weak_induction

## Type
definition  (epistemic status: `definition` — it packages the primitive
`metatheoretic_induction` as a proof method; `constructive_grade: intuitionistic`)

## Statement
For a predicate `P` on `ℕ`: if `P(0)` and `∀n (P(n) → P(n+1))`, then `∀n P(n)`.
As a proof method: to prove `∀n P(n)`, prove the **base case** `P(0)` and the
**induction step** `P(n) → P(n+1)` (assuming `P(n)`, the *induction hypothesis*).

## Symbols
- `P`: a predicate on `ℕ` (`ℕ → Prop`, metatheoretic).
- `n`: the induction variable, arbitrary in the step.
- IH: the assumed `P(n)` inside the step.

## Prerequisites (tsort edges into this node)
`metatheoretic_induction`.

## Content
`weak_induction` **is** the induction axiom of `metatheoretic_induction`,
presented as a strategy. It is the fifth Peano axiom in the capsule stack; here
it is primitive (metatheoretic ℕ, `conventions.md`). `strong_induction`,
`well_ordering_principle`, and structural induction are all provably equivalent
to it (`induction_equivalence`) or instances of the same schema
(`structural_induction`).

## Constructive grade
`intuitionistic` — `Nat.rec` is the recursor of an inductive type; no classical
principle. A proof by weak induction is fully constructive and computes.

## Lean status
`lean_status: core`. `induction n with | zero => … | succ n ih => …` is exactly
this. In `validation/proof-checks.lean`, `strong_of_weak` builds strong
induction *from* `Nat`-recursion (the `aux` lemma is a plain
`induction n`); `#print axioms strong_of_weak` → **no axioms**.

## Type / well-formedness check
`well_formed`. The step must prove `P(n) → P(n+1)` for **arbitrary** `n`
(eigenvariable) — not for a specific `n`, and not `P(n−1) → P(n)` with an
unnoticed `n = 0` gap. `P` must be a genuine predicate on all of `ℕ` (a `P`
secretly defined only for `n ≥ 1` needs the base shifted).

## Specialization / boundary cases
- **base at `b`**: to prove `∀n ≥ b, P(n)`, take base `P(b)` and step
  `P(n) → P(n+1)` for `n ≥ b` (equivalently, induct on `Q(k) := P(b+k)`).
- **two-step / `P(n) ∧ P(n+1) → P(n+2)`** (e.g. Fibonacci bounds): needs *two*
  base cases and is really `strong_induction` in disguise.
- finite range `{0, …, N}`: induction still applies; or just `proof_by_cases`
  with `N+1` cases.

## Where it fails / is misapplied
- **missing / wrong base case**: "`P(n) → P(n+1)` for all `n`, therefore
  `∀n P(n)`" proves nothing without `P(0)`. The classic fake proof "all horses
  are the same colour" fails exactly at the `n = 1 → n = 2` step, not the base —
  a reminder that the *step* must hold for **every** `n`, including small ones.
- **inducting on the wrong variable** in a multi-variable statement.
- **strengthening needed**: many statements are not provable by weak induction
  as stated but are after strengthening the IH (or switching to
  `strong_induction`).
- **non-well-founded carrier**: on `ℤ` or `ℚ` there is no `weak_induction`
  (`induction_equivalence` counterexample: cyclic / no-least-element carriers).

## Common misuse
Verifying the step only for large `n`; using `P(n+1)` (the goal) to justify a
step; "induction" on a real parameter; forgetting the IH is `P(n)` not
`∀k ≤ n, P(k)` (that is `strong_induction`).

## Related nodes (non-prerequisite)
- `equivalent_to`: `strong_induction`, `well_ordering_principle` (proved as
  `induction_equivalence`).
- `instance_of`: the general `structural_induction` schema (ℕ = the inductive
  type with constructors `0`, `succ`).
- `generalised_by`: `transfinite_induction` (`math-sets-functions-cardinality`).

## Sources
[velleman_3e] §6.1; [hammack_bop] ch. 10; [enderton_logic_2e] §3.3.
