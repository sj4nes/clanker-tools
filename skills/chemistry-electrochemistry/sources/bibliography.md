# Bibliography — Release 0.1

Source keys used in `formulas/electrochemistry.md` and the node entries.

| key | reference |
|---|---|
| `BLM` | T. L. Brown, H. E. LeMay, B. E. Bursten et al., *Chemistry: The Central Science*, 14th ed., Pearson, 2018. Ch. 4 (aqueous reactions), ch. 20 (electrochemistry). |
| `Atkins` | P. Atkins, J. de Paula, J. Keeler, *Atkins' Physical Chemistry*, 11th ed., Oxford, 2018. Ch. 6 (chemical potential of electrified systems / electrochemistry), ch. 16 (ion transport), ch. 25 (electrode processes). |
| `Bard` | A. J. Bard, L. R. Faulkner, *Electrochemical Methods: Fundamentals and Applications*, 2nd ed., Wiley, 2001. Ch. 1 (overview), ch. 3 (kinetics of electrode reactions), ch. 4 (mass transfer), ch. 13 (double layer), ch. 15 (electrode reactions with coupled chemistry / corrosion). |
| `Newman` | J. Newman, K. E. Thomas-Alyea, *Electrochemical Systems*, 3rd ed., Wiley, 2004. Ch. 1 (fundamental concepts), ch. 22 (batteries / flow systems). |
| `Pletcher` | D. Pletcher, F. C. Walsh, *Industrial Electrochemistry*, 2nd ed., Blackie, 1990. Ch. 1 (fundamentals), ch. 2 (cell design), ch. 3 (inorganic electrolytic processes: chlor-alkali, chlorate, water electrolysis, Hall–Héroult, electrowinning, electrorefining). |
| `Skyllas-Kazacos` | M. Skyllas-Kazacos, C. Menictas, T. Lim, in *Prog. Energy Combust. Sci.* (redox flow battery reviews), and M. Skyllas-Kazacos et al., "Progress in flow battery research and development", *J. Electrochem. Soc.* 158 (2011) R55. §1 (architecture), §2 (chemistries), §3 (performance / efficiency), §4 (membranes, crossover, shunt currents). |
| `IUPAC` | IUPAC *Compendium of Chemical Terminology* (the Gold Book): "anode", "cathode", "standard hydrogen electrode", "electrode potential", "cell diagram", "overpotential", "charge number of cell reaction", "electrolyte". |
| `SI` | *The International System of Units (SI Brochure)*, 9th ed., BIPM, 2019. §2.3 (base units: ampere, mole), §2.3.1 (defining constants: `e`, `N_A`). |
| `CODATA` | CODATA Internationally Recommended 2018 Values of the Fundamental Physical Constants: `F = 96485.33212 C/mol`, `e = 1.602176634×10⁻¹⁹ C`, `N_A = 6.02214076×10²³ mol⁻¹`, `R = 8.314462618 J mol⁻¹ K⁻¹`. |

## Cross-capsule imports

Bridge nodes are quoted from, and their derivations remain in:

- [`chemistry-foundations`](../../chemistry-foundations/SKILL.md) — half-reactions,
  redox balancing, the mole, molar mass, mole ratio, molarity, `K` / `Q`, the
  reaction isotherm, standard state, the dilute-ideal-solution assumption, the
  ideal-gas law, molar volume.
- [`physics-thermodynamics`](../../physics-thermodynamics/SKILL.md) — Gibbs free
  energy, entropy.

Electrical primitives (`electric_charge`, `electric_current`, `electric_potential`,
`electrical_work`, `electrical_power`, `resistance`, `ohms_law`) are treated as a
root set; a future `physics-circuits` capsule would supply them with derivations.

## Numeric values quoted in entries

Standard reduction potentials are the conventional 298.15 K aqueous values as
tabulated in `BLM` appendix E and `Bard` appendix C. Limiting molar ionic
conductivities (`λ°`) and transport numbers are the 298.15 K aqueous values in
`Atkins` ch. 16 data tables. Industrial figures (cell voltages, current
efficiencies, specific energies for chlor-alkali, aluminium, zinc) are
representative values from `Pletcher` ch. 3 and standard industry references;
they vary by plant and technology generation and are used only for
order-of-magnitude worked examples. Flow-battery performance ranges are from
`Skyllas-Kazacos`.
