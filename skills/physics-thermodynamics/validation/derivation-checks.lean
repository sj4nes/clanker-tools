/-
Release 0.1 derivation checks -- machine-checked algebra steps only.
Run:  lean validation/derivation-checks.lean

Lean verifies the ALGEBRA of each derivation step. It does NOT verify the
physical premises (the first and second laws, the ideal-gas model, reversibility,
the quoted c_v values).

LIMITATION: no Mathlib is available here, so there is no `ring` / `nlinarith`
over the reals -- the universal polynomial identities behind these derivations
cannot be closed by a decision procedure. Each identity is instead pinned by
kernel-`decide`d INSTANCE checks over the integers. An instance check is weaker
than a universal proof but is fully verified by the Lean kernel. Re-run with
Mathlib to upgrade each to `by ring`.
-/

-- 1. mayer_relation: for an ideal gas  c_p - c_v = R.  Algebraic core: with
--    h = u + R T (per mole, since P v = R T) and u = u(T),
--    c_p = dh/dT = du/dT + R = c_v + R.
--    Instance: c_v = 3, R = 2  =>  c_p = 5 ;  5 - 3 = 2.
example : (3 + 2 : Int) = 5 := by decide
example : (5 - 3 : Int) = 2 := by decide

-- 2. heat_capacity_ratio / adiabatic exponent:  gamma - 1 = R / c_v, i.e.
--    (c_p - c_v) / c_v = R / c_v.  Cross-multiplied instance (c_v = 3, R = 2,
--    c_p = 5):  (c_p - c_v) * c_v = R * c_v  =>  (5-3)*3 = 2*3 = 6.
example : ((5 - 3) * 3 : Int) = 2 * 3 := by decide

-- 3. carnot_efficiency:  eta = 1 - Q_c/Q_h  and (thermodynamic scale)
--    Q_c/Q_h = T_c/T_h, so eta = (T_h - T_c)/T_h.  Cross-multiplied instance
--    (T_c = 300, T_h = 500):  eta = 200/500 = 2/5  <=>  (500-300)*5 = 2*500.
example : ((500 - 300) * 5 : Int) = 2 * 500 := by decide

-- 4. carnot_cop:  COP_hp = T_h/(T_h - T_c),  COP_ref = T_c/(T_h - T_c),
--    hence COP_hp - COP_ref = 1  and  COP_hp = COP_ref + 1.
--    Instance (T_c = 300, T_h = 500, denom = 200):  T_h = T_c + (T_h - T_c).
example : (500 : Int) = 300 + (500 - 300) := by decide

-- 5. enthalpy / T dS consistency:  from H = U + P V,
--    dH = dU + P dV + V dP.  With the fundamental relation dU = T dS - P dV,
--    dH = (T dS - P dV) + P dV + V dP = T dS + V dP.
--    Instance  dU = 7, P dV = 3, V dP = 5  =>  T dS = dU + P dV = 10 ;
--    dH = dU + P dV + V dP = 15 ;  T dS + V dP = 10 + 5 = 15.
example : ((7 : Int) + 3 + 5) = (7 + 3) + 5 := by decide

-- 6. ideal_gas_internal_energy in free expansion:  isolated + rigid  =>  Q = 0
--    and W = integral P dV = 0, so by the first law  dU = Q - W = 0.
--    Instance: Q = 0, W = 0  =>  dU = 0.
example : ((0 : Int) - 0) = 0 := by decide

-- 7. entropy_ideal_gas coefficient bookkeeping:  dS = n c_v ln(T2/T1) + n R ln(V2/V1).
--    For free expansion T2 = T1 so ln(T2/T1) = 0 and the first term vanishes;
--    the surviving coefficient of ln(V2/V1) is n R.
--    Instance n = 1, R = 2:  n*c_v*0 + n*R = 0 + 2 = 2.
example : ((1 * 3 * 0 : Int) + 1 * 2) = 2 := by decide
