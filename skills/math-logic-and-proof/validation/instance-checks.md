# Instance checks — index (generated from results/*.yaml)

Which concrete check backs each headline node. Kernel-checked cores and
`decide` instances live in `validation/proof-checks.lean` (see
`proof-checks.md` for the genuine-vs-instance split); numerical worksheets
in `validation/instance-checks.bc`. `cited` / `partial` = established in the
literature or downstream of a cited result, not fully re-checked here.


## wff_unique_readability

- **lean_status:** `core` — validation/proof-checks.lean -- Wff as an inductive type makes this the injectivity + no-confusion of the constructors (rfl-level); the string-grammar version is cited.
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## de_morgan_prop

- **lean_status:** `core` — validation/proof-checks.lean -- not_or_iff (intuitionistic, term mode); not_and_iff uses Classical.em. decide on all 4 rows.
- **bc:** `validation/instance-checks.bc` (numeric worksheet)

## functional_completeness

- **lean_status:** `core` — validation/proof-checks.lean -- constructive: the wff is built from the table. instance checks: reconstruct xor, majority-of-3, the 16 binary functions.
- **bc:** `validation/instance-checks.bc` (numeric worksheet)

## deduction_theorem

- **lean_status:** `core` — validation/proof-checks.lean -- induction over the Deriv_H inductive predicate.
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## nd_hilbert_equivalence

- **lean_status:** `core` — validation/proof-checks.lean §5-5b -- Deriv (ND fragment) and H (a classical Hilbert calculus matching it rule for rule: K, S, MP, the three conj schemas, ex falso, and the classical reductio axiom (neg p -> bot) -> p) as separate inductive predicates over Wff. `deriv_iff_H : Deriv Γ φ ↔ H Γ φ` proved GENUINELY, both directions by induction: H_of_deriv (the ->I case IS the deduction theorem; conj/botE/RAA cases one H.mp each), deriv_of_H (each axiom schema a short impI-built Deriv theorem). Deriv.weaken (context monotone under subset) also proved. `#print axioms deriv_iff_H` -> propext only.
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## soundness_prop

- **lean_status:** `core` — validation/proof-checks.lean -- induction over Deriv_ND; each rule case discharged by the truth_value_recursion clauses.
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## post_completeness_theorem

- **lean_status:** `cited` — validation/proof-checks.lean proves soundness (the converse) outright; the completeness direction is CITED ([enderton_logic_2e] §2.2, [vandalen_5e] §1.5). A plain-Lean proof for a countable atom set is feasible (Lindenbaum by Nat-recursion + LEM, truth lemma by structural_induction_wff, no Mathlib) and is the next Lean target -- see proof-checks.md and BACKLOG.
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## compactness_prop

- **lean_status:** `cited` — inherits the status of propositional completeness (cited). validation/proof-checks.lean proves soundness; the Koenig-lemma route is the more Lean-tractable one for a countable atom set and is not yet formalised.
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## free_for

- **well-definedness:** recursion on the structure of phi: atomic -> true; connective -> componentwise; quantifier Qy psi -> (x not free in Qy psi) or (y not in var(t) and free_for(t,x,psi)). Total and decidable.
- **bc:** `validation/instance-checks.bc` (numeric worksheet)

## tarski_satisfaction

- **well-definedness:** the recursion is well-founded on formula_complexity; the quantifier clause reduces satisfaction of forall x psi to satisfaction of the STRICTLY SIMPLER psi under a modified assignment. Total.
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## substitution_lemma_semantic

- **lean_status:** `partial` — validation/proof-checks.lean -- named-variable version with the FreeFor predicate; the quantifier case is the substantive one. Mathlib cites its de Bruijn analogue.
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## quantifier_negation

- **lean_status:** `core` — validation/proof-checks.lean -- three intuitionistic directions term-mode; not_forall_iff = Classical.not_forall; decide instance on a 3-element domain.
- **bc:** `validation/instance-checks.bc` (numeric worksheet)

## quantifier_order

- **lean_status:** `core` — validation/proof-checks.lean -- forall_exists_of_exists_forall (one line); the non-implication by a decide-checked finite countermodel.
- **bc:** `validation/instance-checks.bc` (numeric worksheet)

## soundness_fol

- **lean_status:** `partial` — validation/proof-checks.lean -- proved outright once satisfaction and the substitution lemma are in place; the eigenvariable case is the bookkeeping-heavy one.
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## godel_completeness_theorem

- **lean_status:** `partial` — validation/proof-checks.lean + proof-checks.md#godel_completeness_theorem -- Formula/Term/Structure/satisfaction as inductive types; soundness outright; Henkin construction carried as far as feasible, connected to Mathlib FirstOrder.Language completeness where present (mathlib_cited), every sorry / informal step logged. Epistemic label NOT upgraded past the kernel.
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## compactness_fol

- **lean_status:** `partial` — validation/proof-checks.lean -- inherits the status of the completeness proof.
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## lowenheim_skolem_down

- **lean_status:** `partial` — validation/proof-checks.lean -- follows once the term model is shown countable; inherits completeness status.
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## induction_equivalence

- **lean_status:** `core` — validation/proof-checks.lean -- all three implications over Nat, plain Lean (Nat.strong_induction_on / a well-ordering lemma), no Mathlib needed.
- **bc:** `validation/instance-checks.bc` (numeric worksheet)

## undecidability_fol_validity

- **lean_status:** `none`
- **bc:** `validation/instance-checks.bc` (numeric worksheet)

## godel_incompleteness_first

- **lean_status:** `none` — cited: [smith_godel_2e]. (Mathlib has a formalisation of the first incompleteness theorem; not connected in this capsule -- out of scope.)
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## godel_incompleteness_second

- **lean_status:** `none` — cited: [smith_godel_2e] part IV.
- **bc:** (no numeric worksheet; the type check and specialization cases apply)
