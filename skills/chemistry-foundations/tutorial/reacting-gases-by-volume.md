# Reacting Gases by Volume

> Generated from the `chemistry-foundations` capsule (Release 0.1) with the
> `formula-tree-tutorial` skill. The chemistry, the prerequisite order, and
> every calculation come from that capsule.

For gases you rarely weigh anything. You measure a pressure, a volume, and a
temperature, and the ideal-gas law turns that into an amount — which the
balanced equation then converts to any other species. At fixed temperature and
pressure the shortcut is even cleaner: gas *volumes* react in the same ratio as
the coefficients. This tutorial walks the capsule's chain to that result:

`ideal_gas_law` → `molar_volume` → (`mole_fraction` → `daltons_law` →
`partial_pressure`) → `mole_ratio` → **`gas_stoichiometry`**.

## How to run this

Install [upmd](https://upmd.dev), then from the repository root run
`upmd skills/chemistry-foundations/tutorial/reacting-gases-by-volume.md` for the
interactive walk, or
`upmd --ci --all skills/chemistry-foundations/tutorial/reacting-gases-by-volume.md`
to run every calculation top to bottom.

Each section ends with a calculation you run yourself. Blocks depend on earlier
ones, so
`upmd --ci -b capstone skills/chemistry-foundations/tutorial/reacting-gases-by-volume.md`
runs the whole chain up to the capstone.

## What you need first

Algebra and ratios; SI units; that a `chemical_equation` can be balanced and its
`stoichiometric_coefficient`s (`ν`) read as a mole ratio. These are the
capsule's upstream nodes — assumed here, not rebuilt.

The dimensional checks track exponents on the `[M, L, T, Θ, N]` basis — mass,
length, time, temperature, and amount of substance (`N`, the mole). A consistent
relation prints `0 0 0 0 0` for (left side − right side).

One first-class assumption governs everything below: **`ideal_gas`** — point
molecules with no intermolecular forces, the low-pressure / high-temperature
limit. Near condensation, at high pressure, or in the critical region the
relations here stop being quantitative (van der Waals / virial corrections,
out of scope). In this capsule the assumption is prose inside the
`bridge_imported` `ideal_gas_law` entry; promoting it to its own graph node is a
Release 0.2 item.

---

## 0. Setup

The worked example is the combustion of hydrogen, `2H₂ + O₂ → 2H₂O(g)`. The
constants are the capsule's: the molar gas constant (`gas_constant` entry) and
the IUPAC molar volume at STP (`standard_conditions_stp` / `molar_volume`). The
scenario is a measured sample of hydrogen gas.

```bash [name:setup]
export R=8.314462618      # J mol^-1 K^-1, molar gas constant (capsule: gas_constant)
export VM_STP=22.711      # L/mol, ideal-gas molar volume at IUPAC STP (273.15 K, 1 bar)
export P_PA=1.00e5        # Pa, the sample pressure (= 1 bar)
export V_H2_L=5.00        # L, the measured volume of H2
export T_K=300            # K, the sample temperature (NOT degrees Celsius)
echo "sample: ${V_H2_L} L of H2 at ${P_PA} Pa, ${T_K} K ; reaction 2 H2 + O2 -> 2 H2O(g)"
```

## 1. The ideal gas law

`ideal_gas_law` (`P V = n R T`, imported from `physics-thermodynamics`) ties the
four state variables of a gas sample together. `P` is in pascals
(`M L⁻¹ T⁻²`), `V` in m³ (`L³`), `n` in moles (`N`), `T` in **kelvin** (`Θ`),
and `R` carries `M L² T⁻² Θ⁻¹ N⁻¹` so the whole thing is dimensionally an
energy on each side. Two failure modes dominate: using °C instead of K, and
using an `R` whose units do not match `P` and `V`. The check is dimensional.

Formula: **`P V = n R T`**

```bash [name:chk_ideal_gas_law, deps:setup]
bc -l <<'EOF'
/* exponents (m, l, t, th, n) */
pm=1; pl=-1; pt=-2; pth=0; pn=0     /* P -> M L^-1 T^-2       */
vm=0; vl=3; vt=0; vth=0; vn=0       /* V -> L^3              */
nm=0; nl=0; nt=0; nth=0; nn=1       /* n -> N               */
rm=1; rl=2; rt=-2; rth=-1; rn=-1    /* R -> M L^2 T^-2 Th^-1 N^-1 */
tm=0; tl=0; tt=0; tth=1; tn=0       /* T -> Theta           */
print (pm+vm)-(nm+rm+tm)," ",(pl+vl)-(nl+rl+tl)," ",(pt+vt)-(nt+rt+tt)," ",(pth+vth)-(nth+rth+tth)," ",(pn+vn)-(nn+rn+tn)," (want 0 0 0 0 0)\n"
EOF
```

```bash [name:try_ideal_gas_law, deps:chk_ideal_gas_law]
# solve P V = n R T for n at the sample conditions; change T_K or P_PA and re-run
V_M3=$(echo "scale=8; $V_H2_L / 1000" | bc -l)      # L -> m^3
n=$(echo "scale=6; ($P_PA * $V_M3) / ($R * $T_K)" | bc -l)
echo "n(H2) = P V / (R T) = ($P_PA * $V_M3) / ($R * $T_K) = $n mol"
```

Both sides carry energy dimensions; `n = PV/RT` gives the amount of gas in the
sample from the three things you can actually measure.

## 2. Molar volume

Set `n = 1` and the law gives the volume one mole of any ideal gas occupies:
`molar_volume`, `V_m = R T / P`, with dimension `L³ N⁻¹`. It is **not** a
constant — it scales with `T/P`. At the capsule's IUPAC STP (`T = 273.15 K`,
`P = 1 bar`) it is `22.711 L/mol`; at 298.15 K and 1 bar it is `24.79 L/mol`.
The check confirms the dimension, then the STP number.

Formula: **`V_m = R T / P`**

```bash [name:chk_molar_volume, deps:chk_ideal_gas_law]
bc -l <<'EOF'
/* [R T / P] must be L^3 N^-1 -> (0, 3, 0, 0, -1) */
rm=1; rl=2; rt=-2; rth=-1; rn=-1
tm=0; tl=0; tt=0; tth=1; tn=0
pm=1; pl=-1; pt=-2; pth=0; pn=0
print (rm+tm-pm)-0," ",(rl+tl-pl)-3," ",(rt+tt-pt)-0," ",(rth+tth-pth)-0," ",(rn+tn-pn)-(-1)," (want 0 0 0 0 0)\n"
EOF
# numeric: V_m at IUPAC STP, in litres per mole
awk -v r="$R" 'BEGIN{
  T = 273.15; P = 1.0e5
  vm_m3 = r * T / P            # m^3/mol
  printf "V_m(STP) = %.3f L/mol   (capsule: 22.711)\n", vm_m3 * 1000
}'
```

`R T / P` lands on volume-per-amount, and at STP a mole of ideal gas fills about
22.7 litres.

## 3. Partial pressures

In a gas mixture each component `i` has a `mole_fraction` `xᵢ = nᵢ / n_total`
(dimensionless, `Σ xᵢ = 1`). `daltons_law` says the pressures add:
`P_total = Σᵢ Pᵢ`, where `Pᵢ` is the pressure that component would exert alone.
`partial_pressure` combines the two: `Pᵢ = xᵢ · P_total`. The practical use is
collecting a gas over water — the measured pressure is the gas *plus* water
vapour, so you subtract the vapour pressure to get the dry-gas partial pressure.
Two dimensional checks, then the dry-air mole fractions.

Formula: **`P_total = Σᵢ Pᵢ`**  and  **`Pᵢ = xᵢ · P_total`**

```bash [name:chk_partial_pressure, deps:chk_ideal_gas_law]
bc -l <<'EOF'
pm=1; pl=-1; pt=-2; pth=0; pn=0     /* any pressure -> M L^-1 T^-2 */
/* P_total = sum P_i : every term is a pressure */
print "P_total = sum P_i : ", pm-pm," ",pl-pl," ",pt-pt," ",pth-pth," ",pn-pn," (want 0 0 0 0 0)\n"
/* P_i = x_i P_total : x_i is dimensionless (0,0,0,0,0) */
xm=0; xl=0; xt=0; xth=0; xn=0
print "P_i = x_i P_tot  : ", pm-(xm+pm)," ",pl-(xl+pl)," ",pt-(xt+pt)," ",pth-(xth+pth)," ",pn-(xn+pn)," (want 0 0 0 0 0)\n"
EOF
# capsule special case: dry air mole fractions
awk 'BEGIN{
  xN2 = 0.78; xO2 = 0.21; xAr_etc = 1 - xN2 - xO2
  printf "dry air:  x(N2) = %.2f  x(O2) = %.2f  x(rest) = %.2f\n", xN2, xO2, xAr_etc
  if (xN2 + xO2 + xAr_etc == 1) print "PASS: mole fractions sum to 1"
  else { print "FAIL"; exit 1 }
}'
```

Partial pressures add to the total, and scaling the total by a dimensionless
mole fraction keeps pressure dimensions — so `Pᵢ = xᵢ P_total` is well-formed.

## 4. Balancing and the mole ratio

The balanced equation is the recipe. `conservation_of_mass` fixes the
coefficients (every element's atoms match across the arrow); the `mole_ratio`
`n_B = n_A · (ν_B / ν_A)` then converts any species' amount to any other's. The
check inventories the atoms of the scenario reaction and reads off its ratio.

Formula: **`n_B = n_A · (ν_B / ν_A)`**

```bash [name:chk_mole_ratio, deps:chk_ideal_gas_law]
awk 'BEGIN{
  # 2 H2 + 1 O2  ->  2 H2O(g)
  hL = 2*2;  hR = 2*2
  oL = 1*2;  oR = 2*1
  printf "atoms:  H %d = %d   O %d = %d\n", hL, hR, oL, oR
  # mole ratios from nu(H2)=2, nu(O2)=1, nu(H2O)=2
  nH2 = 1.0
  nO2  = nH2 * 1 / 2
  nH2O = nH2 * 2 / 2
  printf "per 1 mol H2:  %.2f mol O2 consumed,  %.2f mol H2O formed\n", nO2, nH2O
  if (hL==hR && oL==oR && nO2==0.5 && nH2O==1.0) print "PASS: balanced 2:1:2, ratio reads off the coefficients"
  else { print "FAIL"; exit 1 }
}'
```

Hydrogen and oxygen balance at `2, 1, 2`, so one mole of H₂ consumes half a mole
of O₂ and makes one mole of water vapour.

## 5. Gas stoichiometry

`gas_stoichiometry` is just `PV = nRT` plus the mole ratio: convert a measured
`P, V, T` to moles, apply the ratio, convert back if you need a volume. **At
fixed `T` and `P`** there is a shortcut — Avogadro's principle makes amount
proportional to volume, so gas *volumes* react in the coefficient ratio directly
(the capsule's Gay-Lussac special case). It fails the moment `T` or `P` differs
between the measurements, or for a non-gaseous species.

Rule: **at fixed `T, P`:  `V_B = V_A · (ν_B / ν_A)`**  (gas species only)

```bash [name:chk_gas_stoichiometry, deps:"chk_mole_ratio | chk_ideal_gas_law"]
awk 'BEGIN{
  # capsule special case: 2 vol H2 + 1 vol O2 -> 2 vol H2O(g), same T and P
  vH2 = 2
  vO2  = vH2 * 1 / 2
  vH2O = vH2 * 2 / 2
  printf "%g vol H2  +  %g vol O2  ->  %g vol H2O(g)   (fixed T, P)\n", vH2, vO2, vH2O
  if (vO2 == 1 && vH2O == 2) print "PASS: volumes react as 2:1:2, the coefficient ratio"
  else { print "FAIL"; exit 1 }
}'
```

At one temperature and pressure the volume ratio *is* the mole ratio — no
conversion to moles needed.

---

## Capstone: from a measured volume of H₂ to a volume of steam

You have the whole chain. Take the `5.00 L` of H₂ from Setup: find the volume of
O₂ it needs at the same conditions, the moles of H₂ present, and the volume the
water vapour produced would occupy at STP.

```bash [name:capstone, deps:"chk_gas_stoichiometry | chk_molar_volume | chk_partial_pressure"]
# 1. O2 required and H2O(g) produced, at the SAME T and P (volume ratio)
vO2=$(echo "scale=4; $V_H2_L * 1 / 2" | bc -l)
vH2O=$(echo "scale=4; $V_H2_L * 2 / 2" | bc -l)
echo "at ${T_K} K, ${P_PA} Pa:  ${V_H2_L} L H2  needs ${vO2} L O2,  makes ${vH2O} L H2O(g)"

# 2. moles of H2 in the sample, from P V = n R T
V_M3=$(echo "scale=10; $V_H2_L / 1000" | bc -l)
nH2=$(echo "scale=6; ($P_PA * $V_M3) / ($R * $T_K)" | bc -l)
echo "n(H2) = P V / (R T) = $nH2 mol"

# 3. n(H2O) from the 2:2 mole ratio, then its volume at STP via the molar volume
nH2O=$(echo "scale=6; $nH2 * 2 / 2" | bc -l)
vH2O_stp=$(echo "scale=4; $nH2O * $VM_STP" | bc -l)
echo "n(H2O) = $nH2O mol  ->  at STP that is $nH2O * $VM_STP = $vH2O_stp L"

# checks: the same-conditions volumes must match the coefficient ratio,
# and the STP volume must be smaller than the 300 K volume (gas contracts on cooling)
awk -v vo2="$vO2" -v vh2o="$vH2O" -v vsrc="$V_H2_L" -v vstp="$vH2O_stp" 'BEGIN{
  ratio_ok = (vo2 == vsrc/2 && vh2o == vsrc)
  cool_ok  = (vstp < vsrc)
  if (ratio_ok && cool_ok)
    print "PASS: volumes follow 2:1:2 at fixed T,P; the STP volume is smaller (cooled from 300 K to 273 K)"
  else { print "FAIL"; exit 1 }
}'
```

If the capstone prints `PASS`, the chain held: the ideal-gas law turned a
pressure–volume–temperature reading into moles, the balanced equation set the
ratio, and at fixed conditions the gas volumes reacted straight in the
coefficient ratio — no balance, no molar masses.

## Where to go next

- The full [`chemistry-foundations`](../SKILL.md) capsule. Real-gas equations of
  state (van der Waals, virial) are named but not developed — `scope.md`.
- `kp_kc_relation` (`K_p = K_c (RT/P°)^{Δn}`) — where partial pressures feed a
  gas-phase equilibrium constant; and `heterogeneous_equilibrium`.
- `daltons_law`'s gas-over-water correction is used quantitatively in the
  equilibrium and acid–base bands (`indexes/topic-index.md`).
- The sibling tutorials
  [`how-much-can-this-make.md`](how-much-can-this-make.md) (percent yield),
  [`reaction-enthalpy-from-formation.md`](reaction-enthalpy-from-formation.md)
  (reaction enthalpy), and
  [`balancing-a-redox-equation.md`](balancing-a-redox-equation.md).
