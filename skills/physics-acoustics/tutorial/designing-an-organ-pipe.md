# Designing an Organ Pipe

> Generated from the `physics-acoustics` capsule (Release 0.1) with the
> `formula-tree-tutorial` skill. The physics, the prerequisite order, and
> every calculation come from that capsule.

## How to run this

Install `upmd` (https://upmd.dev), then run `upmd designing-an-organ-pipe.md`
for the interactive walk, or `upmd --ci --all designing-an-organ-pipe.md` to
run every calculation top to bottom. Each section ends with a code block you
run yourself; blocks depend on earlier ones, so
`upmd --ci -b capstone designing-an-organ-pipe.md` runs the full chain.

## What you need first

The speed of sound as a known number — worked out from scratch in
[`how-fast-does-sound-travel.md`](how-fast-does-sound-travel.md). This
tutorial starts from `c ≈ 343 m/s` and asks a different question: not "how
fast is sound," but "what length of pipe makes a chosen note."

---

## 0. Setup

```bash [name:setup]
export c=343   # m/s, speed of sound in air at 20C (see the speed-of-sound tutorial)
echo "speed of sound: $c m/s"
```

## 1. From Newton's second law to a wave equation

Two linearized fluid equations, both direct consequences of ideas you
already know, combine into the wave equation:

- **Linearized continuity**: mass isn't created or destroyed, so a local
  buildup of density (`d(rho')/dt`) must come from fluid flowing in faster
  than it flows out (`rho0 * du/dx`).
- **Linearized Euler's equation**: this *is* `F = ma` for a fluid element —
  a pressure gradient (`-dp'/dx`) accelerates the fluid it's pushing on
  (`rho0 * du/dt`).

Eliminating the particle velocity `u` between these two, using the speed of
sound to relate pressure and density changes, leaves one equation in `p'`
alone: **`d^2(p')/dt^2 = c^2 d^2(p')/dx^2`** — the **linear acoustic wave
equation**. Every result in this tutorial is downstream of this one line.

## 2. Plane waves and the dispersion relation

Try a traveling-wave guess, `p'(x,t) = A cos(kx - omega t + phi)`, in the
wave equation, and it only works — the guess only solves the equation — for
one particular relationship between the wavenumber `k` and the angular
frequency `omega`: **`omega = c k`**, the **dispersion relation**. This is
the capsule's `dispersion_relation` node, and it's the fact that a sound
wave's speed doesn't depend on its frequency (unlike, say, water waves) —
concert A and a foghorn travel at the same 343 m/s.

```bash [name:chk_dispersion_relation, deps:setup]
f=1000  # Hz, an arbitrary test frequency
scale=6
lambda=$(echo "scale=6; $c / $f" | bc -l)
pi=$(echo "scale=10; 4*a(1)" | bc -l)
k=$(echo "scale=6; 2 * $pi / $lambda" | bc -l)
omega=$(echo "scale=6; 2 * $pi * $f" | bc -l)
echo "lambda = $lambda m, k = $k rad/m, omega = $omega rad/s"
echo "omega - c*k (should be ~0):"
echo "scale=6; $omega - $c * $k" | bc -l
```

The near-zero result (a small truncation artifact from `lambda`'s finite
`scale`, not a real discrepancy) confirms `omega = c k` at a concrete
frequency — the same check `physics-acoustics/validation/instance-checks.bc`
runs.

## 3. Standing waves in a pipe

A single traveling wave doesn't resonate — it just passes through. A **pipe
of finite length** reflects the wave at each end, and the superposition of
the original wave and its reflection is a **standing wave**: a pattern
fixed in space (nodes and antinodes at fixed positions) oscillating in
time, rather than a pattern that travels. A pipe only supports a standing
wave — only *resonates* — at frequencies where a whole number of half- or
quarter-wavelengths fits exactly between its ends, set by the boundary
condition at each end:

- **Both ends the same type** (open-open, so pressure is forced to a node
  at both ends, or closed-closed, so pressure is free to be an antinode at
  both ends): resonances at **`f_n = n c / (2L)`**, every integer `n`.
- **One end open, one end closed**: only the *odd* harmonics fit, at
  **`f_n = (2n-1) c / (4L)`** — half the spacing of the symmetric case,
  which is why a clarinet (effectively closed-open) sounds an octave lower
  than a flute (effectively open-open) of the same length.

```bash [name:chk_pipe_resonance, deps:chk_dispersion_relation]
pipe_len=0.5   # m
echo "pipe length: $pipe_len m"
f1_symmetric=$(echo "scale=4; $c / (2 * $pipe_len)" | bc -l)
f1_mixed=$(echo "scale=4; $c / (4 * $pipe_len)" | bc -l)
echo "fundamental, open-open or closed-closed: $f1_symmetric Hz"
echo "fundamental, one open one closed:        $f1_mixed Hz"
echo "(want 343 Hz and 171.5 Hz)"
```

That matches `physics-acoustics/validation/instance-checks.bc`'s worked
0.5 m pipe exactly, and the mixed-boundary fundamental coming out at half
the symmetric one is the "clarinet vs. flute" fact stated above, not a
separate coincidence.

---

## Capstone: what length pipe plays concert A?

Rearrange the symmetric-boundary formula for the length instead of the
frequency — `L = c / (2f)` — and you can *design* a resonator instead of
just analyzing one. Concert A is 440 Hz.

```bash [name:capstone, deps:chk_pipe_resonance]
target_f=440   # Hz, concert A
echo "target note: $target_f Hz"
len_symmetric=$(echo "scale=4; $c / (2 * $target_f)" | bc -l)
len_mixed=$(echo "scale=4; $c / (4 * $target_f)" | bc -l)
echo "open-open or closed-closed pipe length: $len_symmetric m"
echo "one-open-one-closed pipe length:        $len_mixed m"
echo "(the closed-open pipe is half the length for the same note --"
echo " the physical reason a clarinet body is shorter than a flute"
echo " body for the same fundamental pitch)"
```

An open-open (or closed-closed) pipe for concert A comes out to about
0.39 m; a one-open-one-closed pipe reaches the same pitch at about 0.195 m
— half the length, for the reason worked out in section 3.

## Where to go next

- The full `physics-acoustics` capsule: `skills/physics-acoustics/` —
  impedance, intensity, reflection/transmission at a boundary, and more.
- [`how-fast-does-sound-travel.md`](how-fast-does-sound-travel.md), if you
  arrived here first: derives the `c` this tutorial takes as given.
- Not covered here: `interference` (two arbitrary sources, not just a
  pipe's own reflection), `specific_acoustic_impedance` /
  `characteristic_impedance`, `acoustic_intensity`, `decibel_spl`, the
  Doppler effect, and `reflection_coefficient_normal_incidence` /
  `transmission_coefficient_normal_incidence` — all in the capsule, all
  `bc`-verified in `validation/instance-checks.md`, left for a future
  tutorial.
