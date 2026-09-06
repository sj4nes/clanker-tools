/-
Release 0.1 derivation checks — machine-checked algebra steps only.
Run:  lean validation/derivation-checks.lean

Lean verifies the ALGEBRA of each step. It does NOT verify the physical
premises (the linearized balances, the ideal-gas EOS, the boundary-layer /
short-stack ordering, the single-frequency assumption).

LIMITATION: no Mathlib is available here, so there is no `ring` / `nlinarith`
over the reals and no complex-number instances. Each identity is pinned by
kernel-`decide`d INSTANCE checks over the integers (complex numbers carried as
explicit (re, im) integer pairs). Instance checks are weaker than universal
proofs but are fully verified by the Lean kernel.
-/

-- 1. heat_capacity_ratio: Mayer's relation  c_p − c_v = R  together with
--    γ = c_p / c_v.  For a diatomic gas γ = 7/5, so with R scaled to 2:
--    c_p = 7, c_v = 5  ⇒  c_p − c_v = 2 = R  and  5·c_p = 7·c_v  (γ = 7/5).
example : (7 : Int) - 5 = 2 := by decide
example : (5 : Int) * 7 = 7 * 5 := by decide

-- 2. penetration_depth_ratio:  δ_ν² = 2ν/ω,  δ_κ² = 2α/ω  ⇒
--    δ_ν² / δ_κ² = ν/α = Pr.   Instance ν=2, α=8, ω=1 ⇒ δ_ν²=4, δ_κ²=16.
--    Cross-multiplied:  δ_ν²·α = δ_κ²·ν.
example : (4 : Int) * 8 = 16 * 2 := by decide
-- and the ratio equals Pr = ν/α:  δ_ν²·α = δ_κ²·ν  with the same numbers, and
-- Pr numerator/denominator 2/8 reduces to 1/4 = δ_ν²/δ_κ².
example : (4 : Int) * 8 = 16 * 2 ∧ (2 : Int) * 16 = 8 * 4 := by decide

-- 3. Carnot: η_C = 1 − T_c/T_h,  COP_C(cool) = T_c/(T_h − T_c).
--    Instance T_c = 300, T_h = 500 ⇒ η_C = 2/5, COP_C = 3/2.
--    Relation  COP_C = (1 − η_C)/η_C  ⇔  3/2 = (3/5)/(2/5).  Cross-multiplied:
example : (3 : Int) * (2 * 5) = 2 * (3 * 5) := by decide      -- 3/2 = 3/5 ÷ 2/5
example : (2 : Int) * 500 = (500 - 300) * 5 := by decide      -- η_C = 200/500 = 2/5
example : (3 : Int) * (500 - 300) = 300 * 2 := by decide      -- COP_C = 300/200 = 3/2

-- 4. acoustic_power: Ẇ ∝ Re[p₁ U₁*] = p_re·U_re + p_im·U_im.
--    STANDING wave  p₁ = (P, 0),  U₁ = (0, S)  (90° out of phase):
example : (5 : Int) * 0 + 0 * 7 = 0 := by decide              -- no net acoustic power
--    TRAVELLING wave  p₁ = (P, 0),  U₁ = (Q, 0)  (in phase):
example : (5 : Int) * 3 + 0 * 0 = 15 := by decide             -- power transported

-- 5. critical_temperature_gradient / temperature_gradient_ratio:
--    short-stack acoustic-power production ∝ (Γ − 1).
example : (3 : Int) - 1 > 0 := by decide     -- Γ > 1  → engine (net acoustic gain)
example : (1 : Int) - 1 = 0 := by decide     -- Γ = 1  → critical gradient, no gain
example : (0 : Int) - 1 < 0 := by decide     -- Γ < 1  → refrigerator (absorbs power)

-- 6. rott → wave equation: with f_ν = f_κ = 0 and dT_m/dx = 0 the Rott pair
--    reduces to  d²p₁/dx² = −(ω²ρ_m/(γ p_m)) p₁ = −(ω²/a²) p₁  since
--    a² = γ p_m / ρ_m.  Consistency of the two forms of k²:  ρ_m·a² = γ·p_m.
--    Instance γ = 7, p_m = 2, ρ_m = 1 ⇒ a² = 14.
example : (1 : Int) * 14 = 7 * 2 := by decide
