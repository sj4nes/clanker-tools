# cantor_diagonal_argument

## Type
theorem  (epistemic status: `proved_theorem`, `constructive`)

## Statement
Given any sequence `(x_k)_{k∈ℕ}` of reals in `[0,1]`, one can construct a real
`d ∈ [0,1]` with `d ≠ x_k` for every `k`.

## Symbols
- `x_k`: the `k`-th real of the given list
- `a_{kj}`: the `j`-th decimal digit of `x_k`
- `d`: the constructed real that the list omits

## Prerequisites (tsort edges into this node)
`real_number`, `rational_dense_in_real` (decimal expansions),
`countable_set`, `real_order`, `nat_division_with_remainder` (digit extraction).

## Construction
Write each `x_k` in decimal, `x_k = 0.a_{k1} a_{k2} a_{k3} …`. Define the digits
of `d = 0.d_1 d_2 d_3 …` by

    d_k = 5   if a_{kk} ≠ 5,     d_k = 6   if a_{kk} = 5.

Every `d_k ∈ {5,6} ⊆ {1,…,8}`, so `d` has a **unique** decimal expansion and
`d ∈ [0,1]`. For each `k`, `d` and `x_k` differ in the `k`-th digit, and since
neither has a `0`- or `9`-tail this is a genuine inequality of reals. Hence
`d ≠ x_k` for all `k`. ∎

## The one subtlety — a *type* issue
Digits are chosen from `{1,…,8}` on purpose. If `d` were allowed a `9`-tail we
could hit `d = 0.4999… = 0.5000… = x_k`: digitwise different, **equal as
reals**. Avoiding `0` and `9` makes "differs in digit `k`" imply "differs as a
real" (`objects.md` rule 7).

## Checked
- **Lean** `proof-checks.lean` §6: `cantor` — the *abstract* diagonal
  (`f a ≠ (fun x => ¬ f x x)`), a genuine kernel proof, no Mathlib. It is the
  same move one type-level up.
- **bc** `instance-checks.bc`: a worked 5-element list of decimals → an explicit
  6th real differing on the diagonal.
- The decimal bookkeeping and `0.999…` handling stay informal (cited).

## Specialization / boundary cases
- a worked 5-element instance → an explicit 6th real (`instance-checks.bc`).
- the same argument on **binary** strings is `cantor_theorem` for `X = ℕ`
  (`|ℕ| < |𝒫(ℕ)|`).
- any interval `(a,b)` with `a < b` is uncountable by rescaling.

## Hypothesis-dropped counterexamples
- **allow `9`-tail digits in `d`:** the proof breaks (see the subtlety).
- **list of rationals instead of reals:** the diagonal `d` escapes `ℚ`, not the
  list — which is *consistent*, because `ℚ` **is** countable
  (`rational_countable`). The argument genuinely needs the ambient set to be
  `ℝ`.

## Common misuse
Also demanding `d` be irrational (unnecessary — it just has to differ from every
`x_k`); thinking the list must be given by a formula (it works for *any*
`x : ℕ → ℝ`); reading it as a statement about one non-computable real rather
than about the whole set.

## Related nodes (non-prerequisite)
- generalises from `cantor_theorem`
- feeds `real_uncountable`

## Sources
[cantor_1891]; [rudin_principles] Theorem 2.14; [enderton] ch. 6.
