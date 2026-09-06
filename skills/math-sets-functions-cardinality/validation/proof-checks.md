# Proof checks — what Lean verified vs. what is cited

Run: `lean validation/proof-checks.lean` (exit 0, no `sorry`).

**Environment:** Lean 4.33.1, **no Mathlib**. The ZF axioms, Zorn's lemma, the
ordinal spine, Cantor–Schröder–Bernstein, and the infinite-cardinal arithmetic
are set-level and rest on the cited sources. Lean checks the **finitary /
first-order cores** — and a surprising amount goes through in plain Lean because
"a set is a predicate `X → Prop`".

| Lean item | Kind | Universal? | Supports (nodes) | What stays cited |
|---|---|---|---|---|
| `preim_iUnion`, `preim_iInter`, `preim_compl` | `rfl` | **yes, any types** | `preimage_algebra` | nothing — these are the whole content, and they are definitional |
| `img_union` | `funext` + `propext` | **yes** | `image_algebra` | — |
| `img_inter_sub` (only `→`) | plain Lean | **yes** | `image_algebra` (the asymmetry) | that the reverse needs injectivity (the `x²` counterexample) |
| `comp_inj`, `comp_surj` | plain Lean | **yes** | `composition_preserves_properties` | the bijection case (immediate from these two) |
| `cantor` | diagonal, plain Lean | **yes, any type** | `cantor_theorem`, `cantor_diagonal`, and (one level up) `peano_holds_in_omega`'s `x ∉ x` | the Separation instance forming `D`; the `|X| ≤ |𝒫(X)|` half |
| `not_forall_iff` (`Classical.not_forall`), `not_exists_iff` (`not_exists`) | core | **yes** (one classical) | `quantifier_negation`, `de_morgan_laws` | pushing the negation through nested quantifiers in a specific statement |
| `cls_eq_iff` | plain Lean | **yes** | `equivalence_partition_correspondence`, `quotient_set`, `well_defined_on_quotient` | that the classes cover `X` and are nonempty (one-liners) |
| `pigeonhole_5_into_4` | `decide` | **instance** (function spelled out) | `pigeonhole_principle` | the universal `¬∃ f : Fin (n+1) → Fin n` injective (an induction; `Fintype` is Mathlib) |

## Node-by-node bookkeeping

- The **preimage algebra** is the highlight: `f⁻¹` commuting with `⋃`, `⋂`, and
  complement is `rfl` in Lean once sets are predicates. This is the node that
  `math-real-analysis`'s continuity and compactness proofs actually stand on,
  and it is now machine-checked and universal.
- **Cantor's diagonal theorem** is a genuine 2-line plain-Lean proof
  (`iff_not_self (iff_of_eq (congrFun h a))`), no Mathlib — it backs
  `cantor_theorem`, `cantor_diagonal`, and (via the same "no `x ∈ x`" move)
  the injectivity of the successor in `peano_holds_in_omega`.
- `lean_status` in each `results/*.yaml` is `core` (a genuine plain-Lean proof),
  `instance` (a `decide` sample), `cited` (set-level, not formalised), or
  `none` (axioms).
- **Choice bookkeeping.** Every result carries `choice_grade`:
  - `choice_free`: `preimage_algebra`, `cantor_theorem`, `cantor_diagonal`,
    `cantor_schroeder_bernstein`, `hartogs_number`, `pigeonhole_principle`,
    `equivalence_partition_correspondence`, `well_defined_on_quotient`,
    `omega_construction`, `peano_holds_in_omega`, `recursion_theorem`.
  - `needs_countable_choice`: `countable_closure_properties` (union clause),
    `finite_iff_not_dedekind_infinite`.
  - `needs_full_AC`: `zorn_lemma`, `well_ordering_theorem`, `ac_equivalences`,
    `cardinal_comparability`, `infinite_cardinal_arithmetic` (the `κ·κ=κ`
    clause), `right_inverse_iff_surjective`, `aleph_hierarchy`.
- `continuum_hypothesis` is `independent_of_ZFC` — the one node that is neither
  proved nor an axiom. Gödel's `L` and Cohen's forcing are cited, out of scope.
