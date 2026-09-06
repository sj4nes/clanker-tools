# Formula index (Release 0.1) — by quantity / result

Full entries: `../formulas/thermoacoustics.md`. Exactness label in parentheses.
`(draft)` = structure and dimensions checked, coefficients pending source
reconciliation (Swift 1988 / 2002).

| Quantity / result | Node | Formula | Label |
|---|---|---|---|
| Equation of state | ideal_gas_law | `p = ρ R T` | constitutive_model |
| Specific-heat ratio | heat_capacity_ratio | `γ = c_p/c_v` ; `c_p − c_v = R` | derived_exact |
| Thermal expansion (gas) | thermal_expansion_ideal_gas | `β = 1/T_m` | derived_exact |
| Carnot efficiency | carnot_efficiency | `η_C = 1 − T_C/T_H` | derived_exact |
| Carnot COP (cooling) | carnot_cop | `COP_C = T_C/(T_H − T_C)` | derived_exact |
| Kinematic viscosity | kinematic_viscosity | `ν = μ/ρ_m` | definition |
| Thermal diffusivity | thermal_diffusivity | `α = k/(ρ_m c_p)` | definition |
| Prandtl number | prandtl_number | `Pr = ν/α = μ c_p/k` | definition |
| Sound speed | adiabatic_sound_speed | `a = sqrt(γ R T_m)` | derived_exact |
| Wave equation | acoustic_wave_equation | `∂²_t p₁ = a² ∂²_x p₁` | derived_exact |
| Dispersion | dispersion_relation | `ω = a k` | derived_exact |
| Wavelength / frequency | wavelength, frequency | `λ = 2π/k` ; `f = ω/2π` | derived_exact |
| Plane wave | plane_wave | `p₁ = P e^{i(ωt−kx)}`, `u₁ = p₁/ρ_m a` | derived_exact |
| Characteristic impedance | characteristic_impedance | `z₀ = ρ_m a` | derived_exact |
| Specific impedance | specific_acoustic_impedance | `z = p₁/u₁` (complex) | definition |
| Volume flow rate | volume_flow_rate | `U₁ = u₁ A` | definition |
| Acoustic power | acoustic_power | `Ẇ = ½ Re[p₁ U₁*]` | derived_exact |
| Thermal penetration depth | thermal_penetration_depth | `δ_κ = sqrt(2α/ω)` | derived_exact |
| Viscous penetration depth | viscous_penetration_depth | `δ_ν = sqrt(2ν/ω)` | derived_exact |
| Penetration ratio | penetration_depth_ratio | `δ_ν/δ_κ = sqrt(Pr)` | derived_exact |
| Hydraulic radius | hydraulic_radius | `r_h = A_gas/Π` | definition |
| Viscous f-function | thermoacoustic_function_fnu | `f_ν(δ_ν, r_h)` complex | derived_exact (draft) |
| Thermal f-function | thermoacoustic_function_fkappa | `f_κ(δ_κ, r_h)` complex | derived_exact (draft) |
| Boundary-layer limit | boundary_layer_limit_f | `f_j ≈ (1−i)δ_j/(2 r_h)` | approximation (draft) |
| Rott momentum | rott_momentum_equation | `dp₁/dx = −iωρ_m U₁ / [A(1−f_ν)]` | derived_exact |
| Rott continuity | rott_continuity_equation | `dU₁/dx = −iωA[1+(γ−1)f_κ]p₁/(γp_m) + (…)U₁` | derived_exact (draft) |
| Rott wave equation | rott_wave_equation | 2nd-order ODE for `p₁(x)` | derived_exact (draft) |
| Critical temp. gradient | critical_temperature_gradient | `∇T_crit = ω\|p₁\| / (ρ_m c_p \|u₁\|)` | derived_exact |
| Gradient ratio | temperature_gradient_ratio | `Γ = ∇T_m / ∇T_crit` | definition |
| Short-stack acoustic power | short_stack_acoustic_power | `ΔẆ₂ ∝ (Γ − 1) − viscous loss` | approximation (draft) |
| Short-stack heat flux | short_stack_heat_flux | `Q̇₂ ∝ \|p₁\|\|u₁\| × phasing` | approximation (draft) |
| Thermoacoustic heat flux | thermoacoustic_heat_flux | `Q̇₂ = −½ρ_m c_p A Re[⟨u₁T₁*⟩]` | derived_exact (draft) |
| Total energy flux | total_energy_flux | `Ḣ₂ = Ẇ₂ + Q̇₂` (const w/o heat exch.) | derived_exact (draft) |
| Onset | oscillation_onset | `gain(∇T_m) = losses` | derived_exact |
| Engine efficiency | thermoacoustic_efficiency | `η = Ẇ / Q̇_H` | definition |
| Refrigerator COP | thermoacoustic_cop | `COP = Q̇_C / Ẇ` | definition |
| Relative-Carnot | relative_carnot_performance | `η_rel = η/η_C` | derived_exact |
