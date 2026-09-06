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

- **Upward (this → set capsule).** `math-sets-functions-cardinality` Release 0.1
  lists `proposition_logic`, `predicate_logic`, `quantifier_negation`,
  `quantifier_order`, `proof_methods` as primitives "cited to a future
  `math-logic-and-proof`". This capsule supplies them. A Release 0.2 of the set
  capsule can replace those five primitive nodes with `requires` edges into the
  nodes named above.
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
