# Worked slice: `bolzano_weierstrass` through every stage

A minimal end-to-end pass for one Release 0.1 (elementary real analysis) node
and its prerequisites. Illustrates the method; not a full release.

## 1. Scope (excerpt of `scope.md`)

> Release 0.1 — sequences and convergence in ℝ. Included: ℝ as a complete
> ordered field (least-upper-bound property taken as the completeness axiom;
> construction of ℝ cited, not built), sequences, subsequences, convergence,
> bounded/monotone sequences, the nested-interval property, Bolzano–Weierstrass,
> Cauchy sequences and completeness. Excluded: series, continuity, metric-space
> generality, ℝⁿ for n>1, topology. Level: upper-undergraduate. Proofs:
> sketched; key steps checked with Lean where Mathlib is available, else
> instance-checked over ℤ. Choice: not used; the ℝ¹ bisection proof is
> choice-free — noted.

## 2. Nodes (`nodes/nodes.tsv` excerpt)

```text
id	type	title	area	status	role	primary_statement
real_number	primitive	Real number	real_analysis	active	foundation	-
ordered_field	structure	Ordered field	algebra	active	foundation	-
lub_property	axiom	Least-upper-bound property	real_analysis	active	foundation	every nonempty bounded-above subset of R has a supremum
completeness_of_R	definition	Completeness of R	real_analysis	reviewed	foundation	R has the lub_property
sequence	definition	Sequence	real_analysis	active	foundation	a function x : N -> R
subsequence	definition	Subsequence	real_analysis	active	foundation	x . n_j with n_j strictly increasing
bounded_sequence	hypothesis	Bounded sequence	real_analysis	active	foundation	exists M, |x_n| <= M for all n
convergence_of_sequence	definition	Convergence	real_analysis	reviewed	core	forall eps>0 exists N forall n>=N |x_n - L| < eps
monotone_sequence	hypothesis	Monotone sequence	real_analysis	active	foundation	nondecreasing or nonincreasing
monotone_convergence_theorem	theorem	Monotone convergence	real_analysis	reviewed	core	a bounded monotone real sequence converges
nested_interval_property	theorem	Nested interval property	real_analysis	reviewed	core	a nested sequence of closed bounded intervals has nonempty intersection
bolzano_weierstrass	theorem	Bolzano-Weierstrass	real_analysis	reviewed	headline	every bounded real sequence has a convergent subsequence
```

## 3. Foundational stance (`conventions.md` excerpt)

> `real_number` and `ordered_field` are primitive for Release 0.1. ℝ is
> characterized, not constructed: the **least-upper-bound property** (`lub_property`)
> is the completeness **axiom**; `completeness_of_R` is the definitional node
> "ℝ has `lub_property`". The equivalent formulations (Cauchy-complete +
> Archimedean; monotone convergence; nested intervals + Archimedean; Dedekind
> cuts) are recorded as `equivalent_to` relations, each pointing to its
> equivalence-lemma node. This fixes the `completeness ↔ sup-property` cycle:
> `lub_property` is upstream of everything; the others derive from it
> one-directionally.

## 5. Edges (`edges/dependencies.plan` excerpt)

```text
# The ordered-field structure and the reals underlie every statement here.
real_number ordered_field
ordered_field lub_property
lub_property completeness_of_R

# A subsequence is defined in terms of a sequence.
sequence subsequence

# Convergence is a statement about a sequence and a candidate limit in R.
sequence convergence_of_sequence
real_number convergence_of_sequence

# Monotone convergence: a bounded monotone sequence converges to its sup/inf,
# which exists by the lub property.
sequence monotone_convergence_theorem
bounded_sequence monotone_convergence_theorem
monotone_sequence monotone_convergence_theorem
convergence_of_sequence monotone_convergence_theorem
completeness_of_R monotone_convergence_theorem

# Nested interval property: proved from the lub property (sup of left endpoints).
completeness_of_R nested_interval_property

# Bolzano-Weierstrass: bounded sequence -> build a nested sequence of intervals
# by bisection, each containing infinitely many terms; the common point is the
# subsequential limit. Needs the nested interval property and convergence.
bounded_sequence bolzano_weierstrass
subsequence bolzano_weierstrass
convergence_of_sequence bolzano_weierstrass
nested_interval_property bolzano_weierstrass
```

Non-prerequisite relations (`edges/relations.tsv`):

```text
equivalent_to	lub_property	monotone_convergence_theorem	over an Archimedean ordered field; see eqv_lub_mct
equivalent_to	lub_property	cauchy_completeness_plus_archimedean	see eqv_lub_cauchy
proved_using	bolzano_weierstrass	monotone_subsequence_lemma	alt route: every real sequence has a monotone subsequence, then MCT
strengthens	bolzano_weierstrass	sequential_compactness_of_closed_bounded	out of scope for 0.1 (needs closed sets)
```

## 6. Validate + sort

```sh
sh validation/graph-check.sh      # graph-check: ok
sh build/build-tree.sh            # build-tree: ok (11 ordered nodes)
```

`indexes/tsort-order.txt` (one valid order — independent roots may reorder):

```text
real_number
ordered_field
lub_property
completeness_of_R
sequence
bounded_sequence
monotone_sequence
subsequence
convergence_of_sequence
monotone_convergence_theorem
nested_interval_property
bolzano_weierstrass
```

No stderr from `tsort` → acyclic. Every edge verified `pos[A] < pos[B]`. The
`completeness ↔ sup` cycle never appears because `lub_property` is the single
upstream axiom and MCT / nested-intervals point *out of* it, not back.

## 7. Proof check — via `lean` skill (primary)

Claim: **BW for ℝ¹ by bisection.** State in Lean: given `x : ℕ → ℝ` and `M` with
`∀ n, |x n| ≤ M`, there is a strictly monotone `φ : ℕ → ℕ` and `L : ℝ` with
`Tendsto (x ∘ φ) atTop (𝓝 L)`.

- **With Mathlib**: this is essentially `tendsto_subseq_of_bounded` /
  `IsCompact.tendsto_subseq` on `Set.Icc (-M) M`. Record `lean_status: proved`,
  and the note: *Lean verified the ℝ¹ statement via Mathlib's compactness of
  closed intervals; the bisection argument itself is not the formal proof term.*
- **Without Mathlib**: no real analysis. Fall back to the **combinatorial core**
  — the pigeonhole step — as an instance check over `ℤ`: for a function
  `f : Fin 8 → Fin 2`, `decide` that some fibre has ≥ 4 elements. Label it
  *"instance check of the 'one half contains infinitely many terms' step, not
  the theorem."* Record `lean_status: partial`.

Record in `validation/proof-checks.md#bolzano_weierstrass`: what the kernel saw
(the ℝ¹ existence statement, or just the pigeonhole instance) vs what stays
informal (the coordinate induction to ℝᵏ, out of scope here anyway).

## 7. Instance & counterexample checks — via `bc` skill

Dropping hypotheses, computed in `bc` (`validation/instance-checks.md`):

- **drop boundedness:** `x_n = n`. For `n = 1..1e4`, `x_n` strictly increasing,
  no repeats, gaps `= 1`; any subsequence `→ ∞`. Confirms the counterexample.
- **drop completeness (work in ℚ):** `a_n` = `sqrt(2)` truncated to `n` digits.
  `bc` with `scale=40`: `a_5 = 1.41421`, `a_10 = 1.4142135623`; `|a_n - a_{n+1}|
  → 0` (Cauchy) but the limit `1.41421356...` is irrational — no limit in ℚ.
- **specialization, constant sequence `x_n = 3`:** trivially `|x_n - 3| = 0 <
  eps`; whole sequence is its own convergent subsequence. Holds.
- **`bc` note in the file:** *these are instances. They exhibit counterexamples
  (which is a valid disproof of the dropped-hypothesis version) and sanity-check
  the specialization; they do not prove BW.*

## 8. Views

- `indexes/hypothesis-index.md` — `bounded_sequence`: `monotone_convergence_theorem`,
  `bolzano_weierstrass`, …; `completeness_of_R`: `monotone_convergence_theorem`,
  `nested_interval_property`, `bolzano_weierstrass`.
- `indexes/counterexample-index.md` — `bounded_sequence` dropped → `x_n = n`
  (from `bolzano_weierstrass`); `completeness` dropped → digit truncations of √2
  in ℚ.
- `indexes/status-index.md` — `axiom`: `lub_property`; `proved_theorem`:
  `monotone_convergence_theorem`, `nested_interval_property`,
  `bolzano_weierstrass` (with `lean_status` per node).
- `indexes/prerequisite-paths.md` — minimal path to `bolzano_weierstrass` from
  graph structure: `real_number → ordered_field → lub_property →
  completeness_of_R → nested_interval_property`; `sequence → {subsequence,
  convergence_of_sequence}`; `bounded_sequence`.
- `indexes/symbol-index.md` via `ptx -W '[A-Za-z0-9_]+' -A` over `results/*.yaml`
  → `eps`, `N`, `M`, `x_n`, `L` each list their results; confirm with `rg`.

## Completion report (excerpt)

> Scope: Release 0.1 elementary real-sequence analysis; ℝ characterized (lub
> axiom), not constructed; excludes series, continuity, ℝⁿ, topology. Graph: 12
> nodes, 15 prerequisite edges, 2 primitive/structure roots + 1 axiom. `tsort`
> succeeded, stderr empty → acyclic (BSD-safe check). Results by status: 1 axiom,
> 2 definitions, 3 proved theorems. `bolzano_weierstrass`: type-checked
> (well-formed); ℝ¹ statement `lean_status: proved` with Mathlib
> (`cited`/`partial` without); 3 hypothesis-dropped counterexamples computed via
> `bc`; specialization (constant sequence) checked. Cycle `completeness ↔ sup`
> pre-resolved by making `lub_property` the single upstream axiom. Limitations:
> a curated dependency graph, not a complete account of real analysis; a valid
> `tsort` order confirms only the encoded constraints; the `bc` instances
> disprove dropped-hypothesis variants and sanity-check specializations but are
> not proofs; Lean verified the formalized ℝ¹ statement, not the informal
> bisection narrative or the ℝᵏ extension.
