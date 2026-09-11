---
name: physics-acoustics
description: Linear (small-signal) acoustics in fluids as a curated, dependency-ordered knowledge capsule -- the floor physics-thermoacoustics needs and previously lacked. The linearized continuity and Euler equations, the adiabatic bulk modulus, the speed of sound (general thermodynamic and ideal-gas forms), the linear acoustic wave equation, plane-wave solutions and the dispersion relation, specific and characteristic impedance, intensity and the decibel scale, superposition/interference/standing waves/pipe resonance, normal-incidence reflection and transmission, and the Doppler effect. Every formula carries its symbols, SI units, dimensions, exactness label, assumptions as first-class graph nodes, one limiting-case check, failure modes, and a source. Built with the physics-formula-tree method; its roots are discharged against physics-newtonian and physics-thermodynamics by physics-formula-atlas in the same release, rather than left as undischarged duplicates. Use when solving or checking a linear-acoustics problem (wave speed, impedance, SPL, resonance, Doppler shift), when you need the minimum prerequisite chain for an acoustics formula, or when tracing a physics-thermoacoustics result's full dependency chain back to Newtonian/thermodynamic primitives via physics-formula-atlas.
---

# physics-acoustics

Linear (small-signal) acoustics in fluids — the floor
[`physics-thermoacoustics`](../physics-thermoacoustics/SKILL.md) assumed in
prose but never had a real capsule for; `small_amplitude` and
`time_harmonic` were re-declared there as unlinked roots (see
`physics-formula-atlas/validation/duplicate-primitives.md`). Read
[`scope.md`](scope.md) first.

## What's here

Continuity + linearized Euler + the adiabatic bulk modulus → the linear
acoustic wave equation → plane-wave solutions and the dispersion relation
→ impedance, intensity, the decibel scale → superposition, standing waves,
pipe resonance → reflection/transmission at an impedance mismatch → the
Doppler effect. 50 nodes, 85 `tsort` edges, acyclic, 7 genuine roots.

Explicitly **inviscid** — viscosity and thermal dissipation are
`physics-thermoacoustics`'s territory, kept out here so the two capsules
don't duplicate content (see `scope.md`'s exclusions).

## Discharged from the start

Built after [`physics-formula-atlas`](../physics-formula-atlas/SKILL.md)
existed, so every genuine root here (`real_numbers`, `length`, `mass`,
`time`, `SI_units`, `gas_constant`, `heat_capacity_ratio`) — and two further
local copies that aren't roots but are still pure duplicates
(`newton_second_law`, `ideal_gas_law`) — got a cross-capsule discharge edge
into `physics-newtonian`/`physics-thermodynamics` in the same session,
rather than sitting undischarged the way `physics-thermodynamics`'s and
`physics-thermoacoustics`'s roots did before the atlas existed. Only
`mean_density` stays genuinely capsule-local (no `density` node exists
anywhere in `physics-thermodynamics`).

```sh
python3 ../physics-formula-atlas/build/prereq-path.py physics-acoustics:acoustic_wave_equation_1d --roots-only
# -> 8 physics-newtonian primitives, crossing two capsule boundaries
```

## Build and verify

```sh
sh build/all.sh                        # graph -> tsort -> bc
sh build/build-tree.sh                 # 50 nodes, 85 edges, acyclic, 7 roots
bc -q -l validation/instance-checks.bc  # speed of sound, dispersion, SPL, pipe resonance, Doppler, reflection
```

## Release 0.1 at a glance

50 nodes (18 roots/local-floor copies, 32 native acoustics content), 85
`tsort` edges, acyclic, 0 isolated, 7 genuine capsule-local roots (all 7
discharged against `physics-newtonian`/`physics-thermodynamics` — see
above). No Lean cores this release — proofs are algebraic derivations
worked in each node entry and `bc`-checked at concrete instances (same
proof-policy call `bayes-bridge` made).

## Method verification (Release 0.1)

| Stage | Tool | Result |
|---|---|---|
| graph + sort | GNU `tsort` | 50 nodes, 85 edges, **acyclic**; every edge respected; 0 isolated, 7 roots |
| instances | GNU `bc` 7.0.3 | clean run: speed of sound in dry air (343.25 m/s), the dispersion relation, SPL at 2 Pa (≈100 dB), pipe resonance (343 Hz / 171.5 Hz), Doppler shift (767/644 Hz), air-water reflection coefficient (0.9994) — `validation/instance-checks.md` |
| cross-capsule discharge | `physics-formula-atlas` | all 7 roots + 2 non-root duplicates discharged; combined atlas graph 289 nodes / 730 edges, `tsort`-clean |

Full results: `validation/instance-checks.md`.
