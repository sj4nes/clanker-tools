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

## Status
`bc` 7.0.3 (GNU), `-q -l`, scale set explicitly per block. Ran clean, no
errors.
