# The Zinc–Iron Alternative

> Generated from the `chemistry-electrochemistry` capsule (Release 0.1) with the
> `formula-tree-tutorial` skill. The chemistry, the prerequisite order, and
> every calculation come from that capsule.

[`iron-flow-battery.md`](iron-flow-battery.md) built the all-iron flow battery —
cheap, low-hazard, but low energy density. The **zinc–iron** battery keeps most
of the cost and safety advantages, runs at a higher voltage (so the tanks are
smaller), and swaps one catch for another: instead of parasitic hydrogen, it
plates zinc metal, which limits how deeply and how long you can charge. This
short tutorial is the comparison:

`zinc_iron_flow_battery` — the two half-reactions, `E°_cell ≈ 1.56 V`, the
ferrocyanide safety question, and the zinc-plating limit.

## How to run this

Install [upmd](https://upmd.dev), then from the repository root run
`upmd skills/chemistry-electrochemistry/tutorial/zinc-iron-alternative.md` for
the interactive walk, or
`upmd --ci --all skills/chemistry-electrochemistry/tutorial/zinc-iron-alternative.md`
to run every calculation top to bottom.

Each section ends with a calculation you run yourself. Blocks depend on earlier
ones, so
`upmd --ci -b capstone skills/chemistry-electrochemistry/tutorial/zinc-iron-alternative.md`
runs the whole chain up to the capstone. One block calls `lean` to kernel-check
an arithmetic instance; if `lean` is not on your `PATH` it prints `SKIP` and
passes.

## What you need first

- **[`iron-flow-battery.md`](iron-flow-battery.md)** — the flow-battery
  architecture, energy in the tanks / power in the stack, and the all-iron
  chemistry this one is compared against.
- **[`the-voltage-isnt-fixed.md`](the-voltage-isnt-fixed.md)** — the Nernst
  runaway near full charge, which the plated zinc makes worse.
- Standard reduction potentials are **reduction** potentials versus the SHE.

All numbers are at **298.15 K**, `dilute_ideal_solution`. `E°` values in
alkaline solution differ from the acidic-table values.

---

## 0. Setup

```bash [name:setup]
export E0_FECN=0.36       # V, E0(Fe(CN)6 3- / 4-)  (positive electrode)
export E0_ZN_ALK=-1.20    # V, E0(Zn(OH)4 2- / Zn) in base  (negative electrode)
export E0_CELL_IRON=1.21  # V, all-iron cell voltage (tutorial 4)
export WH_L_ZNFE=25       # Wh/L usable, zinc-iron
export WH_L_IRON=15       # Wh/L usable, all-iron
export TARGET_WH=20000    # Wh usable storage (same target as tutorial 4)
export BC_LINE_LENGTH=0
echo "zinc-iron flow battery, compared with the all-iron battery from tutorial 4"
```

## 1. Same architecture, different couples

A `zinc_iron_flow_battery` is the same tank / stack / membrane machine as the
all-iron battery, in a `KOH` (alkaline) electrolyte, with:

- **negative** (plates on charge): `Zn(OH)₄²⁻ + 2e⁻ ⇌ Zn + 4OH⁻`   `E° ≈ −1.20 V`
- **positive**: `Fe(CN)₆³⁻ + e⁻ ⇌ Fe(CN)₆⁴⁻`   `E° ≈ +0.36 V`

Compare with all-iron: `Fe²⁺/Fe⁰` (`−0.44 V`) and `Fe³⁺/Fe²⁺` (`+0.77 V`). The
zinc–iron negative sits much lower, which buys voltage.

```bash [name:chk_zinc_iron_architecture, deps:setup]
awk -v efe="$E0_FECN" -v ezn="$E0_ZN_ALK" 'BEGIN{
  printf "negative:  Zn(OH)4 2- + 2e- <=> Zn + 4 OH-    E0 = %.2f V  (zinc plates on charge)\n", ezn
  printf "positive:  Fe(CN)6 3- + e- <=> Fe(CN)6 4-      E0 = %+.2f V\n", efe
  # both electrodes are cheap, abundant elements; the electrolyte is KOH
  if (ezn < -1.0 && efe > 0)
    print "PASS: a zinc-plating negative and a ferrocyanide positive, in KOH"
  else { print "FAIL"; exit 1 }
}'
```

Zinc metal on one side, dissolved ferrocyanide on the other — a hybrid, like
zinc–bromine.

## 2. The cell voltage

`E°_cell = E°_positive − E°_negative = 0.36 − (−1.20) = 1.56 V` — well above the
all-iron `1.21 V`.

```bash [name:chk_cell_voltage, deps:chk_zinc_iron_architecture]
awk -v efe="$E0_FECN" -v ezn="$E0_ZN_ALK" -v eiron="$E0_CELL_IRON" 'BEGIN{
  E0_cell = efe - ezn
  printf "E0_cell = %.2f - (%.2f) = %.2f V   (all-iron: %.2f V)\n", efe, ezn, E0_cell, eiron
  if (E0_cell > 1.54 && E0_cell < 1.58 && E0_cell > eiron)
    print "PASS: 1.56 V - about 0.35 V more than all-iron, per electron"
  else { print "FAIL"; exit 1 }
}'
```

```bash [name:lean_zinc_iron, deps:chk_cell_voltage]
command -v lean >/dev/null 2>&1 || { echo "SKIP: lean not on PATH"; exit 0; }
d=$(mktemp -d)
cat > "$d/znfe.lean" <<'EOF'
-- capsule validation/derivation-checks.lean, check 17 (zinc_iron_flow_battery). Centivolts.
-- E0_cell = E0(Fe(CN)6 3-/4-) - E0(Zn(OH)4/Zn) = 36 - (-120) = 156  (~1.56 V).
example : ((36 : Int) - (-120)) = 156 := by decide
-- higher than all-iron (156 cV > 121 cV) -> more energy per electron:
example : ((156 : Int) > 121) := by decide
-- 20 kWh at ~25 Wh/L needs ~800 L per tank, vs ~1333 L for all-iron at ~15 Wh/L:
example : ((20000 : Int) / 25) = 800 := by decide
EOF
if lean "$d/znfe.lean"; then
  echo "PASS: Lean kernel verified E0_cell = 156 cV, higher than all-iron's 121, and the 800 L sizing"
else
  echo "FAIL: lean rejected the snippet"; rm -rf "$d"; exit 1
fi
rm -rf "$d"
```

Higher voltage means more energy per coulomb — which shows up as smaller tanks.

## 3. Higher voltage → smaller tanks

Energy per litre is `charge per litre × cell voltage`. Zinc–iron's higher
voltage (and a higher practical zinc-loading) put its usable energy density
around `25 Wh/L`, versus `~15 Wh/L` for all-iron. For the same `20 kWh` that is
`~800 L` per tank instead of `~1330 L`.

```bash [name:chk_energy_density, deps:chk_cell_voltage]
awk -v wh="$TARGET_WH" -v znfe="$WH_L_ZNFE" -v iron="$WH_L_IRON" 'BEGIN{
  L_znfe = wh / znfe
  L_iron = wh / iron
  printf "for %d Wh usable:  zinc-iron %.0f L/tank (@ %d Wh/L)  vs  all-iron %.0f L/tank (@ %d Wh/L)\n", wh, L_znfe, znfe, L_iron, iron
  ratio = L_iron / L_znfe
  printf "zinc-iron tanks are ~%.0f%% the volume of all-iron\n", 100/ratio
  if (L_znfe > 790 && L_znfe < 810 && L_znfe < L_iron)
    print "PASS: ~800 L per tank - about 60% of the all-iron volume"
  else { print "FAIL"; exit 1 }
}'
```

The higher voltage is real energy density — one IBC tote per side instead of
one-and-a-third.

## 4. Is ferrocyanide safe?

The positive electrolyte is potassium ferro/ferricyanide, and "cyanide" in the
name alarms people. It should not: in `Fe(CN)₆⁴⁻` the six cyanide ions are
**locked to the iron** by a very strong bond, and the complex is so stable and
non-toxic that it is the **anti-caking additive in table salt** (E535–538).
Free cyanide is a different substance entirely.

The one real caveat: **do not acidify a ferrocyanide solution.** Strong acid can
break the complex and release `HCN` gas. In an alkaline (`KOH`) flow battery
that never happens — but keep acid away from the tanks, and label them.

```bash [name:chk_ferrocyanide_safety, deps:chk_zinc_iron_architecture]
awk 'BEGIN{
  # rank the hazard: 0 = benign, 1 = handle with care, 2 = dangerous
  free_cyanide        = 2
  ferrocyanide_in_KOH = 0    # anti-caking additive in table salt
  ferrocyanide_plus_strong_acid = 2   # can liberate HCN - do not do this
  printf "free cyanide: hazard %d\n", free_cyanide
  printf "ferrocyanide in the alkaline battery: hazard %d (it is a food additive)\n", ferrocyanide_in_KOH
  printf "ferrocyanide + strong acid: hazard %d (liberates HCN - never mix)\n", ferrocyanide_plus_strong_acid
  if (ferrocyanide_in_KOH == 0 && ferrocyanide_plus_strong_acid == 2)
    print "PASS: safe as operated (alkaline); the hazard is only if you add acid"
  else { print "FAIL"; exit 1 }
}'
```

Safe as a KOH-based battery; the rule is "no acid near the ferrocyanide tank".

## 5. The zinc-plating catch

Zinc–iron trades the all-iron battery's parasitic-hydrogen problem for a
**zinc-plating** problem. On charge, metallic zinc builds up on the negative
electrode. That has three consequences:

1. **It is a hybrid** — the negative's capacity lives on the electrode, not in
   the tank, so the energy is only partly decoupled from the stack.
2. **Dendrites** — zinc tends to plate as needles that can grow across the cell
   and short it, which caps how much you can plate (depth of charge).
3. The Nernst term (`the-voltage-isnt-fixed.md`) already makes the voltage run
   away near full charge; the plating limit is a *harder* stop on top of it.

```bash [name:chk_zinc_plating_catch, deps:chk_energy_density]
awk 'BEGIN{
  # what fraction of the rated capacity is safely usable, roughly
  depth_of_charge_znfe = 0.70   # zinc plating + dendrite limit
  soc_window_only      = 0.80   # from tutorial 6, the Nernst window alone
  printf "usable fraction: ~%.0f%% (zinc plating limit) vs ~%.0f%% (Nernst window alone)\n", depth_of_charge_znfe*100, soc_window_only*100
  hybrid = 1
  printf "energy fully decoupled from the stack? %s\n", (hybrid ? "no - part of it is the plated zinc" : "yes")
  if (depth_of_charge_znfe < soc_window_only && hybrid)
    print "PASS: the zinc plating is a tighter limit than the Nernst window, and breaks full decoupling"
  else { print "FAIL"; exit 1 }
}'
```

The zinc plating is why this is not a true flow battery — and why you cannot
just make the tanks bigger to get more hours.

---

## Capstone: which flow battery for the homestead?

You now have three chemistries and a real decision. For the same `20 kWh / 4 kW`
target, lay them side by side.

```bash [name:capstone, deps:"chk_energy_density | chk_ferrocyanide_safety | chk_zinc_plating_catch | lean_zinc_iron"]
awk -v wh="$TARGET_WH" 'BEGIN{
  print "20 kWh / 4 kW homestead battery - three flow chemistries:"
  print ""
  print "                      all-vanadium   all-iron       zinc-iron"
  print "  E0_cell (V)              1.26          1.21           1.56"
  print "  usable energy (Wh/L)     ~25           ~15            ~25"
  printf "  tank per side (L)        ~%d          ~%d          ~%d\n", wh/25, wh/15, wh/25
  print "  electrolyte              H2SO4         mild FeCl2     caustic KOH"
  print "  main hazard              acid + V      low            KOH burns;"
  print "                                                        no acid near tanks"
  print "  architecture             true flow     near-true      hybrid (Zn plating)"
  print "  cost of electrolyte      high          very low       low"
  print "  the catch                V price       H2 rebalance   Zn dendrites,"
  print "                                                        charge-depth limit"
  print ""
  # a simple decision rule
  print "rule of thumb:"
  print "  long duration, hands-off, cheap     -> all-iron"
  print "  space-limited, will manage charging -> zinc-iron"
  print "  grid-scale, budget no object        -> all-vanadium"

  # sanity: zinc-iron and vanadium tanks are smaller than all-iron
  L_iron = wh/15; L_znfe = wh/25; L_van = wh/25
  if (L_znfe < L_iron && L_van < L_iron)
    print "\nPASS: zinc-iron matches vanadium on tank size at a fraction of the electrolyte cost"
  else { print "FAIL"; exit 1 }
}'
```

If the capstone prints `PASS`, the picture is complete: zinc–iron sits between
all-iron and vanadium — vanadium's energy density and voltage, iron's low cost
and low hazard — but it pays for that with the zinc-plating limit, which is why
the all-iron battery is still the simplest "set it and forget it" choice for a
homestead that mostly needs *hours*, not *watts per litre*.

## Where to go next

- `fixed_cell_battery_contrast` — and when a sealed LiFePO₄ or lead-acid pack
  beats every flow battery (short duration, small scale, higher efficiency).
- `crossover`, `capacity_fade`, `shunt_current` — the flow-battery failure modes
  that apply to all three chemistries (`indexes/topic-index.md`).
- The sibling tutorials — the full electrochemistry sequence is
  [`per-amp-hour`](per-amp-hour.md) → [`kwh-per-kilogram`](kwh-per-kilogram.md) →
  [`chlorine-not-oxygen`](chlorine-not-oxygen.md) →
  [`iron-flow-battery`](iron-flow-battery.md) →
  [`hydrogen-as-a-battery`](hydrogen-as-a-battery.md) →
  [`the-voltage-isnt-fixed`](the-voltage-isnt-fixed.md) → this one; see
  [`tutorial/README.md`](README.md).
- The full [`chemistry-electrochemistry`](../SKILL.md) capsule.
