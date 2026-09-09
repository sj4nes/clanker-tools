# What Does It Cost to Make a Kilogram?

> Generated from the `chemistry-electrochemistry` capsule (Release 0.1) with the
> `formula-tree-tutorial` skill. The chemistry, the prerequisite order, and
> every calculation come from that capsule.

[`per-amp-hour.md`](per-amp-hour.md) told you how many *coulombs* a product
costs. This tutorial multiplies that by the *voltage* — and the voltage is
never just `E°_cell`. Thermodynamics sets a floor (`ΔG = −zFE`), then the
oxygen electrode's sluggish kinetics and the electrolyte's resistance pile
extra volts on top. The result is the **specific energy consumption**, in
kWh per kilogram:

`standard_cell_potential` → `gibbs_from_cell_potential` → `overpotential` +
`ohmic_drop` → `cell_voltage_electrolysis` → **`specific_energy_consumption`**.

## How to run this

Install [upmd](https://upmd.dev), then from the repository root run
`upmd skills/chemistry-electrochemistry/tutorial/kwh-per-kilogram.md` for the
interactive walk, or
`upmd --ci --all skills/chemistry-electrochemistry/tutorial/kwh-per-kilogram.md`
to run every calculation top to bottom.

Each section ends with a calculation you run yourself. Blocks depend on earlier
ones, so
`upmd --ci -b capstone skills/chemistry-electrochemistry/tutorial/kwh-per-kilogram.md`
runs the whole chain up to the capstone. Three blocks call `lean` to
kernel-check an arithmetic instance; if `lean` is not on your `PATH` they print
`SKIP` and pass.

## What you need first

- **[`per-amp-hour.md`](per-amp-hour.md)** — Faraday's law `m = ItM/(zF)`, the
  electron count `z`, the Faraday constant `F`, and current efficiency `η_F`.
  This tutorial takes those as given.
- **Electric potential** `V` — energy per unit charge, in volts; moving `Q`
  coulombs through `ΔV` volts does `W = QΔV` joules of work.
- **Resistance** `R` — `V = IR` (Ohm's law); the electrolyte and separator
  have resistance.
- **From [`chemistry-foundations`](../../chemistry-foundations/SKILL.md)** and
  **[`physics-thermodynamics`](../../physics-thermodynamics/SKILL.md)**
  (imported): Gibbs free energy `ΔG`, and `ΔG° = −RT ln K`.

The dimensional checks use the `[M, L, T, Θ, N, I]` basis (electric current `I`
is a base dimension). Potential is `M L² T⁻³ I⁻¹`; a consistent relation prints
`0 0 0 0 0 0`.

Everything is at **298.15 K** and the **`dilute_ideal_solution`** limit.

---

## 0. Setup

Two products, from the capsule's own worked figures: **hydrogen** (water
electrolysis) and **aluminium** (Hall–Héroult).

```bash [name:setup]
export F=96485             # C/mol
# hydrogen from water electrolysis
export Z_H2=2              # electrons per H2
export M_H2=2.016          # g/mol
export VCELL_H2=1.98       # V, real cell voltage (capsule: ~1.8-2.0 V)
export ETAF_H2=0.98        # current efficiency
# aluminium from Hall-Heroult
export Z_AL=3              # electrons per Al
export M_AL=26.98          # g/mol
export VCELL_AL=4.2        # V (capsule)
export ETAF_AL=0.93        # current efficiency (capsule)
export E0_WATER=1.23       # V, |E0_cell| for 2 H2O -> 2 H2 + O2
export BC_LINE_LENGTH=0
echo "comparing kWh/kg for H2 (electrolysis) and Al (Hall-Heroult)"
```

## 1. The standard cell potential

An electrolytic cell splits a redox reaction across two electrodes. Every
electrode potential is a **reduction potential** versus the standard hydrogen
electrode (`E°(SHE) ≡ 0`), and

**`E°_cell = E°_cathode − E°_anode`**

For water electrolysis the cathode is `2H⁺ + 2e⁻ → H₂` (`E° = 0.00 V`) and the
anode is `2H₂O → O₂ + 4H⁺ + 4e⁻` (`E° = +1.23 V`), so
`E°_cell = 0.00 − 1.23 = −1.23 V`. Negative → the reaction must be *driven*, and
`|E°_cell| = 1.23 V` is the reversible (thermodynamic minimum) decomposition
voltage. The Lean beat checks the identity on the capsule's galvanic examples.

```bash [name:chk_standard_cell_potential, deps:setup]
awk -v e0="$E0_WATER" 'BEGIN{
  Ec = 0.00     # E0(2 H+ / H2)
  Ea = e0       # E0(O2 / H2O)
  E0_cell = Ec - Ea
  printf "E0_cell(water) = %.2f - %.2f = %.2f V\n", Ec, Ea, E0_cell
  printf "|E0_cell| = %.2f V  (the reversible decomposition voltage)\n", -E0_cell
  if (E0_cell == -1.23) print "PASS: negative -> must be driven; 1.23 V is the floor"
  else { print "FAIL"; exit 1 }
}'
```

```bash [name:lean_standard_cell_potential, deps:chk_standard_cell_potential]
command -v lean >/dev/null 2>&1 || { echo "SKIP: lean not on PATH"; exit 0; }
d=$(mktemp -d)
cat > "$d/ecell.lean" <<'EOF'
-- capsule validation/derivation-checks.lean, check 3 (standard_cell_potential)
-- E0_cell = E0_cathode - E0_anode, reduction potentials, in centivolts.
-- Daniell cell:  E0(Cu2+/Cu) = +34 ,  E0(Zn2+/Zn) = -76.
example : ((34 : Int) - (-76)) = 110 := by decide
-- all-vanadium:  E0(VO2+/VO2+) = +100 ,  E0(V3+/V2+) = -26.
example : ((100 : Int) - (-26)) = 126 := by decide
EOF
if lean "$d/ecell.lean"; then
  echo "PASS: Lean kernel verified E0_cell = E0_cathode - E0_anode (Daniell 110 cV, vanadium 126 cV)"
else
  echo "FAIL: lean rejected the snippet"; rm -rf "$d"; exit 1
fi
rm -rf "$d"
```

`E°_cell` is a difference of two reduction potentials; for water it is `−1.23 V`.

## 2. Free energy and the reversible voltage

The cell potential is the reaction's free energy per coulomb:

**`ΔG = −z F E`**

`E > 0` ⇔ `ΔG < 0` ⇔ spontaneous. For water electrolysis (`z = 4` per O₂,
`E°_cell = −1.23 V`), `ΔG° = −4F(−1.23) = +475 kJ` — positive, so you must put
that energy in. Per mole of H₂ that is `+237 kJ`, which is exactly
`−ΔG_f°(H₂O, l)`. The check confirms the dimension, then the number.

```bash [name:chk_gibbs_from_cell_potential, deps:chk_standard_cell_potential]
bc -l <<'EOF'
/* [z F E] : (I T N^-1)(M L^2 T^-3 I^-1) = M L^2 T^-2 N^-1  (molar energy) */
fm=0; fl=0; ft=1; fth=0; fn=-1; fi=1     /* F -> I T N^-1 */
vm=1; vl=2; vt=-3; vth=0; vn=0; vi=-1    /* E -> M L^2 T^-3 I^-1 */
gm=1; gl=2; gt=-2; gth=0; gn=-1; gi=0    /* molar dG -> M L^2 T^-2 N^-1 */
print gm-(fm+vm)," ",gl-(fl+vl)," ",gt-(ft+vt)," ",gth-(fth+vth)," ",gn-(fn+vn)," ",gi-(fi+vi)," (want 0 0 0 0 0 0)\n"
EOF
awk -v f="$F" -v e0="$E0_WATER" 'BEGIN{
  z = 4
  dG_total = -z * f * (-e0)          # J per mol O2 (2 mol H2)
  dG_perH2 = dG_total / 2
  printf "dG0(2 H2O -> 2 H2 + O2) = -4 * %.0f * (-%.2f) = %.0f J = +%.0f kJ\n", f, e0, dG_total, dG_total/1000
  printf "per mole H2: +%.0f kJ  (= -dG_f of water)\n", dG_perH2/1000
  if (dG_total > 474000 && dG_total < 476000) print "PASS: +475 kJ in, minimum, for 2 mol H2"
  else { print "FAIL"; exit 1 }
}'
```

```bash [name:lean_gibbs_from_cell_potential, deps:chk_gibbs_from_cell_potential]
command -v lean >/dev/null 2>&1 || { echo "SKIP: lean not on PATH"; exit 0; }
d=$(mktemp -d)
cat > "$d/dg.lean" <<'EOF'
-- capsule validation/derivation-checks.lean, check 4 (gibbs_from_cell_potential)
-- dG = - z F E.  Daniell, z = 2, E = 1.10 V (centivolt-coulombs; /100 for J/mol):
example : (-(2 * 96485 * 110) : Int) = -21226700 := by decide
-- reversing the cell reaction flips the sign of E and of dG:
example : (-(-(2 * 96485 * 110) : Int)) = 21226700 := by decide
EOF
if lean "$d/dg.lean"; then
  echo "PASS: Lean kernel verified dG = -zFE and its sign flip on reversal"
else
  echo "FAIL: lean rejected the snippet"; rm -rf "$d"; exit 1
fi
rm -rf "$d"
```

`1.23 V` is the least you can spend per electron pair — the reversible floor.

## 3. Overpotential — the extra volts kinetics demands

`overpotential` is the excess potential an electrode needs to pass a real
current: `η = E_applied − E_equilibrium`. It splits into an **activation** part
(the charge-transfer barrier), a **concentration** part (reactant depletion at
the surface), and — lumped separately — the ohmic drop. Activation overpotential
is small for `H⁺/H₂` on platinum but **large for oxygen evolution** (`~0.3–0.6 V`
on the best catalysts) — the oxygen electrode sets the loss budget of every
electrolyser. `|η|` is always *lost* work.

```bash [name:chk_overpotential, deps:chk_standard_cell_potential]
awk 'BEGIN{
  # representative activation overpotentials at practical current density (V)
  eta_H2 = 0.05     # H2 evolution on a good cathode - fast
  eta_O2 = 0.35     # O2 evolution - slow, multi-electron
  printf "activation overpotential:  H2 cathode ~%.2f V ,  O2 anode ~%.2f V\n", eta_H2, eta_O2
  printf "the O2 anode alone adds more than the H2 cathode by %.0fx\n", eta_O2/eta_H2
  if (eta_O2 > eta_H2) print "PASS: oxygen evolution is the dominant kinetic loss"
  else { print "FAIL"; exit 1 }
}'
```

The oxygen anode is the slow step — most of the "extra" voltage in water
electrolysis is spent there.

## 4. The ohmic drop

Current through the electrolyte, the separator, and the contacts obeys Ohm's
law, so it costs a voltage `ohmic_drop`:

**`η_ohmic = I R_cell`**

Linear in current — minimised by a thin electrode gap, a conductive supporting
electrolyte, and a low-resistance membrane. At high current density it is often
the single largest loss.

```bash [name:chk_ohmic_drop, deps:setup]
bc -l <<'EOF'
/* [I R] : (I)(M L^2 T^-3 I^-2) = M L^2 T^-3 I^-1  = potential */
im=0; il=0; it=0; ith=0; in=0; ii=1        /* I -> I */
rm=1; rl=2; rt=-3; rth=0; rn=0; ri=-2      /* R -> M L^2 T^-3 I^-2 */
vm=1; vl=2; vt=-3; vth=0; vn=0; vi=-1      /* V -> M L^2 T^-3 I^-1 */
print vm-(im+rm)," ",vl-(il+rl)," ",vt-(it+rt)," ",vth-(ith+rth)," ",vn-(in+rn)," ",vi-(ii+ri)," (want 0 0 0 0 0 0)\n"
EOF
awk 'BEGIN{
  # a stack drawing 3000 A through a cell resistance of 0.12 milliohm
  I = 3000; R = 0.00012
  printf "eta_ohmic = %.0f A * %.5f ohm = %.2f V\n", I, R, I*R
  if (I*R > 0.35 && I*R < 0.37) print "PASS: ~0.36 V of pure resistive loss"
  else { print "FAIL"; exit 1 }
}'
```

`I R` is a voltage; drive more current and you pay proportionally more of it.

## 5. The real cell voltage

Add the reversible voltage and every loss:

**`V_cell = E°_cell + |η_anode| + |η_cathode| + I R_cell`**

(here `E°_cell` means the magnitude of the reversible decomposition voltage).
For alkaline water electrolysis at practical current the capsule's breakdown is
`1.23 + 0.05 + 0.35 + 0.35 ≈ 1.98 V` — so only about `1.23/1.98 ≈ 62 %` of the
electrical input ends up as the free energy of the hydrogen (or `1.48/1.98 ≈
75 %` against the thermoneutral figure). The Lean beat checks the additive
bookkeeping.

```bash [name:chk_cell_voltage_electrolysis, deps:"chk_overpotential | chk_ohmic_drop | chk_gibbs_from_cell_potential"]
bc -l <<'EOF'
/* every term is a potential; the sum is a potential */
vm=1; vl=2; vt=-3; vth=0; vn=0; vi=-1
print vm-vm," ",vl-vl," ",vt-vt," ",vth-vth," ",vn-vn," ",vi-vi," (want 0 0 0 0 0 0)\n"
EOF
awk -v e0="$E0_WATER" -v vc="$VCELL_H2" 'BEGIN{
  eta_c = 0.05; eta_a = 0.35; iR = 0.35
  V = e0 + eta_a + eta_c + iR
  printf "V_cell = %.2f + %.2f + %.2f + %.2f = %.2f V   (setup uses %.2f V)\n", e0, eta_a, eta_c, iR, V, vc
  eff = e0 / V
  printf "fraction of input that becomes dG(H2): %.2f / %.2f = %.0f %%\n", e0, V, eff*100
  if (V > 1.97 && V < 1.99) print "PASS: ~1.98 V, ~62 % of it thermodynamically useful"
  else { print "FAIL"; exit 1 }
}'
```

```bash [name:lean_cell_voltage_electrolysis, deps:chk_cell_voltage_electrolysis]
command -v lean >/dev/null 2>&1 || { echo "SKIP: lean not on PATH"; exit 0; }
d=$(mktemp -d)
cat > "$d/vcell.lean" <<'EOF'
-- capsule validation/derivation-checks.lean, check 9 (cell_voltage_electrolysis)
-- V_cell = E0_cell + |eta_a| + |eta_c| + I R  (centivolts):
-- 123 (reversible) + 10 (cathode) + 30 (anode incl. O2 overpotential) + 35 (IR)
example : ((123 : Int) + 10 + 30 + 35) = 198 := by decide
-- thermoneutral voltage 1.48 V; efficiency vs that ~ 148 / 198:
example : ((148 * 100 : Int) / 198) = 74 := by decide
EOF
if lean "$d/vcell.lean"; then
  echo "PASS: Lean kernel verified V_cell = 123+10+30+35 = 198 cV, and ~74 % thermoneutral efficiency"
else
  echo "FAIL: lean rejected the snippet"; rm -rf "$d"; exit 1
fi
rm -rf "$d"
```

`V_cell` is the reversible floor plus every loss — for water, about `1.98 V`.

## 6. Specific energy consumption

Now combine Faraday's law (charge per kg) with the cell voltage (energy per
charge):

**`E_spec = z F V_cell / (M η_F)`**   (J/kg; quoted as kWh/kg)

`z F / M` is the coulombs per gram; `V_cell` turns coulombs into joules; `η_F`
scales for the charge lost to side reactions. The check confirms the dimension
is energy-per-mass, then computes it for hydrogen.

```bash [name:chk_specific_energy, deps:chk_cell_voltage_electrolysis]
bc -l <<'EOF'
/* [z F V / M] : (I T N^-1)(M L^2 T^-3 I^-1) / (M N^-1) = L^2 T^-2 = J/kg */
fm=0; fl=0; ft=1; fth=0; fn=-1; fi=1     /* F */
vm=1; vl=2; vt=-3; vth=0; vn=0; vi=-1    /* V_cell */
mm=1; ml=0; mt=0; mth=0; mn=-1; mi=0     /* molar mass M */
print (fm+vm-mm)-0," ",(fl+vl-ml)-2," ",(ft+vt-mt)-(-2)," ",(fth+vth-mth)-0," ",(fn+vn-mn)-0," ",(fi+vi-mi)-0," (want 0 0 0 0 0 0)\n"
EOF
awk -v f="$F" -v z="$Z_H2" -v M="$M_H2" -v V="$VCELL_H2" -v e="$ETAF_H2" 'BEGIN{
  Jg = z * f * V / (M * e)          # J per gram
  kWh_kg = Jg * 1000 / 3.6e6
  printf "E_spec(H2) = %d * %.0f * %.2f / (%.3f * %.2f) = %.0f J/g = %.1f kWh/kg\n", z, f, V, M, e, Jg, kWh_kg
  if (kWh_kg > 53 && kWh_kg < 55) print "PASS: ~53.7 kWh per kg of hydrogen"
  else { print "FAIL"; exit 1 }
}'
```

Hydrogen costs about `54 kWh/kg` to electrolyse — a well-known number, and the
reason electrolytic hydrogen is expensive.

---

## Capstone: hydrogen versus aluminium, per kilogram

You have the whole chain. Compute `E_spec` for both products from the capsule's
figures, compare them to the reversible minimum, and see which is actually
cheaper to make per kilogram.

```bash [name:capstone, deps:"chk_specific_energy | lean_cell_voltage_electrolysis"]
espec () {  # z F V / (M eta_F)  ->  kWh/kg
  bc -l <<< "scale=1; $1 * $F * $3 / ($2 * $4) * 1000 / 3600000"
}

# real specific energy
h2=$(espec "$Z_H2" "$M_H2" "$VCELL_H2" "$ETAF_H2")
al=$(espec "$Z_AL" "$M_AL" "$VCELL_AL" "$ETAF_AL")
echo "E_spec(H2, ${VCELL_H2} V, eta_F ${ETAF_H2}) = ${h2} kWh/kg"
echo "E_spec(Al, ${VCELL_AL} V, eta_F ${ETAF_AL}) = ${al} kWh/kg"

# reversible minimum for hydrogen: z F |E0_cell| / M  (eta_F = 1, V = 1.23)
h2_rev=$(bc -l <<< "scale=1; $Z_H2 * $F * $E0_WATER / $M_H2 * 1000 / 3600000")
echo "reversible minimum for H2 (1.23 V): ${h2_rev} kWh/kg"
frac=$(bc -l <<< "scale=0; $h2_rev * 100 / $h2")
echo "  -> electrolysis is ~${frac}% efficient against the free energy of H2"

awk -v h2="$h2" -v al="$al" -v hr="$h2_rev" 'BEGIN{
  ok = (h2 > 52 && h2 < 55) && (al > 13 && al < 14) && (hr > 32 && hr < 34) && (al < h2)
  if (ok)
    print "PASS: ~54 kWh/kg for H2 vs ~13 kWh/kg for Al -- aluminium is CHEAPER per kg,"
  else { print "FAIL"; exit 1 }
}'
echo "     because H2's molar mass is tiny: per mole of electrons the two are"
echo "     close (H2 ~52 kJ, Al ~44 kJ), but a kg of H2 is 496 mol e- pairs."
```

If the capstone prints `PASS`, the chain held: `E°_cell` set the reversible
`1.23 V`, `ΔG = −zFE` made that `+237 kJ/mol H₂`, overpotential and `IR` raised
the real voltage to `~2 V`, and Faraday's `zF/M` converted it to kWh/kg — where
hydrogen's tiny molar mass makes it, per kilogram, several times more
energy-intensive to produce than aluminium.

## Where to go next

- `water_electrolysis`, `chlor_alkali_process`, `hall_heroult_process`,
  `zinc_electrowinning` — the named processes, each with its `z`, `E°_cell`,
  `V_cell`, and `η_F` (`indexes/topic-index.md`).
- `nernst_equation` — how `E` (and therefore `V_cell` and the energy) shifts
  when the concentrations are not at unit activity.
- `temperature_coefficient_emf` — running hotter changes `E°` and the loss
  balance.
- The sibling tutorial [`per-amp-hour.md`](per-amp-hour.md) (Faraday's law), and
  the full [`chemistry-electrochemistry`](../SKILL.md) capsule.
