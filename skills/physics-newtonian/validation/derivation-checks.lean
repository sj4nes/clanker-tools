/-
Release 0.1 derivation checks — machine-checked algebra steps only.
Run:  lean validation/derivation-checks.lean

Lean verifies the ALGEBRA of each derivation step. It does NOT verify the
physical premises (Newton's second law, constant acceleration, the Hooke
model, the small-angle / nonrelativistic regime).

LIMITATION: no Mathlib is available in this environment, so there is no
`ring` / `nlinarith` over the reals — the universal polynomial identities
behind these derivations cannot be closed by a decision procedure here.
Instead each identity is pinned by kernel-`decide`d INSTANCE checks over the
integers. An instance check is weaker than a universal proof but is fully
verified by the Lean kernel. Re-run with Mathlib to upgrade to `by ring`.
-/

-- 1. constant_acceleration_kinematics: eliminating t between  v = v0 + a t  and
--    Δx = v0 t + ½ a t²  gives  v² = v0² + 2 a Δx.
--    Instance: v0 = 3, a = 2, t = 5  ⇒  v = 13, Δx = 15 + 25 = 40.
--    13² = 169 ;  3² + 2·2·40 = 9 + 160 = 169.
example : ((3 : Int) + 2 * 5) ^ 2 = 3 ^ 2 + 2 * 2 * (3 * 5 + 2 * 5 ^ 2 / 2) := by decide

-- 2. work_energy_theorem (constant a over displacement dx): W = F·dx = (m a) dx,
--    ΔK = ½ m (v² − v0²) = ½ m (2 a dx) = (m a) dx  ⇒  W = ΔK identically.
--    Instance (×2 to clear the ½): m = 4, a = 6, dx = 10, v0 = 3.
--    2·W = 2·(4·6·10) = 480 ;  m·((v0²+2a·dx) − v0²) = 4·(2·6·10) = 480.
example : (2 : Int) * ((4 * 6) * 10) = 4 * ((3 ^ 2 + 2 * 6 * 10) - 3 ^ 2) := by decide

-- 3. elastic_pe: work done BY the Hookean force F = −k s from 0 to x is
--    ∫₀ˣ (−k s) ds = −½ k x², so stored U = ½ k x².  Instance: k = 5, x = 7.
--    (2 k x²)/2 = k x² = 245  (write ½ as an exact integer division).
example : ((2 * 5 * 7 ^ 2 : Int)) / 2 = 5 * 7 ^ 2 := by decide

-- 4. angular_frequency_shm: x(t) = A cos(ω t) solves  m x'' = −k x  iff
--    m(−A ω² c) = −k (A c)  for c = cos(ω t)  ⇔  m ω² = k.
--    Instance: m = 3, ω² = 4, k = 12, (A c) = 9  ⇒  3·(−9·4) = −(12·9) = −108.
example : (3 : Int) * (-(9 * 4)) = -(12 * 9) := by decide

-- 5. simple_pendulum: with the small-angle torque τ ≈ −(m g L) θ and I = m L²,
--    θ'' = −(g/L) θ, i.e. ω² = g/L, so  T = 2π√(L/g).  Algebraic core:
--    (m g L) / (m L²) = g / L.  Instance: m = 2, g = 10, L = 5.
--    (2·10·5) / (2·25) = 100 / 50 = 2 ;  g/L = 10/5 = 2.
example : ((2 * 10 * 5 : Int)) / (2 * 5 ^ 2) = 10 / 5 := by decide
