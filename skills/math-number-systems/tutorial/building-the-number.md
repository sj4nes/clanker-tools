# Building the number that isn't there

> Generated from the `math-number-systems` capsule (Release 0.1) with the
> `theorem-tree-tutorial` skill. The mathematics, the prerequisite order, and
> every calculation and proof come from that capsule —
> `validation/proof-checks.lean` and `validation/instance-checks.bc` in
> particular.

`√2` is a number you can name — the diagonal of a unit square — but there is no
fraction equal to it. This tutorial follows that gap from both sides. First it
builds `ℤ` and then `ℚ` as **quotients**, and at each step runs the check that an
operation on classes *is actually a function* (and a counterexample where it is
not). Then it makes the gap precise: `{x ∈ ℚ : x² < 2}` is bounded but has no
least upper bound in `ℚ`. Then it builds `ℝ` from **Dedekind cuts** — a real
*is* the set of rationals below it — and shows the same set now has a supremum,
**exhibited** as a union, not postulated. By the end `√2` exists, and every step
was choice-free and constructive.

## How to run this

Install [`upmd`](https://upmd.dev), then from the repository root:

- `upmd skills/math-number-systems/tutorial/building-the-number.md` — the walk.
- `upmd --ci --all skills/math-number-systems/tutorial/building-the-number.md` —
  run every check (the gate).
- `upmd --ci -b capstone skills/math-number-systems/tutorial/building-the-number.md`
  — the verdict and its chain.

Blocks `deps:` earlier ones in the capsule's partial order. The `lean_…` blocks
call the Lean 4 kernel through a shell wrapper (`upmd` has no Lean runner); if
`lean` is missing they print `SKIP` and still exit 0.

## What you need first

`ℕ` with `0`, successor, `+`, `·`, `<`, and `gcd` — the Peano layer, which this
capsule builds but which we take as given here. Equivalence relations and the
idea of a **quotient set** (classes of an equivalence relation). Nothing about
`ℝ` — that is the point of the tutorial.

Every result below has `uses_choice: false`, and `lub_property` in particular is
`constructive` — the sharpest contrast with `math-real-analysis`, where the
identical statement is the completeness **axiom** `lub_axiom`.

---

## 0. Setup

The recurring object is the **Babylonian sequence** `x_{n+1} = (x_n + 2/x_n)/2`,
`x_0 = 2` — every term a fraction, its square marching to 2.

```bash [name:setup]
export SEED=2
export SQRT2="$(echo 'scale=40; sqrt(2)' | bc -l)"
echo "seed x_0 = $SEED ;  sqrt(2) ~ $(echo "$SQRT2" | cut -c1-30) ..."
```

## 1. ℤ — the integers as a quotient

**`integer`**: `ℤ = (ℕ×ℕ)/∼`, where `(a,b) ∼ (c,d)` iff `a+d = b+c`. The class
`[(a,b)]` stands for "`a − b`" — written with `+` only, because subtraction does
not exist yet. Before the quotient can be formed, `∼` must be an **equivalence
relation**: reflexivity and symmetry are immediate, and transitivity uses
additive cancellation in `ℕ`. Then every operation — addition, negation, order —
is *defined on representatives* and separately shown to **respect `∼`**. The
check below does that for addition; the counterexample shows an operation that
does not. *(Landau; Tao, Analysis I.)*

```bash [name:chk_integer, deps:setup]
# a class [(a,b)] has "value" a - b.  Correct addition: (a,b)+(c,d) = (a+c, b+d).
val () { echo $(( $1 - $2 )); }
# [(5,2)] and [(8,5)] are the same class:
echo "[(5,2)] ~ [(8,5)] ?   5+5 = $(( 5 + 5 )) ,  2+8 = $(( 2 + 8 ))   -> equal (both name +3)"
# add [(1,4)] (value -3) to each representative, check the results agree:
r1=$(val $(( 5 + 1 )) $(( 2 + 4 )))          # [(5,2)] + [(1,4)] = [(6,6)]
r2=$(val $(( 8 + 1 )) $(( 5 + 4 )))          # [(8,5)] + [(1,4)] = [(9,9)]
echo "[(5,2)]+[(1,4)] = $r1     [(8,5)]+[(1,4)] = $r2     (want equal: + is well-defined)"
[ "$r1" = "$r2" ] || { echo "FAIL: addition disagreed across representatives"; exit 1; }
```

```bash [name:lean_integer, deps:setup]
command -v lean >/dev/null || { echo "SKIP: lean not on PATH"; exit 0; }
d=$(mktemp -d)
cat > "$d/z.lean" <<'LEAN'
-- math-number-systems/validation/proof-checks.lean, sections 1-2
-- GENUINE, universal over the integers (omega).
-- (a,b) ~ (c,d)  :<->  a + d = b + c.
theorem z_rel_trans (a b c d e f : Int)
    (h1 : a + d = b + c) (h2 : c + f = d + e) : a + f = b + e := by omega
-- addition respects the relation:
theorem z_add_well_defined (a b a' b' c d c' d' : Int)
    (h1 : a + b' = b + a') (h2 : c + d' = d + c') :
    (a + c) + (b' + d') = (b + d) + (a' + c') := by omega
LEAN
if lean "$d/z.lean" 2>/dev/null; then
  echo "kernel accepted, for ALL integers:"
  echo "  ~ is transitive   (so N x N really is partitioned into classes)"
  echo "  addition respects ~   (so [(a,b)]+[(c,d)] does not depend on the reps)"
else
  echo "FAIL: lean rejected the Z cores"; rm -rf "$d"; exit 1
fi
rm -rf "$d"
```

```bash [name:cx_integer, deps:chk_integer]
# a BADLY-defined "operation": [(a,b)] (+) [(c,d)] := [(a*c, b*d)]  (componentwise product)
badval () { echo $(( $1 * $3 - $2 * $4 )); }   # value of [(a*c, b*d)]
# same class [(5,2)] = [(8,5)], same second operand [(1,4)]:
b1=$(badval 5 2 1 4)                            # [(5*1, 2*4)] = [(5,8)]  -> -3
b2=$(badval 8 5 1 4)                            # [(8*1, 5*4)] = [(8,20)] -> -12
echo "[(5,2)] (+) [(1,4)] = $b1      [(8,5)] (+) [(1,4)] = $b2"
echo "$b1 != $b2  =>  this '(+)' gives different answers for the SAME class."
echo "It is not a function on Z. Well-definedness is a real obligation, not a"
echo "formality -- and transitivity of ~ is what makes 'the set of classes'"
echo "meaningful in the first place."
[ "$b1" != "$b2" ] || { echo "FAIL: expected the bad op to disagree"; exit 1; }
```

## 2. ℚ — the rationals as a quotient of ℤ

**`rational_number`**: `ℚ = (ℤ×ℤ*)/∼`, where `ℤ* = ℤ∖{0}` and `(a,b) ∼ (c,d)` iff
`ad = bc`. The class `[(a,b)]` is "`a/b`". Transitivity of `∼` needs `ℤ` to be an
**integral domain**: from `ad = bc` and `cf = de` you get `d(af) = d(be)`, and
you cancel `d ≠ 0` — which is legal exactly because `ℤ` has **no zero divisors**.
The second coordinate must be nonzero; drop that and `[(a,0)] ∼ [(c,0)]` for all
`a, c` and the whole structure collapses (§2 counterexample). *(Landau; Tao.)*

```bash [name:chk_rational_number, deps:chk_integer]
# class [(a,b)] has value a/b.  [(2,4)] and [(1,2)] are the same:
echo "[(2,4)] ~ [(1,2)] ?   2*2 = $(( 2 * 2 )) ,  4*1 = $(( 4 * 1 ))   -> equal"
# rational addition: (a,b)+(c,d) = (ad+bc, bd).  Add [(1,3)] to each representative:
n1=$(( 2*3 + 4*1 )); d1=$(( 4*3 ))              # [(2,4)] + [(1,3)] = [(10,12)]
n2=$(( 1*3 + 2*1 )); d2=$(( 2*3 ))              # [(1,2)] + [(1,3)] = [(5,6)]
echo "[(2,4)]+[(1,3)] = [($n1,$d1)]   [(1,2)]+[(1,3)] = [($n2,$d2)]"
# equal as rationals iff n1*d2 = n2*d1:
[ "$(( n1 * d2 ))" = "$(( n2 * d1 ))" ] || { echo "FAIL: + disagreed across reps"; exit 1; }
echo "  $n1 * $d2 = $(( n1 * d2 ))  =  $n2 * $d1 = $(( n2 * d1 ))   (+ is well-defined on Q)"
```

```bash [name:lean_rational_number, deps:setup]
command -v lean >/dev/null || { echo "SKIP: lean not on PATH"; exit 0; }
d=$(mktemp -d)
cat > "$d/q.lean" <<'LEAN'
-- math-number-systems/validation/proof-checks.lean, section 8  (INSTANCE, `decide`)
-- ~_Q transitivity on the chain (1,2) ~ (2,4) ~ (3,6):  ad = bc form.
example : (1 * 4 = 2 * 2) ∧ (2 * 6 = 4 * 3) ∧ (1 * 6 = 2 * 3) := by decide
LEAN
if lean "$d/q.lean" 2>/dev/null; then
  echo "kernel checked (INSTANCE): (1,2) ~ (2,4) and (2,4) ~ (3,6), and indeed (1,2) ~ (3,6)."
  echo "The universal statement -- transitivity for all (a,b),(c,d),(e,f) -- needs the"
  echo "'cancel d != 0 because Z is a domain' step, and is cited (proof-checks.md)."
else
  echo "FAIL: lean rejected the Q instance"; rm -rf "$d"; exit 1
fi
rm -rf "$d"
```

```bash [name:cx_rational_number, deps:chk_rational_number]
# drop "second coordinate nonzero": allow [(a,0)].
# ~_Q says (a,0) ~ (c,0) iff a*0 = 0*c, i.e. 0 = 0 -- ALWAYS true.
echo "with b = 0 allowed:  (1,0) ~ (7,0) ?   1*0 = $(( 1 * 0 )) ,  0*7 = $(( 0 * 7 ))   -> 'equal'"
echo "  so [(1,0)] = [(2,0)] = [(7,0)] = ... : every 'a/0' is one single class."
echo "  and (1,0) ~ (0,0) too, so that class also equals [(0,0)] = 0/0."
echo "  addition/multiplication with it are inconsistent -- division by zero, and"
echo "  the field axioms fail. The ZERO-divisor version fails even earlier:"
# in Z/6:  2*3 = 0.  Take (a,b)=(2,1), (c,d)=(3,2): ad=4, bc=6=0 mod 6 -> NOT related the same way
echo "  in Z/6:  2*3 = $(( (2*3) % 6 ))  (a zero divisor) => the cancellation step in the"
echo "  transitivity proof is invalid, and Frac(Z/6) is not a field."
```

## 3. √2 is irrational — the number ℚ cannot hold

**`sqrt2_irrational`**: no rational `x` has `x² = 2`. Suppose `x = p/q` in lowest
terms (`gcd(p,q) = 1`) with `p² = 2q²`. Then `2 ∣ p²`, so `2 ∣ p` (division with
remainder mod 2), say `p = 2k`; then `4k² = 2q²`, so `q² = 2k²`, so `2 ∣ q` — but
then `2 ∣ gcd(p,q) = 1`, a contradiction. Epistemic status: `proved_theorem`,
and **`constructive`** — from any putative `p/q` the argument *produces* the
contradiction. It applies to `√n` for every non-square `n`; `√4 = 2` is rational
precisely because 4 is a square (§3 counterexample). *(Landau; Hardy–Wright.)*

```bash [name:chk_sqrt2_irrational, deps:chk_rational_number]
# brute: no p/q with q <= 2000 has p^2 = 2 q^2   (validation/instance-checks.bc)
found=0; q=1
while [ "$q" -le 2000 ]; do
  p=$(echo "scale=0; sqrt(2*$q*$q)/1" | bc -l)
  for pp in "$p" "$((p + 1))"; do
    [ "$(echo "$pp*$pp - 2*$q*$q" | bc)" = 0 ] && found=1
  done
  q=$((q + 1))
done
echo "fractions p/q, q <= 2000, with (p/q)^2 = 2 :  $found   (want 0)"
[ "$found" = 0 ] || { echo "FAIL: found a rational square root of 2"; exit 1; }
# yet the Babylonian sequence's SQUARE marches to 2:
x=$SEED
for i in 1 2 3 4 5; do x=$(echo "scale=40; ($x + 2/$x)/2" | bc -l); done
echo "x_5           = $(echo "$x" | cut -c1-30)   (a fraction)"
echo "x_5 squared   = $(echo "scale=40; $x*$x" | bc -l | cut -c1-30)   (-> 2)"
```

```bash [name:lean_sqrt2_irrational, deps:setup]
command -v lean >/dev/null || { echo "SKIP: lean not on PATH"; exit 0; }
d=$(mktemp -d)
cat > "$d/s2.lean" <<'LEAN'
-- math-number-systems/validation/proof-checks.lean, section 9  (INSTANCE, `decide`)
-- no p, q with 1 <= q < 50 and p^2 = 2 q^2.
-- The universal statement is the parity / infinite-descent argument, cited.
example : ∀ p q : Fin 50, q.val ≥ 1 → p.val * p.val ≠ 2 * (q.val * q.val) := by decide
LEAN
if lean "$d/s2.lean" 2>/dev/null; then
  echo "kernel checked (INSTANCE): no p^2 = 2 q^2 for q in 1..49."
  echo "the parity argument (2|p^2 => 2|p => 2|q => 2|gcd(p,q)=1, contradiction) is"
  echo "the universal proof, and is cited -- decide over Fin 50 is not it."
else
  echo "FAIL: lean rejected the sqrt2 instance"; rm -rf "$d"; exit 1
fi
rm -rf "$d"
```

```bash [name:cx_sqrt2_irrational, deps:chk_sqrt2_irrational]
# drop "n is not a perfect square": sqrt(4) = 2 IS rational.
# p^2 = 4 q^2 has the whole family p = 2q:
for q in 1 2 3 7; do
  p=$(( 2 * q ))
  echo "  q = $q :  p = 2q = $p ,  p^2 = $(( p*p )) ,  4 q^2 = $(( 4*q*q ))   -> equal, and p/q = 2"
done
echo "The theorem is specifically about NON-squares. For a square, the descent"
echo "terminates at the exact root instead of contradicting."
```

### In the wild

The step "`2 ∣ p²` ⇒ `2 ∣ p`" is a statement about the **2-adic valuation**
`v₂(n)` — the exponent of 2 in `n`. Written that way the proof is one line:
`p² = 2q²` gives `2·v₂(p) = 1 + 2·v₂(q)`, an even number equal to an odd one.
The same tool, one prime at a time, decides *every* such question:
**`√n` is rational ⟺ `vₚ(n)` is even for every prime `p`** (i.e. `n` is a
perfect square); `log₂ 3` is irrational because `2^a = 3^b` forces
`v₂` and `v₃` to disagree. The `p`-adic valuation and its completion `ℚ_p` are
built from exactly this observation and run through all of number theory —
Hensel's lemma, the local–global principle, elliptic-curve arithmetic. The
block below runs the criterion at `p = 2, 3` and checks it against brute
square-testing.

```bash [name:app_sqrt2_irrational, deps:chk_sqrt2_irrational]
# vp(n): exponent of prime p in n
vp() { n=$1; p=$2; c=0; while [ $(( n % p )) -eq 0 ]; do n=$(( n / p )); c=$(( c + 1 )); done; echo "$c"; }
echo "  n   v2  v3   all-valuations-even?   perfect square?   sqrt(n) rational?"
mismatch=0
for n in 2 3 4 8 9 12 16 18 25 36; do
  v2=$(vp "$n" 2); v3=$(vp "$n" 3)
  # strip the 2- and 3-parts; whatever remains must itself be a perfect square
  rest=$n
  i=0; while [ $i -lt "$v2" ]; do rest=$(( rest / 2 )); i=$(( i + 1 )); done
  i=0; while [ $i -lt "$v3" ]; do rest=$(( rest / 3 )); i=$(( i + 1 )); done
  rs=$(echo "scale=0; sqrt($rest)/1" | bc -l)
  even_all=$([ $(( v2 % 2 )) -eq 0 ] && [ $(( v3 % 2 )) -eq 0 ] && [ $(( rs*rs )) -eq "$rest" ] && echo yes || echo no)
  r=$(echo "scale=0; sqrt($n)/1" | bc -l)
  is_sq=$([ $(( r*r )) -eq "$n" ] && echo yes || echo no)
  printf "  %-3s %-3s %-3s  %-20s  %-15s   %s\n" "$n" "$v2" "$v3" "$even_all" "$is_sq" "$even_all"
  [ "$even_all" = "$is_sq" ] || mismatch=1
done
echo
echo "valuation-parity criterion agrees with brute square-testing on every n: \
$([ $mismatch -eq 0 ] && echo yes || echo NO)   (want yes)"
[ "$mismatch" -eq 0 ] || { echo "FAIL: criterion disagreed"; exit 1; }
echo "n = 2:  v2 = 1 (odd)      -> sqrt(2) irrational   <- this is sqrt2_irrational"
echo "n = 4:  v2 = 2 (even)     -> sqrt(4) = 2 rational  <- the section-3 counterexample"
echo "n = 12: v2 = 2, v3 = 1    -> sqrt(12) irrational   (the 3-part is the obstruction)"
```

## 4. The crisis, made precise — ℚ has a bounded set with no supremum

**`rational_incomplete_lub`**: `A = {x ∈ ℚ : x² < 2}` is nonempty (`1 ∈ A`) and
bounded above (by `2`), yet has **no least upper bound in `ℚ`**. For any rational
upper bound `p`: if `p² < 2`, the rational `p + (2−p²)/(2p+2)` is larger and
still in `A`, so `p` is not an upper bound; if `p² > 2`, a slightly smaller
rational is still an upper bound, so `p` is not the least; and `p² = 2` is
impossible. So no rational is the least upper bound — the boundary sits at `√2`,
which is not there. *(Rudin; Abbott.)*

```bash [name:chk_rational_incomplete_lub, deps:chk_sqrt2_irrational]
# hunt the largest terminating decimal in A at ever finer resolution
x=1; step=1; k=1
while [ "$k" -le 22 ]; do
  step=$(echo "scale=25; $step/10" | bc)
  while [ "$(echo "scale=25; ($x + $step)^2 <= 2" | bc)" = 1 ]; do
    x=$(echo "scale=25; $x + $step" | bc)
  done
  k=$((k + 1))
done
echo "largest 22-decimal rational whose square is <= 2 :"
echo "  $x"
echo "  its square            : $(echo "scale=25; $x*$x" | bc)   (< 2)"
echo "  next tick overshoots  : $(echo "scale=25; ($x + 1/10^22)^2" | bc)   (> 2)"
echo "The candidate for sup A needs one more digit forever. In Q there is no"
echo "rational it converges to -- that is the incompleteness."
```

```bash [name:cx_rational_incomplete_lub, deps:chk_rational_incomplete_lub]
# move the ambient field to R: the SAME set A acquires a supremum, sqrt(2).
lo=1; hi=2
for i in $(seq 1 80); do
  mid=$(echo "scale=45; ($lo + $hi)/2" | bc)
  if [ "$(echo "scale=45; $mid*$mid < 2" | bc)" = 1 ]; then lo=$mid; else hi=$mid; fi
done
echo "rational lower bounds of A climb to : $(echo "$lo" | cut -c1-34)"
echo "rational upper bounds of A fall to  : $(echo "$hi" | cut -c1-34)"
echo "gap                                 : $(echo "scale=45; $hi - $lo" | bc)"
echo "IN R the boundary IS an element -- sup A = sqrt(2). Completeness is exactly"
echo "the thing Q is missing, and R is what we build to supply it."
```

### In the wild

This is the concrete failure that every *completeness axiom* exists to rule out:
"bounded + monotone ⇒ convergent", the nested-interval theorem, Bolzano–
Weierstrass, and the Cauchy criterion are equivalent ways of saying this gap is
filled. Numerical analysis lives on the consequence — a bisection or Newton
iteration produces a Cauchy sequence of rationals (or floats), and only
completeness guarantees the limit it is closing on **exists**.

```bash [name:app_rational_incomplete_lub, deps:chk_rational_incomplete_lub]
# a bisection on [1,2] for sqrt(2): each step halves the interval, so after n
# steps the width is 2^-n.  How many steps for k correct decimal digits?
for k in 6 12 20 40; do
  # need 2^-n <= 10^-k   =>   n >= k / log10(2)   (log10 2 = ln2/ln10)
  n=$(echo "scale=8; x = $k / (l(2)/l(10)); scale=0; x/1 + 1" | bc -l)
  echo "  $k digits of sqrt(2)  ->  $n bisection steps"
done
echo "  each step appends one rational to a Cauchy sequence; completeness is the"
echo "  promise that the sequence has somewhere to converge to."
```

## 5. The fix — a real number is a Dedekind cut

**`dedekind_cut`**: a cut is a set `A ⊆ ℚ` that is nonempty, not all of `ℚ`,
**downward closed** (`p ∈ A ∧ q < p ⇒ q ∈ A`), and has **no greatest element**.
A real number *is* such a set — the set of every rational below it. `q* = {p ∈ ℚ
: p < q}` is the cut for a rational `q`; `{p ∈ ℚ : p ≤ 0 ∨ p² < 2}` is a cut with
no rational "cut point" — its value is `√2`. The "no greatest element" clause is
what makes `q ↦ q*` injective; drop it and `{p ≤ q}` and `{p < q}` become two
different cuts for the same `q` (§5 counterexample). *(Dedekind 1872; Rudin.)*

```bash [name:chk_dedekind_cut, deps:chk_rational_incomplete_lub]
# check the four clauses for  A = { p in Q : p <= 0 or p^2 < 2 }  (the sqrt(2) cut)
inA () { echo "scale=20; ($1 <= 0) || ($1 * $1 < 2)" | bc -l; }
echo "A = { p : p <= 0 or p^2 < 2 }"
echo "  nonempty        : 0 in A ?  $(inA 0)          (1 = yes)"
echo "  proper (!= Q)   : 2 in A ?  $(inA 2)          (0 = no, so A != Q)"
echo "  downward closed : 1.4 in A ($(inA 1.4)) and 0.5 < 1.4 => 0.5 in A ($(inA 0.5))"
echo "  no greatest     : 1.41 in A ($(inA 1.41)), and 1.414 in A ($(inA 1.414)) is bigger,"
echo "                    and 1.4142 ($(inA 1.4142)) bigger still -- you can always inch up"
[ "$(inA 0)" = 1 ] && [ "$(inA 2)" = 0 ] && [ "$(inA 0.5)" = 1 ] || { echo "FAIL: not a cut"; exit 1; }
```

```bash [name:cx_dedekind_cut, deps:chk_dedekind_cut]
# drop "no greatest element": now { p : p <= 2 } and { p : p < 2 } are BOTH cuts.
le2 () { echo "scale=6; $1 <= 2" | bc -l; }
lt2 () { echo "scale=6; $1 < 2"  | bc -l; }
echo "closed  { p : p <= 2 } :  2 in it ? $(le2 2)     downward closed, proper"
echo "open    { p : p <  2 } :  2 in it ? $(lt2 2)     downward closed, proper"
echo "they differ only at p = 2.  Without the 'no greatest' clause BOTH count as"
echo "cuts, so the rational 2 has TWO reals -- the embedding q |-> q* is not"
echo "injective, and Q no longer sits inside R properly."
```

## 6. ℝ is an ordered field — arithmetic on sets of rationals

**`real_is_ordered_field`**: `(ℝ, +, ·, 0*, 1*, ≤)` satisfies the ordered-field
axioms, each checked at the level of sets of rationals. `A + B = {a + b : a ∈ A,
b ∈ B}` is again a cut; order is inclusion. **Multiplication needs sign cases** —
defining `A · B = {ab}` for all cuts fails: once `A` contains arbitrarily
negative rationals, `{ab}` is unbounded above and is not a cut (§6
counterexample). `lean_status: cited` — the set-level field-axiom
verifications are not formalised in the Mathlib-free capsule. *(Rudin; Landau.)*

```bash [name:chk_real_is_ordered_field, deps:chk_dedekind_cut]
# represent a cut by its sup value.  Addition of cuts adds the values.
# 0* = { p : p < 0 } (value 0) ,  1* = { p : p < 1 } (value 1)
echo "0* + 1* :  A + B = { a + b : a < 0, b < 1 } = { r : r < 1 } = 1*"
echo "  value check: 0 + 1 = $(echo "0 + 1" | bc)   (want 1)"
# sign-case multiplication: (-1*) * (-1*) should be 1*, not (-1)*  via {ab}
echo "(-1*) * (-1*) :  sign case '(neg)(neg) = pos' gives value (-1)*(-1) = $(echo "(-1)*(-1)" | bc)   (want 1)"
[ "$(echo "0 + 1" | bc)" = 1 ] && [ "$(echo "(-1)*(-1)" | bc)" = 1 ] || { echo FAIL; exit 1; }
```

```bash [name:cx_real_is_ordered_field, deps:chk_real_is_ordered_field]
# naive multiplication A*B = { a*b : a in A, b in B } for ALL cuts.
# take A = 0* = { p : p < 0 } (all negative rationals) and B = 1* = { p : p < 1 }.
# a can be as negative as we like; fix b = 1/2 in B.  Then a*b -> +infinity.
echo "A*B with A = 0*, B = 1*, taking a -> -infinity and b = 1/2:"
for a in -10 -100 -1000000; do
  echo "  a = $a , b = 0.5  ->  a*b = $(echo "$a * 0.5" | bc)"
done
echo "{ a*b } is unbounded ABOVE -- it is all of Q, which is NOT a cut."
echo "=> multiplication of cuts must be defined by cases on the signs."
```

## 7. The payoff — every bounded set of reals has a supremum

**`lub_property`**: every nonempty `S ⊆ ℝ` bounded above has a supremum, and it
is `sup S = ⋃_{A ∈ S} A` — the union of the cuts. The content is that this union
*is a cut*: nonempty (`S` is), proper (`S` bounded above by some cut `B`, so the
union sits inside `B ≠ ℚ`), downward closed (a union of downward-closed sets),
no greatest element. It contains every `A ∈ S` (upper bound) and sits inside
every upper bound (least). **`constructive`, choice-free** — the supremum is
*exhibited* as a specific set of rationals. In `math-real-analysis` this exact
statement is the axiom `lub_axiom`. *(Dedekind 1872; Rudin.)*

```bash [name:chk_lub_property, deps:"chk_dedekind_cut | chk_real_is_ordered_field"]
# S = { q* : q in Q, q^2 < 2 }.  sup S = union of all those q* = { p : p < some q with q^2 < 2 }
#                                       = { p : p <= 0 or p^2 < 2 }  = the sqrt(2) cut.
inUnion () {   # is rational r in the union?  r < q for some rational q with q^2 < 2
  echo "scale=20; ($1 <= 0) || ($1 * $1 < 2)" | bc -l
}
echo "sup S  =  union of { q* : q^2 < 2 }:"
echo "  1.41  in sup S ?  $(inUnion 1.41)   (1: 1.41^2 = $(echo "scale=4;1.41*1.41" | bc) < 2)"
echo "  1.42  in sup S ?  $(inUnion 1.42)   (0: 1.42^2 = $(echo "scale=4;1.42*1.42" | bc) > 2)"
echo "  the boundary is exactly sqrt(2) -- and this set EXISTS, as a union. No"
echo "  axiom, no choice: sup S is written down."
[ "$(inUnion 1.41)" = 1 ] && [ "$(inUnion 1.42)" = 0 ] || { echo FAIL; exit 1; }
```

```bash [name:cx_lub_property, deps:chk_lub_property]
# drop "S bounded above": S = { q* : q in Q } (all rational cuts).
echo "S = { q* : q in Q }, no upper bound:"
echo "  the union of ALL q* is { p : p < q for some rational q } = all of Q."
echo "  all of Q is NOT a cut (the 'proper subset' clause fails)."
echo "  => no supremum. Boundedness is not decoration; it is what keeps the"
echo "  union inside some cut B, hence a cut itself."
# and the same statement for Q instead of R is simply false -- section 4.
echo
echo "  (and: this whole property is FALSE for Q -- rational_incomplete_lub. R is"
echo "  the field built to make it true.)"
```

### In the wild

Every theorem of first-year analysis — the extreme and intermediate value
theorems, the mean value theorem, the fundamental theorem of calculus — is
downstream of this one property; `math-real-analysis` takes it as its axiom
`lub_axiom` and this capsule **proves** it. The "sup = union of the cuts"
construction is exact real arithmetic in miniature: a bounded family's supremum
is *computed* (bisection realises it to any precision), not postulated.

```bash [name:app_lub_property, deps:chk_lub_property]
# the sup as a computation: sup { q : q^2 < 2 } by bisection = sqrt(2), to k digits.
lo=1; hi=2
for i in $(seq 1 150); do
  mid=$(echo "scale=50; ($lo + $hi)/2" | bc)
  if [ "$(echo "scale=50; $mid*$mid < 2" | bc)" = 1 ]; then lo=$mid; else hi=$mid; fi
done
echo "sup { q in Q : q^2 < 2 }  (150 bisection steps):"
echo "  = $(echo "$lo" | cut -c1-42)"
echo "  reference sqrt(2)"
echo "  = $(echo "$SQRT2" | cut -c1-42)"
match=$(echo "scale=38; a = $lo - sqrt(2); if (a < 0) a = -a; a < 1/10^36" | bc -l)
[ "$match" = 1 ] || { echo "FAIL: bisected sup does not match sqrt(2)"; exit 1; }
echo "  the supremum lub_property guarantees is exactly the number we can compute."
```

## 8. √2 exists

**`nth_root_exists`**: for every real `x > 0` and every `n ≥ 1` there is a unique
`y > 0` with `yⁿ = x`. Proof: `E = {t > 0 : tⁿ < x}` is nonempty and bounded
above, so `y = sup E` exists by `lub_property`; then `yⁿ < x` and `yⁿ > x` are
each ruled out by nudging, leaving `yⁿ = x`. It fails for `x < 0` and even `n`
(square roots of negatives live in `ℂ`, §8 counterexample), and it fails in `ℚ`
— `√2` is precisely the gap of §4, now filled. *(Rudin; Landau.)*

```bash [name:chk_nth_root_exists, deps:chk_lub_property]
# y = sup { t > 0 : t^n < x }, by bisection   (validation/instance-checks.bc)
lo=1; hi=2
for i in $(seq 1 120); do mid=$(echo "scale=40; ($lo+$hi)/2" | bc); \
  if [ "$(echo "scale=40; $mid*$mid < 2" | bc)" = 1 ]; then lo=$mid; else hi=$mid; fi; done
echo "sqrt(2)   = $(echo "$lo" | cut -c1-34)   check ^2 = $(echo "scale=34; $lo*$lo" | bc | cut -c1-20)"
lo=1; hi=2
for i in $(seq 1 120); do mid=$(echo "scale=40; ($lo+$hi)/2" | bc); \
  if [ "$(echo "scale=40; $mid*$mid*$mid < 2" | bc)" = 1 ]; then lo=$mid; else hi=$mid; fi; done
echo "2^(1/3)   = $(echo "$lo" | cut -c1-34)   check ^3 = $(echo "scale=34; $lo*$lo*$lo" | bc | cut -c1-20)"
```

```bash [name:cx_nth_root_exists, deps:chk_nth_root_exists]
# drop x > 0:  x = -1, n = 2.  E = { t > 0 : t^2 < -1 } is EMPTY (t^2 >= 0 > -1... wait < -1).
echo "x = -1, n = 2:  E = { t > 0 : t^2 < -1 }"
for t in 0.5 1 2 5; do
  echo "  t = $t :  t^2 = $(echo "$t*$t" | bc) ,  < -1 ?  $(echo "$t*$t < -1" | bc)   (0 = no)"
done
echo "E is empty, so sup E does not exist -- there is no real square root of -1."
echo "(it lives in C, which this capsule does not build.)"
```

---

## Capstone — one sequence, two number systems

```bash [name:capstone, deps:"chk_nth_root_exists | chk_rational_incomplete_lub | lean_integer"]
echo "================================================================"
echo "   x_{n+1} = ( x_n + 2/x_n ) / 2 ,      x_0 = 2"
echo "================================================================"
echo
echo "  Built above, in order:"
echo "    Z = (N x N)/~        [chk_integer]   -- + and order well-defined on classes"
echo "    Q = (Z x Z*)/~       [chk_rational_number]"
echo "    sqrt(2) not in Q     [chk_sqrt2_irrational]"
echo "    A = {x^2<2} has no sup in Q          [chk_rational_incomplete_lub]"
echo "    a real = a Dedekind cut             [chk_dedekind_cut]"
echo "    R is an ordered field               [chk_real_is_ordered_field]"
echo "    every bounded S has sup = union     [chk_lub_property]"
echo "    every positive real has an n-th root [chk_nth_root_exists]"
echo
r=$(echo "scale=45; x = 2; for (i = 0; i < 50; i++) x = (x + 2/x)/2; x" | bc -l)
s=$(echo "scale=45; sqrt(2)" | bc -l)
echo "  The Babylonian sequence: every term a rational (a class [(p,q)] in Q)."
echo "    x_50  = $(echo "$r" | cut -c1-40)"
echo "    sqrt2 = $(echo "$s" | cut -c1-40)"
[ "$(echo "$r" | cut -c1-40)" = "$(echo "$s" | cut -c1-40)" ] || { echo "FAIL"; exit 1; }
echo
echo "  IN Q:  the sequence is Cauchy but its 'limit' -- sup { x : x^2 < 2 } --"
echo "         is not a rational. The number is missing."
echo "  IN R:  that supremum IS an element: the cut  { p : p <= 0 or p^2 < 2 }"
echo "         = union { q* : q^2 < 2 },  EXHIBITED by lub_property, and equal to"
echo "         the y from nth_root_exists with y^2 = 2."
echo
echo "  Every step was choice_free and constructive: sqrt(2) was BUILT, not"
echo "  postulated. This is the construction 'math-real-analysis' cites when it"
echo "  says 'R is a complete ordered field, construction assumed' -- lub_property"
echo "  here discharges its axiom lub_axiom."
```

## Where to go next

- The full [`math-number-systems`](../SKILL.md) capsule — `real_uniqueness` (any
  two complete ordered fields are isomorphic), the Cauchy-completion route, and
  the cardinality thread (`ℚ` countable, `ℝ` not).
- [`math-real-analysis`](../../math-real-analysis/SKILL.md) picks up exactly
  here, taking `lub_property` as its axiom; its tutorial
  [`hole-in-the-rationals.md`](../../math-real-analysis/tutorial/hole-in-the-rationals.md)
  runs the same Babylonian sequence from the *analysis* side.
- Other cuts from this capsule: [`docs/tutorial-map.md`](../../../docs/tutorial-map.md).
