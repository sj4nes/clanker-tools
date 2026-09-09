# Formula index (Release 0.1) — by relation

Full entries: `../formulas/electrochemistry.md`. Exactness label in the last
column. `†` = a dimensional check in `../validation/dimensional-checks.bc`;
`‡` = a kernel-checked arithmetic instance in
`../validation/derivation-checks.lean`.

| Relation | Node | Formula | Label |
|---|---|---|---|
| Faraday constant | faraday_constant | `F = N_A e = 96485 C/mol` † | definition |
| Charge from current | charge_from_current | `Q = I t` (`= ∫ I dt`) † | derived_formula |
| Charge ↔ moles of electrons | charge_mole_electron_bridge | `Q = z F n` †‡ | derived_formula |
| Faraday's law of electrolysis | faradays_law_electrolysis | `m = I t M / (z F)` †‡ | derived_formula |
| Moles of product | moles_of_product_electrolysis | `n_prod = Q / (z F ν)` ‡ | derived_formula |
| Gas volume of product | gas_volume_electrolysis | `V = n_prod R T / P` ‡ | derived_formula |
| Current (Faradaic) efficiency | current_efficiency | `η_F = n_actual / n_theoretical` | definition |
| Specific energy consumption | specific_energy_consumption | `E_spec = z F V_cell / (M η_F)` †‡ | derived_formula |
| Cell potential | cell_potential | `E_cell = E_cathode − E_anode` ‡ | derived_formula |
| Standard cell potential | standard_cell_potential | `E°_cell = E°_cathode − E°_anode` ‡ | derived_formula |
| Gibbs ↔ cell potential | gibbs_from_cell_potential | `ΔG = −z F E` †‡ | derived_exact |
| Standard Gibbs ↔ E° | standard_gibbs_from_cell_potential | `ΔG° = −z F E°_cell` ‡ | derived_exact |
| E° ↔ equilibrium constant | equilibrium_from_cell_potential | `E°_cell = (R T / z F) ln K` †‡ | derived_exact |
| Temperature coefficient | temperature_coefficient_emf | `(∂E/∂T)_P = ΔS / (z F)` † | derived_formula |
| Nernst equation | nernst_equation | `E = E° − (R T / z F) ln Q` †‡ | derived_exact |
| Nernst at 298 K | nernst_298k_form | `E = E° − (0.05916 V / z) log₁₀ Q` ‡ | derived_formula |
| Concentration cell | concentration_cell | `E = −(R T / z F) ln([dil]/[conc])` | derived_formula |
| Current density | current_density | `j = I / A` † | definition |
| Overpotential | overpotential | `η = E_applied − E_equilibrium` | definition |
| Ohmic drop | ohmic_drop | `η_ohmic = I R_cell` † | derived_formula |
| Butler–Volmer *(stated)* | butler_volmer_equation | `j = j₀[e^{αzFη/RT} − e^{−(1−α)zFη/RT}]` †‡ | principle_law |
| Tafel equation | tafel_equation | `η_act = a + b log₁₀ j`,  `b = 2.303RT/(αzF)` ‡ | empirical_law |
| Decomposition potential | decomposition_potential | `V_decomp ≈ \|E°_cell\| + \|η_a\| + \|η_c\|` | derived_formula |
| Cell voltage (electrolysis) | cell_voltage_electrolysis | `V_cell = E°_cell + \|η_a\| + \|η_c\| + I R` ‡ | derived_formula |
| Cell voltage (discharge) | cell_voltage_discharge | `V_cell = E°_cell − \|η_a\| − \|η_c\| − I R` | derived_formula |
| Conductivity | conductivity | `κ = 1/ρ` (from `R` and cell geometry) | definition |
| Molar conductivity | molar_conductivity | `Λ_m = κ / c` | definition |
| Kohlrausch's law | kohlrausch_law | `Λ_m° = ν₊ λ₊° + ν₋ λ₋°` | empirical_law |
| Ionic mobility | ionic_mobility | `u = v_drift / E`,  `λ_i° = z_i F u_i` † | definition |
| Transport number | transport_number | `t_i = I_i / I_total`,  `Σ t_i = 1` | definition |
| Debye–Hückel–Onsager *(named)* | debye_huckel_onsager | `Λ_m = Λ_m° − k √c` | empirical_law |
| Flow-battery energy capacity | flow_battery_energy_capacity | `E_stored = c V_tank z F ΔE_avg` †‡ | derived_formula |
| Flow-battery power | flow_battery_power | `P = N_cells A_stack j V_cell` † | derived_formula |
| State of charge | state_of_charge | `SOC = c_charged / c_total` | definition |
| Coulombic efficiency | coulombic_efficiency | `η_C = Q_out / Q_in` | definition |
| Voltage efficiency | voltage_efficiency | `η_V = V_discharge / V_charge` | definition |
| Energy (round-trip) efficiency | energy_efficiency | `η_E = η_C η_V` †‡ | derived_formula |

## Qualitative / example / bookkeeping nodes (no single formula)
electrons_per_formula_unit · electrochemical_series ·
spontaneity_from_cell_potential · cell_potential_vs_soc · overpotential parts ·
exchange_current_density · competing_electrode_reactions ·
thermodynamic_vs_kinetic_product · oxygen_overpotential ·
electrode_material_selection · supporting_electrolyte · ionic_conduction ·
migration_vs_diffusion · cell_notation · galvanic_cell · electrolytic_cell ·
anode · cathode · salt_bridge · ion_exchange_membrane · standard_hydrogen_electrode ·
standard_reduction_potential · energy_power_decoupling · shunt_current ·
crossover · capacity_fade · water_electrolysis · reversible_fuel_cell ·
chlor_alkali_process · chlorate_perchlorate · hall_heroult_process ·
copper_electrorefining · zinc_electrowinning · all_vanadium_flow_battery ·
iron_flow_battery · zinc_iron_flow_battery · iron_chromium_flow_battery ·
zinc_bromine_flow_battery · fixed_cell_battery_contrast ·
corrosion_as_galvanic_cell · pourbaix_diagram · electrical_double_layer
