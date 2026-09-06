# Scope — Release 0.1

Knowledge capsule: **linear thermoacoustics** — the coupling of acoustic
oscillations and heat transport that underlies thermoacoustic engines and
refrigerators. Built with the
[`physics-formula-tree`](../physics-formula-tree/SKILL.md) method.

Scoped to track *the theory that produced the most effective real devices*: the
**Rott linear thermoacoustic wave equation** and its regenerator / traveling-wave
limit (Ceperley concept; Backhaus & Swift thermoacoustic-Stirling engine),
with Swift's short-stack boundary-layer analysis of the standing-wave device as
the analytic on-ramp.

## Included

- Continuum + ideal-gas + thermodynamic prerequisites: equation of state,
  `c_p`/`c_v`/`gamma`, adiabatic vs isothermal processes, entropy, the two laws,
  thermal expansion, Carnot efficiency and COP.
- Transport properties: dynamic and kinematic viscosity, thermal conductivity
  and diffusivity, the Prandtl number.
- Linear acoustics of an ideal gas: linearized continuity and Euler equations,
  the wave equation, adiabatic sound speed, plane / standing / traveling waves,
  angular frequency, wavenumber, wavelength, characteristic and specific acoustic
  impedance, volume flow rate, time-averaged acoustic power.
- Thermoacoustic boundary layers: thermal and viscous penetration depths and
  their ratio, hydraulic radius, the stack vs regenerator regimes.
- **Rott's theory:** linearized Navier–Stokes and energy equations with a wall;
  the complex thermoacoustic functions `f_nu`, `f_kappa` (and their
  boundary-layer limit); the Rott momentum, continuity, and wave equations with
  an imposed mean temperature gradient.
- Energy conversion: total energy flux, thermoacoustic heat flux, the acoustic
  power gradient along `x`, the critical temperature gradient and the ratio
  `Gamma`, the short-stack acoustic-power and heat-flux results, the two
  dissipation mechanisms, entropy generation.
- Devices: standing-wave engine and refrigerator; traveling-wave (Stirling)
  engine and refrigerator; the feedback torus; oscillation onset; thermoacoustic
  efficiency and COP; the Carnot limit and relative-Carnot performance.

## Excluded

- Nonlinear thermoacoustics: acoustic streaming, harmonic generation, turbulence,
  Gedeon streaming, shock formation, amplitude-dependent losses.
- Time-domain / multi-frequency analysis; startup transients beyond the onset
  threshold.
- Numerical device design (DeltaEC) — the method it integrates is in scope; the
  software and its shooting method are not.
- Pulse-tube cryocooler phasor-network details (inertance, orifice, double-inlet)
  beyond noting the family relationship.
- Solid-side heat conduction losses, heat-exchanger effectiveness, and mean-flow
  (combustion-driven, cascade) systems.
- Mixtures, real-gas effects, condensation, plasma, magnetoacoustics.
- Structural / materials / manufacturing considerations.

## Conventions

- **Math level:** complex phasor calculus, ordinary differential equations,
  single-variable + partial derivatives, cycle-averaged integrals.
- **Assumed background:** the [`physics-newtonian`](../physics-newtonian/SKILL.md)
  capsule (kinematics, `F=ma`, work/energy), plus elementary thermodynamics and
  vector calculus.
- **Unit system:** SI, with base dimensions `[M, L, T, Θ]` (temperature added —
  see `conventions.md`).
- **Phasor convention:** `q(x,t) = Re[ q_1(x) e^{+iωt} ]`; `q_1` complex, `x` the
  axial coordinate. Time-average `⟨AB⟩ = ½ Re[A_1 B_1*]`.
- **Sign convention:** `x` increases from the cold end toward the hot end of a
  stack/regenerator; a *positive* mean temperature gradient `dT_m/dx > 0` is
  "hot end in the `+x` direction". Acoustic power `Ẇ` positive in `+x`.
- **Linearity:** all thermoacoustic relations are first order in the acoustic
  amplitude for the fields and second order (cycle-averaged) for energy flows —
  the standard Rott/Swift ordering. Acoustic Mach number `Ma = |u_1|/a << 1`.
- **Derivations:** summarised in node entries; load-bearing algebra machine-checked
  with Lean (`validation/derivation-checks.lean`).
- **Exactness policy:** labels used — `definition`, `mathematical_identity`,
  `fundamental_law`, `derived_exact`, `constitutive_model`, `approximation`,
  `asymptotic_relation`.
- **Audience:** an agent reasoning about thermoacoustic device physics that needs
  each relation's symbols, units, regime of validity, prerequisites, and failure
  modes.

## Release status

`draft` — pipeline run recorded in `validation/`. The intricate Rott coefficient
functions (`f_nu`, `f_kappa` full geometry forms) and the full short-stack
power/flux coefficients are carried at `draft` node status pending a line-by-line
source reconciliation (Swift 2002, ch. 4–5); their *structure* and *dimensions*
are checked. See `README.md`.
