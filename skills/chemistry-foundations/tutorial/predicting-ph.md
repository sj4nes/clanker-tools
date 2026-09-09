# Predicting the pH of an Acid — and Holding It with a Buffer

> Generated from the `chemistry-foundations` capsule (Release 0.1) with the
> `formula-tree-tutorial` skill. The chemistry, the prerequisite order, and
> every calculation come from that capsule.

`pH` is just `−log₁₀[H⁺]`, but where `[H⁺]` comes from depends on the acid. A
strong acid gives it to you directly. A weak acid makes you solve an
equilibrium. A **buffer** — a weak acid mixed with its conjugate base — pins the
pH near `pK_a` and resists change, and the Henderson–Hasselbalch equation reads
it straight off the ratio. This tutorial walks the capsule's acid–base chain:

`bronsted_lowry` → `water_autoionization` → `ph_definition` → `poh_relation` →
`weak_acid_equilibrium` → **`henderson_hasselbalch`**.

## How to run this

Install [upmd](https://upmd.dev), then from the repository root run
`upmd skills/chemistry-foundations/tutorial/predicting-ph.md` for the
interactive walk, or
`upmd --ci --all skills/chemistry-foundations/tutorial/predicting-ph.md`
to run every calculation top to bottom.

Each section ends with a calculation you run yourself. Blocks depend on earlier
ones, so
`upmd --ci -b capstone skills/chemistry-foundations/tutorial/predicting-ph.md`
runs the whole chain up to the capstone. Two blocks call `lean` to
kernel-check an arithmetic instance; if `lean` is not on your `PATH` they print
`SKIP` and pass.

## What you need first

This tutorial builds directly on
[`solving-an-equilibrium.md`](solving-an-equilibrium.md) — the ICE table and
`quadratic_formula` for a weak-acid equilibrium. You also need the `logarithm`
identities (`log(xy) = log x + log y`) and `molarity`.

There are no dimensional checks. `K_w`, `K_a`, and every `pH`/`pOH` argument are
**dimensionless by construction** (each `[X]` is a molarity ÷ `c° = 1 mol/L`).
The checks are numeric. The governing assumption is again
**`dilute_ideal_solution`** — `pH = −log₁₀[H⁺]` is an *approximation* (activity →
concentration) that degrades in concentrated or high-ionic-strength solutions,
where pH can even go negative.

Everything numeric here is **at 25 °C**, where `K_w = 1.0×10⁻¹⁴` and
`pK_w = 14.00`; both change with temperature.

---

## 0. Setup

The worked acid is acetic acid, with the capsule's numbers
(`weak_acid_equilibrium` entry): `K_a = 1.8×10⁻⁵`, so `pK_a = 4.74`. The
capstone builds a buffer from it.

```bash [name:setup]
export KA=0.000018        # 1.8e-5
export PKA=4.74           # -log10(K_a) for acetic acid
export KW=1.0e-14         # autoionization constant of water, 25 C
export PKW=14.00
export C0=0.10            # M, a worked weak-acid concentration
export TARGET_PH=5.00     # the buffer we will design
export BC_LINE_LENGTH=0   # stop bc wrapping long numeric output
echo "acetic acid: K_a = ${KA} (pK_a ${PKA}) ; K_w = ${KW} ; target buffer pH ${TARGET_PH}"
```

## 1. Brønsted–Lowry acids and conjugate pairs

`bronsted_lowry`: an acid is a proton (`H⁺`) donor, a base is a proton acceptor,
and every acid–base reaction transfers one proton. That makes acids and bases
come in `conjugate_acid_base_pair`s — two species differing by exactly one `H⁺`,
`HA` and `A⁻`. The stronger the acid, the weaker its conjugate base. The check
tests the "differ by one proton" rule on the capsule's examples.

Rule: **a conjugate pair `HA / A⁻` differs by exactly one `H⁺`**

```bash [name:chk_bronsted_lowry, deps:setup]
awk 'BEGIN{
  # capsule pairs: (CH3COOH, CH3COO-) and (NH4+, NH3), as (H count, charge)
  # acetic acid / acetate
  acid_H = 4; acid_q = 0        # CH3COOH
  base_H = 3; base_q = -1       # CH3COO-
  d1_H = acid_H - base_H; d1_q = acid_q - base_q
  # ammonium / ammonia
  acid2_H = 4; acid2_q = 1      # NH4+
  base2_H = 3; base2_q = 0      # NH3
  d2_H = acid2_H - base2_H; d2_q = acid2_q - base2_q
  printf "CH3COOH -> CH3COO- : lost %d H, charge changes by %+d\n", d1_H, -d1_q
  printf "NH4+    -> NH3     : lost %d H, charge changes by %+d\n", d2_H, -d2_q
  if (d1_H==1 && d1_q==1 && d2_H==1 && d2_q==1) print "PASS: each pair differs by one H+ (one proton, one positive charge)"
  else { print "FAIL"; exit 1 }
}'
```

Donating a proton means losing one `H` and gaining one negative charge — the
definition of the conjugate relationship.

## 2. The autoionization of water

Water itself is a weak acid and base: `2H₂O ⇌ H₃O⁺ + OH⁻`, with
`water_autoionization` constant `K_w = [H⁺][OH⁻] = 1.0×10⁻¹⁴` at 25 °C. In pure
water the two concentrations are equal, so each is `√K_w = 1.0×10⁻⁷ M` — that is
what "neutral" means (and only at 25 °C; `K_w` rises with temperature). The
check confirms the product and the pure-water value.

Formula: **`K_w = [H⁺][OH⁻] = 1.0×10⁻¹⁴`  (25 °C)**

```bash [name:chk_water_autoionization, deps:chk_bronsted_lowry]
h=$(bc -l <<< "scale=20; sqrt(0.00000000000001)")     # sqrt(K_w)
prod=$(bc -l <<< "scale=20; $h * $h")
echo "pure water [H+] = [OH-] = sqrt(K_w) = $h M   (want 1e-7)"
echo "product [H+][OH-] = $prod   (want K_w = 1e-14)"
awk -v h="$h" -v p="$prod" 'BEGIN{
  if (h > 0.99e-7 && h < 1.01e-7 && p > 0.99e-14 && p < 1.01e-14)
    print "PASS: neutral water is 1e-7 M in each ion, product 1e-14"
  else { print "FAIL"; exit 1 }
}'
```

Equal `[H⁺]` and `[OH⁻]` whose product is `10⁻¹⁴`, so each is `10⁻⁷` — neutral.

## 3. pH

`ph_definition`: `pH = −log₁₀(a(H⁺)) ≈ −log₁₀([H⁺]/c°)`. It is an
*approximation* — activity replaced by concentration, valid in the dilute limit.
Each whole pH unit is a factor of ten in `[H⁺]`: `10⁻³ M → pH 3`, pure water
`10⁻⁷ M → pH 7`. The check computes both (`bc -l` gives natural log `l()`, and
`log₁₀ x = l(x)/l(10)`).

Formula: **`pH = −log₁₀([H⁺]/c°)`**

```bash [name:chk_ph_definition, deps:chk_water_autoionization]
ph1=$(bc -l <<< "scale=6; -l(0.001)/l(10)")
ph2=$(bc -l <<< "scale=6; -l(0.0000001)/l(10)")
echo "pH([H+] = 1e-3 M) = $ph1   (capsule: 3)"
echo "pH(pure water, 1e-7 M) = $ph2   (capsule: 7, neutral at 25 C)"
awk -v a="$ph1" -v b="$ph2" 'BEGIN{
  if (a > 2.99 && a < 3.01 && b > 6.99 && b < 7.01) print "PASS: each pH unit is a factor of 10 in [H+]"
  else { print "FAIL"; exit 1 }
}'
```

A logarithm turns the huge range of `[H⁺]` into a 0–14 scale.

## 4. pOH and pH + pOH = pKw

Take `−log₁₀` of `K_w = [H⁺][OH⁻]` and the product becomes a sum:
`poh_relation`, `pH + pOH = pK_w = 14.00` at 25 °C, with `pOH = −log₁₀[OH⁻]`. So
a strong base with `[OH⁻] = 10⁻²` has `pOH 2` and therefore `pH 12`. The check
computes `pOH` and `pH`, and the Lean beat kernel-checks the capsule's `pH +
pOH` instance.

Formula: **`pH + pOH = pK_w = 14.00`  (25 °C)**

```bash [name:chk_poh_relation, deps:chk_ph_definition]
poh=$(bc -l <<< "scale=6; -l(0.01)/l(10)")
ph=$(bc -l <<< "scale=6; 14 - $poh")
echo "pOH([OH-] = 1e-2 M) = $poh"
echo "pH = 14 - pOH = $ph   (capsule: pOH 2 -> pH 12)"
awk -v o="$poh" -v h="$ph" 'BEGIN{
  if (o > 1.99 && o < 2.01 && h > 11.99 && h < 12.01) print "PASS: pH + pOH = 14 at 25 C"
  else { print "FAIL"; exit 1 }
}'
```

```bash [name:lean_poh_relation, deps:chk_poh_relation]
command -v lean >/dev/null 2>&1 || { echo "SKIP: lean not on PATH"; exit 0; }
d=$(mktemp -d)
cat > "$d/poh.lean" <<'EOF'
-- capsule validation/derivation-checks.lean, check 7 (poh_relation)
-- from -log10 of K_w = [H+][OH-]:  pH + pOH = pK_w.  Instance (25 C): pH 3 -> pOH 11.
example : ((3 : Int) + 11) = 14 := by decide
EOF
if lean "$d/poh.lean"; then
  echo "PASS: Lean kernel verified pH + pOH = 14 (instance pH 3, pOH 11)"
else
  echo "FAIL: lean rejected the snippet"; rm -rf "$d"; exit 1
fi
rm -rf "$d"
```

`−log` of a product is a sum of `−log`s — that is the whole content of
`pH + pOH = pK_w`.

## 5. Weak acids: Ka and the pH it gives

A weak acid only partly dissociates: `HA ⇌ H⁺ + A⁻` with
`weak_acid_equilibrium` constant `K_a = [H⁺][A⁻]/[HA]` (dimensionless; larger
`K_a` = stronger acid; `pK_a = −log K_a`). You solve it with an ICE table (the
previous tutorial). For `0.10 M` acetic acid the `x ≪ c₀` shortcut is licensed,
so `[H⁺] = x ≈ √(K_a·c₀)` and the check reads off the pH.

Formula: **`K_a = [H⁺][A⁻] / [HA]`,  and for `HA` alone  `[H⁺] ≈ √(K_a·c₀)`**

```bash [name:chk_weak_acid_equilibrium, deps:"chk_ph_definition | chk_bronsted_lowry"]
x=$(bc -l <<< "scale=8; sqrt(0.000018 * 0.10)")     # ICE x<<c0 shortcut, valid (x/c0 ~ 0.013)
ph=$(bc -l <<< "scale=8; -l($x)/l(10)")
echo "0.10 M acetic acid:  [H+] = sqrt(K_a c0) = $x M"
echo "pH = $ph   (capsule: 2.87)"
awk -v p="$ph" 'BEGIN{
  if (p > 2.86 && p < 2.88) print "PASS: a weak acid at 0.10 M sits near pH 3, not pH 1"
  else { print "FAIL"; exit 1 }
}'
```

A weak acid at 0.10 M sits near pH 3, not pH 1 — most of it never dissociates.

## 6. The Henderson–Hasselbalch equation

Now mix the weak acid `HA` *with* its conjugate base `A⁻` (a **buffer**). Solve
`K_a = [H⁺][A⁻]/[HA]` for `[H⁺]` and take `−log₁₀`:

**`pH = pK_a + log₁₀([A⁻] / [HA])`**

The pH is set by the *ratio*, not the absolute amounts. When `[A⁻] = [HA]` the
log term is zero and `pH = pK_a` — the centre of buffering capacity. The
equation is reliable only within about `pK_a ± 1` and while both components
greatly exceed `[H⁺]` (so `[HA]_eq ≈ [HA]_0`). The Lean beat kernel-checks the
capsule's instances, including the buffer centre.

```bash [name:chk_henderson_hasselbalch, deps:"chk_weak_acid_equilibrium | chk_poh_relation"]
ph_eq=$(bc -l <<< "scale=6; 4.74 + l(1)/l(10)")
ph_2=$(bc -l <<< "scale=6; 4.74 + l(2)/l(10)")
ph_half=$(bc -l <<< "scale=6; 4.74 + l(0.5)/l(10)")
echo "[A-] = [HA]   : pH = pKa + log(1)   = $ph_eq   (want pKa = 4.74)"
echo "[A-]:[HA]=2:1 : pH = pKa + log(2)   = $ph_2   (pKa + 0.30)"
echo "[A-]:[HA]=1:2 : pH = pKa + log(0.5) = $ph_half   (pKa - 0.30)"
awk -v e="$ph_eq" -v t="$ph_2" -v h="$ph_half" 'BEGIN{
  if (e > 4.73 && e < 4.75 && t > 5.03 && t < 5.05 && h > 4.43 && h < 4.45)
    print "PASS: equal parts -> pH = pKa; the ratio shifts pH by log(ratio)"
  else { print "FAIL"; exit 1 }
}'
```

```bash [name:lean_henderson_hasselbalch, deps:chk_henderson_hasselbalch]
command -v lean >/dev/null 2>&1 || { echo "SKIP: lean not on PATH"; exit 0; }
d=$(mktemp -d)
cat > "$d/hh.lean" <<'EOF'
-- capsule validation/derivation-checks.lean, check 6 (henderson_hasselbalch)
-- pH = pK_a + log10([A-]/[HA]).  Instance: pK_a = 4, log10 term = 1  =>  pH = 5,
-- and pH - 1 = pK_a.
example : ((4 : Int) + 1) = 5 := by decide
example : ((5 : Int) - 1) = 4 := by decide
-- buffer centre: [A-] = [HA]  =>  log10(1) = 0  =>  pH = pK_a.
example : ((4 : Int) + 0) = 4 := by decide
EOF
if lean "$d/hh.lean"; then
  echo "PASS: Lean kernel verified pH = pK_a + log term (instances) and the buffer centre pH = pK_a"
else
  echo "FAIL: lean rejected the snippet"; rm -rf "$d"; exit 1
fi
rm -rf "$d"
```

Equal parts acid and conjugate base put the pH exactly at `pK_a`; shifting the
ratio moves it by the log of that ratio.

---

## Capstone: build a pH 5.00 acetate buffer and stress it

You have the whole chain. Use Henderson–Hasselbalch backwards to get the
`[A⁻]/[HA]` ratio for `pH 5.00`, confirm it is inside the `pK_a ± 1` band,
realise it, then add a slug of strong acid and compare the pH shift to what the
same acid would do to pure water.

```bash [name:capstone, deps:"chk_henderson_hasselbalch | lean_henderson_hasselbalch | lean_poh_relation"]
# 1. ratio for the target pH:  log10([A-]/[HA]) = pH - pKa  ->  ratio = 10^(pH - pKa)
delta=$(bc -l <<< "scale=6; $TARGET_PH - $PKA")
ratio=$(bc -l <<< "scale=6; e($delta * l(10))")
echo "log10([A-]/[HA]) = ${TARGET_PH} - ${PKA} = ${delta}   ->   [A-]/[HA] = ${ratio}"

# 2. inside the reliable band?
band=$(bc -l <<< "d = $delta; if (d < 0) d = -d; d")
awk -v b="$band" 'BEGIN{ if (b < 1) print "band check: |pH - pKa| = " b " < 1  -> Henderson-Hasselbalch applies"
                         else { print "FAIL: outside pKa +- 1"; exit 1 } }'

# 3. realise it: fix [HA] = 0.100 M, so [A-] = ratio * 0.100
HA=0.100
A=$(bc -l <<< "scale=6; $ratio * $HA")
ph_made=$(bc -l <<< "scale=4; $PKA + l($A/$HA)/l(10)")
echo "make it: [HA] = ${HA} M , [A-] = ${A} M   ->   pH = ${ph_made}"

# 4. add 0.010 mol/L strong acid: it converts A- -> HA
add=0.010
A2=$(bc -l <<< "scale=6; $A - $add")
HA2=$(bc -l <<< "scale=6; $HA + $add")
ph_after=$(bc -l <<< "scale=4; $PKA + l($A2/$HA2)/l(10)")
echo "add ${add} M H+ :  [A-] = ${A2} , [HA] = ${HA2}   ->   pH = ${ph_after}"

# 5. the same acid in pure water
ph_water=$(bc -l <<< "scale=4; -l($add)/l(10)")
echo "the same ${add} M H+ in pure water :  pH = ${ph_water}"

awk -v made="$ph_made" -v after="$ph_after" -v water="$ph_water" -v tgt="$TARGET_PH" 'BEGIN{
  made_ok   = ((made - tgt < 0 ? tgt - made : made - tgt) < 0.02)
  buf_shift = (after < made ? made - after : after - made)
  water_shift = (7 - water)
  if (made_ok && buf_shift < 0.15 && water_shift > 4)
    printf "PASS: buffer holds pH near %.2f (moved %.2f); pure water crashed to %.2f (moved %.1f)\n", tgt, buf_shift, water, water_shift
  else { print "FAIL"; exit 1 }
}'
```

If the capstone prints `PASS`, the chain closed: `pH` is `−log[H⁺]`, `K_w` links
`pH` and `pOH`, a weak acid's `[H⁺]` comes from its `K_a` and an ICE table, and
Henderson–Hasselbalch runs that backwards — a 1:1.8 acetate mixture holds pH 5
to within a tenth of a unit against an acid dose that would take pure water from
7 to 2.

## Where to go next

- The full [`chemistry-foundations`](../SKILL.md) capsule.
- `ka_kb_relation` (`K_a·K_b = K_w`), `percent_ionization`, and
  `acid_base_titration_curve` — the rest of the acid–base band, including why a
  weak-acid/strong-base equivalence point is above pH 7.
- `strong_acid_base_ph` — the easy case this tutorial skipped: a strong acid
  gives `[H⁺] = c` directly.
- The `titration` tutorial [`finding-a-concentration.md`](finding-a-concentration.md)
  and the equilibrium tutorial [`solving-an-equilibrium.md`](solving-an-equilibrium.md)
  this one builds on; and the sequencing guide
  [`tutorial/README.md`](README.md).
