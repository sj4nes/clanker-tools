/-
Release 0.1 derivation checks -- machine-checked arithmetic of the electrochemical
bookkeeping identities only.  Run:  lean validation/derivation-checks.lean
(exit 0, no output = all pass)

Lean verifies the ALGEBRA / ARITHMETIC of each identity at specific integer
values.  It does NOT verify the electrochemistry: that dG = -RT ln K (imported),
that dG = dH - T dS (imported), the Butler-Volmer rate law, or any tabulated
E0, K, molar mass, or industrial cell voltage / current efficiency.

LIMITATION: no Mathlib here, so no `ring` / `nlinarith` over the reals.  Each
identity is pinned by kernel-`decide`d INSTANCE checks over the integers
(potentials in centivolts or millivolts, charges in coulombs, energies scaled).
An instance check is weaker than a universal proof but is fully verified by the
Lean kernel.  Re-run with Mathlib to upgrade each `by decide` to `by ring`.

Constants used: F = 96485 C/mol ; R T = 2478 J/mol at 298.15 K (integer) ;
RT ln10 / F = 5916 (in units of 0.01 mV) ; RT/F = 2569 (0.01 mV).
-/

-- 1. faradays_law_electrolysis:  Q = z F n  <=>  n = Q / (z F).
--    1 F reduces 1 mol of a z = 1 species:
example : ((1 : Int) * 96485 * 1) = 96485 := by decide
--    2 F (192970 C) reduces exactly 1 mol of a z = 2 species (Cu2+ + 2e- -> Cu):
example : ((192970 : Int) / (2 * 96485)) = 1 := by decide

-- 2. Faraday volume ratio in water electrolysis.  Cathode 2 H2O + 2e- -> H2 + 2 OH-
--    (2 F per mol H2); anode 2 H2O -> O2 + 4 H+ + 4e- (4 F per mol O2).
--    Same charge Q  =>  n(H2) : n(O2) = (Q/2F) : (Q/4F) = 2 : 1.
example : ((4 : Int) / 2) = 2 := by decide
--    electron balance of the summed cell reaction: 2 H2 carry 4 e-, 1 O2 carries 4 e-.
example : ((2 : Int) * 2) = 4 * 1 := by decide

-- 3. standard_cell_potential:  E0_cell = E0_cathode - E0_anode  (reduction potentials).
--    Daniell cell, centivolts:  E0(Cu2+/Cu) = +34 ,  E0(Zn2+/Zn) = -76.
example : ((34 : Int) - (-76)) = 110 := by decide
--    all-vanadium:  E0(VO2+/VO2+) = +100 ,  E0(V3+/V2+) = -26  (centivolts).
example : ((100 : Int) - (-26)) = 126 := by decide

-- 4. gibbs_from_cell_potential:  dG = - z F E.
--    Daniell, z = 2, E = 1.10 V:  dG = -2 * 96485 * 110  (centivolt-coulombs;
--    divide by 100 for J/mol => -212267 J/mol = -212 kJ/mol).
example : (-(2 * 96485 * 110) : Int) = -21226700 := by decide
--    reversing the cell reaction flips the sign of E and of dG:
example : (-(-(2 * 96485 * 110) : Int)) = 21226700 := by decide

-- 5. equilibrium_from_cell_potential:  ln K = z F E0 / (R T).
--    Daniell: z F E0 = 2 * 96485 * 1.10 = 212267 J/mol ; R T = 2478 J/mol.
--    ln K ~ 212267 / 2478 = 85  (=> K ~ e^85, essentially complete).
example : ((212267 : Int) / 2478) = 85 := by decide

-- 6. nernst_equation at Q = K gives E = 0.
--    E = E0 - (RT/zF) ln Q ; with E0 = (RT/zF) ln K and Q = K:
--    instance (RT/zF) ln K = x = 85  =>  E = 85 - 85 = 0.
example : ((85 : Int) - 85) = 0 := by decide
--    Q < K  =>  ln Q < ln K  =>  E > 0 (galvanic drives forward).  Instance ln Q term = 40:
example : ((85 : Int) - 40) > 0 := by decide

-- 7. nernst_298k_form:  the RT ln10 / F prefactor is 0.05916 V; per decade of Q
--    the shift is (5916 / z)  in units of 0.01 mV.
example : ((5916 : Int) / 1) = 5916 := by decide     -- z = 1: 59.16 mV / decade
example : ((5916 : Int) / 2) = 2958 := by decide     -- z = 2: 29.58 mV / decade

-- 8. butler_volmer_equation / tafel_equation.
--    at eta = 0 both exponentials equal 1, so j = j0 (1 - 1) = 0:
example : ((1 : Int) - 1) = 0 := by decide
--    Tafel slope b = 2.303 R T / (alpha z F).  alpha = 0.5, z = 1, RT/F = 2569
--    (0.01 mV):  b = 2303 * 2569 / (5 * 1000) = 1183  => ~118.3 mV / decade.
example : ((2303 * 2569 : Int) / (5 * 1000)) = 1183 := by decide

-- 9. cell_voltage_electrolysis:  V_cell = E0_cell + |eta_a| + |eta_c| + I R.
--    alkaline water electrolysis at ~0.3 A/cm2 (centivolts):
--    123 (reversible) + 10 (cathode) + 30 (anode incl. O2 overpotential) + 35 (IR)
example : ((123 : Int) + 10 + 30 + 35) = 198 := by decide     -- => ~1.98 V
--    thermoneutral voltage 1.48 V; efficiency ~ 148 / 198:
example : ((148 * 100 : Int) / 198) = 74 := by decide          -- ~74 %

-- 10. flow_battery_energy_capacity:  Q = c V_tank z F.
--     1.6 M vanadium (1600 mol/m^3), 1 m^3, z = 1:
example : ((1600 : Int) * 96485) = 154376000 := by decide      -- C per m^3
--     as amp-hours: 154376000 / 3600 ~ 42882 A h  (~42.9 kA h)
example : ((154376000 : Int) / 3600) = 42882 := by decide

-- 11. energy_efficiency:  eta_E = eta_C * eta_V.
--     eta_C = 0.97 , eta_V = 0.85  (percent):
example : ((97 * 85 : Int)) = 8245 := by decide                -- => eta_E = 82.45 %
--     the round trip cannot beat either factor:
example : ((8245 : Int) < 9700) := by decide

-- 12. copper_electrorefining: both electrodes are Cu2+/Cu, so E0_cell = 0.
example : ((34 : Int) - 34) = 0 := by decide

-- 13. specific_energy_consumption charge factor: z F per mole of a z = 3 metal (Al).
example : ((3 : Int) * 96485) = 289455 := by decide            -- C per mol Al
--     ~37037 mol Al per tonne (M ~ 27 g/mol):
example : ((1000000 : Int) / 27) = 37037 := by decide

-- 14. thermodynamic_vs_kinetic_product (chlor-alkali anode).  Centivolts.
--     Thermodynamics favours O2:  E0(O2/H2O) = 123  <  E0(Cl2/Cl-) = 136.
example : ((123 : Int) < 136) := by decide
--     But the anode runs whichever needs the LOWER applied potential, E0 + eta:
--     Cl2:  136 + 3  = 139   vs   O2:  123 + 50 = 173.   Cl2 wins.
example : ((136 : Int) + 3) < (123 + 50) := by decide

-- 15. chlor_alkali_process: 2 NaCl + 2 H2O -> Cl2 + H2 + 2 NaOH, z = 2.
--     Cl2 (2 e-) and H2 (2 e-) are produced in a 1 : 1 mole ratio, NaOH 2 : 1.
example : ((2 : Int) * 1) = (1 * 2) := by decide
--     charge to make 1 tonne of Cl2 (M ~ 71 g/mol, z = 2):
--     ~14084 mol/tonne * 2 * 96485 C ~ 2.72e9 C.
example : ((1000000 : Int) / 71) = 14084 := by decide

-- 16. iron_flow_battery.  Centivolts.
--     E0_cell = E0(Fe3+/Fe2+) - E0(Fe2+/Fe0) = 77 - (-44) = 121  (~1.21 V).
example : ((77 : Int) - (-44)) = 121 := by decide
--     the negative plates iron BELOW the H2 line thermodynamically (E0 < 0),
--     so H2 evolution competes on charge and drives the rebalancing need:
example : ((-44 : Int) < 0) := by decide
--     sizing: 20 kWh of usable storage at ~15 Wh/L needs ~1333 L per tank.
example : ((20000 : Int) / 15) = 1333 := by decide
