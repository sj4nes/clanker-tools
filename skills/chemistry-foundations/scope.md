# Scope — Release 0.1

Knowledge capsule: **general chemistry I — the quantitative foundations**, built
with the [`physics-formula-tree`](../physics-formula-tree/SKILL.md) method
(adapted: reactions and equilibria are first-class nodes; a periodic-table /
thermochemical-data table is a cited reference the graph draws on, not derived).

This capsule is intended as the verified substrate for a later, separate
**synthesis / process capsule** (a "how to make X" tree keyed by
product → route → feedstocks → unit operations → hazards) for the homesteading /
self-sufficiency project. That layer is **not** in this release.

## Included

- SI + chemistry units: mole, molar mass (g/mol), amount concentration (mol/L),
  pressure (Pa, atm, bar, torr), and `[M L T Θ N]` dimensional analysis with
  **N (amount of substance)** first-class.
- **Atomic bookkeeping:** atomic mass unit, relative atomic mass, isotopes and
  isotopic abundance, the mole and the Avogadro constant, molar mass, percent
  composition, empirical vs molecular formula.
- **Stoichiometry:** balancing chemical equations (conservation of mass and
  charge), the mole ratio, limiting reagent, theoretical / actual / percent
  yield.
- **Solutions:** molarity, dilution `c1 V1 = c2 V2`, solution stoichiometry,
  titration to an equivalence point.
- **Gases:** the ideal-gas law as a constitutive model, molar volume at STP,
  Dalton's law of partial pressures, gas stoichiometry, mole fraction.
- **Thermochemistry:** system/surroundings, heat and work sign convention,
  enthalpy `H`, enthalpy of reaction `ΔH_rxn`, calorimetry `q = m c ΔT`,
  **Hess's law**, standard enthalpy of formation `ΔH_f°` and
  `ΔH_rxn° = Σ n ΔH_f°(products) − Σ n ΔH_f°(reactants)`, bond-enthalpy
  estimation.
- **Chemical equilibrium:** dynamic equilibrium, the reaction quotient `Q`, the
  equilibrium constant `K_c` and `K_p` with `K_p = K_c (RT)^{Δn}`, the reaction
  isotherm sign relation `ΔG° = −RT ln K` (stated; `ΔG` is imported from the
  thermodynamics capsule, not re-derived), Le Chatelier's principle as a
  qualitative rule, ICE-table solving.
- **Acids and bases:** Arrhenius and Brønsted–Lowry definitions, autoionization
  of water `K_w`, `pH = −log a(H⁺)` (activity ≈ concentration in the dilute
  limit), strong-acid/base pH, weak-acid equilibrium `K_a`, `K_a K_b = K_w`,
  the Henderson–Hasselbalch equation, buffers, and the titration curve
  qualitatively.
- **Redox bookkeeping:** oxidation number rules, identifying the oxidized and
  reduced species, balancing redox equations by half-reactions in acidic and
  basic solution.
- **Qualitative structure feeding the graph (convention/definition nodes only):**
  periodic law and periodic trends (atomic radius, ionization energy,
  electronegativity), Lewis structures and the octet rule, formal charge,
  VSEPR geometry, bond polarity and molecular polarity, intermolecular forces
  (dispersion, dipole–dipole, hydrogen bonding).

## Excluded

- **All orbital / quantum treatment of bonding** — no Schrödinger equation, no
  hydrogenic energies, no quantum numbers, no atomic-orbital shapes, no
  hybridization *as orbital mixing*, no molecular-orbital / LCAO theory, no
  crystal-field / ligand-field theory. VSEPR and hybridization *labels*
  (sp/sp²/sp³) are used only as geometry mnemonics. (A future
  `chemistry-quantum-and-bonding` capsule.)
- **Chemical kinetics** — no rate laws, no rate constants, no Arrhenius
  equation, no reaction mechanisms, no catalysis as a rate effect. Equilibrium
  is treated thermodynamically, not as forward rate = reverse rate with rate
  constants. (A future `chemistry-reaction-thermo-kinetics` capsule.)
- **Electrochemistry** — no galvanic/electrolytic cells, no standard electrode
  potentials, no Nernst equation, no Faraday's laws of electrolysis. Redox in
  this release is **balancing only**.
- **Colligative properties** (boiling-point elevation, freezing-point
  depression, osmotic pressure) beyond naming them.
- **Nuclear chemistry**, **organic chemistry** (nomenclature, functional groups,
  reaction types), **coordination chemistry**, **solid-state / materials
  chemistry**, **spectroscopy**, **analytical instrumentation**.
- **The derivation of `ΔG = ΔH − TΔS` and of `ΔG° = −RT ln K`** — imported as
  bridge nodes from [`physics-thermodynamics`](../physics-thermodynamics/SKILL.md)
  with an explicit `imported` status, not proved here.
- **Activity coefficients / non-ideal solution theory** — every `K`, `Q`, and
  `pH` expression in this release carries the `dilute_ideal_solution`
  assumption node; Debye–Hückel and beyond are out.
- **Real-gas equations of state** beyond naming van der Waals as the correction
  the ideal-gas model omits.
- Laboratory technique, measurement uncertainty, numerical root-finding for ICE
  tables (the quadratic is solved exactly; higher-degree cases are flagged, not
  solved numerically).

## Conventions

- **Math level:** algebra, logarithms (base 10 and natural), the quadratic
  formula, ratios and proportion, summation notation. No calculus is required in
  this release — `H`, `ΔH`, `ΔG` are used as state-function *differences*, not
  differentials.
- **Assumed background:** the existence of atoms, elements, and the periodic
  table as an empirical ordering; that matter is conserved in chemical change;
  elementary physics (energy, temperature, pressure = force / area). Imported,
  not re-derived.
- **Unit system:** SI with chemistry-customary units named explicitly. Amount of
  substance in **moles**; temperature in **kelvin** for all gas-law and
  equilibrium expressions (Celsius only where a node says "empirical").
  Standard state: `P° = 1 bar`, stated concentration `1 mol/L`, temperature
  **not** fixed by the standard state (default tables at 298.15 K).
- **Thermochemical sign convention:** heat added *to* the system is positive;
  work done *by* the system is positive; `ΔH < 0` is exothermic. Linked to the
  `heat_work_sign_convention` node and consistent with the thermodynamics
  capsule.
- **Exactness policy:** each node carries one label — `definition`,
  `conservation_law`, `empirical_law`, `constitutive_model`,
  `mathematical_identity`, `derived_exact`, `bridge_imported`, `approximation`,
  `qualitative_rule`, `bookkeeping_procedure`, `reference_data`, `heuristic`.
  `PV=nRT` is a `constitutive_model`; Le Chatelier is a `qualitative_rule`;
  `pH = −log[H⁺]` is an `approximation` (activity → concentration);
  Hess's law is `derived_exact` (from `H` being a state function).

## Release boundary in one line

Atoms → the mole → formulas → balanced equations → limiting reagent and yield →
solution and gas stoichiometry → thermochemistry through Hess's law →
equilibrium `K`/`Q`/ICE → acid–base `K_a`/`K_w`/buffers → redox balancing.
Everything rate-dependent, orbital-based, or electrochemical is a later capsule.
