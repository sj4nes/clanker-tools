# Formula index (Release 0.1) — by physical quantity

Full entries: `../formulas/thermodynamics.md`. Exactness labels in parentheses.
Sign convention: `dU = δQ − δW`, `δW = P dV`.

| Area | Node | Formula | Label |
|---|---|---|---|
| Temperature | zeroth_law | `A~C ∧ B~C ⇒ A~B` | fundamental_law |
| Equation of state | ideal_gas_law | `P V = n R T` | constitutive_model |
| Energy accounting | first_law_thermodynamics | `dU = δQ − δW` | fundamental_law |
| Heat | heat | `δQ = dU + δW` | definition |
| Work | work_thermodynamic | `δW = P dV` | definition |
| Heat capacity | heat_capacity_cv | `c_v = (∂u/∂T)_v` | definition |
| Heat capacity | heat_capacity_cp | `c_p = (∂h/∂T)_p` | definition |
| Heat capacity | mayer_relation | `c_p − c_v = R` (ideal gas) | derived_exact |
| Heat capacity | heat_capacity_ratio | `γ = c_p / c_v` | derived_exact |
| Energy function | enthalpy | `H = U + P V` | derived_exact |
| Ideal gas | ideal_gas_internal_energy | `du = c_v dT`, `u = u(T)` | derived_exact |
| Ideal gas | adiabatic_reversible_ideal_gas | `P V^γ = const`, `T V^{γ−1} = const` | derived_exact |
| Throttling | joule_thomson_coefficient | `μ_JT = (∂T/∂P)_H` | derived_exact |
| Engine | heat_engine | `η = |W| / |Q_h|` | definition |
| Refrigerator | refrigerator | `COP = |Q| / |W|` | definition |
| Second law | kelvin_planck_statement | no single-reservoir cyclic engine | fundamental_law |
| Second law | clausius_statement | no spontaneous cold→hot heat | fundamental_law |
| Second law | carnot_theorem | `η_rev ≥ η_any` | fundamental_law |
| Temperature scale | thermodynamic_temperature_scale | `|Q_h|/|Q_c| = T_h/T_c` | definition |
| Engine | carnot_efficiency | `η = 1 − T_c / T_h` | derived_exact |
| Refrigerator | carnot_cop | `COP_ref = T_c/(T_h−T_c)` | derived_exact |
| Second law | clausius_inequality | `∮ δQ/T ≤ 0` | fundamental_law |
| Entropy | entropy | `dS = δQ_rev / T` | definition |
| Entropy | entropy_increase_principle | `ΔS_universe ≥ 0` | fundamental_law |
| Entropy | entropy_ideal_gas | `ΔS = n c_v ln(T₂/T₁) + n R ln(V₂/V₁)` | derived_exact |
| Entropy | tds_relations | `T dS = dU + P dV = dH − V dP` | mathematical_identity |
| Potentials | fundamental_relation_u | `dU = T dS − P dV` | mathematical_identity |
| Potentials | helmholtz_free_energy | `F = U − T S` | derived_exact |
| Potentials | gibbs_free_energy | `G = H − T S` | derived_exact |
| Potentials | free_energy_extremum | `dF ≤ 0` (T,V) ; `dG ≤ 0` (T,P) | fundamental_law |
| Potentials | maxwell_relations | `(∂S/∂V)_T = (∂P/∂T)_V`, … | mathematical_identity |
| Third law | third_law_thermodynamics | `S → S₀` as `T → 0` | fundamental_law |
