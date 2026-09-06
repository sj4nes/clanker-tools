# assignment

## Type
definition  (epistemic status: `definition`; `constructive_grade: n/a` —
`naive_collection`)

## Statement
A **variable assignment** (valuation) in a structure `𝔄` is a function
`s : Var → |𝔄|` mapping each variable to a domain element. The **update**
`s(x ↦ a)` (also `s[x/a]`, `s_x^a`) agrees with `s` everywhere except at `x`,
where it takes value `a`.

## Symbols
- `s`, `s'`: assignments; `s(x ↦ a)`: the update at `x`.

## Prerequisites (tsort edges into this node)
`structure`, `naive_collection`.

## Content
The parameter that lets **open** formulas be evaluated: `𝔄 ⊨ φ [s]`
(`tarski_satisfaction`) needs `s` for the free variables of `φ`. The quantifier
clauses recurse via updates: `𝔄 ⊨ ∀x φ [s]` iff `𝔄 ⊨ φ [s(x ↦ a)]` for every
`a ∈ |𝔄|`. For a **sentence**, `s` is irrelevant (`coincidence_lemma`).

## Constructive grade
`n/a` — a `naive_collection`-level function; classicality is elsewhere.

## Lean status
`lean_status: cited`. Mathlib uses `Fin n → M` (a finite tuple for the `n` free
de Bruijn variables) rather than a total `Var → M`; `Function.update` / cons is
the update. Not in `validation/proof-checks.lean` (propositional).

## Type / well-formedness check
`well_formed`. `s` total on `Var` (or at least on `FV(φ)` — `coincidence_lemma`
says only those matter). `s(x ↦ a)` is again a total assignment. Two updates on
**different** variables commute: `s(x ↦ a)(y ↦ b) = s(y ↦ b)(x ↦ a)` for
`x ≠ y` — used in the quantifier cases of `substitution_lemma_semantic`.

## Specialization / boundary cases
- `φ` a **sentence**: `𝔄 ⊨ φ [s]` independent of `s` — write `𝔄 ⊨ φ`.
- `s` restricted to `FV(φ)`: unchanged truth value (`coincidence_lemma`).
- **finitely many free variables** (always, for a wff): `s` matters only at
  those — so an assignment is effectively a finite tuple.
- update by a **named** element `s(x ↦ s̄(t))`: the semantic counterpart of the
  syntactic substitution `φ[t/x]` (`substitution_lemma_semantic`).

## Hypothesis-dropped counterexamples
- **`s` undefined at a free variable of `φ`**: `𝔄 ⊨ φ [s]` is undefined.
- **update on the same variable twice, expecting commutation**:
  `s(x ↦ a)(x ↦ b) = s(x ↦ b)` — the second wins; not a "swap".
- **empty domain**: no assignment exists (`Var → ∅` is empty) — another reason
  domains are nonempty.

## Common misuse
Treating an open formula's truth as `s`-independent; forgetting updates on the
same variable overwrite; assuming updates on different variables interfere;
confusing `s(x ↦ a)` (semantic update) with `φ[t/x]` (syntactic substitution).

## Related nodes (non-prerequisite)
- `feeds`: `term_evaluation`, `tarski_satisfaction`.
- `related`: `coincidence_lemma` (only `FV` matters),
  `substitution_lemma_semantic` (update ↔ substitution).
- `propositional_shadow`: a `truth_assignment` (no domain, just bits).

## Sources
[enderton_logic_2e] §2.2; [chiswell_hodges] ch. 5; [vandalen_5e] §3.1.
