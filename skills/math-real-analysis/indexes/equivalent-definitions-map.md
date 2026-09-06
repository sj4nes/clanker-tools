# Equivalent-definitions and equivalence map — Release 0.1

Concepts with several standard definitions are **one node** (the canonical form
for the release), with the other forms recorded here and as `equivalent_to`
rows in `edges/relations.tsv`. Downstream theorems edge the **canonical node**,
never a non-canonical form. This is how the capsule avoids definitional cycles.

| Node | Canonical definition (0.1) | Equivalent form(s) | Equivalence needs | Lemma id |
|---|---|---|---|---|
| `completeness_of_R` / `lub_axiom` | every nonempty bounded-above set has a `sup` | monotone convergence; nested intervals + Archimedean; Cauchy-complete + Archimedean; every Dedekind cut is realized | an Archimedean ordered field | `eqv_lub_mct`, `eqv_lub_nip`, `eqv_lub_cauchy` (not built in 0.1) |
| `compact_set` | every open cover has a finite subcover | `sequential_compactness` (every sequence has a subsequence converging in the set); closed and bounded (`heine_borel`) | subset of ℝ (or a metric space) | proved both ways in `heine_borel` + `sequential_compactness` |
| `continuity_at_point` | ε–δ at the point | `sequential_continuity` (`f(x_n)→f(c)` whenever `x_n→c`); preimage-of-open (global) | `(⇐)` of the sequential form uses `countable_choice` | node `sequential_continuity` |
| `function_limit` | ε–δ (with `c` a limit point) | `sequential_criterion_limit` | `(⇐)` uses `countable_choice` | node `sequential_criterion_limit` |
| `closed_set` | complement is open | `closed_iff_seq_closed` (contains all limits of its convergent sequences); contains its limit points (`closure` = itself) | in ℝ | node `closed_iff_seq_closed` |
| `connected_set` | no separation into two disjoint nonempty relatively open sets | `connected_iff_interval` (for `A ⊆ ℝ`) | `lub_axiom` | node `connected_iff_interval` |
| `uniform_convergence` | `sup_D |f_n − f| → 0` | `uniform_cauchy_criterion` (uniformly Cauchy) | completeness of ℝ | node `uniform_cauchy_criterion` |
| `radius_of_convergence` | `1/R = limsup |a_n|^{1/n}` | ratio form `lim |a_n/a_{n+1}|` when it exists; `sup{r : (|a_n| r^n) bounded}` | the ratio form needs the ratio limit to exist | `edges/relations.tsv` |
| `derivative` | limit of the difference quotient | Carathéodory: `∃φ` continuous at `c` with `f(x)−f(c) = φ(x)(x−c)`, `f'(c)=φ(c)` | — (equivalent outright) | not built in 0.1 |
| `riemann_integral` | `inf_P U(f,P) = sup_P L(f,P)` (Darboux) | tagged Riemann sums with mesh → 0 | — (equivalent outright) | not built in 0.1 |

## Reading this with `tsort`

`tsort` linearizes only the **canonical** prerequisite graph. The
`equivalent_to` edges are deliberately absent from `edges/dependencies.edges`;
adding any of them would create one of the cycles in `edges/cycles.md`.
