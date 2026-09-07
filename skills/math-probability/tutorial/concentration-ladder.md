# The concentration ladder

> Generated from the `math-probability` capsule (Release 0.1) with the
> `theorem-tree-tutorial` skill. The mathematics, the prerequisite order, and
> every calculation and proof come from that capsule —
> `validation/proof-checks.lean` and each result's YAML entry in particular.

There is one inequality in probability — **Markov's** — and four theorems that
are just Markov applied to a cleverer function each time:

| apply Markov to … | and you get |
|---|---|
| `(X − μ)²` | **Chebyshev** — a polynomial tail from the variance |
| `e^{tX}`, optimised over `t` | **Chernoff** — an *exponential* tail from the MGF |
| `e^{tX}` for a bounded centred `X` | **Hoeffding's lemma** — a sub-Gaussian MGF bound |
| the Chernoff bound to a sum of independent bounded terms | **Hoeffding's inequality** — a distribution-free bound on a sample mean |

Each rung is tighter and needs a stronger hypothesis. This tutorial climbs the
ladder on concrete distributions, runs the capsule's kernel-checked core of each
step, and — at every rung — drops the hypothesis and watches the bound break.

## How to run this

Install [`upmd`](https://upmd.dev), then from the repository root:

- `upmd skills/math-probability/tutorial/concentration-ladder.md` — the walk.
- `upmd --ci --all skills/math-probability/tutorial/concentration-ladder.md` —
  run every check (the gate).
- `upmd --ci -b capstone skills/math-probability/tutorial/concentration-ladder.md`
  — the sample-size payoff and its chain.

Blocks `deps:` earlier ones in the capsule's partial order. The `lean_…` blocks
call the Lean 4 kernel through a shell wrapper (`upmd` has no Lean runner); if
`lean` is absent they print `SKIP` and exit 0.

## What you need first

**Expectation** and its linearity and monotonicity; **variance** and
`Var(X) = E[X²] − E[X]²`; the **indicator** `1_A` with `E[1_A] = P(A)`;
**convex functions** and the supporting-line inequality; the **moment
generating function** `M_X(t) = E[e^{tX}]` and the fact that MGFs of independent
variables **multiply**. All of these are earlier nodes in the same capsule —
here they are used, not rebuilt.

Every result below is `choice_free` and `constructive`. The first three
(`markov`, `chebyshev`, `jensen`) carry a **genuine, universal** Lean core; the
last three (`chernoff`, `hoeffding_lemma`, `hoeffding_inequality`) are
`lean_status: cited` — they need `exp`/`log`, i.e. Mathlib — so those rungs get
the kernel core of the *Markov step underneath them* plus a cited reference.

Numbers use `bc -l` decimals with tolerance comparisons — these bounds are
genuinely transcendental (`e^{-4.5}`, `cosh 1`), not exact rationals.

---

## 0. Setup

```bash [name:setup]
export PI="$(echo 'scale=30; 4*a(1)' | bc -l)"
export TOL="0.0000001"
echo "pi and a comparison tolerance loaded"
```

## 1. Markov's inequality — the whole ladder in one line

**`markov_inequality`**: if `X ≥ 0` almost surely and `a > 0`, then
`P(X ≥ a) ≤ E[X] / a`. The proof is one pointwise inequality:
`a · 1_{X ≥ a} ≤ X · 1_{X ≥ a} ≤ X` (this is where `X ≥ 0` is used), then take
expectations. `status_label: proved_theorem`, `lean_status: core`. The two
hypotheses — **`X ≥ 0`** and **`a > 0`** — are both essential; §1's
counterexample drops the first. Markov is usually *very* loose (tight only for a
two-point `{0, a}` law); its value is that it needs nothing but the mean.
*(Billingsley; Boucheron–Lugosi–Massart.)*

```bash [name:chk_markov_inequality, deps:setup]
# X ~ Exponential(1): E[X] = 1.  Tail at a = 3.
a=3
actual=$(echo "scale=10; e(-$a)" | bc -l)              # P(X >= 3) = e^-3
bound=$(echo "scale=10; 1/$a" | bc -l)                 # Markov: E[X]/a = 1/3
echo "X ~ Exp(1),  a = $a"
echo "  P(X >= a) exact  = $actual"
echo "  Markov bound E/a = $bound        (want >= exact; loose)"
ok=$(echo "$bound >= $actual" | bc -l); [ "$ok" = 1 ] || { echo "FAIL"; exit 1; }
# the tight case: two-point law X in {0, a}, P(X = a) = q
q=0.2
echo "two-point X in {0,$a}, P(X=$a) = $q:  P(X>=a) = $q,  bound = E/a = (a*q)/a = $q  -> EQUAL"
```

```bash [name:lean_markov_inequality, deps:setup]
command -v lean >/dev/null || { echo "SKIP: lean not on PATH"; exit 0; }
d=$(mktemp -d)
cat > "$d/mk.lean" <<'LEAN'
-- math-probability/validation/proof-checks.lean, section 4 (Prob.markov_finite)
-- Markov, finite support, GENUINE and universal by list induction.
-- tailmass a X = sum of weights p_i with value x_i >= a  (the mass of {X >= a}).
-- For nonnegative integer weights/values and a >= 1:  a * P(X >= a) <= E[X].
def wsum : List (Int × Int) → Int
  | []          => 0
  | (p, x) :: t => p * x + wsum t
def tailmass (a : Int) : List (Int × Int) → Int
  | []          => 0
  | (p, x) :: t => (if a ≤ x then p else 0) + tailmass a t
theorem markov_finite (a : Int) (ha : 1 ≤ a) :
    ∀ (X : List (Int × Int)), (∀ q ∈ X, 0 ≤ q.1 ∧ 0 ≤ q.2) →
      a * tailmass a X ≤ wsum X := by
  intro X
  induction X with
  | nil => simp [tailmass, wsum]
  | cons hd tl ih =>
    intro hpos
    obtain ⟨p, x⟩ := hd
    have hp : 0 ≤ p := (hpos (p, x) (by simp)).1
    have hx : 0 ≤ x := (hpos (p, x) (by simp)).2
    have htl : a * tailmass a tl ≤ wsum tl := ih (fun q hq => hpos q (by simp [hq]))
    simp only [tailmass, wsum, Int.mul_add]
    by_cases hc : a ≤ x
    · simp only [hc, if_true]
      have h1 : a * p ≤ x * p := Int.mul_le_mul_of_nonneg_right hc hp
      have h2 : x * p = p * x := Int.mul_comm x p
      omega
    · simp only [hc, if_false, Int.mul_zero]
      have h3 : 0 ≤ p * x := Int.mul_nonneg hp hx
      omega
LEAN
if lean "$d/mk.lean" 2>/dev/null; then
  echo "kernel accepted, for EVERY finite nonnegative law:  a * P(X >= a) <= E[X]"
  echo "the induction: each outcome either clears the threshold (contributes p*x >= a*p)"
  echo "or does not (contributes p*x >= 0).  This is Markov."
else
  echo "FAIL: lean rejected markov_finite"; rm -rf "$d"; exit 1
fi
rm -rf "$d"
```

```bash [name:cx_markov_inequality, deps:chk_markov_inequality]
# drop X >= 0: a mean-zero two-point law X in {-M, M}, each with probability 1/2
m=10; a=5
p_tail="0.5"                        # P(X >= 5) = P(X = 10) = 1/2
e_over_a=$(echo "scale=10; 0/$a" | bc -l)   # E[X] = 0, so E[X]/a = 0
echo "X in {-$m, $m} each prob 1/2,  E[X] = 0,  a = $a"
echo "  P(X >= a)   = $p_tail"
echo "  E[X] / a    = $e_over_a"
echo "  $p_tail  >  $e_over_a   => Markov violated. The one-sided X >= 0 is essential;"
echo "  for a signed X you must centre and take |.|  (that is the next rung)."
ok=$(echo "$p_tail > $e_over_a" | bc -l); [ "$ok" = 1 ] || { echo "FAIL"; exit 1; }
```

### In the wild

Markov is rarely quoted raw, but it is the base of everything above it and of
the **probabilistic method** (Erdős): to prove an object with no bad feature
exists, show `E[# bad features] < 1`, so `P(≥1 bad) < 1` by Markov — the first
lower bounds on Ramsey numbers and the existence proofs for good
error-correcting codes and expander graphs. In algorithm analysis, "expected
time `T`" plus Markov gives "time `≤ 2T` with probability `≥ ½`", then
independent repetition amplifies.

## 2. Chebyshev — Markov on the squared deviation

**`chebyshev_inequality`**: if `Var(X) < ∞` and `k > 0`, then
`P(|X − E[X]| ≥ k) ≤ Var(X) / k²`. `derives_from: markov_inequality` — apply it
to the nonnegative variable `Y = (X − μ)²` with threshold `k²`:
`P(|X − μ| ≥ k) = P(Y ≥ k²) ≤ E[Y]/k² = Var(X)/k²`. The step
`{|X − μ| ≥ k} = {(X − μ)² ≥ k²}` is the kernel core below. The hypothesis is
**finite variance**; drop it and the polynomial `1/k²` decay is simply false
(§2 counterexample). Chebyshev is two-sided and still loose — it is what the
weak law of large numbers is built on, nothing sharper. *(Billingsley;
Grimmett–Stirzaker.)*

```bash [name:chk_chebyshev_inequality, deps:chk_markov_inequality]
# X ~ Exponential(1): mu = 1, Var = 1.  Deviation k = 3.
k=3
# P(|X - 1| >= 3) = P(X >= 4) + P(X <= -2) = P(X >= 4) = e^-4  (X >= 0)
actual=$(echo "scale=10; e(-4)" | bc -l)
bound=$(echo "scale=10; 1/($k*$k)" | bc -l)            # Var/k^2 = 1/9
echo "X ~ Exp(1),  mu = 1, Var = 1,  k = $k"
echo "  P(|X - mu| >= k) exact = $actual"
echo "  Chebyshev  Var/k^2     = $bound        (want >= exact)"
ok=$(echo "$bound >= $actual" | bc -l); [ "$ok" = 1 ] || { echo "FAIL"; exit 1; }
# the "c standard deviations" form: k = c*sd, bound = 1/c^2
echo "k = 2 sd  =>  P(|X - mu| >= 2 sd) <= 1/4 = $(echo "scale=4; 1/4" | bc -l)  (distribution-free)"
```

```bash [name:lean_chebyshev_inequality, deps:setup]
command -v lean >/dev/null || { echo "SKIP: lean not on PATH"; exit 0; }
d=$(mktemp -d)
cat > "$d/cheb.lean" <<'LEAN'
-- math-probability/validation/proof-checks.lean, section 6 (Prob.chebyshev_reduction_fwd)
-- the reduction Chebyshev needs: { |y| >= k }  is contained in  { y^2 >= k^2 },
-- for k >= 0.  GENUINE, universal over the integers.
theorem chebyshev_reduction_fwd (y k : Int) (hk : 0 ≤ k)
    (h : k ≤ y ∨ y ≤ -k) : k * k ≤ y * y := by
  rcases h with h | h
  · exact Int.mul_le_mul h h hk (by omega)
  · have := Int.mul_le_mul (by omega : k ≤ -y) (by omega : k ≤ -y) hk (by omega)
    have e : (-y) * (-y) = y * y := by grind
    omega
LEAN
if lean "$d/cheb.lean" 2>/dev/null; then
  echo "kernel accepted, all integers, k >= 0:  (k <= y  or  y <= -k)  =>  k^2 <= y^2"
  echo "so P(|X - mu| >= k) <= P((X - mu)^2 >= k^2), and Markov on (X - mu)^2 finishes:"
  echo "  <= E[(X - mu)^2] / k^2  =  Var(X) / k^2."
else
  echo "FAIL: lean rejected chebyshev_reduction_fwd"; rm -rf "$d"; exit 1
fi
rm -rf "$d"
```

```bash [name:cx_chebyshev_inequality, deps:chk_chebyshev_inequality]
# drop finite variance: X ~ Cauchy.  Var and even E do not exist.
# P(|X| >= k) = 1 - (2/pi) arctan(k) = (2/pi) arctan(1/k).
p10=$(echo "scale=10; (2/$PI) * a(1/10)" | bc -l)
p20=$(echo "scale=10; (2/$PI) * a(1/20)" | bc -l)
r=$(echo "scale=4; $p10 / $p20" | bc -l)
echo "X ~ Cauchy:  P(|X| >= 10) = $p10"
echo "             P(|X| >= 20) = $p20"
echo "  ratio P(10)/P(20) = $r    (~2, i.e. 1/k decay -- would be ~4 for 1/k^2)"
echo "The Cauchy tail is 1/k, not 1/k^2. No finite variance => no Chebyshev bound."
# 1/k decay: k * P(|X| >= k) -> constant (2/pi)
c10=$(echo "scale=6; 10 * $p10" | bc -l)
echo "  k * P(|X| >= k) at k=10 : $c10   (-> 2/pi = $(echo "scale=6; 2/$PI" | bc -l), a constant)"
ok=$(echo "$r < 3" | bc -l); [ "$ok" = 1 ] || { echo "FAIL: expected ~1/k, not ~1/k^2"; exit 1; }
```

### In the wild

Chebyshev on the sample mean *is* the weak law of large numbers, so the **margin
of error in every opinion poll** traces back to this inequality. It also powers
one-pass **streaming algorithms**: the AMS frequency-moment sketch (Alon–Matias–
Szegedy, 2005 Gödel Prize) bounds its estimator with Chebyshev, then "median of
means" boosts confidence — HyperLogLog, the unique-visitor counter in Redis,
BigQuery, and Presto, is a descendant.

```bash [name:app_chebyshev_inequality, deps:chk_chebyshev_inequality]
# Chebyshev sample size for a poll: P(|Xbar - p| >= eps) <= Var(Xbar)/eps^2
#   <= (1/4)/(n eps^2) <= delta   =>   n >= 1/(4 delta eps^2)
eps="0.03"; delta="0.05"
# NB: compute at high scale (bc truncates intermediate products), round up at the end
n=$(echo "scale=8; x = 1 / (4 * $delta * $eps * $eps); scale=0; x/1 + 1" | bc -l)
echo "poll to within eps = $eps at 95% confidence, distribution-free (Chebyshev):"
echo "  n >= 1/(4 delta eps^2) = $n respondents"
echo "  (the CLT / Hoeffding refine this by ~10x -- see the capstone)"
```

## 3. Jensen — the convexity that makes Chernoff possible

**`jensen_inequality`**: if `φ` is convex and `X, φ(X)` are integrable, then
`φ(E[X]) ≤ E[φ(X)]`. Proof: the supporting line `L` at `c = E[X]` has
`L ≤ φ` everywhere and `L(E[X]) = φ(E[X])`, so
`E[φ(X)] ≥ E[L(X)] = L(E[X]) = φ(E[X])`. The kernel core below is the case
`φ(x) = x²` on a two-point law, proved **universally** via the factorisation
`n·(t x² + (n−t) y²) − (t x + (n−t) y)² = t(n−t)(x−y)² ≥ 0`. The one hypothesis
is **convexity**; for a *concave* `φ` the inequality reverses — the single most
common misuse (§3 counterexample). Taking `φ(x) = e^x` gives
`e^{E[X]} ≤ E[e^X]`, which is exactly what turns the Chernoff exponent into
something you can bound. *(Boucheron–Lugosi–Massart; Durrett.)*

```bash [name:chk_jensen_inequality, deps:setup]
# two-point law X in {0, 2}, each probability 1/2.  E[X] = 1.
# phi(x) = e^x  (convex):
lhs=$(echo "scale=10; e(1)" | bc -l)                        # e^{E[X]}
rhs=$(echo "scale=10; (e(0) + e(2)) / 2" | bc -l)           # E[e^X]
echo "phi = exp,  X in {0,2} each 1/2:"
echo "  e^{E[X]}  = $lhs"
echo "  E[e^X]    = $rhs        (want >= LHS: convex)"
ok=$(echo "$rhs >= $lhs" | bc -l); [ "$ok" = 1 ] || { echo "FAIL"; exit 1; }
# phi(x) = x^2:  E[X]^2 = 1  <=  E[X^2] = (0 + 4)/2 = 2   (this is Var(X) >= 0)
echo "phi = square:  E[X]^2 = 1  <=  E[X^2] = 2   (i.e. Var(X) = 1 >= 0)"
```

```bash [name:lean_jensen_inequality, deps:setup]
command -v lean >/dev/null || { echo "SKIP: lean not on PATH"; exit 0; }
d=$(mktemp -d)
cat > "$d/jen.lean" <<'LEAN'
-- math-probability/validation/proof-checks.lean, section 7 (Prob.jensen_sq)
-- Jensen for phi = square, two-point law with weights t and n-t (t/n in [0,1]).
-- GENUINE, universal in t, x, y, n via the factorization t(n-t)(x-y)^2 >= 0.
theorem sq_nonneg' (z : Int) : 0 ≤ z * z := by
  rcases Int.le_total 0 z with h | h
  · exact Int.mul_nonneg h h
  · have : 0 ≤ (-z) * (-z) := Int.mul_nonneg (by omega) (by omega)
    have e : (-z) * (-z) = z * z := by grind
    omega
theorem jensen_sq (n t x y : Int) (h0 : 0 ≤ t) (h1 : t ≤ n) (hn : 0 < n) :
    (t * x + (n - t) * y) * (t * x + (n - t) * y)
      ≤ n * (t * (x * x) + (n - t) * (y * y)) := by
  have key : n * (t * (x * x) + (n - t) * (y * y))
               - (t * x + (n - t) * y) * (t * x + (n - t) * y)
             = (t * (n - t)) * ((x - y) * (x - y)) := by grind
  have h2 : 0 ≤ t * (n - t) := Int.mul_nonneg h0 (by omega)
  have h3 : 0 ≤ (x - y) * (x - y) := sq_nonneg' _
  have h4 : 0 ≤ (t * (n - t)) * ((x - y) * (x - y)) := Int.mul_nonneg h2 h3
  omega
LEAN
if lean "$d/jen.lean" 2>/dev/null; then
  echo "kernel accepted, all t,x,y,n with 0 <= t <= n, 0 < n:"
  echo "  (t x + (n-t) y)^2  <=  n (t x^2 + (n-t) y^2)"
  echo "i.e. phi(E[X])  <=  E[phi(X)]  for phi = square -- the gap is t(n-t)(x-y)^2."
else
  echo "FAIL: lean rejected jensen_sq"; rm -rf "$d"; exit 1
fi
rm -rf "$d"
```

```bash [name:cx_jensen_inequality, deps:chk_jensen_inequality]
# drop convexity: phi(x) = sqrt(x)  is CONCAVE.  X in {1, 9} each prob 1/2.
ex=5                                                  # E[X] = (1 + 9)/2
lhs=$(echo "scale=10; sqrt($ex)" | bc -l)             # phi(E[X]) = sqrt(5)
rhs=$(echo "scale=10; (sqrt(1) + sqrt(9)) / 2" | bc -l)   # E[phi(X)] = (1 + 3)/2 = 2
echo "phi = sqrt (concave),  X in {1,9} each 1/2,  E[X] = $ex:"
echo "  phi(E[X]) = sqrt(5) = $lhs"
echo "  E[phi(X)] = 2        = $rhs"
echo "  $lhs  >  $rhs   => the inequality REVERSED. Jensen needs phi convex;"
echo "  for concave phi you get phi(E[X]) >= E[phi(X)]."
ok=$(echo "$lhs > $rhs" | bc -l); [ "$ok" = 1 ] || { echo "FAIL"; exit 1; }
```

### In the wild

Jensen on `−log` is **Gibbs' inequality** — the KL divergence is `≥ 0` — which is
the entropy bound behind every ZIP, PNG, and FLAC, and the reason the **EM
algorithm** (Gaussian mixtures, speech HMMs, topic models) and the **ELBO** that
trains variational autoencoders both work: each maximises a Jensen lower bound
on a log-likelihood. In finance, `E[log(1+R)] ≤ log(1+E[R])` is "volatility
drag"; concave utility is why risk-averse agents buy insurance.

```bash [name:app_jensen_inequality, deps:chk_jensen_inequality]
# Gibbs' inequality: KL(p || q) = sum p_i log(p_i / q_i) >= 0, with equality iff p = q.
# p = true letter frequencies (toy), q = a wrong model.
echo "KL(p || q) = sum p_i ln(p_i / q_i)  for two 4-symbol distributions:"
kl=$(echo "scale=8
  p[0]=0.4; p[1]=0.3; p[2]=0.2; p[3]=0.1
  q[0]=0.25; q[1]=0.25; q[2]=0.25; q[3]=0.25
  s = 0
  for (i = 0; i < 4; i++) s += p[i] * l(p[i]/q[i])
  s" | bc -l)
echo "  KL(p || uniform) = $kl  nats   (>= 0, and > 0 since p != uniform)"
echo "  => you cannot compress p-distributed data below H(p); a wrong model q costs"
echo "     exactly KL(p||q) extra nats per symbol."
ok=$(echo "$kl > 0" | bc -l); [ "$ok" = 1 ] || { echo "FAIL: KL must be >= 0"; exit 1; }
```

## 4. Chernoff — Markov on `e^{tX}`, then optimise

**`chernoff_bound`**: for any `X` with an MGF and any `a`,
`P(X ≥ a) ≤ inf_{t > 0} e^{−ta} M_X(t)`. `derives_from: markov_inequality`: for
fixed `t > 0`, `{X ≥ a} = {e^{tX} ≥ e^{ta}}`, and Markov on the nonnegative
`e^{tX}` gives `P(X ≥ a) ≤ e^{−ta} M_X(t)`; then take the best `t`. Epistemic
status: `proved_theorem`, but **`lean_status: cited`** — the kernel core is the
Markov step (§1's `markov_finite`); the `e^{tX}` transform and the optimisation
are `exp`/`log` and live outside the Mathlib-free capsule. The hypothesis is
**the MGF exists for some `t > 0`**; a heavy tail has `M_X(t) = ∞` and the bound
says nothing (§4 counterexample). *(Boucheron–Lugosi–Massart; Durrett.)*

```bash [name:chk_chernoff_bound, deps:"chk_markov_inequality | chk_jensen_inequality"]
# X ~ N(0,1):  M_X(t) = e^{t^2/2}.  Bound at a = 3 is  inf_t e^{-3t + t^2/2}.
a=3
# exponent -a t + t^2/2 is minimised at t = a; value e^{-a^2/2}
best=$(echo "scale=10; e(-($a*$a)/2)" | bc -l)
# a single, un-optimised t = 1:
one=$(echo "scale=10; e(-$a*1 + 1/2)" | bc -l)
actual="0.00135"                                     # P(Z >= 3), from a table
cheb=$(echo "scale=10; 1/($a*$a)" | bc -l)           # Chebyshev for comparison
echo "X ~ N(0,1),  a = $a:"
echo "  P(Z >= a) actual        ~ $actual"
echo "  Chernoff (optimised t=a) = $best      (e^{-a^2/2})"
echo "  Chernoff (single t = 1)  = $one      (valid, but loose -- optimise!)"
echo "  Chebyshev  Var/a^2       = $cheb       (polynomial: 10x looser than Chernoff)"
ok=$(echo "$best >= $actual && $one >= $best && $cheb > $best" | bc -l)
[ "$ok" = 1 ] || { echo "FAIL: ladder order violated"; exit 1; }
```

```bash [name:cx_chernoff_bound, deps:chk_chernoff_bound]
# drop MGF existence: X ~ Cauchy.  M_X(t) = E[e^{tX}] = integral e^{tx}/(pi(1+x^2)) dx.
# For any t > 0 the integrand ~ e^{tx}/x^2 -> infinity; the integral diverges.
t="0.5"
prev=0
echo "X ~ Cauchy,  t = $t:  partial integral of e^{tx}/(pi(1+x^2)) over [-R, R]:"
for r in 5 10 15 20 25; do
  # crude midpoint sum, step 0.5
  s=$(echo "scale=8
    total = 0
    for (x = -$r; x < $r; x += 0.5) { total += e($t*(x+0.25)) / ($PI*(1 + (x+0.25)^2)) * 0.5 }
    total" | bc -l)
  echo "  R = $r :  ~ $s"
  prev=$s
done
echo "It grows without bound: M_X(t) = infinity for every t > 0."
echo "=> inf_t e^{-ta} M_X(t) = infinity. The Chernoff bound is vacuous for Cauchy;"
echo "   only the polynomial bounds (Markov/Chebyshev/moment) can say anything."
big=$(echo "$prev > 5" | bc -l); [ "$big" = 1 ] || { echo "FAIL: expected divergence"; exit 1; }
```

### In the wild

Chernoff bounds are *the* tool of randomized-algorithm analysis: **randomized
rounding** (LP relaxation → round → Chernoff shows near-optimality) for routing
and scheduling; the **Johnson–Lindenstrauss lemma** (`k = O(ε⁻² log n)` random
projections preserve all pairwise distances — a Chernoff bound on a χ²) behind
nearest-neighbour search and compressed sensing; the **error exponent** in
Shannon's coding theorems; and committee-based blockchains (Algorand, Ouroboros)
bounding an adversary's chance of capturing a random committee.

```bash [name:app_chernoff_bound, deps:chk_chernoff_bound]
# Johnson-Lindenstrauss: to embed n points into R^k with all pairwise distances
# within (1 +- eps), it suffices that k >= (8 / eps^2) * ln(n)  (a Chernoff bound).
for npts in 1000 1000000; do
  for eps in 0.1 0.3; do
    k=$(echo "scale=8; x = (8 / ($eps * $eps)) * l($npts); scale=0; x/1 + 1" | bc -l)
    echo "  n = $npts points, eps = $eps :  k >= (8/eps^2) ln n = $k dimensions"
  done
done
echo "  ^ independent of the original dimension -- 1e6 points compress to a few"
echo "    thousand coordinates with distances essentially intact."
```

## 5. Hoeffding's lemma — a bounded, centred variable is sub-Gaussian

**`hoeffding_lemma`**: if `a ≤ X ≤ b` almost surely and `E[X] = 0`, then
`M_X(t) ≤ exp(t² (b − a)² / 8)` for every real `t`. Proof: `e^{tx}` is convex, so
on `[a, b]` it lies below its chord; take expectations (using `E[X] = 0`), then
show the log of the bound has second derivative `≤ (b − a)²/4` and integrate
twice. `status_label: proved_lemma`, `lean_status: cited` (Hoeffding 1963). The
hypothesis is **boundedness**; an unbounded centred variable is at best
sub-*exponential*, not sub-Gaussian (§5 counterexample). This lemma is the only
new ingredient between Chernoff and Hoeffding's inequality. *(Hoeffding 1963;
Boucheron–Lugosi–Massart Lemma 2.2.)*

```bash [name:chk_hoeffding_lemma, deps:"chk_jensen_inequality | chk_chernoff_bound"]
# symmetric two-point X in {-1, +1} each prob 1/2:  a = -1, b = 1, E[X] = 0.
# M_X(t) = (e^{-t} + e^{t})/2 = cosh(t).   Bound: e^{t^2 (b-a)^2 / 8} = e^{t^2 * 4 / 8} = e^{t^2/2}.
for t in 0.5 1 2; do
  mgf=$(echo "scale=10; (e(-$t) + e($t)) / 2" | bc -l)
  bound=$(echo "scale=10; e($t*$t / 2)" | bc -l)
  echo "t = $t :  M_X(t) = cosh(t) = $mgf   <=   e^{t^2/2} = $bound"
  ok=$(echo "$bound >= $mgf" | bc -l); [ "$ok" = 1 ] || { echo "FAIL at t=$t"; exit 1; }
done
echo "(b-a)^2 / 8 = 4/8 = 1/2, so the sub-Gaussian parameter is (b-a)/2 = 1 -- exact"
echo "for this symmetric law."
```

### In the wild

"Bounded ⇒ sub-Gaussian" is the hypothesis under essentially all of
high-dimensional statistics and the analysis of stochastic optimisation
(Wainwright 2019). It is the single ingredient added between the Chernoff bound
and Hoeffding's inequality below.

```bash [name:cx_hoeffding_lemma, deps:chk_hoeffding_lemma]
# drop boundedness: X = Y - 1 with Y ~ Exponential(1).  E[X] = 0, but X in [-1, infinity).
# M_X(t) = e^{-t} E[e^{tY}] = e^{-t} / (1 - t)   for t < 1.
echo "centred exponential X = Y - 1,  Y ~ Exp(1):  M_X(t) = e^{-t}/(1-t)"
for t in 0.5 0.9 0.99; do
  mgf=$(echo "scale=8; e(-$t) / (1 - $t)" | bc -l)
  # smallest sub-Gaussian constant c that would work at this t:  c >= ln(M) / t^2
  cmin=$(echo "scale=6; l($mgf) / ($t*$t)" | bc -l)
  echo "  t = $t :  M_X(t) = $mgf ,  needs a sub-Gaussian constant c >= $cmin"
done
echo "As t -> 1 the MGF blows up while any e^{c t^2} stays finite: the required c"
echo "keeps growing. X is sub-EXPONENTIAL, not sub-Gaussian -- Hoeffding's lemma"
echo "fails, and Bernstein's inequality takes over."
final=$(echo "scale=8; e(-0.99)/(1-0.99)" | bc -l)
big=$(echo "$final > 30" | bc -l); [ "$big" = 1 ] || { echo "FAIL: expected blow-up"; exit 1; }
```

## 6. Hoeffding's inequality — the distribution-free bound on a sample mean

**`hoeffding_inequality`**: if `X_1, …, X_n` are **independent** with
`a_i ≤ X_i ≤ b_i` a.s. and `S = Σ X_i`, then
`P(S − E[S] ≥ s) ≤ exp(−2 s² / Σ_i (b_i − a_i)²)`. Proof: Chernoff on `S − E[S]`,
the MGF factorises by independence (`mgf_sum_independent`), and Hoeffding's lemma
bounds each factor; then optimise `t`. `lean_status: cited` (the Markov/Chernoff
core is `markov_finite`; the rest is algebra). **Two** hypotheses:
**boundedness** of each `X_i` and **independence** — §6's counterexample drops
independence. For `X_i ∈ [0,1]` the sample-mean form is
`P(X̄ − E[X̄] ≥ ε) ≤ e^{−2 n ε²}` — the workhorse of empirical means, bandits,
and PAC learning. *(Hoeffding 1963; Boucheron–Lugosi–Massart.)*

```bash [name:chk_hoeffding_inequality, deps:"chk_hoeffding_lemma | chk_chernoff_bound | chk_chebyshev_inequality"]
# n = 100 fair coin flips.  X_i in [0,1], S = #heads, E[S] = 50.  Deviation s = 15.
n=100; s=15
hoeff=$(echo "scale=12; e(-2 * $s*$s / $n)" | bc -l)      # exp(-2 s^2 / n),  b_i - a_i = 1
var_s=$(echo "scale=6; $n * (1/4)" | bc -l)               # Var(S) = n p(1-p) = 25
cheb=$(echo "scale=12; $var_s / ($s*$s)" | bc -l)         # Var(S)/s^2
# exact upper-tail binomial P(S >= 65), summed
exact=$(echo "scale=14
  bn = 1
  total = 0
  for (k = 0; k <= $n; k++) {
    if (k == 0) c = 1 else c = c * ($n - k + 1) / k
    if (k >= 65) total += c
  }
  total / (2 ^ $n)" | bc -l)
echo "n = $n fair flips,  deviation s = $s:"
echo "  P(S - 50 >= 15) exact (binomial) ~ $exact"
echo "  Hoeffding  e^{-2 s^2 / n}         = $hoeff        (want >= exact)"
echo "  Chebyshev  Var(S)/s^2            = $cheb        (polynomial: ~10x looser)"
ok=$(echo "$hoeff >= $exact && $cheb > $hoeff" | bc -l)
[ "$ok" = 1 ] || { echo "FAIL: ladder order violated"; exit 1; }
```

```bash [name:cx_hoeffding_inequality, deps:chk_hoeffding_inequality]
# drop independence: X_1 = ... = X_n = a single Bernoulli(1/2).  S = n * X_1 in {0, n}.
n=100; s=15
actual="0.5"                            # P(S - n/2 >= s) = P(X_1 = 1) = 1/2  (any s < n/2)
hoeff=$(echo "scale=12; e(-2 * $s*$s / $n)" | bc -l)
echo "X_1 = ... = X_$n = one Bernoulli(1/2)  (perfectly dependent),  S in {0, $n}:"
echo "  P(S - 50 >= $s) actual = $actual"
echo "  Hoeffding claims       <= $hoeff   (-> 0)"
echo "  $actual  >>  $hoeff   => Hoeffding violated. The MGF does not factorise"
echo "  without independence; Azuma / McDiarmid handle bounded-difference dependence."
ok=$(echo "$actual > $hoeff" | bc -l); [ "$ok" = 1 ] || { echo "FAIL"; exit 1; }
```

### In the wild

Hoeffding's inequality is the bound of machine learning: the **PAC generalisation
guarantee** (Valiant, Turing Award) — a union bound over a hypothesis class plus
Hoeffding per hypothesis — and the confidence radius in the **UCB bandit**
(ad selection, Yahoo front-page news via LinUCB), which is also the selection
rule in the **Monte Carlo Tree Search inside AlphaGo** (UCT). Streaming
**Hoeffding trees** split a decision-tree node once the bound certifies the
winning attribute; **differential privacy** (RAPPOR, Apple telemetry, the 2020
US Census) states its accuracy this way.

```bash [name:app_hoeffding_inequality, deps:chk_hoeffding_inequality]
# PAC: how many labelled examples to pick the best of |H| candidate rules,
# to within eps error, with confidence 1 - delta?   n >= ln(|H|/delta) / (2 eps^2)
eps="0.02"; delta="0.05"
for h in 1000 1000000; do
  n=$(echo "scale=8; x = l($h / $delta) / (2 * $eps * $eps); scale=0; x/1 + 1" | bc -l)
  echo "  |H| = $h , eps = $eps , 95% conf :  n >= ln(|H|/delta)/(2 eps^2) = $n examples"
done
# the UCB exploration radius as a bandit run progresses (arm pulled n_i of t rounds):
echo
for t in 100 10000 1000000; do
  ni=$(( t / 10 ))
  radius=$(echo "scale=4; sqrt(2 * l($t) / $ni)" | bc -l)
  echo "  UCB radius at t = $t, arm pulled $ni times :  sqrt(2 ln t / n_i) = $radius"
done
```

---

## Capstone — how many samples?

*You want to estimate a coin's bias `p` to within `ε = 0.05`, with 99%
confidence (`δ = 0.01`). How many flips?*

```bash [name:capstone, deps:"chk_hoeffding_inequality | cx_hoeffding_inequality | lean_markov_inequality | app_hoeffding_inequality"]
eps="0.05"; delta="0.01"
echo "================================================================"
echo "  estimate p to within eps = $eps at confidence 1 - delta = 0.99"
echo "================================================================"
echo
echo "  The ladder, one idea (Markov) applied to a cleverer function each rung:"
echo "    Markov      P(X >= a) <= E[X]/a                     [genuine Lean core]"
echo "    Chebyshev   Markov on (X - mu)^2   -> Var/k^2       [genuine Lean core]"
echo "    Jensen      convexity, makes e^{tX} tractable       [genuine Lean core]"
echo "    Chernoff    Markov on e^{tX}, optimise t -> exp tail [cited: needs exp]"
echo "    Hoeffding L bounded + centred => sub-Gaussian MGF   [cited: Hoeffding 63]"
echo "    Hoeffding I Chernoff + indep MGFs + the lemma       [cited: assembly]"
echo
# Hoeffding two-sided:  P(|Xbar - p| >= eps) <= 2 e^{-2 n eps^2} <= delta
#   => n >= ln(2/delta) / (2 eps^2)
n_hoeff=$(echo "scale=4; l(2/$delta) / (2 * $eps*$eps)" | bc -l)
# Chebyshev:  Var(Xbar)/eps^2 <= (1/4)/(n eps^2) <= delta  => n >= 1/(4 delta eps^2)
n_cheb=$(echo "scale=4; 1 / (4 * $delta * $eps*$eps)" | bc -l)
echo "  Chebyshev needs   n >= 1/(4 delta eps^2)      = $n_cheb"
echo "  Hoeffding needs    n >= ln(2/delta)/(2 eps^2)  = $n_hoeff"
ratio=$(echo "scale=1; $n_cheb / $n_hoeff" | bc -l)
echo
echo "  Hoeffding's exponential tail buys a ${ratio}x smaller sample -- and it is"
echo "  still distribution-free (any bounded X_i, no variance estimate needed)."
ok=$(echo "$n_cheb > $n_hoeff" | bc -l); [ "$ok" = 1 ] || { echo "FAIL"; exit 1; }
echo
echo "  VERDICT: every rung is Markov wearing a different coat. The first three"
echo "  have a kernel-checked core in the capsule; the exponential rungs are"
echo "  cited (they need exp/log). All six are choice_free."
echo
echo "  IN THE WILD, all six rungs at once: the same sample-size arithmetic sets"
echo "  n for an A/B test, the width of a bandit's confidence interval (ad"
echo "  selection, AlphaGo's tree search), the target dimension of a random"
echo "  projection (nearest-neighbour search), and the PAC guarantee that a"
echo "  trained model generalises."
echo
echo "  WHERE IT BITES BACK: every rung needs its hypothesis. Recommender bandits"
echo "  misbehave when arms are not independent [cx_hoeffding_inequality]; a"
echo "  Chebyshev/CLT bound on financial losses is worthless when the loss has no"
echo "  finite variance [cx_chebyshev_inequality -- the 2008 tail]; and a"
echo "  concentration bound on a heavy-tailed metric is a false promise."
```

## Where to go next

- The full [`math-probability`](../SKILL.md) capsule — the modes of convergence,
  the laws of large numbers (Chebyshev/Markov are what the *weak* law is built
  on), the central limit theorem.
- `hoeffding_inequality`'s relatives, past this path: Bernstein (a variance
  bound + one-sided bound, tighter when variances are small), Azuma–Hoeffding
  and McDiarmid (bounded-difference dependence).
- Other cuts from this capsule: [`docs/tutorial-map.md`](../../../docs/tutorial-map.md).
