# How Much Can This Reaction Actually Make?

> Generated from the `chemistry-foundations` capsule (Release 0.1) with the
> `formula-tree-tutorial` skill. The chemistry, the prerequisite order, and
> every calculation come from that capsule.

A balanced equation is a recipe in *moles*, but you weigh reactants in *grams*
and you never get quite as much product as the recipe promises. This tutorial
walks the capsule's dependency chain from the atomic mass scale up to a
**percent yield** — the fraction of the theoretical maximum a real prep
delivers:

`relative_atomic_mass` → `molar_mass` → `molar_mass_from_formula` →
`amount_from_mass` → `balancing_chemical_equations` → `mole_ratio` →
`limiting_reagent` → `theoretical_yield` → **`percent_yield`**.

## How to run this

Install [upmd](https://upmd.dev), then from the repository root run
`upmd skills/chemistry-foundations/tutorial/how-much-can-this-make.md` for the
interactive walk, or
`upmd --ci --all skills/chemistry-foundations/tutorial/how-much-can-this-make.md`
to run every calculation top to bottom.

Each section ends with a calculation you run yourself. Blocks depend on earlier
ones, so
`upmd --ci -b capstone skills/chemistry-foundations/tutorial/how-much-can-this-make.md`
runs the whole chain up to the capstone. Two blocks call `lean` to
kernel-check an arithmetic instance; if `lean` is not on your `PATH` they print
`SKIP` and pass.

## What you need first

Algebra, ratios, and summation notation; that atoms, isotopes, and elements
exist. These are the capsule's discharged primitives (`si_units`,
`summation_notation`, `ratio_proportion`, `atom`, `atomic_structure`,
`atomic_number`, `element`, `ion`, `isotope`, `chemical_substance`,
`chemical_reaction`) — assumed here, not built.

The dimensional checks track exponents on the `[M, L, T, Θ, N]` basis — mass,
length, time, temperature, and **amount of substance** (`N`, the mole, a base
dimension in this capsule). A consistent relation prints `0 0 0 0 0` for
(left side − right side). Amount `n` has dimension `N`; a raw count is
dimensionless.

---

## 0. Setup

The worked example is the synthesis of water, `2H₂ + O₂ → 2H₂O`. The molar
masses are all values the capsule states (`molar_mass_from_formula` and
`amount_from_mass` entries): `A_r(H) = 1.008`, `A_r(O) = 16.00`, so
`M(H₂) = 2.016`, `M(O₂) = 32.00`, `M(H₂O) = 18.02` g/mol. The scenario masses
are the inputs you would put on the balance.

```bash [name:setup]
export AR_H=1.008         # relative atomic mass of hydrogen (u)
export AR_O=16.00         # relative atomic mass of oxygen (u)
export M_H2=2.016         # g/mol, 2 * A_r(H)
export M_O2=32.00         # g/mol, capsule: "the molecular mass (O2 = 32.00)"
export M_H2O=18.02        # g/mol, capsule: "18.02 g water -> 1 mol"
export MASS_H2=10.0       # g of H2 charged to the reactor
export MASS_O2=64.0       # g of O2 charged to the reactor
export ACTUAL_H2O=68.5    # g of H2O actually recovered
echo "scenario: 2 H2 + O2 -> 2 H2O ; charged ${MASS_H2} g H2 + ${MASS_O2} g O2 ; recovered ${ACTUAL_H2O} g H2O"
```

## 1. Relative atomic mass

An element's `relative_atomic_mass` `A_r(X) = Σᵢ fᵢ Aᵢ` is the abundance-weighted
mean of its isotope masses, in atomic mass units (`1 u = (1/12) m(¹²C)`). The
`fᵢ` are isotopic mole fractions and sum to 1, so `A_r` is a *convex
combination* — it always lands between the lightest and heaviest isotope mass.
`A_r` is dimensionless (a mass *relative* to `u`). The check reproduces the
capsule's chlorine value.

Formula: **`A_r(X) = Σᵢ fᵢ Aᵢ`**

```bash [name:chk_relative_atomic_mass, deps:setup]
bc -l <<'EOF'
scale = 4
/* capsule special case: Cl = 0.7576*34.969 + 0.2424*36.966 */
f35 = 0.7576; a35 = 34.969
f37 = 0.2424; a37 = 36.966
print "f35 + f37 = ", f35 + f37, "  (want 1)\n"
print "A_r(Cl)   = ", f35*a35 + f37*a37, "  (want about 35.45)\n"
EOF
```

```bash [name:lean_relative_atomic_mass, deps:chk_relative_atomic_mass]
command -v lean >/dev/null 2>&1 || { echo "SKIP: lean not on PATH"; exit 0; }
d=$(mktemp -d)
cat > "$d/ar.lean" <<'EOF'
-- capsule validation/derivation-checks.lean, check 10 (relative_atomic_mass)
-- abundances form a convex combination: sum of abundances = 1 (Cl instance x1000)
example : ((758 : Int) + 242) = 1000 := by decide
EOF
if lean "$d/ar.lean"; then
  echo "PASS: Lean kernel verified the abundances sum to 1 (758 + 242 = 1000, x1000)"
else
  echo "FAIL: lean rejected the snippet"; rm -rf "$d"; exit 1
fi
rm -rf "$d"
```

The weights sum to one and the mean sits between 35 and 37 — so a natural
chlorine sample behaves as though every atom weighed 35.45 u.

## 2. The mole and molar mass

`amount_of_substance` (`n`, unit mole, dimension `N`) counts entities;
`N = n · N_A` ties it to a raw number with `N_A = 6.02214076×10²³ mol⁻¹`.
`molar_mass` is the bridge to grams: `M = m / n`, unit g/mol, dimension
`M N⁻¹`. Numerically `M` in g/mol equals `A_r` (or the formula-mass sum) — but
they are different quantities, a mass-per-amount versus a pure ratio. Both
checks are dimensional.

Formula: **`N = n N_A`**  and  **`M = m / n`**

```bash [name:chk_molar_mass, deps:setup]
bc -l <<'EOF'
/* exponents (m, l, t, th, n) */
nm=0; nl=0; nt=0; nth=0; nn=1        /* amount n     -> N     */
am=0; al=0; at=0; ath=0; an=-1       /* N_A          -> N^-1  */
cm=0; cl=0; ct=0; cth=0; cn=0        /* count N      -> 1     */
print "N = n N_A : ", cm-(nm+am)," ",cl-(nl+al)," ",ct-(nt+at)," ",cth-(nth+ath)," ",cn-(nn+an)," (want 0 0 0 0 0)\n"
mm=1; ml=0; mt=0; mth=0; mmn=0       /* mass m       -> M     */
bigm=1; bigl=0; bigt=0; bigth=0; bign=-1   /* molar mass M -> M N^-1 */
print "M = m / n : ", bigm-(mm-nm)," ",bigl-(ml-nl)," ",bigt-(mt-nt)," ",bigth-(mth-nth)," ",bign-(mmn-nn)," (want 0 0 0 0 0)\n"
EOF
```

Count is amount times `N_A` (dimensionless); molar mass is mass over amount
(`M N⁻¹`). Both land clean.

## 3. Molar mass from a formula

For a compound, `molar_mass_from_formula` adds up the atoms:
`M = Σᵢ (countᵢ · A_r,ᵢ)` g/mol. Drop a subscript multiplier and the whole
downstream calculation is wrong. The check reproduces the capsule's sulfuric-acid
value and builds the three molar masses this tutorial needs.

Formula: **`M = Σᵢ (countᵢ · A_r,ᵢ)`**

```bash [name:chk_molar_mass_from_formula, deps:"chk_relative_atomic_mass | chk_molar_mass"]
bc -l <<'EOF'
scale = 3
/* capsule special case: H2SO4 = 2(1.008) + 32.06 + 4(16.00) */
h2so4 = 2*1.008 + 32.06 + 4*16.00
print "M(H2SO4) = ", h2so4, "  (want about 98.08)\n"
EOF
# the scenario's molar masses, from A_r(H) and A_r(O)
awk -v h="$AR_H" -v o="$AR_O" 'BEGIN{
  printf "M(H2)  = 2*%.3f          = %.3f g/mol\n", h, 2*h
  printf "M(O2)  = 2*%.2f          = %.2f g/mol\n", o, 2*o
  printf "M(H2O) = 2*%.3f + %.2f  = %.2f g/mol\n", h, o, 2*h + o
}'
```

The formula sum for H₂SO₄ matches the table, and the same rule gives
`M(H₂) = 2.016`, `M(O₂) = 32.00`, `M(H₂O) = 18.02`.

## 4. Amount from mass

Rearranging `M = m / n` gives `amount_from_mass`: `n = m / M`. This is the step
that turns a balance reading into moles, so the recipe can be applied. Result is
in moles (`N`); the classic error is a unit mismatch, or using an element's
`A_r` where the molecule's `M` is meant (`O` is 16.00, `O₂` is 32.00).

Formula: **`n = m / M`**

```bash [name:chk_amount_from_mass, deps:chk_molar_mass_from_formula]
bc -l <<'EOF'
/* dimensional: [n] = [m] - [M]  ->  N = M - (M N^-1) */
nm=0; nl=0; nt=0; nth=0; nn=1        /* n -> N        */
mm=1; ml=0; mt=0; mth=0; mmn=0       /* m -> M        */
bm=1; bl=0; bt=0; bth=0; bn=-1       /* M -> M N^-1   */
print nm-(mm-bm)," ",nl-(ml-bl)," ",nt-(mt-bt)," ",nth-(mth-bth)," ",nn-(mmn-bn)," (want 0 0 0 0 0)\n"
EOF
# capsule special case: 18.02 g water -> 1 mol ; 9.01 g -> 0.5 mol
awk -v m="$M_H2O" 'BEGIN{
  printf "18.02 / %.2f = %.4f mol   (want 1)\n",   m, 18.02/m
  printf " 9.01 / %.2f = %.4f mol   (want 0.5)\n", m,  9.01/m
}'
```

Mass over molar mass is an amount — and 18.02 g of water is exactly one mole.

## 5. Conservation and balancing

A `chemical_equation` is legal only when every element's atoms
(`conservation_of_mass`) and the total charge (`conservation_of_charge`) match
across the arrow. `balancing_chemical_equations` chooses the
`stoichiometric_coefficient`s (`ν`) that make that true. The check inventories
the atoms of the scenario reaction.

Formula: **`Σ atoms(reactants) = Σ atoms(products)`**, element by element

```bash [name:chk_balancing, deps:setup]
awk 'BEGIN{
  # 2 H2 + 1 O2  ->  2 H2O
  hL = 2*2;  hR = 2*2
  oL = 1*2;  oR = 2*1
  printf "H: %d = %d   O: %d = %d\n", hL, hR, oL, oR
  if (hL==hR && oL==oR) print "PASS: 2 H2 + O2 -> 2 H2O is balanced"
  else { print "FAIL"; exit 1 }
}'
```

Hydrogen and oxygen both balance, so `2, 1, 2` is the recipe.

## 6. The mole ratio

The coefficients are a fixed proportion between *amounts*:
`mole_ratio` is `n_B = n_A · (ν_B / ν_A)`. Never a mass ratio, and never from an
unbalanced equation. The check uses the capsule's worked case, ammonia synthesis.

Formula: **`n_B = n_A · (ν_B / ν_A)`**

```bash [name:chk_mole_ratio, deps:"chk_amount_from_mass | chk_balancing"]
awk 'BEGIN{
  # capsule: N2 + 3 H2 -> 2 NH3 ; 1 mol N2 needs 3 mol H2, gives 2 mol NH3
  nN2 = 1
  nH2  = nN2 * 3 / 1
  nNH3 = nN2 * 2 / 1
  printf "1 mol N2  ->  %g mol H2 needed,  %g mol NH3 produced\n", nH2, nNH3
  if (nH2==3 && nNH3==2) print "PASS: amounts track the 1:3:2 coefficient ratio"
  else { print "FAIL"; exit 1 }
}'
```

One mole of N₂ demands three of H₂ and yields two of NH₃ — the conversion
factor for every "how much" question.

## 7. The limiting reagent

With two reactants, one runs out first and caps the product. Find it by
comparing `nᵢ / νᵢ` across the reactants — **not** raw moles, and not whichever
is lighter. Smallest `nᵢ / νᵢ` is the `limiting_reagent`; the rest are in
excess. The check reproduces the capsule's case, and the Lean beat
kernel-checks the cross-multiplied comparison that decides it.

Formula: **limiting = argminᵢ (nᵢ / νᵢ)**

```bash [name:chk_limiting_reagent, deps:chk_mole_ratio]
awk 'BEGIN{
  # capsule special case: 1 mol N2 + 1 mol H2, N2 + 3 H2 -> 2 NH3
  nN2 = 1; nuN2 = 1
  nH2 = 1; nuH2 = 3
  rN2 = nN2/nuN2        # 1/1 = 1
  rH2 = nH2/nuH2        # 1/3 = 0.333
  printf "n/nu:  N2 = %.3f   H2 = %.3f\n", rN2, rH2
  lim = (rH2 < rN2) ? "H2" : "N2"
  nNH3 = (rH2 < rN2 ? rH2 : rN2) * 2   # extent * nu(NH3)
  printf "limiting reagent = %s ;  max NH3 = %.2f mol\n", lim, nNH3
  if (lim=="H2" && nNH3 > 0.66 && nNH3 < 0.67) print "PASS: H2 limits, ~0.67 mol NH3 (matches capsule)"
  else { print "FAIL"; exit 1 }
}'
```

```bash [name:lean_limiting_reagent, deps:chk_limiting_reagent]
command -v lean >/dev/null 2>&1 || { echo "SKIP: lean not on PATH"; exit 0; }
d=$(mktemp -d)
cat > "$d/lim.lean" <<'EOF'
-- capsule validation/derivation-checks.lean, check 12 (limiting_reagent)
-- N2 (1 mol, nu 1) + H2 (1 mol, nu 3): compare 1/1 vs 1/3 by cross-multiplying,
-- 1*3 vs 1*1  =>  the H2 ratio (1/3) is the smaller, so H2 limits.
example : (1 * 3 : Int) > (1 * 1) := by decide
EOF
if lean "$d/lim.lean"; then
  echo "PASS: Lean kernel verified 1*3 > 1*1, so 1/3 < 1/1 and H2 is limiting"
else
  echo "FAIL: lean rejected the snippet"; rm -rf "$d"; exit 1
fi
rm -rf "$d"
```

H₂ has the smaller `n / ν`, so it limits — even though there is exactly as much
H₂ as N₂ by moles.

## 8. Theoretical yield

The `theoretical_yield` is what you would get if the limiting reagent were
consumed completely: `n_product = n_limiting · (ν_product / ν_limiting)`, then
`m = n · M` for a mass. Base it on the limiting reagent, never the excess one,
and convert to whatever unit the question asks.

Formula: **`n_product = n_limiting · (ν_product / ν_limiting)`,  `m = n M`**

```bash [name:chk_theoretical_yield, deps:"chk_limiting_reagent | chk_molar_mass_from_formula"]
awk -v mH2O="$M_H2O" 'BEGIN{
  # carry the capsule case forward: H2 limits at n/nu = 1/3, product NH3 nu = 2
  # (using NH3 here would need M(NH3); demonstrate n->m with M(H2O) instead)
  nProd = (1.0/3.0) * 2            # 0.667 mol of product per the ratio
  printf "n_product      = (1/3) * 2 = %.3f mol\n", nProd
  printf "as a mass (M = %.2f g/mol) : m = n M = %.2f g\n", mH2O, nProd*mH2O
  if (nProd > 0.66 && nProd < 0.67) print "PASS: 0.667 mol, matching the limiting-reagent step"
  else { print "FAIL"; exit 1 }
}'
```

The limiting reagent fixes the product amount; `m = nM` turns it into grams.

## 9. Percent yield

Real preps lose product — to side reactions, to transfers, to incomplete
reaction. The `percent_yield` is what fraction of the theoretical maximum you
actually isolated: `%yield = (actual / theoretical) · 100`, same units top and
bottom. A value above 100 % means a wet or impure product or a weighing error —
never a real excess.

Formula: **`%yield = (actual / theoretical) · 100`**

```bash [name:chk_percent_yield, deps:chk_theoretical_yield]
awk 'BEGIN{
  actual = 8.5; theoretical = 10.0
  y = actual / theoretical * 100
  printf "actual %.1f g / theoretical %.1f g * 100 = %.1f %%\n", actual, theoretical, y
  if (y == 85) print "PASS: 85% yield"
  else { print "FAIL"; exit 1 }
  # a value over 100 is a red flag, not a bonus:
  bad = 11.5 / 10.0 * 100
  printf "if you measured 11.5 g: %.0f %% -> impure/wet product, not a real excess\n", bad
}'
```

Actual over theoretical, as a percent — the single number that says how well the
prep went.

---

## Capstone: yield of the water synthesis

You have the whole chain. Weigh out the reactants from Setup, find the limiting
reagent, compute the theoretical mass of water, and compare it to what was
recovered.

```bash [name:capstone, deps:"chk_percent_yield | chk_amount_from_mass | chk_mole_ratio"]
# 1. masses -> moles  (n = m / M)
nH2=$(echo "scale=4; $MASS_H2 / $M_H2" | bc -l)
nO2=$(echo "scale=4; $MASS_O2 / $M_O2" | bc -l)
echo "n(H2) = ${MASS_H2} / ${M_H2} = ${nH2} mol"
echo "n(O2) = ${MASS_O2} / ${M_O2} = ${nO2} mol"

# 2. limiting reagent: compare n / nu   (nu_H2 = 2, nu_O2 = 1)
rH2=$(echo "scale=4; $nH2 / 2" | bc -l)
rO2=$(echo "scale=4; $nO2 / 1" | bc -l)
echo "n/nu:  H2 = ${rH2}   O2 = ${rO2}"
lim=$(awk -v a="$rH2" -v b="$rO2" 'BEGIN{ print (a < b) ? "H2" : "O2" }')
ext=$(awk -v a="$rH2" -v b="$rO2" 'BEGIN{ print (a < b) ? a : b }')
echo "limiting reagent = ${lim}  (reaction extent = ${ext})"

# 3. theoretical yield of H2O:  n = extent * nu(H2O) = extent * 2 ;  m = n M
nH2O=$(echo "scale=4; $ext * 2" | bc -l)
mH2O=$(echo "scale=2; $nH2O * $M_H2O" | bc -l)
echo "theoretical: n(H2O) = ${ext} * 2 = ${nH2O} mol  ->  m = ${nH2O} * ${M_H2O} = ${mH2O} g"

# 4. percent yield
pct=$(echo "scale=2; $ACTUAL_H2O / $mH2O * 100" | bc -l)
echo "recovered ${ACTUAL_H2O} g  ->  percent yield = ${ACTUAL_H2O} / ${mH2O} * 100 = ${pct} %"

awk -v p="$pct" 'BEGIN{
  if (p > 0 && p < 100) print "PASS: a physically sensible yield below the theoretical maximum"
  else { print "FAIL: yield out of range"; exit 1 }
}'
```

If the capstone prints `PASS`, every link held: isotope masses gave molar
masses, molar masses turned grams into moles, the balanced equation set the
ratio, the limiting reagent capped the product, and the recovered mass came in
under the theoretical ceiling — as a real reaction always does.

## Where to go next

- The full [`chemistry-foundations`](../SKILL.md) capsule — solution and gas
  stoichiometry, thermochemistry, equilibrium, acid–base, redox.
- `solution_stoichiometry` (`n = cV`, then the mole ratio) and `titration` —
  the same yield logic for reactions in solution.
- `gas_stoichiometry` — the mole ratio combined with `PV = nRT`.
- `empirical_formula` and `molecular_formula` — the reverse direction, going
  from percent composition back to a formula (`indexes/topic-index.md`, the mole
  band).
- The sibling tutorial
  [`reaction-enthalpy-from-formation.md`](reaction-enthalpy-from-formation.md) —
  the *energy* released by a reaction, from a formation table.
