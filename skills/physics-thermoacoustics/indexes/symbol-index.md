# Symbol index (Release 0.1)

Formula-statement symbol occurrences. Discovery: `ptx -A -W '[A-Za-z_][A-Za-z0-9_]*' formulas/thermoacoustics.md`; results confirmed by whole-token match against each `## node — statement` line.

### `U`
  - `volume_flow_rate` — `U₁ = u₁ A`
  - `acoustic_power` — `Ẇ = ½ Re[ p₁ U₁* ]`
  - `rott_momentum_equation` — `dp₁/dx = − iω ρ_m / [ A (1 − f_ν) ] · U₁`

### `P`
  - `plane_wave` — `p₁(x,t) = P e^{i(ωt − kx)}` , `u₁ = p₁/(ρ_m a)`

### `p`
  - `ideal_gas_law` — `p = ρ R T`
  - `acoustic_wave_equation` — `∂²p₁/∂t² = a² ∂²p₁/∂x²`
  - `plane_wave` — `p₁(x,t) = P e^{i(ωt − kx)}` , `u₁ = p₁/(ρ_m a)`
  - `specific_acoustic_impedance` — `z = p₁ / u₁`
  - `acoustic_power` — `Ẇ = ½ Re[ p₁ U₁* ]`
  - `critical_temperature_gradient` — `∇T_crit = ω |p₁| / (ρ_m c_p |u₁|)`

### `k`
  - `thermal_diffusivity` — `α = k / (ρ_m c_p)`
  - `prandtl_number` — `Pr = ν / α = μ c_p / k`
  - `dispersion_relation` — `ω = a k`

### `a`
  - `adiabatic_sound_speed` — `a = sqrt(γ R T_m)`
  - `acoustic_wave_equation` — `∂²p₁/∂t² = a² ∂²p₁/∂x²`
  - `dispersion_relation` — `ω = a k`
  - `plane_wave` — `p₁(x,t) = P e^{i(ωt − kx)}` , `u₁ = p₁/(ρ_m a)`
  - `characteristic_impedance` — `z₀ = ρ_m a`

### `x`
  - `acoustic_wave_equation` — `∂²p₁/∂t² = a² ∂²p₁/∂x²`
  - `plane_wave` — `p₁(x,t) = P e^{i(ωt − kx)}` , `u₁ = p₁/(ρ_m a)`

### `t`
  - `acoustic_wave_equation` — `∂²p₁/∂t² = a² ∂²p₁/∂x²`
  - `plane_wave` — `p₁(x,t) = P e^{i(ωt − kx)}` , `u₁ = p₁/(ρ_m a)`

### `A`
  - `volume_flow_rate` — `U₁ = u₁ A`
  - `rott_momentum_equation` — `dp₁/dx = − iω ρ_m / [ A (1 − f_ν) ] · U₁`
  - `thermoacoustic_heat_flux *(draft)*` — `Q̇₂ = −½ ρ_m c_p A Re[ ⟨ u₁ T₁* ⟩ ] + (solid/gas conduction)`

