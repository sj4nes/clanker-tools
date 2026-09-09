# Symbol index (Release 0.1)

For each symbol, the nodes whose **formula statement** uses it. Hand-curated and
confirmed against each `## <node> — <statement>` line in
`../formulas/electrochemistry.md` (see `../build/gen-symbol-index.sh` for the
discovery pass). Units and dimensions are in each node's entry; the dimensional
basis is `[M L T Θ N I]`.

### `Q` — electric charge (C, `I T`)
charge_from_current · charge_mole_electron_bridge · faradays_law_electrolysis ·
moles_of_product_electrolysis · coulombic_efficiency · flow_battery_energy_capacity

### `I` — electric current (A)
electric_current · charge_from_current · electrical_power · ohms_law ·
current_density · ohmic_drop · transport_number

### `t` — time (s)
electric_current · charge_from_current · faradays_law_electrolysis

### `E`, `V` — potential / cell voltage (V, `M L² T⁻³ I⁻¹`)
electric_potential · electrical_work · electrical_power · ohms_law ·
cell_potential · standard_cell_potential · gibbs_from_cell_potential ·
nernst_equation · nernst_298k_form · concentration_cell · overpotential ·
cell_voltage_electrolysis · cell_voltage_discharge · flow_battery_energy_capacity ·
flow_battery_power

### `E°` — standard reduction / cell potential
standard_reduction_potential · standard_cell_potential ·
spontaneity_from_cell_potential · standard_gibbs_from_cell_potential ·
equilibrium_from_cell_potential · nernst_equation · nernst_298k_form ·
decomposition_potential · all_vanadium_flow_battery

### `F` — Faraday constant (`I T N⁻¹`)
faraday_constant · charge_mole_electron_bridge · faradays_law_electrolysis ·
moles_of_product_electrolysis · specific_energy_consumption ·
gibbs_from_cell_potential · equilibrium_from_cell_potential · nernst_equation ·
temperature_coefficient_emf · butler_volmer_equation · ionic_mobility ·
flow_battery_energy_capacity

### `e` — elementary charge
elementary_charge · faraday_constant

### `z` — electrons per formula unit (dimensionless)
electrons_per_formula_unit · charge_mole_electron_bridge ·
faradays_law_electrolysis · moles_of_product_electrolysis ·
specific_energy_consumption · gibbs_from_cell_potential ·
equilibrium_from_cell_potential · nernst_equation · nernst_298k_form ·
temperature_coefficient_emf · butler_volmer_equation · tafel_equation ·
flow_battery_energy_capacity

### `n` — amount of substance (mol, `N`)
amount_of_substance · charge_mole_electron_bridge · moles_of_product_electrolysis ·
molarity

### `M` — molar mass (g/mol, `M N⁻¹`)
molar_mass · faradays_law_electrolysis · specific_energy_consumption

### `m` — mass (g)
molar_mass · faradays_law_electrolysis

### `R` — molar gas constant
gas_constant · equilibrium_from_cell_potential · nernst_equation ·
temperature_coefficient_emf · butler_volmer_equation · tafel_equation ·
ideal_gas_law

### `T` — temperature (K, `Θ`)
equilibrium_from_cell_potential · nernst_equation · temperature_coefficient_emf ·
butler_volmer_equation · ideal_gas_law · gas_volume_electrolysis

### `K` — equilibrium constant; `Q` — reaction quotient (dimensionless)
equilibrium_constant · reaction_quotient · reaction_isotherm ·
equilibrium_from_cell_potential · nernst_equation · nernst_298k_form ·
concentration_cell · cell_potential_vs_soc

### `ΔG` — Gibbs free energy of reaction
gibbs_free_energy · reaction_isotherm · gibbs_from_cell_potential ·
standard_gibbs_from_cell_potential

### `ΔS` — entropy of reaction
entropy · temperature_coefficient_emf

### `η` (eta) — overpotential (V)
overpotential · activation_overpotential · concentration_overpotential ·
ohmic_drop · butler_volmer_equation · tafel_equation · decomposition_potential ·
cell_voltage_electrolysis · cell_voltage_discharge

### `η_C`, `η_V`, `η_E`, `η_F` — efficiencies (dimensionless)
current_efficiency (`η_F`) · specific_energy_consumption (`η_F`) ·
coulombic_efficiency (`η_C`) · voltage_efficiency (`η_V`) ·
energy_efficiency (`η_E`)

### `j` — current density (A/m², `I L⁻²`); `j₀` — exchange current density
current_density · activation_overpotential · concentration_overpotential ·
ohmic_drop · butler_volmer_equation · exchange_current_density (`j₀`) ·
tafel_equation · flow_battery_power

### `R_cell` — cell resistance (Ω)
resistance · ohms_law · ohmic_drop · cell_voltage_electrolysis ·
cell_voltage_discharge

### `κ`, `Λ_m`, `λ_i°` — conductivity, molar conductivity, limiting ionic conductivity
conductivity (`κ`) · molar_conductivity (`Λ_m`) · kohlrausch_law (`Λ_m°`, `λ_i°`) ·
ionic_mobility (`λ_i°`) · debye_huckel_onsager

### `u` — ionic mobility; `t_i` — transport number
ionic_mobility (`u`) · transport_number (`t_i`)

### `c` — molarity (mol/L, `N L⁻³`)
molarity · conductivity · molar_conductivity · state_of_charge ·
flow_battery_energy_capacity · debye_huckel_onsager

### `α` — transfer coefficient; `b` — Tafel slope
butler_volmer_equation (`α`) · tafel_equation (`α`, `b`)

### `SOC` — state of charge
state_of_charge · cell_potential_vs_soc

### `A_stack`, `V_tank`, `N_cells` — flow-battery stack / tank sizing
flow_battery_energy_capacity (`V_tank`) · flow_battery_power (`A_stack`, `N_cells`)
