# bolzano_weierstrass

## Type
theorem  (epistemic status: `nonconstructive_result`)

## Statement
Every bounded sequence `(x_n)` in `ℝ` has a subsequence `(x_{n_j})` that
converges to some `L ∈ ℝ`.

## Symbols
- `(x_n)`: a real sequence, `x : ℕ → ℝ`
- `(n_j)`: the extracted index map, `j ↦ n_j`, **strictly increasing** `ℕ → ℕ`
- `L`: the subsequential limit, `L ∈ ℝ`

## Prerequisites (tsort edges into this node)
`bounded_sequence`, `subsequence`, `sequence_convergence`,
`nested_interval_theorem`
(and transitively: `lub_axiom` → `completeness_of_R` → `nested_interval_theorem`;
`interval`, `real_number`, `absolute_value`, `natural_number`, …)

## Hypotheses
`(x_n)` is bounded: `∃M, ∀n, |x_n| ≤ M`. Ambient field `ℝ` complete
(`lub_axiom`, entering through `nested_interval_theorem`).

## Proof sketch
Bisection. `[a_0, b_0]` bounds the range. Halve it; at least one closed half
contains `x_n` for infinitely many `n` — keep it (deterministic tie-break: left
half if it qualifies, else right). Iterate: nested closed intervals `I_k` of
length `(b_0 − a_0)/2^k`, each holding `x_n` for infinitely many `n`.
`⋂ I_k = {L}` by `nested_interval_theorem`. Choose `n_1 < n_2 < ⋯` with
`x_{n_k} ∈ I_k`; then `|x_{n_k} − L| ≤ (b_0 − a_0)/2^k → 0`.

**Checked with Lean:** `validation/proof-checks.lean` §3 (the squeeze
`a ≤ x ≤ b`, both within ε of `L` ⇒ `x` within ε of `L` — the final estimate),
and §5 (the geometric decay `(b_0−a_0)/2^k`). The "a half contains infinitely
many terms" step and the ε-N logic are **not** formalized here — cited.

## Epistemic status: why `nonconstructive_result`
The tie-break makes the construction **choice-free**. But "this half contains
`x_n` for infinitely many `n`" is a `Σ⁰₂` predicate, decided non-constructively;
the `sup` inside `nested_interval_theorem` is likewise not computed. Given an
explicit modulus of boundedness the limit and subsequence are computable to any
precision, so with that data the theorem is effectively constructive — noted.

## Type / well-formedness check
`well_formed` (see `validation/type-checks.md#bolzano_weierstrass`). Forced
explicit: the index map must be **strictly increasing** (not just "some terms").

## Specialization / boundary cases
- constant sequence `x_n = c` → the whole sequence converges.
- finitely many distinct values → a constant subsequence.
- an enumeration of `ℚ ∩ [0,1]` → subsequences converging to **every** point of
  `[0,1]`.

## Hypothesis-dropped counterexamples
- **drop bounded:** `x_n = n`; consecutive terms differ by 1, so no subsequence
  is Cauchy (`validation/instance-checks.bc`).
- **drop completeness** (in `ℚ`): digit-truncations of `√2` — bounded, every
  subsequence Cauchy, none converges in `ℚ`.
- **drop finite dimension** (in `ℓ²`, out of scope, for contrast): the unit
  vectors `e_n` are bounded, pairwise distance `√2`, no convergent subsequence.

## Common misuse
Concluding the *whole* sequence converges; applying it in an incomplete space or
in infinite dimensions; forgetting that the limit `L` need not be a term of the
sequence.

## Related nodes (non-prerequisite)
- `equivalent_to`: `lub_axiom` (BW + Archimedean ⟺ lub) — `edges/relations.tsv`
- `proved_using` (alt route): `monotone_subsequence_lemma` +
  `monotone_convergence_theorem`
- feeds: `cauchy_convergence_criterion`, `sequential_compactness`,
  `heine_cantor`

## Sources
[rudin_principles_3e] Theorem 3.6; [abbott_understanding_2e] Theorem 2.5.5;
[tao_analysis_I_4e] Theorem 6.6.8.
