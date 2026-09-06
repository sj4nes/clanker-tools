# Formula entries — Release 0.1

A view generated from and reconciled against the graph. Each entry: statement,
symbols (SI unit, `[M L T Θ]` dimension), exactness label, assumptions,
preconditions, direct prerequisites, one limiting/special case, failure modes,
source. Dimensional checks: `validation/dimensional-checks.bc`. Derivation-step
algebra: `validation/derivation-checks.lean`.

Sources: `Swift2002` = G. W. Swift, *Thermoacoustics: A Unifying Perspective for
Some Engines and Refrigerators*, ASA (2002; 2nd ed. Springer 2017);
`Swift1988` = G. W. Swift, "Thermoacoustic engines," *J. Acoust. Soc. Am.*
**84**, 1145 (1988); `Rott1980` = N. Rott, "Thermoacoustics," *Adv. Appl. Mech.*
**20**, 135 (1980); `Ceperley1979` = P. H. Ceperley, "A pistonless Stirling
engine—the traveling wave heat engine," *JASA* **66**, 1508 (1979);
`BackhausSwift2000` = S. Backhaus & G. W. Swift, "A thermoacoustic-Stirling heat
engine: Detailed study," *JASA* **107**, 3148 (2000).

---

## ideal_gas_law — `p = ρ R T`
- p: pressure, Pa, `M L^-1 T^-2`. ρ: density, kg/m³, `M L^-3`. R: specific gas
  constant, J/(kg·K), `L^2 T^-2 Θ^-1`. T: temperature, K, `Θ`.
- Label: constitutive_model. Assumptions: ideal gas (no intermolecular forces,
  point molecules); applied to the **mean** state `(p_m, ρ_m, T_m)`.
- Prereqs: ideal_gas, mean_pressure, mean_density, mean_temperature,
  gas_constant_specific, SI_units.
- Special case: at fixed `T_m`, `p_m ∝ ρ_m`; used to get `β = 1/T_m` and
  `a² = γ p_m/ρ_m`.
- Failure: high density / low temperature (van der Waals); dissociating or
  reacting gas; near condensation.
- Source: Swift2002 §2.

## heat_capacity_ratio — `γ = c_p / c_v` ; `c_p − c_v = R`
- γ: dimensionless (`1.67` monatomic, `1.4` diatomic). c_p, c_v, R:
  J/(kg·K), `L^2 T^-2 Θ^-1`.
- Label: derived_exact (ideal gas — Mayer's relation).
- Prereqs: specific_heat_cp, specific_heat_cv, gas_constant_specific, ideal_gas.
- Special case: `c_p = γR/(γ−1)`, `c_v = R/(γ−1)` (lean check 1: with γ = 7/5,
  `c_p − c_v = R` and `5 c_p = 7 c_v`).
- Failure: real-gas / temperature-dependent specific heats; vibrational modes
  activating with `T`.
- Source: Swift2002 §2.

## thermal_expansion_ideal_gas — `β = 1 / T_m`
- β: isobaric thermal expansion coefficient, 1/K, `Θ^-1`. T_m: K, `Θ`.
- Label: derived_exact (from `ρ = p/(RT)` at fixed `p`).
- Prereqs: thermal_expansion_coefficient, ideal_gas_law, mean_temperature.
- Special case: makes `∇T_crit` independent of `β` for a gas — substitute to get
  `∇T_crit = ω|p₁|/(ρ_m c_p |u₁|)`.
- Failure: non-ideal gas (`β` then depends on `p` and the compressibility).
- Source: Swift2002 §2.

## carnot_efficiency — `η_C = 1 − T_C / T_H`
- η_C: dimensionless. T_C, T_H: cold/hot reservoir temperatures, K, `Θ`.
- Label: derived_exact (second law, reversible cycle). Precondition: `T_H > T_C`.
- Prereqs: second_law_thermodynamics, mean_temperature.
- Special case: `T_C → T_H` ⇒ `η_C → 0`; `T_C → 0` ⇒ `η_C → 1`.
- Failure: quoting it as achievable — real engines reach a fraction of it;
  irreversible cycles fall short.
- Source: Swift2002 §1.

## carnot_cop — `COP_C = T_C / (T_H − T_C)`  (cooling)
- COP_C: dimensionless, unbounded as `T_H → T_C`. T_C, T_H: K, `Θ`.
- Label: derived_exact. Precondition: `T_H > T_C`.
- Prereqs: second_law_thermodynamics, mean_temperature.
- Special case: relation to Carnot efficiency `COP_C = (1 − η_C)/η_C` (lean
  check 3).
- Failure: treating it as a design target; the heating COP is `COP_C + 1`.
- Source: Swift2002 §1.

## kinematic_viscosity — `ν = μ / ρ_m`
- ν: m²/s, `L^2 T^-1`. μ: dynamic viscosity, Pa·s, `M L^-1 T^-1`. ρ_m: `M L^-3`.
- Label: definition. Prereqs: dynamic_viscosity, mean_density.
- Special case: sets the viscous penetration depth `δ_ν = sqrt(2ν/ω)`.
- Failure: strong density stratification along the stack (`ν` then varies with `x`).
- Source: Swift2002 §3.

## thermal_diffusivity — `α = k / (ρ_m c_p)`
- α: m²/s, `L^2 T^-1`. k: thermal conductivity, W/(m·K), `M L T^-3 Θ^-1`.
  ρ_m c_p: `M L^-1 T^-2 Θ^-1`.
- Label: definition. Prereqs: thermal_conductivity, mean_density, specific_heat_cp.
- Special case: sets the thermal penetration depth `δ_κ = sqrt(2α/ω)`.
- Failure: temperature-dependent `k` over a large `ΔT` across the stack.
- Source: Swift2002 §3.

## prandtl_number — `Pr = ν / α = μ c_p / k`
- Pr: dimensionless (`~0.71` air, `~0.68` helium, `~0.24` He–Xe mixtures used to
  cut viscous loss).
- Label: definition. Prereqs: kinematic_viscosity, thermal_diffusivity.
- Special case: `δ_ν/δ_κ = sqrt(Pr)` (lean check 2). `Pr → 0` would eliminate
  viscous loss relative to thermal contact — the motivation for gas mixtures.
- Failure: none as a definition; the `μ c_p/k` form assumes the same mean state.
- Source: Swift2002 §3.

## adiabatic_sound_speed — `a = sqrt(γ R T_m)`
- a: m/s, `L T^-1`. γ: dimensionless. R: `L^2 T^-2 Θ^-1`. T_m: `Θ`.
- Label: derived_exact (ideal gas; acoustic compressions are adiabatic because
  the cycle is fast compared with thermal diffusion in the free gas).
- Prereqs: adiabatic_process, ideal_gas_law, heat_capacity_ratio,
  mean_temperature, gas_constant_specific.
- Special case: `a² = γ p_m/ρ_m`; the isothermal value `sqrt(RT_m)` is smaller by
  `sqrt(γ)` (Newton's error, Laplace's correction).
- Failure: near a wall within `δ_κ`, propagation is neither adiabatic nor
  isothermal — that intermediate regime *is* thermoacoustics.
- Source: Swift2002 §2.

## acoustic_wave_equation — `∂²p₁/∂t² = a² ∂²p₁/∂x²`
- p₁: acoustic pressure, Pa, `M L^-1 T^-2`. a: `L T^-1`. Free gas, 1-D.
- Label: derived_exact (combine linearized continuity + Euler + adiabatic EOS).
- Assumptions: linearization; inviscid; no wall / boundary layer; uniform mean
  state.
- Prereqs: linearized_continuity, linearized_euler, adiabatic_sound_speed.
- Special case: harmonic solutions give `ω = a k` (dispersionless).
- Failure: inside a stack/regenerator — replaced by the Rott wave equation with
  `f_ν`, `f_κ`, and `dT_m/dx`.
- Source: Swift2002 §2.

## dispersion_relation — `ω = a k`
- ω: rad/s, `T^-1`. a: `L T^-1`. k: wavenumber, rad/m, `L^-1`.
- Label: derived_exact (free gas). Prereqs: acoustic_wave_equation,
  angular_frequency, wavenumber, adiabatic_sound_speed.
- Special case: `λ = 2πa/ω`; a 1 kHz wave in air (`a ≈ 343`) has `λ ≈ 0.34 m`.
- Failure: dissipative or bounded media give a complex `k` (attenuation);
  thermoacoustic ducts have `k = k(x)` through `T_m(x)`.
- Source: Swift2002 §2.

## plane_wave — `p₁(x,t) = P e^{i(ωt − kx)}` , `u₁ = p₁/(ρ_m a)`
- P: complex amplitude, Pa. Travels in `+x` at speed `a`.
- Label: derived_exact (free gas). Prereqs: acoustic_wave_equation,
  dispersion_relation, phasor_notation.
- Special case: `z = p₁/u₁ = ρ_m a` (real) — pure travelling wave carries
  `Ẇ = |P|²/(2ρ_m a)`.
- Failure: reflections make the field a standing/travelling mixture; near sources
  or discontinuities the plane-wave form breaks down.
- Source: Swift2002 §2.

## characteristic_impedance — `z₀ = ρ_m a`
- z₀: Pa·s/m, `M L^-2 T^-1`. Prereqs: mean_density, adiabatic_sound_speed.
- Label: derived_exact. Special case: the specific acoustic impedance of a pure
  travelling wave equals `±z₀`.
- Failure: not the impedance seen in a resonator or a stack — that is
  `z = p₁/u₁`, generally complex.
- Source: Swift2002 §2.

## specific_acoustic_impedance — `z = p₁ / u₁`
- z: Pa·s/m, `M L^-2 T^-1`, generally **complex**. Prereqs: acoustic_pressure,
  acoustic_velocity, characteristic_impedance.
- Label: definition. Special case: `z` real ⇒ travelling-wave phasing, maximum
  power transport; `z` purely imaginary ⇒ standing-wave phasing, zero net power.
- Failure: undefined where `u₁ = 0` (pressure antinode) — use the reciprocal or
  the pair `(p₁, U₁)`.
- Source: Swift2002 §4.

## volume_flow_rate — `U₁ = u₁ A`
- U₁: m³/s, `L^3 T^-1`, complex. u₁: `L T^-1`. A: gas cross-section, m², `L^2`.
- Label: definition. Prereqs: acoustic_velocity, cross_sectional_uniformity.
- Special case: `U₁` (not `u₁`) is continuous across an area change — the natural
  variable for the Rott network equations.
- Failure: non-uniform `A(x)`, or a porous medium where the gas fraction `φ`
  enters (`U₁ = φ u₁ A_frontal`).
- Source: Swift2002 §4.

## acoustic_power — `Ẇ = ½ Re[ p₁ U₁* ]`
- Ẇ: W, `M L^2 T^-3`. p₁: Pa. U₁: m³/s. `*` = complex conjugate.
- Label: derived_exact (cycle time-average of `p·U`).
- Assumptions: single frequency; linear fields; time-average over one period.
- Prereqs: time_average, acoustic_pressure, volume_flow_rate,
  specific_acoustic_impedance.
- Special case: standing wave (`p₁` real, `U₁` imaginary) ⇒ `Ẇ = 0`; travelling
  wave (`p₁`, `U₁` in phase) ⇒ `Ẇ = ½|p₁||U₁|` (lean check 4).
- Failure: multi-frequency fields (cross terms average to zero only for distinct
  harmonics); nonlinear amplitudes.
- Source: Swift2002 §4.

## thermal_penetration_depth — `δ_κ = sqrt(2α/ω)`
- δ_κ: m, `L`. α: `L^2 T^-1`. ω: `T^-1`. The distance heat diffuses in `1/ω` s.
- Label: derived_exact (diffusion length of the oscillatory thermal problem).
- Prereqs: thermal_diffusivity, angular_frequency.
- Special case: air at 300 K, 100 Hz ⇒ `δ_κ ≈ 0.2 mm`. Gas within `~δ_κ` of the
  wall exchanges heat with it over a cycle; gas further away is adiabatic.
- Failure: turbulent or high-amplitude flow (effective diffusivity rises);
  `δ_κ` comparable to the channel — then use the full `f_κ`.
- Source: Swift2002 §3; Rott1980.

## viscous_penetration_depth — `δ_ν = sqrt(2ν/ω)`
- δ_ν: m, `L`. ν: `L^2 T^-1`. The distance momentum diffuses in `1/ω` s.
- Label: derived_exact. Prereqs: kinematic_viscosity, angular_frequency.
- Special case: `δ_ν = δ_κ sqrt(Pr)`, so `δ_ν < δ_κ` for gases.
- Failure: as `δ_κ`.
- Source: Swift2002 §3; Rott1980.

## penetration_depth_ratio — `δ_ν / δ_κ = sqrt(Pr)`
- Dimensionless. Prereqs: thermal_penetration_depth, viscous_penetration_depth,
  prandtl_number.
- Label: derived_exact (`δ_ν²/δ_κ² = ν/α = Pr`, lean check 2).
- Special case: `Pr < 1` ⇒ viscous layer thinner than thermal layer — favourable;
  lowering `Pr` (He–Xe mixtures) is a standard way to cut viscous loss.
- Failure: none — algebraic identity of the two definitions.
- Source: Swift2002 §3.

## hydraulic_radius — `r_h = A_gas / Π`
- r_h: m, `L`. A_gas: open flow area, `L^2`. Π: wetted perimeter, `L`.
- Label: definition. Special case: parallel plates gap `2y₀` ⇒ `r_h = y₀`;
  circular pore radius `r` ⇒ `r_h = r/2`.
- Prereqs: (geometry primitive) — feeds `stack_regime`, `regenerator_regime`,
  and the `f` functions.
- Failure: highly irregular or partly blocked passages.
- Source: Swift2002 §4.

## thermoacoustic_function_fnu — `f_ν(δ_ν, r_h)`  *(draft)*
- f_ν: dimensionless, **complex**, geometry-dependent. Channel-averaged solution
  of the linearized viscous momentum equation across the pore.
- Label: derived_exact (given the geometry) — but the closed forms per geometry
  are carried at draft status pending line-by-line reconciliation with Swift2002
  §4 (parallel plates: `f_ν = tanh[(1+i)y₀/δ_ν] / [(1+i)y₀/δ_ν]`; circular:
  Bessel-function form).
- Assumptions: laminar flow; rigid wall; `r_h` and `δ_ν` the only length scales.
- Prereqs: linearized_navier_stokes, viscous_penetration_depth, hydraulic_radius,
  complex_numbers.
- Special case: `r_h ≫ δ_ν` ⇒ `f_ν → (1−i)δ_ν/(2 r_h) → 0` (boundary-layer
  limit); `r_h ≪ δ_ν` ⇒ `f_ν → 1` (fully viscous / Poiseuille-like).
- Failure: transitional/turbulent oscillatory flow; entrance effects at pore ends.
- Source: Swift2002 §4; Rott1980.

## thermoacoustic_function_fkappa — `f_κ(δ_κ, r_h)`  *(draft)*
- f_κ: dimensionless, **complex**, geometry-dependent. Same functional form as
  `f_ν` with `δ_κ` in place of `δ_ν`. Measures how thermally connected the gas is
  to the wall.
- Label: derived_exact (given geometry); closed forms at draft status.
- Prereqs: linearized_energy_equation, thermal_penetration_depth,
  hydraulic_radius, complex_numbers.
- Special case: `r_h ≫ δ_κ` (stack) ⇒ `f_κ → (1−i)δ_κ/(2 r_h) → 0` (mostly
  adiabatic gas, thin active layer); `r_h ≪ δ_κ` (regenerator) ⇒ `f_κ → 1`
  (gas isothermal with the matrix — the reversible limit).
- Failure: finite solid heat capacity / conductivity (adds a correction factor
  `ε_s`); as `f_ν`.
- Source: Swift2002 §4; Rott1980.

## boundary_layer_limit_f — `f_j ≈ (1 − i) δ_j / (2 r_h)`  *(draft)*
- Leading term of `f_ν`, `f_κ` when the pore is wide, `r_h ≫ δ_j`.
- Label: approximation (first order in `δ_j/r_h`).
- Prereqs: thermoacoustic_function_fnu, thermoacoustic_function_fkappa,
  stack_regime.
- Special case: substituting into the Rott equations gives Swift's short-stack
  boundary-layer results; the real part → viscous/thermal-relaxation dissipation,
  the imaginary part → reactive loading.
- Failure: regenerator (`r_h ≲ δ_j`), where the full `f_j` is needed and
  `Re[f_j]` is not small.
- Source: Swift1988; Swift2002 §4.

## rott_momentum_equation — `dp₁/dx = − iω ρ_m / [ A (1 − f_ν) ] · U₁`
- p₁: Pa. U₁: m³/s. ρ_m: `M L^-3`. A: `L^2`. ω: `T^-1`. f_ν: complex,
  dimensionless. `[dp₁/dx] = M L^-2 T^-2` (dimensional check passes).
- Label: derived_exact — `x`-momentum of the linearized, wall-bounded, laminar,
  single-frequency flow, channel-averaged.
- Assumptions: laminar; no mean flow; single frequency; `f_ν` captures all wall
  viscous effects.
- Prereqs: linearized_navier_stokes, thermoacoustic_function_fnu,
  volume_flow_rate, angular_frequency, mean_density, ordinary_differential_equation.
- Special case: `f_ν → 0` (wide duct) recovers the inviscid `dp₁/dx = −iωρ_m U₁/A`,
  i.e. linearized Euler.
- Failure: turbulence; junctions and area steps (handled by matching conditions,
  not this ODE); very high amplitude.
- Source: Swift2002 §4 (eq. for `dp₁/dx`); Rott1980.

## rott_continuity_equation *(draft)*
`dU₁/dx = − iωA[1 + (γ−1) f_κ] / (γ p_m) · p₁ + (f_κ − f_ν) / [(1 − f_ν)(1 − Pr)] · (1/T_m)(dT_m/dx) · U₁`
- Combines linearized continuity with the energy equation carrying the imposed
  mean temperature gradient. Second term is the thermoacoustic coupling.
- Label: derived_exact; carried draft pending term-by-term source reconciliation
  (Swift2002 §4).
- Assumptions: ideal gas; single frequency; no mean flow; `dT_m/dx` imposed.
- Prereqs: linearized_continuity, linearized_energy_equation,
  thermoacoustic_function_fkappa, thermoacoustic_function_fnu,
  heat_capacity_ratio, mean_pressure, mean_temperature_gradient, prandtl_number,
  ordinary_differential_equation.
- Special case: `dT_m/dx = 0`, `f_κ → 0` ⇒ `dU₁/dx = −iωA p₁/(γ p_m)` (linearized
  continuity for adiabatic gas); with the momentum equation this gives the free
  wave equation `d²p₁/dx² = −(ω²/a²) p₁` (lean check 6).
- Failure: as the momentum equation; also breaks if `Pr → 1` in the written form
  (the coupling term needs the `Pr = 1` limit taken carefully).
- Source: Swift2002 §4; Rott1980.

## rott_wave_equation *(draft)*
- Second-order ODE for `p₁(x)` obtained by eliminating `U₁` between the Rott
  momentum and continuity equations; coefficients depend on `f_ν`, `f_κ`,
  `dT_m/dx`, and the mean state.
- Label: derived_exact; draft (inherits the continuity-equation status).
- Prereqs: rott_momentum_equation, rott_continuity_equation,
  ordinary_differential_equation.
- Special case: uniform `T_m`, `f_ν = f_κ = 0` ⇒ `d²p₁/dx² + (ω/a)² p₁ = 0`.
- Failure: as its constituents; numerical integration (DeltaEC's shooting method)
  is the practical solver — out of scope here.
- Source: Rott1980; Swift2002 §4.

## critical_temperature_gradient — `∇T_crit = ω |p₁| / (ρ_m c_p |u₁|)`
- ∇T_crit: K/m, `Θ L^-1`. ω: `T^-1`. |p₁|: Pa. ρ_m: `M L^-3`. c_p:
  `L^2 T^-2 Θ^-1`. |u₁|: `L T^-1`. (dimensional check passes.)
- Label: derived_exact (standing-wave phasing, ideal gas via `β = 1/T_m`).
  It is the mean gradient at which a gas parcel's adiabatic temperature
  oscillation exactly matches the local mean-temperature change over its
  displacement — no net heat exchange with the wall.
- Assumptions: standing-wave phasing; short stack; boundary-layer limit; ideal
  gas.
- Prereqs: acoustic_pressure, acoustic_velocity, angular_frequency, mean_density,
  specific_heat_cp, thermal_expansion_ideal_gas, standing_wave_phasing.
- Special case: `∇T_m = ∇T_crit` ⇒ the stack neither produces nor absorbs
  acoustic power (lean check 5).
- Failure: travelling-wave phasing (different expression); large amplitude;
  non-ideal gas (keep the `β T_m` factor).
- Source: Swift1988; Swift2002 §4.

## temperature_gradient_ratio — `Γ = ∇T_m / ∇T_crit`
- Γ: dimensionless. Prereqs: mean_temperature_gradient,
  critical_temperature_gradient.
- Label: definition. Special case: `Γ > 1` → engine (net acoustic power
  produced); `Γ = 1` → neutral; `Γ < 1` → refrigerator (net acoustic power
  absorbed, heat pumped up the gradient). (lean check 5.)
- Failure: only meaningful in the short-stack standing-wave picture; the
  travelling-wave engine is not characterised by a single `Γ`.
- Source: Swift1988.

## short_stack_acoustic_power *(draft)*
`ΔẆ₂ ≈ ¼ (δ_κ Π Δx) [ (ω (γ−1) / (γ p_m)) |p₁|² (Γ − 1) − (ω ρ_m / (1 + Pr))(δ_ν/δ_κ) |u₁|² ]`  (schematic, standing wave)
- Acoustic power produced (`+`) or absorbed (`−`) by a short stack: a gain term
  `∝ (Γ − 1)` and a viscous-loss term `∝ |u₁|²`.
- Label: approximation (first order in `δ/r_h` and `Δx/λ`). Draft: the exact
  coefficients need reconciliation with Swift1988 eqs. (60)–(80).
- Assumptions: short stack; boundary-layer limit; standing wave; ideal gas.
- Prereqs: short_stack_approximation, acoustic_power_gradient,
  temperature_gradient_ratio, thermal_penetration_depth.
- Special case: `Γ = 1` and negligible viscosity ⇒ `ΔẆ₂ = 0`.
- Failure: regenerator; long stack; strong `T_m` variation; high amplitude.
- Source: Swift1988; Swift2002 §4.

## short_stack_heat_flux *(draft)*
`Q̇₂ ≈ − ¼ δ_κ Π Δx (ω/a) ... |p₁||u₁| [ Γ − (1 + sqrt(Pr) + Pr)/(1 + sqrt(Pr)) ]`  (schematic)
- Time-averaged heat transported along `x` by the wave in the stack.
- Label: approximation. Draft (as above).
- Prereqs: short_stack_approximation, thermoacoustic_heat_flux,
  temperature_gradient_ratio, thermal_penetration_depth.
- Special case: proportional to the `p₁`–`u₁` product and to the phasing; zero
  for a pure travelling-wave phase in a stack with no gradient.
- Failure: as the acoustic-power result.
- Source: Swift1988; Swift2002 §4.

## thermoacoustic_heat_flux *(draft)* — `Q̇₂ = −½ ρ_m c_p A Re[ ⟨ u₁ T₁* ⟩ ] + (solid/gas conduction)`
- Q̇₂: W, `M L^2 T^-3`. T₁: acoustic temperature, K, `Θ`. (dimensional check
  passes for the leading convective term.)
- Label: derived_exact (definition of the cycle-averaged enthalpy flux); draft
  because the full expression carries `f_κ`, `f_ν` and conduction terms.
- Prereqs: rott_wave_equation, linearized_energy_equation, specific_heat_cp,
  mean_density, time_average, no_mean_flow.
- Special case: in a lossless duct with no stack, `dḢ₂/dx = 0` (energy
  conservation) links `Q̇₂` and `Ẇ₂`.
- Failure: streaming present; multi-frequency; solid-side conduction dominant.
- Source: Swift2002 §4 (total power `Ḣ₂`).

## total_energy_flux *(draft)* — `Ḣ₂ = Ẇ₂ + Q̇₂`
- Ḣ₂: W, `M L^2 T^-3`. The cycle-averaged total energy carried past a plane.
- Label: derived_exact. Draft (inherits `Q̇₂` status).
- Prereqs: rott_wave_equation, acoustic_power, thermoacoustic_heat_flux,
  time_average, no_mean_flow.
- Special case: **`Ḣ₂` is constant along any segment with no heat exchange** —
  the key bookkeeping identity for device analysis. In an engine, `Ḣ₂` in the
  stack equals the heat input at the hot exchanger.
- Failure: side heat leaks; streaming enthalpy flux; radiation.
- Source: Swift2002 §4; BackhausSwift2000.

## oscillation_onset — `acoustic gain(∇T_m) = round-trip losses`
- The threshold mean temperature gradient (or hot-end temperature ratio) at
  which a thermoacoustic engine self-excites: the least-damped acoustic mode of
  the resonator reaches zero net attenuation.
- Label: derived_exact (eigenvalue condition of the Rott wave equation with the
  resonator boundary conditions). Dimensionless when expressed as `T_H/T_C` at
  onset.
- Prereqs: acoustic_power_gradient, dissipation_mechanisms,
  temperature_gradient_ratio, acoustic_resonator.
- Special case: just above onset the amplitude grows exponentially until
  nonlinear saturation (out of scope); standing-wave engines typically need
  `T_H/T_C` well above 1, travelling-wave engines onset closer to 1.
- Failure: predicts only the threshold and small-amplitude growth rate, not the
  steady operating amplitude.
- Source: Swift2002 §5; Rott1980.

## thermoacoustic_efficiency — `η = Ẇ / Q̇_H`
- η: dimensionless. Ẇ: net acoustic power delivered by the engine, W. Q̇_H: heat
  input at the hot exchanger, W.
- Label: definition. Prereqs: total_energy_flux, acoustic_power,
  first_law_thermodynamics.
- Special case: for the Backhaus–Swift travelling-wave engine `η ≈ 0.30`
  (`≈ 0.40 η_C`); standing-wave engines `η ≈ 0.10–0.20`.
- Failure: must state whether `Ẇ` is gross or net of the resonator/load losses,
  and whether `Q̇_H` includes exchanger imperfection.
- Source: BackhausSwift2000; Swift2002 §5.

## thermoacoustic_cop — `COP = Q̇_C / Ẇ`
- COP: dimensionless. Q̇_C: heat lifted from the cold load, W. Ẇ: acoustic power
  input, W.
- Label: definition. Prereqs: total_energy_flux, acoustic_power,
  first_law_thermodynamics.
- Special case: relative COP `COP/COP_C` of good thermoacoustic refrigerators
  `≈ 0.2–0.4`; pulse-tube cryocoolers (same family) reach higher at their design
  point.
- Failure: as efficiency — define the control volume and which losses are inside.
- Source: Swift2002 §5.

## relative_carnot_performance — `η_rel = η / η_C`  (or `COP / COP_C`)
- Dimensionless, in `[0, 1]` for any real device (second law).
- Label: derived_exact. Prereqs: thermoacoustic_efficiency, carnot_efficiency,
  carnot_limit.
- Special case: the honest figure of merit for comparing devices across
  different `T_H/T_C`; `η_rel → 1` only for a reversible machine.
- Failure: comparing raw `η` across different temperature spans is misleading —
  always normalise.
- Source: Swift2002 §1, §5.
