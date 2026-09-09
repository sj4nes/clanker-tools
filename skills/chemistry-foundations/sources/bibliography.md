# Bibliography — Release 0.1

| Key | Reference |
|---|---|
| `BLM` | T. L. Brown, H. E. LeMay, B. E. Bursten et al., *Chemistry: The Central Science*, 14th ed., Pearson, 2018. |
| `Ox` | D. W. Oxtoby, H. P. Gillis, L. J. Butler, *Principles of Modern Chemistry*, 8th ed., Cengage, 2016. |
| `Zum` | S. S. Zumdahl, D. J. DeCoste, *Chemistry*, 10th ed., Cengage, 2018. |
| `Atkins` | P. Atkins, J. de Paula, *Atkins' Physical Chemistry*, 11th ed., Oxford, 2018 (for the reaction isotherm and equilibrium thermodynamics). |
| `IUPAC` | IUPAC, *Compendium of Chemical Terminology* (the "Gold Book"), 2nd ed. + online updates. |
| `SI` | BIPM, *The International System of Units (SI Brochure)*, 9th ed., 2019 (mole and `N_A` redefinition). |
| `CODATA` | CODATA 2018 recommended values of the fundamental physical constants (`N_A`, `R`). |
| `NIST-JANAF` | M. W. Chase, *NIST-JANAF Thermochemical Tables*, 4th ed., 1998 (standard enthalpies of formation, bond enthalpies). |

## Convention notes

- **Thermochemical sign convention** `ΔU = q − w`, `w` = work done *by* the
  system, `ΔH < 0` exothermic — matches [`physics-thermodynamics`](../../physics-thermodynamics/scope.md).
  `BLM` and `Zum` use `ΔE = q + w` (work done *on* the system); their `w` has
  been sign-flipped where quoted. `Atkins` uses this capsule's convention.
- **Standard state** `P° = 1 bar` per current IUPAC (older tables use 1 atm;
  the difference in `ΔH_f°` is negligible, in `S°` small — noted per node).
- **Equilibrium constants are dimensionless**: each concentration is divided by
  `c° = 1 mol/L` and each pressure by `P° = 1 bar` before forming the quotient
  (`IUPAC`, `Atkins` §6). Textbooks that write `K` with units are using the
  informal convention.
- **`ΔG° = −RT ln K` and `ΔG = ΔH − TΔS`** are quoted from `Atkins` ch. 3/6 and
  imported as bridge nodes; their derivation is in the thermodynamics capsule.
- **pH** `= −log₁₀ a(H⁺)`; this capsule uses `a(H⁺) ≈ [H⁺]/c°` (the
  `dilute_ideal_solution` node). Activity coefficients / Debye–Hückel are out of
  scope.
