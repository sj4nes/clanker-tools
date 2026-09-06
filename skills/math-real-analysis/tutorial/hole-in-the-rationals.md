# The Hole in the Rationals

> Generated from the `math-real-analysis` capsule (Release 0.1) with the
> executable-tutorial method. The mathematics, the prerequisite order, and every
> calculation come from that capsule — `validation/instance-checks.bc` and
> `validation/proof-checks.lean` in particular.

An interactive walk from one stubborn sequence to the axiom that makes calculus
possible. You will meet the least-upper-bound axiom, the monotone convergence
theorem, the nested interval theorem, Bolzano–Weierstrass, and the Cauchy
criterion — and at each step you run a calculation that shows it working, then a
calculation that shows it **failing** the moment you move from `ℝ` to `ℚ`.

## How to run this

Install [`upmd`](https://upmd.dev), then from the repository root:

- `upmd skills/math-real-analysis/tutorial/hole-in-the-rationals.md` — the
  interactive walk (needs a real terminal).
- `upmd --ci --all skills/math-real-analysis/tutorial/hole-in-the-rationals.md`
  — run every calculation top to bottom (the verification gate).
- `upmd --ci -b capstone skills/math-real-analysis/tutorial/hole-in-the-rationals.md`
  — run the final verdict and everything it depends on.

Each block has `deps:` on the blocks for its prerequisites, in the same partial
order as the capsule's dependency graph, so you can run any single check and
`upmd` pulls its chain.

Two blocks call the Lean 4 kernel through a shell wrapper (`upmd` has no native
Lean runner). They need `lean` on your `PATH`; if it is missing they print a
`SKIP` line and still exit 0.

## What you need first

Rational arithmetic, the idea of a sequence `x : ℕ → ℝ`, and absolute value as
distance. Everything else is built below, in the order the capsule's graph
requires:

`supremum` → `lub_axiom` → `completeness_of_R` → `sequence_convergence` →
`monotone_convergence_theorem` → `nested_interval_theorem` →
`bolzano_weierstrass` → `cauchy_convergence_criterion`.

The recurring character is the **Babylonian sequence** `x_{n+1} = (x_n + 2/x_n)/2`
with `x_0 = 2`. It is the star of `validation/instance-checks.bc`.

---

## 0. Setup

The seed, a high-precision value of `√2` to compare against, and a tolerance.

```bash [name:setup]
export SEED=2
export SQRT2="$(echo 'scale=60; sqrt(2)' | bc -l)"
export EPS="$(echo 'scale=60; 1/10^12' | bc -l)"
echo "x_0 = $SEED"
echo "sqrt(2) ~ $(echo "$SQRT2" | cut -c1-42) ..."
echo "tolerance for 'converged' = 1e-12"
```

## 1. √2 is not a fraction

If `p/q` in lowest terms had `(p/q)² = 2` then `p² = 2q²`, so `p` is even, so
`4 | p² = 2q²`, so `q` is even — contradicting lowest terms. Below: a brute
check that no `p/q` with `q ≤ 300` squares to 2, and a look at the Babylonian
sequence, whose *square* marches straight to 2 even though no term is `√2`.

```bash [name:chk_sqrt2_irrational, deps:setup]
found=0
q=1
while [ "$q" -le 300 ]; do
  p=$(echo "scale=0; sqrt(2*$q*$q)/1" | bc -l)
  for pp in "$p" "$((p + 1))"; do
    r=$(echo "$pp*$pp - 2*$q*$q" | bc)
    [ "$r" = 0 ] && found=1
  done
  q=$((q + 1))
done
echo "fractions p/q with q<=300 and (p/q)^2 = 2 : $found   (want 0)"
[ "$found" = 0 ] || { echo "FAIL: found a rational square root of 2"; exit 1; }

x=$SEED
for i in 1 2 3 4 5; do x=$(echo "scale=40; ($x + 2/$x)/2" | bc -l); done
echo "x_5           = $x"
echo "x_5 squared   = $(echo "scale=40; $x*$x" | bc -l)   (-> 2, yet x_5 is a fraction)"
```

## 2. Suprema: the least upper bound of a set

For `A ⊆ ℝ` bounded above, `sup A` is the **least** of its upper bounds: `u` is
an upper bound and nothing smaller is. It need not lie in `A`. Consider
`A = { x : x² < 2 }`. Its upper bounds are the numbers with square `≥ 2`. Below
we hunt the largest terminating decimal in `A` at ever finer resolution — the
candidate for `sup A` keeps needing one more digit.

```bash [name:chk_supremum, deps:setup]
x=1
step=1
k=1
while [ "$k" -le 18 ]; do
  step=$(echo "scale=20; $step/10" | bc)
  while [ "$(echo "scale=20; ($x + $step)^2 <= 2" | bc)" = 1 ]; do
    x=$(echo "scale=20; $x + $step" | bc)
  done
  k=$((k + 1))
done
echo "largest 18-decimal rational whose square is <= 2 : $x"
echo "  its square         : $(echo "scale=20; $x*$x" | bc)      (< 2)"
echo "  next tick overshoots: $(echo "scale=20; ($x + 1/10^18)^2" | bc)   (> 2)"
echo "sup A sits pinched between these forever -- it is sqrt(2), not any decimal."
```

## 3. The least-upper-bound axiom — where ℝ and ℚ part ways

**`lub_axiom`**: every nonempty `A ⊆ ℝ` that is bounded above has a supremum
**in ℝ**. This is the completeness axiom of Release 0.1 (`completeness_of_R` is
"an ordered field with this property"); the construction of `ℝ` is cited, not
built. The same sentence is **false for ℚ**: below, rational lower bounds
(square `< 2`) and rational upper bounds (square `> 2`) of `A` close on each
other, but the number they trap has square exactly 2 — so `A` has no *least*
rational upper bound.

```bash [name:chk_lub_axiom, deps:chk_supremum]
lo=1; hi=2
i=1
while [ "$i" -le 80 ]; do
  mid=$(echo "scale=45; ($lo + $hi)/2" | bc)
  if [ "$(echo "scale=45; $mid*$mid < 2" | bc)" = 1 ]; then lo=$mid; else hi=$mid; fi
  i=$((i + 1))
done
echo "rational lower bounds of A climb to : $(echo "$lo" | cut -c1-40)"
echo "rational upper bounds of A fall to  : $(echo "$hi" | cut -c1-40)"
echo "gap hi - lo                         : $(echo "scale=45; $hi - $lo" | bc)"
echo
echo "In R  : the boundary is sup A = sqrt(2), a genuine element. Axiom holds."
echo "In Q  : the boundary is not a rational, so A has upper bounds but no LEAST"
echo "        one. The axiom fails. That absence is the hole."
```

## 4. Convergence of a sequence

`x_n → L` means: for every `ε > 0` there is an `N` with `|x_n − L| < ε` for all
`n ≥ N` (`sequence_convergence`, the `ε–N` idiom; quantifier order `∀ε ∃N`).
The limit is unique when it exists. Below: for the Babylonian sequence and
`ε = 10⁻¹²`, find the `N`. It is tiny — the sequence doubles its correct digits
each step.

```bash [name:chk_sequence_convergence, deps:setup]
x=$SEED
n=0
while [ "$(echo "scale=60; d = $x - $SQRT2; if (d < 0) d = -d; d >= $EPS" | bc -l)" = 1 ]; do
  x=$(echo "scale=60; ($x + 2/$x)/2" | bc -l)
  n=$((n + 1))
  [ "$n" -gt 100 ] && { echo "FAIL: no convergence by n=100"; exit 1; }
done
echo "first n with |x_n - sqrt(2)| < 1e-12 :  N = $n"
echo "x_$n = $(echo "$x" | cut -c1-40)"
```

## 5. Monotone and bounded

Two hypotheses, as first-class nodes. `bounded_sequence`: some `M` has
`|x_n| ≤ M` for all `n`. `monotone_sequence`: nondecreasing, or nonincreasing.
After its first step the Babylonian sequence is **decreasing** and **bounded
below by `√2`** (that lower bound is the AM–GM inequality, checked in §6).

```bash [name:chk_monotone_bounded, deps:setup]
x=$SEED
prev=$SEED
for n in 1 2 3 4 5; do
  x=$(echo "scale=60; ($x + 2/$x)/2" | bc -l)
  step=$(echo "scale=60; $x - $prev" | bc)
  above=$(echo "scale=60; $x*$x - 2" | bc)
  echo "x_$n  ~ $(echo "$x" | cut -c1-24)"
  echo "      step  = $(echo "$step" | cut -c1-16)   (< 0: decreasing)"
  echo "      x^2-2 = $(echo "$above" | cut -c1-16)   (> 0: above sqrt 2)"
  neg=$(echo "$step < 0" | bc); pos=$(echo "$above > 0" | bc)
  { [ "$neg" = 1 ] && [ "$pos" = 1 ]; } || { echo "FAIL: monotonicity/bound broken at n=$n"; exit 1; }
  prev=$x
done
echo "decreasing, and every term stays strictly above sqrt(2): bounded below."
```

## 6. The kernel checks the bound — AM–GM

Why is `(x + 2/x)/2 ≥ √2` for `x > 0`? Because `a² + b² ≥ 2ab` (equivalently
`(a − b)² ≥ 0`), with `a = x`, `b = 2/x`. `validation/proof-checks.lean` §8
pins this with a kernel-checked **instance** (`a = 5, b = 3`); the universal
statement needs `ring`/`nlinarith`, i.e. Mathlib, and is cited. Here we run that
exact check.

```bash [name:chk_amgm_lean, deps:chk_monotone_bounded]
command -v lean >/dev/null || { echo "SKIP: lean not on PATH"; exit 0; }
d=$(mktemp -d)
cat > "$d/amgm.lean" <<'LEAN'
-- math-real-analysis/validation/proof-checks.lean, section 8
-- AM-GM core  a^2 + b^2 >= 2ab  behind monotone_convergence_theorem's sqrt(2) example
-- INSTANCE a = 5, b = 3:  2*5*3 = 30  <=  25 + 9 = 34
example : (2 : Int) * 5 * 3 <= 5 ^ 2 + 3 ^ 2 := by decide
LEAN
if lean "$d/amgm.lean" 2>/dev/null; then
  echo "kernel accepted:  2*a*b <= a^2 + b^2   (instance a=5, b=3)"
  echo "this is the algebraic heart of 'x_n stays above sqrt(2)'."
else
  echo "FAIL: lean rejected the AM-GM instance"; rm -rf "$d"; exit 1
fi
rm -rf "$d"
```

## 7. The Monotone Convergence Theorem

**`monotone_convergence_theorem`**: a bounded monotone real sequence converges —
to `sup_n x_n` if nondecreasing, `inf_n x_n` if nonincreasing. The proof *is*
the least-upper-bound axiom: the limit is the supremum (or infimum) that
`lub_axiom` hands you. Epistemic status: `nonconstructive_result` — the `sup` is
not computed. Below: the Babylonian sequence converges (to `√2`, matching to 40
places by `x_6`); then the **counterexample** — the identical sequence read
inside `ℚ` satisfies every hypothesis and has no limit.

```bash [name:chk_mct, deps:"chk_monotone_bounded | chk_sequence_convergence | chk_lub_axiom"]
x=$SEED
for n in 1 2 3 4 5 6; do x=$(echo "scale=40; ($x + 2/$x)/2" | bc -l); done
echo "IN R:  x_6   = $x"
echo "       sqrt2 = $(echo 'scale=40; sqrt(2)' | bc -l)"
match=$(echo "scale=38; a = $x - sqrt(2); if (a < 0) a = -a; a < 1/10^37" | bc -l)
[ "$match" = 1 ] || { echo "FAIL: x_6 does not match sqrt(2) to 37 places"; exit 1; }
echo "       bounded + monotone  =>  converges.  (limit = sup/inf, from lub_axiom)"
echo
echo "IN Q:  the SAME sequence -- every x_n is a fraction, it is decreasing, it is"
echo "       bounded below -- but sqrt(2) is not rational, so within Q it has NO"
echo "       limit. Drop completeness and the theorem is false."
```

## 8. The Nested Interval Theorem

**`nested_interval_theorem`**: a decreasing chain of nonempty closed bounded
intervals `I_1 ⊇ I_2 ⊇ ⋯` has `⋂ I_k ≠ ∅` (a single point when the widths → 0).
Again `lub_axiom` under the hood: the common point is the supremum of the left
endpoints. Below: bisect `[1,2]` toward `√2`, watch the interval collapse; then
the **counterexample** — take the same intervals with *rational* endpoints and
in `ℚ` the intersection is empty.

```bash [name:chk_nested_intervals, deps:chk_lub_axiom]
lo=1; hi=2
k=1
while [ "$k" -le 40 ]; do
  mid=$(echo "scale=45; ($lo + $hi)/2" | bc)
  if [ "$(echo "scale=45; $mid*$mid < 2" | bc)" = 1 ]; then lo=$mid; else hi=$mid; fi
  case $k in
    1|3|6|12|24|40)
      w=$(echo "scale=45; $hi - $lo" | bc)
      echo "I_$k = [ $(echo "$lo" | cut -c1-20) , $(echo "$hi" | cut -c1-20) ]   width $(echo "$w" | cut -c1-10)" ;;
  esac
  k=$((k + 1))
done
echo
echo "IN R:  intersection = { sqrt(2) }."
echo "IN Q:  identical intervals, rational endpoints, nonempty and closed and"
echo "       shrinking -- yet no rational lies in every one.  Intersection empty."
```

## 9. Bolzano–Weierstrass

**`bolzano_weierstrass`**: every bounded real sequence has a convergent
subsequence. The proof is bisection — halve a bounding interval, keep a half
that still holds infinitely many terms, repeat; the nested intervals pin the
subsequential limit. Below we run that on `x_n = sin n` (bounded in `[−1,1]`,
never convergent). We *pick a target* `0.5` and keep the half containing it —
both halves always hold infinitely many `sin n` (equidistribution), so this is a
legal choice, and it shows you can steer a subsequence to any point. Then the
**counterexample**: `x_n = n`, unbounded, has no convergent subsequence at all.

```bash [name:chk_bolzano_weierstrass, deps:"chk_nested_intervals | chk_sequence_convergence"]
awk 'BEGIN {
  lo = -1; hi = 1; N = 1000000; target = 0.5
  for (k = 1; k <= 16; k++) {
    mid = (lo + hi) / 2
    if (target < mid) hi = mid; else lo = mid
    c = 0
    for (n = 1; n <= N; n++) { s = sin(n); if (s >= lo && s <= hi) c++ }
    if (k == 1 || k == 4 || k == 8 || k == 12 || k == 16)
      printf "  k=%2d: window [% .5f, % .5f]  holds %d of the first %d terms\n", k, lo, hi, c, N
  }
  print  "  (every finer window still holds infinitely many terms -- our finite"
  print  "   sample just stops resolving them)"
  printf "=> a subsequence of sin(n) converges to %.2f; aim elsewhere, reach any point of [-1,1]\n", target
}'
echo
echo "drop boundedness:  x_n = n."
awk 'BEGIN { for (n = 1; n <= 6; n++) printf "x_%d=%d  ", n, n; print "...   consecutive gaps are 1" }'
echo "  => every |x_m - x_n| >= 1, no subsequence is Cauchy, none converges."
```

## 10. The kernel checks the triangle inequality

The Cauchy criterion's easy direction (`converges ⇒ Cauchy`) is
`|x_m − x_n| ≤ |x_m − L| + |L − x_n|`. That is the triangle inequality, and
`validation/proof-checks.lean` §1 proves it **universally over ℤ** with `omega`
— a genuine proof, not an instance. We run it.

```bash [name:chk_triangle_lean, deps:setup]
command -v lean >/dev/null || { echo "SKIP: lean not on PATH"; exit 0; }
d=$(mktemp -d)
cat > "$d/tri.lean" <<'LEAN'
-- math-real-analysis/validation/proof-checks.lean, section 1
-- triangle inequality, UNIVERSAL over the integers
theorem tri (a b : Int) : (a + b).natAbs <= a.natAbs + b.natAbs := by omega
theorem tri3 (a b c : Int) : (a - c).natAbs <= (a - b).natAbs + (b - c).natAbs := by omega
LEAN
if lean "$d/tri.lean" 2>/dev/null; then
  echo "kernel accepted (for ALL integers a, b, c):"
  echo "  |a - c|  <=  |a - b| + |b - c|"
  echo "this is the whole of 'convergent => Cauchy'."
else
  echo "FAIL: lean rejected the triangle inequality"; rm -rf "$d"; exit 1
fi
rm -rf "$d"
```

## 11. The Cauchy Convergence Criterion

**`cauchy_convergence_criterion`**: a real sequence converges **iff** it is
Cauchy — `∀ε>0 ∃N ∀m,n≥N : |x_m − x_n| < ε`. The point of "Cauchy" is that it
never mentions the limit, so you can certify convergence without knowing the
value. The `⇐` direction leans on Bolzano–Weierstrass. Below: the Babylonian
sequence is visibly Cauchy; then the **counterexample that names the hole** —
the decimal truncations of `√2` are Cauchy in `ℚ` with no rational limit.

```bash [name:chk_cauchy, deps:"chk_sequence_convergence | chk_bolzano_weierstrass | chk_triangle_lean"]
x=$SEED
x3=""; x5=""; x7=""
for n in 0 1 2 3 4 5 6 7; do
  case $n in 3) x3=$x;; 5) x5=$x;; 7) x7=$x;; esac
  x=$(echo "scale=60; ($x + 2/$x)/2" | bc -l)
done
echo "IN R (Babylonian sequence):"
echo "  |x_7 - x_5| = $(echo "scale=60; a = $x7 - $x5; if (a<0) a=-a; a" | bc | cut -c1-34)"
echo "  |x_7 - x_3| = $(echo "scale=60; a = $x7 - $x3; if (a<0) a=-a; a" | bc | cut -c1-34)"
echo "  late terms are mutually within 1e-30 -> Cauchy -> (criterion) it converges."
echo
echo "IN Q (the hole, from validation/instance-checks.bc):"
for k in 1 3 5 10 20; do
  echo "  a_$k = $(echo "scale=$k; sqrt(2)" | bc -l)      (terminates -> rational)"
done
echo "  (a_k) is Cauchy: |a_j - a_k| <= 10^{-min(j,k)}."
echo "  Its only candidate limit is sqrt(2), which is NOT rational."
echo "  => a Cauchy sequence of rationals with no limit in Q.  Q is incomplete."
```

## 12. Capstone — the verdict

One sequence, two universes.

```bash [name:capstone, deps:"chk_mct | chk_nested_intervals | chk_cauchy"]
echo "================================================================"
echo "   x_{n+1} = ( x_n + 2/x_n ) / 2 ,      x_0 = 2"
echo "================================================================"
echo
echo "  Established in the sections above:"
echo "    * decreasing after step 1           [chk_monotone_bounded]"
echo "    * bounded below by sqrt(2)          [chk_amgm_lean]"
echo "    * Cauchy                            [chk_cauchy, chk_triangle_lean]"
echo "    * every term is a rational number   [chk_sqrt2_irrational]"
echo
r=$(echo "scale=45; x = 2; for (i = 0; i < 50; i++) x = (x + 2/x)/2; x" | bc -l)
s=$(echo "scale=45; sqrt(2)" | bc -l)
echo "  IN R:  bounded + monotone --(MCT)--> converges;  Cauchy --(criterion)--> converges."
echo "         limit  = $(echo "$r" | cut -c1-40)"
echo "         sqrt2  = $(echo "$s" | cut -c1-40)"
[ "$(echo "$r" | cut -c1-40)" = "$(echo "$s" | cut -c1-40)" ] || { echo "FAIL: limit != sqrt(2)"; exit 1; }
echo
echo "  IN Q:  EVERY hypothesis above still holds -- the sequence is rational,"
echo "         decreasing, bounded, Cauchy -- and yet it has NO limit, because the"
echo "         number it closes in on is not a fraction."
echo
echo "  That missing number is the hole.  lub_axiom is precisely the assertion"
echo "  that R has none.  Monotone convergence, nested intervals, Bolzano-"
echo "  Weierstrass and the Cauchy criterion are all it, wearing different hats."
echo
echo "  VERDICT: completeness is not a technicality. It is the one axiom that"
echo "           separates calculus from arithmetic."
```
