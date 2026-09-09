# How Much Do You Make Per Amp-Hour?

> Generated from the `chemistry-electrochemistry` capsule (Release 0.1) with the
> `formula-tree-tutorial` skill. The chemistry, the prerequisite order, and
> every calculation come from that capsule.

Electrolysis is a conversion between two ledgers: **coulombs** through the wire
and **moles** of product at the electrode. The Faraday constant is the exchange
rate, the balanced half-reaction sets how many electrons each formula unit
costs, and Faraday's law turns a current and a clock into a mass. This tutorial
walks the capsule's chain to that law and to what it tells you about making
hydrogen:

`faraday_constant` → `charge_from_current` → `electrons_per_formula_unit` →
`charge_mole_electron_bridge` → **`faradays_law_electrolysis`** →
`moles_of_product_electrolysis` / `gas_volume_electrolysis` →
`current_efficiency`.

## How to run this

Install [upmd](https://upmd.dev), then from the repository root run
`upmd skills/chemistry-electrochemistry/tutorial/per-amp-hour.md` for the
interactive walk, or
`upmd --ci --all skills/chemistry-electrochemistry/tutorial/per-amp-hour.md`
to run every calculation top to bottom.

Each section ends with a calculation you run yourself. Blocks depend on earlier
ones, so
`upmd --ci -b capstone skills/chemistry-electrochemistry/tutorial/per-amp-hour.md`
runs the whole chain up to the capstone. Two blocks call `lean` to
kernel-check an arithmetic instance; if `lean` is not on your `PATH` they print
`SKIP` and pass.

## What you need first

**From electricity** (the capsule treats these as a root set; a future
`physics-circuits` capsule will own them):

- **Electric charge** `Q` — conserved, measured in coulombs (C), quantised in
  units of the elementary charge `e = 1.602×10⁻¹⁹ C`.
- **Electric current** `I` — the rate of charge flow, `I = dQ/dt`, in amperes
  (A = C/s); at constant current `Q = I t`.

**From [`chemistry-foundations`](../../chemistry-foundations/SKILL.md)** (imported):
the mole and the Avogadro constant, molar mass `M = m/n`, balancing a
half-reaction, and the mole ratio.

The dimensional checks track exponents on the `[M, L, T, Θ, N, I]` basis —
electric current `I` is a base dimension here. Charge is `I T`; a consistent
relation prints `0 0 0 0 0 0` for (left side − right side).

---

## 0. Setup

The worked example is a hydrogen electrolyser. The constants are the capsule's:
the Faraday constant, the STP molar volume (imported), and the molar mass of
`H₂`.

```bash [name:setup]
export F=96485            # C/mol, the Faraday constant (= N_A e)
export VM_STP=22.711      # L/mol, ideal-gas molar volume at STP (imported)
export M_H2=2.016         # g/mol
export I_A=100            # A, the electrolyser current
export ETA_F=0.98         # current efficiency for H2 at the cathode
export BC_LINE_LENGTH=0   # stop bc wrapping long numeric output
echo "electrolyser at ${I_A} A ; making H2 (2 H2O + 2e- -> H2 + 2 OH-) ; current efficiency ${ETA_F}"
```

## 1. The Faraday constant

`faraday_constant` is the charge of **one mole of electrons**:
`F = N_A e = 96485 C/mol`. It is the single number that converts between the
coulombs your power supply pushes and the moles of electrons the electrode
reaction consumes. Its dimension is `I T N⁻¹` (charge per amount).

Formula: **`F = N_A e`**

```bash [name:chk_faraday_constant, deps:setup]
bc -l <<'EOF'
/* exponents (m, l, t, th, n, i) */
nam=0; nal=0; nat=0;  nath=0; nan=-1; nai=0    /* N_A -> N^-1 */
em=0;  el=0;  et=1;   eth=0;  en=0;   ei=1     /* e (a charge) -> I T */
fm=0;  fl=0;  ft=1;   fth=0;  fn=-1;  fi=1     /* F -> I T N^-1 */
print fm-(nam+em)," ",fl-(nal+el)," ",ft-(nat+et)," ",fth-(nath+eth)," ",fn-(nan+en)," ",fi-(nai+ei)," (want 0 0 0 0 0 0)\n"
EOF
# 1 F deposits 1 mol of a z = 1 species (108 g Ag); 1/2 mol of a z = 2 species (32 g Cu)
awk -v f="$F" 'BEGIN{
  n_z1 = f / (1 * f)     # mol per faraday, z = 1
  n_z2 = f / (2 * f)     # mol per faraday, z = 2
  printf "1 F -> %.3f mol (z=1) ,  %.3f mol (z=2)\n", n_z1, n_z2
  if (n_z1 == 1 && n_z2 == 0.5) print "PASS: one faraday = one mole of electrons"
  else { print "FAIL"; exit 1 }
}'
```

Charge per mole of electrons — the exchange rate for every calculation below.

## 2. Charge from a current

`charge_from_current`: at constant current, `Q = I t` (in general `Q = ∫ I dt`).
Amperes times seconds are coulombs. This is how you turn "the electrolyser ran
at 100 A for an hour" into a number of coulombs.

Formula: **`Q = I t`**

```bash [name:chk_charge_from_current, deps:setup]
bc -l <<'EOF'
im=0; il=0; it=0;  ith=0; in=0; ii=1     /* current I -> I */
/* time exponent is (0,0,1,0,0,0) */
qm=0; ql=0; qt=1;  qth=0; qn=0; qi=1     /* charge Q -> I T */
print qm-(im+0)," ",ql-(il+0)," ",qt-(it+1)," ",qth-(ith+0)," ",qn-(in+0)," ",qi-(ii+0)," (want 0 0 0 0 0 0)\n"
EOF
# capsule special case: 2.00 A for 1.00 h
awk -v f="$F" 'BEGIN{
  Q = 2.00 * 3600
  printf "2.00 A * 3600 s = %.0f C = %.4f F\n", Q, Q/f
  if (Q == 7200) print "PASS"; else { print "FAIL"; exit 1 }
}'
```

`I t` is a charge; `7200 C` is only about `0.075` of a mole of electrons.

## 3. Electrons per formula unit

`electrons_per_formula_unit` is `z`: the number of electrons in the **balanced**
half-reaction, per formula unit of the species you care about. Get it wrong and
every downstream number is wrong by that factor. The check reads `z` off three
half-reactions from the capsule.

Formula: **`z` = electrons in the balanced half-reaction**

```bash [name:chk_electrons_per_formula_unit, deps:setup]
awk 'BEGIN{
  # Cu2+  + 2 e-        -> Cu           : z = 2
  # Al3+  + 3 e-        -> Al           : z = 3
  # 2 H2O              -> O2 + 4 H+ + 4 e- : z = 4  (per O2)
  # 2 H2O + 2 e-       -> H2 + 2 OH-    : z = 2  (per H2)
  zCu = 2; zAl = 3; zO2 = 4; zH2 = 2
  printf "Cu2+/Cu : z=%d   Al3+/Al : z=%d   O2 evolution : z=%d   H2 evolution : z=%d\n", zCu, zAl, zO2, zH2
  if (zCu==2 && zAl==3 && zO2==4 && zH2==2) print "PASS: z is the electron count of the balanced half-reaction"
  else { print "FAIL"; exit 1 }
}'
```

`z` = 2 for hydrogen, 4 for oxygen — the origin of the `2 : 1` volume ratio you
see at the end.

## 4. Charge → moles of electrons → moles of species

`charge_mole_electron_bridge`: `Q = z F n`, so `n = Q / (z F)`. Divide the
coulombs by `z F` and you have the moles of product. Every term is present:
`z` (dimensionless), `F` (`I T N⁻¹`), `n` (`N`) → `Q` (`I T`).

Formula: **`Q = z F n`   (so   `n = Q / (z F)`)**

```bash [name:chk_charge_mole_electron_bridge, deps:"chk_faraday_constant | chk_charge_from_current | chk_electrons_per_formula_unit"]
bc -l <<'EOF'
fm=0; fl=0; ft=1; fth=0; fn=-1; fi=1     /* F -> I T N^-1 */
nm=0; nl=0; nt=0; nth=0; nn=1;  ni=0     /* n -> N */
qm=0; ql=0; qt=1; qth=0; qn=0;  qi=1     /* Q -> I T ; z dimensionless */
print qm-(fm+nm)," ",ql-(fl+nl)," ",qt-(ft+nt)," ",qth-(fth+nth)," ",qn-(fn+nn)," ",qi-(fi+ni)," (want 0 0 0 0 0 0)\n"
EOF
# capsule special case: 7200 C reduces how many moles of a z = 2 species?
awk -v f="$F" 'BEGIN{
  Q = 7200; z = 2
  n = Q / (z * f)
  printf "n = %.0f / (2 * %.0f) = %.4f mol\n", Q, f, n
  if (n > 0.0373 && n < 0.0374) print "PASS: ~0.037 mol, from 7200 C at z = 2"
  else { print "FAIL"; exit 1 }
}'
```

Coulombs over `z F` is moles — the whole conversion in one step.

## 5. Faraday's law of electrolysis

Multiply `n = Q/(zF)` by the molar mass and you get a **mass**:

**`m = (Q / F)(M / z) = (I t M) / (z F)`**

`m` in grams, `I` in amps, `t` in seconds, `M` in g/mol, `z` dimensionless. The
check confirms the dimension collapses to mass, then reproduces the capsule's
copper-plating number.

```bash [name:chk_faradays_law, deps:chk_charge_mole_electron_bridge]
bc -l <<'EOF'
/* [I t M / (z F)] : (I T)(M N^-1) / (I T N^-1) = M */
itm=1; itl=0; itt=1; itth=0; itn=-1; iti=1   /* I t M -> M I T N^-1 */
zfm=0; zfl=0; zft=1; zfth=0; zfn=-1; zfi=1    /* z F -> I T N^-1 */
mm=1; ml=0; mt=0; mth=0; mn=0; mi=0           /* mass m -> M */
print mm-(itm-zfm)," ",ml-(itl-zfl)," ",mt-(itt-zft)," ",mth-(itth-zfth)," ",mn-(itn-zfn)," ",mi-(iti-zfi)," (want 0 0 0 0 0 0)\n"
EOF
# capsule special case: Cu plating, I = 2.00 A, t = 3600 s, z = 2, M = 63.55
awk -v f="$F" 'BEGIN{
  I = 2.00; t = 3600; z = 2; M = 63.55
  m = (I * t * M) / (z * f)
  printf "m(Cu) = (2.00 * 3600 * 63.55) / (2 * %.0f) = %.3f g\n", f, m
  if (m > 2.370 && m < 2.372) print "PASS: 2.371 g of copper per 2.00 A-hour"
  else { print "FAIL"; exit 1 }
}'
```

```bash [name:lean_faradays_law, deps:chk_faradays_law]
command -v lean >/dev/null 2>&1 || { echo "SKIP: lean not on PATH"; exit 0; }
d=$(mktemp -d)
cat > "$d/far.lean" <<'EOF'
-- capsule validation/derivation-checks.lean, check 1 (faradays_law_electrolysis)
-- Q = z F n  <=>  n = Q / (z F).
-- 1 F reduces exactly 1 mol of a z = 1 species:
example : ((1 : Int) * 96485 * 1) = 96485 := by decide
-- 2 F (192970 C) reduces exactly 1 mol of a z = 2 species (Cu2+ + 2e- -> Cu):
example : ((192970 : Int) / (2 * 96485)) = 1 := by decide
EOF
if lean "$d/far.lean"; then
  echo "PASS: Lean kernel verified 1 F -> 1 mol (z=1) and 2 F -> 1 mol (z=2)"
else
  echo "FAIL: lean rejected the snippet"; rm -rf "$d"; exit 1
fi
rm -rf "$d"
```

A current and a clock give a mass — no need to weigh anything during the run.

## 6. Moles of product and gas volume

`moles_of_product_electrolysis`: `n_product = Q / (z F ν)`, with `ν` the
product's coefficient in the half-reaction. For hydrogen,
`2H₂O + 2e⁻ → H₂ + 2OH⁻` gives `n(H₂) = Q / (2F)` — **one mole of H₂ per
`2F = 192970 C`**. `gas_volume_electrolysis` then applies the ideal-gas law:
`V = n_product R T / P`. The Lean beat checks the `2 : 1` H₂ : O₂ ratio.

Formula: **`n_product = Q / (z F ν)`,   then   `V = n_product R T / P`**

```bash [name:chk_moles_and_volume, deps:chk_faradays_law]
awk -v f="$F" -v vm="$VM_STP" 'BEGIN{
  # 1 faraday of charge
  Q = f
  nH2 = Q / (2 * f)        # z = 2 per H2
  nO2 = Q / (4 * f)        # z = 4 per O2
  printf "1 F -> %.3f mol H2 (= %.2f L STP) and %.3f mol O2 (= %.2f L STP)\n", nH2, nH2*vm, nO2, nO2*vm
  ratio = nH2 / nO2
  if (nH2 == 0.5 && ratio == 2) print "PASS: 0.5 mol H2 per faraday; H2 : O2 = 2 : 1 by moles (and volume)"
  else { print "FAIL"; exit 1 }
}'
```

```bash [name:lean_gas_ratio, deps:chk_moles_and_volume]
command -v lean >/dev/null 2>&1 || { echo "SKIP: lean not on PATH"; exit 0; }
d=$(mktemp -d)
cat > "$d/ratio.lean" <<'EOF'
-- capsule validation/derivation-checks.lean, check 2 (Faraday volume ratio)
-- H2 needs 2 F per mol, O2 needs 4 F per mol; same charge Q =>
-- n(H2) : n(O2) = (Q/2F) : (Q/4F) = 4/2 : 1 = 2 : 1
example : ((4 : Int) / 2) = 2 := by decide
-- electron balance of the summed cell reaction: 2 H2 carry 4 e-, 1 O2 carries 4 e-
example : ((2 : Int) * 2) = 4 * 1 := by decide
EOF
if lean "$d/ratio.lean"; then
  echo "PASS: Lean kernel verified H2 : O2 = 2 : 1 and the 4 = 4 electron balance"
else
  echo "FAIL: lean rejected the snippet"; rm -rf "$d"; exit 1
fi
rm -rf "$d"
```

Half a mole of hydrogen per faraday, and twice the volume of oxygen — straight
from `z = 2` versus `z = 4`.

## 7. Current efficiency

Faraday's law gives the **theoretical** yield — what you would get if every
electron went to the wanted reaction. `current_efficiency` `η_F = n_actual /
n_theoretical` is the fraction that actually did; the rest went to side
reactions (the other gas, corrosion, the reverse reaction).

Formula: **`η_F = n_actual / n_theoretical`**

```bash [name:chk_current_efficiency, deps:chk_faradays_law]
awk 'BEGIN{
  # a chlor-alkali membrane cell: ~0.96 for NaOH
  n_theo = 100.0
  n_act  = 96.0
  eta = n_act / n_theo
  printf "actual %.0f / theoretical %.0f = current efficiency %.2f\n", n_act, n_theo, eta
  if (eta == 0.96) print "PASS: 96% - the other 4% of the charge went to side reactions"
  else { print "FAIL"; exit 1 }
  # eta_F > 1 is impossible - it means the theoretical basis or the assay is wrong
  print "note: eta_F > 1 is never a real result"
}'
```

Multiply the Faraday-law figure by `η_F` for the real output.

---

## Capstone: sizing a hydrogen electrolyser

You have the whole chain. The electrolyser from Setup runs at `100 A`. Find the
hourly hydrogen output (moles, litres at STP, and after the `98 %` current
efficiency), then the charge needed to make `1 kg` of hydrogen.

```bash [name:capstone, deps:"chk_moles_and_volume | chk_current_efficiency | lean_gas_ratio"]
# charge in one hour
Q_hr=$(bc -l <<< "$I_A * 3600")
echo "charge in 1 h: ${I_A} A * 3600 s = ${Q_hr} C"

# theoretical H2 per hour  (z = 2 per H2)
n_theo=$(bc -l <<< "scale=4; $Q_hr / (2 * $F)")
v_theo=$(bc -l <<< "scale=3; $n_theo * $VM_STP")
echo "theoretical: n(H2) = ${Q_hr} / (2 * ${F}) = ${n_theo} mol/h  = ${v_theo} L/h at STP"

# after current efficiency
n_act=$(bc -l <<< "scale=4; $n_theo * $ETA_F")
echo "at ${ETA_F} current efficiency: ${n_act} mol/h actual"

# charge to make 1 kg of H2
n_kg=$(bc -l <<< "scale=4; 1000 / $M_H2")
Q_kg=$(bc -l <<< "scale=1; $n_kg * 2 * $F")
Ah_kg=$(bc -l <<< "scale=0; $Q_kg / 3600")
echo "1 kg H2 = ${n_kg} mol  ->  Q = ${n_kg} * 2 * ${F} = ${Q_kg} C = ${Ah_kg} A-hour"

awk -v nth="$n_theo" -v nac="$n_act" -v vth="$v_theo" -v ah="$Ah_kg" 'BEGIN{
  ok = (nth > 1.86 && nth < 1.87) && (nac < nth) && (vth > 42 && vth < 43) && (ah > 26000 && ah < 27000)
  if (ok) print "PASS: ~1.87 mol/h (~42 L/h STP) theoretical; ~26.6 kA-h per kg H2 (before the cell voltage)"
  else { print "FAIL"; exit 1 }
}'
echo
echo "That is the current bookkeeping only. Multiply the charge by the cell"
echo "voltage (~1.8-2.0 V, not 1.23 V) for the energy - the next tutorial."
```

If the capstone prints `PASS`, the chain held: `Q = I t` gave the coulombs,
`z = 2` and `F` converted them to moles of hydrogen, the ideal-gas law gave the
volume, and the current efficiency scaled it to reality — and making a kilogram
of hydrogen takes about `26.6` kilo-amp-hours of charge, whatever voltage you
run the cell at.

## Where to go next

- `specific_energy_consumption` (`E_spec = z F V_cell / (M η_F)`) — the same
  bookkeeping times the cell voltage, giving kWh/kg; and `overpotential` /
  `cell_voltage_electrolysis`, why `V_cell` is well above `E°_cell`.
- `water_electrolysis`, `chlor_alkali_process`, `hall_heroult_process`,
  `copper_electrorefining`, `zinc_electrowinning` — the named processes this law
  runs (`indexes/topic-index.md`).
- `flow_battery_energy_capacity` — `Q = c V_tank z F` is the same charge–mole
  bridge, used to size a battery instead of a synthesis.
- The full [`chemistry-electrochemistry`](../SKILL.md) capsule.
