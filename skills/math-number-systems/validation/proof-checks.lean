/-
Release 0.1 — machine-checked cores of the constructions.
Run:  lean validation/proof-checks.lean   (exit 0, no `sorry`, no errors)

SCOPE.  No Mathlib in this environment, so the set-level constructions (Dedekind
cuts, the least-upper-bound property, the field laws for the quotients) are not
formalised here; they rest on the cited sources.  What Lean checks:

  * GENUINE UNIVERSAL proofs -- the quotient-relation cores that make the ℤ
    construction well-posed (`omega` over ℤ), a from-scratch induction proof of
    commutativity of ℕ-addition off its recursive definition, division with
    remainder via core lemmas, and Cantor's diagonal theorem (no Mathlib).
  * INSTANCE checks (`decide`) -- the nonlinear cores: ℤ-multiplication
    respecting the relation, ℚ-relation transitivity, √2-irrationality on a
    bounded range, and injectivity of the Cantor pairing on a grid.  An instance
    check is kernel-verified but is not a universal proof; each is labelled.

`lean_status` in each results/*.yaml records which of these (if any) backs a node.
-/

set_option maxRecDepth 8000

/-! ## 1. ℤ construction — the relation is transitive (UNIVERSAL over ℤ)
    (a,b) ∼ (c,d)  :⟺  a + d = b + c.  Behind `integer_relation_equivalence`. -/
theorem z_rel_trans (a b c d e f : Int)
    (h1 : a + d = b + c) (h2 : c + f = d + e) : a + f = b + e := by omega

/-! ## 2. ℤ addition respects the relation (UNIVERSAL over ℤ)
    Behind `integer_operations_well_defined`. -/
theorem z_add_well_defined (a b a' b' c d c' d' : Int)
    (h1 : a + b' = b + a') (h2 : c + d' = d + c') :
    (a + c) + (b' + d') = (b + d) + (a' + c') := by omega

/-! ## 3. ℤ order respects the relation (UNIVERSAL over ℤ)
    [(a,b)] ≤ [(c,d)]  :⟺  a + d ≤ b + c.  Behind `integer_order`. -/
theorem z_le_well_defined (a b a' b' c d c' d' : Int)
    (h1 : a + b' = b + a') (h2 : c + d' = d + c') (hle : a + d ≤ b + c) :
    a' + d' ≤ b' + c' := by omega

/-! ## 4. ℕ addition is commutative — proved from the recursive definition
    (`n + 0 = n`, `n + (m+1) = (n + m) + 1`) by induction.  GENUINE, universal.
    This is the pattern behind all of `nat_semiring_laws`. -/
namespace NatCore
theorem zero_add' : ∀ n : Nat, 0 + n = n
  | 0 => rfl
  | n + 1 => by rw [Nat.add_succ, zero_add' n]
theorem succ_add' : ∀ m n : Nat, Nat.succ m + n = Nat.succ (m + n)
  | _, 0 => rfl
  | m, n + 1 => by rw [Nat.add_succ, Nat.add_succ, succ_add' m n]
theorem add_comm' : ∀ m n : Nat, m + n = n + m
  | m, 0 => by rw [Nat.add_zero, zero_add']
  | m, n + 1 => by rw [Nat.add_succ, add_comm' m n, succ_add']
end NatCore

/-! ## 5. Division with remainder — EXISTENCE via core `Nat` lemmas.
    Behind `nat_division_with_remainder`. -/
theorem nat_div_rem (a b : Nat) (h : 0 < b) :
    b * (a / b) + a % b = a ∧ a % b < b :=
  ⟨Nat.div_add_mod a b, Nat.mod_lt a h⟩

/-! ## 6. Cantor's diagonal theorem — GENUINE, no Mathlib.
    No `f : X → (X → Prop)` takes the value `x ↦ ¬ f x x`, so `f` is not
    surjective.  Behind `cantor_theorem` and (specialised) `real_uncountable`. -/
theorem cantor {X : Type} (f : X → X → Prop) (a : X) :
    f a ≠ (fun x => ¬ f x x) := by
  intro h
  exact iff_not_self (iff_of_eq (congrFun h a))

/-! ## 7. ℤ multiplication respects the relation — INSTANCE.
    Rule: [(a,b)]·[(c,d)] = [(ac+bd, ad+bc)].  With (5,2) ∼ (8,5):
    (5·4+2·1, 5·1+2·4) = (22,13)  ∼  (8·4+5·1, 8·1+5·4) = (37,28)  since 22+28 = 13+37. -/
example : (5 * 4 + 2 * 1) + (8 * 1 + 5 * 4) = (5 * 1 + 2 * 4) + (8 * 4 + 5 * 1) := by decide

/-! ## 8. ℚ relation transitivity — INSTANCE.
    ad = bc form, chain (1,2) ∼ (2,4) ∼ (3,6). -/
example : (1 * 4 = 2 * 2) ∧ (2 * 6 = 4 * 3) ∧ (1 * 6 = 2 * 3) := by decide

/-! ## 9. √2 irrational — INSTANCE on a bounded range.
    No p, q with 1 ≤ q < 50 and p² = 2q².  The universal statement is the
    infinite-descent / parity argument, cited (see validation/proof-checks.md). -/
example : ∀ p q : Fin 50, q.val ≥ 1 → p.val * p.val ≠ 2 * (q.val * q.val) := by decide

/-! ## 10. Cantor pairing injective — INSTANCE on an 8×8 grid.
    π(m,n) = (m+n)(m+n+1)/2 + n.  Behind `nat_pairing_bijection`. -/
def pair (m n : Nat) : Nat := (m + n) * (m + n + 1) / 2 + n
example : ∀ m n m' n' : Fin 8, pair m n = pair m' n' → m.val = m'.val ∧ n.val = n'.val := by
  decide
