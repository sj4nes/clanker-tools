# substitution_lemma_semantic

## Type
proposition  (epistemic status: `proved_theorem`; `constructive_grade:
intuitionistic`)

## Statement
If `t` is **free for `x` in `φ`** (`free_for`), then for every structure `𝔄` and
assignment `s`:

    𝔄 ⊨ φ[t/x] [s]   ⟺   𝔄 ⊨ φ [ s(x ↦ s̄(t)) ].

("Substituting the term `t` for `x` syntactically = updating the assignment to
give `x` the value `t` denotes.") For terms: `s̄(u[t/x]) = (s(x ↦ s̄(t)))‾(u)`.

## Symbols
- `φ[t/x]`: `substitution`; `s(x ↦ s̄(t))`: assignment update at `x` to the
  value of `t`.

## Prerequisites (tsort edges into this node)
`substitution`, `term_evaluation`, `tarski_satisfaction`, `free_for`,
`coincidence_lemma`.

## Proof
Induction on `φ` (`structural_induction_wff`), with the term sub-lemma first
(induction on `u`). Atomic: from the term sub-lemma. Connectives: IH.
**Quantifier `∀y φ`** (with `y ≠ x`, `x ∈ FV(∀y φ)`): the `free_for` condition
forces `y ∉ var(t)`, so `s(x ↦ s̄(t))(y ↦ a)` and `s(y ↦ a)(x ↦ s̄(t))` agree on
`FV(φ)` (the two updates commute and `s̄(t)` is unaffected by `y`) —
`coincidence_lemma` closes the step for every `a`.

## Constructive grade
`intuitionistic` — a structural induction, no classical step.

## Lean status
`lean_status: cited` (corrected from `partial` — audited 2026-09-11; see
`BACKLOG.md`). This node's universal statement — for every `φ`, `t`, `x`,
`s` with `free_for(t,x,φ)` — is not kernel-checked: `proof-checks.lean` has
no `FreeFor` predicate or satisfaction relation, so there is nothing to
state the lemma in. What genuinely is checked, and belongs to the sibling
`free_for` node (`lean_status: core`), is one concrete instance of the
capture-bug mechanism this lemma's hypothesis guards against:
`free_for_matters` (`∀x. ∃y. y = x+1` true; capture form `∃y. y = y+1`
false). That instance check demonstrates *why* the hypothesis is needed;
it does not establish the universal lemma. In a **de Bruijn**
representation (Mathlib) capture is structurally impossible and the lemma
has a clean, vacuous form — cited, not connected here. Cited:
[enderton_logic_2e] Lemma 24B.

## Type / well-formedness check
`well_formed` **iff** `free_for(t, x, φ)` — the hypothesis is the entire
type-safety content. Without it the two sides genuinely differ (see
counterexample). Uses `coincidence_lemma` for the quantifier case; `s` must be
defined on `FV(φ) ∪ var(t)`.

## Specialization / boundary cases
- `t = c` (constant): `𝔄 ⊨ φ[c/x] [s] ⟺ 𝔄 ⊨ φ [s(x ↦ c^𝔄)]` — the form used in
  **`∀E`** soundness (`soundness_fol`).
- `t = x`: both sides are `𝔄 ⊨ φ [s]`.
- `φ` atomic: reduces to the term sub-lemma.
- `φ` quantifier-free: `free_for` automatic; the lemma is routine.

## Hypothesis-dropped counterexamples
- **`free_for` violated**: `φ = ∃y ¬(x = y)` ("some element differs from `x`"),
  `t = y`. `φ[y/x] = ∃y ¬(y = y)` — **unsatisfiable**. But
  `𝔄 ⊨ φ [s(x ↦ s(y))]` holds whenever `|𝔄|` has ≥ 2 elements. The two sides
  **disagree** — the lemma is **false** without `free_for`. This is why
  `∀E`/`∃I` carry the `free_for` obligation.

## Common misuse
Applying it (or `∀E`/`∃I`, which depend on it) without checking `free_for`;
assuming substitution "obviously commutes with satisfaction"; forgetting the
term sub-lemma; using it when `alpha_equivalence` should first re-establish
`free_for`.

## Related nodes (non-prerequisite)
- `requires`: `free_for` (essential hypothesis); `coincidence_lemma`
  (quantifier case).
- `guards`: `nd_rules_quantifier` (`∀E`, `∃I`), `soundness_fol`.
- `used_by`: `soundness_fol`, `godel_completeness_theorem` (Henkin axioms),
  `equality_congruence`.
- `demonstrated_by`: `free_for_matters` in `validation/proof-checks.lean`
  (the failure case).

## Sources
[enderton_logic_2e] §2.2 (Substitution Lemma); [chiswell_hodges] §7.1;
[vandalen_5e] §3.1.
