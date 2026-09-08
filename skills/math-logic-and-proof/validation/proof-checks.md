# proof-checks.md — what the kernel verified vs. what is cited

`lean validation/proof-checks.lean` — **exit 0, no `sorry`**, Lean 4.33.1, **no
Mathlib**. `#print axioms` at the end of the file confirms:

| theorem | axioms | reading |
|---|---|---|
| `soundness` (`soundness_prop`) | `propext` | genuine universal proof |
| `deduction` (`deduction_theorem`) | `propext` | genuine universal proof |
| `deriv_iff_H` (`nd_hilbert_equivalence`) | `propext` | genuine universal proof — the full `Deriv ↔ H` round trip, both directions by induction |
| `Deriv.weaken` (weakening for `nd_derivation`) | `propext` | genuine universal proof |
| `strong_of_weak` (`induction_equivalence`) | *(none)* | genuine, fully constructive |
| `not_forall_iff` (`quantifier_negation`, classical dir.) | `propext, Classical.choice, Quot.sound` | **correctly** classical — this is the `needs_LEM` law |

## Kernel-verified (genuine, universal)

| capsule node | Lean name | notes |
|---|---|---|
| `wff_unique_readability` | `Wff.conj_injective`, `Wff.conj_ne_disj` | constructor injectivity / no-confusion = unique readability for the inductive type; the string-grammar parenthesis-counting proof is cited |
| `double_negation` | `dne`, `dni` | `dni` (`p → ¬¬p`) constructive; `dne` classical — the split |
| `de_morgan_prop` | `not_or_iff`, `not_and_iff`, `cap_not_and_of_disj` | `not_or_iff` + `cap_not_and_of_disj` intuitionistic; `not_and_iff`'s `→` uses `Classical.em` |
| `implication_as_disjunction` | `impl_iff_or` | `→` needs LEM, `←` free |
| `contraposition` | `contrapose_weak`, `contrapose_iff` | half free, full needs DNE |
| `exportation` | `exportation` | fully intuitionistic; the Curry–Howard currying `(A×B→C)≃(A→B→C)` |
| `distributivity_prop` | `distrib_and_or` | `∧` over `∨`, both directions, term-mode |
| `commutativity_associativity_idempotence` | `and_comm'`, `and_assoc'`, `and_idem'` | term-mode, no axioms |
| `absorption` | `absorption_and` | `p ∧ (p ∨ q) ↔ p`, term-mode |
| `biconditional_as_conjunction` | `biconditional_as_conj` | `(p ↔ q) ↔ (p→q) ∧ (q→p)` |
| `truth_value_recursion` | `Wff.eval` | the recursion, one clause per constructor; `eval v (conj p q) = … := rfl` |
| `satisfaction` | `Wff.eval v φ = true` | used throughout; `Entails` is built on it |
| `truth_assignment` | `v : Nat → Bool` | the model of the whole `⊨` side |
| `semantic_consequence` | `Entails` | `∀ v, (∀ q ∈ Γ, eval v q) → eval v p`; `soundness` concludes it |
| `logical_equivalence` | `Wff.Equiv` + `equiv_refl/symm/trans` | equivalence relation on `Wff` |
| `tautology` / `contradiction_unsat` | `Wff.Taut` / `Wff.Contradiction` + `taut_iff_neg_contra` | duals |
| `satisfiability` | `Wff.Sat` + `sat_iff_not_contra` | `←` via `Classical.byContradiction` |
| `substitution_of_equivalents` | `equiv_neg`, `equiv_conj`, `equiv_disj`, `equiv_impl` | connective-congruence steps; full theorem is their structural closure |
| `functional_completeness` | `binary_dnf`, `not_from_nand`, `and_from_nand`, `or_from_nand` | every binary `f` equals its `{¬,∧,∨}` DNF; NAND generates `{¬,∧,∨}` |
| `dnf_from_truth_table` | `binary_dnf` | `f a b = ⋁` (minterm of each `T`-row), all 4 cases by `cases … <;> simp` |
| `binary_boolean_functions_16` | `binary_dnf` + `bc` count | all 16 have a `{¬,∧,∨}` form; `2^(2^2)=16` |
| `sheffer_stroke` | `nand`, `not/and/or_from_nand` | `{↑}` generates `{¬,∧,∨}` |
| `wff_syntax` / `wff_unique_readability` | `inductive Wff`, `conj_injective`, `conj_ne_disj` | constructors injective + disjoint (no-confusion) |
| `structural_induction_wff` / `recursion_on_wff` | `induction φ` / `def eval` | the recursor of the `Wff` inductive type |
| `true_false_constants` | `Wff.fls` + `Deriv.falseE` | ⊥ constructor + ⊥E |
| `soundness_prop` | `soundness` | induction on `Deriv` (ax, →I, →E, ∧I, ∧E, ⊥E, RAA); `raa`/`falseE` cases handled by `Bool.noConfusion` |
| `deduction_theorem` | `deduction` | induction on the Hilbert derivation `H`; the `mp` case uses the `S` schema, every axiom case is `K`-prefixed |
| `nd_rules_propositional` | `Deriv` constructors | `ax`, `impI` (→I / discharge), `impE` (→E), `andI`, `andEl`, `andEr`, `falseE` (⊥E), `raa` — a representative fragment |
| `nd_derivation` / `assumption_discharge` | `Deriv` / `Deriv.impI` | `impI : Deriv (p :: Γ) q → Deriv Γ (p → q)` is discharge; `Deriv.weaken` (context monotone under `⊆`) proved by induction |
| `modus_ponens` | `Deriv.impE`, `H.mp` | |
| `raa_rule` | `Deriv.raa` + `dne` | classical; `#print axioms` shows `Classical.choice` on `dne` |
| `explosion_ex_falso` | `Deriv.falseE`, `Deriv.explosion` | ⊥E constructor |
| `hilbert_system_prop` / `hilbert_derivation` | `inductive H` (`k`, `s`, `mp`, `andI`, `andEl`, `andEr`, `efq`, `raaAx`), `H.self` | classical calculus matching the `Deriv` fragment rule for rule (`¬` primitive, enters only via `raaAx : (¬p → ⊥) → p`) |
| `derived_rules` | `Deriv.cut`, `Deriv.and_comm`, `Deriv.explosion` | short compositions of primitive rules |
| `nd_hilbert_equivalence` | `deriv_iff_H` (`= ⟨H_of_deriv, deriv_of_H⟩`), `deduction`, `Deriv.weaken` | **genuine, universal.** `H_of_deriv`: induction on `Deriv`, the `impI` case *is* the deduction theorem, the `∧`/`⊥E`/`RAA` cases use the matching `H` schemas. `deriv_of_H`: induction on `H`, each axiom schema a short `impI`-built `Deriv` theorem. `#print axioms deriv_iff_H` → `propext` only |
| `quantifier_negation` | `not_exists_iff`, `cap_not_forall_of_exists_not`, `not_forall_iff` | 3 of 4 directions intuitionistic; `not_forall_iff` = `Classical.not_forall` |
| `quantifier_order` | `forall_exists_of_exists_forall` | `∃∀ → ∀∃` genuine |
| `induction_equivalence` | `strong_of_weak`, `well_ordering` | weak → strong → well-ordering, over `Nat`, plain Lean |

## Instance checks (`decide` / concrete model — necessary, not sufficient)

| node | Lean name | what it shows |
|---|---|---|
| `binary_boolean_functions_16` | `xor_nf`, `iff_nf`, `imp_nf` | three connectives in `{¬,∧,∨}` normal form |
| `quantifier_order` (converse fails) | `exists_forall_not_converse` | `r x y := x ≠ y` on `Bool`: `∀x∃y` holds, `∃y∀x` fails, by `decide` |
| `free_for` | `free_for_matters` | `∀x. ∃y. y = x+1` true, capture form `∃y. y = y+1` false — `∀E` unsound without the side condition |

## Cited only — NOT formalised here (see `sources/bibliography.md`)

`post_completeness_theorem`, `godel_completeness_theorem` (the Henkin
construction), `compactness_prop` / `compactness_fol`, `soundness_fol` (stated;
the propositional core `soundness` stands), `lowenheim_skolem_down` /
`lowenheim_skolem_up`, `substitution_lemma_semantic` (the mechanism is shown by
`free_for_matters`; the universal lemma is cited), and **every boundary node**
(`undecidability_fol_validity`, `godel_incompleteness_first` / `_second`,
`tarski_undefinability`, `halting_problem`, `church_turing_thesis`).

`lean_status` in the result YAMLs records this per node. A Mathlib-enabled
release would connect `godel_completeness_theorem` to
`Mathlib.ModelTheory` (`FirstOrder.Language` + its completeness development)
and upgrade the status to `mathlib_cited`. The epistemic label is **never**
upgraded past what the kernel checks.

## `bc validation/instance-checks.bc`

Runs clean (`scale = 0` throughout). Enumerates the 8-row truth table of the
hypothetical syllogism (tautology confirmed); the De Morgan truth-table
agreement with the constructive-grade note; NAND reconstruction of ¬/∧/∨ and the
count `2^(2^2)=16`; `∀x∃y` vs `∃y∀x` on `y ≡ x+1 (mod 4)` over a 4-element
domain (`1` vs `0`); the `free_for` capture bug (`phi(3)=1`, captured `=0`);
the structural shape of a negated ε–δ statement; and least-element search as
well-ordering (`least n with n² > 30` is `6`).
