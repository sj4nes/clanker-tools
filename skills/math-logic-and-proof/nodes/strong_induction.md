# strong_induction

## Type
theorem  (epistemic status: `proved_theorem`; `constructive_grade: intuitionistic`;
equivalent to `weak_induction`)

## Statement
For a predicate `P` on `ℕ`: if `∀n ((∀k < n, P(k)) → P(n))`, then `∀n P(n)`.
As a method: to prove `∀n P(n)`, prove `P(n)` assuming `P(k)` for **all** `k < n`
(the strong induction hypothesis). No separate base case is needed — the `n = 0`
instance has the vacuous hypothesis `∀k < 0, P(k)`.

## Symbols
- `P`: a predicate on `ℕ`.
- strong IH: `∀k < n, P(k)` (all smaller values, not just the predecessor).

## Prerequisites (tsort edges into this node)
`weak_induction`, `metatheoretic_induction`.

## Content / proof
Derived from `weak_induction` applied to `Q(n) := ∀k ≤ n, P(k)` (or
`Q(n) := ∀k < n, P(k)`): `Q(0)` is vacuous/`P(0)`, and `Q(n) → Q(n+1)` is
exactly the strong step. Hence `∀n Q(n)`, so `∀n P(n)`. This is
`strong_of_weak` in `validation/proof-checks.lean`.

## Constructive grade
`intuitionistic` — proved from `Nat`-recursion with no classical input
(`#print axioms strong_of_weak` → none). Equivalent in strength to
`weak_induction`: it proves exactly the same theorems, just often more
conveniently.

## Lean status
`lean_status: core`. `strong_of_weak` genuinely derives it; also
`Nat.strong_induction_on` / `Nat.strongRecOn` in core.

## Type / well-formedness check
`well_formed`. The step must establish `P(n)` from `∀k < n, P(k)` for
**arbitrary** `n`. A frequent slip: implicitly assuming `n ≥ 1` (so the
"predecessor" `n − 1` exists) and never checking `n = 0` — but with the strong
schema, `n = 0` is automatic *only if* the step's argument does not secretly
require a smaller element to exist.

## Specialization / boundary cases
- **weak induction** is the special case where the step uses only `k = n − 1`.
- **prime factorisation**, **Euclidean division**, **Fibonacci / recurrence
  bounds**, well-definedness of functions given by course-of-values recursion —
  the standard homes for strong induction.
- **finite descent** (`proof_by_contradiction` + least counterexample) is the
  contrapositive packaging (`induction_equivalence`,
  strong ⟺ well-ordering).

## Where it fails / is misapplied
- **step secretly needs a witness below `n`**: e.g. "`P(n)` because `P(n−2)`
  holds" — fine for `n ≥ 2`, but the `n = 0` and `n = 1` cases have no such
  `n − 2` and must be handled. The vacuous-base convenience does **not** excuse
  a step that assumes smaller elements exist.
- inducting on a quantity that is not a natural number / not well-founded.
- circular: using `P(n)` or `P(n+1)` inside the step.

## Common misuse
"No base case needed" taken to mean small cases never need thought; using
`≤ n` when the argument needs `< n` (or vice versa); confusing the strong IH
`∀k<n P(k)` with `P(n−1)`; applying it where the order is not well-founded.

## Related nodes (non-prerequisite)
- `equivalent_to`: `weak_induction`, `well_ordering_principle`
  (`induction_equivalence`).
- `special_case_of` (reverse): `weak_induction` is the `k = n−1`-only instance.
- `generalised_by`: `transfinite_induction`.

## Sources
[velleman_3e] §6.4; [hammack_bop] ch. 10; [enderton_logic_2e] §3.3.
