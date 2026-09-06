# Specialization / boundary cases and hypothesis-dropped counterexamples

For every headline node: (a) at least one **specialization** that must come out
right, and (b) at least one **counterexample** showing a named hypothesis cannot
be dropped. Numeric parts are computed in `validation/instance-checks.bc`.

## `monotone_convergence_theorem`
**Specializations:** constant sequence `x_n = c` → converges to `c` (= its sup).
Eventually-constant → same. `x_n = 1 − 1/n` (increasing, bounded by 1) → 1.
**Counterexamples when a hypothesis is dropped:**
- drop *bounded*: `x_n = n` is increasing, does not converge.
- drop *monotone*: `x_n = (−1)^n` is bounded, does not converge.
- drop *completeness of the ambient field* (work in ℚ): `x_{n+1} = (x_n +
  2/x_n)/2`, `x_1 = 2` is decreasing and bounded below, all terms rational,
  Cauchy — but its only candidate limit √2 ∉ ℚ. (`instance-checks.bc`: `x_6`
  matches √2 to 40 places.)

## `bolzano_weierstrass`
**Specializations:** constant sequence → whole sequence converges. A sequence
taking finitely many values → some value repeats infinitely → constant
subsequence. An enumeration of ℚ ∩ [0,1] → has subsequences converging to every
point of [0,1].
**Counterexamples:**
- drop *bounded*: `x_n = n` — differences are always 1, no Cauchy subsequence
  (`instance-checks.bc`).
- drop *completeness* (in ℚ): digit-truncations of √2 — bounded in ℚ, every
  subsequence Cauchy, none converges in ℚ.
- drop *finite dimension* (in `ℓ²`, out of scope, noted for contrast): the unit
  vectors `e_n` are bounded, pairwise distance √2, no convergent subsequence.

## `cauchy_convergence_criterion`
**Specialization:** a convergent sequence is Cauchy (the easy direction), for any
`(x_n)`.
**Counterexample:** drop *completeness* — in ℚ, `(1, 1.4, 1.41, 1.414, …)` is
Cauchy and does not converge. This *is* the defining failure of ℚ.

## `heine_borel`
**Specializations:** `[a,b]` is compact. A finite set is compact. `∅` is compact.
**Counterexamples:**
- drop *closed*: `(0,1)` is bounded, not compact — the cover
  `{(1/n, 1)}_{n≥2}` has no finite subcover.
- drop *bounded*: `[0,∞)` is closed, not compact — `{(−1, n)}_{n≥1}` has no
  finite subcover.
- drop *subset of ℝ* (the metric-space caveat): the closed unit ball of `ℓ²` is
  closed and bounded but **not** compact.

## `extreme_value_theorem`
**Specialization:** a constant function on `[a,b]` attains its (equal) max and
min everywhere.
**Counterexamples:**
- drop *closed interval*: `f(x) = x` on `(0,1)` attains neither sup nor inf.
- drop *bounded interval*: `f(x) = arctan x` on `ℝ` attains neither `±π/2`.
- drop *continuity*: `f(x) = x − ⌊x⌋` on `[0,1]` (with `f(1)=0`) has sup 1,
  never attained.

## `intermediate_value_theorem`
**Specialization:** `f(x) = x² − 2` on `[1,2]`: `f(1) = −1 < 0 < 2 = f(2)`, so a
root in `(1,2)` — bisection gives √2 (`instance-checks.bc`).
**Counterexamples:**
- drop *continuity*: the step function `g = 0` on `[1,1.5)`, `g = 1` on
  `[1.5,2]` never takes the value `0.5`.
- drop *connected domain*: `f(x) = 1/x` on `[−1,0)∪(0,1]` never takes `0`
  though it takes `−1` and `1`.

## `mean_value_theorem`
**Specialization:** `f(x) = x²` on `[1,3]`: secant slope `(9−1)/(3−1) = 4`,
`f'(c) = 2c = 4` ⇒ `c = 2 ∈ (1,3)` (`instance-checks.bc`). Rolle is the
sub-case `f(a) = f(b)`.
**Counterexamples:**
- drop *continuity at an endpoint*: `f(x) = x` on `(0,1]`, `f(0) := 1`. Not
  continuous at 0; no `c` with `f'(c) = (f(1)−f(0))/1 = 0`.
- drop *differentiability on `(a,b)`*: `f(x) = |x|` on `[−1,1]`. Secant slope 0,
  but `f' = ±1` wherever it exists.

## `taylor_theorem`
**Specialization:** `n = 1` is exactly the MVT. `f` a polynomial of degree `< n`
⇒ remainder is 0. `e^x` at 0, degree 4: `P_4(1) = 65/24 ≈ 2.7083`,
`|R_4| ≈ 0.00995 < e/120 ≈ 0.0227` (`instance-checks.bc`).
**Counterexample:** drop *`f ∈ Cⁿ`*: `f(x) = x²·sin(1/x)` (`f(0)=0`) is
differentiable once but `f''` does not exist at 0 — no 2nd-order Taylor with a
Lagrange remainder there.

## `riemann_integral` / `continuous_implies_integrable`
**Specializations:** a constant `c` on `[a,b]` → `c(b−a)`. A step function →
sum of rectangle areas. A monotone function → integrable
(`monotone_implies_integrable`).
**Counterexamples:**
- drop *bounded*: `f(x) = 1/√x` on `(0,1]` (with any value at 0) is unbounded —
  not Riemann integrable (it is improperly integrable; out of scope).
- drop *continuity* **and** *monotonicity*: the Dirichlet function `1_ℚ` on
  `[0,1]` has `L(f,P) = 0`, `U(f,P) = 1` for every `P` — not integrable.
- keep continuity, note it is not necessary: `1_{[1/2,1]}` on `[0,1]` is
  discontinuous at `1/2` yet integrable (value `1/2`). "Continuous ⇒ integrable"
  is one-directional.

## `ftc_part1` / `ftc_part2`
**Specialization:** `f ≡ 1` ⇒ `F(x) = x − a`, `F' = 1`. FTC II with `f = G'`
polynomial recovers the power rule for integrals.
**Counterexamples:**
- FTC I, drop *`f` continuous at `x`*: with `f = 1_{[c,b]}` on `[a,b]`,
  `F(x) = ∫_a^x f` has a corner at `c`; `F'(c)` does not exist though `F` is
  still continuous.
- FTC II, drop *`G` an antiderivative everywhere*: `G(x) = |x|` on `[−1,1]` is
  not differentiable at 0, and `∫_{−1}^{1} G'` (defined a.e. as `sgn`) is `0`,
  but `G(1) − G(−1) = 0` only by coincidence of symmetry; take `G` with a jump
  and the identity fails outright.
- FTC II, drop *`f` integrable*: with `f` = derivative of Volterra's function
  (bounded, not Riemann integrable; out of scope, noted) the RHS makes sense but
  the LHS does not.

## `uniform_convergence` / `uniform_limit_continuous`
**Specialization:** if the `f_n` are eventually equal to `f`, convergence is
uniform. Uniform convergence on `D` ⇒ uniform on every subset of `D`.
**Counterexamples:**
- drop *uniform* (keep pointwise): `f_n(x) = x^n` on `[0,1]` → a discontinuous
  limit; `sup_x|f_n − f| = 1` for all `n` (`instance-checks.bc`). The limit is
  not continuous.
- drop *`f_n` continuous*: uniform limit of discontinuous functions can be
  anything a uniform limit can be — e.g. `f_n = 1_{[1/n, 1]}` → `1_{(0,1]}`
  uniformly on `[δ,1]`; each `f_n` and the limit are discontinuous.
- domain matters: `x^n` → 0 **uniformly** on `[0, 0.9]` (`sup = 0.9^n → 0`).

## `weierstrass_m_test`
**Specialization:** `f_n(x) = x^n/2^n` on `[−1,1]`: `|f_n| ≤ 2^{−n}`,
`Σ 2^{−n} = 1 < ∞` ⇒ `Σ f_n` converges uniformly (it is `1/(1 − x/2)`).
**The M-test is sufficient, not necessary** (recorded on the node):
`f_n(x) = (−1)^n x^n / n` on `[0,1]` has `sup_x |f_n(x)| = 1/n`, so
`Σ sup|f_n| = Σ 1/n = ∞` and the M-test does **not** apply — yet `Σ f_n`
converges uniformly on `[0,1]` (Abel/Dirichlet test: `Σ(−1)^n/n` converges and
`x^n` is monotone and uniformly bounded). So a failed M-test is not a proof of
non-uniform convergence.
**Genuine counterexample to interchange without uniformity:** `f_n(x) = x^n` on
`[0,1)` converges pointwise to `0`, `∫_0^1 f_n = 1/(n+1) → 0` here so integration
survives, but on `g_n = n·1_{(0,1/n)}` (spike): `g_n → 0` pointwise while
`∫_0^1 g_n = 1` for all `n` — the limit and the integral do not commute because
convergence is not uniform.

## `geometric_series`
**Specialization:** `r = 0` ⇒ sum `1`. `r = 1/2` ⇒ sum `2`
(`instance-checks.bc`: partial(0..60) = 1.9999…).
**Counterexamples:** `r = 1` ⇒ partial sums `= n+1 → ∞`. `r = −1` ⇒ partial
sums oscillate `1,0,1,0,…`, no limit. `r = 2` ⇒ `2^{n+1}−1 → ∞`. The hypothesis
`|r| < 1` is exactly the boundary.
