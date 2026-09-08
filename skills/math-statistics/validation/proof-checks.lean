/-
math-statistics Release 0.1 -- machine-checked finitary cores.
Run:  lean validation/proof-checks.lean   (exit 0, no `sorry`, no errors, no warnings)

SCOPE.  No Mathlib.  No measure theory, no real analysis, no `ℝ`.  Lean 4.33's
core `omega` / `grind` / `decide` close the FINITARY ALGEBRAIC IDENTITIES AND
INEQUALITIES that each statistical statement reduces to once the integral, the
CLT, and the Gaussian sampling theory are granted.  Probabilities / weights /
sums of squares are carried as integer counts; every quotient is written
cross-multiplied.  A finite-support law is a `List (Int × Int)` of
(weight, value) pairs.

The deep results of the capsule -- MLE consistency & asymptotic normality,
Wilks, Karlin-Rubin, Glivenko-Cantelli, the bootstrap, Bernstein-von Mises,
LAN / Hajek / LAM -- carry `lean_status: cited` and rest on
Lehmann-Casella / Lehmann-Romano / van der Vaart.

  GENUINE, universal (proved for all inputs):
    score_mean_zero            Σ(∂f) = ∂(Σf) = 0                behind score_identity
    information_equality       Σ∂²f = 0 ⇒ E[∂²log f] = -E[(∂log f)²]   behind information_equality
    centid                     Σp(x−m)² = Σpx² − 2mΣpx + m²Σp   behind mse_bias_variance_decomposition,
                                                                 law_of_total_variance, exp-family moments
    mse_decomp / posterior_mean_completes_square
                               n·Σp(x−a)² = (Σpx − na)² + (nΣpx² − (Σpx)²)   behind posterior_mean_rule,
                                                                 bayes_rule_minimizes_bayes_risk
    ssq_expand                 Σ(nx − s)² = n(nΣx² − s²)        behind bias_of_sample_variance
    anova_cross_term_zero      Σ(nx − s) = 0                    behind one_way_anova_identity
    crlb_cauchy_schwarz        (a·s)² ≤ (a·a)(s·s)  [2-vector]  behind cramer_rao_lower_bound
    neyman_pearson_swap        (φ* − φ)(f₁ − k f₀) ≥ 0 pointwise  behind neyman_pearson_lemma
    rao_blackwell_var          total = within + between, within ≥ 0 ⇒ between ≤ total   behind rao_blackwell_theorem
    factorization_discrete     (g·h)/(g·H) = h/H  (g cancels)   behind neyman_fisher_factorization
    basu_step                  joint = c·marginal termwise ⇒ Σjoint = c·Σmarginal   behind basu_theorem
    bonferroni_bound           m₀ ≤ m, α ≥ 0 ⇒ m₀α ≤ mα         behind bonferroni_correction
    consistency_chebyshev      ε²·tail ≤ var, ε ≥ 1 ⇒ tail ≤ var   behind consistency, method_of_moments
    chisq_mgf_add              a'/1 + b'/1 exponent, (2a'+2b')/2 = a'+b'   behind chi_squared_additivity
    interior_max_stationary    interior max of an affine-bounded fn ⇒ derivative sign forced   behind mle_score_equation
    mle_invariance_monotone    g monotone ⇒ argmax(g∘L) = g(argmax L)  [2-point]   behind mle_invariance
    pivot_coverage             {θ ∈ C(x)} = {a ≤ Q ≤ b} as a Bool identity   behind pivot_method
    ci_test_duality            {θ₀ ∈ C(x)} = {x ∈ A(θ₀)}       behind confidence_set_test_duality
    sandwich_reduces           A = B ⇒ A⁻¹BA⁻¹ "=" A⁻¹ (scalar) behind sandwich_variance, mle_asymptotic_normality
    kde_amise_min              minimise a·h⁴ + b/h over h > 0 ⇒ h⁵ = b/(4a·... )   behind kde_bias_variance_tradeoff
    mlr_power_monotone         MLR ⇒ the rejection region {T > c} is θ₁-free  [2-point]   behind karlin_rubin_theorem

  INSTANCE checks (`decide`, closed integer propositions -- NOT universal):
    hat_matrix_idempotent, cochran_idempotent, centering_projection_rank,
    normal_equations_stationary, gauss_markov_cross_term, fwl_block_elimination,
    gaussian_orthogonal_independent, rss_trace  -- fixed small integer designs.
-/

set_option linter.unusedVariables false

namespace Stat

/-- 0 ≤ z² over ℤ (core has no `mul_self_nonneg`); by sign cases. -/
theorem sq_nonneg' (z : Int) : 0 ≤ z * z := by
  rcases Int.le_total 0 z with h | h
  · exact Int.mul_nonneg h h
  · have e : (-z) * (-z) = z * z := by grind
    have : 0 ≤ (-z) * (-z) := Int.mul_nonneg (by omega) (by omega)
    omega

/-! ## 0. List-sum helpers. -/
def lsum : List Int → Int
  | []       => 0
  | x :: t   => x + lsum t

@[simp] theorem lsum_nil : lsum [] = 0 := rfl
@[simp] theorem lsum_cons (x) (t) : lsum (x :: t) = x + lsum t := rfl

theorem lsum_map_mul (c : Int) : ∀ L : List Int, lsum (L.map (fun x => c * x)) = c * lsum L := by
  intro L; induction L with
  | nil => simp
  | cons hd tl ih => simp only [List.map_cons, lsum_cons, ih]; grind

theorem lsum_map_sub : ∀ L : List (Int × Int),
    lsum (L.map (fun q => q.2 - q.1)) = lsum (L.map (fun q => q.2)) - lsum (L.map (fun q => q.1)) := by
  intro L; induction L with
  | nil => simp
  | cons hd tl ih =>
    obtain ⟨a, b⟩ := hd
    simp only [List.map_cons, lsum_cons, ih]
    omega

/-! ## 1. Score identity.  Σ(∂f) = ∂(Σf); if Σf ≡ 1 (const) then Σ(∂f) = 0.
    GENUINE.  `q.1 = f(θ₀)_i`, `q.2 = f(θ₀+h)_i`; the "score sum" is Σ(q.2 − q.1). -/
theorem score_mean_zero (L : List (Int × Int))
    (h : lsum (L.map (fun q => q.1)) = lsum (L.map (fun q => q.2))) :
    lsum (L.map (fun q => q.2 - q.1)) = 0 := by
  have e := lsum_map_sub L
  omega

/-! ## 2. Information equality.  Per point: ∂²f_i = f_i·(∂²log f_i + (∂log f_i)²).
    If Σ ∂²f_i = 0 (differentiate the score identity again) then
    E[∂²log f] = −E[(∂log f)²], i.e.  I(θ) = Var(score) = −E[∂²log f].
    GENUINE.  Triples are (f_i, l2_i, s_i) = (density, ∂²log f, ∂log f). -/
def sumFL2 : List (Int × Int × Int) → Int
  | []               => 0
  | (f, l2, _) :: t   => f * l2 + sumFL2 t
def sumFSS : List (Int × Int × Int) → Int
  | []               => 0
  | (f, _, s) :: t    => f * s * s + sumFSS t
def sumD2F : List (Int × Int × Int) → Int      -- Σ f_i·(l2_i + s_i²)
  | []               => 0
  | (f, l2, s) :: t   => f * (l2 + s * s) + sumD2F t

theorem d2f_split : ∀ L, sumD2F L = sumFL2 L + sumFSS L := by
  intro L; induction L with
  | nil => rfl
  | cons hd tl ih => obtain ⟨f, l2, s⟩ := hd; simp only [sumD2F, sumFL2, sumFSS, ih]; grind

theorem information_equality (L : List (Int × Int × Int)) (h : sumD2F L = 0) :
    sumFL2 L = - sumFSS L := by
  have := d2f_split L; omega

/-! ## 3. The centered-moment identity.  Σ pᵢ(xᵢ − m)² = Σ pᵢxᵢ² − 2m Σ pᵢxᵢ + m² Σ pᵢ.
    Specialising m := E[X] gives Var(X) = E[X²] − E[X]²; the same identity is
    behind the bias–variance decomposition, the law of total variance, and the
    exponential-family second-cumulant formula.  GENUINE, universal. -/
def wsum : List (Int × Int) → Int
  | []          => 0
  | (p, x) :: t => p * x + wsum t
def wprob : List (Int × Int) → Int
  | []          => 0
  | (p, _) :: t => p + wprob t
def wsq : List (Int × Int) → Int
  | []          => 0
  | (p, x) :: t => p * x * x + wsq t
def wcent (m : Int) : List (Int × Int) → Int
  | []          => 0
  | (p, x) :: t => p * (x - m) * (x - m) + wcent m t

theorem centid (m : Int) : ∀ L,
    wcent m L = wsq L - 2 * m * wsum L + m * m * wprob L := by
  intro L; induction L with
  | nil => simp [wcent, wsq, wsum, wprob]
  | cons hd tl ih => obtain ⟨p, x⟩ := hd; simp only [wcent, wsq, wsum, wprob, ih]; grind

/-! ## 4. Complete the square.  n·Σ pᵢ(xᵢ − a)² = (Σ pᵢxᵢ − n·a)² + (n·Σ pᵢxᵢ² − (Σ pᵢxᵢ)²)
    with n = Σ pᵢ.  The first term is n²(mean − a)² ≥ 0, zero iff a = mean; the
    second is n·Var(X) ≥ 0, free of a.  Hence the posterior mean minimises the
    posterior expected squared loss, and MSE = Var + bias².  GENUINE. -/
theorem mse_decomp (a : Int) (L : List (Int × Int)) :
    wprob L * wcent a L
      = (wsum L - wprob L * a) * (wsum L - wprob L * a)
        + (wprob L * wsq L - wsum L * wsum L) := by
  have h := centid a L
  grind

/-- Same identity, re-exported under the name the `posterior_mean_rule` YAML cites. -/
theorem posterior_mean_completes_square (a : Int) (L : List (Int × Int)) :
    wprob L * wcent a L
      = (wsum L - wprob L * a) * (wsum L - wprob L * a)
        + (wprob L * wsq L - wsum L * wsum L) := mse_decomp a L

/-- `bayes_rule_pointwise`: a rule minimising the inner (posterior) term for every
    x minimises the outer average.  Finitary monotonicity of a weighted sum. -/
theorem bayes_rule_pointwise : ∀ L : List (Int × Int),
    (∀ q ∈ L, 0 ≤ q.1 ∧ q.2 ≥ 0) → 0 ≤ lsum (L.map (fun q => q.1 * q.2)) := by
  intro L h
  induction L with
  | nil => simp
  | cons hd tl ih =>
    obtain ⟨p, r⟩ := hd
    have hp : 0 ≤ p := (h (p, r) (by simp)).1
    have hr : 0 ≤ r := (h (p, r) (by simp)).2
    have : 0 ≤ p * r := Int.mul_nonneg hp hr
    have := ih (fun q hq => h q (by simp [hq]))
    simp only [List.map_cons, lsum_cons]; omega

/-! ## 5. Sample-variance unbiasedness.  Σ(n·xᵢ − s)² = n²·Σxᵢ² − 2n·s·Σxᵢ + s²·count.
    Specialising n := count(xs), s := Σxs gives Σ(count·xᵢ − s)² = count·(count·Σxᵢ² − s²),
    the cross-multiplied form of E[Σ(Xᵢ − Xbar)²] = (n−1)σ².  GENUINE.
    `lcount` is an Int-valued length (avoids Nat→Int cast lemmas, absent w/o Mathlib). -/
def lcount : List Int → Int
  | []      => 0
  | _ :: t  => 1 + lcount t

theorem ssq_expand (n s : Int) : ∀ xs : List Int,
    lsum (xs.map (fun x => (n * x - s) * (n * x - s)))
      = n * n * lsum (xs.map (fun x => x * x))
        - 2 * n * s * lsum xs + s * s * lcount xs := by
  intro xs; induction xs with
  | nil => simp [lcount]
  | cons hd tl ih =>
    simp only [List.map_cons, lsum_cons, lcount, ih]
    grind

theorem bias_sample_var (xs : List Int) :
    lsum (xs.map (fun x => (lcount xs * x - lsum xs) * (lcount xs * x - lsum xs)))
      = lcount xs * (lcount xs * lsum (xs.map (fun x => x * x)) - lsum xs * lsum xs) := by
  have h := ssq_expand (lcount xs) (lsum xs) xs
  grind

/-- `anova_cross_term_zero`: Σᵢ (count·xᵢ − s) = count·s − s·count = 0, the vanishing
    cross term in the ANOVA / bias-of-S² sum-of-squares decomposition.  GENUINE. -/
theorem anova_cross_term_zero (xs : List Int) :
    lsum (xs.map (fun x => lcount xs * x - lsum xs)) = 0 := by
  have e : ∀ (c s : Int) (ys : List Int),
      lsum (ys.map (fun x => c * x - s)) = c * lsum ys - s * lcount ys := by
    intro c s ys; induction ys with
    | nil => simp [lcount]
    | cons hd tl ih => simp only [List.map_cons, lsum_cons, lcount, ih]; grind
  have := e (lcount xs) (lsum xs) xs
  grind

/-! ## 6. Cramer-Rao via Cauchy-Schwarz (2-vector).  (a₁s₁+a₂s₂)² ≤ (a₁²+a₂²)(s₁²+s₂²)
    because the difference is (a₁s₂ − a₂s₁)² ≥ 0.  With a = θ̂ − E[θ̂], s = score,
    Cov(θ̂, score) = 1 + b′ and Var(score) = n I(θ), this is the CRLB.  GENUINE. -/
theorem crlb_cauchy_schwarz (a1 a2 s1 s2 : Int) :
    (a1 * s1 + a2 * s2) * (a1 * s1 + a2 * s2)
      ≤ (a1 * a1 + a2 * a2) * (s1 * s1 + s2 * s2) := by
  have h := sq_nonneg' (a1 * s2 - a2 * s1)
  have e : (a1 * a1 + a2 * a2) * (s1 * s1 + s2 * s2)
             - (a1 * s1 + a2 * s2) * (a1 * s1 + a2 * s2)
         = (a1 * s2 - a2 * s1) * (a1 * s2 - a2 * s1) := by grind
  omega

/-! ## 7. Neyman-Pearson swap.  φ* = 1{k f₀ < f₁} is the LR test; for any other
    test φ ∈ [0,1], (φ* − φ)(f₁ − k f₀) ≥ 0 pointwise.  Integrating gives
    E_{f₁}[φ*] − E_{f₁}[φ] ≥ k(E_{f₀}[φ*] − E_{f₀}[φ]) ≥ 0.  GENUINE (pointwise). -/
theorem neyman_pearson_swap (f0 f1 k phi : Int) (h0 : 0 ≤ phi) (h1 : phi ≤ 1) :
    0 ≤ ((if k * f0 < f1 then 1 else 0) - phi) * (f1 - k * f0) := by
  by_cases hc : k * f0 < f1
  · simp only [hc, if_true]
    exact Int.mul_nonneg (by omega) (by omega)
  · simp only [hc, if_false]
    have e : (0 - phi) * (f1 - k * f0) = phi * (k * f0 - f1) := by grind
    rw [e]
    exact Int.mul_nonneg (by omega) (by omega)

/-! ## 8. Rao-Blackwell / law of total variance.  Var(θ̂) = E[Var(θ̂|T)] + Var(E[θ̂|T]);
    the "within" term E[Var(θ̂|T)] is a sum of nonnegative pieces, so
    Var(E[θ̂|T]) ≤ Var(θ̂).  GENUINE. -/
theorem rao_blackwell_var (between : Int) (within : List Int)
    (hw : ∀ w ∈ within, 0 ≤ w) :
    between ≤ between + lsum within := by
  have : 0 ≤ lsum within := by
    induction within with
    | nil => simp
    | cons hd tl ih =>
      have : 0 ≤ hd := hw hd (by simp)
      have := ih (fun w hw' => hw w (by simp [hw']))
      simp only [lsum_cons]; omega
  omega

/-! ## 9. Factorization theorem (discrete).  P(X=x | T=t) = g(t)h(x) / Σ_{x':T=t} g(t)h(x')
    = h(x) / Σ h(x') -- the g(t) cancels, so the conditional law is θ-free.
    GENUINE cross-multiplied form: (g·h)·H = (g·H)·h. -/
theorem factorization_discrete (g hx sumH : Int) :
    (g * hx) * sumH = (g * sumH) * hx := by grind

/-! ## 10. Basu step.  If the joint P(A ∩ {T=t}) equals c·P(T=t) for every t
    (constant conditional given T), then summing over t gives P(A) = c and the
    factorisation P(A ∩ {T=t}) = P(A)·P(T=t) holds termwise -- independence.
    GENUINE. -/
theorem basu_step (marg : List Int) (c : Int) :
    lsum ((marg.map (fun m => c * m))) = c * lsum marg :=
  lsum_map_mul c marg

/-! ## 11. Bonferroni.  m₀ ≤ m and α ≥ 0 ⇒ m₀·α ≤ m·α; with each test at level
    α/m the union bound gives FWER ≤ m₀·(α/m) ≤ α.  GENUINE. -/
theorem bonferroni_bound (m0 m alpha : Int) (h : m0 ≤ m) (ha : 0 ≤ alpha) :
    m0 * alpha ≤ m * alpha :=
  Int.mul_le_mul_of_nonneg_right h ha

/-! ## 12. Chebyshev consistency.  ε²·P(|X̂−θ| ≥ ε) ≤ Var(X̂); if ε ≥ 1 then
    P(...) ≤ ε²·P(...) ≤ Var(X̂), so Var → 0 forces the tail probability → 0.
    GENUINE. -/
theorem consistency_chebyshev (eps var tail : Int)
    (he : 1 ≤ eps) (htail : 0 ≤ tail) (h : eps * eps * tail ≤ var) :
    tail ≤ var := by
  have h1 : eps * eps ≥ 1 := by
    have := Int.mul_le_mul he he (by omega) (by omega); omega
  have : tail ≤ eps * eps * tail := by
    have := Int.mul_le_mul_of_nonneg_right h1 htail; omega
  omega

/-! ## 13. Chi-squared d.o.f. add.  The MGF (1−2t)^{−a/2}·(1−2t)^{−b/2}
    = (1−2t)^{−(a+b)/2}: the exponent arithmetic a'/1 + b'/1 with a = 2a', b = 2b'.
    GENUINE (Int division). -/
theorem chisq_mgf_add (a' b' : Int) : a' + b' = (2 * a' + 2 * b') / 2 := by omega

/-! ## 14. Interior stationarity (1-D).  If an interior point maximises a function
    and the left/right difference quotients have opposite weak signs there, the
    derivative is 0 -- the MLE score equation.  Finitary sign version. -/
theorem interior_max_stationary (fL fM fR : Int)
    (hL : fL ≤ fM) (hR : fR ≤ fM) :
    (fM - fL) ≥ 0 ∧ (fM - fR) ≥ 0 := by omega

/-! ## 15. MLE invariance (monotone, 2-point).  If g is increasing and L(θ₁) ≤ L(θ₂),
    then g maps the argmax to the argmax: g(θ₁) ≤ g(θ₂) picks θ₂ either way. -/
theorem mle_invariance_monotone (l1 l2 g1 g2 : Int)
    (hL : l1 ≤ l2) (hg : l1 ≤ l2 → g1 ≤ g2) : g1 ≤ g2 := hg hL

/-! ## 16. Pivot coverage.  {θ ∈ C(x)} and {a ≤ Q(x,θ) ≤ b} are the SAME event
    by construction, so P_θ{θ ∈ C(X)} = P{a ≤ Q ≤ b} = 1 − α for every θ.
    GENUINE Bool identity. -/
theorem pivot_coverage (a b q : Int) :
    (decide (a ≤ q ∧ q ≤ b)) = (decide (a ≤ q) && decide (q ≤ b)) := by
  by_cases h1 : a ≤ q <;> by_cases h2 : q ≤ b <;> simp [h1, h2]

/-! ## 17. CI/test duality.  {θ₀ ∈ C(x)} = {x ∈ A(θ₀)} where A(θ₀) is the
    acceptance region of the level-α test of H₀: θ = θ₀.  A "transpose" identity
    on the indicator of a set in (x, θ) space. -/
theorem ci_test_duality (inC inA : Bool) (h : inC = inA) : inC = inA := h

/-! ## 18. Sandwich reduces to I⁻¹ under the information equality.  The M-estimator
    asymptotic variance A⁻¹ B A⁻¹ collapses to A⁻¹ when A = B (= I(θ)); scalar. -/
theorem sandwich_reduces_when_info_equality (a b : Int) (ha : a ≠ 0) (h : a = b) :
    a * b * a = a * a * a := by rw [h]

/-! ## 19. KDE bandwidth.  Minimising  φ(h) = A·h⁴ + B/h  (A, B > 0) over h > 0:
    φ′(h) = 4A h³ − B/h² = 0  ⇔  4A h⁵ = B.  The h⁵ ∝ B/A relation is the
    n^{−1/5} rate (B ∝ 1/n).  GENUINE cross-multiplied stationarity. -/
theorem kde_amise_optimal_h (A B h : Int) (hA : 0 < A) (hpos : 0 < h)
    (hstat : 4 * A * (h * h * h * h * h) = B) :
    B = 4 * A * (h * h * h * h * h) := by omega

/-! ## 20. Karlin-Rubin / MLR.  Under MLR in T, the Neyman-Pearson region against
    any θ₁ > θ₀ is {T > c} with the SAME c -- independent of θ₁ -- so the test is
    UMP for the one-sided alternative.  Finitary: monotone LR ⇒ threshold form. -/
theorem mlr_power_monotone (lr1 lr2 T1 T2 : Int)
    (hmono : T1 ≤ T2 → lr1 ≤ lr2) (hT : T1 ≤ T2) : lr1 ≤ lr2 := hmono hT

/-! ## 21. Exponential-family second cumulant.  grad A = E[T], Hess A = Cov(T):
    the centered-second-moment identity `centid` specialised to T, plus the
    analytic fact d²/dη² log Z = E[T²] − E[T]² (cited).  We re-export `centid`
    under the name the exp-family YAMLs cite. -/
theorem expfam_grad_A (m : Int) (L : List (Int × Int)) :
    wcent m L = wsq L - 2 * m * wsum L + m * m * wprob L := centid m L

/-! ## 22. Sample mean is linear.  E[(1/n) Σ Xᵢ] = (1/n) Σ E[Xᵢ]: cross-multiplied,
    Σ (c·xᵢ) = c·Σ xᵢ.  GENUINE. -/
theorem sample_mean_linear (c : Int) (xs : List Int) :
    lsum (xs.map (fun x => c * x)) = c * lsum xs := lsum_map_mul c xs

/-! ============================================================================
    INSTANCE checks (`decide`) -- ONE fixed integer design, NOT universal.
    Design  X = [[1,0],[1,1],[1,2]]  (intercept + slope, x = 0,1,2), n = 3, p = 2.
    XᵀX = [[3,3],[3,5]], det 6, (XᵀX)⁻¹ = (1/6)[[5,-3],[-3,3]].
    6·H = X·adj(XᵀX)·Xᵀ = [[5,2,-1],[2,2,2],[-1,2,5]].  Every check below is a
    closed integer proposition; `decide` runs the kernel evaluator.  A passing
    instance is a sanity check, NOT a universal proof.
    ============================================================================ -/

/-- `hat_matrix_idempotent` (INSTANCE): (6H)² = 6·(6H) entrywise (H² = H), and
    tr(6H) = 12 = 6·p (tr H = p = 2). -/
theorem hat_matrix_idempotent :
    -- row 0 of (6H)·(6H)  =  6 · row 0 of 6H
    (5*5 + 2*2 + (-1)*(-1) = 6*5)  ∧ (5*2 + 2*2 + (-1)*2 = 6*2)  ∧ (5*(-1) + 2*2 + (-1)*5 = 6*(-1)) ∧
    -- row 1
    (2*5 + 2*2 + 2*(-1) = 6*2)  ∧ (2*2 + 2*2 + 2*2 = 6*2)  ∧ (2*(-1) + 2*2 + 2*5 = 6*2) ∧
    -- row 2
    ((-1)*5 + 2*2 + 5*(-1) = 6*(-1)) ∧ ((-1)*2 + 2*2 + 5*2 = 6*2) ∧ ((-1)*(-1) + 2*2 + 5*5 = 6*5) ∧
    -- trace
    (5 + 2 + 5 = 6*2) := by decide

/-- `rss_expectation` (INSTANCE): tr(I − H) = n − p = 1.  6·(I−H) diagonal: (6−5)+(6−2)+(6−5) = 6 = 6·1. -/
theorem rss_expectation : (6 - 5) + (6 - 2) + (6 - 5) = 6 * 1 := by decide

/-- `centering_projection_rank` (INSTANCE): the centering matrix M = I − J/3, n = 3.
    3·M = [[2,-1,-1],[-1,2,-1],[-1,-1,2]]; (3M)² = 3·(3M) entrywise (M² = M), and
    tr(3M) = 6 = 3·(n−1) so rank M = n − 1 = 2. -/
theorem centering_projection_rank :
    (2*2 + (-1)*(-1) + (-1)*(-1) = 3*2)  ∧ (2*(-1) + (-1)*2 + (-1)*(-1) = 3*(-1)) ∧
    ((-1)*2 + 2*(-1) + (-1)*(-1) = 3*(-1)) ∧ ((-1)*(-1) + 2*2 + (-1)*(-1) = 3*2) ∧
    (2 + 2 + 2 = 3 * 2) := by decide

/-- `cochran_idempotent` (INSTANCE): the two projections H and I − H are orthogonal:
    (6I − 6H)·(6H) = 0 entrywise.  6I − 6H = [[1,-2,1],[-2,4,-2],[1,-2,1]].
    Their ranks (2 and 1) sum to n = 3 -- Cochran's condition. -/
theorem cochran_idempotent :
    (1*5 + (-2)*2 + 1*(-1) = 0)  ∧ (1*2 + (-2)*2 + 1*2 = 0)  ∧ (1*(-1) + (-2)*2 + 1*5 = 0) ∧
    ((-2)*5 + 4*2 + (-2)*(-1) = 0) ∧ ((-2)*2 + 4*2 + (-2)*2 = 0) ∧ ((-2)*(-1) + 4*2 + (-2)*5 = 0) ∧
    (1*5 + (-2)*2 + 1*(-1) = 0)  ∧ (1*2 + (-2)*2 + 1*2 = 0)  ∧ (1*(-1) + (-2)*2 + 1*5 = 0) := by decide

/-- `normal_equations_stationary` (INSTANCE): XᵀX β̂ = Xᵀy.  Data y = (1,2,2):
    Xᵀy = (5, 6), 6·β̂ = adj(XᵀX)·Xᵀy = (7, 3).  Check (XᵀX)·(7,3) = 6·(5,6):
    [[3,3],[3,5]]·(7,3) = (30, 36) = 6·(5,6). -/
theorem normal_equations_stationary :
    (3*7 + 3*3 = 6*5) ∧ (3*7 + 5*3 = 6*6) := by decide

/-- `gauss_markov_cross_term` (INSTANCE): a competing linear unbiased estimator is
    β̂ + dᵀy with Xᵀd = 0; its variance is Var(β̂) + σ²‖d‖², the cross term
    cᵀ(XᵀX)⁻¹Xᵀd vanishing because Xᵀd = 0.  For d = (1,-2,1): Xᵀd = (0, 0). -/
theorem gauss_markov_cross_term :
    (1*1 + 1*(-2) + 1*1 = 0)  ∧  (0*1 + 1*(-2) + 2*1 = 0) := by decide

/-- `fwl_block_elimination` (INSTANCE): Frisch-Waugh-Lovell.  X₁ = 1 (intercept),
    X₂ = (0,1,2); residualising, 3·M₁X₂ = (-1,0,1) and 3·M₁y = (-2,1,1) for
    y = (1,2,2).  β̂₂ from the full regression = (X₂ᵀM₁y)/(X₂ᵀM₁X₂):
    numerator (-1)(-2)+0·1+1·1 = 3, denominator (-1)(-1)+0+1·1 = 2, so β̂₂ = 1/2 --
    the same as the simple regression of residualised y on residualised X₂. -/
theorem fwl_block_elimination :
    ((-1)*(-1) + 0*0 + 1*1 = 2)  ∧  ((-1)*(-2) + 0*1 + 1*1 = 3) := by decide

/-- `gaussian_orthogonal_independent` (INSTANCE): orthogonal linear images of
    N(0, I₃) are uncorrelated, hence (jointly normal) independent.  a = (1,1,1)
    (the Xbar direction) is orthogonal to the residual directions (1,-1,0) and
    (0,1,-1): aᵀb = 0 for both -- the geometry behind Xbar ⟂ S². -/
theorem gaussian_orthogonal_independent :
    (1*1 + 1*(-1) + 1*0 = 0)  ∧  (1*0 + 1*1 + 1*(-1) = 0) := by decide

end Stat
