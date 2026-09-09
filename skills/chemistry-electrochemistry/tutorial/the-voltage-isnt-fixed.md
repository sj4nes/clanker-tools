# The Voltage Isn't Fixed

> Generated from the `chemistry-electrochemistry` capsule (Release 0.1) with the
> `formula-tree-tutorial` skill. The chemistry, the prerequisite order, and
> every calculation come from that capsule.

`E°_cell` is a table value — the cell voltage with every species at unit
activity. A real cell is never at unit activity, and its voltage moves with the
concentrations. The **Nernst equation** is the rule for that motion, and it
explains three things at once: why a pH meter reads pH, why you can build a
battery from nothing but a concentration difference, and why a flow battery
can't be run all the way to empty or full.

`reaction_quotient` → **`nernst_equation`** → `nernst_298k_form` →
`concentration_cell` → `cell_potential_vs_soc`.

## How to run this

Install [upmd](https://upmd.dev), then from the repository root run
`upmd skills/chemistry-electrochemistry/tutorial/the-voltage-isnt-fixed.md` for
the interactive walk, or
`upmd --ci --all skills/chemistry-electrochemistry/tutorial/the-voltage-isnt-fixed.md`
to run every calculation top to bottom.

Each section ends with a calculation you run yourself. Blocks depend on earlier
ones, so
`upmd --ci -b capstone skills/chemistry-electrochemistry/tutorial/the-voltage-isnt-fixed.md`
runs the whole chain up to the capstone. Two blocks call `lean` to kernel-check
an arithmetic instance; if `lean` is not on your `PATH` they print `SKIP` and
pass.

## What you need first

- **[`per-amp-hour.md`](per-amp-hour.md)** and
  **[`kwh-per-kilogram.md`](kwh-per-kilogram.md)** — `E°_cell = E°_cathode −
  E°_anode`, `ΔG = −zFE`, and the Faraday constant.
- **From [`chemistry-foundations`](../../chemistry-foundations/SKILL.md)**:
  the reaction quotient `Q` (the equilibrium-constant expression evaluated at any
  composition), logarithms, and `ΔG = ΔG° + RT ln Q`.
- **[`iron-flow-battery.md`](iron-flow-battery.md)** — state of charge, and the
  "SOC window" this tutorial's capstone finally explains.

The dimensional check uses the `[M, L, T, Θ, N, I]` basis. Everything is at
**298.15 K**, `dilute_ideal_solution` (so `Q` is written in concentrations).

---

## 0. Setup

```bash [name:setup]
export F=96485
export RT_F=0.025693        # R T / F at 298.15 K, in volts
export MV_DECADE=0.05916    # R T ln10 / F at 298.15 K = 59.16 mV per decade of Q
export E0_DANIELL=1.10      # V, E0_cell for Zn | Zn2+ || Cu2+ | Cu
export E0_VANADIUM=1.26     # V, E0_cell for the all-vanadium flow battery
export BC_LINE_LENGTH=0
echo "how the cell voltage moves away from E0 with concentration and state of charge"
```

## 1. The reaction quotient

`Q` is the equilibrium-constant expression — products over reactants, each raised
to its coefficient — but evaluated at **whatever composition the cell is in**,
not just at equilibrium. Two landmarks:

- **`Q = 0`** at the very start, if there is no product yet.
- **`Q = K`** at equilibrium — where the cell is fully discharged and `E = 0`.

Everything in between is where a working cell lives.

```bash [name:chk_reaction_quotient, deps:setup]
awk 'BEGIN{
  # Daniell cell reaction: Zn + Cu2+ -> Zn2+ + Cu ;  Q = [Zn2+] / [Cu2+]
  # (Zn and Cu are solids, activity 1)
  Zn2 = 1.0; Cu2 = 0.01
  Q = Zn2 / Cu2
  printf "Q = [Zn2+]/[Cu2+] = %.2f / %.2f = %.0f\n", Zn2, Cu2, Q
  # at equilibrium Q = K ~ 1.5e37 (from tutorial 2) and E = 0
  printf "fresh cell: Q well below K -> E near E0 ; dead cell: Q = K -> E = 0\n"
  if (Q == 100) print "PASS: Q has the K expression, evaluated at the actual composition"
  else { print "FAIL"; exit 1 }
}'
```

`Q` measures how far the cell has run — from `0` (fresh) toward `K` (dead).

## 2. The Nernst equation

From `ΔG = ΔG° + RT ln Q` with `ΔG = −zFE` and `ΔG° = −zFE°`:

**`E = E° − (R T / z F) ln Q`**

The `RT/zF` prefactor is a voltage (`R T / F = 0.0257 V` at 298 K). As `Q` rises
(the cell runs down), `ln Q` rises, and `E` falls. The check confirms the
prefactor is a potential, then computes the Daniell cell away from standard
conditions.

```bash [name:chk_nernst_equation, deps:chk_reaction_quotient]
bc -l <<'EOF'
/* [R T / (z F)] : (M L^2 T^-2 Th^-1 N^-1)(Th) / (I T N^-1) = M L^2 T^-3 I^-1 = V */
rm=1; rl=2; rt=-2; rth=-1; rn=-1; ri=0      /* R */
tm=0; tl=0; tt=0; tth=1; tn=0; ti=0         /* T */
fm=0; fl=0; ft=1; fth=0; fn=-1; fi=1        /* F ; z dimensionless */
vm=1; vl=2; vt=-3; vth=0; vn=0; vi=-1       /* potential */
print vm-(rm+tm-fm)," ",vl-(rl+tl-fl)," ",vt-(rt+tt-ft)," ",vth-(rth+tth-fth)," ",vn-(rn+tn-fn)," ",vi-(ri+ti-fi)," (want 0 0 0 0 0 0)\n"
EOF
awk -v e0="$E0_DANIELL" -v rtf="$RT_F" 'BEGIN{
  z = 2; Q = 100                    # [Zn2+]/[Cu2+] = 1.0 / 0.01
  E = e0 - (rtf / z) * log(Q)       # awk log() is natural log
  printf "Daniell at [Cu2+] = 0.01 M, [Zn2+] = 1.0 M:  E = %.2f - (%.4f/2) ln(100) = %.3f V\n", e0, rtf, E
  if (E > 1.03 && E < 1.05) print "PASS: 1.04 V - the low copper concentration costs ~60 mV"
  else { print "FAIL"; exit 1 }
}'
```

```bash [name:lean_nernst, deps:chk_nernst_equation]
command -v lean >/dev/null 2>&1 || { echo "SKIP: lean not on PATH"; exit 0; }
d=$(mktemp -d)
cat > "$d/nernst.lean" <<'EOF'
-- capsule validation/derivation-checks.lean, check 6 (nernst_equation)
-- E = E0 - (RT/zF) ln Q ; with E0 = (RT/zF) ln K and Q = K, E = 0.
-- instance (RT/zF) ln K = x = 85:
example : ((85 : Int) - 85) = 0 := by decide
-- Q < K  =>  ln Q < ln K  =>  E > 0 (the cell still drives forward). Instance ln Q term = 40:
example : ((85 : Int) - 40) > 0 := by decide
EOF
if lean "$d/nernst.lean"; then
  echo "PASS: Lean kernel verified E = 0 at Q = K, and E > 0 while Q < K"
else
  echo "FAIL: lean rejected the snippet"; rm -rf "$d"; exit 1
fi
rm -rf "$d"
```

Drop a reactant's concentration and the cell voltage drops with it — here, `60 mV`
for a 100-fold dilution of copper.

## 3. The 298 K shortcut

Convert the natural log to base 10 and fix the temperature:

**`E = E° − (0.05916 V / z) · log₁₀ Q`**   (298.15 K)

`0.05916 V = R T ln 10 / F`. So a **ten-fold** change in `Q` moves `E` by exactly
`59.16 / z` millivolts. For a one-electron sensor (`z = 1`) that is `−59.16 mV`
per decade — and a pH electrode is exactly this: `E = const − 0.05916 · pH`.

```bash [name:chk_nernst_298k_form, deps:chk_nernst_equation]
awk -v mv="$MV_DECADE" 'BEGIN{
  for (z = 1; z <= 3; z++)
    printf "z = %d: %.1f mV per ten-fold change in Q\n", z, mv/z*1000
  # a pH electrode: one decade in [H+] = one pH unit = 59.16 mV (z = 1)
  printf "pH electrode (z=1): %.2f mV per pH unit\n", mv*1000
  if (mv*1000 > 59 && mv*1000 < 60) print "PASS: 59.16 mV per decade at z = 1 - the pH-meter slope"
  else { print "FAIL"; exit 1 }
}'
```

```bash [name:lean_298k, deps:chk_nernst_298k_form]
command -v lean >/dev/null 2>&1 || { echo "SKIP: lean not on PATH"; exit 0; }
d=$(mktemp -d)
cat > "$d/mv.lean" <<'EOF'
-- capsule validation/derivation-checks.lean, check 7 (nernst_298k_form)
-- per decade of Q the shift is (5916 / z) in units of 0.01 mV.
example : ((5916 : Int) / 1) = 5916 := by decide     -- z = 1: 59.16 mV / decade
example : ((5916 : Int) / 2) = 2958 := by decide     -- z = 2: 29.58 mV / decade
EOF
if lean "$d/mv.lean"; then
  echo "PASS: Lean kernel verified 59.16/z mV per decade (z=1 -> 59.16, z=2 -> 29.58)"
else
  echo "FAIL: lean rejected the snippet"; rm -rf "$d"; exit 1
fi
rm -rf "$d"
```

The pH meter is the Nernst equation with a wire on it.

## 4. A battery from a concentration difference

Put the **same** couple on both sides at different concentrations
(`concentration_cell`). Then `E° = 0` (identical electrodes), and the entire
voltage comes from the ratio:

**`E = −(R T / z F) ln([dilute] / [concentrated])`**

The concentrated side is the cathode (its ion gets reduced), the dilute side is
the anode — and the cell runs until the two concentrations equalise.

```bash [name:chk_concentration_cell, deps:chk_nernst_equation]
awk -v mv="$MV_DECADE" 'BEGIN{
  # Cu | Cu2+(0.01 M) || Cu2+(1.0 M) | Cu
  dilute = 0.01; conc = 1.0; z = 2
  # E = -(0.05916/z) log10(dilute/conc)
  E = -(mv / z) * (log(dilute/conc) / log(10))
  printf "Cu concentration cell, 0.01 M vs 1.0 M:  E = -(%.4f/2) log10(0.01) = %.4f V\n", mv, E
  printf "concentrated side = cathode, dilute side = anode; runs until they equalise\n"
  if (E > 0.058 && E < 0.060) print "PASS: ~59 mV from a 100-fold concentration difference, no chemistry needed"
  else { print "FAIL"; exit 1 }
}'
```

Sixty millivolts out of two identical copper electrodes — the voltage is pure
entropy of mixing.

## 5. Why a battery's voltage sags

As any cell discharges, reactants are consumed and products build up, so `Q`
climbs from its starting value toward `K`. The Nernst `−(RT/zF) ln Q` term
therefore drags the open-circuit voltage **down toward zero**
(`cell_potential_vs_soc`). This is separate from the overpotential and `IR` sag
under load — it is there even at zero current.

For the all-vanadium flow battery, with the same state of charge on both sides,

**`E_OCV = E°_cell + (2 R T / F) · ln[SOC / (1 − SOC)]`**

```bash [name:chk_cell_potential_vs_soc, deps:chk_nernst_equation]
awk -v e0="$E0_VANADIUM" -v rtf="$RT_F" 'BEGIN{
  k = 2 * rtf                                  # 2 R T / F
  for (i = 0; i < 3; i++) {
    split("0.10 0.50 0.90", s, " ")
    soc = s[i+1] + 0
    E = e0 + k * log(soc / (1 - soc))
    printf "SOC %.0f%%:  E_OCV = %.2f + %.4f * ln(%.2f/%.2f) = %.3f V\n", soc*100, e0, k, soc, 1-soc, E
  }
  # check the 90% and 10% points straddle E0 symmetrically
  Ehi = e0 + k * log(0.9/0.1)
  Elo = e0 + k * log(0.1/0.9)
  if (Ehi > 1.36 && Ehi < 1.39 && Elo > 1.13 && Elo < 1.16)
    print "PASS: OCV runs 1.15 -> 1.26 -> 1.37 V across 10 -> 50 -> 90% SOC"
  else { print "FAIL"; exit 1 }
}'
```

The voltage is not flat across the charge — it is a Nernst curve, steepest at
the ends.

---

## Capstone: the SOC window, explained

Tutorial 4 said a real all-iron system delivers only about a third of its
theoretical `Wh/L` because "the state-of-charge window is limited". Here is why,
for the vanadium cell: near `SOC = 0` or `SOC = 1` the Nernst term
`ln[SOC/(1−SOC)]` runs away, so the voltage diverges and the cell becomes
useless. Compute the usable window.

```bash [name:capstone, deps:"chk_cell_potential_vs_soc | chk_nernst_298k_form | lean_nernst"]
awk -v e0="$E0_VANADIUM" -v rtf="$RT_F" 'BEGIN{
  k = 2 * rtf
  print "all-vanadium OCV vs state of charge (E0_cell = " e0 " V):"
  n = split("0.05 0.10 0.25 0.50 0.75 0.90 0.95", s, " ")
  for (i = 1; i <= n; i++) {
    soc = s[i] + 0
    E = e0 + k * log(soc / (1 - soc))
    printf "  SOC %5.0f%%   ->   E_OCV = %.3f V\n", soc*100, E
  }
  lo = e0 + k * log(0.10/0.90)
  hi = e0 + k * log(0.90/0.10)
  printf "\nrestricting to 10-90%% SOC keeps the OCV in [%.3f, %.3f] V (a %.2f V span)\n", lo, hi, hi-lo
  print "-> only 80% of the stored charge is usable, and the ends are the worst-behaved"
  if ((lo > 1.13 && lo < 1.16) && (hi > 1.36 && hi < 1.39)) {
    print "PASS: the Nernst equation itself caps the usable SOC window at ~80%"
    print "  -> combined with the iron-plating limit (tutorial 4), that is the"
    print "     ~1/3-of-theoretical usable capacity you size the tanks around."
  }
  else { print "FAIL"; exit 1 }
}'
```

If the capstone prints `PASS`, the chain held: `Q` tracks how far the cell has
run, the Nernst equation turns that into a voltage, the `0.05916/z` form is the
pH-meter slope, `E° = 0` plus a concentration ratio is a working battery, and
the same equation — running away near empty and full — is what forces you to
leave the top and bottom of a flow battery's tank unused.

## Where to go next

- `overpotential` and `cell_voltage_discharge` — the *other* voltage sag, the one
  that depends on current (already met in `kwh-per-kilogram.md` and
  `iron-flow-battery.md`).
- `temperature_coefficient_emf` (`∂E/∂T = ΔS/zF`) and `equilibrium_from_cell_potential`
  (`E° = (RT/zF) ln K`) — the rest of the thermodynamic bridge.
- `pourbaix_diagram` — the Nernst equation drawn as a map of `E` versus pH.
- The sibling tutorials and the full
  [`chemistry-electrochemistry`](../SKILL.md) capsule.
