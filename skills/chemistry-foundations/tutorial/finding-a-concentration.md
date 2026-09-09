# Finding an Unknown Concentration by Titration

> Generated from the `chemistry-foundations` capsule (Release 0.1) with the
> `formula-tree-tutorial` skill. The chemistry, the prerequisite order, and
> every calculation come from that capsule.

You have a solution of something and you need to know how concentrated it is.
Titration answers that: run in a reagent of *known* concentration until it has
exactly consumed the unknown, read the volume delivered, and the balanced
equation does the rest. This tutorial walks the capsule's solutions chain to
that calculation:

`molarity` → `dilution_equation` → `solution_stoichiometry` → `titration` →
**`equivalence_point`**.

## How to run this

Install [upmd](https://upmd.dev), then from the repository root run
`upmd skills/chemistry-foundations/tutorial/finding-a-concentration.md` for the
interactive walk, or
`upmd --ci --all skills/chemistry-foundations/tutorial/finding-a-concentration.md`
to run every calculation top to bottom.

Each section ends with a calculation you run yourself. Blocks depend on earlier
ones, so
`upmd --ci -b capstone skills/chemistry-foundations/tutorial/finding-a-concentration.md`
runs the whole chain up to the capstone.

## What you need first

Algebra and ratios; SI units; that a `chemical_equation` can be balanced and its
`stoichiometric_coefficient`s (`ν`) read as a `mole_ratio` (`n_B = n_A · ν_B/ν_A`
— covered in the stoichiometry tutorials). These are the capsule's upstream
nodes, assumed here.

The dimensional checks track exponents on the `[M, L, T, Θ, N]` basis — mass,
length, time, temperature, and amount of substance (`N`, the mole). A consistent
relation prints `0 0 0 0 0` for (left side − right side). Concentration `c` has
dimension `N L⁻³`; an amount `n` has dimension `N`.

All of this is the **dilute limit** in spirit, but note: `molarity`,
`dilution_equation`, `solution_stoichiometry`, `titration`, and
`equivalence_point` are *exact* stoichiometric bookkeeping — they do **not**
carry the `dilute_ideal_solution` assumption (that node only feeds the
equilibrium and pH relations). A titration calculation is as accurate as your
volumes and your standard.

---

## 0. Setup

The worked example is a sulfuric-acid sample of unknown concentration, titrated
with sodium hydroxide: `H₂SO₄ + 2NaOH → Na₂SO₄ + 2H₂O` (a diprotic acid against
a monobasic base — the capsule's `equivalence_point` special case, ratio 1:2).
The NaOH titrant is itself made by dilution from a stock.

```bash [name:setup]
export C_STOCK=1.000       # M, NaOH stock concentration
export V_STOCK_ML=10.00    # mL of stock taken
export V_TITRANT_ML=100.0  # mL, final titrant volume after dilution
export V_ANALYTE_ML=25.00  # mL of the unknown H2SO4 pipetted
export V_EQ_ML=32.40       # mL of titrant delivered to reach the equivalence point
export NU_ANALYTE=1        # stoichiometric coefficient of H2SO4
export NU_TITRANT=2        # stoichiometric coefficient of NaOH
echo "titrate ${V_ANALYTE_ML} mL unknown H2SO4 with diluted NaOH; equivalence at ${V_EQ_ML} mL"
```

## 1. Molarity

`molarity` is amount of solute per litre of **solution** (not of solvent):
`c = n / V`, unit mol/L (written `M`), dimension `N L⁻³`. The classic error is
measuring the volume of solvent you added rather than the final solution volume
— they differ because mixing changes volume. The check is dimensional, then the
capsule's worked number.

Formula: **`c = n / V`**

```bash [name:chk_molarity, deps:setup]
bc -l <<'EOF'
/* exponents (m, l, t, th, n) */
cm=0; cl=-3; ct=0; cth=0; cn=1      /* c -> N L^-3 */
nm=0; nl=0; nt=0; nth=0; nn=1       /* n -> N     */
vm=0; vl=3; vt=0; vth=0; vn=0       /* V -> L^3   */
print cm-(nm-vm)," ",cl-(nl-vl)," ",ct-(nt-vt)," ",cth-(nth-vth)," ",cn-(nn-vn)," (want 0 0 0 0 0)\n"
EOF
# capsule special case: 0.5 mol in 2 L -> 0.25 M
awk 'BEGIN{
  c = 0.5 / 2.0
  printf "0.5 mol / 2 L = %.2f M   (capsule: 0.25)\n", c
  if (c == 0.25) print "PASS"; else { print "FAIL"; exit 1 }
}'
```

Amount over solution volume; `N L⁻³` is the dimension of every concentration
below.

## 2. Dilution

Adding solvent changes the volume and the concentration but **not** the amount
of solute, so `n = cV` is constant across a dilution: `dilution_equation`,
`c₁V₁ = c₂V₂`. Any consistent volume unit works (the litres cancel). It applies
*only* across a dilution — never across a reaction, where moles are consumed.
The check confirms both sides are an amount, then the capsule's worked number.

Formula: **`c₁V₁ = c₂V₂`**

```bash [name:chk_dilution_equation, deps:chk_molarity]
bc -l <<'EOF'
/* c V on each side must be an amount, N */
cm=0; cl=-3; ct=0; cth=0; cn=1
vm=0; vl=3; vt=0; vth=0; vn=0
print (cm+vm)-0," ",(cl+vl)-0," ",(ct+vt)-0," ",(cth+vth)-0," ",(cn+vn)-1," (want 0 0 0 0 0, i.e. c*V = N)\n"
EOF
# capsule special case: 10 mL of 6 M HCl diluted to 100 mL
awk 'BEGIN{
  c1 = 6.0; v1 = 10.0; v2 = 100.0
  c2 = c1 * v1 / v2
  printf "6 M * 10 mL / 100 mL = %.1f M   (capsule: 0.6)\n", c2
  if (c2 == 0.6) print "PASS"; else { print "FAIL"; exit 1 }
}'
```

`c·V` is an amount on both sides, and diluting 6 M acid ten-fold gives 0.6 M.

## 3. Solution stoichiometry

To bring a solution into a reaction calculation, convert concentration and
volume to moles (`n = cV`), then apply the balanced-equation `mole_ratio` like
any other stoichiometry. `solution_stoichiometry` is exactly that two-step. The
check reproduces the capsule's silver-chloride precipitation, a 1:1 case.

Formula: **`n = cV`,  then  `n_B = n_A · (ν_B / ν_A)`**

```bash [name:chk_solution_stoichiometry, deps:chk_molarity]
awk 'BEGIN{
  # capsule special case: 25.0 mL of 0.100 M AgNO3
  c = 0.100; v_L = 25.0 / 1000
  nAg = c * v_L
  # Ag+ + Cl- -> AgCl(s) , ratio 1:1
  nAgCl = nAg * 1 / 1
  printf "n(Ag+)  = %.4f M * %.4f L = %.3e mol\n", c, v_L, nAg
  printf "n(AgCl) = %.3e mol   (capsule: 2.50e-3, ratio 1:1)\n", nAgCl
  # compare to 2.50e-3 within rounding
  d = (nAgCl > 0.00250) ? nAgCl - 0.00250 : 0.00250 - nAgCl
  if (d < 1e-6) print "PASS"; else { print "FAIL"; exit 1 }
}'
```

Concentration times volume is moles; the 1:1 ratio carries it straight to the
product.

## 4. Titration

`titration` delivers a reagent of known concentration (the *titrant*) from a
burette until it has exactly consumed the *analyte*. The volume at that point —
signalled by an indicator colour change or an instrument — is taken as the
equivalence point. The relation being solved is always
`n(titrant) = (ν_titrant / ν_analyte) · n(analyte)`. The one systematic error to
respect: the **endpoint** (what you observe) is not identical to the
**equivalence point** (where the reaction is stoichiometrically complete) unless
the indicator is well matched to the curve.

Rule: **at the equivalence point, `n(titrant) = (ν_titrant / ν_analyte) · n(analyte)`**

```bash [name:chk_titration, deps:chk_solution_stoichiometry]
awk 'BEGIN{
  # demonstrate the relation on round numbers: analyte 1.00e-3 mol, ratio 2:1
  nA = 1.00e-3
  nuT = 2; nuA = 1
  nT = (nuT / nuA) * nA
  printf "n(analyte) = %.2e mol, ratio nuT:nuA = %d:%d  ->  n(titrant) = %.2e mol\n", nA, nuT, nuA, nT
  if (nT == 2.00e-3) print "PASS: twice the analyte amount, as a 2:1 ratio demands"
  else { print "FAIL"; exit 1 }
}'
```

The titrant amount at the equivalence point is fixed by the analyte amount and
the coefficient ratio — nothing else.

## 5. The equivalence point

Rearrange the titration relation to solve for what you came for — the analyte
concentration:

**`c_analyte = c_titrant · V_titrant · (ν_analyte / ν_titrant) / V_analyte`**

Both `c_titrant · V_titrant` and `c_analyte · V_analyte` are amounts (`N`); the
coefficient ratio is dimensionless; so the whole right side has dimension
`N L⁻³`, a concentration. The check confirms that, then the capsule's
diprotic-vs-monobasic case (ratio 1:2 → the acid needs twice its own volume of
base).

```bash [name:chk_equivalence_point, deps:"chk_titration | chk_dilution_equation"]
bc -l <<'EOF'
/* c_A = c_T V_T (nuA/nuT) / V_A  ;  ratio dimensionless */
cm=0; cl=-3; ct=0; cth=0; cn=1     /* c_T -> N L^-3 */
vm=0; vl=3; vt=0; vth=0; vn=0      /* V   -> L^3   */
/* [c_T] + [V_T] - [V_A]  should equal [c_A] = (0,-3,0,0,1) */
print (cm+vm-vm)-0," ",(cl+vl-vl)-(-3)," ",(ct+vt-vt)-0," ",(cth+vth-vth)-0," ",(cn+vn-vn)-1," (want 0 0 0 0 0)\n"
EOF
# capsule special case: diprotic acid vs monobasic base, equal concentrations
awk 'BEGIN{
  # H2A + 2 B -> ... ; nu(acid)=1, nu(base)=2 ; if c(acid) = c(base) then
  # V(base) at equivalence = 2 * V(acid)
  cAcid = 0.10; cBase = 0.10; vAcid = 25.0
  vBase = cAcid * vAcid * (2.0/1.0) / cBase
  printf "25.0 mL of 0.10 M diprotic acid needs %.1f mL of 0.10 M base  (capsule: twice the volume)\n", vBase
  if (vBase == 50.0) print "PASS"; else { print "FAIL"; exit 1 }
}'
```

The right side is a concentration, and a diprotic acid consumes twice its volume
of an equal-strength monobasic base.

---

## Capstone: the unknown sulfuric acid

You have the whole chain. First make the titrant by dilution, then use the
equivalence-point volume to back out the acid concentration.

```bash [name:capstone, deps:"chk_equivalence_point | chk_dilution_equation"]
# 1. prepare the titrant: dilute the NaOH stock  (c1 V1 = c2 V2)
c_titrant=$(echo "scale=6; $C_STOCK * $V_STOCK_ML / $V_TITRANT_ML" | bc -l)
echo "titrant: ${C_STOCK} M * ${V_STOCK_ML} mL / ${V_TITRANT_ML} mL = ${c_titrant} M NaOH"

# 2. moles of titrant delivered at the equivalence point  (n = c V)
n_titrant=$(echo "scale=8; $c_titrant * $V_EQ_ML / 1000" | bc -l)
echo "n(NaOH) at equivalence = ${c_titrant} M * ${V_EQ_ML} mL = ${n_titrant} mol"

# 3. moles of analyte, from the 1:2 mole ratio
n_analyte=$(echo "scale=8; $n_titrant * $NU_ANALYTE / $NU_TITRANT" | bc -l)
echo "n(H2SO4) = n(NaOH) * ${NU_ANALYTE}/${NU_TITRANT} = ${n_analyte} mol"

# 4. analyte concentration  (c = n / V)
c_analyte=$(echo "scale=6; $n_analyte / ($V_ANALYTE_ML / 1000)" | bc -l)
echo "c(H2SO4) = ${n_analyte} mol / ${V_ANALYTE_ML} mL = ${c_analyte} M"

# cross-check against the one-line equivalence-point formula
c_check=$(echo "scale=6; $c_titrant * $V_EQ_ML * ($NU_ANALYTE / $NU_TITRANT) / $V_ANALYTE_ML" | bc -l)
echo "one-line formula c_T V_T (nuA/nuT) / V_A = ${c_check} M"
awk -v a="$c_analyte" -v b="$c_check" 'BEGIN{
  d = (a > b) ? a - b : b - a
  if (d < 1e-5) print "PASS: step-by-step and the closed formula agree on c(H2SO4)"
  else { print "FAIL: " a " vs " b; exit 1 }
}'
```

If the capstone prints `PASS`, the chain closed: dilution set the titrant
strength, `n = cV` turned volumes into amounts at both ends, and the balanced
equation's 1:2 ratio linked them — giving the acid concentration from nothing
but volumes and one known standard.

## Where to go next

- The full [`chemistry-foundations`](../SKILL.md) capsule.
- `arrhenius_acid_base` / `bronsted_lowry` and the acid–base band — an
  acid–base titration's *curve* (`acid_base_titration_curve`) and why the
  equivalence pH is not always 7.
- `ph_definition`, `weak_acid_equilibrium`, `henderson_hasselbalch` — where the
  `dilute_ideal_solution` assumption *does* enter, for weak-acid titrations and
  buffers (`indexes/assumption-index.md`).
- The sibling tutorials
  [`how-much-can-this-make.md`](how-much-can-this-make.md) (percent yield),
  [`reacting-gases-by-volume.md`](reacting-gases-by-volume.md) (gas
  stoichiometry),
  [`reaction-enthalpy-from-formation.md`](reaction-enthalpy-from-formation.md),
  and [`balancing-a-redox-equation.md`](balancing-a-redox-equation.md).
