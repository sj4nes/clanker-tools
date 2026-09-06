# Conventions and foundational choices — Release 0.1

## Notation conventions (each is a `notation_convention` node where it affects a statement)

| Convention | Choice for this release | Node |
|---|---|---|
| ℕ | ℕ = {1, 2, 3, …}, **excludes 0**. "ℕ₀" is used when 0 is wanted (series indices, Taylor). | `natural_number` |
| Intervals | `[a,b]` closed, `(a,b)` open, `a ≤ b` always assumed; `[a,b]` with `a=b` is the single point `{a}`. | `interval` |
| `⊂` vs `⊆` | `⊆` inclusion (allows equality); `⊊` strict. `⊂` is **not used**. | — |
| Sequence indexing | `(x_n)_{n≥1}` unless stated; a shift of the index does not change convergence. | `sequence` |
| Function domain | A "function on `D`" means `f : D → ℝ` with `D ⊆ ℝ`. Limits at `c` require `c` to be a **limit point of `D`**; continuity at `c` requires only `c ∈ D`. | `function_limit`, `continuity_at_point` |
| `sup ∅`, `inf ∅` | left undefined in 0.1 (all sup/inf are of nonempty sets); `sup` of an unbounded-above set is **not** written as `+∞` in the core (only in the `limsup_liminf` extended-value node). | `supremum`, `infimum` |
| Derivative at an endpoint | one-sided; `f'(a)` on `[a,b]` is the right derivative. | `derivative` |
| Integral orientation | `∫_a^b = −∫_b^a`; the core theory is stated for `a < b` and extended by this convention. | `riemann_integral` |
| `log` | natural logarithm (base `e`); appears only in examples, not core statements. | — |
| Empty sum / product | `Σ_{k=1}^{0} = 0`, `Π_{k=1}^{0} = 1`. | `partial_sum` |
| "positive" / "negative" | strict (`> 0` / `< 0`); "nonnegative" for `≥ 0`. | — |

## Foundational primitives (documented per SKILL.md step 3)

- **`set`, `function`** — primitive at the working level. We use ZFC informally
  and never unfold a set to the ∈-axioms. Alternative foundations (type theory,
  NBG, ETCS) are intentionally out of scope.
- **`natural_number`** — primitive, with the **Peano axioms** as `axiom`-typed
  content on the node; `induction` is a separate `principle_law` node that
  `derives_from` it. A set-theoretic construction (finite ordinals) is out of
  scope. Chosen primitive because Release 0.1 is analysis, not foundations of
  arithmetic.
- **`rational_field` (ℚ)** — primitive as *an ordered field* (the operations,
  order, and their axioms are assumed). Its construction from ℤ (itself from ℕ)
  is cited, not built. Chosen primitive because the analytic content begins at
  ℝ; ℚ only supplies the "dense, ordered, **not** complete" contrast object.
- **`real_number` (ℝ)** — primitive, characterized as *the* Dedekind-complete
  ordered field: the ordered-field axioms plus `lub_axiom`. Existence and
  uniqueness-up-to-order-isomorphism are **cited** ([rudin_principles_3e] ch. 1
  appendix; [tao_analysis_I] ch. 5). A term is not primitive because its
  construction is tedious — ℝ is primitive here because *its completeness is the
  single hypothesis the whole release turns on*, and pinning it as one named
  axiom keeps that dependency visible in every downstream node.

## Cycle resolutions (full record; see `edges/cycles.md`)

1. **completeness ⟺ least-upper-bound ⟺ monotone convergence ⟺ nested intervals
   + Archimedean ⟺ Cauchy-complete + Archimedean.** These five are provably
   equivalent over an Archimedean ordered field. Forcing mutual `derives_from`
   edges is a cycle. **Resolution:** `lub_axiom` is *the* completeness axiom for
   0.1; it is upstream of everything. `monotone_convergence_theorem`,
   `nested_interval_theorem`, and `cauchy_convergence_criterion` each
   `derives_from` it **one-directionally**. The reverse implications are
   recorded as `equivalent_to` relations, each pointing to an equivalence-lemma
   note in `edges/relations.tsv` — they are *not* graph edges.

2. **limit ⟺ continuity.** Continuity is often defined "f is continuous at c if
   lim_{x→c} f(x) = f(c)", and limits are often motivated by continuity.
   **Resolution:** `continuity_at_point` is defined by its **own ε–δ statement**
   with no `function_limit` prerequisite. `function_limit` is an independent
   node. "continuity at c ⟺ the limit exists and equals f(c)" (when c is a
   limit point of the domain) is a `proposition` deriving from both, not a
   definition edge.

3. **derivative ⟺ continuity.** The derivative is defined via a function limit
   of the difference quotient; "differentiable ⇒ continuous" is a theorem, not
   part of the definition. **Resolution:** `derivative` `requires`
   `function_limit` (not `continuity_at_point`); the implication is the
   separate node `differentiable_implies_continuous`.

4. **compactness ⟺ sequential compactness ⟺ closed-and-bounded.** In ℝ (indeed
   any metric space) these coincide, and each is used to prove the others in
   different texts. **Resolution:** `compact_set` is defined by the
   **open-cover** property (canonical for the release). `heine_borel_theorem`
   ("compact ⟺ closed and bounded, for subsets of ℝ") and
   `sequential_compactness` ("compact ⟺ every sequence has a convergent
   subsequence with limit in the set") are **theorems** deriving from the
   open-cover definition + `nested_interval_theorem` / `bolzano_weierstrass`.
   Downstream theorems (EVT, Heine–Cantor, integrability of continuous
   functions) edge whichever characterization their sketch actually uses.

5. **integral ⟺ measure / area.** Not a cycle here because measure is out of
   scope: the Riemann integral is defined purely from Darboux sums (sup/inf over
   partitions). No "area" primitive is used.

## Distinguishing three orderings

The generated `indexes/tsort-order.txt` is a **prerequisite** order: every node
appears after everything needed to *state or prove* it. It is **not**:

- the **historical** order (the MVT predates a rigorous `lub_axiom` by
  ~150 years);
- the **pedagogical** order (many courses do continuity before a full treatment
  of `limsup`);
- the **logical order within a single proof** (a proof of the IVT may invoke
  `lub_axiom` at its first line, but that only means `lub_axiom` precedes
  `intermediate_value_theorem`, which it does).

Independent nodes (e.g. `geometric_series` and `open_set`) may appear in either
order in the linearization; do not read tie-order as necessity.
