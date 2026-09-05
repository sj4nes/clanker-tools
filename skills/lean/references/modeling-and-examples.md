# Modeling and worked examples

## Worked examples

### Prototype an identity, then promote it

```lean
import Mathlib

example (a b : Nat) : a + b = b + a := by
  exact Nat.add_comm a b
```

### Sum of the first n odd naturals equals n squared

Informal claim: for every natural number `n`, the sum of the first `n` odd naturals equals `n^2`. Numeric domain: `Nat` (nonnegativity is genuine). Prototype boundary cases as examples before committing:

```lean
example : (Finset.range 0).sum (fun k => 2 * k + 1) = 0 ^ 2 := by norm_num
example : (Finset.range 3).sum (fun k => 2 * k + 1) = 3 ^ 2 := by norm_num
```

Then state and prove by induction on `n` (or search Mathlib first — `Finset.sum_range_succ` plus `ring`/`omega` on the successor step).

### `List.length_append` — induction aligned with recursive structure

```lean
theorem length_append {α : Type} (xs ys : List α) :
    (xs ++ ys).length = xs.length + ys.length := by
  induction xs with
  | nil => simp
  | cons x xs ih => simp [ih, Nat.add_right_comm]
```

Induction is the canonical method here because `++` recurses on its first argument. (With Mathlib imported, a bare `simp [ih]` closes the `cons` case; in plain Lean the successor step leaves an arithmetic goal, hence `Nat.add_right_comm` — or finish it with `omega`.) Do not reach for induction when a goal merely mentions a `List`.

### `debit_nonnegative` — surface the essential requirement

Definitions first:

```lean
def ValidAmount (amount : Int) : Prop := 0 ≤ amount
def CanDebit (balance amount : Int) : Prop := ValidAmount amount ∧ amount ≤ balance
def Debit (balance amount : Int) : Int := balance - amount
```

Theorem — the statement is the specification; review it before polishing the proof:

```lean
theorem debit_nonnegative
    {balance amount : Int}
    (h_balance : 0 ≤ balance)
    (h_can_debit : CanDebit balance amount) :
    0 ≤ Debit balance amount := by
  obtain ⟨_, h_le⟩ := h_can_debit
  have h_sub : 0 ≤ balance - amount := Int.sub_nonneg.mpr h_le
  exact h_sub
```

`linarith` (Mathlib) or `omega` would also close it, but the `have` makes `amount ≤ balance` visible as the fact that matters. With Mathlib imported the lemma is the general `sub_nonneg`; in plain Lean use `Int.sub_nonneg` — searching for the right name is step 4 of the workflow.

### Counterexample: refuting a false universal

```lean
example : ¬ (∀ n : Nat, n + 1 = n) := by
  intro h
  have h0 := h 0
  norm_num at h0
```

Use this pattern to challenge a proposed specification before formalizing its "positive" form.

## Testing theorem statements

Lean can prove a theorem that is logically valid but not what was intended. Challenge the specification:

- For a proposed universal theorem, prove representative boundary cases as `example`s (`n = 0`, `n = 1`, empty list, max boundary).
- For claims you suspect are false, try to construct a counterexample as above.
- For definitions, test representative values with `#eval targetFunction 0` / `#eval targetFunction 10` — a debugging aid only, for executable definitions; it proves nothing.
- Where property-based or implementation tests exist, use them to generate candidate conjectures and edge cases, then formalize the precise property in Lean.

## Modeling stateful systems

Recommended architecture — define the state, its well-formedness, one transition, then reachability, then safety by induction.

```lean
structure State where
  balance  : AccountId → Int
  reserved : AccountId → Int

def WellFormed (s : State) : Prop :=
  ∀ a, 0 ≤ s.reserved a ∧ s.reserved a ≤ s.balance a

def Reserve (a : AccountId) (amount : Int) (s s' : State) : Prop :=
  0 ≤ amount ∧
  amount ≤ s.balance a - s.reserved a ∧
  s' = { balance := s.balance,
         reserved := fun account =>
           if account = a then s.reserved account + amount
           else s.reserved account }
```

Preservation lemma for a single transition:

```lean
theorem reserve_preserves_wellFormed
    {a amount s s'}
    (h_wf : WellFormed s)
    (h_reserve : Reserve a amount s s') :
    WellFormed s' := by
  obtain ⟨h_amount, h_avail, h_eq⟩ := h_reserve
  subst h_eq
  intro account
  by_cases h : account = a
  · subst h
    constructor
    · have := (h_wf account).1; simp; linarith
    · simp [h]; linarith [(h_wf account).1, (h_wf account).2]
  · simpa [h] using h_wf account
```

(The exact tactic script depends on Mathlib version and the `AccountId` decidable-equality instance; the shape is: split on the updated key, use extensional reasoning for the function update, and linear arithmetic for the bounds.)

Reachability and safety by induction:

```lean
inductive Reachable : State → Prop where
  | initial : Reachable initialState
  | step {s s'} : Reachable s → Step s s' → Reachable s'

theorem reachable_wellFormed : ∀ s, Reachable s → WellFormed s := by
  intro s h_reachable
  induction h_reachable with
  | initial => exact initial_wellFormed
  | step h_reachable h_step ih => exact step_preserves_wellFormed ih h_step
```

This is the reusable pattern:

```text
initial state is safe  ∧  each transition preserves safety  ⇒  every reachable state is safe
```

**Scope limits.** A safe sequential transition system does not establish concurrency correctness. If interleavings, atomicity, message delay, crash recovery, or external nondeterminism matter, model them explicitly or use a complementary model-checking tool (see the `tla-checker` skill). Do not claim the production storage operation is atomic, or that implementation code refines this model, unless that correspondence is established separately.

## Factoring proofs into semantic lemmas

When a monolithic preservation proof obscures the argument, factor at meaningful boundaries:

```lean
lemma reserve_does_not_change_balance ...
lemma reserve_increases_reserved ...
lemma reserve_preserves_reserved_bounds ...
theorem reserve_preserves_wellFormed ...   -- combines the three
```

Each lemma name states its semantic content. Do not split trivial one-line steps into dozens of micro-lemmas.
