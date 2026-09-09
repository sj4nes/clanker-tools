/-
Release 0.1 derivation checks -- machine-checked algebra steps only.
Run:  lean validation/derivation-checks.lean   (exit 0, no output = all pass)

Lean verifies the ALGEBRA of each bookkeeping identity. It does NOT verify the
chemistry: that H is a state function (Hess's law), that the ideal-gas model
holds (K_p/K_c), that dG = dH - T dS (imported from physics-thermodynamics), or
any tabulated enthalpy / K value.

LIMITATION: no Mathlib here, so no `ring` / `nlinarith` over the reals. Each
identity is pinned by kernel-`decide`d INSTANCE checks over the integers
(enthalpies in kJ/mol, p-values as integer log units). An instance check is
weaker than a universal proof but is fully verified by the Lean kernel.
Re-run with Mathlib to upgrade each `by decide` to `by ring`.
-/

-- 1. hess_law:  dH(A -> C)  =  dH(A -> B) + dH(B -> C)   (path independence).
--    Instance: dH1 = -30, dH2 = -70  =>  dH_total = -100.
example : ((-30 : Int) + (-70)) = -100 := by decide
--    reversing a step flips its sign:  dH(B -> A) = -dH(A -> B).
example : (-(-30 : Int)) = 30 := by decide

-- 2. enthalpy_from_formation_enthalpies:
--    dHrxn = [sum n*dHf(products)] - [sum n*dHf(reactants)].
--    CH4(g) + 2 O2(g) -> CO2(g) + 2 H2O(l), kJ/mol:
--    dHf: CH4 -75, O2 0, CO2 -393, H2O(l) -286.
--    dHrxn = (-393 + 2*(-286)) - (-75 + 2*0) = -965 + 75 = -890.
example : (((-393 : Int) + 2*(-286)) - ((-75) + 2*0)) = -890 := by decide
--    scaling the equation by k scales dHrxn by k (k = 2):
example : (2 * (-890 : Int)) = -1780 := by decide

-- 3. kp_kc_relation:  K_p = K_c * (R T / P0)^{dn},  dn = n_gas(prod) - n_gas(react).
--    Exponent bookkeeping instance: N2 + 3 H2 -> 2 NH3  =>  dn = 2 - (1 + 3) = -2.
example : ((2 : Int) - (1 + 3)) = -2 := by decide
--    dn = 0  =>  factor is 1  =>  K_p = K_c  (instance K_c = 7):
example : (7 * (1:Int)^(0:Nat)) = 7 := by decide
--    cross-multiplied instance, dn = 1, RT/P0 = 3, K_c = 5  =>  K_p = 15:
example : ((5 : Int) * 3^(1:Nat)) = 15 := by decide

-- 4. reaction_isotherm / spontaneity:  dG = dG0 + R T ln Q  and  dG0 = -R T ln K.
--    At equilibrium Q = K  =>  dG = -R T ln K + R T ln K = 0.
--    Instance with (R T ln K) = x = 12:
example : ((-12 : Int) + 12) = 0 := by decide
--    Q < K  =>  ln(Q/K) < 0  =>  dG < 0 (forward). Instance: R T = 4,
--    ln(Q/K) = -2  =>  dG = -8 < 0.
example : ((4 : Int) * (-2)) = -8 := by decide

-- 5. ka_kb_relation:  K_a * K_b = K_w   <=>   pK_a + pK_b = pK_w.
--    Multiplicative instance: K_a = 2, K_b = 3  =>  K_w = 6.
example : ((2 : Int) * 3) = 6 := by decide
--    Log-form instance (25 C): pK_a = 5, pK_b = 9  =>  pK_w = 14.
example : ((5 : Int) + 9) = 14 := by decide

-- 6. henderson_hasselbalch:  from  K_a = [H+] * ([A-]/[HA]),  take -log10:
--    pK_a = pH - log10([A-]/[HA]),  hence  pH = pK_a + log10([A-]/[HA]).
--    Instance: pK_a = 4, log10([A-]/[HA]) = 1  =>  pH = 5, and  pH - 1 = pK_a.
example : ((4 : Int) + 1) = 5 := by decide
example : ((5 : Int) - 1) = 4 := by decide
--    buffer centre: [A-] = [HA]  =>  log10(1) = 0  =>  pH = pK_a.
example : ((4 : Int) + 0) = 4 := by decide

-- 7. poh_relation:  pH + pOH = pK_w   (from -log10 of K_w = [H+][OH-]).
--    Instance (25 C): pH = 3  =>  pOH = 11,  3 + 11 = 14.
example : ((3 : Int) + 11) = 14 := by decide

-- 8. balancing_redox_half_reactions: electrons lost = electrons gained.
--    MnO4^- + 5 Fe^2+ + 8 H+ -> Mn^2+ + 5 Fe^3+ + 4 H2O:
--    reduction gains 5 e-; oxidation is 5 x (1 e- lost).  5*1 = 1*5.
example : ((5 : Int) * 1) = 1 * 5 := by decide
--    charge balance, left vs right:  (-1) + 5*(2) + 8*(1)  =  5*(3) + 2  =  17.
example : (((-1 : Int) + 5*2 + 8*1)) = (5*3 + 2) := by decide

-- 9. formal_charge: sum of formal charges = species charge.  CO instance:
--    C: 4 - 2 - 6/2 = -1 ;  O: 6 - 2 - 6/2 = +1 ;  sum = 0 (neutral CO).
example : ((4 - 2 - 6/2 : Int) + (6 - 2 - 6/2)) = 0 := by decide

-- 10. relative_atomic_mass is a convex combination: sum of abundances = 1, so
--     A_r lies between the min and max isotope mass.  Cl instance (x1000):
--     f(35) = 758, f(37) = 242, 758 + 242 = 1000.
example : ((758 : Int) + 242) = 1000 := by decide

-- 11. molecular_formula: k = M_molecular / M_empirical is a positive integer.
--     glucose instance: M_emp(CH2O) = 30, M_mol = 180  =>  k = 6, 6*30 = 180.
example : ((180 : Int) / 30) = 6 := by decide
example : ((6 : Int) * 30) = 180 := by decide

-- 12. limiting_reagent: compare n_i / nu_i; the reactant with the smallest
--     ratio limits.  N2 (1 mol, nu 1) + H2 (1 mol, nu 3):  1/1 vs 1/3.
--     Cross-multiplied: 1*3 vs 1*1  =>  3 > 1  =>  H2 ratio (1/3) is smaller.
example : (1 * 3 : Int) > (1 * 1) := by decide
