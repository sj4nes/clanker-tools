# Type / well-formedness checks (generated from results/*.yaml)

One `## <node>` section per headline result: the statement's type-check
status, the well-formedness note (what must hold for the statement to even
make sense), and each symbol's type. A passing type check is **necessary,**
**not sufficient** — a well-typed statement can still be false on a missing
hypothesis, a strictness, a constructive-grade slip, or a quantifier order.
The remaining 109 nodes carry this on their `nodes/<id>.md` detail page.


## wff_unique_readability

- **status:** `well_formed`
- **note:** the statement is about strings that are wffs; the parenthesisation convention (conventions.md, wff_syntax) is what makes it true. Drop the parentheses and it is false.
- **symbols:**
  - `phi` — a well-formed formula (`Wff`)
  - `psi, chi` — immediate subformulas (`Wff`)
  - `op` — the principal connective (`one of and, or, imp, iff`)
- **hypotheses:** fully_parenthesised_or_precedence_fixed
- **constructive grade:** `intuitionistic`

## de_morgan_prop

- **status:** `well_formed`
- **symbols:**
  - `p, q` — wffs / propositional atoms (`Wff`)
- **hypotheses:** (none / unconditional within scope)
- **constructive grade:** `needs_LEM` — the "and" law splits: not(p or q) <-> (not p and not q) is INTUITIONISTIC; not(p and q) <- (not p or not q) is INTUITIONISTIC; but not(p and q) -> (not p or not q) is NOT intuitionistically valid (it implies weak excluded middle). Node graded needs_LEM for its strongest component.

## functional_completeness

- **status:** `well_formed`
- **symbols:**
  - `f` — an n-ary Boolean function (`BooleanFunction`)
  - `n` — arity (`natural number`)
  - `phi` — a wff computing f (`Wff`)
- **hypotheses:** (none / unconditional within scope)
- **constructive grade:** `intuitionistic` — the DNF construction is fully explicit; classical logic not needed to BUILD phi, only its correctness proof uses case analysis on Bool (decidable, fine intuitionistically).

## deduction_theorem

- **status:** `well_formed`
- **note:** propositional -- no eigenvariable / free_for conditions. First-order version needs "phi closed or the generalisation is on a variable not free in phi".
- **symbols:**
  - `Gamma` — a set of wffs (`Context`)
  - `phi, psi` — wffs (`Wff`)
- **hypotheses:** (none / unconditional within scope)
- **constructive grade:** `intuitionistic` — holds for the intuitionistic Hilbert system (axioms 1 and 2 suffice; the classical axiom is not used).

## nd_hilbert_equivalence

- **status:** `well_formed`
- **note:** both sides over the same Wff type and same finite Gamma; propositional, so no free_for obligation in the deduction-theorem step.
- **symbols:**
  - `Gamma` — a finite set of wffs (`Context`)
  - `phi` — a wff (`Wff`)
- **hypotheses:** same_connective_set_both_calculi, classical_rule_present_on_both_or_neither
- **constructive grade:** `needs_DNE` — as shipped both calculi are classical (ND has raa_rule; Hilbert has the contraposition axiom), so the equivalence is needs_DNE. The intuitionistic fragments (drop RAA / the classical axiom) coincide intuitionistically -- recorded, and it is what lets each downstream law be graded from either calculus.

## soundness_prop

- **status:** `well_formed`
- **symbols:**
  - `Gamma` — a set of wffs (`Context`)
  - `phi` — a wff (`Wff`)
- **hypotheses:** rules_are_truth_preserving
- **constructive grade:** `needs_DNE` — the RAA rule case needs double-negation elimination in the metatheory (matching the classical object rule). A soundness proof for the intuitionistic fragment is fully constructive.

## post_completeness_theorem

- **status:** `well_formed`
- **symbols:**
  - `Gamma` — a set of wffs (possibly infinite) (`Context`)
  - `phi` — a wff (`Wff`)
- **hypotheses:** classical_calculus
- **constructive grade:** `needs_full_classical` — Lindenbaum decides each wff in or out (LEM at every stage). For a countable atom set this is LEM + metatheoretic_induction, NO choice. For an uncountable atom set it needs Zorn / an ultrafilter -- recorded. The truth lemma not/or clauses use completeness of Delta.

## compactness_prop

- **status:** `well_formed`
- **symbols:**
  - `Gamma` — a (possibly infinite) set of wffs (`Context`)
  - `Gamma0` — a finite subset (`Context`)
- **hypotheses:** finite_satisfiability
- **constructive grade:** `needs_full_classical` — countable atom set: needs only what post_completeness_theorem needs (LEM + metatheoretic_induction, or Koenig's lemma / weak Koenig). Uncountable atom set: equivalent to the Boolean prime ideal theorem (a weak choice principle, strictly weaker than full AC).

## free_for

- **status:** `well_formed`
- **note:** this node IS the type check for every substitution-under-a-binder statement. It is defined by recursion on phi (recursion_on_wff), independently of the substitution operation itself (see edges/cycles.md section 1).
- **symbols:**
  - `t` — a term (`Term`)
  - `x` — the variable being substituted for (`Var`)
  - `phi` — a first-order formula (`Wff`)
- **hypotheses:** (none / unconditional within scope)
- **constructive grade:** `intuitionistic`

## tarski_satisfaction

- **status:** `well_formed`
- **note:** metatheory: naive_collections -- depends on naive_collection (the domain A and the quantification "for every a in A"). Recursion on phi is licensed by wff_unique_readability (recursion_on_wff). s must be defined on FV(phi); coincidence_lemma says only those matter.
- **symbols:**
  - `A` — a structure with domain A (`Structure`)
  - `phi` — a first-order formula (`Wff`)
  - `s` — a variable assignment (`Var -> A`)
  - `a` — a domain element (`element of A`)
- **hypotheses:** nonempty_domain
- **constructive grade:** `intuitionistic` — the DEFINITION is intuitionistic. Deciding satisfaction in an infinite structure is not effective (the forall-clause quantifies over A), but that is a decidability matter, not a constructivity-of-the-definition matter.

## substitution_lemma_semantic

- **status:** `well_formed`
- **note:** the free_for(t,x,phi) hypothesis is the entire type-safety content -- without it the two sides genuinely differ (see counterexample). Proof is by structural_induction_wff and needs coincidence_lemma for the quantifier case.
- **symbols:**
  - `A` — a structure (`Structure`)
  - `phi` — a formula (`Wff`)
  - `t` — a term (`Term`)
  - `s` — an assignment (`Var -> A`)
- **hypotheses:** t_free_for_x_in_phi
- **constructive grade:** `intuitionistic`

## quantifier_negation

- **status:** `well_formed`
- **note:** both sides are first_order_wff; x binds the same occurrences on each side; no substitution, so no free_for obligation. Stated for formulas (free vars allowed), evaluated under an assignment.
- **symbols:**
  - `phi` — a first-order formula (`Wff`)
  - `x` — an object variable (`Var`)
- **hypotheses:** nonempty_domain
- **constructive grade:** `needs_LEM` — SPLIT. Intuitionistic: not exists x phi <-> forall x not phi (both directions); exists x not phi -> not forall x phi. NEEDS LEM: not forall x phi -> exists x not phi. Node graded needs_LEM for its strongest component. Mirrors de_morgan_prop.

## quantifier_order

- **status:** `well_formed`
- **note:** x and y must be DISTINCT and neither captured; this is a notation_convention node (conventions.md) because the whole capsule depends on never silently swapping the order.
- **symbols:**
  - `phi` — a formula with x (`Wff`)
  - `x, y` — distinct object variables (`Var`)
- **hypotheses:** distinct_variables
- **constructive grade:** `intuitionistic` — the valid direction is intuitionistic. Note: extracting the uniform y in the invalid direction, when it DID hold, would be a choice-flavoured move -- but the point here is that it does not hold.

## soundness_fol

- **status:** `well_formed`
- **note:** metatheory: naive_collections. The delicate cases are forall-E / exists-I (need substitution_lemma_semantic, hence free_for) and the eigenvariable rules (need coincidence_lemma + the eigenvariable_condition).
- **symbols:**
  - `Gamma` — a set of first-order formulas (`Theory`)
  - `phi` — a first-order formula (`Wff`)
- **hypotheses:** rules_truth_preserving, eigenvariable_condition_enforced
- **constructive grade:** `needs_DNE` — the RAA / classical-rule case needs DNE in the metatheory. The core quantifier-rule cases are constructive.

## godel_completeness_theorem

- **status:** `well_formed`
- **note:** metatheory: naive_collections (quantifies over "all models"). The Henkin axioms need each witness constant free for x -- automatic for constants, but checked; alpha_equivalence keeps nested substitutions capture-free.
- **symbols:**
  - `Gamma` — a set of sentences of a language L (`Theory`)
  - `phi` — an L-sentence (`Wff`)
  - `M` — the term model produced (`Structure`)
- **hypotheses:** first_order, classical_logic, equality_is_identity
- **constructive grade:** `needs_full_classical`

## compactness_fol

- **status:** `well_formed`
- **symbols:**
  - `Gamma` — a set of sentences (`Theory`)
  - `Gamma0` — a finite subset (`Theory`)
- **hypotheses:** finite_satisfiability
- **constructive grade:** `needs_full_classical`

## lowenheim_skolem_down

- **status:** `well_formed`
- **note:** metatheory: naive_collections; "countable" is |L| <= aleph_0 and |M| <= aleph_0 (cardinality talk imported from the set capsule as naive_collection).
- **symbols:**
  - `L` — a first-order language (`signature`)
  - `Gamma` — a satisfiable set of L-sentences (`Theory`)
  - `M` — the countable model (`Structure`)
- **hypotheses:** countable_language, satisfiable_theory
- **constructive grade:** `needs_full_classical`

## induction_equivalence

- **status:** `well_formed`
- **note:** stated in the metatheory (metatheoretic_induction supplies weak induction as primitive). The equivalence is a metatheorem about which principle to take as the axiom -- all give the same theorems.
- **symbols:**
  - `N` — the metatheoretic natural numbers (`N (meta)`)
  - `P` — an arbitrary predicate on N (`N -> Prop (meta)`)
- **hypotheses:** naturals_with_zero_successor_and_order, successor_injective_and_no_predecessor_of_zero
- **constructive grade:** `needs_DNE` — weak <-> strong is intuitionistic. The well-ordering principle for arbitrary predicates is classically equivalent to them but its "find the least element" content uses excluded middle (decidability of P at each step). For DECIDABLE P all three are intuitionistically equivalent.

## undecidability_fol_validity

- **status:** `well_formed`
- **note:** "algorithm" / "decidable" via church_turing_thesis (informal primitive decidability). The claim is about the set of valid sentences of a sufficiently rich language.
- **symbols:**
  - `phi` — a first-order sentence in a language with at least one binary relation symbol (`Wff`)
- **hypotheses:** language_expressive_enough, church_turing_thesis
- **constructive grade:** `n/a`

## godel_incompleteness_first

- **status:** `well_formed`
- **note:** a schema over theories T. Each hypothesis is a predicate on T: consistency (consistency_fol), decidable axiom set (decidability / church_turing_thesis), interpretability of Q (a provability condition).
- **symbols:**
  - `T` — a first-order theory (`Theory`)
  - `G_T` — the Goedel sentence (`Wff`)
  - `Q` — Robinson arithmetic (`Theory`)
- **hypotheses:** T_consistent, T_recursively_axiomatised, T_interprets_Q
- **constructive grade:** `n/a` — the theorem and its usual proof are effective/constructive (G_T is explicitly constructed); "constructive_grade" (intuitionistic/LEM) does not apply to a boundary node.

## godel_incompleteness_second

- **status:** `well_formed`
- **note:** schema over T. Needs T to prove the Hilbert-Bernays-Loeb derivability conditions (a stronger arithmetic hypothesis than the first theorem -- roughly PA, not just Q).
- **symbols:**
  - `T` — a first-order theory (`Theory`)
  - `Con(T)` — the sentence not Prov_T(quote (0=1)), a Pi_1 formula (`Wff`)
- **hypotheses:** T_consistent, T_recursively_axiomatised, T_proves_HBL_derivability_conditions
- **constructive grade:** `n/a`
