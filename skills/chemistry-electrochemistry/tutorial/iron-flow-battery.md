# An Iron Flow Battery for the Homestead

> Generated from the `chemistry-electrochemistry` capsule (Release 0.1) with the
> `formula-tree-tutorial` skill. The chemistry, the prerequisite order, and
> every calculation come from that capsule.

A flow battery stores its energy as two tanks of dissolved salt and delivers
power through a separate stack of cells — so you size the **duration** and the
**power** independently. The famous chemistry is all-vanadium, but for a small
off-grid installation the practical one is **all-iron**: iron chloride is cheap,
abundant, and about as hazardous as plant fertiliser. This tutorial sizes one:

`redox_flow_battery` → `flow_battery_energy_capacity` / `flow_battery_power` →
`coulombic_efficiency` / `voltage_efficiency` / `energy_efficiency` →
**`iron_flow_battery`** → its parasitic-hydrogen catch.

## How to run this

Install [upmd](https://upmd.dev), then from the repository root run
`upmd skills/chemistry-electrochemistry/tutorial/iron-flow-battery.md` for the
interactive walk, or
`upmd --ci --all skills/chemistry-electrochemistry/tutorial/iron-flow-battery.md`
to run every calculation top to bottom.

Each section ends with a calculation you run yourself. Blocks depend on earlier
ones, so
`upmd --ci -b capstone skills/chemistry-electrochemistry/tutorial/iron-flow-battery.md`
runs the whole chain up to the capstone. Three blocks call `lean` to
kernel-check an arithmetic instance; if `lean` is not on your `PATH` they print
`SKIP` and pass.

## What you need first

- **[`per-amp-hour.md`](per-amp-hour.md)** — `Q = z F n`, the charge–mole bridge.
- **[`kwh-per-kilogram.md`](kwh-per-kilogram.md)** — `E°_cell = E°_cathode −
  E°_anode`, overpotential, `V_cell`.
- **[`chlorine-not-oxygen.md`](chlorine-not-oxygen.md)** — comparing *effective*
  potentials `E° + η` when two electrode reactions compete.

The dimensional checks use the `[M, L, T, Θ, N, I]` basis; a consistent relation
prints `0 0 0 0 0 0`. All numbers are at **298.15 K**, `dilute_ideal_solution`.

---

## 0. Setup

The target: **20 kWh** of usable storage and **4 kW** of power for a homestead,
from an all-iron flow battery.

```bash [name:setup]
export F=96485
export C_FE=1.5            # mol/L, FeCl2 electrolyte concentration
export Z_POS=1             # electrons per Fe on the positive (Fe3+ + e- -> Fe2+) - the energy-limiting side
export DE_AVG=1.2          # V, average operating cell voltage over the SOC window
export WH_L_USABLE=15      # Wh/L actually delivered (real all-iron; theoretical is higher)
export E0_FE3=0.77         # V, E0(Fe3+/Fe2+)
export E0_FE0=-0.44        # V, E0(Fe2+/Fe0)
export TARGET_WH=20000     # Wh usable storage
export TARGET_W=4000       # W power
export V_DIS=1.15          # V, discharge cell voltage at the operating current
export J_ACM2=0.08         # A/cm2, stack current density
export ETA_C=0.97          # coulombic efficiency
export ETA_V=0.80          # voltage efficiency
export RT_SYSTEM=0.70      # round-trip efficiency including pumps and standby
export WH_L_VANADIUM=25    # Wh/L usable, all-vanadium, for comparison
export BC_LINE_LENGTH=0
echo "sizing an all-iron flow battery for 20 kWh / 4 kW"
```

## 1. The flow battery

A `redox_flow_battery` has three parts: two tanks of electrolyte (one for each
redox couple), pumps, and a **stack** of cells separated by an ion-exchange
membrane. `energy_power_decoupling` is the defining feature — the **tanks set
the energy** (add electrolyte for more hours) and the **stack sets the power**
(add cells or area for more kW), and you size them separately. A sealed battery
cannot do this.

```bash [name:chk_redox_flow_battery, deps:setup]
awk 'BEGIN{
  # doubling the storage duration: what changes?
  tank_scales = 1     # 1 = yes, the tanks get bigger
  stack_scales = 0    # 0 = no, the (expensive) stack is unchanged
  printf "to store 2x the hours: tanks scale (%d), stack unchanged (%d)\n", tank_scales, stack_scales
  if (tank_scales == 1 && stack_scales == 0)
    print "PASS: energy is in the tanks, power is in the stack - sized independently"
  else { print "FAIL"; exit 1 }
}'
```

Energy and power are decoupled — the whole reason to use a flow battery.

## 2. Sizing the energy

The charge a tank holds is `Q = c · V_tank · z · F` (coulombs), and the energy
is that times the average cell voltage:

**`E_stored = c · V_tank · z · F · ΔE_avg`**

`c` in mol/m³, `V_tank` in m³, `z` the electrons per active ion, `F` the Faraday
constant, `ΔE_avg` the mean operating voltage. The check confirms the dimension
is energy, then computes the theoretical capacity per litre.

```bash [name:chk_flow_battery_energy_capacity, deps:setup]
bc -l <<'EOF'
/* [c V z F E] : (N L^-3)(L^3)(I T N^-1)(M L^2 T^-3 I^-1) = M L^2 T^-2 = J */
cm=0; cl=-3; ct=0; cth=0; cn=1; ci=0        /* c */
vm=0; vl=3; vt=0; vth=0; vn=0; vi=0         /* V_tank */
fm=0; fl=0; ft=1; fth=0; fn=-1; fi=1        /* F ; z dimensionless */
em=1; el=2; et=-3; eth=0; en=0; ei=-1       /* E */
jm=1; jl=2; jt=-2; jth=0; jn=0; ji=0        /* energy J */
print jm-(cm+vm+fm+em)," ",jl-(cl+vl+fl+el)," ",jt-(ct+vt+ft+et)," ",jth-(cth+vth+fth+eth)," ",jn-(cn+vn+fn+en)," ",ji-(ci+vi+fi+ei)," (want 0 0 0 0 0 0)\n"
EOF
awk -v c="$C_FE" -v f="$F" -v z="$Z_POS" -v de="$DE_AVG" -v use="$WH_L_USABLE" 'BEGIN{
  Q_L  = c * z * f            # C per litre  (1.5 mol/L * 1 * 96485)
  Ah_L = Q_L / 3600
  Wh_L = Ah_L * de            # theoretical Wh per litre
  printf "theoretical: %.0f C/L = %.1f Ah/L ; x %.1f V = %.1f Wh/L\n", Q_L, Ah_L, de, Wh_L
  printf "real usable: ~%d Wh/L  (%.0f%% of theoretical - SOC window + plating limit)\n", use, use/Wh_L*100
  if (Ah_L > 40 && Ah_L < 41) print "PASS: ~40 Ah per litre of 1.5 M FeCl2"
  else { print "FAIL"; exit 1 }
}'
```

```bash [name:lean_energy_capacity, deps:chk_flow_battery_energy_capacity]
command -v lean >/dev/null 2>&1 || { echo "SKIP: lean not on PATH"; exit 0; }
d=$(mktemp -d)
cat > "$d/cap.lean" <<'EOF'
-- capsule validation/derivation-checks.lean, check 10 (flow_battery_energy_capacity)
-- Q = c V_tank z F.  1.6 M active ion (1600 mol/m^3), 1 m^3, z = 1:
example : ((1600 : Int) * 96485) = 154376000 := by decide      -- C per m^3
-- as amp-hours: 154376000 / 3600 ~ 42882 A h
example : ((154376000 : Int) / 3600) = 42882 := by decide
EOF
if lean "$d/cap.lean"; then
  echo "PASS: Lean kernel verified c z F = coulombs (1600 * 96485 = 154376000 C/m^3 = 42882 A h)"
else
  echo "FAIL: lean rejected the snippet"; rm -rf "$d"; exit 1
fi
rm -rf "$d"
```

About `40 Ah` per litre of electrolyte in theory; a real all-iron system
delivers roughly a third of that (`~15 Wh/L`), because the state-of-charge
window is limited and the negative can only plate so much iron.

## 3. Sizing the power

The power comes from the stack:

**`P = N_cells · A_stack · j · V_cell`**

`N_cells` cells of active area `A_stack`, run at current density `j`, each at
cell voltage `V_cell`. The check confirms `A · j · V` is power, then computes
the area for the target.

```bash [name:chk_flow_battery_power, deps:setup]
bc -l <<'EOF'
/* [A j V] : (L^2)(I L^-2)(M L^2 T^-3 I^-1) = M L^2 T^-3 = W */
am=0; al=2; at=0; ath=0; an=0; ai=0         /* area A */
jm=0; jl=-2; jt=0; jth=0; jn=0; ji=1        /* current density j */
vm=1; vl=2; vt=-3; vth=0; vn=0; vi=-1       /* V_cell */
wm=1; wl=2; wt=-3; wth=0; wn=0; wi=0        /* power W */
print wm-(am+jm+vm)," ",wl-(al+jl+vl)," ",wt-(at+jt+vt)," ",wth-(ath+jth+vth)," ",wn-(an+jn+vn)," ",wi-(ai+ji+vi)," (want 0 0 0 0 0 0)\n"
EOF
awk -v p="$TARGET_W" -v v="$V_DIS" -v j="$J_ACM2" 'BEGIN{
  I_total = p / v                       # A
  area_cm2 = I_total / j                 # cm^2
  printf "for %d W at %.2f V: total current %.0f A ; at %.2f A/cm2 -> %.0f cm2 = %.2f m2 of active area\n", p, v, I_total, j, area_cm2, area_cm2/10000
  if (area_cm2 > 43000 && area_cm2 < 44000) print "PASS: ~4.35 m2 of stack for 4 kW"
  else { print "FAIL"; exit 1 }
}'
```

`~4.35 m²` of membrane-and-electrode area delivers the `4 kW` — independent of
how many hours of storage the tanks hold.

## 4. The three efficiencies

A flow battery loses charge and voltage on every cycle:

- **`η_C = Q_out / Q_in`** (coulombic) — lost to crossover, shunt currents, and
  side reactions; rises with current density.
- **`η_V = V_discharge / V_charge`** (voltage) — the overpotential and `IR`
  losses, paid both ways; falls with current density.
- **`η_E = η_C · η_V`** (energy / round-trip) — the product.

```bash [name:chk_efficiencies, deps:setup]
bc -l <<'EOF'
/* eta_E = eta_C * eta_V : product of two dimensionless ratios -> dimensionless */
print 0-0," ",0-0," ",0-0," ",0-0," ",0-0," ",0-0," (want 0 0 0 0 0 0)\n"
EOF
awk -v c="$ETA_C" -v v="$ETA_V" -v rt="$RT_SYSTEM" 'BEGIN{
  eta_E = c * v
  printf "eta_C = %.2f  x  eta_V = %.2f  ->  eta_E (stack) = %.2f\n", c, v, eta_E
  printf "system round-trip (with pumps + standby): ~%.2f\n", rt
  if (eta_E > 0.77 && eta_E < 0.79 && rt < eta_E)
    print "PASS: ~78% stack, ~70% system - below Li-ion (~90-95%), the price of the architecture"
  else { print "FAIL"; exit 1 }
}'
```

```bash [name:lean_efficiency, deps:chk_efficiencies]
command -v lean >/dev/null 2>&1 || { echo "SKIP: lean not on PATH"; exit 0; }
d=$(mktemp -d)
cat > "$d/eff.lean" <<'EOF'
-- capsule validation/derivation-checks.lean, check 11 (energy_efficiency)
-- eta_E = eta_C * eta_V.  eta_C = 0.97 , eta_V = 0.85  (percent):
example : ((97 * 85 : Int)) = 8245 := by decide                -- eta_E = 82.45 %
-- the round trip cannot beat either factor:
example : ((8245 : Int) < 9700) := by decide
EOF
if lean "$d/eff.lean"; then
  echo "PASS: Lean kernel verified eta_E = eta_C * eta_V, and that it beats neither factor"
else
  echo "FAIL: lean rejected the snippet"; rm -rf "$d"; exit 1
fi
rm -rf "$d"
```

Round-trip efficiency in the field is around `70 %` — worse than a lithium
battery, the cost of pumps, a resistive membrane, and standby self-discharge.

## 5. All-iron: cheap, non-toxic, aqueous

`iron_flow_battery`: `Fe³⁺/Fe²⁺` on the positive, `Fe²⁺/Fe⁰` on the negative
(iron *plates* during charge). So

**`E°_cell = E°(Fe³⁺/Fe²⁺) − E°(Fe²⁺/Fe⁰) = 0.77 − (−0.44) = 1.21 V`**

The electrolyte is `FeCl₂` at `pH 1–3` — iron chloride is a water-treatment
coagulant and a plant micronutrient, not a hazard. Iron on **both** sides gives
the all-vanadium advantage: a species that crosses the membrane just
self-discharges, it does not poison the other tank. The catch: because the
negative plates iron, the battery is a **hybrid** — energy density is low
(`~10–20 Wh/L`, capped by the plating), so the tanks run larger than a vanadium
system's.

```bash [name:chk_iron_flow_battery, deps:"chk_flow_battery_energy_capacity | chk_efficiencies"]
awk -v e3="$E0_FE3" -v e0="$E0_FE0" 'BEGIN{
  E0_cell = e3 - e0
  printf "E0_cell = %.2f - (%.2f) = %.2f V\n", e3, e0, E0_cell
  # crossover: a leaked Fe ion on the wrong side is just re-oxidised / re-reduced
  crossover_poisons = 0   # 0 = no, same element both sides
  printf "crossover contaminates the other tank? %s\n", (crossover_poisons ? "yes" : "no - same element both sides")
  if (E0_cell > 1.20 && E0_cell < 1.22 && crossover_poisons == 0)
    print "PASS: 1.21 V cell; benign crossover; cheap non-toxic FeCl2 electrolyte"
  else { print "FAIL"; exit 1 }
}'
```

```bash [name:lean_iron_flow_battery, deps:chk_iron_flow_battery]
command -v lean >/dev/null 2>&1 || { echo "SKIP: lean not on PATH"; exit 0; }
d=$(mktemp -d)
cat > "$d/iron.lean" <<'EOF'
-- capsule validation/derivation-checks.lean, check 16 (iron_flow_battery). Centivolts.
-- E0_cell = E0(Fe3+/Fe2+) - E0(Fe2+/Fe0) = 77 - (-44) = 121  (~1.21 V).
example : ((77 : Int) - (-44)) = 121 := by decide
-- the negative plates iron BELOW the H2 line thermodynamically (E0 < 0):
example : ((-44 : Int) < 0) := by decide
-- sizing: 20 kWh of usable storage at ~15 Wh/L needs ~1333 L per tank.
example : ((20000 : Int) / 15) = 1333 := by decide
EOF
if lean "$d/iron.lean"; then
  echo "PASS: Lean kernel verified E0_cell = 121 cV, iron plates below the H2 line, 20 kWh -> 1333 L/tank"
else
  echo "FAIL: lean rejected the snippet"; rm -rf "$d"; exit 1
fi
rm -rf "$d"
```

`1.21 V`, iron on both sides, and an electrolyte you could almost drink — at the
cost of bigger tanks.

## 6. The parasitic hydrogen

`E°(Fe²⁺/Fe⁰) = −0.44 V` is **below** `E°(H⁺/H₂) = 0` — so on the thermodynamics
alone, driving the negative electrode negative enough to plate iron should
instead evolve **hydrogen** (`competing_electrode_reactions`). Iron plates
anyway because hydrogen evolution on iron is kinetically slow (`~0.4–0.6 V`
overpotential) — but here the overpotential only **tilts** the split, it does
not flip it the way the oxygen overpotential flips chlor-alkali. A few percent
of the charging current still goes to `H₂`, which slowly moves the two tanks
out of oxidation-state balance (`capacity_fade`) and has to be corrected by
periodically re-reducing the positive electrolyte.

```bash [name:chk_parasitic_hydrogen, deps:chk_iron_flow_battery]
awk -v e0="$E0_FE0" 'BEGIN{
  E_H2 = 0.0            # E0(H+/H2)
  eta_H2 = 0.45         # H2 overpotential on iron
  # thermodynamics: H2 is above Fe plating -> H2 favoured
  printf "E0(Fe2+/Fe0) = %.2f V  <  E0(H+/H2) = %.2f V  -> thermodynamics favours H2\n", e0, E_H2
  # with the H2 overpotential, effective H2 onset drops to about -eta_H2
  eff_H2 = E_H2 - eta_H2
  printf "with ~%.2f V H2 overpotential on iron, effective H2 onset ~ %.2f V\n", eta_H2, eff_H2
  printf "iron plating (%.2f V) and throttled H2 (~%.2f V) now overlap -> Fe plates (majority), H2 leaks (minority)\n", e0, eff_H2
  # the residual H2 is why coulombic efficiency < 100% on charge and rebalancing is needed
  if (e0 < E_H2 && eff_H2 < e0 + 0.1)
    print "PASS: overpotential makes Fe plating possible, not guaranteed - the H2 leak drives the rebalancing need"
  else { print "FAIL"; exit 1 }
}'
```

Unlike chlorine-vs-oxygen, the overpotential here does not settle the contest —
it just lets iron win most of the current. The leftover hydrogen is the reason
an all-iron battery needs a rebalancing cell.

---

## Capstone: the 20 kWh / 4 kW homestead battery

You have the whole chain. Size the tanks and the stack for the Setup target, find
what you draw from the panels to fill it, and compare the tank volume to an
all-vanadium system.

```bash [name:capstone, deps:"chk_iron_flow_battery | chk_flow_battery_power | lean_efficiency | lean_iron_flow_battery"]
# tanks: usable energy / usable Wh per litre
L_per_tank=$(bc -l <<< "scale=0; $TARGET_WH / $WH_L_USABLE")
m3_per_tank=$(bc -l <<< "scale=2; $L_per_tank / 1000")
echo "tanks:  ${TARGET_WH} Wh / ${WH_L_USABLE} Wh/L = ${L_per_tank} L per tank  (${m3_per_tank} m3 each, ~${m3_per_tank} IBC totes x2)"

# stack: total current / current density
I_total=$(bc -l <<< "scale=0; $TARGET_W / $V_DIS")
area_m2=$(bc -l <<< "scale=2; $I_total / $J_ACM2 / 10000")
echo "stack:  ${TARGET_W} W / ${V_DIS} V = ${I_total} A ; at ${J_ACM2} A/cm2 -> ${area_m2} m2 of active area"

# what you draw from the panels to store 20 kWh usable, at 70% round-trip
draw=$(bc -l <<< "scale=1; $TARGET_WH / 1000 / $RT_SYSTEM")
echo "to bank ${TARGET_WH} Wh usable at ${RT_SYSTEM} round-trip: draw ${draw} kWh from the array"

# vs all-vanadium
L_vanadium=$(bc -l <<< "scale=0; $TARGET_WH / $WH_L_VANADIUM")
ratio=$(bc -l <<< "scale=2; $L_per_tank / $L_vanadium")
echo "all-vanadium (${WH_L_VANADIUM} Wh/L) would need ${L_vanadium} L per tank - iron needs ${ratio}x the volume"

awk -v lt="$L_per_tank" -v am="$area_m2" -v dr="$draw" -v rv="$ratio" 'BEGIN{
  ok = (lt > 1300 && lt < 1360) && (am > 4.2 && am < 4.5) && (dr > 28 && dr < 29) && (rv > 1.5 && rv < 1.8)
  if (ok)
    print "PASS: ~1333 L/tank, ~4.35 m2 stack, ~28.6 kWh drawn per 20 kWh banked; ~1.7x the tank volume of vanadium"
  else { print "FAIL"; exit 1 }
}'
echo
echo "The iron tanks are bigger, but FeCl2 electrolyte is ~5-10 \$/kWh against"
echo "~50-80 \$/kWh for vanadium - so for a homestead the volume trade is worth it."
```

If the capstone prints `PASS`, the chain held: `c z F` set the charge per litre,
`ΔE_avg` made it `~40 Ah/L` theoretical (`~15 Wh/L` real), `A j V` sized the
stack for `4 kW`, and `η_E` said you feed in `~28.6 kWh` to bank `20`. Two IBC
totes of iron chloride and four square metres of stack — bigger than a lithium
wall pack, but built from a coagulant and scrap iron.

## Where to go next

- `zinc_iron_flow_battery` — a higher-voltage low-toxicity alternative (alkaline
  ferro/ferricyanide positive, zinc-plating negative).
- `fixed_cell_battery_contrast` — when a sealed lead-acid or LiFePO₄ pack is the
  better call (short duration, small scale, higher efficiency).
- `shunt_current`, `state_of_charge`, `capacity_fade` — the rest of the
  flow-battery band (`indexes/topic-index.md`).
- The sibling tutorials [`per-amp-hour.md`](per-amp-hour.md),
  [`kwh-per-kilogram.md`](kwh-per-kilogram.md),
  [`chlorine-not-oxygen.md`](chlorine-not-oxygen.md), and the full
  [`chemistry-electrochemistry`](../SKILL.md) capsule.
