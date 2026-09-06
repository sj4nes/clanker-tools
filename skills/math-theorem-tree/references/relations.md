# Relation types, cycles, bridges, approximation ladders

## Which relations become `tsort` edges

`tsort` needs a directed **acyclic** prerequisite graph. Mathematical knowledge
is richer, so store relation types separately.

| Relationship | Meaning | `tsort` edge? | Stored in |
|---|---|---|---|
| `requires` | necessary prerequisite for correct statement/proof/use | **yes** | `edges/dependencies.plan` |
| `defines` | one node formally introduces another | usually yes | `edges/dependencies.plan` |
| `derives_from` | the stated proof invokes a prior result | **yes** | `edges/dependencies.plan` |
| `valid_when` | hypothesis / regime / convergence condition required for use | **yes** | `edges/dependencies.plan` |
| `generalizes` | one result/definition extends another | no | `edges/relations.tsv` |
| `special_case_of` | constrained instance of a more general result | no (reverse pedagogical pressure) | `edges/relations.tsv` |
| `equivalent_to` | provably equivalent statement or alternative definition | no (point to the equivalence lemma) | `edges/relations.tsv` |
| `strengthens` | same hypotheses, sharper conclusion | no | `edges/relations.tsv` |
| `dual_of` | categorical / order / linear-algebra dual | no | `edges/relations.tsv` |
| `contrapositive_of` / `converse_of` | logical transform of a statement | no | `edges/relations.tsv` |
| `approximates` | numerical scheme / asymptotic approximation | no (store regime + error order) | `edges/relations.tsv` |
| `historically_precedes` | historical sequence | no | `edges/relations.tsv` |
| `commonly_confused_with` | frequent misuse pair | no | `edges/relations.tsv` |
| `proved_using` (optional route) | an alternative, non-canonical proof path | no (canonical route only is a `tsort` edge) | `edges/relations.tsv` |
| `illustrated_by` | example / exercise validates comprehension | no | `edges/relations.tsv` |

`edges/relations.tsv`: `type<TAB>source_id<TAB>target_id<TAB>note`.

Forcing all of these into `tsort` edges creates artificial cycles and destroys
the meaning of the dependency order. Do not do it.

## The edge test

For every candidate `tsort` edge `A B`, first write the plain-language claim in a
`#` comment in `dependencies.plan`, then check:

> "Can I truthfully say **A must be understood / introduced before B can be
> correctly stated, proved, interpreted, or applied** — within this release's
> scope?"

If no, it is not a `tsort` edge. Never reverse direction: if the mean value
theorem is proved from Rolle's theorem, and the release introduces the MVT
after Rolle, the edge is `rolles_theorem mean_value_theorem`.

Prefer the **minimum direct prerequisite set**. Do not attach `field_axioms`,
`associativity`, `distributivity` to every algebraic identity; work at a
consistent abstraction level (`real_number`, `ordered_field`). Do not make every
possible proof route a mandatory prerequisite — the canonical proof's
dependencies are edges; alternate routes go in the node's `proof_routes`
metadata.

## Equivalent definitions

A concept with several standard definitions (compactness: open-cover / sequential
/ closed-and-bounded-in-Rⁿ; continuity: ε–δ / sequential / preimage-of-open;
prime: no proper divisors / `p | ab ⇒ p|a or p|b`) is **one node**. Pick one
definition as canonical *for the release*, record it in `conventions.md`, and:

- give the node a single `defines`/`requires` prerequisite set for the canonical
  form;
- add each other form as an `equivalent_to` relation whose `note` names the
  **equivalence lemma node** (a separate `lemma` node, with its own hypotheses —
  e.g. "sequential = open-cover compactness" needs the space to be a metric
  space, or second-countable);
- never edge the non-canonical forms as prerequisites of downstream theorems —
  edge the canonical node.

This is the main way math avoids the definitional cycles that would otherwise
appear.

## Cycle patterns and resolutions

`tsort` on a cyclic graph: GNU exits non-zero; **BSD/macOS prints
`tsort: cycle in data` to stderr, emits a meaningless order, and exits 0** —
always check stderr (this is the `tsort` skill's rule).

Protocol when a cycle is reported: stop publication; preserve the edge list and
diagnostics; name the cycle nodes; translate every cycle edge to plain language;
classify each as true-prerequisite / equivalent-definition /
alternative-proof-route / explanatory / historical / duplicate; move
non-prerequisites to `edges/relations.tsv`; if a genuine foundational choice
remains, declare one concept primitive (or one statement the axiom) for this
scope; re-run `build-tree.sh`; record in `edges/cycles.md`.

| Observed cycle | Underlying issue | Resolution |
|---|---|---|
| `completeness_of_R → sup_property`, `sup_property → completeness_of_R` | ℝ's completeness stated two provably-equivalent ways | pick one as the **axiom** of the ordered field for this release (e.g. least-upper-bound); the other becomes a `proposition` node deriving one-directionally, with an `equivalent_to` relation. |
| limit ↔ continuity | continuity defined via limits, limit examples described as "continuous" | define continuity by ε–δ directly (no `limit` prerequisite); `limit` is its own node; sequential characterizations are equivalence lemmas. |
| `determinant → eigenvalue`, `eigenvalue → determinant` | det defined via eigenvalues, char. poly uses det | determinant is primitive-ish: define via permutation expansion or multilinearity (needs only `permutation`, `multilinear_form`); eigenvalues then `derive_from` `characteristic_polynomial` which `derives_from` `determinant`. |
| measure ↔ integral | integral defined from measure, measure of a set = integral of its indicator | Lebesgue: `measure` first (from a σ-algebra + countable additivity), `integral` `derives_from` `measure`; "μ(E) = ∫ 1_E" is a proposition, not a definition edge. |
| `natural_number ↔ set` | ℕ built from sets, sets counted by ℕ | fix the foundational stance in `conventions.md`: either ℕ primitive (Peano axioms as `axiom` nodes) or ℕ constructed (finite ordinals); the other direction is a note. |
| theorem A `derives_from` B, B `derives_from` A | two results each "proved from" the other in different texts | one is canonical for the release; the other's proof-from-the-first is a `proved_using` alternative route in metadata. |

Record every resolution in `edges/cycles.md`: the cycle, each edge's
classification, what was moved / made primitive / made the axiom, and why.

## Cross-area bridges (high-value nodes)

Bridges reduce isolated result clusters. Each is a node with fully audited
hypotheses and a convention link.

| Bridge | Connects | Hypothesis to make explicit |
|---|---|---|
| fundamental theorem of calculus | differentiation ↔ integration | `f` continuous on `[a,b]` (part 1); `f` Riemann-integrable + antiderivative exists (part 2) |
| Heine–Borel | topology ↔ analysis on ℝⁿ | subset of **ℝⁿ**, finite dimension; fails in general metric spaces |
| spectral theorem | linear algebra ↔ analysis / geometry | real symmetric / complex self-adjoint; finite-dim or compact operator |
| Stokes' theorem | vector calculus ↔ differential forms | oriented manifold with boundary, `ω` compactly supported, `C¹` |
| Riesz representation | Hilbert space ↔ its dual | completeness of the inner-product space |
| Cayley's theorem | abstract groups ↔ permutation groups | — |
| Stone–Weierstrass | algebra ↔ approximation | compact Hausdorff domain, subalgebra separates points, contains constants |
| central limit theorem | probability ↔ analysis (normal law) | i.i.d., finite variance |
| Lax–Milgram | PDE weak forms ↔ Hilbert space | bilinear form bounded + coercive |

Never present a bridge as universally applicable — link its hypothesis nodes as
`tsort` prerequisites.

## Approximation / discretization ladders (applied)

Stored in `edges/relations.tsv` as `approximates`, **not** as `tsort` edges (an
approximation must not be forced to precede the exact object it approximates).
For each `approximates` pair record: the scheme / approximate object, the exact
object, the small parameter / regime (`h → 0`, `n → ∞`, `ε → 0`), the
leading error term or **order of accuracy** if the source gives it, the
stability / convergence condition, and the consequence of using it outside its
regime.

```text
approximates  forward_euler          exact_ode_flow        h -> 0; local error O(h^2), global O(h); needs h * L < 2 for stability
approximates  rk4                    exact_ode_flow        h -> 0; global error O(h^4)
approximates  central_difference     first_derivative      h -> 0; error O(h^2); catastrophic cancellation as h -> 0 in float
approximates  trapezoidal_rule       definite_integral     n -> inf; error O(h^2) for C^2 integrands
approximates  taylor_polynomial_n    analytic_function     |x - a| small; remainder R_n = f^(n+1)(xi) (x-a)^(n+1)/(n+1)!
approximates  newtons_method_iterate  exact_root            near a simple root; quadratic convergence; diverges from a bad start
```

Distinguish the **mathematical** limit from the **practical** validity limit:
`central_difference → f'(x)` as `h → 0` exactly in ℝ, but in floating point the
error is minimized at a finite `h ≈ sqrt(eps)` and grows as `h` shrinks further
— record both, and run the `bc` skill's instance check to show the crossover.
