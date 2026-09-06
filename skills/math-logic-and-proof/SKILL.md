---
name: math-logic-and-proof
description: >-
  Logic and proof as a curated, dependency-ordered knowledge capsule — the
  deepest floor under the set / number-system / analysis stack. Propositional
  logic (syntax, truth-functional semantics, the equivalence catalogue, normal
  forms, functional completeness); natural deduction AND a parallel Hilbert
  system with the equivalence lemma and the deduction theorem; first-order
  syntax (terms, substitution, the free-for condition), Tarski satisfaction, and
  structures; the quantifier laws (quantifier negation, quantifier order,
  prenex form); the metatheorems — soundness, Lindenbaum, Post and Godel
  completeness via the Henkin term model, compactness, Lowenheim-Skolem; a
  fifteen-node block of proof methods (contradiction, contrapositive, cases,
  weak / strong / structural induction, well-ordering, counterexample); and
  stated-not-proved boundary nodes (Godel incompleteness, undecidability of
  first-order validity, the halting problem, Tarski undefinability). A 130-node
  acyclic graph. Every logical law and proof method carries a CONSTRUCTIVE GRADE
  (intuitionistic / needs_LEM / needs_DNE / needs_full_classical). Use when you
  need the logical foundation a proof rests on, the prerequisite chain for a
  metatheorem, or to know exactly which classical principle a law uses. Built
  with the math-theorem-tree method; discharges the logic primitives of
  math-sets-functions-cardinality.
version: 0.1.0
author: Simon Janes
tags: [mathematics, logic, proof-theory, model-theory, foundations, natural-deduction, completeness, compactness, incompleteness, dependencies, knowledge-capsule, lean]
---

# Logic and Proof — Release 0.1

A knowledge capsule built with the
[`math-theorem-tree`](../math-theorem-tree/SKILL.md) method: a **130-node
directed acyclic graph** — propositional logic, natural deduction and a Hilbert
system, first-order syntax and semantics, the quantifier laws, the
soundness / completeness / compactness / Löwenheim–Skolem metatheorems, a
proof-methods block, and stated boundary nodes for incompleteness and
undecidability — linearised with `tsort`. It is the **deepest floor** under
[`math-sets-functions-cardinality`](../math-sets-functions-cardinality/SKILL.md):
the five primitives that capsule cites (`proposition_logic`, `predicate_logic`,
`quantifier_negation`, `quantifier_order`, `proof_methods`) are developed here.

## Scope

**Read [`scope.md`](scope.md) first.** In brief: propositional syntax with
unique readability and structural recursion; truth-functional semantics, the
equivalence catalogue, NNF/CNF/DNF, functional completeness and the Sheffer
stroke; **natural deduction** as the spine and a **Hilbert system** in parallel,
with `nd_hilbert_equivalence` and the **deduction theorem**; first-order terms,
formulas, free/bound variables, **substitution and the "free for" side
condition**, prenex form; **structures**, variable assignments, **Tarski
satisfaction**; the quantifier laws — **quantifier negation**, quantifier
distribution, **quantifier order** (`∀∃` vs `∃∀`); **soundness**,
**Lindenbaum's lemma**, **Post** and **Gödel completeness** via the **Henkin
term model**, **compactness**, **downward Löwenheim–Skolem**; a 15-node
**proof-methods** block including **weak / strong / structural induction** and
**well-ordering**, proved equivalent; and **stated-not-proved** boundary nodes:
**Gödel I & II**, **undecidability of first-order validity**, the **halting
problem**, **Tarski undefinability**, the **Church–Turing thesis** (`heuristic`).

**Excluded:** proofs of the boundary nodes (arithmetisation, the fixed-point
lemma); sequent-calculus proof theory and cut elimination; model theory proper
(types, saturation, ultraproducts, categoricity); higher-order and non-classical
*calculi*; set theory (the capsule above); computability as a subject.
Foundational stance and the seven designed-out cycles:
[`conventions.md`](conventions.md). Well-formedness rules (unique readability,
the free-for condition, eigenvariable conditions, nonempty domains):
[`objects.md`](objects.md).

## The syntax ↔ collections loop

Model theory needs "sets"; set theory needs logic. This capsule keeps the
**syntactic/proof-theoretic subgraph self-contained** — roots `symbol`,
`string`, `finite_sequence`, `inductive_definition`, `metatheoretic_induction`,
through `derivability`, `deduction_theorem`, `consistency`, with **no
`naive_collection` edge** — and tags every **semantic** node
`metatheory: naive_collections` with a `requires naive_collection` edge.
`naive_collection` is primitive here and discharged **from above** by
`math-sets-functions-cardinality`'s ZF axioms, exactly as that capsule's
`proposition_logic` primitive is discharged from here. The bidirectional
`grounds` relation is recorded in [`edges/cross-capsule.md`](edges/cross-capsule.md)
and linearised in neither capsule's `tsort` graph.

## How to use this capsule

1. **Find the result** — [`nodes/nodes.tsv`](nodes/nodes.tsv) (full registry);
   [`indexes/`](indexes/) once built.
2. **Read its entry** — [`nodes/<id>.md`](nodes/) (**every one of the 130 nodes
   has a detail page**); [`results/<id>.yaml`](results/) for the 21 headline
   nodes carries the same content as a structured record.
3. **Check what it needs** — [`indexes/tsort-order.txt`](indexes/tsort-order.txt)
   and [`indexes/reverse-dependencies.txt`](indexes/reverse-dependencies.txt);
   prerequisite paths once built.
4. **Check the constructive grade** — every logical-law and proof-method entry
   carries `constructive_grade`: `intuitionistic`, `needs_LEM`, `needs_DNE`, or
   `needs_full_classical`.
5. **Check the Lean status** — `lean_status` per node: `core` (genuine plain-Lean
   proof), `mathlib_cited`, `partial` (recorded gaps), `stated`, `instance`,
   `none`.

## The spine

```
symbol/string/finite_sequence/inductive_definition/metatheoretic_induction
  -> wff_syntax -> wff_unique_readability -> structural_induction_wff / recursion_on_wff
  -> truth_assignment -> satisfaction -> tautology / semantic_consequence
  -> the equivalence catalogue -> NNF/CNF/DNF -> functional_completeness
  -> nd_derivation / nd_rules_propositional  ||  hilbert_system_prop
  -> deduction_theorem -> nd_hilbert_equivalence -> derivability
  -> consistency -> soundness_prop
  -> maximal_consistent_set -> lindenbaum_lemma_prop -> truth_lemma_prop
  -> post_completeness_theorem -> compactness_prop
  -- FOL --
  signature -> term_syntax -> first_order_wff -> free_bound_variables
  -> substitution / free_for -> prenex_normal_form
  -> [naive_collection] structure -> assignment -> term_evaluation
  -> tarski_satisfaction -> model / validity / semantic_consequence_fol
  -> quantifier_negation / quantifier_order
  -> nd_rules_quantifier (eigenvariable_condition) -> derivability_fol -> soundness_fol
  -> henkin_constants -> henkin_theory -> lindenbaum_lemma_fol -> term_model
  -> truth_lemma_fol -> godel_completeness_theorem
  -> compactness_fol -> lowenheim_skolem_down -> skolem_paradox / non_categoricity
  -- boundary --
  decidability / church_turing_thesis -> undecidability_fol_validity / halting_problem
  -> godel_incompleteness_first -> godel_incompleteness_second / tarski_undefinability
```

## Build and verify

```sh
sh build/all.sh                        # graph -> tsort -> views -> lean -> bc -> yaml check
sh build/build-tree.sh                 # 130 nodes, 312 edges, acyclic (stderr-checked), 7 roots
lean validation/proof-checks.lean      # exit 0, no sorry
bc -q -l validation/instance-checks.bc
```

**Lean (4.33, no Mathlib, exit 0, no `sorry`).** Genuine universal proofs on
`propext` alone: `soundness_prop` (induction on a natural-deduction calculus),
`deduction_theorem` (induction on a Hilbert calculus), `induction_equivalence`
(weak → strong → well-ordering, zero axioms). The equivalence catalogue with the
**constructive-grade split** made explicit — intuitionistic directions in term
mode, `needs_LEM` / `needs_DNE` directions flagged with `Classical`. Instance
checks (`decide` / concrete model): NAND completeness, `∃y∀x` non-converse,
the `free_for` capture bug. **Cited, not formalised:** `post_completeness_theorem`,
`godel_completeness_theorem` (the Henkin construction), `compactness_*`,
`lowenheim_skolem_*`, and every boundary node — the split is tracked per node in
[`validation/proof-checks.md`](validation/proof-checks.md) and never upgraded
past the kernel. A Mathlib release would connect completeness to
`Mathlib.ModelTheory`.

**`bc`** — truth-table enumeration (hypothetical syllogism), the De Morgan
grade split, NAND reconstruction + the `2^(2^2)=16` count, `∀x∃y` vs `∃y∀x` on
`y ≡ x+1 (mod 4)`, the capture bug, well-ordering as least-element search.

## Status (Release 0.1, draft)

Complete: [`scope.md`](scope.md), [`conventions.md`](conventions.md),
[`objects.md`](objects.md), [`notation.md`](notation.md), the 130-node registry
[`nodes/nodes.tsv`](nodes/nodes.tsv), the evidence-backed dependency graph
[`edges/dependencies.plan`](edges/dependencies.plan) (acyclic,
stderr-checked), [`edges/cycles.md`](edges/cycles.md),
[`edges/relations.tsv`](edges/relations.tsv),
[`edges/cross-capsule.md`](edges/cross-capsule.md),
[`sources/bibliography.md`](sources/bibliography.md), **21 headline result
YAMLs**, **a detail page for all 130 nodes** (`nodes/*.md`; prerequisites
machine-checked against the graph),
`validation/proof-checks.lean` (+`.md`),
`validation/instance-checks.bc`, and the generated
[`indexes/`](indexes/) (status, constructive-grade, counterexample, hypothesis,
prerequisite-paths). `sh build/all.sh` is green end to end.
To do: a Mathlib-backed completeness formalisation; the symbol/KWIC index via
`ptx`; promote more `draft` nodes to `reviewed`.
