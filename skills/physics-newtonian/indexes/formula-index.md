# Formula index (Release 0.1) — by physical quantity

Full entries: `../formulas/newtonian.md`. Exactness labels in parentheses.

| Quantity | Node | Formula | Label |
|---|---|---|---|
| Position | position | `x(t)` | definition |
| Displacement | displacement | `Δx = x − x₀` | definition |
| Velocity | velocity | `v = dx/dt` | definition |
| Speed | speed | `\|v\|` | definition |
| Acceleration | acceleration | `a = dv/dt` | definition |
| Kinematics (const a) | constant_acceleration_kinematics | `v = v₀ + at` ; `x = x₀ + v₀t + ½at²` ; `v² = v₀² + 2aΔx` | derived_exact |
| Force / motion | newton_second_law | `F_net = m a` | fundamental_law |
| Interaction forces | newton_third_law | `F₁₂ = −F₂₁` | fundamental_law |
| Weight | weight | `W = m g` | constitutive_model |
| Kinetic friction | friction_kinetic | `f_k = μ_k N` | constitutive_model |
| Spring force | hookes_law | `F = −k x` | constitutive_model |
| Work | work | `W = ∫ F dx` | definition |
| Kinetic energy | kinetic_energy | `K = ½ m v²` | derived_exact |
| Work ↔ energy | work_energy_theorem | `W_net = ΔK` | derived_exact |
| Potential energy | potential_energy | `ΔU = −W_cons` | definition |
| Force ↔ potential | force_from_potential | `F = −dU/dx` | derived_exact |
| Gravitational PE (uniform) | gravitational_pe_uniform | `U = m g h` | derived_exact |
| Elastic PE | elastic_pe | `U = ½ k x²` | derived_exact |
| Mechanical energy | mechanical_energy | `E = K + U` | definition |
| Energy conservation | conservation_of_mechanical_energy | `E = const` | fundamental_law (conditional) |
| Power | power | `P = dE/dt` ; `P = F v` | definition |
| Momentum | momentum | `p = m v` | definition |
| Impulse | impulse | `J = ∫ F dt` | definition |
| Impulse ↔ momentum | impulse_momentum_theorem | `J = Δp` | derived_exact |
| Momentum conservation | conservation_of_momentum | `Σp = const` | fundamental_law |
| Small angle | small_angle_approximation | `sin θ ≈ θ` | approximation |
| SHM | simple_harmonic_motion | `x = A cos(ωt + φ)` | derived_exact |
| SHM frequency | angular_frequency_shm | `ω = √(k/m)` | derived_exact |
| SHM period | shm_period | `T = 2π/ω` | derived_exact |
| Pendulum period | simple_pendulum | `T = 2π√(L/g)` | derived_exact (small angle) |
| Gravitation | newton_gravitation | `F = G m₁m₂ / r²` | fundamental_law |
| Gravitational field | gravitational_field | `g = G M / r²` | derived_exact |
| Gravitational PE (1/r) | gravitational_pe_general | `U = −G m₁m₂ / r` | derived_exact |
