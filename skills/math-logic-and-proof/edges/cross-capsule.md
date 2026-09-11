# Cross-capsule relations — `grounds` (NOT a `tsort` edge in either capsule)

The foundations are genuinely circular. This capsule and
`math-sets-functions-cardinality` each take, as a primitive, something the other
develops. Recorded here; linearised in neither.

| this capsule | direction | other capsule | meaning |
|---|---|---|---|
| `naive_collection` (primitive here) | ← grounded by | `axiom_extensionality` … `axiom_choice` (the ZF(C) axioms) | the "set of" talk in every semantic node is what ZFC axiomatises |
| `proposition_logic` (primitive there) | ← grounded by | `nd_rules_propositional`, `derivability`, `soundness_prop`, `post_completeness_theorem` | that capsule's propositional-logic primitive is this subgraph |
| `predicate_logic` (primitive there) | ← grounded by | `quantifier_syntax`, `nd_rules_quantifier`, `tarski_satisfaction`, `godel_completeness_theorem` | ditto for quantifiers |
| `quantifier_negation` (primitive there) | ← grounded by | `quantifier_negation` (this capsule) | same law, developed here |
| `quantifier_order` (primitive there) | ← grounded by | `quantifier_order` (this capsule) | same convention, developed here |
| `proof_methods` (primitive there) | ← grounded by | the `proof_methods` area (14 nodes here) | contradiction / cases / induction / counterexample developed here |

## Discharge status

- **Upward (this → set capsule) — done, Release 0.2.**
  `math-sets-functions-cardinality` Release 0.1 listed `proposition_logic`,
  `predicate_logic`, `quantifier_negation`, `quantifier_order`, `proof_methods`
  as primitives "cited to a future `math-logic-and-proof`". Its Release 0.2
  records the discharge in its own
  [`edges/cross-capsule.md`](../math-sets-functions-cardinality/edges/cross-capsule.md)
  and promotes `proposition_logic`/`predicate_logic` `active` → `reviewed`.
  **No `tsort` edge was added** — the two capsules' primitives are mutually
  grounding (this capsule's `naive_collection` is grounded by the set
  capsule's ZFC axioms, downward, below), so a `requires` edge either way would
  misencode a genuine foundational circularity as a false acyclic dependency.
  The discharge is a documented metadata link, consistent with this file's own
  rule that neither `tsort` graph contains the loop.
- **Downward (set capsule → this).** `naive_collection` stays primitive here.
  Every semantic node (`structure`, `assignment`, `tarski_satisfaction`,
  `model`, `soundness_*`, Henkin, `godel_completeness_theorem`,
  `compactness_*`, `lowenheim_skolem_*`) carries `metatheory: naive_collections`
  and a `requires naive_collection` edge. The purely syntactic/proof-theoretic
  subgraph (roots `symbol`, `string`, `finite_sequence`, `inductive_definition`,
  `metatheoretic_induction` through `derivability`, `deduction_theorem`,
  `consistency`) never touches it.

**Neither capsule's `tsort` graph contains this loop.** The circularity is the
honest state of the foundations, recorded, not hidden.
