# Specialization / boundary cases and hypothesis-dropped counterexamples

Per headline node: at least one **specialization** that must come out right, and
at least one **counterexample** showing a hypothesis (or a Peano/domain
assumption) cannot be dropped. Numeric parts are in
`validation/instance-checks.bc`; abstract cores in `validation/proof-checks.lean`.

## `peano_axioms`
**Specialization:** induction with `X = {n : P(n)}` is ordinary proof by
induction; the recursion theorem is the deep consequence.
**Counterexamples:**
- drop *`S` injective*: `ℤ/nℤ` with successor `+1` — recursion by `f(0)=a`,
  `f(S k)=g(k,f k)` is over-determined once the cycle closes.
- drop *`0` not a successor*: a finite cycle `{0,…,k−1}` — `0 = S(k−1)`, so the
  base equation and the step equation at `k−1` both fix `f(0)`.
- drop *induction*: `ℕ ⊔ (an extra ℤ-chain)` satisfies axioms 1–4; the extra
  chain is invisible to base-plus-successor but breaks uniqueness of recursive
  definitions.

## `recursion_theorem`
**Specializations:** `g(n,x) = x+1`, `a = 0` ⇒ `f = id` (sanity); `g` ignoring
`n` gives plain iteration; `g` using `n` gives primitive recursion.
**Counterexamples:** same as `peano_axioms` — each dropped Peano axiom breaks
existence or uniqueness of `f`.

## `integer` / `rational_number`
**Specializations:**
- `[(n,0)]` / `[(a,1)]` are the embedded images of `ℕ` / `ℤ`.
- `[(5,2)] = [(8,5)]` since `5+5 = 2+8`; `[(2,4)] = [(1,2)]` since `2·2 = 4·1`
  (`instance-checks.bc`).
- `[(a,b)] = [(a+k, b+k)]` for all `k` — a class is a whole diagonal.
**Counterexamples:**
- `∼` not transitive ⇒ no partition ⇒ "the set of classes" is ill-defined.
- ℚ from a ring **with zero divisors**: localising `ℤ/6` collapses — `Frac`
  needs an integral domain. `∼_ℚ` transitivity fails without ℤ-cancellation.
- second coordinate `= 0` allowed ⇒ `[(a,0)] ∼ [(c,0)]` for all `a,c`, field
  structure destroyed.

## `integer_is_ordered_integral_domain` / `rational_is_ordered_field`
**Specialization:** restricting the ℚ structure to `[(a,1)]` reproduces the ℤ
ordered ring; restricting ℝ to `q*` reproduces the ℚ ordered field.
**Counterexamples:**
- ℤ is a domain but **not a field** — `2` has no inverse (`rational_is_field`
  is exactly the fix).
- `ℤ/4` is a commutative ring but **not a domain** — `2·2 = 0`.
- `ℂ` is a field that admits **no** compatible total order (`i² = −1` would
  force `−1 ≥ 0`).
- a finite field `𝔽_p` is not orderable (finite ordered domains don't exist).

## `sqrt2_irrational`
**Specializations:** the same argument gives `√n` irrational for every
non-square `n`; `p² = 2q²` has no positive-`q` solution (`instance-checks.bc`:
none with `q ≤ 2000`).
**Counterexamples:**
- drop *`n` non-square*: `√4 = 2 ∈ ℚ`.
- "drop" lowest terms: infinite descent still works — same content, no gain.

## `rational_incomplete_lub`
**Specialization:** in ℝ the same `A = {x : x² < 2}` **does** have a sup, `√2`
(`lub_property` + `nth_root_exists`). Decimal search: square `< 2` forever, next
tick `> 2` (`instance-checks.bc`).
**Counterexamples:**
- move to ℝ ⇒ the theorem is false — completeness is precisely what ℚ lacks.
- the incompleteness is **not** because `A` is unbounded — `A` is bounded by 2.

## `dedekind_cut`
**Specializations:** `q*` is a cut for every `q ∈ ℚ`; `{p : p ≤ 0 or p² < 2}`
is the `√2` cut.
**Counterexamples:**
- drop *proper subset*: `A = ℚ` (`+∞`) and `A = ∅` (`−∞`) are not reals.
- drop *downward closed*: `{0, 2}` — a real is fixed by **all** rationals below
  it.
- drop *no greatest element*: `{p : p ≤ q}` and `{p : p < q}` become two
  different reals for one `q`; the "no greatest" clause is what makes
  `rational_embeds_in_real` injective.

## `real_number` / `real_is_ordered_field`
**Specializations:** `q ↦ q*` is an ordered-field embedding of ℚ; sign-case
multiplication reproduces `(−)(−) = (+)`.
**Counterexamples:**
- define `A·B := {ab : a∈A, b∈B}` for all cuts ⇒ once a cut has arbitrarily
  negative rationals the product is all of ℚ — **not a cut**. Sign cases are
  mandatory.
- drop *no greatest element* ⇒ `−A` and `0*` become ambiguous.

## `lub_property`
**Specializations:** `S = {q* : q < 1}` ⇒ `sup S = 1*`; `S = {q* : q² < 2}` ⇒
`sup S = √2` cut; `sup{A} = A`.
**Counterexamples:**
- drop *`S` nonempty*: `sup ∅` would be a least real — none exists.
- drop *`S` bounded above*: `⋃ S = ℚ`, not a cut, no sup.
- ambient field ℚ instead of ℝ ⇒ **false** (`rational_incomplete_lub`).

## `nth_root_exists`
**Specializations:** `n = 1` ⇒ `y = x`; `x = 2, n = 2` ⇒ the missing `√2`;
`2^{1/3} ≈ 1.2599` (`instance-checks.bc`).
**Counterexamples:**
- drop *`x > 0`*: `x = −1, n = 2` has no real root.
- ambient field ℚ ⇒ no `√2` — the theorem is a payoff of `lub_property`.

## `real_uniqueness`
**Specializations:** the Dedekind and Cauchy ℝ's are isomorphic
(`dedekind_cauchy_equivalent`); "the reals" is well-posed.
**Counterexamples:**
- drop *Dedekind-complete*: ℚ and the real algebraic numbers are Archimedean
  ordered fields not isomorphic to ℝ (both countable).
- drop *ordered*: ℂ (`|ℂ| = |ℝ|`) is not order-isomorphic to anything; bare
  field-isomorphism of ℝ is a different, choice-dependent question.
- non-Archimedean ordered fields (hyperreals) are outside the theorem.

## `cantor_diagonal_argument` / `real_uncountable`
**Specializations:** a worked 5-element list ⇒ an explicit 6th real
(`instance-checks.bc`); the same argument on binary strings is `cantor_theorem`
for `X = ℕ`; every interval `(a,b)`, `a<b`, is uncountable.
**Counterexamples:**
- allow *`9`-tail digits* in `d` ⇒ `d = 0.4999… = 0.5 = x_k` digitwise-different
  but equal — proof breaks. Digits from `{1,…,8}` fix it.
- list of **rationals** ⇒ the diagonal escapes ℚ, not the list — consistent,
  since ℚ **is** countable (`rational_countable`).

## `countable_union_countable`
**Specializations:** `ℤ = ⋃_n {−n,n}`; `ℚ = ⋃_{d∈ℕ⁺} {a/d : a∈ℤ}`; a finite
union needs no choice.
**Counterexamples:**
- drop *`countable_choice`*: consistent with ZF (Feferman–Levy) that ℝ is a
  countable union of countable sets — the theorem genuinely needs CC.
- drop *index set countable*: `ℝ = ⋃_{x∈ℝ} {x}` — uncountable union of
  (countable) singletons.
- misuse: "ℝ is a countable union of countable sets" is **false**
  (`real_uncountable`) — in any countable cover of ℝ some piece is uncountable.
