/-
Release 0.1 — machine-checked cores of the set/function/cardinality theory.
Run:  lean validation/proof-checks.lean   (exit 0, no `sorry`, no errors)

SCOPE.  No Mathlib.  The ZF axioms, Zorn's lemma, the ordinal spine,
Cantor-Schroeder-Bernstein, and the infinite-cardinal arithmetic are not
formalised here -- they rest on the cited sources.  What Lean checks:

  * GENUINE UNIVERSAL proofs, in plain Lean 4, of the finitary cores that the
    rest of mathematics leans on directly: the PREIMAGE ALGEBRA (f^-1 commutes
    with arbitrary union / intersection / complement), the image laws, the fact
    that composites of injections are injections, the equivalence-class
    identity [x] = [y] <-> x ~ y, classical quantifier negation, and CANTOR'S
    DIAGONAL THEOREM (no surjection X -> P(X)).
  * one INSTANCE check (`decide`) of the pigeonhole principle, with the function
    spelled out (Fintype is Mathlib, so `forall f : Fin 5 -> Fin 4` is not
    decidable as written).

Sets here are predicates `X -> Prop`; `preim f B := fun x => B (f x)`.
-/

universe u v
variable {X : Type u} {Y : Type v} {I : Type}

def preim (f : X → Y) (B : Y → Prop) : X → Prop := fun x => B (f x)
def img   (f : X → Y) (A : X → Prop) : Y → Prop := fun y => ∃ x, A x ∧ f x = y

/-! ## 1. Preimage algebra — behind `preimage_algebra`.  GENUINE, universal.
    f^-1 commutes with an arbitrary union, an arbitrary intersection, and
    complement.  Each is definitional once sets are predicates. -/
theorem preim_iUnion (f : X → Y) (B : I → Y → Prop) :
    preim f (fun y => ∃ i, B i y) = fun x => ∃ i, preim f (B i) x := rfl
theorem preim_iInter (f : X → Y) (B : I → Y → Prop) :
    preim f (fun y => ∀ i, B i y) = fun x => ∀ i, preim f (B i) x := rfl
theorem preim_compl (f : X → Y) (B : Y → Prop) :
    preim f (fun y => ¬ B y) = fun x => ¬ preim f B x := rfl

/-! ## 2. Image laws — behind `image_algebra`.  GENUINE.
    f[A ∪ B] = f[A] ∪ f[B] exactly; f[A ∩ B] ⊆ f[A] ∩ f[B] only. -/
theorem img_union (f : X → Y) (A B : X → Prop) :
    img f (fun x => A x ∨ B x) = fun y => img f A y ∨ img f B y := by
  funext y; apply propext; constructor
  · rintro ⟨x, hx | hx, rfl⟩
    · exact Or.inl ⟨x, hx, rfl⟩
    · exact Or.inr ⟨x, hx, rfl⟩
  · rintro (⟨x, hx, rfl⟩ | ⟨x, hx, rfl⟩)
    · exact ⟨x, Or.inl hx, rfl⟩
    · exact ⟨x, Or.inr hx, rfl⟩
theorem img_inter_sub (f : X → Y) (A B : X → Prop) (y : Y) :
    img f (fun x => A x ∧ B x) y → img f A y ∧ img f B y := by
  rintro ⟨x, ⟨ha, hb⟩, rfl⟩; exact ⟨⟨x, ha, rfl⟩, ⟨x, hb, rfl⟩⟩

/-! ## 3. Composition preserves injectivity / surjectivity — behind
    `composition_preserves_properties`.  GENUINE. -/
def Inj (f : X → Y) : Prop := ∀ a b, f a = f b → a = b
def Surj (f : X → Y) : Prop := ∀ y, ∃ x, f x = y
theorem comp_inj {g : Y → X} {f : X → Y} (hg : Inj g) (hf : Inj f) : Inj (g ∘ f) :=
  fun a b h => hf a b (hg (f a) (f b) h)
theorem comp_surj {g : Y → X} {f : X → Y} (hg : Surj g) (hf : Surj f) : Surj (g ∘ f) :=
  fun z => let ⟨y, hy⟩ := hg z; let ⟨x, hx⟩ := hf y; ⟨x, by simp [Function.comp, hx, hy]⟩

/-! ## 4. Cantor's diagonal theorem — behind `cantor_theorem`, `cantor_diagonal`.
    GENUINE, no Mathlib.  No `f : X → (X → Prop)` takes the value
    `x ↦ ¬ f x x`, so `f` is not surjective. -/
theorem cantor (f : X → X → Prop) (a : X) : f a ≠ (fun x => ¬ f x x) := by
  intro h; exact iff_not_self (iff_of_eq (congrFun h a))

/-! ## 5. Classical quantifier negation — behind `quantifier_negation`,
    `de_morgan_laws`.  `not_forall` is classical; `not_exists` is constructive. -/
theorem not_forall_iff {p : I → Prop} : (¬ ∀ i, p i) ↔ ∃ i, ¬ p i := Classical.not_forall
theorem not_exists_iff {p : I → Prop} : (¬ ∃ i, p i) ↔ ∀ i, ¬ p i := not_exists

/-! ## 6. Equivalence classes — behind `equivalence_partition_correspondence`,
    `quotient_set`.  GENUINE.  [x] = [y]  ⟺  x ∼ y. -/
def cls (r : X → X → Prop) (x : X) : X → Prop := fun z => r x z
theorem cls_eq_iff (r : X → X → Prop)
    (hr : ∀ x, r x x) (hs : ∀ x y, r x y → r y x) (ht : ∀ x y z, r x y → r y z → r x z)
    (x y : X) : cls r x = cls r y ↔ r x y := by
  constructor
  · intro h
    have hx : (r x x) = (r y x) := congrFun h x
    exact hs y x (hx ▸ hr x)
  · intro hxy; funext z; apply propext
    exact ⟨fun hxz => ht y x z (hs x y hxy) hxz, fun hyz => ht x y z hxy hyz⟩

/-! ## 7. Pigeonhole — behind `pigeonhole_principle`.  INSTANCE: five values in
    `Fin 4` must repeat (the function is spelled out as `(a,b,c,d,e)` because
    `Fintype (Fin 5 → Fin 4)` is Mathlib). -/
theorem pigeonhole_5_into_4 : ∀ a b c d e : Fin 4,
    a = b ∨ a = c ∨ a = d ∨ a = e ∨ b = c ∨ b = d ∨ b = e ∨ c = d ∨ c = e ∨ d = e := by
  decide
