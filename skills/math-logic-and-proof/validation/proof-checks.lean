/-
Release 0.1 — machine-checked cores of the logic-and-proof capsule.
Run:  lean validation/proof-checks.lean      (exit 0, no `sorry`, no errors)

SCOPE.  No Mathlib.  Lean 4's own `Prop` is intuitionistic natural deduction,
which this file exploits: intuitionistic laws are term-mode proofs, the
classical ones are flagged with `Classical.*`.

WHAT THE KERNEL VERIFIES (genuine + universal, unless marked INSTANCE):

  1. A `Wff` type + `eval`; unique readability = constructor injectivity /
     no-confusion.
  2. The propositional equivalence catalogue with the CONSTRUCTIVE-GRADE split:
     intuitionistic directions term-mode; `needs_LEM` / `needs_DNE` directions
     use `Classical` and say so.
  3. NAND functional completeness (not/and/or from `↑`); XOR / IFF / IMP as
     {not,and,or} normal forms -- INSTANCE.
  4. A natural-deduction calculus `Deriv` and its SOUNDNESS -- genuine, by
     induction on the derivation.
  5. A classical Hilbert calculus `H` matching the `Deriv` fragment rule for
     rule; the DEDUCTION THEOREM -- genuine; `Deriv` WEAKENING -- genuine; and
     the full `Deriv ↔ H` ROUND TRIP (`deriv_iff_H`) -- genuine, both directions
     by induction (`nd_hilbert_equivalence`).
  6. Quantifier negation: the 4-way split (`quantifier_negation`).
  7. Quantifier order: `∃∀ → ∀∃` genuine; converse fails -- INSTANCE countermodel.
  8. The capture bug behind `free_for` -- INSTANCE.
  9. Induction equivalence: weak → strong → well-ordering over `Nat` -- genuine.

ONLY CITED (validation/proof-checks.md, sources/bibliography.md):
  post_completeness_theorem, godel_completeness_theorem, compactness_*,
  lowenheim_skolem_*, and every boundary node.  Plain Lean 4 without Mathlib is
  not the place for the Henkin construction.
-/

/-! ## 1. Propositional syntax -/

inductive Wff where
  | atom : Nat → Wff
  | fls  : Wff
  | neg  : Wff → Wff
  | conj : Wff → Wff → Wff
  | disj : Wff → Wff → Wff
  | impl : Wff → Wff → Wff
  deriving DecidableEq, Repr

namespace Wff

def eval (v : Nat → Bool) : Wff → Bool
  | atom n   => v n
  | fls      => false
  | neg p    => ! eval v p
  | conj p q => eval v p && eval v q
  | disj p q => eval v p || eval v q
  | impl p q => (! eval v p) || eval v q

/-- Unique readability, structural form: constructors injective and disjoint,
    so `eval` and any recursion on `Wff` are well defined -- the point
    `wff_unique_readability` makes for the string grammar. -/
theorem conj_injective {p q p' q' : Wff} (h : conj p q = conj p' q') :
    p = p' ∧ q = q' := by injection h with h1 h2; exact ⟨h1, h2⟩

theorem conj_ne_disj (p q p' q' : Wff) : conj p q ≠ disj p' q' := by
  intro h; injection h

example (v : Nat → Bool) (p q : Wff) :
    eval v (conj p q) = (eval v p && eval v q) := rfl

end Wff

/-! ## 2. Equivalence catalogue with the constructive-grade split -/

/-- `not_exists` shape -- INTUITIONISTIC. -/
theorem not_or_iff {p q : Prop} : (¬ (p ∨ q)) ↔ (¬ p ∧ ¬ q) :=
  ⟨fun h => ⟨fun hp => h (Or.inl hp), fun hq => h (Or.inr hq)⟩,
   fun ⟨hp, hq⟩ h => h.elim hp hq⟩

/-- De Morgan for `∧` -- the `→` direction is `needs_LEM`. -/
theorem not_and_iff {p q : Prop} : (¬ (p ∧ q)) ↔ (¬ p ∨ ¬ q) := by
  constructor
  · intro h
    rcases Classical.em p with hp | hp
    · exact Or.inr (fun hq => h ⟨hp, hq⟩)
    · exact Or.inl hp
  · rintro (hp | hq) ⟨hpp, hqq⟩
    · exact hp hpp
    · exact hq hqq

/-- Converse of De Morgan-∧ on its own -- INTUITIONISTIC. -/
theorem cap_not_and_of_disj {p q : Prop} : (¬ p ∨ ¬ q) → ¬ (p ∧ q) := by
  rintro (hp | hq) ⟨hpp, hqq⟩
  · exact hp hpp
  · exact hq hqq

/-- Double negation elimination -- `needs_DNE`. -/
theorem dne {p : Prop} : ¬ ¬ p → p := fun h => Classical.byContradiction (fun hn => h hn)

/-- `p → ¬¬p` is INTUITIONISTIC. -/
theorem dni {p : Prop} : p → ¬ ¬ p := fun hp hn => hn hp

/-- Implication as disjunction -- `→` needs LEM, `←` intuitionistic. -/
theorem impl_iff_or {p q : Prop} : (p → q) ↔ (¬ p ∨ q) := by
  constructor
  · intro h
    rcases Classical.em p with hp | hp
    · exact Or.inr (h hp)
    · exact Or.inl hp
  · rintro (hp | hq) hpp
    · exact absurd hpp hp
    · exact hq

/-- Contraposition -- half is free, full form needs DNE. -/
theorem contrapose_weak {p q : Prop} : (p → q) → (¬ q → ¬ p) :=
  fun h hnq hp => hnq (h hp)

theorem contrapose_iff {p q : Prop} : (p → q) ↔ (¬ q → ¬ p) :=
  ⟨contrapose_weak, fun h hp => dne (fun hnq => h hnq hp)⟩

/-- Exportation -- fully INTUITIONISTIC. -/
theorem exportation {p q r : Prop} : ((p ∧ q) → r) ↔ (p → q → r) :=
  ⟨fun h hp hq => h ⟨hp, hq⟩, fun h ⟨hp, hq⟩ => h hp hq⟩

/-- Commutativity, associativity, idempotence, absorption, distributivity --
    all INTUITIONISTIC (term-mode, no `Classical`). -/
theorem and_comm' {p q : Prop} : (p ∧ q) ↔ (q ∧ p) :=
  ⟨fun ⟨a, b⟩ => ⟨b, a⟩, fun ⟨a, b⟩ => ⟨b, a⟩⟩
theorem and_assoc' {p q r : Prop} : ((p ∧ q) ∧ r) ↔ (p ∧ (q ∧ r)) :=
  ⟨fun ⟨⟨a, b⟩, c⟩ => ⟨a, b, c⟩, fun ⟨a, b, c⟩ => ⟨⟨a, b⟩, c⟩⟩
theorem and_idem' {p : Prop} : (p ∧ p) ↔ p := ⟨fun ⟨a, _⟩ => a, fun a => ⟨a, a⟩⟩
theorem absorption_and {p q : Prop} : (p ∧ (p ∨ q)) ↔ p :=
  ⟨fun ⟨a, _⟩ => a, fun a => ⟨a, Or.inl a⟩⟩
theorem distrib_and_or {p q r : Prop} : (p ∧ (q ∨ r)) ↔ ((p ∧ q) ∨ (p ∧ r)) :=
  ⟨fun ⟨a, bc⟩ => bc.elim (fun b => Or.inl ⟨a, b⟩) (fun c => Or.inr ⟨a, c⟩),
   fun h => h.elim (fun ⟨a, b⟩ => ⟨a, Or.inl b⟩) (fun ⟨a, c⟩ => ⟨a, Or.inr c⟩)⟩
theorem biconditional_as_conj {p q : Prop} : (p ↔ q) ↔ ((p → q) ∧ (q → p)) :=
  ⟨fun h => ⟨h.mp, h.mpr⟩, fun ⟨a, b⟩ => ⟨a, b⟩⟩

/-! ## 2b. Propositional SEMANTICS as wff-level predicates -- behind
    `logical_equivalence`, `tautology`, `satisfiability`, `contradiction_unsat`,
    `substitution_of_equivalents`.  All GENUINE (structural, term/`simp`). -/

namespace Wff

/-- `a` and `b` have the same value under every assignment. -/
def Equiv (a b : Wff) : Prop := ∀ v, eval v a = eval v b
/-- true under every assignment. -/
def Taut (a : Wff) : Prop := ∀ v, eval v a = true
/-- false under every assignment. -/
def Contradiction (a : Wff) : Prop := ∀ v, eval v a = false
/-- true under at least one assignment. -/
def Sat (a : Wff) : Prop := ∃ v, eval v a = true

theorem equiv_refl (a : Wff) : Equiv a a := fun _ => rfl
theorem equiv_symm {a b : Wff} (h : Equiv a b) : Equiv b a := fun v => (h v).symm
theorem equiv_trans {a b c : Wff} (h1 : Equiv a b) (h2 : Equiv b c) : Equiv a c :=
  fun v => (h1 v).trans (h2 v)

/-- `Taut a  ↔  Contradiction (neg a)` -- tautology / contradiction are duals. -/
theorem taut_iff_neg_contra (a : Wff) : Taut a ↔ Contradiction (neg a) := by
  constructor
  · intro h v; simp [eval, h v]
  · intro h v; have := h v; simp [eval] at this; exact this

/-- `Sat a  ↔  ¬ Contradiction a`. -/
theorem sat_iff_not_contra (a : Wff) : Sat a ↔ ¬ Contradiction a := by
  constructor
  · rintro ⟨v, hv⟩ h; rw [h v] at hv; exact Bool.noConfusion hv
  · intro h
    apply Classical.byContradiction
    intro hns
    apply h
    intro v
    cases hv : eval v a with
    | false => rfl
    | true  => exact absurd ⟨v, hv⟩ hns

/-- SUBSTITUTION OF EQUIVALENTS, connective-congruence form: replacing an
    immediate subformula by an equivalent one preserves `Equiv`.  The full
    statement is the structural-induction closure of these five. -/
theorem equiv_neg {a a' : Wff} (h : Equiv a a') : Equiv (neg a) (neg a') := by
  intro v; simp [eval, h v]
theorem equiv_conj {a a' b b' : Wff} (ha : Equiv a a') (hb : Equiv b b') :
    Equiv (conj a b) (conj a' b') := by intro v; simp [eval, ha v, hb v]
theorem equiv_disj {a a' b b' : Wff} (ha : Equiv a a') (hb : Equiv b b') :
    Equiv (disj a b) (disj a' b') := by intro v; simp [eval, ha v, hb v]
theorem equiv_impl {a a' b b' : Wff} (ha : Equiv a a') (hb : Equiv b b') :
    Equiv (impl a b) (impl a' b') := by intro v; simp [eval, ha v, hb v]

end Wff

/-! ## 3. Functional completeness -/

def nand (a b : Bool) : Bool := ! (a && b)

theorem not_from_nand (a : Bool)     : (! a)     = nand a a := by cases a <;> rfl
theorem and_from_nand (a b : Bool)   : (a && b)  = nand (nand a b) (nand a b) := by
  cases a <;> cases b <;> rfl
theorem or_from_nand  (a b : Bool)   : (a || b)  = nand (nand a a) (nand b b) := by
  cases a <;> cases b <;> rfl

/-- INSTANCE: three of the sixteen binary connectives in {not,and,or} normal form. -/
theorem xor_nf (a b : Bool) : (xor a b) = ((a || b) && ! (a && b)) := by
  cases a <;> cases b <;> rfl
theorem iff_nf (a b : Bool) : (a == b)  = ((a && b) || (! a && ! b)) := by
  cases a <;> cases b <;> rfl
theorem imp_nf (a b : Bool) : ((! a) || b) = (! (a && ! b)) := by
  cases a <;> cases b <;> rfl

/-- DNF FROM THE TRUTH TABLE -- behind `dnf_from_truth_table`, `functional_completeness`.
    EVERY binary Boolean function equals the disjunction, over the rows where it
    is `true`, of the conjunction of matching literals.  Genuine (all 4 cases). -/
theorem binary_dnf (f : Bool → Bool → Bool) (a b : Bool) :
    f a b =
      ( (f true true  && (a && b))
      || (f true false && (a && !b))
      || (f false true && (!a && b))
      || (f false false && (!a && !b)) ) := by
  cases a <;> cases b <;> simp

/-! ## 4. Natural deduction and SOUNDNESS -/

abbrev Ctx := List Wff

/-- A representative fragment of propositional natural deduction:
    assumptions, `→I`/`→E` (`impI` is `assumption_discharge`), `∧I`/`∧E`,
    `⊥E` (`falseE` = `explosion_ex_falso`), and the classical `RAA` (`raa`).
    Enough for `soundness` and the derived rules; the `∨` rules and `¬I` are
    omitted (they add nothing to the soundness argument). -/
inductive Deriv : Ctx → Wff → Prop where
  | ax     {Γ p}   : p ∈ Γ → Deriv Γ p
  | impI   {Γ p q} : Deriv (p :: Γ) q → Deriv Γ (Wff.impl p q)
  | impE   {Γ p q} : Deriv Γ (Wff.impl p q) → Deriv Γ p → Deriv Γ q
  | andI   {Γ p q} : Deriv Γ p → Deriv Γ q → Deriv Γ (Wff.conj p q)
  | andEl  {Γ p q} : Deriv Γ (Wff.conj p q) → Deriv Γ p
  | andEr  {Γ p q} : Deriv Γ (Wff.conj p q) → Deriv Γ q
  | falseE {Γ p}   : Deriv Γ Wff.fls → Deriv Γ p
  | raa    {Γ p}   : Deriv (Wff.neg p :: Γ) Wff.fls → Deriv Γ p

/-- `Γ ⊨ p`. -/
def Entails (Γ : Ctx) (p : Wff) : Prop :=
  ∀ v, (∀ q ∈ Γ, Wff.eval v q = true) → Wff.eval v p = true

private theorem sat_cons {v : Nat → Bool} {p : Wff} {Γ : Ctx}
    (hp : Wff.eval v p = true) (hΓ : ∀ q ∈ Γ, Wff.eval v q = true) :
    ∀ q ∈ p :: Γ, Wff.eval v q = true := by
  intro q hq
  rcases List.mem_cons.1 hq with rfl | hq
  · exact hp
  · exact hΓ q hq

/-- SOUNDNESS (`soundness_prop`).  Genuine, universal, by induction on `Deriv`.
    The `raa` case is where the metatheory turns classical (`Bool` case split). -/
theorem soundness {Γ : Ctx} {p : Wff} (d : Deriv Γ p) : Entails Γ p := by
  induction d with
  | @ax Γ p h => intro v hv; exact hv p h
  | @impI Γ p q _ ih =>
      intro v hv
      show ((! Wff.eval v p) || Wff.eval v q) = true
      cases hp : Wff.eval v p with
      | false => simp
      | true  => have := ih v (sat_cons hp hv); simp [this]
  | @impE Γ p q _ _ ih1 ih2 =>
      intro v hv
      have h1 := ih1 v hv
      have h2 := ih2 v hv
      show Wff.eval v q = true
      have h1' : ((! Wff.eval v p) || Wff.eval v q) = true := h1
      rw [h2] at h1'
      simpa using h1'
  | @andI Γ p q _ _ ih1 ih2 =>
      intro v hv
      show (Wff.eval v p && Wff.eval v q) = true
      simp [ih1 v hv, ih2 v hv]
  | @andEl Γ p q _ ih =>
      intro v hv
      have h : (Wff.eval v p && Wff.eval v q) = true := ih v hv
      cases hp : Wff.eval v p with
      | true  => rfl
      | false => rw [hp] at h; simp at h
  | @andEr Γ p q _ ih =>
      intro v hv
      have h : (Wff.eval v p && Wff.eval v q) = true := ih v hv
      cases hq : Wff.eval v q with
      | true  => rfl
      | false => rw [hq] at h; simp at h
  | @falseE Γ p _ ih =>
      intro v hv
      have hbot := ih v hv          -- eval v fls = true, i.e. false = true
      exact Bool.noConfusion hbot
  | @raa Γ p _ ih =>
      intro v hv
      cases hp : Wff.eval v p with
      | true  => rfl
      | false =>
          have hneg : Wff.eval v (Wff.neg p) = true := by
            show (! Wff.eval v p) = true
            rw [hp]; rfl
          have hbot := ih v (sat_cons hneg hv)
          exact Bool.noConfusion hbot

/-- Derived rules -- behind `derived_rules`.  Admissible in the `Deriv` fragment,
    each a short composition of the primitive rules. -/
theorem Deriv.explosion {Γ : Ctx} {p : Wff} (h : Deriv Γ Wff.fls) : Deriv Γ p :=
  Deriv.falseE h
/-- CUT: `Γ ⊢ p` and `Γ, p ⊢ q` give `Γ ⊢ q` -- `→I` then `→E`. -/
theorem Deriv.cut {Γ : Ctx} {p q : Wff} (h1 : Deriv Γ p) (h2 : Deriv (p :: Γ) q) :
    Deriv Γ q := Deriv.impE (Deriv.impI h2) h1
/-- `∧` commutation as an admissible rule. -/
theorem Deriv.and_comm {Γ : Ctx} {p q : Wff} (h : Deriv Γ (Wff.conj p q)) :
    Deriv Γ (Wff.conj q p) := Deriv.andI (Deriv.andEr h) (Deriv.andEl h)

/-! ## 5. Hilbert calculus, the deduction theorem, and the `Deriv ↔ H` round trip -/

/-- A classical propositional Hilbert calculus matching the `Deriv` fragment
    rule for rule: `K`/`S` + modus ponens for `→`, the three `∧` schemas,
    ex falso (`efq`), and the classical reductio axiom (`raaAx`,
    `(¬p → ⊥) → p`).  `¬` is primitive and — as in `Deriv` — enters only through
    `raaAx`. -/
inductive H : Ctx → Wff → Prop where
  | ax   {Γ p}     : p ∈ Γ → H Γ p
  | k    {Γ p q}   : H Γ (Wff.impl p (Wff.impl q p))
  | s    {Γ p q r} : H Γ (Wff.impl (Wff.impl p (Wff.impl q r))
                                   (Wff.impl (Wff.impl p q) (Wff.impl p r)))
  | mp   {Γ p q}   : H Γ (Wff.impl p q) → H Γ p → H Γ q
  | andI {Γ p q}   : H Γ (Wff.impl p (Wff.impl q (Wff.conj p q)))
  | andEl {Γ p q}  : H Γ (Wff.impl (Wff.conj p q) p)
  | andEr {Γ p q}  : H Γ (Wff.impl (Wff.conj p q) q)
  | efq  {Γ p}     : H Γ (Wff.impl Wff.fls p)
  | raaAx {Γ p}    : H Γ (Wff.impl (Wff.impl (Wff.neg p) Wff.fls) p)

theorem H.self (Γ : Ctx) (p : Wff) : H Γ (Wff.impl p p) :=
  H.mp (H.mp (H.s (p := p) (q := Wff.impl p p) (r := p)) H.k) H.k

/-- DEDUCTION THEOREM (`deduction_theorem`).  Genuine, universal, by induction on
    the Hilbert derivation.  Every axiom case is `K`-prefixed; `mp` uses `S`. -/
theorem deduction {Γ : Ctx} {p q : Wff} (h : H (p :: Γ) q) : H Γ (Wff.impl p q) := by
  induction h with
  | @ax r hr =>
      rcases List.mem_cons.1 hr with rfl | hr
      · exact H.self Γ r
      · exact H.mp H.k (H.ax hr)
  | k => exact H.mp H.k H.k
  | s => exact H.mp H.k H.s
  | @mp r t _ _ ih1 ih2 => exact H.mp (H.mp H.s ih1) ih2
  | andI => exact H.mp H.k H.andI
  | andEl => exact H.mp H.k H.andEl
  | andEr => exact H.mp H.k H.andEr
  | efq => exact H.mp H.k H.efq
  | raaAx => exact H.mp H.k H.raaAx

/-! ### 5b. The round trip (`nd_hilbert_equivalence`) -- genuine, universal. -/

/-- `a :: ·` is monotone under `⊆` (helper for `Deriv.weaken`). -/
private theorem cons_sub_cons {a : Wff} {l₁ l₂ : Ctx} (h : l₁ ⊆ l₂) :
    a :: l₁ ⊆ a :: l₂ := by
  intro x hx
  rcases List.mem_cons.1 hx with rfl | hx
  · exact List.mem_cons.2 (Or.inl rfl)
  · exact List.mem_cons.2 (Or.inr (h hx))

/-- WEAKENING for natural deduction: enlarging the context (in particular adding
    unused hypotheses) preserves derivability.  Genuine, by induction on the
    derivation; `impI` / `raa` push the extra context under the discharged
    assumption via `cons_sub_cons`.  (The `H ⟹ Deriv` axiom translations below
    are built context-generically and do not need this, but it is the structural
    lemma the round trip is classically stated with.) -/
theorem Deriv.weaken {Γ Γ' : Ctx} {p : Wff} (d : Deriv Γ p) : Γ ⊆ Γ' → Deriv Γ' p := by
  induction d generalizing Γ' with
  | @ax Γ p hmem => intro hsub; exact Deriv.ax (hsub hmem)
  | @impI Γ p q _ ih => intro hsub; exact Deriv.impI (ih (cons_sub_cons hsub))
  | @impE Γ p q _ _ ih1 ih2 => intro hsub; exact Deriv.impE (ih1 hsub) (ih2 hsub)
  | @andI Γ p q _ _ ih1 ih2 => intro hsub; exact Deriv.andI (ih1 hsub) (ih2 hsub)
  | @andEl Γ p q _ ih => intro hsub; exact Deriv.andEl (ih hsub)
  | @andEr Γ p q _ ih => intro hsub; exact Deriv.andEr (ih hsub)
  | @falseE Γ p _ ih => intro hsub; exact Deriv.falseE (ih hsub)
  | @raa Γ p _ ih => intro hsub; exact Deriv.raa (ih (cons_sub_cons hsub))

/-- `H ⟹ Deriv`.  Each Hilbert axiom schema is a short natural-deduction theorem
    (built from `impI` + assumptions, generic in `Γ`); `mp` is `→E`.  Genuine,
    by induction on the Hilbert derivation. -/
theorem deriv_of_H {Γ : Ctx} {p : Wff} (h : H Γ p) : Deriv Γ p := by
  induction h with
  | @ax p hmem => exact Deriv.ax hmem
  | k => exact Deriv.impI (Deriv.impI (Deriv.ax (.tail _ (.head _))))
  | s =>
      refine Deriv.impI (Deriv.impI (Deriv.impI ?_))
      exact Deriv.impE
        (Deriv.impE (Deriv.ax (.tail _ (.tail _ (.head _)))) (Deriv.ax (.head _)))
        (Deriv.impE (Deriv.ax (.tail _ (.head _))) (Deriv.ax (.head _)))
  | @mp p q _ _ ih1 ih2 => exact Deriv.impE ih1 ih2
  | andI =>
      exact Deriv.impI (Deriv.impI
        (Deriv.andI (Deriv.ax (.tail _ (.head _))) (Deriv.ax (.head _))))
  | andEl => exact Deriv.impI (Deriv.andEl (Deriv.ax (.head _)))
  | andEr => exact Deriv.impI (Deriv.andEr (Deriv.ax (.head _)))
  | efq => exact Deriv.impI (Deriv.falseE (Deriv.ax (.head _)))
  | raaAx =>
      exact Deriv.impI (Deriv.raa
        (Deriv.impE (Deriv.ax (.tail _ (.head _))) (Deriv.ax (.head _))))

/-- `Deriv ⟹ H`.  Genuine, by induction on the natural-deduction derivation.
    The `impI` (discharge) case is exactly the DEDUCTION THEOREM; the `∧`, `⊥E`
    and `RAA` cases use the matching Hilbert schemas from §5. -/
theorem H_of_deriv {Γ : Ctx} {p : Wff} (d : Deriv Γ p) : H Γ p := by
  induction d with
  | @ax Γ p hmem => exact H.ax hmem
  | @impI Γ p q _ ih => exact deduction ih
  | @impE Γ p q _ _ ih1 ih2 => exact H.mp ih1 ih2
  | @andI Γ p q _ _ ih1 ih2 => exact H.mp (H.mp H.andI ih1) ih2
  | @andEl Γ p q _ ih => exact H.mp H.andEl ih
  | @andEr Γ p q _ ih => exact H.mp H.andEr ih
  | @falseE Γ p _ ih => exact H.mp H.efq ih
  | @raa Γ p _ ih => exact H.mp H.raaAx (deduction ih)


/-- THE ROUND TRIP: the natural-deduction fragment `Deriv` and the Hilbert
    calculus `H` derive exactly the same consequences from the same context --
    so `derivability` is calculus-independent (`nd_hilbert_equivalence`). -/
theorem deriv_iff_H {Γ : Ctx} {p : Wff} : Deriv Γ p ↔ H Γ p :=
  ⟨H_of_deriv, deriv_of_H⟩

/-! ## 6. Quantifier negation -- the 4-way split (`quantifier_negation`) -/

section QN
variable {α : Type} {p : α → Prop}

theorem not_exists_iff : (¬ ∃ x, p x) ↔ (∀ x, ¬ p x) :=            -- intuitionistic
  ⟨fun h x hx => h ⟨x, hx⟩, fun h ⟨x, hx⟩ => h x hx⟩

theorem cap_not_forall_of_exists_not : (∃ x, ¬ p x) → ¬ ∀ x, p x :=  -- intuitionistic
  fun ⟨x, hx⟩ h => hx (h x)

theorem not_forall_iff : (¬ ∀ x, p x) ↔ (∃ x, ¬ p x) :=           -- needs_LEM
  Classical.not_forall

end QN

/-! ## 7. Quantifier order (`quantifier_order`) -/

theorem forall_exists_of_exists_forall {α β : Type} {r : α → β → Prop} :
    (∃ y, ∀ x, r x y) → (∀ x, ∃ y, r x y) :=
  fun ⟨y, hy⟩ x => ⟨y, hy x⟩

/-- Converse FAILS -- INSTANCE countermodel: `r x y := x ≠ y` on `Bool`. -/
theorem exists_forall_not_converse :
    (∀ x : Bool, ∃ y : Bool, x ≠ y) ∧ ¬ (∃ y : Bool, ∀ x : Bool, x ≠ y) := by
  refine ⟨by decide, by decide⟩

/-! ## 8. The capture bug behind `free_for` -- INSTANCE.
    φ(x) := ∃ y, y = x + 1   holds for every x.
    Capturing substitution of `y` for `x` gives  ∃ y, y = y + 1  -- false.
    So `∀E` without the `free_for` side condition is unsound. -/

def phi (x : Nat) : Prop := ∃ y, y = x + 1
def phiCaptured : Prop := ∃ y, y = y + 1

theorem free_for_matters : (∀ x, phi x) ∧ ¬ phiCaptured := by
  refine ⟨fun x => ⟨x + 1, rfl⟩, ?_⟩
  rintro ⟨y, hy⟩
  exact absurd hy (by omega)

/-! ## 9. Induction equivalence (`induction_equivalence`).  Genuine, over `Nat`. -/

/-- weak → strong (course-of-values). -/
theorem strong_of_weak (P : Nat → Prop)
    (step : ∀ n, (∀ k, k < n → P k) → P n) : ∀ n, P n := by
  have aux : ∀ n, ∀ k, k < n → P k := by
    intro n
    induction n with
    | zero => intro k hk; exact absurd hk (Nat.not_lt_zero k)
    | succ n ih =>
        intro k hk
        rcases Nat.lt_succ_iff_lt_or_eq.1 hk with hk | rfl
        · exact ih k hk
        · exact step k ih
  intro n; exact step n (aux n)

/-- strong → well-ordering: a predicate with a witness has a least witness. -/
theorem well_ordering (P : Nat → Prop) (w : Nat) (hw : P w) :
    ∃ m, P m ∧ ∀ k, k < m → ¬ P k := by
  apply Classical.byContradiction
  intro h
  have hdesc : ∀ n, P n → ∃ k, k < n ∧ P k := by
    intro n hn
    apply Classical.byContradiction
    intro hc
    exact h ⟨n, hn, fun k hk hkP => hc ⟨k, hk, hkP⟩⟩
  have hno : ∀ n, ¬ P n := by
    apply strong_of_weak
    intro n ih hn
    rcases hdesc n hn with ⟨k, hk, hkP⟩
    exact ih k hk hkP
  exact hno w hw

#print axioms soundness
#print axioms deduction
#print axioms deriv_iff_H
#print axioms Deriv.weaken
#print axioms strong_of_weak
#print axioms not_forall_iff
