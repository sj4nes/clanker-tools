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

- **lean_status:** `cited` — proof-checks.lean has no FreeFor predicate or satisfaction relation -- this node's universal statement is cited, not kernel-checked; corrected from a prior partial that named a predicate that was never formalised. What IS checked, by free_for_matters (see validation/proof-checks.md#free_for), is one concrete instance of the underlying capture-bug mechanism this lemma's hypothesis guards against -- attributed to the free_for node (lean_status: core, an instance check, not this node's universal lemma). Cited: [enderton_logic_2e] Lemma 24B, [chiswell_hodges] Lemma 3.4.3; Mathlib's de Bruijn representation sidesteps the lemma entirely (capture is structurally impossible there).
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## quantifier_negation

- **lean_status:** `core` — validation/proof-checks.lean -- three intuitionistic directions term-mode; not_forall_iff = Classical.not_forall; decide instance on a 3-element domain.
- **bc:** `validation/instance-checks.bc` (numeric worksheet)

## quantifier_order

- **lean_status:** `core` — validation/proof-checks.lean -- forall_exists_of_exists_forall (one line); the non-implication by a decide-checked finite countermodel.
- **bc:** `validation/instance-checks.bc` (numeric worksheet)

## soundness_fol

- **lean_status:** `cited` — proof-checks.lean has no first-order satisfaction/Structure formalisation, so none of this node's own content (the forall-E / exists-I / eigenvariable cases) is kernel-checked -- corrected from a prior partial that described an unexecuted plan. What IS checked is the propositional core (soundness_prop, genuinely proved on propext) this node reduces to on the propositional fragment; the FOL-specific quantifier and equality cases remain cited ([enderton_logic_2e] Thm 24C, [vandalen_5e] Thm 2.6.1). See validation/proof-checks.md's "Cited only" list.
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## godel_completeness_theorem

- **lean_status:** `cited` — validation/proof-checks.lean is explicitly, by its own header comment, "not the place for the Henkin construction" -- no Formula/Term/Structure/satisfaction inductive types exist in it. Corrected from a prior partial that described an aspirational plan never executed (the plan text is preserved below as a Release 0.2 target, not a current claim). Cited: [enderton_logic_2e] Thm 25.14, [vandalen_5e] Thm 2.5.3. A Mathlib-enabled release would connect to Mathlib.ModelTheory (FirstOrder.Language) and its completeness development, upgrading to mathlib_cited -- see BACKLOG.md and validation/proof-checks.md's "Cited only" section.
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## compactness_fol

- **lean_status:** `cited` — inherits the status of godel_completeness_theorem, corrected there from partial to cited (proof-checks.lean has no first-order content to inherit from). Cited: [enderton_logic_2e] Thm 25.16, [vandalen_5e] Thm 2.5.7. Mathlib has Theory.isSatisfiable_iff_isFinitelySatisfiable, not connected here.
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## lowenheim_skolem_down

- **lean_status:** `cited` — inherits the status of godel_completeness_theorem, corrected there from partial to cited -- the term-model countability argument this node needs is not formalised either. Cited: [enderton_logic_2e] Thm 25.19. Mathlib has exists_elementarySubstructure_card_eq, not connected here.
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
