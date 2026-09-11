# Are a Megaphone and a Long-Range Microphone the Same Thing?

> Generated from the `physics-acoustics` capsule (Release 0.1) with the
> `formula-tree-tutorial` skill. The physics, the prerequisite order, and
> every calculation come from that capsule.

## How to run this

Install `upmd` (https://upmd.dev), then run `upmd horns-and-reciprocity.md`
for the interactive walk, or `upmd --ci --all horns-and-reciprocity.md` to
run every calculation top to bottom. Each section ends with a code block
you run yourself; `upmd --ci -b capstone horns-and-reciprocity.md` runs the
full chain.

## What you need first

The speed of sound as a known number (from
[`how-fast-does-sound-travel.md`](how-fast-does-sound-travel.md)) and the
idea of a pressure reflection coefficient at an impedance boundary —
`physics-acoustics/nodes/reflection_coefficient_normal_incidence.md`
covers it, and this tutorial reuses its worked air/water numbers directly.

---

## 0. Setup

```bash [name:setup]
export c=343          # m/s, speed of sound in air
export z_air=415      # Pa*s/m, characteristic impedance of air
export z_water=1480000  # Pa*s/m, characteristic impedance of water
echo "c=$c m/s, z_air=$z_air, z_water=$z_water Pa*s/m"
```

## 1. Reciprocity: can you swap source and receiver?

For any **linear, passive** acoustic system — no amplifiers, no nonlinear
distortion, nothing actively pumping energy in — the **acoustic reciprocity
theorem** says the pressure a source at point A produces at point B equals
the pressure an equal source at B would produce at A. Swap source and
receiver, and the transfer function between them doesn't change.

This is a structural fact about the wave equation being linear (so
solutions superpose) and self-adjoint (so the roles of "cause" and
"measurement point" are interchangeable in the governing math) — it holds
for a horn, a parabolic dish, an open room, anything passive.

A clean instance of it: the **power** transmission coefficient across an
impedance boundary, `tau = 1 - R^2` where `R = (z2-z1)/(z2+z1)`, doesn't
care which side you call the source. Swapping `z1` and `z2` flips the sign
of `R` but not `R^2`:

```bash [name:chk_reciprocity, deps:setup]
r_12=$(echo "scale=8; ($z_water - $z_air) / ($z_water + $z_air)" | bc -l)
r_21=$(echo "scale=8; ($z_air - $z_water) / ($z_air + $z_water)" | bc -l)
tau_12=$(echo "scale=8; 1 - $r_12 * $r_12" | bc -l)
tau_21=$(echo "scale=8; 1 - $r_21 * $r_21" | bc -l)
echo "power transmission, air treated as source side:   $tau_12"
echo "power transmission, water treated as source side: $tau_21"
echo "difference (should be exactly 0):"
echo "$tau_12 - $tau_21" | bc -l
```

Zero difference — the coupling efficiency between air and water doesn't
know or care which side you call "source." That's why the same horn shape
works as a megaphone (concentrate a diaphragm's output) and as an ear
trumpet (concentrate incoming sound onto an ear): reciprocity guarantees
identical performance run in either direction.

## 2. But a horn and a dish don't work the same way

Reciprocity says a horn *run backwards* behaves the same. It says nothing
about whether a **horn** and a **parabolic dish** are the same kind of
device — and they aren't:

- A **horn** solves an *impedance-matching* problem. A small vibrating
  diaphragm has high acoustic impedance (it's stiff and light); open air
  has low impedance (2 orders of magnitude lower, similar to the air/water
  gap you just computed, though smaller). A horn's flaring shape tapers one
  into the other gradually, so far less sound reflects back at the throat
  and far more actually leaves as a radiated wave. This is a **near-field**
  problem, governed by the **Webster horn equation**, and it's exactly
  analogous to the impedance-boundary calculation above, except continuous
  instead of a single step.
- A **parabolic dish** (a "shotgun" or dish microphone) solves a
  *geometric focusing* problem instead — it reflects a wide incoming
  wavefront to a single point, the same principle as a satellite dish or a
  reflecting telescope. This is a **far-field, diffraction-limited**
  problem: the dish only focuses well when its diameter is large compared
  to the wavelength, which is why dish microphones are notoriously poor at
  bass (long wavelengths) and have to be physically large. **This capsule
  doesn't cover diffraction or 3-D directivity** (see `scope.md`'s
  exclusions), so this tutorial stops at "here's why they're different,"
  not "here's the dish gain formula."

## 3. The Webster horn equation and its cutoff

For a duct whose cross-section `S(x)` flares slowly (slowly compared to
the wavelength), the plane-wave pressure obeys
**`d/dx(S dp'/dx) + (omega/c)^2 S p' = 0`** — the ordinary 1-D wave
equation with one extra term carrying the geometry. Set `S` constant and
it collapses back to the plain wave equation from
[`designing-an-organ-pipe.md`](designing-an-organ-pipe.md).

The one shape with a clean closed-form answer is the **exponential horn**,
`S(x) = S0 e^(2mx)` (flare constant `m`). Substituting a traveling-wave
guess gives a modified dispersion relation, `k^2 = (omega/c)^2 - m^2` —
compare this to the plain `omega = ck` from the pipe tutorial: here, `k` is
only *real* (the wave actually propagates) when `omega > m c`. Below that,
the wave decays exponentially with distance instead of radiating. That
threshold is the horn's **cutoff frequency**:

**`f_c = m c / (2 pi)`**

— an exponential horn is a high-pass filter. This is *why* horn
loudspeakers have a minimum usable frequency set by how fast they flare,
and why a longer, more gradually-flaring horn (a lower `m`) reaches lower
bass notes, at the cost of a much bigger horn.

```bash [name:chk_exponential_horn, deps:setup]
m_flare=2   # 1/m, a moderately fast flare rate
pi=$(echo "scale=10; 4*a(1)" | bc -l)
f_cutoff=$(echo "scale=4; $m_flare * $c / (2 * $pi)" | bc -l)
echo "flare constant m = $m_flare /m"
echo "cutoff frequency: $f_cutoff Hz"
echo "(below this, the horn attenuates instead of radiating)"
```

`m=2` gives a cutoff around 109 Hz — a realistic bass-horn figure; real
horn loudspeakers typically cut off somewhere in the 40–150 Hz range
depending on how gradually they flare.

---

## Capstone: how much does a longer horn buy you?

Since `f_c = m c / (2 pi)`, a **lower** cutoff (more bass) needs a
**smaller** `m` — a more gradual flare, which means a longer horn for the
same mouth size. Compare two flare rates: the `m=2` horn above, and a
gentler `m=0.5` horn aimed at reaching further into the bass.

```bash [name:capstone, deps:"chk_reciprocity | chk_exponential_horn"]
pi=$(echo "scale=10; 4*a(1)" | bc -l)
for m_flare in 2 0.5; do
  f_cutoff=$(echo "scale=4; $m_flare * $c / (2 * $pi)" | bc -l)
  echo "flare constant m=$m_flare /m  ->  cutoff $f_cutoff Hz"
done
echo ""
echo "a 4x gentler flare buys roughly a 4x lower cutoff --"
echo "f_c is directly proportional to m, so halving the flare rate"
echo "roughly halves the lowest usable frequency, at the cost of"
echo "a horn that has to be roughly that much longer to reach it."
```

That's the whole trade-off horn-loudspeaker designers live with, in one
formula: bass extension is free in principle, but it costs you length.

## Where to go next

- The full `physics-acoustics` capsule: `skills/physics-acoustics/` — the
  reflection/transmission-coefficient node this tutorial's reciprocity
  check reuses, plus intensity, decibels, and more.
- [`how-fast-does-sound-travel.md`](how-fast-does-sound-travel.md) and
  [`designing-an-organ-pipe.md`](designing-an-organ-pipe.md): the two
  tutorials this one builds on.
- Not covered here, and not yet in the capsule: parabolic-dish directivity
  and diffraction-limited focusing (the actual mechanism behind a
  long-range "shotgun" microphone) — a genuinely different, harder problem
  than horn impedance-matching, flagged in `scope.md` as excluded rather
  than silently conflated with the horn case.
