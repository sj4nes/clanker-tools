# Formula and concept entries — Release 0.1

A view generated from and reconciled against the graph. Each entry: statement,
symbols (SI unit and `[M L T Θ N]` dimension where quantitative), exactness
label, assumptions, direct prerequisites, one limiting/special case, failure
modes, source. Dimensional checks: `validation/dimensional-checks.bc`.
Algebraic-identity checks: `validation/derivation-checks.lean`.

**Conventions:** amount in mol; molar mass in g/mol; `T` in K for every gas and
equilibrium expression; thermochemical sign `ΔU = q − w` (work by system
positive), `ΔH < 0` exothermic; `K`, `Q` dimensionless (each `[X]` means
molarity ÷ `1 mol/L`, each `P` means pressure ÷ `1 bar`). See `conventions.md`.

Source keys: `BLM` Brown/LeMay 14e; `Ox` Oxtoby 8e; `Zum` Zumdahl 10e;
`Atkins` Atkins 11e; `IUPAC` Gold Book; `SI` SI Brochure 9e; `CODATA` CODATA
2018; `NIST-JANAF` NIST-JANAF tables.

Exactness labels used: `primitive`, `definition`, `conservation_law`,
`empirical_law`, `constitutive_model`, `mathematical_identity`, `derived_exact`,
`derived_formula`, `bridge_imported`, `approximation`, `qualitative_rule`,
`bookkeeping_procedure`, `reference_data`, `convention`, `assumption`.

---

# Foundations and math

## si_units — the SI base quantities, with the mole as a base unit
- Label: primitive. Seven base units; this capsule uses metre, kilogram, second,
  kelvin, and **mole**. The mole is fixed by `N_A = 6.02214076×10²³ mol⁻¹`
  exactly (2019 redefinition).
- Prereqs: none (root).
- Special case: "amount of substance" (mol) and "mass" (kg) are different base
  quantities — a mole of a substance is a fixed *count*, its mass depends on the
  substance.
- Failure: treating "mole" as a mass or a volume; using g where the
  SI-coherent kg is required in a physics bridge formula.
- Source: `SI` §2.3; `CODATA`.

## dimensional_analysis — track `[M L T Θ N]` exponents through every equation
- Label: convention. A necessary check: `[LHS] = [RHS]` exponent-by-exponent.
- Prereqs: si_units.
- Special case: `N` (amount) is carried explicitly — `R` is
  `M L² T⁻² Θ⁻¹ N⁻¹`, `N_A` is `N⁻¹`, a molar mass is `M N⁻¹`.
- Failure: reading a passed dimensional check as proof of correctness (wrong
  coefficient, sign, or regime still passes).
- Source: `Ox` ch. 1.

## logarithm — `log(xy) = log x + log y`, `log(x/y) = log x − log y`, `log(xⁿ) = n log x`
- Label: mathematical_identity. Base 10 (`log`) for pH; natural (`ln`) for the
  reaction isotherm. `ln x = 2.302585 · log₁₀ x`.
- Prereqs: none (root).
- Special case: `log 1 = 0`; `−log(10⁻⁷) = 7`.
- Failure: mixing bases in `ΔG° = −RT ln K` vs `pH = −log₁₀[H⁺]`; taking a log
  of a dimensioned quantity (the argument must be a pure ratio).
- Source: any algebra text.

## quadratic_formula — `x = (−b ± √(b² − 4ac)) / (2a)` for `ax² + bx + c = 0`
- Label: mathematical_identity. Prereqs: none (root).
- Special case: an ICE table for a weak acid gives `x² / (c₀ − x) = K_a`, i.e.
  `x² + K_a x − K_a c₀ = 0`; take the positive root.
- Failure: keeping the negative (unphysical) root; using the "`x ≪ c₀`"
  approximation when `K_a` is not small relative to `c₀` (check `x/c₀ < 0.05`).
- Source: any algebra text.

## ratio_proportion — `a/b = c/d ⇔ ad = bc`
- Label: mathematical_identity. The engine of every "convert through the mole"
  calculation.
- Prereqs: none (root).
- Special case: `n = m / M` is `m : M :: n : 1`.
- Failure: inverting a conversion factor; dropping units so the ratio is
  ambiguous.
- Source: any algebra text.

## summation_notation — `Σᵢ aᵢ = a₁ + a₂ + …`
- Label: mathematical_identity. Prereqs: none (root).
- Special case: `M = Σᵢ (countᵢ · A_r,ᵢ)` g/mol; `A_r(X) = Σᵢ fᵢ Aᵢ` over
  isotopes; `ΔH_rxn° = Σ n ΔH_f°(prod) − Σ n ΔH_f°(react)`.
- Failure: omitting the stoichiometric coefficient `n` as a weight in the
  thermochemistry sums.
- Source: any algebra text.

---

# Atomic structure and the periodic table

## atom — the smallest unit of an element that retains its chemical identity
- Label: primitive. A dense positive nucleus (protons + neutrons) surrounded by
  electrons; overall neutral.
- Prereqs: none (root).
- Special case: chemical change rearranges atoms among substances but does not
  create, destroy, or transmute them (contrast nuclear change — out of scope).
- Failure: treating the atom as indivisible in *all* contexts (nuclear/quantum
  structure exists — it is just not modeled here).
- Source: `BLM` ch. 2; `IUPAC` "atom".

## atomic_structure — nucleus (Z protons, N neutrons) plus Z electrons when neutral
- Label: primitive. Proton charge `+e`, electron `−e`, neutron `0`; proton and
  neutron mass ≈ 1 u, electron ≈ 1/1836 u.
- Prereqs: none (root).
- Special case: nearly all the atomic mass is in the nucleus; nearly all the
  volume is the electron cloud.
- Failure: using this capsule's shell picture for orbital energies or spectra
  (that needs the quantum capsule).
- Source: `BLM` ch. 2; `Ox` ch. 1.

## atomic_number — `Z` = number of protons in the nucleus
- Label: definition. `Z` fixes the element; a neutral atom has `Z` electrons.
- Prereqs: atomic_structure.
- Special case: an ion has `Z` protons but `Z − q` electrons for charge `+q`.
- Failure: confusing `Z` with mass number `A = Z + N`.
- Source: `BLM` ch. 2.

## element — a pure substance all of whose atoms share one atomic number
- Label: primitive. ~118 known; each has a one/two-letter symbol.
- Prereqs: atom, atomic_number.
- Special case: an element can occur as different allotropes (O₂ vs O₃, graphite
  vs diamond) — same `Z`, different bonding.
- Failure: calling a compound an "element"; conflating the element with one of
  its isotopes.
- Source: `IUPAC` "chemical element".

## periodic_table — elements ordered by increasing `Z` into periods and groups
- Label: primitive (empirical ordering). Groups (columns) collect elements with
  similar chemistry; periods (rows) end at a noble gas.
- Prereqs: element.
- Special case: group 1 = alkali metals (very reactive), group 18 = noble gases
  (nearly inert), the staircase separates metals from nonmetals.
- Failure: reading group number as a guaranteed valence for every element in it
  (transition metals, heavy p-block break the pattern).
- Source: `BLM` ch. 2, ch. 7.

## periodic_law — element properties are a periodic function of atomic number
- Label: empirical_law. The regularity is observed and systematized, not
  derived in this capsule (the driver is electron-shell structure — quantum
  capsule).
- Prereqs: periodic_table.
- Special case: ionization energy, atomic radius, and electronegativity all
  recur with period.
- Failure: expecting strict monotonicity (e.g. the N→O ionization-energy dip).
- Source: `Ox` ch. 3; `BLM` ch. 7.

## periodic_trends — radius ↓ across a period and ↑ down a group; IE and EN opposite
- Label: qualitative_rule. Across a period (→): `Z_eff` rises, radius shrinks,
  ionization energy and electronegativity rise. Down a group (↓): a new shell,
  radius grows, IE and EN fall.
- Prereqs: periodic_law, atomic_number.
- Special case: F is the most electronegative element; Cs/Fr the least (of the
  stable ones); noble gases are usually left off the EN scale.
- Failure: applying the trend across the transition series without care;
  ignoring the well-known second-period anomalies.
- Source: `BLM` ch. 7.

## electronegativity — `χ`, the tendency of a bonded atom to attract shared electrons
- Label: definition (Pauling scale, dimensionless, F ≡ 3.98). Used only
  comparatively here.
- Prereqs: periodic_trends.
- Special case: `Δχ ≳ 1.7` → treat the bond as ionic; `0 < Δχ ≲ 1.7` → polar
  covalent; `Δχ ≈ 0` → nonpolar covalent (rules of thumb, not sharp).
- Failure: using EN values to compute a dipole moment quantitatively; comparing
  values across different EN scales (Pauling vs Mulliken vs Allred–Rochow).
- Source: `BLM` ch. 8; `Ox` ch. 3.

## ionization_energy — `IE`, energy to remove the most loosely held electron from a gaseous atom
- Label: definition, J/mol (or eV/atom), `M L² T⁻² N⁻¹` per mole. Always > 0
  (endothermic).
- Prereqs: periodic_trends.
- Special case: successive IEs rise; a large jump marks a core-shell (e.g. Na
  `IE₂ ≫ IE₁`, so Na⁺ not Na²⁺).
- Failure: confusing IE (cation formation) with electron affinity (anion
  formation).
- Source: `BLM` ch. 7.

## isotope — atoms of one element (same `Z`) with different neutron number `N`
- Label: physical_definition. Notation `¹²C`, `¹⁴C`; mass number `A = Z + N`.
- Prereqs: atomic_structure, atomic_number.
- Special case: isotopes are chemically nearly identical; they differ in mass
  and in nuclear stability.
- Failure: assuming natural isotopic composition for a sample that has been
  enriched or depleted.
- Source: `BLM` ch. 2.

## isotopic_abundance — `fᵢ`, the mole fraction of isotope `i` in a natural sample
- Label: reference_data. `Σᵢ fᵢ = 1`. Measured by mass spectrometry; tabulated
  by IUPAC.
- Prereqs: isotope.
- Special case: for a mononuclidic element (F, Na, Al, P, Au…) one `fᵢ = 1` and
  `A_r` is essentially the isotope mass.
- Failure: using terrestrial averages for extraterrestrial or biologically
  fractionated samples.
- Source: `IUPAC` isotopic-abundance tables.

## atomic_mass_unit — `1 u = 1 Da = (1/12) m(¹²C) ≈ 1.66053907×10⁻²⁷ kg`
- Label: definition. `u`: unit of mass, kg, `M`. Numerically, molar mass in
  g/mol equals the average atomic mass in u.
- Prereqs: atom, si_units.
- Special case: `m(¹²C) ≡ 12 u` exactly (this defines the scale).
- Failure: confusing `u` with `g/mol` (they are numerically equal for the mean
  mass but are different quantities — mass vs mass-per-amount).
- Source: `CODATA`; `IUPAC` "unified atomic mass unit".

## relative_atomic_mass — `A_r(X) = Σᵢ fᵢ Aᵢ`, the abundance-weighted mean isotope mass in u
- Label: definition, dimensionless (mass relative to `u`). Symbols: `fᵢ` mole
  fraction of isotope `i`, `Aᵢ` its mass in u.
- Prereqs: atomic_mass_unit, isotope, isotopic_abundance, summation_notation.
- Dimensional check: `#A_r = sum f_i A_i` (consistent — dimensionless weights ×
  mass).
- Special case: Cl: `0.7576·34.969 + 0.2424·36.966 ≈ 35.45` — matches the
  tabulated standard atomic weight.
- Failure: using an isotope's exact mass where the natural average is meant, or
  vice versa; ignoring that IUPAC now gives intervals for some elements.
- Source: `IUPAC` standard atomic weights; `Ox` ch. 1.

## ion — an atom or group of atoms with a net electric charge
- Label: definition. Cation (`+`, fewer electrons than protons); anion (`−`,
  more).
- Prereqs: atom, atomic_structure.
- Special case: polyatomic ions (SO₄²⁻, NH₄⁺) carry the charge over the whole
  group; the charge is conserved in reactions (`conservation_of_charge`).
- Failure: assuming ionic charge from group number for transition metals;
  forgetting the charge when balancing.
- Source: `BLM` ch. 2.

## chemical_substance — a pure substance: one element or one compound, fixed composition
- Label: physical_definition. Distinguished from a mixture (variable
  composition, separable by physical means).
- Prereqs: element.
- Special case: a compound has a fixed mass ratio of its elements (law of
  definite proportions).
- Failure: treating a solution or an alloy as a compound.
- Source: `IUPAC` "chemical substance"; `Zum` ch. 3.

## chemical_formula — element symbols with subscripts giving the atom ratio
- Label: definition. Empirical (smallest ratio), molecular (actual count per
  molecule), or structural (connectivity). Ionic compounds have only an
  empirical (formula-unit) formula.
- Prereqs: chemical_substance, element.
- Special case: H₂O₂ molecular, HO empirical; NaCl is a formula unit, not a
  molecule.
- Failure: reading an ionic empirical formula as a discrete molecule.
- Source: `BLM` ch. 2.

---

# The mole

## avogadro_constant — `N_A = 6.02214076×10²³ mol⁻¹` (exact)
- Label: definition (fixed value, 2019 SI). `N_A`: `N⁻¹`.
- Prereqs: si_units.
- Special case: one mole of anything contains `N_A` entities; the entity must be
  specified (atoms, molecules, ions, electrons, formula units).
- Failure: leaving the entity unspecified ("a mole of oxygen" — atoms or O₂?).
- Source: `SI` §2.3.1; `CODATA`.

## amount_of_substance — `n`, the SI base quantity counting specified entities in units of the mole
- Label: primitive, mol, `N`.
- Prereqs: avogadro_constant.
- Special case: `n = 1 mol` ⇔ `N = N_A` entities.
- Failure: conflating amount (`n`, mol) with number (`N`, dimensionless) or with
  mass (`m`, kg).
- Source: `SI` §2.3.1.

## number_from_amount — `N = n · N_A`
- Label: derived_formula. `N`: count (1). `n`: mol, `N`. `N_A`: `N⁻¹`.
- Prereqs: amount_of_substance, avogadro_constant.
- Dimensional check: `#N = n N_A` → `N · N⁻¹ = 1` (consistent, dimensionless).
- Special case: `n = 2 mol` → `N = 1.204×10²⁴`.
- Failure: applying to a bulk sample without knowing the entity; rounding `N_A`
  so hard the count is meaningless.
- Source: `Ox` ch. 1.

## molar_mass — `M = m / n`, the mass per mole of a specified substance
- Label: definition. `M`: g/mol (capsule) = `M N⁻¹`. `m`: g. `n`: mol.
- Prereqs: amount_of_substance, si_units.
- Dimensional check: `#M = m / n` → `M N⁻¹` (consistent).
- Special case: numerically `M`(g/mol) = `A_r` or the formula-mass sum.
- Failure: using kg/mol where a formula expects g/mol (or vice versa) — the
  factor 1000; forgetting `M` is substance-specific.
- Source: `IUPAC` "molar mass"; `Ox` ch. 1.

## molar_mass_from_formula — `M = Σᵢ (countᵢ · A_r,ᵢ)` g/mol over the atoms in the formula
- Label: derived_formula. Prereqs: molar_mass, chemical_formula,
  relative_atomic_mass, summation_notation.
- Dimensional check: `#M = sum count_i A_r_i` (consistent — count × mass-per-mole).
- Special case: H₂SO₄: `2(1.008) + 32.06 + 4(16.00) = 98.08` g/mol.
- Failure: dropping a subscript multiplier; using nominal integer masses where
  the abundance-weighted `A_r` is standard.
- Source: `BLM` ch. 3.

## amount_from_mass — `n = m / M`
- Label: derived_formula. `n`: mol. `m`: g. `M`: g/mol.
- Prereqs: molar_mass, ratio_proportion.
- Dimensional check: `#n = m / M` → `N` (consistent).
- Special case: 18.02 g water → 1 mol; 9.01 g → 0.5 mol.
- Failure: mass/molar-mass unit mismatch; using the atomic mass of an element
  where the molecular mass (O₂ = 32.00) is meant.
- Source: `BLM` ch. 3.

## percent_composition — `%X = (countₓ · A_r,X) / M · 100`, mass percent of element X in a compound
- Label: derived_formula. Dimensionless (%).
- Prereqs: molar_mass_from_formula, chemical_formula.
- Dimensional check: `#percent = part_mass / total_mass` (consistent,
  dimensionless).
- Special case: water: `%H = 2(1.008)/18.02·100 = 11.19%`, `%O = 88.81%`; the
  percents sum to 100.
- Failure: using mole percent where mass percent is asked; rounding so the
  percents do not sum to 100.
- Source: `BLM` ch. 3.

## empirical_formula — smallest whole-number mole ratio of the elements, from mass or percent data
- Label: definition + bookkeeping_procedure. Steps: assume 100 g → grams of each
  element → `n = m/M` for each → divide all by the smallest `n` → scale to
  integers.
- Prereqs: percent_composition, amount_from_mass, ratio_proportion.
- Special case: 40.0% C, 6.7% H, 53.3% O → `3.33 : 6.7 : 3.33` → `1 : 2 : 1` →
  CH₂O.
- Failure: rounding a `1.5` or `1.33` ratio to an integer instead of scaling
  (×2, ×3); combustion-analysis O found by difference, not measured.
- Source: `BLM` ch. 3; `Zum` ch. 3.

## molecular_formula — `(empirical formula)_k` with `k = M / M(empirical)`
- Label: derived_formula. `k`: positive integer.
- Prereqs: empirical_formula, molar_mass_from_formula.
- Dimensional check: `#k = M_molecular / M_empirical` (consistent, dimensionless).
- Special case: CH₂O empirical (30.03 g/mol), measured `M = 180.2` → `k = 6` →
  C₆H₁₂O₆.
- Failure: non-integer `k` from a bad molar mass; assuming molecular = empirical
  for an ionic compound (it has no molecular formula).
- Source: `BLM` ch. 3.

---

# Reactions and stoichiometry

## chemical_reaction — a process rearranging atoms among substances, conserving every element and total charge
- Label: primitive. Reactants → products; bonds break and form; mass and charge
  are conserved (`conservation_of_mass`, `conservation_of_charge`).
- Prereqs: chemical_substance, atom.
- Special case: a physical change (melting, dissolving) rearranges nothing at the
  atomic-connectivity level and is not a reaction.
- Failure: writing a "reaction" that does not balance (violates conservation);
  including nuclear transmutation (out of scope).
- Source: `BLM` ch. 3; `IUPAC` "chemical reaction".

## conservation_of_mass — total mass of reactants = total mass of products
- Label: conservation_law. `Σ m(react) = Σ m(products)`; equivalently each
  element's atom count is preserved.
- Prereqs: chemical_reaction, atom.
- Special case: the basis for balancing by atom inventory; mass change in a
  chemical reaction from `E = mc²` is unmeasurably small.
- Failure: forgetting a gaseous product escaped (apparent mass loss); open-system
  bookkeeping.
- Source: `Zum` ch. 3; Lavoisier.

## conservation_of_charge — total charge of reactants = total charge of products
- Label: conservation_law. Essential for ionic and redox equations.
- Prereqs: chemical_reaction, ion.
- Special case: a half-reaction is balanced only when both mass *and* charge
  match across the arrow (electrons supply the charge balance).
- Failure: balancing atoms but leaving a net-charge mismatch in an ionic
  equation.
- Source: `BLM` ch. 20.

## chemical_equation — formulas of reactants and products with states and coefficients, joined by `→`
- Label: definition. `(s)`, `(l)`, `(g)`, `(aq)` label physical state;
  conditions go over the arrow.
- Prereqs: chemical_reaction, chemical_formula.
- Special case: a *net ionic* equation shows only species that change; spectator
  ions are cancelled.
- Failure: changing a subscript (that changes the substance) instead of a
  coefficient to balance.
- Source: `BLM` ch. 3.

## stoichiometric_coefficient — `νᵢ`, the whole-number multiplier on species `i` in a balanced equation
- Label: definition. By convention negative for reactants, positive for products
  in `Σ νᵢ Xᵢ = 0`; usually quoted as positive magnitudes.
- Prereqs: chemical_equation.
- Special case: coefficients are the *smallest* integer set unless a per-mole
  basis (e.g. per mole O₂) is wanted.
- Failure: reading coefficients as masses or as molecule counts in a specific
  sample rather than as ratios.
- Source: `IUPAC` "stoichiometric number"; `Ox` ch. 2.

## balancing_chemical_equations — choose coefficients so every element's atoms and the total charge match both sides
- Label: bookkeeping_procedure. Methods: inspection; algebraic (one unknown per
  species, solve the linear system); half-reaction for redox.
- Prereqs: chemical_equation, conservation_of_mass, conservation_of_charge,
  stoichiometric_coefficient.
- Special case: combustion of `C_xH_y`: balance C, then H, then O last.
- Failure: altering formulas; leaving fractional coefficients when integers are
  required; not checking charge for ionic equations.
- Source: `BLM` ch. 3; `Zum` ch. 3.

## mole_ratio — `n_B = n_A · (ν_B / ν_A)` from the balanced equation
- Label: derived_formula. `n`: mol, `N`. `ν`: dimensionless.
- Prereqs: balancing_chemical_equations, stoichiometric_coefficient,
  amount_of_substance, ratio_proportion.
- Dimensional check: `#n_B = n_A (nu_B / nu_A)` → `N` (consistent).
- Special case: N₂ + 3H₂ → 2NH₃: 1 mol N₂ needs 3 mol H₂, gives 2 mol NH₃.
- Failure: using a mass ratio in place of the mole ratio; taking `ν` from an
  unbalanced equation.
- Source: `BLM` ch. 3.

## limiting_reagent — the reactant that runs out first, found by comparing `nᵢ / νᵢ` across reactants
- Label: bookkeeping_procedure. Smallest `nᵢ / νᵢ` = limiting; it caps all
  product amounts. The others are in *excess* (leftover = initial − consumed).
- Prereqs: mole_ratio, amount_from_mass.
- Special case: 1 mol N₂ + 1 mol H₂ → H₂ limits (`1/3 < 1/1`); max NH₃ =
  `1 · 2/3 = 0.67 mol`.
- Failure: comparing raw moles instead of `nᵢ / νᵢ`; assuming the reactant of
  smaller mass or smaller moles limits.
- Source: `BLM` ch. 3; `Zum` ch. 3.

## theoretical_yield — the product amount/mass from complete consumption of the limiting reagent
- Label: derived_formula. `n_product = n_limiting · (ν_product / ν_limiting)`;
  `m = nM`.
- Prereqs: limiting_reagent, mole_ratio, molar_mass_from_formula.
- Dimensional check: chains `#n_B = n_A (nu ratio)` then `#m = n M`.
- Special case: exactly the max-product calculation from `limiting_reagent`,
  converted to mass.
- Failure: basing it on the excess reagent; forgetting to convert to the
  requested unit (g vs mol).
- Source: `BLM` ch. 3.

## percent_yield — `%yield = (actual yield / theoretical yield) · 100`
- Label: derived_formula. Same units top and bottom (both mass or both mol);
  dimensionless.
- Prereqs: theoretical_yield.
- Special case: `> 100%` signals impure/wet product or measurement error, never
  a real excess.
- Failure: comparing actual mass to a theoretical *mole* figure; using the wrong
  (non-limiting) basis for the theoretical value.
- Source: `BLM` ch. 3.

---

# Solutions

## solution — a homogeneous mixture: solute(s) dispersed molecularly/ionically in a solvent
- Label: physical_definition. Aqueous (`aq`) when the solvent is water.
- Prereqs: chemical_substance.
- Special case: an electrolyte solution conducts (ions present); a nonelectrolyte
  does not.
- Failure: treating a colloid or suspension as a true solution.
- Source: `BLM` ch. 4.

## molarity — `c = n / V`, amount of solute per litre of solution
- Label: definition. `c`: mol/L (M), `N L⁻³`. `n`: mol. `V`: L (solution, not
  solvent).
- Prereqs: solution, amount_of_substance.
- Dimensional check: `#c = n / V` → `N L⁻³` (consistent).
- Special case: 0.5 mol in 2 L → 0.25 M.
- Failure: using volume of solvent added instead of final solution volume;
  temperature dependence (volume expands) ignored for precise work.
- Source: `BLM` ch. 4.

## dilute_ideal_solution — solute–solute interactions negligible; activity ≈ concentration / c°
- Label: assumption. Every `K`, `Q`, and pH expression in this release carries
  it.
- Prereqs: solution.
- Special case: holds well below ~0.01–0.1 M for non-electrolytes; electrolytes
  deviate sooner (Debye–Hückel — out of scope).
- Failure: applying `pH = −log[H⁺]` or an equilibrium expression to concentrated
  or high-ionic-strength solutions and expecting quantitative accuracy.
- Source: `Atkins` ch. 5.

## dilution_equation — `c₁V₁ = c₂V₂` (moles of solute conserved on adding solvent)
- Label: derived_formula (from `n = cV` constant). Any consistent volume unit.
- Prereqs: molarity.
- Dimensional check: `#c V = n` both sides → `N` (consistent).
- Special case: 10 mL of 6 M HCl to 100 mL → `c₂ = 0.6 M`.
- Failure: using it across a reaction (moles not conserved then); mixing volume
  units between sides.
- Source: `BLM` ch. 4.

## solution_stoichiometry — `n = cV`, then apply the balanced-equation mole ratio
- Label: derived_formula. Bridges concentration to reaction bookkeeping.
- Prereqs: molarity, mole_ratio.
- Special case: 25.0 mL of 0.100 M AgNO₃ → `2.50×10⁻³ mol Ag⁺` → `2.50×10⁻³ mol`
  AgCl precipitate.
- Failure: skipping the mole-ratio step; using total volume where the aliquot
  volume is meant.
- Source: `BLM` ch. 4.

## titration — deliver a reagent of known concentration until it exactly consumes the analyte
- Label: bookkeeping_procedure. Read the delivered volume at the endpoint
  (indicator or instrument), take it as the equivalence point.
- Prereqs: solution_stoichiometry.
- Special case: acid–base, redox, precipitation, complexometric titrations all
  use `n(titrant) = (stoich ratio) · n(analyte)`.
- Failure: endpoint ≠ equivalence point if the indicator is poorly matched;
  unaccounted dilution of the analyte.
- Source: `BLM` ch. 4.

## equivalence_point — where `n(titrant) = (ν_titrant / ν_analyte) · n(analyte)`
- Label: definition. Solve for the unknown concentration:
  `c_analyte = c_titrant V_titrant (ν_analyte/ν_titrant) / V_analyte`.
- Prereqs: titration, mole_ratio.
- Dimensional check: `#c V (ratio) = n` (consistent).
- Special case: diprotic acid vs monobasic base → ratio 1:2, twice the titrant
  volume.
- Failure: assuming a 1:1 ratio without checking the balanced equation; using
  the endpoint volume from an over-titrated run.
- Source: `BLM` ch. 4, ch. 17.

---

# Gases

## ideal_gas_law — `P V = n R T` *(imported from `physics-thermodynamics`)*
- Label: bridge_imported / constitutive_model. `P`: Pa, `M L⁻¹ T⁻²`. `V`: m³,
  `L³`. `n`: mol, `N`. `R`: `M L² T⁻² Θ⁻¹ N⁻¹`. `T`: K, `Θ`.
- Assumption: `ideal_gas` — point molecules, no intermolecular forces; the
  low-`P`, high-`T` limit.
- Prereqs: amount_of_substance, gas_constant, dimensional_analysis.
- Dimensional check: `#P V = n R T` (consistent).
- Special case: fixed `T` → `P ∝ 1/V` (Boyle); fixed `P` → `V ∝ T` (Charles);
  fixed `P,T` → `V ∝ n` (Avogadro).
- Failure: near condensation, high pressure, the critical region — use van der
  Waals / virial; using °C instead of K.
- Source: imported; `Atkins` ch. 1; `physics-thermodynamics` `ideal_gas_law`.

## gas_constant — `R = 8.314462618 J mol⁻¹ K⁻¹` (exact, `= N_A k_B`)
- Label: reference_data. Other forms: `0.082057 L·atm·mol⁻¹·K⁻¹`;
  `8.314 L·kPa·mol⁻¹·K⁻¹`.
- Prereqs: si_units.
- Special case: pick the `R` whose units match `P` and `V` in the problem.
- Failure: unit-mismatched `R` (the single most common gas-law error).
- Source: `CODATA` 2018.

## standard_conditions_stp — IUPAC STP: `T = 273.15 K`, `P = 10⁵ Pa (1 bar)`
- Label: convention. Molar volume at STP `= 22.711 L/mol`. (Older "STP" at
  1 atm gives 22.414 L/mol; "SATP" is 298.15 K, 1 bar.)
- Prereqs: ideal_gas_law.
- Special case: quick mental check — ~22.7 L per mole of any ideal gas at STP.
- Failure: mixing the 1 bar and 1 atm conventions (0.4 L/mol difference);
  applying the molar volume off-STP.
- Source: `IUPAC` "STP"; `BLM` ch. 10.

## molar_volume — `V_m = V / n = R T / P` for an ideal gas
- Label: derived_formula. `V_m`: L/mol or m³/mol, `L³ N⁻¹`.
- Prereqs: ideal_gas_law.
- Dimensional check: `#V_m = R T / P` → `L³ N⁻¹` (consistent).
- Special case: 22.711 L/mol at IUPAC STP; 24.79 L/mol at 298.15 K, 1 bar.
- Failure: treating `V_m` as a constant of nature (it scales with `T/P`).
- Source: `BLM` ch. 10.

## mole_fraction — `xᵢ = nᵢ / n_total`, `Σᵢ xᵢ = 1`
- Label: definition. Dimensionless.
- Prereqs: amount_of_substance.
- Special case: dry air `x(N₂) ≈ 0.78`, `x(O₂) ≈ 0.21`.
- Failure: confusing with mass fraction or volume fraction (equal to `x` only
  for ideal gases).
- Source: `BLM` ch. 10; `IUPAC` "amount fraction".

## daltons_law — `P_total = Σᵢ Pᵢ` for a mixture of non-reacting ideal gases
- Label: empirical_law (exact for ideal gases). `Pᵢ` = pressure gas `i` would
  exert alone in the same `V` at the same `T`.
- Prereqs: ideal_gas_law, mole_fraction.
- Dimensional check: `#P_total = sum P_i` (all `M L⁻¹ T⁻²`, consistent).
- Special case: collecting a gas over water — subtract the water vapour pressure
  to get the dry-gas partial pressure.
- Failure: applying to reacting or strongly interacting gases; forgetting the
  vapour-pressure correction.
- Source: `BLM` ch. 10.

## partial_pressure — `Pᵢ = xᵢ · P_total`
- Label: definition (follows from Dalton + ideal gas). `Pᵢ`: Pa.
- Prereqs: daltons_law, mole_fraction.
- Dimensional check: `#P_i = x_i P_total` → `M L⁻¹ T⁻²` (consistent).
- Special case: `K_p` for a gas equilibrium is built from partial pressures
  (÷ `P°`).
- Failure: using concentration where partial pressure is required in `K_p`;
  mole fraction on a wet basis when a dry basis is intended.
- Source: `BLM` ch. 10.

## gas_stoichiometry — combine `PV = nRT` with the balanced-equation mole ratio
- Label: derived_formula. Convert a measured `P,V,T` of one species to moles,
  apply the mole ratio, convert back if needed.
- Prereqs: ideal_gas_law, mole_ratio.
- Special case: at fixed `T,P`, gas *volumes* react in the coefficient ratio
  (Gay-Lussac) — `2 vol H₂ + 1 vol O₂ → 2 vol H₂O(g)`.
- Failure: applying the volume-ratio shortcut when `T` or `P` differ between
  measurements, or to non-gaseous species.
- Source: `BLM` ch. 10.

---

# Thermochemistry

## system_surroundings — the system is the part under study; everything else is the surroundings; together the universe
- Label: physical_definition. Boundary may be open/closed/isolated,
  rigid/movable, diathermal/adiabatic.
- Prereqs: si_units.
- Special case: for a reaction in solution, the system is usually the reacting
  species; the solvent + container are surroundings (or a defined calorimeter).
- Failure: shifting the boundary mid-problem; forgetting heat lost to the
  container.
- Source: `Atkins` ch. 2; `BLM` ch. 5.

## state_function — a property fixed by the current state, independent of path; `∮ dX = 0`
- Label: physical_definition. `U, H, S, G, T, P, V` are state functions;
  `q` and `w` are not.
- Prereqs: system_surroundings.
- Special case: this is exactly what makes Hess's law and the
  formation-enthalpy method valid.
- Failure: calling heat or work a state function ("heat content"); adding `q`
  values along different paths as if path-independent.
- Source: `Atkins` ch. 2.

## heat_work_sign_convention — `ΔU = q − w`; `q > 0` heat into system; `w > 0` work done by system
- Label: convention. `ΔH < 0` exothermic (heat leaves the system), `ΔH > 0`
  endothermic.
- Prereqs: system_surroundings.
- Special case: constant volume → `w = 0` → `ΔU = q_v`; constant pressure →
  `q_p = ΔH`.
- Failure: silent switch to `ΔU = q + w` (work on system) — flips every `w`
  sign. This capsule and its thermo bridge use `q − w`.
- Source: `conventions.md`; `Atkins` ch. 2.

## internal_energy — `U`, total kinetic + potential energy of a system's particles (state function) *(imported)*
- Label: bridge_imported. `U`: J, `M L² T⁻²`. Only differences `ΔU` are defined
  here.
- Prereqs: system_surroundings, state_function.
- Special case: isolated system → `ΔU = 0`.
- Failure: assigning an absolute `U`; forgetting `U` is extensive.
- Source: imported; `physics-thermodynamics` `internal_energy`.

## first_law_thermo — `ΔU = q − w` (energy conservation for a closed system) *(imported)*
- Label: bridge_imported / conservation_law. All terms J, `M L² T⁻²`.
- Prereqs: internal_energy, heat_work_sign_convention.
- Dimensional check: `#dU = q - w` (all energy, consistent).
- Special case: cyclic process → `ΔU = 0` → `q = w`.
- Failure: open systems (mass carries energy); wrong sign convention.
- Source: imported; `physics-thermodynamics` `first_law_thermodynamics`.

## enthalpy — `H = U + P V` (state function; `ΔH = q_p` at constant pressure) *(imported)*
- Label: bridge_imported / derived_exact. `H`: J, `M L² T⁻²`.
- Prereqs: internal_energy, first_law_thermo, state_function.
- Dimensional check: `#H = U + P V` (consistent).
- Special case: at constant `P`, `q_p = ΔH`; for reactions with no gas-mole
  change, `ΔH ≈ ΔU`.
- Failure: using `ΔH = q` when pressure is not constant; reading `H` as "total
  energy".
- Source: imported; `physics-thermodynamics` `enthalpy`.

## specific_heat_capacity — `c = q / (m ΔT)`, heat to raise unit mass by one kelvin
- Label: definition. `c`: J g⁻¹ K⁻¹, `L² T⁻² Θ⁻¹`. Molar heat capacity uses `n`
  in place of `m`.
- Prereqs: heat_work_sign_convention, si_units.
- Dimensional check: `#c = q / (m dT)` → `L² T⁻² Θ⁻¹` (consistent).
- Special case: water `c = 4.184 J g⁻¹ K⁻¹` (large — moderates climate and makes
  water a good calorimeter fluid).
- Failure: using a constant `c` across a phase change; confusing specific
  (per mass) with molar (per mole) heat capacity.
- Source: `BLM` ch. 5.

## calorimetry — `q = m c ΔT` (or `q = C ΔT` with `C` the calorimeter constant)
- Label: derived_formula. `q`: J. `ΔT = T_final − T_initial`.
- Prereqs: specific_heat_capacity.
- Dimensional check: `#q = m c dT` → `M L² T⁻²` (consistent).
- Special case: bomb calorimeter measures `q_v = ΔU`; coffee-cup measures
  `q_p = ΔH`.
- Failure: ignoring heat capacity of the calorimeter hardware; sign of `ΔT`.
- Source: `BLM` ch. 5.

## enthalpy_of_reaction — `ΔH_rxn = H(products) − H(reactants)` for the reaction as written
- Label: definition. `ΔH_rxn`: J or J/mol-of-reaction, `M L² T⁻²`. `ΔH < 0`
  exothermic.
- Prereqs: enthalpy, chemical_equation, state_function.
- Special case: reversing the reaction flips the sign; scaling the equation
  scales `ΔH` by the same factor.
- Failure: quoting `ΔH_rxn` without stating the equation and states it refers
  to; per-mole ambiguity (per mole of which species?).
- Source: `BLM` ch. 5.

## heat_of_reaction_calorimetry — `q_rxn = − q_calorimeter = − (m c ΔT)_surroundings`
- Label: derived_formula. Then `ΔH_rxn = q_rxn / n_reaction` at constant `P`.
- Prereqs: calorimetry, enthalpy_of_reaction, heat_work_sign_convention.
- Dimensional check: `#q_rxn = - m c dT` (consistent).
- Special case: temperature of the solution *rises* → `q_calorimeter > 0` →
  `q_rxn < 0` → exothermic.
- Failure: sign flip; dividing by the wrong amount (use moles of the
  limiting/basis species).
- Source: `BLM` ch. 5.

## standard_state — pure substance at `P° = 1 bar`; solutes at `1 mol/L`; `°` superscript; tables at 298.15 K
- Label: convention. The standard state does not fix temperature; it fixes
  pressure/concentration and phase reference.
- Prereqs: si_units, enthalpy.
- Special case: `ΔH_f°` of an element in its most stable form is exactly 0.
- Failure: assuming "standard" means 298.15 K by definition; mixing 1 bar and
  1 atm tabulations.
- Source: `IUPAC`; `Atkins` ch. 2.

## hess_law — `ΔH_rxn = Σ ΔH(steps)` for any pathway from the same reactants to the same products
- Label: derived_exact (because `H` is a state function). Add/reverse/scale
  known reactions; the enthalpies follow the same operations.
- Prereqs: enthalpy_of_reaction, state_function.
- Special case: `C(s) + ½O₂ → CO` (hard to measure directly) = `C + O₂ → CO₂`
  minus `CO + ½O₂ → CO₂`.
- Failure: not matching physical states between steps; scaling `ΔH` for one step
  but not its coefficients. Lean check 1.
- Source: `BLM` ch. 5; `Ox` ch. 12.

## standard_enthalpy_of_formation — `ΔH_f°`, enthalpy change forming 1 mol of a compound from its elements in their standard states
- Label: reference_data. `ΔH_f°(element, standard form) ≡ 0`. Tabulated at
  298.15 K.
- Prereqs: standard_state, enthalpy_of_reaction, chemical_formula.
- Special case: `ΔH_f°(H₂O, l) = −285.8 kJ/mol`; `(CO₂, g) = −393.5`;
  `(O₃, g) = +142.7` (endothermic to form).
- Failure: using the gas value where the liquid is produced (differs by the
  enthalpy of vaporisation); wrong standard form of the element (C as graphite,
  not diamond).
- Source: `NIST-JANAF`; `BLM` appendix C.

## enthalpy_from_formation_enthalpies — `ΔH_rxn° = Σ n ΔH_f°(products) − Σ n ΔH_f°(reactants)`
- Label: derived_exact (Hess's law applied to formation reactions).
  `n` = stoichiometric coefficient.
- Prereqs: standard_enthalpy_of_formation, hess_law, mole_ratio,
  summation_notation.
- Dimensional check: `#dH_rxn = sum n dHf(prod) - sum n dHf(react)` (all energy,
  consistent).
- Special case: CH₄ + 2O₂ → CO₂ + 2H₂O(l):
  `[−393.5 + 2(−285.8)] − [−74.8 + 0] = −890.3 kJ/mol`.
- Failure: swapping products and reactants (sign error); omitting the coefficient
  weight; wrong phase of a product. Lean check 2.
- Source: `BLM` ch. 5.

## bond_enthalpy — `D(X–Y)`, average enthalpy to break one mole of X–Y bonds in the gas phase (always > 0)
- Label: reference_data. Averaged over many molecules, so approximate for any
  one.
- Prereqs: covalent_bond, enthalpy.
- Special case: `D(H–H) = 436`, `D(C–H) ≈ 413`, `D(C=O in CO₂) ≈ 799 kJ/mol`.
- Failure: using a single-bond value for a double/triple bond; applying gas-phase
  `D` to a condensed-phase reaction without a phase-change correction.
- Source: `NIST-JANAF`; `BLM` ch. 8.

## enthalpy_from_bond_enthalpies — `ΔH_rxn ≈ Σ D(bonds broken) − Σ D(bonds formed)`
- Label: approximation (uses averaged `D`; gas phase). Small parameter: the
  spread of real bond energies around the tabulated average.
- Prereqs: bond_enthalpy, enthalpy_of_reaction, lewis_structure,
  summation_notation.
- Dimensional check: `#dH_rxn = sum D_broken - sum D_formed` (consistent).
- Special case: H₂ + Cl₂ → 2HCl: `[436 + 243] − [2(431)] = −183 kJ/mol`
  (tabulated `ΔH_f°` route gives −184.6).
- Failure: expecting formation-enthalpy accuracy; forgetting it needs correct
  Lewis structures (bond inventory); reactants/products not all gaseous.
- Source: `BLM` ch. 8.

---

# Chemical equilibrium

## reversible_reaction — a reaction that proceeds in both directions under the same conditions, written with `⇌`
- Label: physical_definition.
- Prereqs: chemical_reaction.
- Special case: essentially all reactions are reversible in principle; "goes to
  completion" means `K` is very large.
- Failure: treating `⇌` as "reaction stops"; ignoring the reverse reaction when
  `K` is moderate.
- Source: `BLM` ch. 15.

## dynamic_equilibrium — state where forward and reverse processes proceed at equal rates, so composition is constant
- Label: physical_definition. Macroscopically static, microscopically active.
  In this capsule equilibrium is characterized by `Q = K` (`ΔG = 0`), *not* by
  rate equality (kinetics is out of scope).
- Prereqs: reversible_reaction.
- Special case: adding a catalyst reaches the same equilibrium faster; it does
  not shift the position.
- Failure: thinking concentrations become equal (they become *constant*);
  believing equilibrium means the reaction has stopped.
- Source: `BLM` ch. 15.

## law_of_mass_action — at equilibrium the reaction quotient equals a constant that depends only on `T`
- Label: empirical_law (thermodynamically grounded via the reaction isotherm).
- Prereqs: dynamic_equilibrium, molarity.
- Special case: for `aA + bB ⇌ cC + dD`, `[C]^c[D]^d / ([A]^a[B]^b)` is constant
  at fixed `T`.
- Failure: assuming `K` changes with concentration or pressure (only `T` changes
  `K`; the others shift the *position*).
- Source: Guldberg & Waage; `Ox` ch. 14.

## equilibrium_constant — `K_c = Π [product]^ν / Π [reactant]^ν` (each `[X]` ÷ `c° = 1 mol/L`; dimensionless)
- Label: definition. Value depends only on `T`.
- Prereqs: law_of_mass_action, stoichiometric_coefficient, dilute_ideal_solution.
- Special case: `K ≫ 1` products favoured; `K ≪ 1` reactants favoured; `K ≈ 1`
  comparable.
- Failure: including pure solids/liquids or the solvent (see
  `heterogeneous_equilibrium`); carrying units; forgetting `K` is `T`-specific.
- Source: `BLM` ch. 15; `IUPAC` "equilibrium constant".

## reaction_quotient — `Q`, the same expression as `K` evaluated at an arbitrary (non-equilibrium) composition
- Label: definition. Dimensionless.
- Prereqs: equilibrium_constant.
- Special case: at equilibrium `Q = K`; initially with no product `Q = 0`.
- Failure: using initial concentrations and calling the result `K`; different
  concentration scale than the one `K` was defined on.
- Source: `BLM` ch. 15.

## q_versus_k — `Q < K` → net forward; `Q > K` → net reverse; `Q = K` → at equilibrium
- Label: derived_formula (sign of `ΔG = RT ln(Q/K)`).
- Prereqs: reaction_quotient, equilibrium_constant.
- Dimensional check: `Q`, `K` both dimensionless → ratio dimensionless
  (consistent).
- Special case: this is the quantitative engine behind Le Chatelier.
- Failure: reversing the inequality; comparing `Q` and `K` defined on different
  scales (`K_c` vs `K_p`).
- Source: `BLM` ch. 15.

## kp_kc_relation — `K_p = K_c (RT / P°)^{Δn}` with `Δn = Σ ν(gas products) − Σ ν(gas reactants)`
- Label: derived_formula (substitute `Pᵢ = (nᵢ/V)RT` into `K_p`, normalize by
  `c°` and `P°`).
- Prereqs: equilibrium_constant, ideal_gas_law, partial_pressure.
- Dimensional check: with `c°`, `P°` normalization both `K`s are dimensionless;
  `#(R T c° / P°)` is dimensionless (checks the `(RT)^Δn` bookkeeping).
- Special case: `Δn = 0` (e.g. H₂ + I₂ ⇌ 2HI) → `K_p = K_c` numerically.
- Failure: dropping the `P°`/`c°` normalization and getting a `K` with hidden
  units; using °C in `RT`; counting non-gas species in `Δn`. Lean check 3.
- Source: `Atkins` ch. 6; `BLM` ch. 15.

## heterogeneous_equilibrium — pure solids and pure liquids (and the solvent, dilute) are omitted from `K`
- Label: qualitative_rule (their activity ≈ 1).
- Prereqs: equilibrium_constant, chemical_substance.
- Special case: CaCO₃(s) ⇌ CaO(s) + CO₂(g) → `K = P(CO₂)/P°`; the solids do not
  appear.
- Failure: writing `[CaCO₃]` in `K`; forgetting that "amount of solid present"
  does not shift the equilibrium (as long as some is present).
- Source: `BLM` ch. 15.

## gibbs_free_energy — `G = H − T S` (state function; `ΔG` is the maximum non-expansion work) *(imported)*
- Label: bridge_imported. `G`: J, `M L² T⁻²`.
- Prereqs: enthalpy, standard_state.
- Dimensional check: `#G = H - T S` (consistent; `[T S] = Θ · M L² T⁻² Θ⁻¹`).
- Special case: at constant `T, P`, a process is spontaneous iff `ΔG < 0`.
- Failure: applying the constant-`T,P` spontaneity test at constant `V` or
  variable `T`.
- Source: imported; `physics-thermodynamics` `gibbs_free_energy`.

## gibbs_helmholtz_relation — `ΔG = ΔH − T ΔS` (for a process at constant `T`) *(imported)*
- Label: bridge_imported. All terms J or J/mol.
- Prereqs: gibbs_free_energy, enthalpy_of_reaction.
- Dimensional check: `#dG = dH - T dS` (consistent).
- Special case: sign map — `ΔH < 0, ΔS > 0` → spontaneous at all `T`;
  `ΔH > 0, ΔS < 0` → never; mixed cases have a crossover `T = ΔH/ΔS`.
- Failure: using `ΔS` in J while `ΔH` is in kJ (factor 1000); assuming `ΔH, ΔS`
  are `T`-independent over a wide range.
- Source: imported; `Atkins` ch. 3.

## spontaneity_criterion — at constant `T, P`: `ΔG < 0` spontaneous, `ΔG = 0` at equilibrium, `ΔG > 0` non-spontaneous
- Label: derived_formula (from the second law). "Non-spontaneous" = spontaneous
  in reverse, not "impossible".
- Prereqs: gibbs_free_energy.
- Special case: `ΔG°` uses standard states; the *actual* `ΔG = ΔG° + RT ln Q`
  governs a real mixture.
- Failure: reading `ΔG° > 0` as "no reaction" (a little product still forms —
  `K > 0`); confusing thermodynamic spontaneity with rate.
- Source: `Atkins` ch. 3; `BLM` ch. 19.

## reaction_isotherm — `ΔG° = − R T ln K` (and `ΔG = ΔG° + RT ln Q`) *(imported)*
- Label: bridge_imported. `ΔG°`: J/mol, `M L² T⁻² N⁻¹`. `K`: dimensionless.
- Prereqs: gibbs_free_energy, equilibrium_constant, standard_state, logarithm.
- Dimensional check: `#dG0 = - R T ln K` → `M L² T⁻² N⁻¹` (consistent; `ln K`
  dimensionless).
- Special case: `K = 1` → `ΔG° = 0`; `K = 10` at 298 K → `ΔG° = −5.7 kJ/mol`;
  factor-of-10 in `K` per 5.7 kJ/mol.
- Failure: `log₁₀` instead of `ln`; `T` in °C; a `K` that still carries units.
  Lean check 4.
- Source: imported; `Atkins` ch. 6.

## le_chatelier — a system at equilibrium, disturbed, shifts in the direction that partly counteracts the disturbance
- Label: qualitative_rule (the qualitative reading of `Q` vs `K`).
- Prereqs: dynamic_equilibrium, q_versus_k.
- Special case: add reactant → shift right; compress a gas equilibrium → shift
  toward fewer gas moles; raise `T` → shift in the endothermic direction (and
  `K` itself changes).
- Failure: predicting a shift from adding a pure solid/liquid; predicting a shift
  from a catalyst; treating an inert-gas addition at constant `V` as a
  disturbance (it is not).
- Source: `BLM` ch. 15.

## ice_table — tabulate Initial, Change (in ratio `±ν x`), Equilibrium; substitute into `K`; solve for `x`
- Label: bookkeeping_procedure. Often reduces to a quadratic; use the
  small-`x` approximation only when `x / c₀ < 0.05`.
- Prereqs: equilibrium_constant, reaction_quotient, quadratic_formula, molarity.
- Special case: weak acid `HA`, `c₀`: `K_a = x²/(c₀ − x)`; if `x ≪ c₀`,
  `x ≈ √(K_a c₀)`.
- Failure: keeping the negative root; using the approximation when it fails;
  wrong sign of "change" (decide reaction direction from `Q` vs `K` first).
- Source: `BLM` ch. 15, 16.

---

# Acids and bases

## arrhenius_acid_base — an acid releases H⁺ in water; a base releases OH⁻
- Label: definition. Narrowest of the three models used here.
- Prereqs: ion, solution.
- Special case: HCl → H⁺ + Cl⁻; NaOH → Na⁺ + OH⁻.
- Failure: cannot classify NH₃ (no OH⁻ released directly) or non-aqueous acids —
  use Brønsted–Lowry.
- Source: `BLM` ch. 4, 16.

## bronsted_lowry — an acid is a proton (H⁺) donor; a base is a proton acceptor
- Label: definition. Every acid–base reaction transfers a proton from acid to
  base.
- Prereqs: arrhenius_acid_base.
- Special case: NH₃ + H₂O ⇌ NH₄⁺ + OH⁻ — water is the acid here; water is
  *amphoteric*.
- Failure: forgetting the base must have a lone pair to accept the proton;
  Lewis acid–base (electron-pair) cases (out of scope).
- Source: `BLM` ch. 16.

## conjugate_acid_base_pair — two species differing by one H⁺: `HA` / `A⁻`
- Label: definition. The stronger an acid, the weaker its conjugate base.
- Prereqs: bronsted_lowry.
- Special case: CH₃COOH / CH₃COO⁻; NH₄⁺ / NH₃.
- Failure: pairing species that differ by more than one proton, or by an H atom
  rather than H⁺ (that would be redox).
- Source: `BLM` ch. 16.

## water_autoionization — `2H₂O ⇌ H₃O⁺ + OH⁻`; `K_w = [H⁺][OH⁻] = 1.0×10⁻¹⁴` at 25 °C
- Label: derived_formula (equilibrium constant for water). `K_w` dimensionless;
  rises with `T` (`≈ 10⁻¹⁴` only at 25 °C).
- Prereqs: bronsted_lowry, equilibrium_constant.
- Dimensional check: `[H⁺][OH⁻]` — product of two `c/c°` ratios, dimensionless
  (consistent).
- Special case: pure water: `[H⁺] = [OH⁻] = 1.0×10⁻⁷ M` → pH 7 (neutral *at
  25 °C*).
- Failure: assuming pH 7 is neutral at other temperatures; ignoring
  autoionization for very dilute strong acid (`< 10⁻⁶ M`).
- Source: `BLM` ch. 16.

## ph_definition — `pH = − log₁₀ a(H⁺) ≈ − log₁₀ ([H⁺]/c°)`
- Label: approximation (activity → concentration; `dilute_ideal_solution`).
- Prereqs: water_autoionization, logarithm, dilute_ideal_solution.
- Dimensional check: argument is `[H⁺]/c°`, dimensionless (consistent).
- Special case: `[H⁺] = 10⁻³ M` → pH 3; each pH unit is a factor of 10 in
  `[H⁺]`.
- Failure: pH of concentrated acid (activity ≪ concentration, pH can go
  negative and the formula is quantitatively off); forgetting `c°`.
- Source: `IUPAC` "pH"; `BLM` ch. 16.

## poh_relation — `pOH = − log₁₀[OH⁻]`; `pH + pOH = pK_w = 14.00` at 25 °C
- Label: derived_formula (take `−log` of `K_w = [H⁺][OH⁻]`).
- Prereqs: ph_definition, water_autoionization.
- Dimensional check: sum of two `−log(ratio)` terms = `−log K_w` (consistent).
- Special case: pOH 2 → pH 12.
- Failure: using 14.00 away from 25 °C (`pK_w` ≈ 13.0 at 60 °C).
- Source: `BLM` ch. 16.

## strong_acid_base_ph — a strong monoprotic acid fully ionizes: `[H⁺] = c(acid)`, `pH = −log c`
- Label: derived_formula. Strong base: `[OH⁻] = c` (× 2 for Ca(OH)₂), then
  `pOH`, then `pH`.
- Prereqs: ph_definition, arrhenius_acid_base, molarity.
- Special case: 0.010 M HCl → pH 2.00; 0.010 M NaOH → pOH 2.00 → pH 12.00.
- Failure: applying "100% ionized" to a weak acid; ignoring water autoionization
  below `~10⁻⁶ M`; forgetting the hydroxide multiplicity for M(OH)₂.
- Source: `BLM` ch. 16.

## weak_acid_equilibrium — `K_a = [H⁺][A⁻] / [HA]` (dimensionless); larger `K_a` = stronger acid
- Label: definition. `pK_a = −log K_a`. Solve with an ICE table.
- Prereqs: bronsted_lowry, equilibrium_constant, ice_table.
- Special case: acetic acid `K_a = 1.8×10⁻⁵` (`pK_a 4.74`); 0.10 M →
  `[H⁺] ≈ √(K_a·0.10) = 1.3×10⁻³` → pH 2.87.
- Failure: using the `x ≪ c₀` shortcut when `K_a` is not small vs `c₀`;
  neglecting water's contribution for very dilute or very weak acids.
- Source: `BLM` ch. 16.

## ka_kb_relation — for a conjugate pair, `K_a · K_b = K_w` (so `pK_a + pK_b = pK_w = 14.00` at 25 °C)
- Label: derived_exact (add the `HA` ionization and the `A⁻` hydrolysis — they
  sum to the autoionization of water).
- Prereqs: weak_acid_equilibrium, water_autoionization, conjugate_acid_base_pair.
- Dimensional check: product of two dimensionless `K`s = dimensionless `K_w`
  (consistent).
- Special case: acetic acid `K_a = 1.8×10⁻⁵` → acetate `K_b = 5.6×10⁻¹⁰`.
- Failure: pairing non-conjugate species; using values at different
  temperatures. Lean check 5.
- Source: `BLM` ch. 16.

## percent_ionization — `α = ([H⁺]_eq / c(HA)₀) · 100`
- Label: derived_formula. Dimensionless (%).
- Prereqs: weak_acid_equilibrium, ice_table.
- Special case: rises as the acid is *diluted* (Le Chatelier / Ostwald dilution
  law), even though `[H⁺]` falls.
- Failure: expecting `α` to be concentration-independent; confusing it with
  `K_a`.
- Source: `BLM` ch. 16.

## henderson_hasselbalch — `pH = pK_a + log₁₀([A⁻] / [HA])`
- Label: derived_formula (take `−log` of the `K_a` expression, solved for
  `[H⁺]`).
- Prereqs: weak_acid_equilibrium, ph_definition, logarithm.
- Dimensional check: `log` of a concentration *ratio*, dimensionless
  (consistent).
- Special case: `[A⁻] = [HA]` → `pH = pK_a` (centre of buffer capacity); useful
  band `pK_a ± 1`.
- Failure: applying when `[HA]` or `[A⁻]` is very small or comparable to
  `[H⁺]` (the approximation `[HA]_eq ≈ [HA]_0` fails); very dilute buffers.
  Lean check 6.
- Source: `BLM` ch. 17.

## buffer — a solution of a weak acid and its conjugate base that resists pH change on adding acid/base
- Label: physical_definition. Capacity is greatest when `[HA] ≈ [A⁻]` and both
  concentrations are high.
- Prereqs: weak_acid_equilibrium, conjugate_acid_base_pair, le_chatelier.
- Special case: added strong acid converts `A⁻ → HA` (and vice versa); pH moves
  only slightly per Henderson–Hasselbalch.
- Failure: expecting buffering more than ~1 unit from `pK_a`, or after the added
  acid/base exceeds the buffer component amount.
- Source: `BLM` ch. 17.

## acid_base_titration_curve — pH vs volume of titrant; shape set by the acid/base strengths
- Label: qualitative_rule. Strong–strong: sharp jump through pH 7. Weak acid +
  strong base: buffer region (pH ≈ `pK_a` at half-equivalence), equivalence at
  pH > 7 (conjugate base hydrolysis).
- Prereqs: titration, ph_definition, weak_acid_equilibrium, buffer.
- Special case: half-equivalence point → `pH = pK_a` (a way to measure `K_a`).
- Failure: assuming equivalence is always pH 7; choosing an indicator whose
  range misses the steep part of the curve.
- Source: `BLM` ch. 17.

---

# Redox bookkeeping

## oxidation_number_rules — assign each atom an oxidation number by the priority hierarchy
- Label: bookkeeping_procedure. Hierarchy: free element 0; monatomic ion =
  charge; F = −1; group 1 = +1, group 2 = +2; H = +1 (with nonmetals), −1 (with
  metals); O = −2 (except −1 in peroxides, +2 in OF₂); sum = species charge.
- Prereqs: chemical_formula, ion, electronegativity.
- Special case: Fe in Fe₂O₃ → `2x + 3(−2) = 0` → `x = +3`.
- Failure: applying rules out of priority order (assign F, then O, then H, then
  solve); confusing oxidation number with formal charge or with actual charge.
- Source: `BLM` ch. 4, 20.

## oxidation_reduction — oxidation = loss of electrons (oxidation number ↑); reduction = gain (oxidation number ↓)
- Label: definition. "OIL RIG". The two always occur together.
- Prereqs: oxidation_number_rules, ion.
- Special case: Zn + Cu²⁺ → Zn²⁺ + Cu: Zn oxidized (0 → +2), Cu reduced
  (+2 → 0).
- Failure: identifying one half without the other; using "gain/loss of oxygen"
  as the general definition (only a special case).
- Source: `BLM` ch. 20.

## oxidizing_reducing_agent — the oxidizing agent is reduced (takes electrons); the reducing agent is oxidized (gives electrons)
- Label: definition.
- Prereqs: oxidation_reduction.
- Special case: in Zn + Cu²⁺, Cu²⁺ is the oxidizing agent, Zn is the reducing
  agent.
- Failure: swapping the two (the agent's own change is opposite to the change it
  causes).
- Source: `BLM` ch. 20.

## half_reaction — the oxidation or the reduction written separately, with electrons explicit and mass + charge balanced
- Label: definition.
- Prereqs: oxidation_reduction, conservation_of_charge.
- Special case: Fe²⁺ → Fe³⁺ + e⁻ (oxidation); MnO₄⁻ + 8H⁺ + 5e⁻ → Mn²⁺ + 4H₂O
  (reduction, acidic).
- Failure: not balancing charge with electrons; forgetting H₂O/H⁺ (acidic) or
  H₂O/OH⁻ (basic) for oxygen/hydrogen balance.
- Source: `BLM` ch. 20.

## balancing_redox_half_reactions — balance each half (atoms, then O with H₂O, H with H⁺, charge with e⁻), scale to equal electrons, add
- Label: bookkeeping_procedure. Basic solution: then add OH⁻ to both sides to
  neutralize H⁺ and simplify.
- Prereqs: half_reaction, balancing_chemical_equations, conservation_of_charge.
- Special case: MnO₄⁻ + 5Fe²⁺ + 8H⁺ → Mn²⁺ + 5Fe³⁺ + 4H₂O (electrons: 5 = 5×1).
- Failure: electrons left in the final equation; not clearing H⁺ for a
  basic-solution answer; net charge not equal on both sides after adding.
- Source: `BLM` ch. 20; `Ox` ch. 11.

---

# Qualitative bonding and structure (feeder nodes)

## ionic_bond — electrostatic attraction between oppositely charged ions, formed by electron transfer (large `Δχ`)
- Label: physical_definition. Gives a 3-D lattice, not molecules; high melting
  point; conducts when molten or dissolved.
- Prereqs: ion, electronegativity.
- Special case: metal + nonmetal, `Δχ ≳ 1.7` (rule of thumb).
- Failure: drawing NaCl as a discrete molecule; a sharp ionic/covalent cutoff
  (it is a continuum).
- Source: `BLM` ch. 8.

## covalent_bond — a shared pair of electrons between two atoms (small `Δχ`)
- Label: physical_definition. Bond order 1/2/3; nonpolar (`Δχ ≈ 0`) or polar
  (`0 < Δχ ≲ 1.7`).
- Prereqs: electronegativity, atomic_structure.
- Special case: H₂ (nonpolar), HCl (polar), N₂ (triple bond).
- Failure: assuming all shared-electron bonds are equal; ignoring lone pairs
  when reasoning about geometry.
- Source: `BLM` ch. 8.

## octet_rule — main-group atoms tend toward eight valence electrons (two for H) in stable molecules
- Label: qualitative_rule. A heuristic, with well-known exceptions.
- Prereqs: atomic_structure, periodic_table.
- Special case: CO₂ (O=C=O, all octets); exceptions — BF₃ (6 on B), PCl₅,
  SF₆ (expanded), NO (odd electron).
- Failure: forcing octets on period-3+ central atoms or odd-electron species;
  using it for transition metals.
- Source: `BLM` ch. 8.

## lewis_structure — a valence-electron bookkeeping diagram: bonds as lines, lone pairs as dots
- Label: bookkeeping_procedure. Steps: count valence electrons (± charge),
  connect atoms, complete octets on outer atoms, put the rest on the central
  atom, form multiple bonds if the centre is short.
- Prereqs: covalent_bond, octet_rule, chemical_formula.
- Special case: resonance when two or more equivalent structures exist (NO₃⁻,
  O₃) — the real structure is the average.
- Failure: wrong total electron count (charge sign); exceeding the available
  electrons; a central atom that should be the least electronegative.
- Source: `BLM` ch. 8.

## formal_charge — `FC = (valence e⁻) − (lone-pair e⁻) − ½(bonding e⁻)`
- Label: derived_formula. `Σ FC = ` species charge. Prefer the Lewis structure
  with FCs closest to zero and negative FC on the more electronegative atom.
- Prereqs: lewis_structure.
- Dimensional check: an integer count identity (consistent).
- Special case: CO: C has FC −1, O has FC +1 (sums to 0).
- Failure: confusing FC with oxidation number (FC splits bonds evenly, oxidation
  number gives both electrons to the more electronegative atom).
- Source: `BLM` ch. 8.

## vsepr — electron-domain pairs around a central atom arrange to minimize repulsion, setting the geometry
- Label: qualitative_rule. 2 domains → linear; 3 → trigonal planar; 4 →
  tetrahedral; 5 → trigonal bipyramidal; 6 → octahedral. Lone pairs occupy more
  space and reduce bond angles.
- Prereqs: lewis_structure.
- Special case: H₂O — 4 domains, 2 lone pairs → bent, ~104.5°; NH₃ → trigonal
  pyramidal, ~107°.
- Failure: counting atoms instead of electron domains; forgetting lone pairs;
  using it quantitatively for exact angles.
- Source: `BLM` ch. 9.

## bond_polarity — a covalent bond is polar when the bonded atoms differ in electronegativity; dipole points to the more electronegative atom
- Label: definition. Magnitude scales with `Δχ` (qualitatively).
- Prereqs: covalent_bond, electronegativity.
- Special case: C–O and C–F bonds are strongly polar; C–H barely.
- Failure: equating bond polarity with molecular polarity (geometry can cancel
  bond dipoles).
- Source: `BLM` ch. 8.

## molecular_polarity — a molecule is polar if its bond dipoles do not vector-sum to zero
- Label: qualitative_rule. Depends on both bond polarity and VSEPR geometry.
- Prereqs: bond_polarity, vsepr.
- Special case: CO₂ (polar bonds, linear → nonpolar); H₂O (polar bonds, bent →
  polar); CCl₄ (polar bonds, tetrahedral → nonpolar).
- Failure: judging from bonds alone; ignoring lone-pair contributions to the
  dipole.
- Source: `BLM` ch. 9.

## intermolecular_forces — attractions between molecules: dispersion < dipole–dipole < hydrogen bonding (≪ covalent/ionic bonds)
- Label: qualitative_rule. Set boiling point, melting point, viscosity,
  solubility ("like dissolves like").
- Prereqs: molecular_polarity, bond_polarity.
- Special case: H₂O's hydrogen bonding → anomalously high boiling point and the
  solid being less dense than the liquid.
- Failure: comparing IMF strength to bond strength; forgetting dispersion forces
  grow with molar mass / polarizability and can outweigh a small dipole.
- Source: `BLM` ch. 11.
