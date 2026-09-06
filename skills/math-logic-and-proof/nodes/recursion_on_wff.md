# recursion_on_wff

## Type
theorem  (epistemic status: `proved_theorem` / recursion principle;
`constructive_grade: intuitionistic`)

## Statement
A function `F` on wffs is **uniquely determined** by giving:
- its value on each atom and on `⊥` (base data), and
- for each connective, a rule computing `F(¬φ)` from `F(φ)`, and `F(φ ∘ ψ)` from
  `F(φ)` and `F(ψ)`.

Formally: for any target type `A`, base map `g : Atom → A`, `a_⊥ ∈ A`, and
operations `f_¬ : A → A`, `f_∘ : A → A → A`, there is a **unique** `F : Wff → A`
with `F(p) = g(p)`, `F(⊥) = a_⊥`, `F(¬φ) = f_¬(F φ)`, `F(φ ∘ ψ) = f_∘(F φ)(F ψ)`.

## Symbols
- `F`: the defined function; `A`: its codomain.

## Prerequisites (tsort edges into this node)
`structural_induction_wff`, `wff_unique_readability`.

## Content
The recursion theorem for the `wff_syntax` inductive definition. **Existence**
of `F` is the recursion; **uniqueness** is `structural_induction_wff` (two
functions agreeing on the base data and commuting with the operations agree
everywhere). `wff_unique_readability` is essential: without it "the immediate
subformulas of `φ`" is ambiguous and `F(φ)` is not determined.

Every semantic function is an instance:
- `truth_value_recursion` — `A = Bool`, `g = v`, `f_¬ = not`, `f_∧ = and`, …;
- `subformula` — `A = Finset Wff`;
- `formula_complexity` — `A = ℕ`;
- the NNF / CNF / DNF conversions — `A = Wff`;
- first-order: `term_evaluation`, `tarski_satisfaction` (with quantifier
  operations `A → A` for `∀`, `∃`).

## Constructive grade
`intuitionistic` — it is the eliminator of the inductive type; the resulting `F`
is computable when the base data and operations are.

## Lean status
`lean_status: core`. In Lean this **is** the definitional mechanism:
`def eval (v : Nat → Bool) : Wff → Bool | atom n => v n | fls => false | neg p
=> ! eval v p | …` in `validation/proof-checks.lean` is a `recursion_on_wff`
instance, accepted because `Wff` is `inductive` (the recursor `Wff.rec` is
generated). `example : eval v (conj p q) = (eval v p && eval v q) := rfl`
exhibits the defining equation.

## Type / well-formedness check
`well_formed` **iff** exactly one clause per constructor and each recursive call
is on an immediate subformula (strict `formula_complexity` decrease). Two
clauses for one connective, or a clause referring to a non-subformula, breaks
well-definedness. For **mutually** inductive syntax (terms ⇄ formulas) the
recursion is mutual.

## Specialization / boundary cases
- **primitive recursion** on `ℕ` is the `wff_syntax`-free analogue (constructors
  `0`, `succ`).
- **iteration** (no dependence on the subformula, only on `F` of it): the common
  case.
- **course-of-values recursion** (`F(φ)` depends on `F` of *all* smaller
  formulas): reduce to this via `formula_complexity` + `strong_induction`.
- defining a function into a **quotient** (e.g. `Wff → Wff/≡`): must check the
  operations respect `≡` (`substitution_of_equivalents`) — the
  well-definedness-on-a-quotient obligation.

## Hypothesis-dropped counterexamples
- **without `wff_unique_readability`**: `F(p ∧ q ∨ r)` is ambiguous — two
  subformula decompositions give two values.
- **two clauses for `∧`**: `F` overdetermined / inconsistent.
- **recursive call on a non-subformula** (`F(φ) := f(F(φ[⊤/p]))`): not
  structurally decreasing — may not terminate.
- **coinductive syntax**: recursion is replaced by corecursion; this theorem
  does not apply.

## Common misuse
Defining `⟦·⟧_v` / substitution / a proof-rule action "by recursion on `φ`"
without `wff_unique_readability`; missing a connective clause; a recursive call
that is not on a subformula; forgetting the quotient well-definedness check when
the codomain is `Wff/≡`.

## Related nodes (non-prerequisite)
- `dual_of`: `structural_induction_wff` (recursion = existence, induction =
  uniqueness).
- `licensed_by`: `wff_unique_readability`.
- `instances`: `truth_value_recursion`, `subformula`, `formula_complexity`,
  NNF/CNF/DNF, `term_evaluation`, `tarski_satisfaction`.
- `analogue`: primitive recursion on `ℕ`; the recursion theorem for any
  `inductive_definition`.

## Sources
[enderton_logic_2e] §1.4 (the recursion theorem for wffs); [vandalen_5e] §1.1;
[chiswell_hodges] ch. 2.
