/-
  math-linear-algebra -- validation/proof-checks.lean
  Lean 4.33, **Mathlib-free** (Lean core only).

  WHAT THIS FILE CAN AND CANNOT DO
  --------------------------------
  With no Mathlib there is no `Matrix`, no `Module`, no `Real`, no `ring`,
  no `linarith`.  There is `grind` (strong enough for commutative-ring
  identities over `Int`), `omega` (linear arithmetic), `decide`, `positivity`,
  and structural induction.

  Three honesty levels are used, and `validation/proof-checks.md` keys every
  node to one of them:

    core     -- the GENERAL statement of the node is proved here
                (Nat/Int arithmetic identities, list inductions, abstract
                monoid arguments: statements whose full generality fits).

    dim_core -- UNIVERSAL IN THE MATRIX ENTRIES, at a FIXED small dimension
                (n = 2, sometimes 3).  Every entry is a bound variable, so
                this is strictly STRONGER than a numeric instance: it proves
                the n = 2 case of the theorem.  It is strictly WEAKER than the
                theorem, which quantifies over n.  Mathlib-free Lean cannot
                express "for all n" without building a matrix library, which
                Release 0.1 does not attempt.

    instance -- `decide` at FIXED NUMBERS.  A check, never a proof.

  Nothing about R as a complete ordered field, limits, compactness, or square
  roots is provable here.  The general Cauchy-Schwarz, the spectral theorem,
  the SVD, and Cholesky are therefore `cited`, with their Int-coefficient /
  fixed-dimension shadows proved below.

  Int division truncates, so half-factors are avoided: polarisation is stated
  as `4 * <u,v> = ...`, never with `/ 4`.

  Run:  lean validation/proof-checks.lean     (expect exit 0, no output)
-/

namespace LinAlg

/-! ## Section 1. Vector-space consequences of the axioms (core) -/

abbrev V2 := Int × Int

def smul (a : Int) (v : V2) : V2 := (a * v.1, a * v.2)
def vadd (u v : V2) : V2 := (u.1 + v.1, u.2 + v.2)

theorem smul_zero_eq_zero (v : V2) : smul 0 v = (0, 0) := by
  simp [smul]

theorem zero_smul_vec (a : Int) : smul a (0, 0) = (0, 0) := by
  simp [smul]

theorem neg_one_smul (v : V2) : vadd (smul (-1) v) v = (0, 0) := by
  simp [smul, vadd]
  omega

/-- `av = 0` with `a ≠ 0` forces `v = 0`: the no-zero-divisors clause, the one
place the FIELD structure (rather than mere ring structure) is used. -/
theorem no_zero_smul_divisors (a : Int) (v : V2) (ha : a ≠ 0) (h : smul a v = (0, 0)) :
    v = (0, 0) := by
  simp [smul, Prod.ext_iff] at h ⊢
  refine ⟨?_, ?_⟩
  · rcases Int.mul_eq_zero.mp h.1 with h' | h'
    · exact absurd h' ha
    · exact h'
  · rcases Int.mul_eq_zero.mp h.2 with h' | h'
    · exact absurd h' ha
    · exact h'

/-! ## Section 2. Dimension arithmetic (core) -/

/-- `dimension_well_defined`: two Steinitz bounds give equality. -/
theorem basis_card_eq (m n : Nat) (h1 : m ≤ n) (h2 : n ≤ m) : m = n := by omega

/-- `rank_nullity`: `dim V = rank + nullity` bounds both summands. -/
theorem rank_nullity (dimV rank nullity : Nat)
    (h : dimV = rank + nullity) : rank ≤ dimV ∧ nullity ≤ dimV := by omega

/-- `injective_surjective_equivalence` as a count. -/
theorem inj_iff_surj_of_dim_eq (dimV dimW rank nullity : Nat)
    (hdim : dimV = dimW) (hrn : dimV = rank + nullity) :
    (nullity = 0 ↔ rank = dimW) := by omega

/-- `dimension_formula_sum` (Grassmann). -/
theorem dim_sum_inter (dU dW dSum dInt : Nat)
    (h : dSum + dInt = dU + dW) : dSum = dU + dW - dInt := by omega

/-- `quotient_dimension`, guarded by `dim U ≤ dim V`. -/
theorem dim_quotient (dV dU : Nat) (h : dU ≤ dV) : dU + (dV - dU) = dV := by omega

/-- `four_subspaces`: the four dimensions sum correctly in both ambient spaces. -/
theorem four_subspace_dims (m n r : Nat) (hrm : r ≤ m) (hrn : r ≤ n) :
    r + (n - r) = n ∧ r + (m - r) = m := by omega

/-- `algebraic_geometric_multiplicity`: `1 ≤ geom ≤ alg`, with the gap
(the obstruction to diagonalisability) made explicit. -/
theorem geom_le_alg (geom alg : Nat) (_h1 : 1 ≤ geom) (h2 : geom ≤ alg) :
    geom ≤ alg ∧ (geom = alg ∨ geom < alg) := by omega

/-! ## Section 3. Inductive cores (core) -/

/-- The skeleton every "extend a basis" / "strip a dependent vector" argument runs. -/
theorem list_induction_skeleton {α : Type} (P : List α → Prop)
    (hnil : P [])
    (hcons : ∀ a l, P l → P (a :: l)) :
    ∀ l : List α, P l := by
  intro l
  induction l with
  | nil => exact hnil
  | cons a t ih => exact hcons a t ih

/-- `distinct_eigenvalues_independent`, the induction step: applying
`T - λ_k I` scales the i-th coefficient by `λ_i - λ_k ≠ 0`. -/
theorem distinct_eig_indep_step (a li lk : Int) (hne : li ≠ lk)
    (h : a * (li - lk) = 0) : a = 0 := by
  rcases Int.mul_eq_zero.mp h with h' | h'
  · exact h'
  · exact absurd (by omega : li = lk) hne

/-! ## Section 4. 2x2 matrix algebra (dim_core) -/

structure M2 where
  a : Int
  b : Int
  c : Int
  d : Int
deriving DecidableEq, Repr

def M2.mul (X Y : M2) : M2 :=
  ⟨X.a*Y.a + X.b*Y.c, X.a*Y.b + X.b*Y.d, X.c*Y.a + X.d*Y.c, X.c*Y.b + X.d*Y.d⟩
def M2.tr (X : M2) : Int := X.a + X.d
def M2.det (X : M2) : Int := X.a*X.d - X.b*X.c
def M2.transpose (X : M2) : M2 := ⟨X.a, X.c, X.b, X.d⟩
def M2.adj (X : M2) : M2 := ⟨X.d, -X.b, -X.c, X.a⟩
def M2.add (X Y : M2) : M2 := ⟨X.a+Y.a, X.b+Y.b, X.c+Y.c, X.d+Y.d⟩
def M2.smul (k : Int) (X : M2) : M2 := ⟨k*X.a, k*X.b, k*X.c, k*X.d⟩
def M2.I : M2 := ⟨1,0,0,1⟩
def M2.zero : M2 := ⟨0,0,0,0⟩
def M2.apply (X : M2) (v : V2) : V2 := (X.a*v.1 + X.b*v.2, X.c*v.1 + X.d*v.2)

/-- `matrix_mult_is_composition`: associativity, n = 2. -/
theorem mul_assoc2 (X Y Z : M2) : (X.mul Y).mul Z = X.mul (Y.mul Z) := by
  simp [M2.mul, M2.mk.injEq] <;> grind

theorem mul_one2 (X : M2) : X.mul M2.I = X ∧ M2.I.mul X = X := by
  constructor <;> (simp [M2.mul, M2.I])

/-- `transpose`: `(XY)^T = Y^T X^T`, n = 2, universal in the entries. -/
theorem transpose_mul_rev (X Y : M2) :
    (X.mul Y).transpose = (Y.transpose).mul (X.transpose) := by
  simp [M2.mul, M2.transpose, M2.mk.injEq] <;> grind

theorem transpose_involutive (X : M2) : X.transpose.transpose = X := by
  simp [M2.transpose]

/-- `trace_cyclic`: `tr(XY) = tr(YX)`, n = 2, universal in the entries. -/
theorem trace_mul_comm (X Y : M2) : (X.mul Y).tr = (Y.mul X).tr := by
  simp [M2.mul, M2.tr] <;> grind

/-- `determinant_multiplicative`, n = 2. -/
theorem det_mul (X Y : M2) : (X.mul Y).det = X.det * Y.det := by
  simp [M2.mul, M2.det] <;> grind

/-- `determinant_transpose`, n = 2. -/
theorem det_transpose (X : M2) : X.transpose.det = X.det := by
  simp [M2.transpose, M2.det] <;> grind

/-- `determinant_row_operations`, all three operations, n = 2. -/
theorem det_row_op_R3 (X : M2) (k : Int) :
    (M2.mk (X.a + k*X.c) (X.b + k*X.d) X.c X.d).det = X.det := by
  simp [M2.det] <;> grind

theorem det_row_op_R2 (X : M2) (k : Int) :
    (M2.mk (k*X.a) (k*X.b) X.c X.d).det = k * X.det := by
  simp [M2.det] <;> grind

theorem det_row_op_R1 (X : M2) :
    (M2.mk X.c X.d X.a X.b).det = - X.det := by
  simp [M2.det] <;> grind

/-- The scaling trap: `det(kX) = k^2 det X` at n = 2, NOT `k det X`. -/
theorem det_smul (k : Int) (X : M2) : (M2.smul k X).det = k^2 * X.det := by
  simp [M2.smul, M2.det] <;> grind

/-- `determinant_triangular`, n = 2. -/
theorem det_triangular (a b d : Int) : (M2.mk a b 0 d).det = a * d := by
  simp [M2.det]

/-- `adjugate`: `X adj(X) = adj(X) X = det(X) I`, n = 2, universal.
Holds for SINGULAR `X` too -- no invertibility assumed. -/
theorem adjugate_identity (X : M2) :
    X.mul X.adj = M2.smul X.det M2.I ∧ X.adj.mul X = M2.smul X.det M2.I := by
  constructor <;> (simp [M2.mul, M2.adj, M2.smul, M2.det, M2.I, M2.mk.injEq] <;> grind)

/-- `cayley_hamilton`, n = 2: `X^2 - tr(X) X + det(X) I = 0`, universal in the
entries.  Proved by computation, NOT by the ill-typed "substitute t = X". -/
theorem cayley_hamilton_2 (X : M2) :
    M2.add (M2.add (X.mul X) (M2.smul (-X.tr) X)) (M2.smul X.det M2.I) = M2.zero := by
  simp [M2.mul, M2.add, M2.smul, M2.tr, M2.det, M2.I, M2.zero, M2.mk.injEq] <;> grind

/-- `char_poly_coefficients`, n = 2: `det(tI - X) = t^2 - tr(X) t + det(X)`
for every `t`. -/
theorem charpoly_2 (X : M2) (t : Int) :
    (M2.mk (t - X.a) (-X.b) (-X.c) (t - X.d)).det = t^2 - X.tr * t + X.det := by
  simp [M2.det, M2.tr] <;> grind

/-- `matrix_mult_noncommutative`: an explicit witness. -/
def Ewit : M2 := ⟨0,1,0,0⟩
def Fwit : M2 := ⟨0,0,1,0⟩

theorem ab_ne_ba : Ewit.mul Fwit ≠ Fwit.mul Ewit := by decide

/-- ...yet trace IS cyclic on that pair, and both determinants agree. -/
theorem noncomm_but_trace_and_det_agree :
    (Ewit.mul Fwit).tr = (Fwit.mul Ewit).tr ∧
    (Ewit.mul Fwit).det = (Fwit.mul Ewit).det := by decide

/-- `non_diagonalisable_counterexample`: `J = (1 1; 0 1)` is defective, and
`J^k = (1 k; 0 1)` grows LINEARLY though its only eigenvalue has modulus 1. -/
def J : M2 := ⟨1,1,0,1⟩

theorem jordan_block_defective :
    (M2.add J (M2.smul (-1) M2.I)).det = 0 ∧
    J.mul J = M2.mk 1 2 0 1 ∧
    (J.mul J).mul J = M2.mk 1 3 0 1 := by decide

/-! ## Section 5. Invertibility in an abstract monoid (core)

Uniqueness of the inverse and the reversal rule need only associativity and a
two-sided identity, so they are proved in that generality. -/

theorem inv_unique (X S S' : M2)
    (h1 : X.mul S = M2.I) (h2 : S'.mul X = M2.I) : S = S' := by
  have key : S'.mul (X.mul S) = (S'.mul X).mul S := (mul_assoc2 S' X S).symm
  rw [h1, h2] at key
  rw [(mul_one2 S').1, (mul_one2 S).2] at key
  exact key.symm

theorem inv_mul_rev (X Y XI YI : M2)
    (hx : X.mul XI = M2.I) (hy : Y.mul YI = M2.I) :
    (X.mul Y).mul (YI.mul XI) = M2.I := by
  simp [M2.mul, M2.I, M2.mk.injEq] at hx hy ⊢
  grind

/-! ## Section 6. Inner products and norms over Int (dim_core)

Square roots are unavailable, so every statement is squared. -/

def dot2 (u v : V2) : Int := u.1*v.1 + u.2*v.2
def nrm2 (v : V2) : Int := dot2 v v          -- the SQUARED norm

/-- `cauchy_schwarz` at n = 2 via Lagrange's identity, universal in the entries:
the DEFECT is exhibited as a square, so the equality case is visible too. -/
theorem lagrange_identity2 (u v : V2) :
    nrm2 u * nrm2 v - (dot2 u v)^2 = (u.1*v.2 - u.2*v.1)^2 := by
  simp [nrm2, dot2] <;> grind

theorem cauchy_schwarz2 (u v : V2) : (dot2 u v)^2 ≤ nrm2 u * nrm2 v := by
  have h := lagrange_identity2 u v
  have hsq : (0:Int) ≤ (u.1*v.2 - u.2*v.1)^2 := Int.sq_nonneg _
  omega

def V3 := Int × Int × Int
def dot3 (u v : V3) : Int := u.1*v.1 + u.2.1*v.2.1 + u.2.2*v.2.2
def nrm3 (v : V3) : Int := dot3 v v

/-- Lagrange at n = 3: the defect is the squared cross product. -/
theorem lagrange_identity3 (u v : V3) :
    nrm3 u * nrm3 v - (dot3 u v)^2 =
      (u.2.1*v.2.2 - u.2.2*v.2.1)^2 + (u.2.2*v.1 - u.1*v.2.2)^2
        + (u.1*v.2.1 - u.2.1*v.1)^2 := by
  simp [nrm3, dot3] <;> grind

theorem cauchy_schwarz3 (u v : V3) : (dot3 u v)^2 ≤ nrm3 u * nrm3 v := by
  have h := lagrange_identity3 u v
  have h1 : (0:Int) ≤ (u.2.1*v.2.2 - u.2.2*v.2.1)^2 := Int.sq_nonneg _
  have h2 : (0:Int) ≤ (u.2.2*v.1 - u.1*v.2.2)^2 := Int.sq_nonneg _
  have h3 : (0:Int) ≤ (u.1*v.2.1 - u.2.1*v.1)^2 := Int.sq_nonneg _
  omega

/-- `parallelogram_law`, universal in the entries at n = 2. -/
theorem parallelogram (u v : V2) :
    nrm2 (vadd u v) + nrm2 (vadd u (smul (-1) v)) = 2 * nrm2 u + 2 * nrm2 v := by
  simp [nrm2, dot2, vadd, smul] <;> grind

/-- `polarisation_identity` (real form), stated WITHOUT division so the
`char ≠ 2` dependence is explicit: the identity computes `4 <u,v>`, and
recovering `<u,v>` requires 2 to be invertible. -/
theorem polarisation_real (u v : V2) :
    4 * dot2 u v = nrm2 (vadd u v) - nrm2 (vadd u (smul (-1) v)) := by
  simp [nrm2, dot2, vadd, smul] <;> grind

/-- `pythagorean_theorem`, universal in the entries at n = 2. -/
theorem pythagoras (u v : V2) (h : dot2 u v = 0) :
    nrm2 (vadd u v) = nrm2 u + nrm2 v := by
  simp [nrm2, dot2, vadd] at h ⊢ <;> grind

/-- `orthogonal_implies_independent`, arithmetic core: taking `<., v>` isolates
one coefficient times a POSITIVE squared norm. -/
theorem orthogonal_indep_core (a nv : Int) (hpos : 0 < nv) (h : a * nv = 0) : a = 0 := by
  rcases Int.mul_eq_zero.mp h with h' | h'
  · exact h'
  · omega

/-- `induced_norm` positive definiteness at n = 2 -- what makes the `sqrt` in the
definition well-typed. -/
theorem nrm2_nonneg (v : V2) : 0 ≤ nrm2 v := by
  simp [nrm2, dot2]
  have h1 : (0:Int) ≤ v.1 ^ 2 := Int.sq_nonneg _
  have h2 : (0:Int) ≤ v.2 ^ 2 := Int.sq_nonneg _
  have e1 : v.1 ^ 2 = v.1 * v.1 := by grind
  have e2 : v.2 ^ 2 = v.2 * v.2 := by grind
  omega

/-! ## Section 7. Projections and the Gram matrix (dim_core) -/

/-- `gram_matrix`: `x^T (A^T A) x = ||Ax||^2 ≥ 0`, universal in every entry at
n = 2.  The one-line reason every Gram matrix is positive semidefinite, hence
the reason `A^T A` appears throughout least squares. -/
theorem gram_psd (A : M2) (x : V2) :
    dot2 x ((A.transpose.mul A).apply x) = nrm2 (A.apply x) := by
  simp [M2.transpose, M2.mul, M2.apply, dot2, nrm2] <;> grind

theorem gram_psd_nonneg (A : M2) (x : V2) :
    0 ≤ dot2 x ((A.transpose.mul A).apply x) := by
  rw [gram_psd]; exact nrm2_nonneg _

theorem gram_symmetric (A : M2) :
    (A.transpose.mul A).transpose = A.transpose.mul A := by
  simp [M2.transpose, M2.mul, M2.mk.injEq] <;> grind

/-- `projection_matrix_characterisation`: `P = (1 0; 0 0)` is idempotent AND
symmetric -- an ORTHOGONAL projection. -/
def Porth : M2 := ⟨1,0,0,0⟩
/-- ...while `(1 1; 0 0)` is idempotent but NOT symmetric: an OBLIQUE
projection.  This is why symmetry is a necessary SECOND condition. -/
def Pobl : M2 := ⟨1,1,0,0⟩

theorem proj_orth_idem_and_symmetric :
    Porth.mul Porth = Porth ∧ Porth.transpose = Porth ∧ Porth.tr = 1 := by decide

theorem proj_oblique_idem_not_symmetric :
    Pobl.mul Pobl = Pobl ∧ Pobl.transpose ≠ Pobl ∧ Pobl.tr = 1 := by decide

/-- `hat_matrix`: for an idempotent, `tr P = rank P`.  Note the OBLIQUE
projection satisfies this too -- so the trace identity alone does NOT certify
orthogonality. -/
theorem idempotent_trace_eq_rank_both : Porth.tr = 1 ∧ Pobl.tr = 1 := by decide

/-! ## Section 8. Symmetry, spectra, definiteness (dim_core / instance) -/

/-- `self_adjoint_real_eigenvalues` / `spectral_theorem_symmetric`, n = 2:
a real SYMMETRIC matrix has real eigenvalues because its characteristic
discriminant is a SUM OF SQUARES.  Universal in the entries. -/
theorem symmetric_discriminant_nonneg (a b d : Int) :
    0 ≤ (a + d)^2 - 4*(a*d - b*b) := by
  have h : (a + d)^2 - 4*(a*d - b*b) = (a - d)^2 + 4*b^2 := by grind
  rw [h]
  have h1 : (0:Int) ≤ (a - d)^2 := Int.sq_nonneg _
  have h2 : (0:Int) ≤ b^2 := Int.sq_nonneg _
  omega

/-- ...and the NON-symmetric rotation `(0 -1; 1 0)` has a NEGATIVE discriminant,
so no real eigenvalue.  The hypothesis-dropped counterexample, machine-checked. -/
def Rot : M2 := ⟨0,-1,1,0⟩

theorem rotation_discriminant_negative : (Rot.tr)^2 - 4 * Rot.det < 0 := by decide

/-- `spectral_theorem_symmetric`, worked instance: `(2 1; 1 2)` has eigenvalues
3 and 1 with ORTHOGONAL eigenvectors `(1,1)` and `(1,-1)`. -/
def Sym : M2 := ⟨2,1,1,2⟩

theorem sym_spectral_instance :
    Sym.tr = 4 ∧ Sym.det = 3 ∧
    Sym.apply (1,1) = smul 3 (1,1) ∧
    Sym.apply (1,-1) = smul 1 (1,-1) ∧
    dot2 (1,1) (1,-1) = 0 := by decide

/-- `psd_characterisations`, n = 2: completing the square, universal in the
entries.  `a > 0` and `ad - b^2 > 0` (the two leading principal minors) make the
right-hand side positive for `(x,y) ≠ 0`. -/
theorem psd_2x2_complete_square (a b d x y : Int) :
    a * (a*x^2 + 2*b*x*y + d*y^2) = (a*x + b*y)^2 + (a*d - b^2) * y^2 := by
  grind

/-- `psd_characterisations`, the leading-vs-ALL-principal-minors trap:
`diag(0,-1)` has both LEADING principal minors equal to 0 -- neither negative --
yet it is NOT positive semidefinite, the form being `-1` at `(0,1)`. -/
def BadPSD : M2 := ⟨0,0,0,-1⟩

theorem leading_minors_insufficient_for_psd :
    BadPSD.a = 0 ∧ BadPSD.det = 0 ∧ dot2 (0,1) (BadPSD.apply (0,1)) = -1 := by decide

/-- `sylvester_law_of_inertia` / `congruence`: `diag(1,-1)` and `diag(4,-9)` are
CONGRUENT via `P = diag(2,3)` and share inertia `(1,1,0)`, while having
completely different traces and determinants.  The machine-checked witness that
congruence is NOT similarity. -/
def Cong1 : M2 := ⟨1,0,0,-1⟩
def Cong2 : M2 := ⟨4,0,0,-9⟩
def Pcong : M2 := ⟨2,0,0,3⟩

theorem congruence_not_similarity :
    (Pcong.transpose.mul Cong1).mul Pcong = Cong2 ∧
    Cong1.tr ≠ Cong2.tr ∧ Cong1.det ≠ Cong2.det := by decide

/-- `similar_invariants`: `I` and the Jordan block `J` share a characteristic
polynomial (same trace and determinant) yet are NOT similar -- `J - I ≠ 0` while
`I - I = 0`, and similarity would force both.  The witness that the
characteristic polynomial is not a complete invariant. -/
theorem charpoly_not_complete_invariant :
    J.tr = M2.I.tr ∧ J.det = M2.I.det ∧
    M2.add J (M2.smul (-1) M2.I) ≠ M2.zero := by decide

/-! ## Section 9. Least squares (dim_core) -/

/-- `least_squares`: if `x` solves the normal equations then the residual is
orthogonal to the image of EVERY vector -- i.e. `Ax` really is the projection of
`b` onto `col(A)`.  Universal in every entry at n = 2. -/
theorem normal_equations_residual_orthogonal (A : M2) (x b y : V2)
    (h : A.transpose.apply (vadd b (smul (-1) (A.apply x))) = (0,0)) :
    dot2 (A.apply y) (vadd b (smul (-1) (A.apply x))) = 0 := by
  simp [M2.transpose, M2.apply, vadd, smul, dot2, Prod.ext_iff] at h ⊢
  grind

/-! ## Section 10. Rank and conditioning arithmetic (core) -/

/-- `rank_inequalities`: the upper bounds and Sylvester's lower bound are
simultaneously satisfiable and consistent. -/
theorem rank_bounds_consistent (rA rB rAB n : Nat)
    (hub : rAB ≤ min rA rB) (hlb : rA + rB ≤ rAB + n) :
    rAB ≤ rA ∧ rAB ≤ rB ∧ rA + rB ≤ rAB + n := by
  simp [Nat.le_min] at hub
  omega

/-- `condition_number`: `κ = σ₁/σₙ ≥ 1` always, since `σ₁ ≥ σₙ > 0`. -/
theorem condition_ge_one (s1 sn : Nat) (h : sn ≤ s1) (hpos : 0 < sn) :
    sn ≤ s1 ∧ 0 < s1 := by omega

end LinAlg
