/-
Release 0.1 — machine-checked algebraic cores of the proofs.
Run:  lean validation/proof-checks.lean   (exit 0, no `sorry`, no errors)

SCOPE OF WHAT LEAN CHECKS HERE.  This environment has NO Mathlib, so there is
no `ring` / `nlinarith` / real-analysis library and none of the analytic
theorems (Bolzano–Weierstrass, the MVT, the FTC, …) can be stated over ℝ, let
alone proved, in this file.  What is checked:

  * `omega`  — LINEAR arithmetic over ℤ, UNIVERSALLY.  Covers the triangle /
    reverse-triangle inequalities and the "3-ε" squeeze pattern that recur in
    almost every ε-proof in the capsule.  These are genuine universal proofs of
    the arithmetic lemmas — not instance checks.
  * induction — the two genuinely recursive identities: the telescoping sum
    (behind FTC II and interval additivity) and the geometric ratio bound
    (behind the ratio/root tests).  Genuine universal proofs over ℕ / ℤ.
  * `decide` — INSTANCE checks at sample integer values for the NONLINEAR
    polynomial identities (`ring` would close these universally with Mathlib).
    An instance check is fully kernel-verified but is NOT a universal proof;
    each is labelled INSTANCE below.

Lean verifies NONE of: the ε-δ / ε-N logic, the limit constructions, the use of
`lub_axiom`, compactness, or any statement quantifying over real functions.
Those rest on the cited sources (see validation/proof-checks.md).
-/

/-! ## 1. Triangle inequality — behind `algebra_of_limits`, `cauchy_sequence`,
    `abs_convergence_implies_convergence`, `uniform_cauchy_criterion`.
    Universal over ℤ. -/
theorem tri (a b : Int) : (a + b).natAbs ≤ a.natAbs + b.natAbs := by omega

/-! ## 2. Reverse triangle inequality — behind `differentiable_implies_continuous`
    (bounding `|f(x) - f(c)|`) and `limit_uniqueness`.  Universal over ℤ. -/
theorem rev_tri (a b : Int) : a.natAbs - b.natAbs ≤ (a - b).natAbs := by omega

/-! ## 3. The squeeze / 3-ε pattern — behind `squeeze_theorem`, and the
    `uniform_limit_continuous` 3-ε argument.  If `a ≤ x ≤ b` and both `a` and
    `b` are within `eps` of `L`, so is `x`.  Universal over ℤ. -/
theorem squeeze_core (a x b L eps : Int)
    (hax : a ≤ x) (hxb : x ≤ b)
    (ha : (a - L).natAbs ≤ eps) (hb : (b - L).natAbs ≤ eps) :
    (x - L).natAbs ≤ eps := by omega

/-! ## 4. Telescoping sum — behind `ftc_part2` (∑ (G(tᵢ) − G(tᵢ₋₁)) = G(b) − G(a))
    and `interval_additivity`.  Genuine induction, universal over ℤ. -/
def sdiff (g : Nat → Int) : Nat → Int
  | 0 => 0
  | n + 1 => sdiff g n + (g (n + 1) - g n)

theorem telescope (g : Nat → Int) : ∀ n, sdiff g n = g n - g 0 := by
  intro n
  induction n with
  | zero => simp [sdiff]
  | succ k ih => simp only [sdiff, ih]; omega

/-! ## 5. Geometric ratio bound — behind `ratio_test`, `root_test`,
    `comparison_test` (constructing the geometric majorant).  If every term is
    ≤ `c` times the previous, the nth term is ≤ `cⁿ` times the first.  Genuine
    induction, universal over ℕ. -/
theorem ratio_bound (c : Nat) (a : Nat → Nat) (h : ∀ n, a (n + 1) ≤ c * a n) :
    ∀ n, a n ≤ c ^ n * a 0 := by
  intro n
  induction n with
  | zero => simp
  | succ k ih =>
    calc a (k + 1) ≤ c * a k := h k
      _ ≤ c * (c ^ k * a 0) := Nat.mul_le_mul_left c ih
      _ = c ^ (k + 1) * a 0 := by simp [Nat.pow_succ, Nat.mul_comm, Nat.mul_assoc]

/-! ## 6. Geometric partial-sum identity — behind `geometric_series`.
    (1 − r)·(1 + r + … + rⁿ) = 1 − rⁿ⁺¹.  INSTANCE: r = 3, n = 4.
    (1−3)(1+3+9+27+81) = −2·121 = −242 ;  1 − 3⁵ = 1 − 243 = −242. -/
example : ((1 : Int) - 3) * (1 + 3 + 3 ^ 2 + 3 ^ 3 + 3 ^ 4) = 1 - 3 ^ 5 := by decide

/-! ## 7. Taylor, 2nd order, Lagrange remainder — behind `taylor_theorem`.
    For f(x) = x², a = 1:  f(x) − f(a) − f'(a)(x−a) = f''(ξ)(x−a)²/2, with
    f'' ≡ 2 so ξ is immaterial.  INSTANCE x = 5:
    25 − 1 − 2·1·4 = 16 ;  (2·4²)/2 = 16. -/
example : ((5 : Int) ^ 2 - 1 ^ 2 - 2 * 1 * (5 - 1)) = (2 * (5 - 1) ^ 2) / 2 := by decide

/-! ## 8. AM–GM step — behind the canonical `monotone_convergence_theorem`
    example xₙ₊₁ = (xₙ + 2/xₙ)/2 (decreasing, bounded below by √2), whose core is
    a² + b² ≥ 2ab.  INSTANCE a = 5, b = 3:  34 ≥ 30. -/
example : (2 : Int) * 5 * 3 ≤ 5 ^ 2 + 3 ^ 2 := by decide

/-! ## 9. MVT auxiliary function vanishes at the endpoints — behind
    `rolles_theorem` ⇒ `mean_value_theorem`.  h(x) = f(x) − f(a) − s·(x−a) with
    s = (f(b) − f(a))/(b − a) has h(a) = 0 and h(b) = 0, reducing the MVT to
    Rolle.  `omega` cannot divide by a variable, so this is an INSTANCE:
    f(a) = 2, f(b) = 8, a = 1, b = 4  ⇒  s = 6/3 = 2 ;  h(4) = 8 − 2 − 2·3 = 0. -/
example : (8 : Int) - 2 - ((8 - 2) / (4 - 1)) * (4 - 1) = 0 := by decide
example : (2 : Int) - 2 - ((8 - 2) / (4 - 1)) * (1 - 1) = 0 := by decide
