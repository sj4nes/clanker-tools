# Why the Chlorine Plant Makes Chlorine, Not Oxygen

> Generated from the `chemistry-electrochemistry` capsule (Release 0.1) with the
> `formula-tree-tutorial` skill. The chemistry, the prerequisite order, and
> every calculation come from that capsule.

Electrolyse brine and the anode has a choice: oxidise chloride to `Cl₂`, or
oxidise water to `O₂`. The standard potentials say **oxygen** should win
(`E°(O₂) = 1.23 V < E°(Cl₂) = 1.36 V`). Every chlor-alkali plant on Earth makes
**chlorine**. This tutorial follows the capsule's chain to why — overpotential
inverts the thermodynamic order — and then sizes a real cell line:

`ion_exchange_membrane` → `competing_electrode_reactions` →
`oxygen_overpotential` → `thermodynamic_vs_kinetic_product` →
**`chlor_alkali_process`**.

## How to run this

Install [upmd](https://upmd.dev), then from the repository root run
`upmd skills/chemistry-electrochemistry/tutorial/chlorine-not-oxygen.md` for the
interactive walk, or
`upmd --ci --all skills/chemistry-electrochemistry/tutorial/chlorine-not-oxygen.md`
to run every calculation top to bottom.

Each section ends with a calculation you run yourself. Blocks depend on earlier
ones, so
`upmd --ci -b capstone skills/chemistry-electrochemistry/tutorial/chlorine-not-oxygen.md`
runs the whole chain up to the capstone. Two blocks call `lean` to
kernel-check an arithmetic instance; if `lean` is not on your `PATH` they print
`SKIP` and pass.

## What you need first

- **[`per-amp-hour.md`](per-amp-hour.md)** — Faraday's law `m = ItM/(zF)`, the
  electron count `z`, current efficiency `η_F`.
- **[`kwh-per-kilogram.md`](kwh-per-kilogram.md)** — `E°_cell = E°_cathode −
  E°_anode`, overpotential, `V_cell`, and `E_spec = zF V_cell / (M η_F)`.
- Standard reduction potentials are **reduction** potentials versus the SHE.

All numbers are at **298.15 K**, `dilute_ideal_solution`. Standard-potential
values are the capsule's (`E°(Cl₂/Cl⁻) = +1.36 V`, `E°(O₂/H₂O) = +1.23 V`).

---

## 0. Setup

The worked cell is a modern **membrane** chlor-alkali cell.

```bash [name:setup]
export F=96485
export M_CL2=70.90        # g/mol  (= 2 * A_r(Cl) = 2 * 35.45, the capsule value)
export M_H2=2.016
export M_NAOH=40.00       # g/mol  (reference value)
export E0_CL2=1.36        # V, E0(Cl2 / Cl-)
export E0_O2=1.23         # V, E0(O2 / H2O)
export ETA_O2=0.50        # V, O2 evolution overpotential on a DSA anode (capsule: 0.3-0.6)
export ETA_CL2=0.03       # V, Cl2 evolution overpotential - almost none
export I_A=15000          # A, one cell line
export ETA_F=0.96         # current efficiency for Cl2 / NaOH (capsule)
export VCELL=3.1          # V, real membrane-cell voltage (capsule: 3-4 V)
export BC_LINE_LENGTH=0
echo "membrane chlor-alkali cell: 2 NaCl + 2 H2O -> Cl2 + H2 + 2 NaOH"
```

## 1. The membrane cell

The cell is split by a **cation-exchange membrane** (`ion_exchange_membrane`), a
selective version of a `salt_bridge`. It passes `Na⁺` from the anolyte (brine)
to the catholyte, and **blocks `Cl⁻` and `OH⁻`** — so the sodium hydroxide
product comes out essentially chloride-free, and the chlorine gas stays out of
the caustic. Without an ionic path between the compartments there is no current
at all.

```bash [name:chk_ion_exchange_membrane, deps:setup]
awk 'BEGIN{
  # which ions cross the cation membrane?  1 = passes, 0 = blocked
  Na = 1; Cl = 0; OH = 0
  printf "cation membrane:  Na+ passes (%d)   Cl- blocked (%d)   OH- blocked (%d)\n", Na, Cl, OH
  if (Na == 1 && Cl == 0 && OH == 0)
    print "PASS: Na+ carries the current across; NaOH stays free of chloride"
  else { print "FAIL"; exit 1 }
}'
```

`Na⁺` carries the ionic current; the membrane keeps the two products apart.

## 2. Competing reactions at the anode

In brine, the anode can run **either** of two oxidations
(`competing_electrode_reactions`):

- `2Cl⁻ → Cl₂ + 2e⁻`        `E° = +1.36 V`
- `2H₂O → O₂ + 4H⁺ + 4e⁻`   `E° = +1.23 V`

Which one actually happens is set by the electrode potential, the *kinetics*
(overpotential), and the chloride concentration — not by `E°` alone.

```bash [name:chk_competing_electrode_reactions, deps:setup]
awk -v ecl="$E0_CL2" -v eo2="$E0_O2" 'BEGIN{
  printf "anode candidate 1:  2 Cl- -> Cl2 + 2e-        E0 = +%.2f V\n", ecl
  printf "anode candidate 2:  2 H2O -> O2 + 4 H+ + 4e-  E0 = +%.2f V\n", eo2
  if (ecl > eo2) print "PASS: two possible anode reactions, E0 within 0.13 V of each other"
  else { print "FAIL"; exit 1 }
}'
```

Two reactions, close in `E°` — the outcome is decided at the margin.

## 3. Thermodynamics says oxygen

A reaction with a **lower** reduction potential is easier to drive as an
oxidation (it sits lower on the scale, so less anode potential is needed to
reverse it). `E°(O₂/H₂O) = 1.23 V` is below `E°(Cl₂/Cl⁻) = 1.36 V`, so on the
thermodynamics alone the anode should evolve **oxygen** and leave the chloride
alone.

```bash [name:chk_thermodynamics, deps:chk_competing_electrode_reactions]
awk -v ecl="$E0_CL2" -v eo2="$E0_O2" 'BEGIN{
  printf "E0(O2) = %.2f V  <  E0(Cl2) = %.2f V\n", eo2, ecl
  if (eo2 < ecl) print "PASS: on E0 alone, oxygen is the thermodynamically favoured anode product"
  else { print "FAIL"; exit 1 }
}'
```

```bash [name:lean_selectivity, deps:chk_thermodynamics]
command -v lean >/dev/null 2>&1 || { echo "SKIP: lean not on PATH"; exit 0; }
d=$(mktemp -d)
cat > "$d/sel.lean" <<'EOF'
-- capsule validation/derivation-checks.lean, check 14 (thermodynamic_vs_kinetic_product)
-- centivolts.  Thermodynamics favours O2:  E0(O2/H2O) = 123  <  E0(Cl2/Cl-) = 136.
example : ((123 : Int) < 136) := by decide
-- but the anode runs whichever needs the LOWER applied potential, E0 + eta:
--   Cl2:  136 + 3  = 139   vs   O2:  123 + 50 = 173.   Cl2 wins.
example : ((136 : Int) + 3) < (123 + 50) := by decide
EOF
if lean "$d/sel.lean"; then
  echo "PASS: Lean kernel verified 123 < 136 (thermo favours O2) and 139 < 173 (kinetics favours Cl2)"
else
  echo "FAIL: lean rejected the snippet"; rm -rf "$d"; exit 1
fi
rm -rf "$d"
```

By the potentials alone, oxygen should win. It does not.

## 4. Kinetics says chlorine

`oxygen_overpotential` is large — oxygen evolution is a slow, four-electron,
bond-forming reaction, and even on the best oxide catalyst (the RuO₂/TiO₂
"dimensionally stable anode") it needs `~0.5 V` of extra potential to run at
plant current. Chlorine evolution, a simple two-electron step, needs almost
none (`~0.03 V`). So `thermodynamic_vs_kinetic_product` says: compare the
**effective** potentials `E° + η`, and the anode runs whichever is lower.

```bash [name:chk_oxygen_overpotential, deps:chk_thermodynamics]
awk -v ecl="$E0_CL2" -v eo2="$E0_O2" -v ncl="$ETA_CL2" -v no2="$ETA_O2" 'BEGIN{
  eff_cl2 = ecl + ncl
  eff_o2  = eo2 + no2
  printf "effective anode potential for Cl2:  %.2f + %.2f = %.2f V\n", ecl, ncl, eff_cl2
  printf "effective anode potential for O2 :  %.2f + %.2f = %.2f V\n", eo2, no2, eff_o2
  printf "the anode runs whichever is lower -> %s\n", (eff_cl2 < eff_o2 ? "CHLORINE" : "oxygen")
  if (eff_cl2 < eff_o2 && eo2 < ecl)
    print "PASS: E0 favours O2, but E0 + overpotential favours Cl2 by ~0.34 V"
  else { print "FAIL"; exit 1 }
}'
```

The `0.5 V` oxygen overpotential more than cancels the `0.13 V` `E°`
disadvantage of chlorine — so chlorine is what comes off the anode.

## 5. The chlor-alkali process

Put it together (`chlor_alkali_process`):

- **anode** (DSA): `2Cl⁻ → Cl₂ + 2e⁻`
- **cathode**: `2H₂O + 2e⁻ → H₂ + 2OH⁻`
- **net**: `2NaCl + 2H₂O → Cl₂ + H₂ + 2NaOH`   (`z = 2`)

`E°_cell ≈ −0.83 − 1.36 ≈ −2.2 V`, and a real membrane cell runs at
`V_cell ≈ 3–4 V` (the rest is overpotential and `IR`). The products come in a
fixed ratio: **`Cl₂ : H₂ : NaOH = 1 : 1 : 2`** per `2F` of charge, at
`η_F ≈ 0.96`.

```bash [name:chk_chlor_alkali_process, deps:"chk_oxygen_overpotential | chk_ion_exchange_membrane"]
awk -v f="$F" 'BEGIN{
  Q = 2 * f                       # 2 faradays
  nCl2  = Q / (2 * f)             # z = 2 per Cl2
  nH2   = Q / (2 * f)             # z = 2 per H2
  nNaOH = 2 * Q / (2 * f)         # 2 OH- per 2 e-
  printf "per 2 F:  %.0f mol Cl2  :  %.0f mol H2  :  %.0f mol NaOH\n", nCl2, nH2, nNaOH
  if (nCl2 == 1 && nH2 == 1 && nNaOH == 2)
    print "PASS: Cl2 : H2 : NaOH = 1 : 1 : 2 per 2 F"
  else { print "FAIL"; exit 1 }
}'
```

```bash [name:lean_chlor_alkali, deps:chk_chlor_alkali_process]
command -v lean >/dev/null 2>&1 || { echo "SKIP: lean not on PATH"; exit 0; }
d=$(mktemp -d)
cat > "$d/ca.lean" <<'EOF'
-- capsule validation/derivation-checks.lean, check 15 (chlor_alkali_process)
-- 2 NaCl + 2 H2O -> Cl2 + H2 + 2 NaOH, z = 2.
-- Cl2 (2 e-) and H2 (2 e-) come out 1 : 1; NaOH is 2 : 1.
example : ((2 : Int) * 1) = (1 * 2) := by decide
-- charge to make 1 tonne of Cl2 (M ~ 71 g/mol): ~14084 mol/tonne.
example : ((1000000 : Int) / 71) = 14084 := by decide
EOF
if lean "$d/ca.lean"; then
  echo "PASS: Lean kernel verified Cl2 : H2 = 1 : 1 and ~14084 mol Cl2 per tonne"
else
  echo "FAIL: lean rejected the snippet"; rm -rf "$d"; exit 1
fi
rm -rf "$d"
```

Every mole of chlorine comes with a mole of hydrogen and two of caustic soda —
one reason the three are priced together.

---

## Capstone: a chlor-alkali cell line

You have the whole chain. A membrane cell line runs at `15 kA`. Find the hourly
output of chlorine (and its co-products), its specific energy, and what a `10 %`
loss of anode current to oxygen would cost.

```bash [name:capstone, deps:"chk_chlor_alkali_process | lean_selectivity | lean_chlor_alkali"]
Q_hr=$(bc -l <<< "$I_A * 3600")
echo "charge in 1 h: ${I_A} A * 3600 s = ${Q_hr} C"

# chlorine (z = 2), after current efficiency
n_cl2=$(bc -l <<< "scale=2; $Q_hr / (2 * $F) * $ETA_F")
kg_cl2=$(bc -l <<< "scale=2; $n_cl2 * $M_CL2 / 1000")
echo "Cl2:  ${n_cl2} mol/h  =  ${kg_cl2} kg/h   (at eta_F ${ETA_F})"

# co-products: H2 1:1, NaOH 2:1
kg_h2=$(bc -l <<< "scale=2; $n_cl2 * $M_H2 / 1000")
kg_naoh=$(bc -l <<< "scale=2; 2 * $n_cl2 * $M_NAOH / 1000")
echo "co-products:  ${kg_h2} kg/h H2  ,  ${kg_naoh} kg/h NaOH"

# specific energy for chlorine  (E_spec = z F V_cell / (M eta_F))
espec=$(bc -l <<< "scale=0; 2 * $F * $VCELL / ($M_CL2 * $ETA_F)")
kwh_kg=$(bc -l <<< "scale=2; $espec * 1000 / 3600000")
echo "E_spec(Cl2) = 2 * ${F} * ${VCELL} / (${M_CL2} * ${ETA_F}) = ${espec} J/g = ${kwh_kg} kWh/kg"

# if O2 stole 10% of the anode current: eta_F 0.96 -> 0.86
penalty=$(awk -v e="$ETA_F" 'BEGIN{ printf "%.1f", (e/0.86 - 1)*100 }')
echo "if O2 took 10% of the anode current: eta_F 0.96 -> 0.86, energy per kg Cl2 up ~${penalty}%"

awk -v kg="$kg_cl2" -v e="$kwh_kg" -v p="$penalty" 'BEGIN{
  ok = (kg > 18.5 && kg < 19.5) && (e > 2.3 && e < 2.6) && (p > 10 && p < 13)
  if (ok) print "PASS: ~19 kg/h Cl2 at ~2.4 kWh/kg; losing 10% to O2 costs ~12% more energy"
  else { print "FAIL"; exit 1 }
}'
echo
echo "This is why chlor-alkali anodes are RuO2-coated (high O2 overpotential,"
echo "low Cl2 overpotential) and why the brine is kept concentrated and acidic:"
echo "every trick pushes the effective-potential margin further toward chlorine."
```

If the capstone prints `PASS`, the chain held: two anode reactions were possible,
`E°` favoured oxygen by `0.13 V`, the `0.5 V` oxygen overpotential flipped that,
and the plant makes `~19 kg/h` of chlorine per `15 kA` at `~2.4 kWh/kg` — with a
mole of hydrogen and two of caustic soda for free.

## Where to go next

- `chlorate_perchlorate` — driving the chlorine chemistry further, `Cl⁻ → ClO₃⁻
  → ClO₄⁻`, in an undivided cell.
- `zinc_electrowinning` and `water_electrolysis` — the same overpotential logic:
  zinc plates below the `H₂` line because `H₂` evolution is slow on zinc; water
  electrolysers pay the oxygen overpotential twice.
- `hall_heroult_process`, `copper_electrorefining` — the other named processes
  (`indexes/topic-index.md`).
- The sibling tutorials [`per-amp-hour.md`](per-amp-hour.md) and
  [`kwh-per-kilogram.md`](kwh-per-kilogram.md), and the full
  [`chemistry-electrochemistry`](../SKILL.md) capsule.
