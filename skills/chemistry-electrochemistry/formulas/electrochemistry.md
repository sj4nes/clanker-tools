# Formula and concept entries — Release 0.1

A view generated from and reconciled against the graph. Each entry: statement,
symbols (SI unit and `[M L T Θ N I]` dimension where quantitative), exactness
label, assumptions, direct prerequisites, one limiting/special case, failure
modes, source. Dimensional checks: `validation/dimensional-checks.bc`.
Algebraic-identity checks: `validation/derivation-checks.lean`.

**Conventions** (see `conventions.md`): all `E°` are **reduction** potentials vs
SHE (`E°(SHE) ≡ 0`); anode = oxidation, cathode = reduction (independent of
terminal sign); `E°_cell = E°_cathode − E°_anode`; `ΔG = −zFE`; `z` = electrons
per formula unit as written; overpotential `|η|` adds to an electrolyser's
voltage and subtracts from a battery's. `T = 298.15 K` and unit activity unless
stated; `dilute_ideal_solution` on every `E`/`Q`/`K`/`Λ_m`. Dimensional basis
adds **`I`** (electric current); charge is `I T`, potential is `M L² T⁻³ I⁻¹`.

Constants: `F = 96485.332 C/mol`; `e = 1.602176634×10⁻¹⁹ C`;
`N_A = 6.02214076×10²³ mol⁻¹`; `R = 8.314462618 J mol⁻¹ K⁻¹`;
`RT/F = 0.025693 V` and `RT ln10 / F = 0.059160 V` at 298.15 K.

Source keys: `BLM` Brown/LeMay 14e; `Atkins` Atkins' Physical Chemistry 11e;
`Bard` Bard & Faulkner 2e; `Newman` Newman & Thomas-Alyea 3e; `IUPAC` Gold Book;
`SI` SI Brochure 9e; `CODATA` CODATA 2018; `Pletcher` Pletcher & Walsh
*Industrial Electrochemistry* 2e; `Skyllas-Kazacos` Skyllas-Kazacos et al.
*Prog. Energy Combust. Sci.* 2017 (flow batteries).

---

# Electrical primitives (root set — a future physics-circuits capsule)

## electric_charge — the conserved quantity carried by electrons and ions
- Label: primitive. `Q`: coulomb (C), `I T`. Conserved; quantised in units of `e`.
- Prereqs: none (root).
- Special case: a mole of electrons carries `−F = −96485 C`.
- Failure: confusing charge (`C`) with current (`C/s = A`) or with amount (`mol`).
- Source: `SI` §2.3; `Atkins` ch. 0.

## elementary_charge — `e = 1.602176634×10⁻¹⁹ C` (exact, 2019 SI)
- Label: reference_data. The charge magnitude of one electron or proton.
- Prereqs: electric_charge.
- Special case: `F = N_A e` — the charge of one mole of electrons.
- Failure: dropping the sign when the carrier is an electron.
- Source: `CODATA`; `SI` §2.3.1.

## electric_current — `I = dQ/dt`, the rate of charge flow
- Label: primitive. `I`: ampere (A), base dimension `I`. `Q = ∫ I dt`.
- Prereqs: electric_charge.
- Special case: constant current → `Q = I t`.
- Failure: treating a time-varying current's charge as `I t` with the peak `I`.
- Source: `SI` §2.3.1.

## electric_potential — `V = W/Q`, work per unit charge moved between two points
- Label: primitive. `V`: volt (V), `M L² T⁻³ I⁻¹`.
- Prereqs: electric_charge.
- Special case: moving `1 C` through `1 V` does `1 J` of work.
- Failure: quoting a single-electrode potential as absolute (only differences,
  and differences from the SHE, are defined).
- Source: `Atkins` ch. 6.

## electrical_work — `W = Q ΔV`, work to move charge `Q` through potential `ΔV`
- Label: definition. `W`: J, `M L² T⁻²`.
- Prereqs: electric_charge, electric_potential.
- Special case: the maximum electrical work a cell can do is `−ΔG = zFE`.
- Failure: using the terminal voltage under load where the reversible `E` is
  meant (or vice versa) — they differ by the overpotential and `IR` drop.
- Source: `Atkins` ch. 6.

## electrical_power — `P = I V`
- Label: definition. `P`: watt (W), `M L² T⁻³`.
- Prereqs: electric_current, electric_potential.
- Special case: `P = I² R = V²/R` for an ohmic load.
- Failure: using `E°_cell` instead of the loaded terminal voltage for a real
  stack's power.
- Source: any circuits text.

## resistance — `R = V/I`, opposition to current flow
- Label: primitive. `R`: ohm (Ω), `M L² T⁻³ I⁻²`.
- Prereqs: electric_current, electric_potential.
- Special case: the electrolyte and separator dominate `R` in most cells.
- Failure: ignoring the temperature and concentration dependence of electrolyte
  resistance.
- Source: any circuits text.

## ohms_law — `V = I R` (linear, for an ohmic conductor)
- Label: empirical_law. Holds for metals and, approximately, for an electrolyte
  at fixed composition and temperature.
- Prereqs: resistance.
- Special case: the `IR` drop inside a cell, `η_ohmic = I R_cell`.
- Failure: applying it across an electrode interface, which is non-ohmic
  (Butler–Volmer).
- Source: any circuits text.

---

# Imported bridge nodes

## avogadro_constant — `N_A = 6.02214076×10²³ mol⁻¹` *(imported)*
- Label: bridge_imported. `N⁻¹`. Prereqs: none here.
- Special case: `F = N_A e`.
- Failure: —.
- Source: imported; `chemistry-foundations` `avogadro_constant`.

## amount_of_substance — `n`, mol, `N` *(imported)*
- Label: bridge_imported. Prereqs: none here.
- Special case: `Q = z F n` for `n` mol of a species reacting by `z` electrons.
- Failure: conflating amount with mass or with number of electrons.
- Source: imported; `chemistry-foundations` `amount_of_substance`.

## molar_mass — `M = m/n`, g/mol *(imported)*
- Label: bridge_imported. `M N⁻¹`. Prereqs: none here.
- Special case: `m = (Q/zF) M` — Faraday's law.
- Failure: using the atomic mass where the deposited species is diatomic or a
  compound.
- Source: imported; `chemistry-foundations` `molar_mass`.

## mole_ratio — `n_B = n_A (ν_B/ν_A)` *(imported)*
- Label: bridge_imported. Prereqs: none here.
- Special case: `n(H₂) : n(O₂) = 2 : 1` in water electrolysis.
- Failure: taking `ν` from an unbalanced electrode reaction.
- Source: imported; `chemistry-foundations` `mole_ratio`.

## molarity — `c = n/V`, mol/L, `N L⁻³` *(imported)*
- Label: bridge_imported. Prereqs: none here.
- Special case: a flow battery's energy scales with `c` and tank volume.
- Failure: using solvent volume rather than solution volume.
- Source: imported; `chemistry-foundations` `molarity`.

## standard_state — unit activity, `1 bar`, `°` superscript; tables at 298.15 K *(imported)*
- Label: bridge_imported. Prereqs: none here.
- Special case: `E°` is the cell potential with every species at unit activity.
- Failure: assuming "standard" fixes the temperature.
- Source: imported; `chemistry-foundations` `standard_state`.

## dilute_ideal_solution — activity ≈ concentration *(imported assumption)*
- Label: assumption. Carried by every `E`, `Q`, `K`, `Λ_m` here.
- Prereqs: none here.
- Special case: fails first for multiply-charged ions (V²⁺, VO₂⁺) at flow-battery
  concentrations (1–2 M) — real cells use empirical corrections.
- Failure: expecting Nernst-equation accuracy to the millivolt in a 2 M
  vanadium electrolyte.
- Source: imported; `chemistry-foundations` `dilute_ideal_solution`.

## ideal_gas_law — `P V = n R T` *(imported)*
- Label: bridge_imported. Prereqs: none here.
- Special case: the volume of H₂/O₂/Cl₂ evolved at an electrode.
- Failure: using °C for `T`; high-pressure electrolysers deviate.
- Source: imported; `chemistry-foundations` `ideal_gas_law`.

## molar_volume — `V_m = RT/P`, `L³ N⁻¹` *(imported)*
- Label: bridge_imported. `22.711 L/mol` at STP.
- Prereqs: ideal_gas_law.
- Special case: `1 mol` of H₂ from `2F = 192970 C` occupies `22.7 L` at STP.
- Failure: treating `V_m` as constant off-STP.
- Source: imported; `chemistry-foundations` `molar_volume`.

## gas_constant — `R = 8.314462618 J mol⁻¹ K⁻¹`
- Label: reference_data. Appears as `RT/zF` in Nernst and `zFη/RT` in
  Butler–Volmer.
- Prereqs: none (root).
- Special case: `RT/F = 0.025693 V`, `RT ln10 / F = 0.059160 V` at 298.15 K.
- Failure: unit-mismatched `R`.
- Source: `CODATA`.

## oxidation_reduction — oxidation = loss of electrons; reduction = gain *(imported)*
- Label: bridge_imported. Prereqs: none here.
- Special case: oxidation at the anode, reduction at the cathode — always.
- Failure: identifying one half without the other.
- Source: imported; `chemistry-foundations` `oxidation_reduction`.

## oxidation_number_rules — assign oxidation numbers by the priority hierarchy *(imported)*
- Label: bridge_imported. Prereqs: none here.
- Special case: the change in oxidation number = electrons transferred per atom.
- Failure: confusing oxidation number with formal charge.
- Source: imported; `chemistry-foundations` `oxidation_number_rules`.

## oxidizing_reducing_agent — the oxidant is reduced; the reductant is oxidized *(imported)*
- Label: bridge_imported. Prereqs: none here.
- Special case: a more positive `E°` = a stronger oxidant.
- Failure: swapping the agent's own change with the change it causes.
- Source: imported; `chemistry-foundations` `oxidizing_reducing_agent`.

## half_reaction — the oxidation or reduction alone, electrons explicit, mass + charge balanced *(imported)*
- Label: bridge_imported. Prereqs: none here.
- Special case: `MnO₄⁻ + 8H⁺ + 5e⁻ → Mn²⁺ + 4H₂O` (`z = 5`).
- Failure: leaving electrons in the combined cell equation.
- Source: imported; `chemistry-foundations` `half_reaction`.

## balancing_redox_half_reactions — scale halves to equal electrons, then add *(imported)*
- Label: bridge_imported. Prereqs: none here.
- Special case: combining the electrode half-reactions to get the cell reaction
  and its `z`.
- Failure: mismatched electron counts across the two halves.
- Source: imported; `chemistry-foundations` `balancing_redox_half_reactions`.

## equilibrium_constant — `K`, dimensionless *(imported)*
- Label: bridge_imported. Prereqs: none here.
- Special case: `E° = (RT/zF) ln K` — a `1.2 V` cell has `K ≈ 10⁴⁰`.
- Failure: carrying units in `K`.
- Source: imported; `chemistry-foundations` `equilibrium_constant`.

## reaction_quotient — `Q`, the `K` expression at any composition *(imported)*
- Label: bridge_imported. Prereqs: none here.
- Special case: at equilibrium `Q = K` and `E = 0` (a dead battery).
- Failure: using initial concentrations and calling the result `K`.
- Source: imported; `chemistry-foundations` `reaction_quotient`.

## reaction_isotherm — `ΔG° = −RT ln K` (and `ΔG = ΔG° + RT ln Q`) *(imported)*
- Label: bridge_imported. Prereqs: none here.
- Special case: combined with `ΔG = −zFE` it gives the Nernst equation.
- Failure: `log₁₀` where `ln` is meant.
- Source: imported; `chemistry-foundations` `reaction_isotherm`.

## gibbs_free_energy — `G = H − TS`; `ΔG` is the maximum non-expansion work *(imported)*
- Label: bridge_imported. `J`, `M L² T⁻²`. Prereqs: none here.
- Special case: `ΔG = −zFE` — the cell potential is `ΔG` per coulomb.
- Failure: applying the constant-`T,P` spontaneity test elsewhere.
- Source: imported; `physics-thermodynamics` `gibbs_free_energy`.

## entropy — `S`, `J/K`, `M L² T⁻² Θ⁻¹` *(imported)*
- Label: bridge_imported. Prereqs: none here.
- Special case: `(∂E/∂T)_P = ΔS/(zF)` — a cell whose reaction increases entropy
  has an emf that rises with temperature.
- Failure: —.
- Source: imported; `physics-thermodynamics` `entropy`.

---

# Faraday: charge ↔ moles of electrons ↔ mass

## faraday_constant — `F = N_A e = 96485.332 C/mol`
- Label: definition. `I T N⁻¹`. The charge of one mole of electrons.
- Prereqs: avogadro_constant, elementary_charge.
- Dimensional check: `[N_A e] = N⁻¹ · I T = I T N⁻¹` (consistent).
- Special case: `1 F` deposits `1 mol` of a `z = 1` species (`108 g` Ag), `½ mol`
  of a `z = 2` species (`32 g` Cu).
- Failure: using `F` in kJ (it is coulombs per mole); dropping `z`.
- Source: `CODATA`; `Atkins` ch. 6.

## charge_from_current — `Q = I t` (constant `I`); `Q = ∫ I dt` in general
- Label: derived_formula. `Q`: C, `I T`.
- Prereqs: electric_current.
- Dimensional check: `[I t] = I · T = I T` (consistent).
- Special case: `2.00 A` for `1.00 h` passes `Q = 2.00 × 3600 = 7200 C ≈ 0.0746 F`.
- Failure: using the average current where the integral is needed for a ramped
  or pulsed waveform.
- Source: `Atkins` ch. 6.

## electrons_per_formula_unit — `z`, the electrons transferred per formula unit of the reaction as written
- Label: definition. Dimensionless positive integer.
- Prereqs: half_reaction, oxidation_reduction, oxidation_number_rules.
- Special case: `Cu²⁺ + 2e⁻ → Cu` has `z = 2`; `Al³⁺ + 3e⁻ → Al` has `z = 3`;
  `2H₂O → O₂ + 4H⁺ + 4e⁻` has `z = 4`.
- Failure: taking `z` from an unbalanced half-reaction; changing `z` when you
  scale the equation without scaling `ΔG`.
- Source: `IUPAC` "charge number of cell reaction"; `Atkins` ch. 6.

## charge_mole_electron_bridge — `Q = z F n`
- Label: derived_formula. Links coulombs through the cell to moles of the
  reacting species.
- Prereqs: faraday_constant, electrons_per_formula_unit, amount_of_substance,
  charge_from_current.
- Dimensional check: `[z F n] = 1 · I T N⁻¹ · N = I T` (consistent with `[Q]`).
- Special case: `n = Q/(zF)`: `7200 C` reduces `7200/(2·96485) = 0.0373 mol` of
  a `z = 2` species.
- Failure: using the species' `ν` where `z` is meant, or vice versa.
- Source: `Atkins` ch. 6.

## faradays_law_electrolysis — `m = (Q/F)(M/z) = (I t M)/(z F)`
- Label: derived_formula. `m`: g. The mass deposited or dissolved by charge `Q`.
- Prereqs: charge_mole_electron_bridge, molar_mass.
- Dimensional check: `[(I t M)/(z F)] = (I T · M N⁻¹)/(1 · I T N⁻¹) = M` (consistent).
- Special case: Cu plating, `I = 2.00 A`, `t = 3600 s`, `z = 2`,
  `M = 63.55 g/mol` → `m = (2.00·3600·63.55)/(2·96485) = 2.371 g`. Lean check 1.
- Failure: `z` for the wrong half-reaction; `M` of the atom where a molecule is
  produced (H₂, not H).
- Source: `BLM` ch. 20; `Pletcher` ch. 1.

## moles_of_product_electrolysis — `n_product = Q / (z F ν)` via the balanced equation
- Label: derived_formula. `ν` the coefficient of the product in the half-reaction.
- Prereqs: charge_mole_electron_bridge, mole_ratio.
- Special case: `2H₂O + 2e⁻ → H₂ + 2OH⁻`: `n(H₂) = Q/(2F)`, so `1 mol` H₂ per
  `2F = 192970 C`.
- Failure: forgetting that `O₂` needs `4F` per mole while `H₂` needs `2F` —
  hence the `2 : 1` volume ratio.
- Source: `Pletcher` ch. 1.

## gas_volume_electrolysis — `V = n_product R T / P` for a gaseous product
- Label: derived_formula (Faraday's law then the ideal-gas law).
- Prereqs: moles_of_product_electrolysis, molar_volume.
- Special case: `1 F` gives `0.5 mol` H₂ = `11.4 L` at STP; water electrolysis
  yields `H₂ : O₂ = 2 : 1` by volume.
- Failure: applying the STP molar volume at the cell's actual temperature and
  (often elevated) pressure; ignoring water vapour in the wet gas.
- Source: `Pletcher` ch. 1.

## current_efficiency — `η_F = n_product,actual / n_product,theoretical` (theoretical from Faraday's law)
- Label: definition. Dimensionless, `[0, 1]`. Also "Faradaic yield" or "current
  yield".
- Prereqs: faradays_law_electrolysis, moles_of_product_electrolysis.
- Special case: chlor-alkali membrane cells run at `η_F ≈ 0.95–0.97` for NaOH;
  Hall–Héroult at `≈ 0.90–0.95` for Al; the rest of the charge goes to side
  reactions (O₂, back-reaction, the reduction of dissolved metal).
- Failure: quoting `η_F > 1` (impossible — it means the theoretical basis or the
  product assay is wrong); confusing it with energy efficiency.
- Source: `Pletcher` ch. 1.

## specific_energy_consumption — `E_spec = z F V_cell / (M η_F)` (J/kg; quoted as kWh/kg or kWh/t)
- Label: derived_formula. The electrical energy to make unit mass of product.
- Prereqs: faradays_law_electrolysis, current_efficiency, electrical_work,
  cell_voltage_electrolysis.
- Dimensional check: `[z F V_cell / M] = (I T N⁻¹ · M L² T⁻³ I⁻¹)/(M N⁻¹) =
  L² T⁻²` = J/kg (consistent; `η_F` dimensionless).
- Special case: aluminium, `z = 3`, `M = 26.98 g/mol`, `V_cell ≈ 4.2 V`,
  `η_F ≈ 0.93` → `E_spec ≈ 13.4 kWh/kg` (≈ 13.4 MWh/tonne). Lean check 2 checks
  the `zF/M` charge-per-kg factor.
- Failure: using `E°_cell` instead of the real `V_cell` (halves the answer);
  omitting `η_F`.
- Source: `Pletcher` ch. 3; industry data for the Al number.

---

# Electrochemical cells

## electrolyte — a substance that conducts electricity by the movement of ions
- Label: physical_definition. Aqueous salt/acid/base solutions, molten salts,
  or ion-conducting solids/polymers.
- Prereqs: electric_charge, molarity.
- Special case: a *strong* electrolyte is fully dissociated; a *supporting*
  electrolyte is added only to carry current and set conductivity.
- Failure: treating a metal (electronic conductor) as an electrolyte; ignoring
  that pure water is a very poor electrolyte (`κ ≈ 5.5×10⁻⁶ S/m`).
- Source: `Atkins` ch. 16; `IUPAC` "electrolyte".

## electrode — an electronic conductor at which a half-reaction exchanges electrons with the external circuit
- Label: physical_definition. May be inert (Pt, C, DSA) or a reactant
  (Cu anode in refining, Al-forming cathode).
- Prereqs: half_reaction, electric_current.
- Special case: the electrode potential is set by the half-reaction at its
  surface, read against a reference.
- Failure: assuming an "inert" electrode is inert in every electrolyte (Pt
  catalyses many reactions; carbon corrodes at high anodic potential).
- Source: `Bard` ch. 1.

## electrochemical_cell — two electrodes in contact with one or more electrolytes, connected by an external circuit
- Label: definition. The site of a redox reaction split into two half-reactions
  in different places.
- Prereqs: electrode, electrolyte.
- Special case: a *galvanic* cell converts chemical energy to electrical work; an
  *electrolytic* cell does the reverse.
- Failure: drawing the two half-cells without an ionic path between them (no salt
  bridge / membrane → no current).
- Source: `BLM` ch. 20.

## anode — the electrode at which oxidation occurs
- Label: definition + convention. Oxidation = electron loss = the electrode that
  *sends* electrons into the external wire.
- Prereqs: electrochemical_cell, oxidation_reduction.
- Special case: the anode is the `−` terminal of a galvanic (discharging) cell
  but the `+` terminal of an electrolytic (driven) cell — the *reaction*, not
  the sign, defines it.
- Failure: memorising "anode = negative" and applying it to an electrolyser.
- Source: `BLM` ch. 20; `IUPAC` "anode".

## cathode — the electrode at which reduction occurs
- Label: definition + convention. Reduction = electron gain = the electrode that
  *draws* electrons from the external wire.
- Prereqs: electrochemical_cell, oxidation_reduction.
- Special case: the cathode is `+` in a galvanic cell, `−` in an electrolytic
  cell; metal is always *plated* at the cathode.
- Failure: as for the anode — sign vs reaction.
- Source: `BLM` ch. 20; `IUPAC` "cathode".

## salt_bridge — an ionic conductor joining two half-cells, completing the circuit while limiting mixing
- Label: physical_definition. Typically KCl or KNO₃ in a gel (ions of nearly
  equal mobility, so it adds little junction potential).
- Prereqs: electrochemical_cell, electrolyte.
- Special case: without it, charge builds up in each half-cell and the current
  stops almost immediately.
- Failure: using a salt whose ion reacts with a half-cell (Cl⁻ with Ag⁺).
- Source: `BLM` ch. 20.

## ion_exchange_membrane — a selective separator that passes one sign (or one species) of ion and blocks the rest
- Label: physical_definition. Cation-exchange (Nafion-type, passes `Na⁺`/`H⁺`) or
  anion-exchange.
- Prereqs: salt_bridge, transport_number.
- Special case: the chlor-alkali membrane passes `Na⁺` to the catholyte but
  blocks `Cl⁻` and `OH⁻`, keeping the NaOH product free of chloride.
- Failure: assuming perfect selectivity — real membranes leak (crossover), which
  sets a flow battery's coulombic efficiency and capacity fade.
- Source: `Pletcher` ch. 3; `Skyllas-Kazacos` §4.

## cell_notation — `anode | anolyte ‖ catholyte | cathode`, oxidation on the left
- Label: convention. `|` a phase boundary, `‖` the salt bridge / membrane.
- Prereqs: anode, cathode, salt_bridge.
- Special case: Daniell cell `Zn(s) | Zn²⁺(aq) ‖ Cu²⁺(aq) | Cu(s)`.
- Failure: writing reduction on the left; omitting states or concentrations.
- Source: `IUPAC` "cell diagram"; `Atkins` ch. 6.

## galvanic_cell — a cell whose reaction is spontaneous, delivering electrical work (`E°_cell > 0`)
- Label: definition. Also "voltaic cell". A discharging battery is galvanic.
- Prereqs: spontaneity_from_cell_potential.
- Special case: `ΔG = −zFE_cell < 0`; the cell drives current through an external
  load until `Q → K` and `E → 0`.
- Failure: assuming a galvanic cell stays at `E°` under load — the terminal
  voltage sags by the overpotentials and `IR` drop.
- Source: `BLM` ch. 20.

## electrolytic_cell — a cell driven by an external source to run a non-spontaneous reaction (`E°_cell < 0`)
- Label: definition. Electrolysis, electroplating, electrowinning, battery
  charging.
- Prereqs: spontaneity_from_cell_potential, electric_potential.
- Special case: the source must supply at least `|E°_cell|` (the reversible
  decomposition voltage) plus the overpotentials and `IR` drop.
- Failure: expecting the product at exactly `|E°_cell|` — real electrolysers run
  well above it.
- Source: `BLM` ch. 20; `Pletcher` ch. 1.

---

# Electrode potentials

## standard_hydrogen_electrode — `2H⁺(a = 1) + 2e⁻ ⇌ H₂(1 bar)` with `E°(SHE) ≡ 0` at every temperature
- Label: convention. Pt-black electrode, `a(H⁺) = 1`, `p(H₂) = 1 bar`.
- Prereqs: half_reaction, standard_state, electric_potential.
- Special case: it is a *chosen zero*, not a measurement — every `E°` is a
  difference from it.
- Failure: treating `E°(SHE) = 0` as a physical fact about hydrogen rather than
  a reference convention.
- Source: `IUPAC` "standard hydrogen electrode"; `Bard` ch. 1.

## standard_reduction_potential — `E°`, the potential of a half-cell (all species at unit activity, 298.15 K) versus the SHE, written as a reduction
- Label: reference_data. `V`, `M L² T⁻³ I⁻¹`. More positive `E°` → stronger
  oxidant.
- Prereqs: standard_hydrogen_electrode, half_reaction.
- Special case: `F₂/F⁻ +2.87`; `Cl₂/Cl⁻ +1.36`; `O₂+4H⁺/H₂O +1.23`;
  `Ag⁺/Ag +0.80`; `Cu²⁺/Cu +0.34`; `2H⁺/H₂ 0.00`; `Fe²⁺/Fe −0.44`;
  `Zn²⁺/Zn −0.76`; `Al³⁺/Al −1.66`; `Li⁺/Li −3.04` (all V vs SHE).
- Failure: adding `E°` values when scaling a half-reaction (`E°` is intensive —
  it does not scale with `z`); using an oxidation potential (sign flipped) in
  `E°_cell = E°_cathode − E°_anode`.
- Source: `BLM` appendix E; `Bard` appendix C.

## electrochemical_series — the elements/couples ranked by `E°`
- Label: qualitative_rule. Equivalent to the "activity series" of metals.
- Prereqs: standard_reduction_potential, oxidizing_reducing_agent.
- Special case: a metal displaces from solution any metal ion below it in the
  series (Zn + Cu²⁺ → Zn²⁺ + Cu); metals below H (`E° < 0`) dissolve in acid.
- Failure: reading the *standard* order as the order under real (non-unit)
  activities, or when overpotential dominates (Zn electrowinning).
- Source: `BLM` ch. 4, ch. 20.

## cell_potential — `E_cell = E_cathode − E_anode` (both as reduction potentials at the actual conditions)
- Label: derived_formula. `V`. Positive for a galvanic cell as written.
- Prereqs: anode, cathode, standard_reduction_potential, electric_potential.
- Dimensional check: a difference of two potentials → `M L² T⁻³ I⁻¹` (consistent).
- Special case: Daniell cell `E°_cell = 0.34 − (−0.76) = 1.10 V`. Lean check 3.
- Failure: `E°_cathode + E°_anode`; forgetting to convert an oxidation potential
  back to a reduction potential.
- Source: `BLM` ch. 20; `Atkins` ch. 6.

## standard_cell_potential — `E°_cell = E°_cathode − E°_anode`, every species at unit activity
- Label: derived_formula. The `E_cell` of the Nernst equation's `E°` term.
- Prereqs: cell_potential, standard_state, balancing_redox_half_reactions.
- Special case: water electrolysis `E°_cell = 0.00 − 1.23 = −1.23 V` — negative,
  so it must be driven; `|E°_cell| = 1.23 V` is the reversible decomposition
  voltage.
- Failure: reporting `E°_cell` without stating the balanced cell reaction it
  belongs to.
- Source: `BLM` ch. 20.

## spontaneity_from_cell_potential — `E°_cell > 0` ⇔ spontaneous (galvanic); `E°_cell < 0` ⇔ must be driven (electrolytic)
- Label: qualitative_rule. From `ΔG° = −zFE°_cell`.
- Prereqs: standard_cell_potential.
- Special case: `E°_cell = 0` ⇔ `K = 1`; the *actual* direction is set by
  `E_cell` (via the Nernst `Q` term), not `E°_cell` alone.
- Failure: reading `E°_cell < 0` as "no reaction" (a little product still forms;
  `K > 0`).
- Source: `Atkins` ch. 6.

---

# The thermodynamic bridge

## gibbs_from_cell_potential — `ΔG = −z F E`
- Label: derived_exact. The cell potential is the reaction's free energy per
  coulomb of charge transferred.
- Prereqs: gibbs_free_energy, cell_potential, faraday_constant,
  electrons_per_formula_unit, electrical_work.
- Dimensional check: `[z F E] = 1 · I T N⁻¹ · M L² T⁻³ I⁻¹ = M L² T⁻² N⁻¹` = J/mol
  (consistent). Lean check 4.
- Special case: Daniell cell `ΔG° = −2 · 96485 · 1.10 = −212 kJ/mol`.
- Failure: dropping the minus sign (`E > 0` ⇒ `ΔG < 0`); using `z` inconsistent
  with the equation `ΔG` is quoted for.
- Source: `Atkins` ch. 6.

## standard_gibbs_from_cell_potential — `ΔG° = −z F E°_cell`
- Label: derived_exact. Prereqs: gibbs_from_cell_potential, standard_cell_potential.
- Special case: water `ΔG°(2H₂O → 2H₂ + O₂) = −4 · 96485 · (−1.23) = +475 kJ`
  (`= +237 kJ per mol H₂`, matching `ΔG_f°(H₂O,l) = −237`).
- Failure: mixing the per-mole basis of `ΔG°` with a different `z`.
- Source: `Atkins` ch. 6.

## equilibrium_from_cell_potential — `E°_cell = (R T / z F) ln K`  (so `ln K = z F E°_cell / R T`)
- Label: derived_exact. Combines `ΔG° = −zFE°` with `ΔG° = −RT ln K`.
- Prereqs: standard_gibbs_from_cell_potential, reaction_isotherm,
  equilibrium_constant.
- Dimensional check: `[(RT/zF)] = (M L² T⁻² Θ⁻¹ N⁻¹ · Θ)/(1 · I T N⁻¹) =
  M L² T⁻³ I⁻¹` = V (consistent; `ln K` dimensionless). Lean check 5.
- Special case: Daniell `ln K = 2 · 96485 · 1.10 / (8.314 · 298.15) = 85.6` →
  `K ≈ 1.5×10³⁷`; a `+1.10 V` cell reaction goes essentially to completion.
- Failure: `log₁₀` for `ln` (drops a factor 2.303); wrong `z`.
- Source: `Atkins` ch. 6.

## temperature_coefficient_emf — `(∂E/∂T)_P = ΔS / (z F)`
- Label: derived_formula. From `ΔG = ΔH − TΔS` and `ΔG = −zFE`.
- Prereqs: gibbs_from_cell_potential, entropy, cell_potential.
- Dimensional check: `[ΔS/(zF)] = (M L² T⁻² Θ⁻¹ N⁻¹)/(I T N⁻¹) = M L² T⁻³ Θ⁻¹ I⁻¹`
  = V/K (consistent).
- Special case: measuring `E` at two temperatures gives `ΔS`, then `ΔH = ΔG +
  TΔS` — a full thermodynamic characterisation from voltage alone.
- Failure: assuming `ΔS` is temperature-independent over a wide range.
- Source: `Atkins` ch. 6.

---

# The Nernst equation

## nernst_equation — `E = E° − (R T / z F) ln Q`
- Label: derived_exact. From `ΔG = ΔG° + RT ln Q` with `ΔG = −zFE`, `ΔG° = −zFE°`.
- Prereqs: gibbs_from_cell_potential, standard_cell_potential, reaction_quotient,
  reaction_isotherm, gas_constant, faraday_constant, electrons_per_formula_unit.
- Dimensional check: `[(RT/zF) ln Q]` = V (as in `equilibrium_from_cell_potential`);
  matches `[E°]` (consistent). Lean check 6.
- Special case: at equilibrium `Q = K`, `E = 0` — a fully discharged cell.
- Failure: writing `Q` with the wrong stoichiometric exponents; using `z` for a
  half-reaction where the cell `z` is meant.
- Source: `Atkins` ch. 6; `BLM` ch. 20.

## nernst_298k_form — `E = E° − (0.05916 V / z) log₁₀ Q`  (298.15 K)
- Label: derived_formula. `0.05916 V = R T ln 10 / F` at 298.15 K.
- Prereqs: nernst_equation.
- Special case: a ten-fold change in `Q` shifts `E` by `59.2/z mV`; for a
  pH electrode (`z = 1`) that is `−59.2 mV` per pH unit. Lean check 7.
- Failure: using `0.05916` away from 25 °C; forgetting the `/z`.
- Source: `BLM` ch. 20.

## concentration_cell — a cell with the *same* couple on both sides (`E° = 0`), driven only by a concentration difference
- Label: derived_formula. `E = −(RT/zF) ln([dilute]/[concentrated])` (the dilute
  side is the anode).
- Prereqs: nernst_equation, standard_cell_potential.
- Special case: `Cu | Cu²⁺(0.01 M) ‖ Cu²⁺(1.0 M) | Cu`:
  `E = (0.05916/2) log(1.0/0.01) = 0.0592 V`.
- Failure: assigning the anode/cathode by habit rather than by which side is more
  dilute; it also runs down as the concentrations equalise.
- Source: `BLM` ch. 20.

## cell_potential_vs_soc — `E` falls toward 0 as the cell discharges (`Q → K`)
- Label: qualitative_rule. The Nernst `Q` term is the discharge curve.
- Prereqs: nernst_equation, equilibrium_from_cell_potential, reaction_quotient.
- Special case: a vanadium flow battery's open-circuit voltage runs from
  `≈ 1.4 V` at high state of charge to `≈ 1.1 V` at low SOC, roughly the Nernst
  shape in the `VO₂⁺/VO²⁺` and `V³⁺/V²⁺` ratios.
- Failure: reading the sag under load as this thermodynamic term — most of the
  drop at high current is overpotential and `IR`, not `Q`.
- Source: `Skyllas-Kazacos` §3; `Atkins` ch. 6.

---

# Kinetics and the real cell voltage

## current_density — `j = I / A`, current normalised to electrode area
- Label: definition. `A/m²`, `I L⁻²`. The intensive variable for electrode
  kinetics and for sizing a stack.
- Prereqs: electric_current.
- Special case: water electrolysers run at `0.5–3 A/cm²`; flow-battery stacks at
  `0.05–0.3 A/cm²`; higher `j` means more power per unit area but more
  overpotential.
- Failure: comparing cells by `I` rather than `j`; using geometric area where
  the electrochemically active (roughened / porous) area is meant.
- Source: `Newman` ch. 1; `Bard` ch. 1.

## overpotential — `η = E_applied − E_equilibrium`, the excess potential needed to drive a net current at an electrode
- Label: definition. `V`. Zero at open circuit; grows with `|j|`. Split into
  `η_act + η_conc + η_ohmic`.
- Prereqs: nernst_equation, electric_potential.
- Special case: `η > 0` at an anode being driven, `η < 0` at a driven cathode;
  `|η|` always represents *lost* work.
- Failure: confusing overpotential (a per-electrode kinetic quantity) with the
  `IR` drop (a bulk resistive loss) — though the latter is often lumped in.
- Source: `Bard` ch. 1; `IUPAC` "overpotential".

## activation_overpotential — the part of `η` that overcomes the charge-transfer energy barrier at the interface
- Label: physical_definition. Dominant at low `|j|`; described by Butler–Volmer /
  Tafel.
- Prereqs: overpotential, current_density.
- Special case: large for `O₂` evolution/reduction (slow, multi-electron) and
  small for `H⁺/H₂` on Pt — which is why oxygen electrodes set the loss budget of
  electrolysers and fuel cells.
- Failure: assuming it is the same on every electrode material — it varies by
  orders of magnitude with the catalyst.
- Source: `Bard` ch. 3.

## concentration_overpotential — the part of `η` from depletion (or build-up) of the reactant at the electrode surface
- Label: physical_definition. Grows sharply as `j` approaches the mass-transport
  limiting current `j_lim`.
- Prereqs: overpotential, current_density, migration_vs_diffusion.
- Special case: `η_conc = (RT/zF) ln(1 − j/j_lim)` → diverges at `j = j_lim`;
  stirring, flow, or higher concentration raises `j_lim`.
- Failure: pushing a cell past `j_lim` (the voltage runs away and side reactions
  take over).
- Source: `Newman` ch. 1; `Bard` ch. 1.

## ohmic_drop — `η_ohmic = I R_cell`, the resistive loss in the electrolyte, separator, and contacts
- Label: derived_formula. Linear in current (`ohms_law`).
- Prereqs: ohms_law, current_density.
- Special case: minimised by a thin gap, a conductive supporting electrolyte, and
  a low-resistance membrane; often the largest single loss in an industrial cell
  at high `j`.
- Failure: treating the interface as ohmic (it is not); neglecting bubble
  coverage, which raises the effective electrolyte resistance in a gas-evolving
  cell.
- Source: `Pletcher` ch. 2.

## butler_volmer_equation — `j = j₀ [ exp(α z F η / R T) − exp(−(1−α) z F η / R T) ]`  *(stated, not derived)*
- Label: principle_law (boundary node — the microkinetic derivation is out of
  scope). `α` the transfer coefficient (≈ 0.5), `j₀` the exchange current
  density.
- Prereqs: activation_overpotential, current_density, exchange_current_density,
  gas_constant, faraday_constant, electrons_per_formula_unit.
- Dimensional check: the exponent `[z F η / R T] = (I T N⁻¹ · M L² T⁻³ I⁻¹) /
  (M L² T⁻² Θ⁻¹ N⁻¹ · Θ)` = dimensionless (consistent — required for `exp`).
  Lean check 8.
- Special case: small `η` → `j ≈ j₀ (zF/RT) η` (linear, a "charge-transfer
  resistance"); large `η` → one exponential dominates (Tafel).
- Failure: applying it where mass transport, not charge transfer, limits the
  current; assuming `α = 0.5` exactly.
- Source: `Bard` ch. 3; `Atkins` ch. 25 (stated here, not derived).

## exchange_current_density — `j₀`, the equal forward and reverse current density at `η = 0` (dynamic equilibrium)
- Label: reference_data. Ranges over ~10 orders of magnitude by couple and
  electrode material.
- Prereqs: current_density, activation_overpotential.
- Special case: `H⁺/H₂`: `j₀ ≈ 10⁻³ A/cm²` on Pt but `≈ 10⁻¹² A/cm²` on Hg (a
  huge H₂ overpotential — exploited in Zn electrowinning and once in chlor-alkali
  mercury cells). `O₂`: `j₀ ≈ 10⁻⁹ A/cm²` on most metals.
- Failure: quoting `j₀` without the electrode material, surface state, and
  electrolyte.
- Source: `Bard` appendix; `Pletcher` ch. 1.

## tafel_equation — `η_act = a + b log₁₀ j`  (the high-overpotential limit of Butler–Volmer)
- Label: empirical_law. `b = 2.303 RT / (α z F)` is the Tafel slope;
  `a = −b log₁₀ j₀`.
- Prereqs: butler_volmer_equation, activation_overpotential.
- Special case: `α = 0.5`, `z = 1`, 25 °C → `b ≈ 0.118 V` per decade of current
  ("120 mV/decade"); extrapolating a Tafel plot to `η = 0` reads off `j₀`.
- Failure: fitting a Tafel slope in the mixed or mass-transport region where it
  is not linear.
- Source: `Bard` ch. 3.

## decomposition_potential — the minimum applied voltage at which continuous electrolysis begins
- Label: derived_formula. `V_decomp ≈ |E°_cell| + |η_a| + |η_c|` at a small
  onset current (the `IR` term is negligible there).
- Prereqs: standard_cell_potential, overpotential, electrolytic_cell.
- Special case: water: `|E°_cell| = 1.23 V` but the observed onset is
  `≈ 1.7–1.9 V` because of the oxygen overpotential.
- Failure: equating it with `|E°_cell|`; assuming it is sharp (it is a soft
  onset set by the Tafel curves).
- Source: `Pletcher` ch. 1.

## cell_voltage_electrolysis — `V_cell = E°_cell + |η_anode| + |η_cathode| + I R_cell`
- Label: derived_formula. The voltage a source must supply to drive the cell at
  current `I`. (`E°_cell` here is the magnitude of the reversible decomposition
  voltage.)
- Prereqs: standard_cell_potential, activation_overpotential,
  concentration_overpotential, ohmic_drop, electrolytic_cell.
- Special case: alkaline water electrolysis at `0.3 A/cm²`: `≈ 1.23 + 0.10 +
  0.30 + 0.35 ≈ 1.9–2.0 V` — only ~65 % of the input energy ends up as `ΔG` of
  H₂. Lean check 9 checks the additive bookkeeping.
- Failure: leaving out any term; using it for the discharge direction (the signs
  of the `η` and `IR` terms flip).
- Source: `Pletcher` ch. 3.

## cell_voltage_discharge — `V_cell = E°_cell − |η_anode| − |η_cathode| − I R_cell`
- Label: derived_formula. The terminal voltage a galvanic cell delivers at
  current `I`; always below `E_cell`.
- Prereqs: standard_cell_potential, activation_overpotential,
  concentration_overpotential, ohmic_drop, galvanic_cell.
- Special case: a vanadium flow battery: `≈ 1.26 − losses ≈ 1.2–1.3 V`
  discharging vs `1.5–1.6 V` charging — the gap is the voltage inefficiency.
- Failure: reporting `E°_cell` as the delivered voltage.
- Source: `Skyllas-Kazacos` §3.

---

# Product selectivity

## competing_electrode_reactions — more than one half-reaction is thermodynamically possible at a given electrode potential
- Label: qualitative_rule. The one that actually runs is set by `E`, kinetics
  (overpotential / `j₀`), and concentration.
- Prereqs: standard_reduction_potential, half_reaction, electrode.
- Special case: at a cathode in aqueous solution, metal deposition competes with
  `H₂` evolution; at an anode, the target oxidation competes with `O₂` evolution
  (and `Cl₂` if chloride is present).
- Failure: assuming the reaction with the most favourable `E°` always dominates —
  overpotential routinely overrides it.
- Source: `Pletcher` ch. 1.

## thermodynamic_vs_kinetic_product — overpotential can make a less thermodynamically favoured reaction the observed product
- Label: qualitative_rule. Compare *effective* potentials `E° ± η`, not `E°`
  alone.
- Prereqs: competing_electrode_reactions, overpotential, standard_cell_potential.
- Special case: chlor-alkali — `E°(O₂) = 1.23 V < E°(Cl₂) = 1.36 V`, so
  thermodynamics favours `O₂`, but `O₂` has `~0.4–0.6 V` overpotential on the DSA
  anode while `Cl₂` has almost none, so `Cl₂` is what evolves.
- Failure: predicting the product from a table of `E°` without the overpotentials
  for that specific electrode.
- Source: `Pletcher` ch. 3.

## oxygen_overpotential — the (large) activation overpotential for the oxygen evolution reaction, `2H₂O → O₂ + 4H⁺ + 4e⁻`
- Label: reference_data. `~0.3–0.6 V` at practical `j` on the best oxide
  catalysts (RuO₂, IrO₂, NiOOH); higher on most metals.
- Prereqs: activation_overpotential, half_reaction.
- Special case: it is why (a) water electrolysers need `~1.9 V` not `1.23 V`,
  (b) chlorine wins over oxygen in chlor-alkali, and (c) metals with `E°` a few
  tenths below `0` (Zn, `−0.76 V`) can still be electrowon from aqueous solution.
- Failure: assuming it is a fixed number — it depends strongly on catalyst, `j`,
  pH, and temperature.
- Source: `Pletcher` ch. 3; `Bard` ch. 15.

## electrode_material_selection — choosing the electrode for its inertness, its overpotential for the wanted vs unwanted reaction, its conductivity, stability, and cost
- Label: qualitative_rule.
- Prereqs: oxygen_overpotential, exchange_current_density,
  competing_electrode_reactions.
- Special case: dimensionally stable anodes (DSA — RuO₂/TiO₂ on Ti) for chlorine;
  Pt or IrO₂ for acid `O₂`; lead or lead-alloy anodes for sulfate electrowinning;
  carbon felt for vanadium flow batteries (cheap, wide potential window).
- Failure: using a catalyst that speeds up the *side* reaction; ignoring
  corrosion of the anode at high anodic potential.
- Source: `Pletcher` ch. 3.

## supporting_electrolyte — an inert salt/acid/base added to carry the current and set the conductivity without being consumed
- Label: physical_definition. Also suppresses migration of the electroactive
  species (so it arrives by diffusion, making the current analysable).
- Prereqs: electrolyte, conductivity, ionic_conduction.
- Special case: `H₂SO₄` in copper refining and zinc electrowinning; `NaOH` in
  alkaline electrolysers; `1 M` KCl in a voltammetry cell.
- Failure: choosing an ion that is itself reduced or oxidised in the working
  potential window.
- Source: `Bard` ch. 1.

---

# Electrolyte transport

## ionic_conduction — current carried through an electrolyte by ions drifting under the electric field
- Label: physical_definition. Cations drift toward the cathode, anions toward the
  anode; both contribute to the current.
- Prereqs: electric_current, electric_potential, electrolyte.
- Special case: unlike a metal (electrons only), an electrolyte's carriers are
  consumed/produced at the electrodes and must be replenished by the cell
  reaction and by transport.
- Failure: assuming conduction is by electrons; ignoring that ion transport
  numbers are generally unequal.
- Source: `Atkins` ch. 16.

## conductivity — `κ`, the current density per unit field in an electrolyte (`κ = 1/ρ`, from the measured resistance and cell geometry)
- Label: definition. `S/m`, `I² T³ M⁻¹ L⁻³`.
- Prereqs: ionic_conduction, ohms_law.
- Special case: `0.1 M` KCl has `κ ≈ 1.29 S/m` at 25 °C (a common calibration
  standard); `1 M` H₂SO₄ `≈ 43 S/m`; pure water `≈ 5.5×10⁻⁶ S/m`.
- Failure: comparing `κ` across concentrations to judge "how good" an ion is —
  use molar conductivity for that.
- Source: `Atkins` ch. 16.

## molar_conductivity — `Λ_m = κ / c`, conductivity per unit concentration
- Label: definition. `S m² mol⁻¹`, `I² T³ M⁻¹ L⁻² N⁻¹`.
- Prereqs: conductivity, molarity.
- Special case: for a strong electrolyte `Λ_m` falls slightly as `√c` rises
  (Kohlrausch/Debye–Hückel–Onsager); for a weak electrolyte it falls steeply
  (less dissociation).
- Failure: forgetting the unit conversion (`S cm² mol⁻¹` vs `S m² mol⁻¹`, a
  factor `10⁴`).
- Source: `Atkins` ch. 16.

## kohlrausch_law — at infinite dilution, `Λ_m° = ν₊ λ₊° + ν₋ λ₋°` (each ion contributes independently)
- Label: empirical_law. `λ_i°` the limiting molar ionic conductivity.
- Prereqs: molar_conductivity, dilute_ideal_solution.
- Special case: `Λ_m°(KCl) = λ°(K⁺) + λ°(Cl⁻) = 73.5 + 76.3 = 149.8 S cm² mol⁻¹`;
  `H⁺` (`349.8`) and `OH⁻` (`198.6`) are anomalously high (Grotthuss proton
  hopping) — why acids and bases conduct so well.
- Failure: applying the additive rule at finite concentration; using it for a
  weak electrolyte without the dissociation correction.
- Source: `Atkins` ch. 16.

## ionic_mobility — `u = v_drift / E_field`, the steady drift speed of an ion per unit field
- Label: definition. `m² V⁻¹ s⁻¹`, `I T² M⁻¹`. `λ_i° = z_i F u_i`.
- Prereqs: ionic_conduction, electric_potential.
- Special case: most small ions have `u ≈ 5×10⁻⁸ m² V⁻¹ s⁻¹`; `H⁺` is `~7×`
  larger.
- Failure: confusing mobility (a transport property) with `j₀` (a kinetic
  property of the electrode reaction).
- Source: `Atkins` ch. 16.

## transport_number — `t_i = I_i / I_total = ν_i u_i |z_i| / Σ ν_j u_j |z_j|`, the fraction of current carried by ion `i` (`Σ t_i = 1`)
- Label: definition. Dimensionless.
- Prereqs: ionic_mobility, electric_current, ionic_conduction.
- Special case: `t₊(KCl) ≈ 0.49`, `t₋ ≈ 0.51` — nearly equal, which is why KCl
  makes a good salt bridge (small liquid-junction potential). In HCl `t(H⁺) ≈
  0.82`.
- Failure: assuming `t₊ = t₋ = 0.5` for every salt; ignoring that a membrane's
  effective transport numbers differ from the bulk solution's.
- Source: `Atkins` ch. 16.

## migration_vs_diffusion — ions move by *migration* (driven by the field) and by *diffusion* (driven by a concentration gradient); convection adds a third mode
- Label: qualitative_rule.
- Prereqs: ionic_conduction, transport_number.
- Special case: adding a supporting electrolyte carries almost all the migration
  current, so the electroactive species arrives essentially by diffusion alone —
  this is what makes voltammetric currents interpretable.
- Failure: neglecting migration of the reactant when there is little or no
  supporting electrolyte (the limiting current is then larger than the diffusion
  estimate).
- Source: `Bard` ch. 4.

---

# Named production processes

## water_electrolysis — `2H₂O(l) → 2H₂(g) + O₂(g)`, `E°_cell = −1.23 V`
- Label: example. Cathode `2H₂O + 2e⁻ → H₂ + 2OH⁻` (or `2H⁺ + 2e⁻ → H₂`); anode
  `2H₂O → O₂ + 4H⁺ + 4e⁻`. `z = 4` per O₂ (`2` per H₂). Alkaline (KOH) or PEM
  (acid, solid polymer).
- Prereqs: electrolytic_cell, half_reaction, standard_cell_potential,
  faradays_law_electrolysis, gas_volume_electrolysis, cell_voltage_electrolysis,
  oxygen_overpotential.
- Special case: real `V_cell ≈ 1.8–2.0 V`; at `1.8 V` the energy efficiency
  (relative to the `1.23 V` HHV-neutral figure, or `1.48 V` thermoneutral) is
  `≈ 1.48/1.8 ≈ 82 %`. Products come off `H₂ : O₂ = 2 : 1` by volume;
  `≈ 0.42 L H₂` (STP) per kA·s.
- Failure: ignoring the oxygen overpotential when estimating the voltage;
  assuming `1.23 V` is achievable.
- Source: `Pletcher` ch. 3.

## reversible_fuel_cell — the same H₂/O₂ cell run spontaneously: `2H₂ + O₂ → 2H₂O`, `E°_cell = +1.23 V`
- Label: example (one node — fuel-cell engineering is out of scope). It is the
  electrolyser's cell reaction reversed; `ΔG° = −4F(1.23) = −475 kJ` (`−237
  kJ/mol H₂`).
- Prereqs: water_electrolysis, galvanic_cell, cell_voltage_discharge,
  gibbs_from_cell_potential.
- Special case: a device that does both (electrolyse when power is cheap,
  discharge when it is scarce) is a "regenerative" or "unitised" fuel cell — a
  hydrogen analogue of a flow battery, with the energy stored as compressed gas.
- Failure: expecting the round trip to approach 100 % — the oxygen electrode's
  overpotential is paid in *both* directions (`~1.9 V` in, `~0.7–0.8 V` out ⇒
  `~40 %` round trip).
- Source: `Pletcher` ch. 3; `Atkins` ch. 6.

## chlor_alkali_process — `2NaCl + 2H₂O → Cl₂ + H₂ + 2NaOH`, membrane cell
- Label: example. Anode `2Cl⁻ → Cl₂ + 2e⁻` (DSA); cathode `2H₂O + 2e⁻ → H₂ +
  2OH⁻`; a cation membrane passes `Na⁺` to the catholyte. `E°_cell ≈ −2.2 V`;
  real `V_cell ≈ 3–4 V`.
- Prereqs: electrolytic_cell, half_reaction, ion_exchange_membrane,
  thermodynamic_vs_kinetic_product, oxygen_overpotential,
  faradays_law_electrolysis, current_efficiency.
- Special case: `Cl₂` evolves although `E°(O₂) < E°(Cl₂)` — the DSA anode gives
  `O₂` a large overpotential and `Cl₂` almost none. `η_F ≈ 0.96` for NaOH; the
  membrane keeps chloride out of the caustic.
- Failure: predicting `O₂` from the `E°` table; running the brine too dilute (the
  `Cl₂` current efficiency then falls as `O₂` takes over).
- Source: `Pletcher` ch. 3.

## chlorate_perchlorate — `Cl⁻ → ClO₃⁻ → ClO₄⁻` by successive anodic oxidation (undivided cell, no membrane)
- Label: example. `NaClO₃`: `Cl⁻ + 3H₂O → ClO₃⁻ + 6H⁺ + 6e⁻` (partly via
  hypochlorite in solution); `NaClO₄`: `ClO₃⁻ + H₂O → ClO₄⁻ + 2H⁺ + 2e⁻` on a
  PbO₂ or Pt anode.
- Prereqs: chlor_alkali_process, competing_electrode_reactions, current_efficiency.
- Special case: chlorate current efficiency (`~90–95 %`) depends on pH, temperature,
  and a chromate additive that suppresses cathodic reduction of the product.
- Failure: expecting high efficiency without controlling the cathodic
  back-reduction; using an anode that pits at the high perchlorate potential.
- Source: `Pletcher` ch. 3.

## hall_heroult_process — `2Al₂O₃ + 3C → 4Al + 3CO₂`, alumina dissolved in molten cryolite (Na₃AlF₆) at ~960 °C
- Label: example. Cathode `Al³⁺ + 3e⁻ → Al(l)`; anode `C + 2O²⁻ → CO₂ + 4e⁻`
  (the carbon anode is consumed). `z = 3` per Al.
- Prereqs: electrolytic_cell, half_reaction, faradays_law_electrolysis,
  specific_energy_consumption, standard_cell_potential.
- Special case: `V_cell ≈ 4.2 V` (only `~1.2 V` is thermodynamic; the rest is
  anode overpotential and the `IR` drop through the bath), `η_F ≈ 0.93` →
  `≈ 13–15 kWh/kg Al`. Recycling aluminium needs `~5 %` of this.
- Failure: applying aqueous `E°` values (this is a molten-salt cell); ignoring
  that the carbon anode adds `CO₂` to the mass and energy balance.
- Source: `Pletcher` ch. 3; industry data.

## copper_electrorefining — impure copper anode dissolves; pure copper plates on the cathode
- Label: example. Both electrodes `Cu²⁺ + 2e⁻ ⇌ Cu`, so `E°_cell ≈ 0`; the
  applied voltage (`~0.2–0.3 V`) just covers the overpotentials and `IR` drop.
- Prereqs: electrolytic_cell, half_reaction, standard_reduction_potential,
  faradays_law_electrolysis, current_efficiency, competing_electrode_reactions.
- Special case: metals nobler than Cu (Ag, Au, Pt) do not dissolve and fall as
  "anode slime" (a valuable by-product); metals less noble (Fe, Ni, Zn) dissolve
  but do not plate, staying in solution. `η_F ≈ 0.95`.
- Failure: letting the electrolyte build up base metals until they co-deposit;
  running `j` so high that dendrites bridge to the anode.
- Source: `Pletcher` ch. 3.

## zinc_electrowinning — `Zn²⁺ + 2e⁻ → Zn` from a purified sulfate leach solution; `2H₂O → O₂ + 4H⁺ + 4e⁻` at a Pb-alloy anode
- Label: example. `E°(Zn²⁺/Zn) = −0.76 V` is *below* `E°(H⁺/H₂) = 0` — zinc
  should not plate from water at all.
- Prereqs: copper_electrorefining, oxygen_overpotential,
  standard_reduction_potential, current_efficiency, cell_voltage_electrolysis.
- Special case: it works because `H₂` evolution has a huge overpotential on zinc
  (and the solution is rigorously purified of `j₀`-raising impurities like Co,
  Ni, Sb); `η_F ≈ 0.90`, `V_cell ≈ 3.3 V`, `≈ 3 kWh/kg Zn`. The textbook example
  of kinetics beating thermodynamics.
- Failure: assuming the activity series forbids it; tolerating trace impurities
  that catalyse `H₂` and collapse the current efficiency.
- Source: `Pletcher` ch. 3.

---

# Redox flow batteries

## redox_flow_battery — a rechargeable cell in which both active species are dissolved and stored in external tanks, pumped through a membrane stack
- Label: definition. Charges (electrolytic) and discharges (galvanic) through the
  same stack; the reaction is a reversible redox couple on each side.
- Prereqs: galvanic_cell, electrolytic_cell, ion_exchange_membrane,
  half_reaction, molarity.
- Special case: the electrodes are inert (carbon felt) — they only transfer
  electrons; no metal plates or strips (except hybrids).
- Failure: treating it like a sealed battery — it needs pumps, plumbing, tank
  headspace management, and has parasitic pump and shunt losses.
- Source: `Skyllas-Kazacos` §1.

## energy_power_decoupling — the tanks set the energy; the stack sets the power; the two are sized independently
- Label: qualitative_rule. The defining advantage of the flow architecture.
- Prereqs: redox_flow_battery.
- Special case: to store twice as many hours, add electrolyte and bigger tanks —
  the stack (the expensive part) is unchanged. A sealed battery cannot do this.
- Failure: assuming cost scales only with energy (the stack, `$/kW`, dominates at
  short duration; the electrolyte, `$/kWh`, dominates at long duration).
- Source: `Skyllas-Kazacos` §1; `Newman` ch. 22.

## flow_battery_energy_capacity — `E_stored = c · V_tank · z · F · ΔE_avg` (per tank; use the smaller of the two)
- Label: derived_formula. Equivalently the charge capacity is `Q = c V_tank z F`
  (C) `= c V_tank z F / 3600` (A·h).
- Prereqs: redox_flow_battery, energy_power_decoupling, charge_mole_electron_bridge,
  molarity, cell_potential.
- Dimensional check: `[c V_tank z F E] = (N L⁻³)(L³)(1)(I T N⁻¹)(M L² T⁻³ I⁻¹) =
  M L² T⁻²` = J (consistent). Lean check 10.
- Special case: `1.6 M` vanadium, `z = 1`, `ΔE_avg ≈ 1.3 V`, per m³:
  `Q = 1600 · 1 · 96485 = 1.54×10⁸ C = 42.9 kA·h`; `E ≈ 55.7 kWh` per m³ of one
  tank (`≈ 25–30 kWh` per m³ counting both electrolytes → the ~15–25 Wh/L that
  vanadium systems actually deliver).
- Failure: forgetting that *both* tanks scale (the usable energy is set by the
  limiting one); using the full `E°_cell` instead of the average operating
  voltage over the SOC window.
- Source: `Skyllas-Kazacos` §3.

## flow_battery_power — `P = N_cells · A_stack · j · V_cell`
- Label: derived_formula. Set by the stack: number of cells, active area,
  operating current density, and cell voltage.
- Prereqs: redox_flow_battery, energy_power_decoupling, current_density,
  cell_voltage_discharge.
- Dimensional check: `[A j V] = L² · I L⁻² · M L² T⁻³ I⁻¹ = M L² T⁻³` = W
  (consistent).
- Special case: `40` cells of `1500 cm²` at `0.1 A/cm²` and `1.3 V` →
  `P = 40 · 0.15 · 100 · 1.3 ≈ 780 W`... (per m² basis: `0.1 A/cm² · 1.3 V =
  1.3 kW/m²`). Higher `j` raises power but cuts voltage efficiency.
- Failure: quoting the open-circuit `E°_cell`; ignoring that peak power is near
  `j` where `V_cell = ½ E_cell` (and efficiency is poor there).
- Source: `Skyllas-Kazacos` §3; `Newman` ch. 22.

## state_of_charge — `SOC = c(charged form) / c(total active species)`, `0 ≤ SOC ≤ 1`
- Label: definition. Both half-cells have an SOC; they should track.
- Prereqs: redox_flow_battery, molarity, nernst_equation.
- Special case: the open-circuit voltage follows the Nernst equation in the SOC
  ratios, e.g. `E_OCV = E°_cell + (2RT/F) ln[SOC/(1−SOC)]` for the vanadium cell
  — measuring `E_OCV` (or the electrolyte colour/potential) reads the SOC.
- Failure: assuming the two sides stay balanced — crossover and gassing drive
  them apart, which is `capacity_fade`.
- Source: `Skyllas-Kazacos` §3.

## coulombic_efficiency — `η_C = Q_discharge / Q_charge`
- Label: definition. Dimensionless, `[0, 1]`. Lost to crossover, shunt currents,
  and any gassing side reactions.
- Prereqs: redox_flow_battery, charge_from_current, current_efficiency,
  crossover, shunt_current.
- Special case: well-built vanadium systems reach `η_C ≈ 0.95–0.98`; it *rises*
  with current density (less time per cycle for crossover to act).
- Failure: confusing it with energy efficiency; measuring it over a partial
  cycle.
- Source: `Skyllas-Kazacos` §3.

## voltage_efficiency — `η_V = V_discharge / V_charge` at a stated current density
- Label: definition. Dimensionless. The overpotential and `IR` losses, paid
  twice (higher `V` in, lower `V` out).
- Prereqs: redox_flow_battery, cell_voltage_discharge, cell_voltage_electrolysis.
- Special case: `≈ 0.80–0.88` for vanadium at moderate `j`; it *falls* as `j`
  rises — the opposite trend to `η_C`, so there is an optimum `j`.
- Failure: quoting it without the current density it was measured at.
- Source: `Skyllas-Kazacos` §3.

## energy_efficiency — `η_E = η_C · η_V` (round-trip)
- Label: derived_formula. Energy out per energy in over a full cycle.
- Prereqs: coulombic_efficiency, voltage_efficiency.
- Dimensional check: product of two dimensionless ratios → dimensionless
  (consistent). Lean check 11.
- Special case: vanadium `η_E ≈ 0.65–0.80` (pumping parasitics drop the *system*
  figure a few points below the stack figure). Compare Li-ion `≈ 0.90–0.95`.
- Failure: reporting the stack `η_E` as the system round-trip (omitting pump and
  shunt losses and self-discharge on standby).
- Source: `Skyllas-Kazacos` §3.

## shunt_current — parasitic ionic current that bypasses the cells through the shared electrolyte manifolds and channels
- Label: physical_definition. Every cell in a stack is ionically connected to
  every other through the common feed/return headers.
- Prereqs: redox_flow_battery, ionic_conduction, electric_potential.
- Special case: worse for tall stacks and short, wide channels; mitigated by long
  narrow channels (more ionic resistance) at the cost of pumping power.
- Failure: designing the flow field for pressure drop alone and ignoring the
  shunt-current path.
- Source: `Skyllas-Kazacos` §4; `Newman` ch. 22.

## crossover — transport of active species through the membrane from one half-cell to the other
- Label: physical_definition. By diffusion, migration, and electro-osmotic drag;
  the membrane's transport numbers are never ideal.
- Prereqs: ion_exchange_membrane, transport_number, redox_flow_battery.
- Special case: in the vanadium cell, a `V` ion that crosses is simply re-oxidised
  or re-reduced on the other side — a self-discharge and an efficiency loss, not
  a contaminant, *because it is the same element on both sides*.
- Failure: choosing a chemistry with different elements per side (Fe/Cr) and a
  leaky membrane — crossover then permanently contaminates and needs periodic
  remixing/rebalancing.
- Source: `Skyllas-Kazacos` §4.

## capacity_fade — the gradual loss of usable capacity from crossover, oxidation-state imbalance between the tanks, gassing, and side reactions
- Label: qualitative_rule. Distinguish *reversible* fade (fix by remixing the
  electrolytes / electrolytic rebalancing) from *irreversible* fade (membrane or
  electrolyte degradation).
- Prereqs: crossover, state_of_charge, redox_flow_battery.
- Special case: vanadium electrolytes can be fully restored by periodically
  mixing the two tanks and recharging — a durability advantage over sealed
  batteries; cell/stack lifetimes of 10–20 years are claimed.
- Failure: treating all fade as permanent; not scheduling rebalancing.
- Source: `Skyllas-Kazacos` §4.

## all_vanadium_flow_battery — `VO₂⁺/VO²⁺` (positive) ‖ `V³⁺/V²⁺` (negative), `E°_cell ≈ 1.26 V`
- Label: example. **The commercial reference and the fully-decoupled (true-flow)
  benchmark — the other chemistries below are read against it.** Positive:
  `VO₂⁺ + 2H⁺ + e⁻ ⇌ VO²⁺ + H₂O` (`E° ≈ +1.00 V`); negative:
  `V³⁺ + e⁻ ⇌ V²⁺` (`E° ≈ −0.26 V`); `z = 1`. Sulfuric-acid electrolyte, both
  species dissolved at every state of charge (nothing plates) so energy and
  power are genuinely independent.
- Prereqs: redox_flow_battery, crossover, standard_reduction_potential,
  half_reaction, energy_efficiency.
- Special case: one element on both sides ⇒ crossover only self-discharges
  (recoverable), no permanent cross-contamination — the reason it became the
  dominant chemistry despite vanadium's cost (`V₂O₅` is expensive and
  price-volatile).
- Failure: exceeding the ~10–40 °C window (`V₂O₅` precipitates hot, `V(II)`
  oxidises in air); running the positive side above `~1.6 V` (carbon and
  membrane degrade); assuming it is the right choice at small scale or on a
  budget (see `iron_flow_battery`).
- Source: `Skyllas-Kazacos` §2.

## iron_chromium_flow_battery — `Fe³⁺/Fe²⁺` (positive) ‖ `Cr³⁺/Cr²⁺` (negative), `E°_cell ≈ 1.18 V`
- Label: example (contrast). The original NASA flow battery: cheap, abundant
  elements.
- Prereqs: all_vanadium_flow_battery, exchange_current_density.
- Special case: the `Cr³⁺/Cr²⁺` reaction is kinetically *slow* (small `j₀`),
  needing a catalyst and elevated temperature; mixed electrolytes (Fe + Cr on
  both sides) are used so crossover does not contaminate.
- Failure: expecting vanadium-like efficiency without addressing the chromium
  electrode kinetics and hydrogen evolution on the negative side.
- Source: `Skyllas-Kazacos` §2.

## zinc_bromine_flow_battery — `Br₂/Br⁻` (positive) ‖ `Zn²⁺/Zn` (negative), `E°_cell ≈ 1.83 V`
- Label: example (contrast — a *hybrid*). Zinc metal is *plated* on the negative
  electrode during charge, so part of the capacity lives in the stack, not the
  tank.
- Prereqs: all_vanadium_flow_battery, electrolytic_cell.
- Special case: higher voltage and energy density than vanadium, but the zinc
  deposit limits how deeply/long it can charge (dendrites, passivation) and the
  bromine must be complexed and stored safely — a real hazard for an
  unsupervised installation.
- Failure: calling it a "true" flow battery — its energy is not fully decoupled
  from the stack because of the plated zinc.
- Source: `Skyllas-Kazacos` §2.

## iron_flow_battery — `Fe³⁺/Fe²⁺` (positive) ‖ `Fe²⁺/Fe⁰` (negative), `E°_cell ≈ 1.21 V`
- Label: example. **The low-cost, low-hazard chemistry — the practical choice
  for a small or off-grid installation.** Positive: `Fe³⁺ + e⁻ ⇌ Fe²⁺`
  (`E° ≈ +0.77 V`); negative: `Fe²⁺ + 2e⁻ ⇌ Fe⁰` (`E° ≈ −0.44 V`, iron *plates*
  during charge). Electrolyte: `FeCl₂` (~1.5–2 M) with a chloride supporting
  salt, `pH ≈ 1–3` (a boric-acid buffer is common).
- Prereqs: redox_flow_battery, all_vanadium_flow_battery, crossover,
  standard_reduction_potential, half_reaction, electrolytic_cell,
  competing_electrode_reactions, thermodynamic_vs_kinetic_product, capacity_fade,
  energy_efficiency.
- Special case: iron on both sides gives the vanadium crossover advantage
  (a leaked ion self-discharges, it does not contaminate) but iron chloride is
  cheap, abundant, and low-toxicity (a water-treatment coagulant, a plant
  micronutrient) and the electrolyte is only mildly acidic. Because the negative
  **plates iron**, it is a *hybrid*: energy density is low (`~10–20 Wh/L`, set by
  the plating capacity), and the energy is not fully decoupled from the stack.
  `E°_cell = 0.77 − (−0.44) = 1.21 V`. Coulombic efficiency `~0.95–0.99`, field
  round-trip `~0.65–0.75`.
- Failure: expecting vanadium-like energy density (the plating limit caps it, so
  the tanks are ~1.5–2× larger per kWh); neglecting pH control and periodic
  electrolytic **rebalancing** (see the H₂ side reaction below); deep-cycling
  past the plated-iron inventory (the negative runs out before the positive).
- Side reaction: during charge, at the negative, `2H⁺ + 2e⁻ → H₂` (`E° = 0`)
  competes with iron plating (`E° = −0.44 V`). Iron plates anyway — hydrogen
  evolution on iron is kinetically slow (a large overpotential), the same
  effective-potential logic as `thermodynamic_vs_kinetic_product` — but the
  small parasitic H₂ current shifts the two tanks out of oxidation-state balance
  (`capacity_fade`), corrected by periodically re-reducing the positive
  electrolyte.
- Source: `Newman` ch. 22; Hruska & Savinell, *J. Electrochem. Soc.* 128 (1981)
  18; ESS Inc. technical literature.

## zinc_iron_flow_battery — `Zn/Zn(OH)₄²⁻` (negative) ‖ `Fe(CN)₆³⁻/⁴⁻` (positive), alkaline, `E°_cell ≈ 1.5–1.8 V`
- Label: example (contrast). Negative: `Zn(OH)₄²⁻ + 2e⁻ ⇌ Zn + 4OH⁻`
  (`E° ≈ −1.2 V` in base, zinc plates on charge); positive:
  `Fe(CN)₆³⁻ + e⁻ ⇌ Fe(CN)₆⁴⁻` (`E° ≈ +0.36 V`). `KOH` electrolyte.
- Prereqs: all_vanadium_flow_battery, iron_flow_battery, zinc_bromine_flow_battery,
  standard_reduction_potential, half_reaction.
- Special case: ferro/ferricyanide is very low toxicity — the Fe–CN bond is
  extremely stable (`Fe(CN)₆⁴⁻` is the anti-caking additive in table salt),
  nothing like free cyanide. Cheap materials, higher cell voltage than all-iron.
  A hybrid (zinc plating), so zinc dendrites and passivation limit how deeply and
  how long it can charge.
- Failure: confusing complexed ferrocyanide with free cyanide (they are not the
  same hazard — but do not mix ferrocyanide solutions with strong acid, which
  can liberate HCN); treating it as a true flow battery (the plated zinc couples
  part of the energy to the stack).
- Source: `Newman` ch. 22; ViZn Energy literature.

## fixed_cell_battery_contrast — lead-acid, Li-ion, NiMH: the active material is inside a sealed cell, so energy and power are coupled
- Label: qualitative_rule (contrast — cell chemistry out of scope). Higher energy
  density and round-trip efficiency than flow batteries, but you cannot add hours
  without adding whole cells.
- Prereqs: energy_power_decoupling, redox_flow_battery.
- Special case: lead-acid `η_E ≈ 0.75–0.85`, `~40 Wh/kg`, `$/kWh` low but cycle
  life short; Li-ion `η_E ≈ 0.9–0.95`, `~150–250 Wh/kg`. Flow wins for long
  duration (`> ~4–8 h`) and long calendar life.
- Failure: comparing on energy density alone — for grid storage the metrics are
  `$/kWh`, cycle life, and safety.
- Source: `Newman` ch. 22.

---

# Boundary nodes (named, not developed)

## corrosion_as_galvanic_cell — spontaneous oxidation of a metal where anodic and cathodic sites coexist on one surface, short-circuited through the metal and a surface electrolyte film
- Label: qualitative_rule (boundary). Anode: `M → Mⁿ⁺ + ne⁻`; cathode (usually):
  `O₂ + 2H₂O + 4e⁻ → 4OH⁻` or `2H⁺ + 2e⁻ → H₂`.
- Prereqs: galvanic_cell, standard_reduction_potential, oxidation_reduction,
  competing_electrode_reactions.
- Special case: joining two metals (galvanic couple) makes the less noble one the
  anode and corrode faster — a sacrificial-anode (Zn, Mg) protects steel this
  way; the quantitative treatment (Pourbaix diagrams, protection-current sizing,
  passivation kinetics) is a future capsule.
- Failure: treating this node as a full corrosion-engineering method.
- Source: `Bard` ch. 15 (named here); `Pletcher` ch. 1.

## pourbaix_diagram — a map of the thermodynamically stable species of an element as a function of electrode potential `E` and `pH`
- Label: reference_data (boundary). Built from the Nernst equation for each
  relevant equilibrium; regions of immunity, corrosion, and passivation.
- Prereqs: corrosion_as_galvanic_cell, nernst_equation, standard_reduction_potential.
- Special case: the water-stability window (`H₂` and `O₂` lines, `1.23 V` apart,
  both sloping `−0.059 V` per pH unit) bounds what any aqueous electrode reaction
  can do.
- Failure: reading a Pourbaix diagram as kinetics — it says what is *stable*, not
  how fast (a passive film may protect a metal that the diagram marks
  "corrosion").
- Source: `Bard` ch. 6 (named here).

## electrical_double_layer — the nanometre-scale structure of charge and oriented solvent at an electrode–electrolyte interface, behaving as a capacitor in series with the reaction
- Label: physical_definition (boundary). Helmholtz / Gouy–Chapman / Stern models
  are out of scope.
- Prereqs: electrode, electrolyte, electric_potential.
- Special case: its capacitance (`~10–40 µF/cm²`) sets the non-Faradaic charging
  current when the potential is swept, and underlies supercapacitors.
- Failure: ignoring the double-layer charging current when interpreting a fast
  transient measurement.
- Source: `Bard` ch. 13 (named here).

## debye_huckel_onsager — `Λ_m = Λ_m° − k √c`, the falloff of molar conductivity with concentration for a strong electrolyte
- Label: empirical_law (boundary — the ionic-atmosphere derivation is out of
  scope). `k` depends on the solvent, temperature, and ion charges.
- Prereqs: kohlrausch_law, molar_conductivity, dilute_ideal_solution.
- Special case: it is the conductivity counterpart of the Debye–Hückel activity
  law; extrapolating `Λ_m` vs `√c` to `c = 0` gives `Λ_m°` for a strong
  electrolyte (Kohlrausch's original method).
- Failure: applying the `√c` law to a weak electrolyte (whose `Λ_m` drop is
  dominated by incomplete dissociation, not the ionic atmosphere).
- Source: `Atkins` ch. 16 (stated here, not derived).
