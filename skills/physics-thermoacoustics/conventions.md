# Conventions and foundational choices

## Dimensional basis

This release uses **four** SI base dimensions: `[M, L, T, Θ]` (mass, length,
time, thermodynamic temperature). Current, amount of substance, and luminous
intensity do not appear. Key derived dimensions:

| Quantity | Symbol | SI unit | `[M L T Θ]` |
|---|---|---|---|
| Pressure | p | Pa | `M L^-1 T^-2` |
| Density | ρ | kg/m³ | `M L^-3` |
| Velocity | u | m/s | `L T^-1` |
| Specific gas constant / specific heat | R, c_p, c_v | J/(kg·K) | `L^2 T^-2 Θ^-1` |
| Dynamic viscosity | μ | Pa·s | `M L^-1 T^-1` |
| Kinematic viscosity / thermal diffusivity | ν, α | m²/s | `L^2 T^-1` |
| Thermal conductivity | k | W/(m·K) | `M L T^-3 Θ^-1` |
| Angular frequency / frequency | ω, f | rad/s, Hz | `T^-1` |
| Wavenumber | κ_w | rad/m | `L^-1` |
| Specific acoustic impedance | z | Pa·s/m | `M L^-2 T^-1` |
| Volume flow rate | U | m³/s | `L^3 T^-1` |
| Acoustic power / energy flux | Ẇ, Ḣ, Q̇ | W | `M L^2 T^-3` |
| Temperature gradient | ∇T_m | K/m | `Θ L^-1` |

## Notation

- **Phasor:** every first-order field is `q(x,t) = Re[ q_1(x) e^{+iωt} ]` with
  `q_1(x)` complex. `q_1*` is the complex conjugate. `|q_1|` is the amplitude.
- **Time average** over one acoustic period: `⟨A B⟩ = ½ Re[A_1 B_1*]` for two
  first-order quantities. Energy flows (`Ẇ`, `Ḣ_2`, `Q̇_2`) are second order and
  written with a subscript 2 following Swift.
- **Mean (zeroth-order) quantities** carry subscript `m`: `p_m`, `ρ_m`, `T_m`.
  They are treated as slowly varying in `x` (only `T_m` and quantities built from
  it vary along the stack at leading order).
- `x` is the axial coordinate, increasing from the **cold** end to the **hot**
  end. `A` (or `A_gas`) is the gas cross-sectional area; `Π` the wetted
  perimeter; `r_h = A_gas/Π` the hydraulic radius.
- Wavenumber is written `κ_w` in prose to avoid collision with thermal
  conductivity `k` and thermal diffusivity; node id is `wavenumber`.
- `γ = c_p/c_v`; `Pr = ν/α` (Prandtl number, `~0.7` for air, `~0.68` for helium).
- Penetration depths: `δ_κ = sqrt(2α/ω)` (thermal), `δ_ν = sqrt(2ν/ω)` (viscous).

## Foundational primitive choices

Accepted as **primitive for Release 0.1** (documented, not derived here):

| Node | Why primitive here | Omitted alternative |
|---|---|---|
| `real_numbers`, `complex_numbers`, `derivative`, `partial_derivative`, `integral`, `ordinary_differential_equation`, `time_average` | complex phasor calculus assumed known | construction from first principles |
| `time`, `position` | metric coordinates of a lab frame | relativistic / curvilinear |
| `mean_pressure`, `mean_density`, `mean_temperature` | the zeroth-order thermodynamic state, taken as given operating conditions | deriving the mean state from a full flow solution |
| `mean_temperature_gradient` | **imposed externally** by the heat exchangers — a boundary condition of the linear problem, not solved for | self-consistent gradient from a coupled solid/gas energy balance |
| `dynamic_viscosity`, `thermal_conductivity`, `specific_heat_cp`, `specific_heat_cv` | gas material properties, taken from tables at `(p_m, T_m)` | kinetic-theory derivation |
| `first_law_thermodynamics`, `second_law_thermodynamics`, `entropy`, `adiabatic_process` | elementary thermodynamics assumed (see `physics-newtonian` for mechanics) | axiomatic thermodynamics |

The mechanics prerequisites (`velocity_field`, momentum balance, work, energy)
are inherited from [`physics-newtonian`](../physics-newtonian/SKILL.md) and not
re-derived; `linearized_euler` and `linearized_navier_stokes` are stated as the
governing balances for this release.

## Cycle-resolution decisions

Recorded in `edges/cycles.md`. Summary of the direction choices that keep the
graph acyclic:

- **sound speed ↔ adiabatic process.** `adiabatic_process` is a thermodynamic
  primitive; `adiabatic_sound_speed` (`a = sqrt(γRT)`) derives from it plus the
  linearized equations. No reverse edge.
- **mean temperature gradient ↔ acoustic field.** In the linear theory `dT_m/dx`
  is an *imposed* input; the Rott equations solve the acoustic field *given* it.
  Edge direction: `mean_temperature_gradient → rott_continuity_equation`. There
  is no edge back — "the wave sets up the gradient" is a device-level feedback
  captured only by the `oscillation_onset` and engine nodes.
- **engine ↔ oscillation.** A thermoacoustic engine produces the wave that drives
  it. The linear theory takes the wave as given and asks whether its amplitude
  grows (`oscillation_onset`). So `oscillation_onset` and the engine examples
  *depend on* the wave equation and the energy-flux relations; neither is a
  prerequisite of the acoustic solution.
- **acoustic power ↔ heat flux.** `short_stack_acoustic_power` and
  `short_stack_heat_flux` are both consequences of the same Rott solution;
  neither is a prerequisite of the other. Their coupling (energy conservation
  `dḢ_2/dx = 0` in a lossless duct) is a `bridge`, not a `requires` edge.
- **f functions ↔ Rott equations.** `f_nu` and `f_kappa` are defined from the
  boundary-value solution of the linearized momentum/energy equations across the
  channel; the Rott 1-D equations then *use* them as coefficients. Edges:
  `linearized_navier_stokes → thermoacoustic_function_fnu →
  rott_momentum_equation` (and the `f_kappa` analogue). The full-geometry forms
  are `draft`.

## Model vs law labels

- `linearized_continuity`, `linearized_euler`, `linearized_navier_stokes`,
  `linearized_energy_equation`, `first_law_thermodynamics`,
  `second_law_thermodynamics` → `fundamental_law` **within the linear-acoustics /
  continuum regime** (each node states the ordering assumption).
- `ideal_gas_law` → `constitutive_model`.
- `thermal_expansion_ideal_gas` (`β = 1/T_m`), `adiabatic_sound_speed`,
  `carnot_efficiency`, `carnot_cop`, the penetration depths and their ratio,
  the Rott momentum/continuity/wave equations, the critical temperature
  gradient → `derived_exact` **within their stated assumptions**.
- `boundary_layer_limit_f`, `short_stack_approximation`,
  `short_stack_acoustic_power`, `short_stack_heat_flux` → `approximation`
  (leading order in `δ/r_h` or in stack length / wavelength).
- `ceperley_traveling_wave`, `gas_parcel_cycle` → `bridge` (conceptual link to
  the Stirling cycle).
