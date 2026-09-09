# Symbol index (Release 0.1)

For each symbol, the nodes whose **formula statement** uses it. Hand-curated and
confirmed against each `## <node> — <statement>` line in
`../formulas/chemistry-foundations.md` (the statements are Unicode-heavy, so this
is not mechanically generated — see `../build/gen-symbol-index.sh` for the
discovery pass). Units and dimensions are in each node's entry.

### `n` — amount of substance (mol, `N`)
number_from_amount · molar_mass · amount_from_mass · mole_ratio · mole_fraction ·
molarity · ideal_gas_law · molar_volume · solution_stoichiometry ·
limiting_reagent · theoretical_yield

### `N` — number of entities (dimensionless count)
number_from_amount

### `N_A` — Avogadro constant (`N⁻¹`)
avogadro_constant · number_from_amount

### `M` — molar mass (g/mol, `M N⁻¹`)
molar_mass · molar_mass_from_formula · amount_from_mass · percent_composition ·
molecular_formula · theoretical_yield

### `m` — mass (g)
molar_mass · amount_from_mass · specific_heat_capacity · calorimetry ·
theoretical_yield · conservation_of_mass

### `c` — amount concentration / molarity (mol/L, `N L⁻³`)
molarity · dilution_equation · solution_stoichiometry · strong_acid_base_ph ·
equivalence_point · percent_ionization

### `c` — specific heat capacity (J g⁻¹ K⁻¹, `L² T⁻² Θ⁻¹`)
specific_heat_capacity · calorimetry

### `V` — volume (m³ or L, `L³`)
molarity · dilution_equation · ideal_gas_law · molar_volume · equivalence_point

### `P` — pressure (Pa, `M L⁻¹ T⁻²`)
ideal_gas_law · molar_volume · daltons_law · partial_pressure · kp_kc_relation

### `T` — thermodynamic temperature (K, `Θ`)
ideal_gas_law · molar_volume · reaction_isotherm · gibbs_free_energy ·
gibbs_helmholtz_relation

### `R` — molar gas constant (`M L² T⁻² Θ⁻¹ N⁻¹`)
gas_constant · ideal_gas_law · molar_volume · kp_kc_relation · reaction_isotherm

### `xᵢ` — mole fraction (dimensionless)
mole_fraction · partial_pressure · daltons_law

### `K`, `K_c` — equilibrium constant (dimensionless)
equilibrium_constant · reaction_quotient · q_versus_k · kp_kc_relation ·
reaction_isotherm · le_chatelier

### `K_p` — pressure equilibrium constant
kp_kc_relation

### `Q` — reaction quotient (dimensionless)
reaction_quotient · q_versus_k

### `Δn` — change in gas moles
kp_kc_relation

### `K_w` — autoionization constant of water
water_autoionization · poh_relation · ka_kb_relation

### `K_a`, `pK_a` — weak-acid constant
weak_acid_equilibrium · ka_kb_relation · henderson_hasselbalch ·
acid_base_titration_curve

### `K_b` — conjugate-base constant
ka_kb_relation

### `[H⁺]` — hydrogen-ion concentration
water_autoionization · ph_definition · strong_acid_base_ph · weak_acid_equilibrium

### `pH`
ph_definition · poh_relation · strong_acid_base_ph · henderson_hasselbalch ·
acid_base_titration_curve

### `pOH`
poh_relation

### `H`, `U` — enthalpy, internal energy (J, `M L² T⁻²`)
internal_energy · first_law_thermo · enthalpy · enthalpy_of_reaction ·
gibbs_free_energy

### `q`, `w` — heat, work (J)
heat_work_sign_convention · first_law_thermo · specific_heat_capacity ·
calorimetry · heat_of_reaction_calorimetry

### `ΔT` — temperature change
specific_heat_capacity · calorimetry

### `ΔH`, `ΔH_rxn` — reaction enthalpy
enthalpy_of_reaction · heat_of_reaction_calorimetry · hess_law ·
enthalpy_from_formation_enthalpies · enthalpy_from_bond_enthalpies ·
gibbs_helmholtz_relation

### `ΔH_f°` — standard enthalpy of formation
standard_enthalpy_of_formation · enthalpy_from_formation_enthalpies

### `D` — bond enthalpy
bond_enthalpy · enthalpy_from_bond_enthalpies

### `G`, `ΔG`, `ΔG°` — Gibbs energy
gibbs_free_energy · gibbs_helmholtz_relation · spontaneity_criterion ·
reaction_isotherm

### `ΔS` — reaction entropy
gibbs_helmholtz_relation

### `Z` — atomic number
atomic_number · element

### `A` — mass number; `A_r` — relative atomic mass
isotope (`A = Z + N`) · relative_atomic_mass (`A_r`) ·
molar_mass_from_formula (`A_r`)

### `fᵢ` — isotopic abundance (mole fraction)
isotopic_abundance · relative_atomic_mass

### `ν` — stoichiometric coefficient
stoichiometric_coefficient · mole_ratio · equilibrium_constant · kp_kc_relation ·
equivalence_point

### `χ`, `Δχ` — electronegativity (Pauling, dimensionless)
electronegativity · ionic_bond · covalent_bond · bond_polarity

### `IE` — ionization energy
ionization_energy

### `k` — integer formula multiplier
molecular_formula

### `α` — percent ionization
percent_ionization

### `FC` — formal charge
formal_charge
