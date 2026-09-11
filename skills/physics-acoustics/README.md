# physics-acoustics

**Status: Release 0.1 built (2026-09-11).**

Linear (small-signal) acoustics in fluids, built with the
[`physics-formula-tree`](../physics-formula-tree/SKILL.md) method — the
floor [`physics-thermoacoustics`](../physics-thermoacoustics/SKILL.md)
assumed in prose but had no real capsule for.

Read [`SKILL.md`](SKILL.md) then [`scope.md`](scope.md).

## Tutorials

Interactive, `upmd`-executable walkthroughs (run
`upmd --ci --all <file>.md` or install [upmd](https://upmd.dev) for the
interactive walk):

- [`tutorial/how-fast-does-sound-travel.md`](tutorial/how-fast-does-sound-travel.md)
  — the minimal path to `speed_of_sound_ideal_gas`; capstone estimates a
  lightning strike's distance from a thunder delay.
- [`tutorial/designing-an-organ-pipe.md`](tutorial/designing-an-organ-pipe.md)
  — continuity + Euler → the wave equation → the dispersion relation →
  pipe resonance; capstone designs a pipe length for concert A (440 Hz).
- [`tutorial/horns-and-reciprocity.md`](tutorial/horns-and-reciprocity.md)
  — acoustic reciprocity, the Webster horn equation, and an exponential
  horn's cutoff frequency; capstone compares two flare rates' bass
  extension. Answers "are a megaphone and a long-range microphone
  symmetric devices?"

## Quick start

```sh
sh build/all.sh
python3 ../physics-formula-atlas/build/prereq-path.py physics-acoustics:acoustic_wave_equation_1d
```

## Why

`physics-formula-atlas`'s discharge audit found `physics-thermoacoustics`
re-declaring `small_amplitude` and `time_harmonic` — genuinely acoustic
concepts — as its own disconnected roots, because no acoustics capsule
existed to develop them. This capsule is that floor: continuity + Euler +
the bulk modulus → the wave equation → plane waves, impedance, intensity,
decibels, resonance, reflection/transmission, Doppler.

## What's next

`physics-thermoacoustics`'s own registry is untouched by this release — it
still carries its own local `small_amplitude`/`time_harmonic` roots rather
than citing this capsule directly. A natural follow-up: extend
`physics-formula-atlas`'s cross-capsule edges to discharge
`physics-thermoacoustics`'s remaining acoustics-adjacent roots
(`small_amplitude`, `time_harmonic`) against this capsule's nodes of the
same name.
