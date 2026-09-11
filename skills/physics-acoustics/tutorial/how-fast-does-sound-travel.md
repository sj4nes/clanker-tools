# How Fast Does Sound Travel?

> Generated from the `physics-acoustics` capsule (Release 0.1) with the
> `formula-tree-tutorial` skill. The physics, the prerequisite order, and
> every calculation come from that capsule.

## How to run this

Install `upmd` (https://upmd.dev), then run `upmd how-fast-does-sound-travel.md`
for the interactive walk, or `upmd --ci --all how-fast-does-sound-travel.md`
to run every calculation top to bottom. Each section ends with a code block
you run yourself; blocks depend on earlier ones, so
`upmd --ci -b chk_speed_of_sound_ideal_gas how-fast-does-sound-travel.md`
runs a single check with its whole dependency chain.

## What you need first

SI units and ordinary algebra — nothing from another capsule tutorial is
assumed. If you want the full derivation this tutorial specializes (why the
speed of sound is `sqrt((dP/drho)_s)` for *any* fluid, not just an ideal
gas), read `physics-acoustics/nodes/` directly; this tutorial takes the
shortest path to one number.

---

## 0. Setup

The equilibrium (mean) state of the air we'll compute through: 20°C dry air
at the values `physics-acoustics/validation/instance-checks.bc` already
validates against the textbook figure.

```bash [name:setup]
export gam=1.4        # heat-capacity ratio for a diatomic gas (air)
export r_gas=8.314     # J/(mol K), the universal gas constant
export temp=293.15     # K, 20 degrees C
export molar_mass=0.02896   # kg/mol, dry air
echo "mean state: T=$temp K, gamma=$gam, R=$r_gas J/(mol K), M=$molar_mass kg/mol"
```

## 1. The mean (equilibrium) state

Every acoustic formula in this capsule describes a small *perturbation* on
top of a background — the **mean pressure** `P0`, **mean density** `rho0`,
and **mean temperature** `T0` the undisturbed air sits at. Sound is what
happens when pressure, density, and velocity wiggle slightly around these
values; without a well-defined background to wiggle around, "small
perturbation" has no meaning. The setup above fixed the one background
quantity this tutorial's path actually needs a number for: `T0 = 293.15 K`.

## 2. The ideal-gas law

The air is modelled as an **ideal gas**: `P V = n R T`, relating pressure,
volume, amount of substance, and temperature through the universal gas
constant `R = 8.314 J/(mol K)`. This is a *constitutive relation* — a
statement about what the fluid *is*, not a law of motion — and it's what
lets the next step trade a fluid-mechanics quantity (compressibility) for a
thermodynamic one (temperature and molar mass) that's easy to look up.

## 3. From compressibility to the speed of sound

A fluid resists being compressed; how strongly it resists is its
**adiabatic bulk modulus** `B_s = rho0 (dP/drho)_s` — "adiabatic" because a
sound wave compresses and expands the gas too fast for heat to flow in or
out. The **speed of sound**, in complete generality, is that resistance per
unit mean density: `c^2 = (dP/drho)_s = B_s / rho0`. This formula is true
for *any* fluid — liquid, gas, or otherwise — with no reference to an ideal
gas at all.

Combine it with the ideal-gas law and the adiabatic condition
(`P V^gamma = const`), and the density dependence cancels, leaving a
formula with no volume or pressure in it at all:

**`c = sqrt(gamma R T0 / M)`**

— the speed of sound in an ideal gas depends on nothing but its
temperature, its heat-capacity ratio, and its molar mass. Hotter air, or a
lighter gas (helium, famously), gives a faster speed of sound; denser air
at the *same temperature* does not slow sound down, which is the
counterintuitive part this derivation earns you.

```bash [name:chk_speed_of_sound_ideal_gas, deps:setup]
echo "scale=6; sqrt($gam * $r_gas * $temp / $molar_mass)" | bc -l
echo "(want approx 343, the textbook figure for dry air at 20C)"
```

The capsule's own `validation/instance-checks.bc` runs this exact
calculation and gets `343.253282` m/s — close enough to the textbook
"343 m/s" that the small gap is just which decimal of `gamma`/`M` a given
textbook rounds to, not a different formula.

---

## Capstone: how far away was that lightning strike?

Thunder and lightning happen at (as far as you'll ever notice) the same
instant; the *delay* you hear is entirely the time sound takes to cross the
distance light crossed instantly. With `c` from above, "count the seconds
between flash and thunder, divide by `c`" gives the distance directly — the
classic rule of thumb ("five seconds per mile") is just this formula with
American units baked in.

```bash [name:capstone, deps:chk_speed_of_sound_ideal_gas]
c=$(echo "scale=6; sqrt($gam * $r_gas * $temp / $molar_mass)" | bc -l)
delay=5   # seconds counted between the flash and the thunder
echo "speed of sound: $c m/s"
echo "scale=1; $c * $delay" | bc -l
echo "(distance in meters for a 5-second flash-to-thunder delay)"
```

A 5-second delay puts the strike about 1.7 km away — and every extra second
you count is another ~343 m, which is exactly why the rule of thumb works
at all: `c` barely changes with the small day-to-day temperature swings
that change `T0` by a few percent.

## Where to go next

- The full `physics-acoustics` capsule: `skills/physics-acoustics/` — the
  linearized continuity and Euler equations `c` comes from, the wave
  equation, impedance, intensity, and more.
- The next tutorial, [`designing-an-organ-pipe.md`](designing-an-organ-pipe.md),
  picks up exactly where this one ends: it takes `c` as a known constant and
  asks what length of pipe resonates at a chosen musical note.
- Not covered here: the decibel scale (`decibel_spl`), the Doppler effect
  (`doppler_general`), and reflection/transmission at an impedance mismatch
  — all in the capsule, all with their own `bc`-verified worked instances in
  `validation/instance-checks.md`, waiting for a future tutorial.
