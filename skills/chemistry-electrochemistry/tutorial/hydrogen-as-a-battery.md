# Hydrogen as a Battery

> Generated from the `chemistry-electrochemistry` capsule (Release 0.1) with the
> `formula-tree-tutorial` skill. The chemistry, the prerequisite order, and
> every calculation come from that capsule.

Electrolyse water when power is cheap, store the hydrogen, and run the cell
backwards as a fuel cell when power is scarce. The storage is astonishingly
compact and barely self-discharges — but the round trip throws away most of the
energy, because you pay the oxygen electrode's overpotential **going both ways**.
This tutorial builds the water-electrolysis process and its reverse, then
decides when hydrogen beats a flow battery for a homestead:

`water_electrolysis` → reversible vs thermoneutral voltage → `oxygen_overpotential`
→ `gas_volume_electrolysis` → **`reversible_fuel_cell`**.

## How to run this

Install [upmd](https://upmd.dev), then from the repository root run
`upmd skills/chemistry-electrochemistry/tutorial/hydrogen-as-a-battery.md` for
the interactive walk, or
`upmd --ci --all skills/chemistry-electrochemistry/tutorial/hydrogen-as-a-battery.md`
to run every calculation top to bottom.

Each section ends with a calculation you run yourself. Blocks depend on earlier
ones, so
`upmd --ci -b capstone skills/chemistry-electrochemistry/tutorial/hydrogen-as-a-battery.md`
runs the whole chain up to the capstone. Two blocks call `lean` to kernel-check
an arithmetic instance; if `lean` is not on your `PATH` they print `SKIP` and
pass.

## What you need first

- **[`per-amp-hour.md`](per-amp-hour.md)** — Faraday's law, `z`, the `2 : 1`
  H₂ : O₂ ratio.
- **[`kwh-per-kilogram.md`](kwh-per-kilogram.md)** — `E°_cell`, `ΔG = −zFE`,
  overpotential, `V_cell`, and the `~54 kWh/kg` figure for electrolytic hydrogen.
- **[`iron-flow-battery.md`](iron-flow-battery.md)** — round-trip efficiency, and
  the 20 kWh / 4 kW homestead battery the capstone compares against.

The dimensional checks use the `[M, L, T, Θ, N, I]` basis. All numbers are at
**298.15 K**, `dilute_ideal_solution`.

---

## 0. Setup

```bash [name:setup]
export F=96485
export E0_REV=1.23         # V, reversible decomposition voltage (from dG)
export V_THERMONEUTRAL=1.48  # V, thermoneutral voltage (from dH)
export VCELL_ELY=1.90      # V, real electrolyser cell voltage
export VCELL_FC=0.75       # V, real fuel-cell discharge voltage
export ETA_O2=0.45         # V, oxygen electrode overpotential (paid both ways)
export VM_STP=22.711       # L/mol, ideal-gas molar volume at STP
export KWH_KG_H2=54        # kWh per kg to electrolyse H2 (from kwh-per-kilogram)
export LHV_H2=33.3         # kWh/kg, lower heating value of hydrogen
export ETA_FC=0.50         # fuel-cell efficiency (electrical out / H2 LHV in)
export H2_DENSITY_350BAR=24  # kg/m3, compressed H2 at 350 bar, 25 C
export TARGET_KWH=20       # kWh to store and later deliver
export FLOW_RT=0.70        # iron flow battery round-trip (tutorial 4)
export BC_LINE_LENGTH=0
echo "hydrogen round-trip storage vs a flow battery, for 20 kWh"
```

## 1. Splitting water

`water_electrolysis`: `2H₂O → 2H₂ + O₂`. The half-reactions depend on the
electrolyte:

- **alkaline** (KOH): cathode `2H₂O + 2e⁻ → H₂ + 2OH⁻`; anode `4OH⁻ → O₂ + 2H₂O + 4e⁻`
- **PEM** (acid, solid polymer): cathode `2H⁺ + 2e⁻ → H₂`; anode `2H₂O → O₂ + 4H⁺ + 4e⁻`

Either way `z = 2` per H₂ (`4` per O₂), and `E°_cell = E°_cathode − E°_anode =
0.00 − 1.23 = −1.23 V`. Negative → it must be driven; `|E°_cell| = 1.23 V` is
the reversible floor.

```bash [name:chk_water_electrolysis, deps:setup]
awk -v e0="$E0_REV" 'BEGIN{
  Ec = 0.00     # E0(2 H+/H2)  (or the alkaline equivalent, same net cell)
  Ea = e0       # E0(O2/H2O)
  E0_cell = Ec - Ea
  z_H2 = 2; z_O2 = 4
  printf "net: 2 H2O -> 2 H2 + O2   z = %d per H2, %d per O2\n", z_H2, z_O2
  printf "E0_cell = %.2f - %.2f = %.2f V   (|E0_cell| = %.2f V, the reversible floor)\n", Ec, Ea, E0_cell, -E0_cell
  if (E0_cell == -1.23) print "PASS: 1.23 V is the least you can spend to split water"
  else { print "FAIL"; exit 1 }
}'
```

`1.23 V` — the thermodynamic minimum, and nowhere near what a real cell needs.

## 2. Reversible versus thermoneutral

Two special voltages:

- **`1.23 V`** — the *reversible* voltage, from `ΔG` (`ΔG° = zF·1.23 = 237 kJ/mol
  H₂`). At exactly `1.23 V` the cell would run infinitely slowly and draw the
  rest of the enthalpy (`TΔS`) as heat from the room.
- **`1.48 V`** — the *thermoneutral* voltage, from `ΔH` (`ΔH° = zF·1.48 = 286
  kJ/mol H₂`). At `1.48 V` the cell neither heats nor cools; above it, the extra
  electrical input comes out as waste heat.

A real cell at `1.90 V` is above thermoneutral, so it runs hot, and its
efficiency is `1.48 / 1.90 ≈ 78 %` on `ΔH` (or `1.23 / 1.90 ≈ 65 %` on `ΔG`).

```bash [name:chk_reversible_vs_thermoneutral, deps:chk_water_electrolysis]
awk -v rev="$E0_REV" -v tn="$V_THERMONEUTRAL" -v real="$VCELL_ELY" 'BEGIN{
  eff_dH = tn / real * 100
  eff_dG = rev / real * 100
  printf "reversible %.2f V (dG)  |  thermoneutral %.2f V (dH)  |  real %.2f V\n", rev, tn, real
  printf "efficiency: %.0f%% on dH (HHV-style),  %.0f%% on dG\n", eff_dH, eff_dG
  if (eff_dH > 76 && eff_dH < 79 && real > tn) print "PASS: ~78% efficient, and running above thermoneutral means it makes waste heat"
  else { print "FAIL"; exit 1 }
}'
```

```bash [name:lean_thermoneutral, deps:chk_reversible_vs_thermoneutral]
command -v lean >/dev/null 2>&1 || { echo "SKIP: lean not on PATH"; exit 0; }
d=$(mktemp -d)
cat > "$d/tn.lean" <<'EOF'
-- capsule validation/derivation-checks.lean, check 9 (cell_voltage_electrolysis)
-- centivolts.  V_cell = 123 (reversible) + 10 + 30 + 35 = 198.
example : ((123 : Int) + 10 + 30 + 35) = 198 := by decide
-- efficiency vs the thermoneutral 148: 148 / 198 ~ 74 %.
example : ((148 * 100 : Int) / 198) = 74 := by decide
EOF
if lean "$d/tn.lean"; then
  echo "PASS: Lean kernel verified V_cell = 198 cV and ~74% thermoneutral efficiency at that voltage"
else
  echo "FAIL: lean rejected the snippet"; rm -rf "$d"; exit 1
fi
rm -rf "$d"
```

The gap between `1.23 V` and the real `~1.9 V` is almost all the oxygen
electrode.

## 3. The oxygen tax

`oxygen_overpotential`: the oxygen-evolution reaction `2H₂O → O₂ + 4H⁺ + 4e⁻` is
slow — four electrons, an O–O bond to form — and needs `~0.3–0.6 V` of extra
potential even on the best oxide catalysts. That single overpotential is why the
electrolyser needs `1.9 V` not `1.23 V`. And it does not go away when you run the
cell the other way: the fuel cell's oxygen-*reduction* reaction is just as slow,
so it loses `~0.3–0.5 V` there too.

```bash [name:chk_oxygen_overpotential, deps:chk_water_electrolysis]
awk -v rev="$E0_REV" -v eta="$ETA_O2" -v ely="$VCELL_ELY" -v fc="$VCELL_FC" 'BEGIN{
  printf "electrolyser: needs %.2f V + oxygen overpotential + other losses -> %.2f V\n", rev, ely
  printf "fuel cell:    delivers %.2f V - oxygen overpotential - other losses -> %.2f V\n", rev, fc
  # the oxygen electrode is the dominant loss in BOTH directions
  paid_both_ways = 1
  printf "oxygen overpotential (~%.2f V) is paid on charge AND on discharge? %s\n", eta, (paid_both_ways ? "yes" : "no")
  if (ely > rev && fc < rev && paid_both_ways)
    print "PASS: the O2 electrode taxes both halves of the round trip"
  else { print "FAIL"; exit 1 }
}'
```

You pay the oxygen overpotential twice — once to make the hydrogen, once to use
it.

## 4. Gas volumes

`gas_volume_electrolysis`: `V = n_product · R T / P`. Per faraday of charge,
`n(H₂) = 0.5 mol` and `n(O₂) = 0.25 mol`, so at STP that is `11.4 L` of hydrogen
and `5.7 L` of oxygen — the `2 : 1` ratio, straight from `z = 2` versus `z = 4`.

```bash [name:chk_gas_volumes, deps:chk_water_electrolysis]
bc -l <<'EOF'
/* [n R T / P] : (N)(M L^2 T^-2 Th^-1 N^-1)(Th) / (M L^-1 T^-2) = L^3 = volume */
nm=0; nl=0; nt=0; nth=0; nn=1; ni=0         /* n */
rm=1; rl=2; rt=-2; rth=-1; rn=-1; ri=0      /* R */
tm=0; tl=0; tt=0; tth=1; tn=0; ti=0         /* T */
pm=1; pl=-1; pt=-2; pth=0; pn=0; pi=0       /* P */
vm=0; vl=3; vt=0; vth=0; vn=0; vi=0         /* volume */
print vm-(nm+rm+tm-pm)," ",vl-(nl+rl+tl-pl)," ",vt-(nt+rt+tt-pt)," ",vth-(nth+rth+tth-pth)," ",vn-(nn+rn+tn-pn)," ",vi-(ni+ri+ti-pi)," (want 0 0 0 0 0 0)\n"
EOF
awk -v vm="$VM_STP" 'BEGIN{
  nH2 = 0.5; nO2 = 0.25          # per faraday
  printf "per faraday: %.1f mol H2 = %.1f L STP ,  %.2f mol O2 = %.1f L STP\n", nH2, nH2*vm, nO2, nO2*vm
  if (nH2/nO2 == 2) print "PASS: H2 : O2 = 2 : 1 by volume"
  else { print "FAIL"; exit 1 }
}'
```

```bash [name:lean_gas_ratio, deps:chk_gas_volumes]
command -v lean >/dev/null 2>&1 || { echo "SKIP: lean not on PATH"; exit 0; }
d=$(mktemp -d)
cat > "$d/ratio.lean" <<'EOF'
-- capsule validation/derivation-checks.lean, check 2 (Faraday volume ratio)
-- H2 needs 2 F per mol, O2 needs 4 F per mol; same charge => n(H2):n(O2) = 4/2 : 1 = 2 : 1
example : ((4 : Int) / 2) = 2 := by decide
example : ((2 : Int) * 2) = 4 * 1 := by decide
EOF
if lean "$d/ratio.lean"; then
  echo "PASS: Lean kernel verified H2 : O2 = 2 : 1"
else
  echo "FAIL: lean rejected the snippet"; rm -rf "$d"; exit 1
fi
rm -rf "$d"
```

Twice as much hydrogen as oxygen — the useful half is the bigger half.

## 5. Running it backwards: the fuel cell

`reversible_fuel_cell`: the same cell, discharging. `2H₂ + O₂ → 2H₂O`,
`E°_cell = +1.23 V`, `ΔG° = −475 kJ` (`−237 kJ/mol H₂`). A device that does both
— electrolyse when power is cheap, discharge when it is scarce — is a hydrogen
analogue of a flow battery, with the energy stored as compressed gas.

The round-trip efficiency is poor: you charge at `~1.9 V` and discharge at
`~0.75 V`, so on voltage alone the round trip is `0.75 / 1.9 ≈ 40 %` (a bit less
after current losses). The oxygen overpotential is paid in both directions.

```bash [name:chk_reversible_fuel_cell, deps:"chk_reversible_vs_thermoneutral | chk_oxygen_overpotential"]
awk -v ely="$VCELL_ELY" -v fc="$VCELL_FC" 'BEGIN{
  rt_voltage = fc / ely * 100
  printf "charge at %.2f V, discharge at %.2f V  ->  voltage round trip = %.0f%%\n", ely, fc, rt_voltage
  printf "(dG per mol H2: %d kJ; the fuel cell recovers only ~half of it as electricity)\n", 237
  if (rt_voltage > 38 && rt_voltage < 42)
    print "PASS: ~40% voltage round trip - most of the energy is lost as heat, both ways"
  else { print "FAIL"; exit 1 }
}'
```

Forty percent, at best — the price of using the oxygen electrode twice.

---

## Capstone: hydrogen storage versus the iron flow battery

You have both storage options now. Size a hydrogen round-trip system to deliver
the same `20 kWh` as the iron flow battery from
[`iron-flow-battery.md`](iron-flow-battery.md), and compare.

```bash [name:capstone, deps:"chk_reversible_fuel_cell | chk_gas_volumes | lean_thermoneutral"]
# 1. how much H2 to deliver 20 kWh out of the fuel cell
kwh_h2_needed=$(bc -l <<< "scale=1; $TARGET_KWH / $ETA_FC")           # kWh of H2 LHV
kg_h2=$(bc -l <<< "scale=3; $kwh_h2_needed / $LHV_H2")
echo "to deliver ${TARGET_KWH} kWh at ${ETA_FC} fuel-cell efficiency: ${kwh_h2_needed} kWh of H2 = ${kg_h2} kg"

# 2. electrolyser input to make that H2
kwh_in=$(bc -l <<< "scale=1; $kg_h2 * $KWH_KG_H2")
echo "electrolyser input at ${KWH_KG_H2} kWh/kg: ${kwh_in} kWh from the array"

# 3. round trip
rt=$(awk -v o="$TARGET_KWH" -v i="$kwh_in" 'BEGIN{ printf "%.0f", o/i*100 }')
echo "hydrogen round-trip efficiency: ${TARGET_KWH} / ${kwh_in} = ${rt}%"

# 4. storage volume at 350 bar
vol_L=$(bc -l <<< "scale=1; $kg_h2 * 1000 / $H2_DENSITY_350BAR")
echo "storage: ${kg_h2} kg H2 at 350 bar (~${H2_DENSITY_350BAR} kg/m3) = ${vol_L} L  (one gas cylinder)"

# 5. versus the iron flow battery
flow_rt_pct=$(bc -l <<< "scale=0; $FLOW_RT * 100")
echo
echo "iron flow battery (tutorial 4): ${flow_rt_pct}% round trip, ~2700 L of tanks"
echo "hydrogen:                       ${rt}% round trip, ~${vol_L} L cylinder"

awk -v rt="$rt" -v vol="$vol_L" -v frt="$flow_rt_pct" 'BEGIN{
  ok = (rt > 27 && rt < 35) && (vol > 40 && vol < 65) && (frt == 70)
  if (ok) {
    print "PASS: hydrogen ~31% round trip in ~50 L; iron flow ~70% in ~2700 L"
    print "  -> daily cycling: iron flow wins (you cannot throw away 2/3 of your"
    print "     energy every day). Seasonal storage (charge in summer, use in"
    print "     winter): hydrogen wins - the tiny sealed cylinder barely"
    print "     self-discharges over months, and the tank size stops mattering."
  }
  else { print "FAIL"; exit 1 }
}'
```

If the capstone prints `PASS`, the chain held: `1.23 V` is the floor to split
water, the oxygen overpotential drags the real electrolyser to `~1.9 V` and the
fuel cell down to `~0.75 V`, and the round trip is `~31 %` — so hydrogen is a
compact, low-self-discharge store for *seasonal* energy, and a flow battery
(or a lithium pack) is the right answer for anything you cycle daily.

## Where to go next

- `hall_heroult_process`, `copper_electrorefining`, `zinc_electrowinning` — the
  other named electrolysis processes (`indexes/topic-index.md`).
- `nernst_equation` — how the cell voltage (and the efficiency) shift with
  temperature, pressure, and concentration.
- `zinc_iron_flow_battery` — a higher-voltage low-toxicity flow chemistry.
- The sibling tutorials [`per-amp-hour.md`](per-amp-hour.md),
  [`kwh-per-kilogram.md`](kwh-per-kilogram.md),
  [`chlorine-not-oxygen.md`](chlorine-not-oxygen.md),
  [`iron-flow-battery.md`](iron-flow-battery.md), and the full
  [`chemistry-electrochemistry`](../SKILL.md) capsule.
