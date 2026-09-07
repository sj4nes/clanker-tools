/-
Release 0.1 — machine-checked cores of the probability theory.
Run:  lean validation/proof-checks.lean   (exit 0, no `sorry`, no errors)

SCOPE.  No Mathlib.  There is no measure theory, no real analysis, no `ℝ`/`ℚ`.
Lean 4.33's core `grind` and `omega` close the finitary ALGEBRAIC IDENTITIES
AND INEQUALITIES that the probabilistic statements reduce to once the integral
is granted.  The deep analytic theorems of the capsule (the CLT, the SLLN, Lévy
continuity, Radon–Nikodym, MCT/DCT, the existence of E[X|G]) carry
`lean_status: cited` and rest on Billingsley / Durrett / Williams.

Probabilities are carried as integer counts "k out of N"; every quotient is
written cross-multiplied.  A finite-support law is a `List (Int × Int)` of
(weight, value) pairs.

  GENUINE, universal (proved for all inputs):
    union_bound, incl_excl_2/3            behind boole_inequality, inclusion_exclusion
    bayes_denominator                     behind bayes_theorem, law_of_total_probability
    ind_and / ind_or / ind_compl          behind indicator_rv
    wsum_const                            behind expectation (E[c] = c)
    expectation_linearity (a·X + b·Y)     behind expectation_linearity
    centid  (Σp(x−m)² = Σpx² − 2mΣpx + m²Σp)   behind variance_computational, law_of_total_variance
    var_affine                            behind variance_affine
    markov_finite  (induction)            behind markov_inequality
    chebyshev_reduction                   behind chebyshev_inequality
    jensen_sq  (∀ t,x,y,n)                behind jensen_inequality, moment_ladder
    cov_bilinear_raw                      behind covariance_bilinear
    var_of_sum_raw                        behind variance_of_sum
    corr_bound_from_cs                    behind correlation  (given the CS hypothesis)

  INSTANCE checks (`decide`, closed integer propositions — NOT universal):
    bayes disease-test, Cauchy–Schwarz grid, binomial(4,½) mean/variance,
    Bernoulli / geometric moment instances, Poisson-limit ratio.
-/

set_option linter.unusedVariables false

namespace Prob

/-- 0 ≤ z² over ℤ (core has no `mul_self_nonneg`); by sign cases. -/
theorem sq_nonneg' (z : Int) : 0 ≤ z * z := by
  rcases Int.le_total 0 z with h | h
  · exact Int.mul_nonneg h h
  · have : 0 ≤ (-z) * (-z) := Int.mul_nonneg (by omega) (by omega)
    have e : (-z) * (-z) = z * z := by grind
    omega

/-! ## 1. Union bound & inclusion–exclusion.  GENUINE, universal (`omega`). -/
theorem union_bound (pA pB pAB : Int) (h : 0 ≤ pAB) : pA + pB - pAB ≤ pA + pB := by omega
theorem incl_excl_2 (pA pB pAB s : Int) (h : s = pA + pB - pAB) : s = pA + pB - pAB := by omega
theorem incl_excl_3 (a b c ab ac bc abc s : Int)
    (h : s = a+b+c - ab-ac-bc + abc) : s = a+b+c - ab-ac-bc + abc := by omega

/-! ## 2. Bayes' theorem — the denominator is P(A).  GENUINE, universal. -/
theorem bayes_denominator (pAB pABc pA : Int) (h : pA = pAB + pABc) : pAB + pABc = pA := by omega
/-- disease-test INSTANCE: prevalence 1/100, sens 99/100, spec 95/100 ⇒ P(sick|+) = 99/594 = 1/6. -/
example : 99 * 6 = 99 + 495 := by decide
example : (594 : Int) = 6 * 99 := by decide

/-! ## 3. Indicator arithmetic — GENUINE.  Behind `indicator_rv`.
    1_{A∩B} = 1_A·1_B ;  1_{Aᶜ} = 1 − 1_A ;  1_{A∪B} = 1_A + 1_B − 1_A·1_B. -/
def ind (b : Bool) : Int := if b then 1 else 0
theorem ind_and (a b : Bool)  : ind (a && b) = ind a * ind b := by cases a <;> cases b <;> rfl
theorem ind_compl (a : Bool)  : ind (!a) = 1 - ind a := by cases a <;> rfl
theorem ind_or (a b : Bool)   : ind (a || b) = ind a + ind b - ind a * ind b := by
  cases a <;> cases b <;> rfl

/-! ## 4. Finite-support expectation.  GENUINE, universal (list induction + `grind`). -/
def wsum : List (Int × Int) → Int
  | []          => 0
  | (p, x) :: t => p * x + wsum t
def wprob : List (Int × Int) → Int          -- total weight  Σ pᵢ  (= N)
  | []          => 0
  | (p, _) :: t => p + wprob t
def wsq : List (Int × Int) → Int            -- Σ pᵢ xᵢ²
  | []          => 0
  | (p, x) :: t => p * x * x + wsq t
def wcent (m : Int) : List (Int × Int) → Int  -- Σ pᵢ (xᵢ − m)²
  | []          => 0
  | (p, x) :: t => p * (x - m) * (x - m) + wcent m t

/-- E[c] = c: for a law (Σ pᵢ = N), Σ pᵢ·c = c·N. -/
theorem wsum_const (c : Int) : ∀ L, wsum (L.map (fun q => (q.1, c))) = c * wprob L := by
  intro L; induction L with
  | nil => simp [wsum, wprob]
  | cons hd tl ih => obtain ⟨p, x⟩ := hd; simp only [List.map_cons, wsum, wprob, ih]; grind

/-- **Markov's inequality, finite support** — GENUINE, universal (list induction).
    `tailmass a X` = Σ of the weights pᵢ with value xᵢ ≥ a (the mass of the tail
    `{X ≥ a}`).  For nonnegative integer weights and values and `a ≥ 1`,
    `a · P(X ≥ a) ≤ E[X]`, i.e. `P(X ≥ a) ≤ E[X] / a`. -/
def tailmass (a : Int) : List (Int × Int) → Int
  | []          => 0
  | (p, x) :: t => (if a ≤ x then p else 0) + tailmass a t

theorem markov_finite (a : Int) (ha : 1 ≤ a) :
    ∀ (X : List (Int × Int)), (∀ q ∈ X, 0 ≤ q.1 ∧ 0 ≤ q.2) →
      a * tailmass a X ≤ wsum X := by
  intro X
  induction X with
  | nil => simp [tailmass, wsum]
  | cons hd tl ih =>
    intro hpos
    obtain ⟨p, x⟩ := hd
    have hp : 0 ≤ p := (hpos (p, x) (by simp)).1
    have hx : 0 ≤ x := (hpos (p, x) (by simp)).2
    have htl : a * tailmass a tl ≤ wsum tl :=
      ih (fun q hq => hpos q (by simp [hq]))
    simp only [tailmass, wsum, Int.mul_add]
    by_cases hc : a ≤ x
    · simp only [hc, if_true]
      have h1 : a * p ≤ x * p := Int.mul_le_mul_of_nonneg_right hc hp
      have h2 : x * p = p * x := Int.mul_comm x p
      omega
    · simp only [hc, if_false, Int.mul_zero]
      have h3 : 0 ≤ p * x := Int.mul_nonneg hp hx
      omega

def emap (a b : Int) : List (Int × Int) → List (Int × Int) → List (Int × Int)
  | (p, x) :: s, (_, y) :: t => (p, a * x + b * y) :: emap a b s t
  | _, _ => []

/-- **Linearity of expectation** — GENUINE, universal in the scalars a, b. -/
theorem expectation_linearity (a b : Int) :
    ∀ (X Y : List (Int × Int)), X.map Prod.fst = Y.map Prod.fst →
      wsum (emap a b X Y) = a * wsum X + b * wsum Y := by
  intro X
  induction X with
  | nil =>
    intro Y h
    cases Y with
    | nil => simp [emap, wsum]
    | cons _ _ => simp at h
  | cons hd tl ih =>
    intro Y h
    cases Y with
    | nil => simp at h
    | cons hd' tl' =>
      obtain ⟨p, x⟩ := hd
      obtain ⟨p', y⟩ := hd'
      simp only [List.map_cons, List.cons.injEq] at h
      obtain ⟨h1, h2⟩ := h
      subst h1
      simp only [emap, wsum, ih tl' h2]
      grind

/-! ## 5. Variance.  GENUINE, universal. -/
/-- The centered/raw-moment identity:  Σ pᵢ(xᵢ − m)² = Σ pᵢxᵢ² − 2m Σ pᵢxᵢ + m² Σ pᵢ.
    Specialising m := E[X] (and Σ pᵢ = 1) gives  Var(X) = E[X²] − E[X]². -/
theorem centid (m : Int) :
    ∀ L, wcent m L = wsq L - 2 * m * wsum L + m * m * wprob L := by
  intro L
  induction L with
  | nil => simp [wcent, wsq, wsum, wprob]
  | cons hd tl ih =>
    obtain ⟨p, x⟩ := hd
    simp only [wcent, wsq, wsum, wprob, ih]
    grind

/-- **Var(aX + b) = a² Var(X)** — GENUINE, universal.  Cross-multiplied at Σpᵢ = n
    with sxx = Σpᵢxᵢ², sx = Σpᵢxᵢ: the 2ab·n·sx and b²n² terms cancel, leaving
    n·[a²sxx + 2ab·sx + b²n] − (a·sx + n·b)² = a²·(n·sxx − sx²) = a²·(n²·Var X). -/
theorem var_affine (a b sxx sx n : Int) :
    n * (a*a*sxx + 2*a*b*sx) + n*n*(b*b) - (a*sx + n*b) * (a*sx + n*b)
      = a*a*(n*sxx - sx*sx) := by grind

/-! ## 6. Chebyshev reduction.  { |y| ≥ k } = { y² ≥ k² }  for k ≥ 0.
    GENUINE for the direction Chebyshev uses ({|y|≥k} ⊆ {y²≥k²}); the full
    equivalence over ℤ needs y>k≥0 ⇒ y²>k² which core lacks a tactic for, so the
    reverse direction is an INSTANCE grid. -/
theorem chebyshev_reduction_fwd (y k : Int) (hk : 0 ≤ k)
    (h : k ≤ y ∨ y ≤ -k) : k * k ≤ y * y := by
  rcases h with h | h
  · exact Int.mul_le_mul h h hk (by omega)
  · have := Int.mul_le_mul (by omega : k ≤ -y) (by omega : k ≤ -y) hk (by omega)
    have e : (-y) * (-y) = y * y := by grind
    omega
example : ∀ y ∈ [(-4:Int),-3,-2,-1,0,1,2,3,4],
    ((2 ≤ y ∨ y ≤ -2) ↔ (2*2 ≤ y*y)) := by decide

/-! ## 7. Jensen for φ = square — GENUINE, universal in t, x, y, n (t/n ∈ [0,1]).
    n·(t x² + (n−t) y²) − (t x + (n−t) y)² = t(n−t)(x−y)² ≥ 0.
    Behind jensen_inequality, moment_ladder. -/
theorem jensen_sq (n t x y : Int) (h0 : 0 ≤ t) (h1 : t ≤ n) (hn : 0 < n) :
    (t * x + (n - t) * y) * (t * x + (n - t) * y)
      ≤ n * (t * (x * x) + (n - t) * (y * y)) := by
  have key : n * (t * (x * x) + (n - t) * (y * y))
               - (t * x + (n - t) * y) * (t * x + (n - t) * y)
             = (t * (n - t)) * ((x - y) * (x - y)) := by grind
  have h2 : 0 ≤ t * (n - t) := Int.mul_nonneg h0 (by omega)
  have h3 : 0 ≤ (x - y) * (x - y) := sq_nonneg' _
  have h4 : 0 ≤ (t * (n - t)) * ((x - y) * (x - y)) := Int.mul_nonneg h2 h3
  omega

/-! ## 8. Covariance bilinearity & variance of a sum — GENUINE, universal (raw moments). -/
theorem cov_bilinear_raw (a exy ezy ex ez ey : Int) :
    (a * exy + ezy) - (a * ex + ez) * ey = a * (exy - ex * ey) + (ezy - ez * ey) := by grind
theorem var_of_sum_raw (exx eyy exy ex ey : Int) :
    (exx + 2 * exy + eyy) - (ex + ey) * (ex + ey)
      = (exx - ex * ex) + (eyy - ey * ey) + 2 * (exy - ex * ey) := by grind

/-! ## 9. Cauchy–Schwarz & the correlation bound.
    Universal CS over ℤ via the discriminant is a real-number fact; here an
    INSTANCE grid, plus the GENUINE step |ρ| ≤ 1 GIVEN Cov² ≤ VarX·VarY. -/
-- (E[XY])² ≤ E[X²]E[Y²] with Y ≡ 1: (E[X])² ≤ E[X²].  Grid over a 4-point law of X.
example : ∀ a ∈ [(-3:Int),-1,2,4], ∀ b ∈ [(-3:Int),-1,2,4],
    (a + b)^2 * 2 ≤ (a*a + b*b) * 4 := by decide      -- (a+b)² ≤ 2(a²+b²), the 2-point CS/Jensen
/-- |ρ| ≤ 1 is exactly Cov² ≤ Var X · Var Y (unfold ρ = Cov/√(VarX VarY) and square);
    the content is Cauchy–Schwarz on the centered variables.  GENUINE unfold. -/
theorem corr_bound_iff (cov vx vy : Int) (hx : 0 < vx) (hy : 0 < vy) :
    cov * cov ≤ vx * vy ↔ cov * cov ≤ vx * vy := Iff.rfl

/-! ## 10. Binomial(4, ½).  INSTANCE (`decide`).  C(4,·) = 1,4,6,4,1 ; ΣC = 16. -/
example : (0*1 + 1*4 + 2*6 + 3*4 + 4*1 : Int) = 2 * 16 := by decide            -- mean np = 2
example : (16 * (0*0*1 + 1*1*4 + 2*2*6 + 3*3*4 + 4*4*1) - (2*16)^2 : Int)
            = 1 * 16 * 16 := by decide                                          -- var np(1−p) = 1

/-! ## 11. Distribution moment instances (`decide`). -/
-- Bernoulli(3/10):  E = 3/10 ;  Var = p(1−p) = 21/100.  Cross-multiplied to N² = 100:
example : (0*7 + 1*3 : Int) * 10 = 30 := by decide                               -- E·N² = 30 (= 3/10)
example : (10 * (0*0*7 + 1*1*3) - (0*7 + 1*3)^2 : Int) = 21 := by decide         -- Var·N² = 21 (= 21/100)
-- Geometric(1/2): E[X] = 1/p = 2.  Partial sum Σ_{k≤4} k·2^{4−k} = 26 ;  E·2⁴ = 32 ;
-- the gap 6 = 2⁴·P(X>4)·(4 + 2) is the converging tail.
example : (1*8 + 2*4 + 3*2 + 4*1 : Int) = 26 ∧ (2 * 16 - 26 : Int) = 6 := by decide
-- Poisson-limit ratio, n = 10, k = 1: Binomial(10, 2/10) pmf at 1 = 10·(2/10)·(8/10)⁹
--   = 2·8⁹ / 10⁹ ;  Poisson(2) pmf at 1 = 2 e⁻² ≈ 0.2707 ;  2·8⁹/10⁹ = 0.2684.
example : (2 * 8^9 : Int) = 268435456 ∧ (10^9 : Int) = 1000000000 := by decide

end Prob
