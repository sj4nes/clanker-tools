# wlog

## Type
definition  (epistemic status: `definition`; `constructive_grade: intuitionistic`,
inherited from the case split)

## Statement
"Without loss of generality, assume `C`." A licensed abbreviation of a
`proof_by_cases` in which a **symmetry** (or a reduction) maps every other case
to the assumed one, so proving the goal under `C` proves it in all cases.

## Symbols
- `R`: the goal.
- `C`: the case actually treated.
- `σ`: the symmetry — a transformation of the data under which `R` is invariant
  and which sends the untreated cases into `C`.

## Prerequisites (tsort edges into this node)
`proof_by_cases`.

## Content
A `wlog` step has **two hidden obligations**, both of which must be dischargeable:
1. **coverage**: every configuration is either already `C`, or mapped to a
   configuration satisfying `C` by `σ`;
2. **invariance**: `R` holds of the original data iff it holds of the
   `σ`-transformed data (so a proof in the `C` case transports back).

If either fails, the "wlog" is illegitimate.

## Constructive grade
`intuitionistic` when the case split is decidable (the usual situation:
`a ≤ b ∨ b ≤ a`, `x ∈ A ∨ x ∉ A` for decidable `A`). Inherits `needs_LEM` if the
underlying disjunction is undecidable.

## Lean status
`lean_status: instance`. Lean has no primitive `wlog` without Mathlib; the
pattern is `rcases le_total a b with h | h` then, in the second branch,
`have := mainlemma b a …; simpa [comm] using this`. Mathlib's `wlog` tactic
automates the bookkeeping. Not exercised in `validation/proof-checks.lean`.

## Type / well-formedness check
`well_formed` only if the invariance is real. The check: write out `σ`
explicitly and confirm `R(data) ↔ R(σ data)`. A `wlog` with an *unstated* `σ` is
a proof gap.

## Specialization / boundary cases
- **ordering**: "wlog `a ≤ b`" — `σ` swaps `a`, `b`; valid when `R` is symmetric
  in `a`, `b`.
- **scaling / translation**: "wlog the interval is `[0,1]`", "wlog the mean is
  `0`" — `σ` is an affine map; valid when `R` is affine-invariant.
- **labelling**: "wlog `x₁` is the largest" — `σ` is a permutation.
- reduction (not strictly symmetry): "wlog `n` is prime" is usually **not**
  valid unless a genuine reduction to the prime case is given.

## Where it fails
- **`R` not invariant under `σ`**: "wlog `a ≤ b`" in proving something about
  `a − b` (sign-sensitive) — swapping changes the truth value.
- **`σ` does not cover all cases**: "wlog `x ≠ 0`" when `x = 0` is a genuine
  separate case needing its own argument.
- **`σ` alters the hypotheses**: transforming the data out of the class the
  theorem is about.
- treating "wlog" as "it is intuitively clear" — the commonest abuse.

## Common misuse
Invoking `wlog` for a convenience assumption that is not symmetry-justified;
omitting the transport-back step; using it to skip a real boundary case;
stacking multiple `wlog`s whose symmetries interfere.

## Related nodes (non-prerequisite)
- `special_case_of`: `proof_by_cases`.
- `uses`: a symmetry of the problem (a group action on the data), stated
  informally in scope.

## Sources
[velleman_3e] §3.5 (as a case-analysis shortcut); [hammack_bop] ch. 8;
Harrison, *Without Loss of Generality* (ITP 2009) for the formal treatment.
