# Instance checks — `bc`

Run: `bc -q -l validation/instance-checks.bc`. Output:
`build/instance-checks.out`. A passing instance check is necessary, not
sufficient — it confirms one concrete case, not the general identity.
Identifier convention: all-lowercase (this `bc` build rejects an uppercase
leading letter as a variable name — `R`, `T`, `M`, `L` were renamed to
`r_gas`, `temp`, `molar_mass`, `pipe_len`; `s`, `c`, `l`, `a`, `e` may be
reused as plain variables here since this build lets a scalar assignment
shadow the same-named math-library function).

## speed_of_sound_ideal_gas
Dry air at 20°C (`gamma=1.4, R=8.314 J/(mol K), T=293.15 K,
M=0.02896 kg/mol`): `c ≈ 343.25 m/s`, matching the textbook figure of
343 m/s for dry air at 20°C.

## dispersion_relation
`f=1000 Hz, c=343 m/s`: `lambda=0.343 m`, `k=18.318 rad/m`,
`omega=6283.18 rad/s`; `omega - c*k ≈ 0.00024` (a rounding artifact from
`lambda`'s truncated scale, not a defect — confirms the identity to the
precision used).

## decibel_spl
`p_rms = 2 Pa` (a loud sound, near the threshold of pain) gives
`L_p ≈ 100.0 dB`, the standard reference figure for that pressure.

## pipe_resonance
`L=0.5 m, c=343 m/s`: symmetric-boundary fundamental `343 Hz`
(`c/2L`); mixed-boundary fundamental `171.5 Hz` (`c/4L`) — half the
symmetric case, as the formula requires.

## doppler_general
A 700 Hz source moving at 30 m/s (`c=343 m/s`): `767.09 Hz` heard while
approaching, `643.69 Hz` while receding — the audible siren-pitch-drop
effect, correct direction and rough magnitude.

## reflection_coefficient_normal_incidence
Air (`z₀≈415 Pa·s/m`) against water (`z₀≈1.48×10⁶ Pa·s/m`):
`R ≈ 0.9994` — matches the well-known figure that ~99.9% of acoustic
energy reflects at an air-water interface, the reason sonar and
ultrasound need coupling gel/water immersion rather than working through
air.

## acoustic_reciprocity_theorem
Specialized to one impedance boundary (reusing the reflection check's
air-water values): the power transmission coefficient `tau = 1 - R^2` is
computed once with air as the "source side" (`z1=415, z2=1.48e6`) and once
with water as the "source side" (`z1` and `z2` swapped). Both give
`tau ≈ 0.00112101`; the difference is exactly `0` — because `R` only flips
sign under the swap, and `R^2` doesn't care about sign. This is the general
reciprocity theorem's structural content (source and receiver are
interchangeable) demonstrated on the one case already in the capsule,
not a full proof of the general theorem.

## exponential_horn
Flare constant `m = 2 /m`, `c = 343 m/s`: cutoff frequency
`f_c = m c / (2π) ≈ 109.19 Hz`. Below this frequency the horn's dispersion
relation (`k² = (ω/c)² − m²`) gives an imaginary wavenumber — the wave
decays exponentially instead of propagating, so the horn acts as a
high-pass filter. `109 Hz` is a realistic bass-horn cutoff (real horn
loudspeakers typically cut off somewhere in the 40–150 Hz range depending
on flare rate), a sanity check on the formula, not a claim about any
specific real device.

## Status
`bc` 7.0.3 (GNU), `-q -l`, scale set explicitly per block. Ran clean, no
errors.
