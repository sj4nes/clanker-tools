# Cross-capsule relations — `grounds` (NOT a `tsort` edge in either capsule)

Mirrors [`math-logic-and-proof/edges/cross-capsule.md`](../../math-logic-and-proof/edges/cross-capsule.md)
from this capsule's side. The foundations are genuinely circular: this capsule
takes propositional/predicate logic as primitive to state the ZF(C) axioms,
while `math-logic-and-proof` takes `naive_collection` (informal "set of" talk)
as primitive to state its semantic nodes (`structure`, `tarski_satisfaction`,
`model`, …). Recorded here; linearised in neither `tsort` graph.

| node here (stays `primitive` for this capsule's own `tsort`) | discharged by (`math-logic-and-proof`) | meaning |
|---|---|---|
| `proposition_logic` | `nd_rules_propositional`, `derivability`, `soundness_prop`, `post_completeness_theorem` | that capsule develops what this one assumes |
| `predicate_logic` | `quantifier_syntax`, `nd_rules_quantifier`, `tarski_satisfaction`, `godel_completeness_theorem` | ditto for quantifiers |
| `quantifier_negation` | `quantifier_negation` (same law, developed there) | `¬∀x P ⟺ ∃x ¬P` |
| `quantifier_order` | `quantifier_order` (same convention, developed there) | `∀∃` strictly stronger than `∃∀` |
| `proof_methods` | the `proof_methods` area (14 nodes there: contradiction / cases / induction / counterexample) | classical proof strategies |

## Release 0.2 (this release)

Discharges the backlog item from `math-logic-and-proof` Release 0.1: the five
primitive nodes above are no longer "cited to a future `math-logic-and-proof`"
— that capsule exists, is built, and is the named discharge. Concretely:

- `proposition_logic` and `predicate_logic` promoted `active` → `reviewed` in
  `nodes/nodes.tsv`, with a `discharged by` note naming the grounding nodes.
- `quantifier_negation`, `quantifier_order`, `proof_methods` gain the same
  `discharged by` note (they were already `reviewed`).
- **No `tsort` edge is added.** A cross-capsule `requires` edge would need both
  endpoints in one registry, and the two capsules' primitives are mutually
  grounding (see above) — encoding it as a real edge in either graph would be
  a modeling error, not a discharge. This table is the discharge; it is
  metadata, read by a person or agent tracing the foundational stance, not by
  either capsule's `tsort` build.
- `scope.md` and `SKILL.md` updated to point here instead of describing the
  logic floor as "cited to a future" capsule.

**Neither capsule's `tsort` graph contains this loop**, before or after this
release. The circularity is the honest state of the foundations, recorded,
not hidden.
