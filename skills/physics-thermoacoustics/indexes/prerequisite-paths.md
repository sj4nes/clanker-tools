# Minimal prerequisite paths (Release 0.1)

Derived from the graph structure (transitive closure of
`edges/dependencies.edges`), not the flat `tsort` order. `[A]` marks an
assumption / regime node — required but not "learned". Within a group the
`tsort` order applies.

## adiabatic_sound_speed  `a = sqrt(γRT_m)`
[ideal_gas] · SI_units · mean_pressure · mean_density · mean_temperature ·
gas_constant_specific → ideal_gas_law ·
specific_heat_cp · specific_heat_cv → heat_capacity_ratio ·
first_law_thermodynamics → adiabatic_process
→ **adiabatic_sound_speed**
Do-not-use if: within `δ_κ` of a wall (neither adiabatic nor isothermal).

## thermal_penetration_depth  `δ_κ = sqrt(2α/ω)`
mean_density · specific_heat_cp · thermal_conductivity → thermal_diffusivity ·
[time_harmonic] → angular_frequency
→ **thermal_penetration_depth**
Then `δ_ν` (needs dynamic_viscosity → kinematic_viscosity) and
`δ_ν/δ_κ = sqrt(Pr)`.

## critical_temperature_gradient  `∇T_crit = ω|p₁|/(ρ_m c_p |u₁|)`
everything under adiabatic_sound_speed, plus:
[small_amplitude] [time_harmonic] → linearization →
acoustic_pressure, acoustic_velocity ·
angular_frequency · mean_density · specific_heat_cp ·
thermal_expansion_coefficient → thermal_expansion_ideal_gas ·
standing_wave → standing_wave_phasing
→ **critical_temperature_gradient**
Then `Γ = ∇T_m/∇T_crit` (needs the imposed mean_temperature_gradient).
Do-not-use if: travelling-wave phasing; large amplitude; non-ideal gas.

## rott_momentum_equation  `dp₁/dx = −iωρ_m U₁/[A(1−f_ν)]`
linearization → acoustic_pressure, acoustic_velocity ·
[laminar_flow] · dynamic_viscosity · partial_derivative ·
linearized_euler → linearized_navier_stokes ·
kinematic_viscosity · angular_frequency → viscous_penetration_depth ·
hydraulic_radius · complex_numbers → thermoacoustic_function_fnu ·
volume_flow_rate · mean_density · ordinary_differential_equation ·
[no_mean_flow]
→ **rott_momentum_equation**
More elementary route: `f_ν → 0` recovers linearized Euler.

## rott_wave_equation  (2nd-order ODE for p₁(x))  *(draft)*
everything under rott_momentum_equation, plus the continuity side:
linearized_continuity · linearized_energy_equation (needs
mean_temperature_gradient, rigid_isothermal_wall, thermal_conductivity) ·
thermoacoustic_function_fkappa · heat_capacity_ratio · mean_pressure ·
prandtl_number → rott_continuity_equation
→ **rott_wave_equation**
Do-not-use as: an analytic solution — it is integrated numerically (DeltaEC,
out of scope).

## travelling_wave_engine  (thermoacoustic-Stirling, TASHE)
[regenerator_regime] (r_h ≪ δ_κ) ·
gas_parcel_cycle · travelling_wave → travelling_wave_phasing ·
isothermal_process → ceperley_travelling_wave ·
specific_acoustic_impedance · characteristic_impedance ·
dissipation_mechanisms → acoustic_impedance_matching ·
acoustic_resonator → feedback_torus ·
acoustic_power_gradient · temperature_gradient_ratio → oscillation_onset ·
rott_wave_equation + acoustic_power + thermoacoustic_heat_flux →
total_energy_flux
→ **travelling_wave_engine**
Why this branch: the regenerator's near-reversible heat exchange (f_κ → 1) is
what lifts real-device efficiency toward Carnot — Backhaus & Swift (2000)
reached η ≈ 0.30 ≈ 0.40 η_C.

## relative_carnot_performance  `η_rel = η/η_C`
second_law_thermodynamics · mean_temperature → carnot_efficiency ·
total_energy_flux + acoustic_power + first_law_thermodynamics →
thermoacoustic_efficiency ·
carnot_efficiency + carnot_cop + thermoacoustic_cop → carnot_limit
→ **relative_carnot_performance**
Do-not-use raw `η` to compare devices across different `T_H/T_C` — normalise.
