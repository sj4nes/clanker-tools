# existence_proof

## Type
definition  (epistemic status: `definition`; **constructive grade is the
distinction itself** — see below)

## Statement
To prove `∃x φ(x)`:
- **constructive / witnessing**: exhibit a specific term `t` and prove `φ(t)`.
  The `∃I` rule: `φ(t) ⊢ ∃x φ(x)`.
- **pure / non-constructive**: derive `∃x φ(x)` without producing any `t` —
  typically by `proof_by_contradiction` (`¬∃x φ` leads to `⊥`), by the
  pigeonhole principle, by a counting/measure argument, or by `LEM` on a
  case split whose branches both yield a (different, unnamed) witness.

## Symbols
- `φ`: a formula with `x` free.
- `t`: the witness term (constructive branch only); `t` must be **free for `x`**
  in `φ` (`free_for`).

## Prerequisites (tsort edges into this node)
`quantifier_syntax`, `nd_rules_quantifier`.

## Content
`∃I` is intuitionistic and is the constructive branch. The non-constructive
branch factors through `not_forall_iff` (`quantifier_negation`, `needs_LEM`):
`¬∀x ¬φ` is classically `∃x φ`, but the passage extracts no `x`.

## Constructive grade
- constructive branch: **`intuitionistic`**.
- pure-existence branch: **`needs_LEM`** (or `needs_DNE`) — and in a
  constructive foundation it does **not** prove `∃x φ` at all, only `¬¬∃x φ`.

The BHK reading: a proof of `∃x φ(x)` *is* a pair `(t, proof of φ(t))`. A
classical existence proof provides a proof of the proposition without providing
the pair.

## Lean status
`lean_status: core`. Constructive: `⟨x + 1, rfl⟩` in `free_for_matters`,
`fun ⟨y, hy⟩ => …` (`∃E`). Non-constructive: `Classical.not_forall` used to get
an unnamed witness (`not_forall_iff`), `#print axioms` shows `Classical.choice`.

## Type / well-formedness check
`well_formed`. Constructive branch: the witness `t` must be **well-typed for the
domain** and `free_for x` in `φ`; `φ(t)` must be `φ` with `t` substituted for the
*free* occurrences of `x` only. Pure branch: the argument must genuinely derive
`⊥` from `¬∃x φ`, using the theory, not merely restate the goal.

## Specialization / boundary cases
- `φ` decidable and the domain searchable (e.g. bounded `ℕ`): the constructive
  proof is a finite search (`bc validation/instance-checks.bc` least-element
  hunt).
- `∃!x φ` (unique existence): constructive existence **plus** `uniqueness_proof`.
- `∃x (φ ∨ ¬φ)`: constructively trivial only if the domain is nonempty and you
  can decide `φ` at some point.

## Where the pure branch fails to deliver
- **you need the object**: "there exists an irrational `x` with `xʸ` rational"
  is famously proved by a `LEM` split on whether `√2^√2` is rational — the
  classic proof names no such `x`. A constructive proof (using
  Gelfond–Schneider) does.
- **algorithmic use downstream**: a non-constructive existence result cannot be
  compiled into a program.
- **infinite search with no bound**: even constructively, `∃n φ(n)` with `φ`
  decidable is not automatically provable — you may not know a bound.

## Common misuse
Saying "let `x` be such that `φ(x)`" (an `∃E` / instantiation) and then treating
`x` as canonical / definable; giving a contradiction proof and then referring to
"**the** `x`"; substituting a witness that is not free for `x`; forgetting the
domain must be nonempty for `∃I` to even make sense.

## Related nodes (non-prerequisite)
- `pairs_with`: `uniqueness_proof` (→ `∃!`).
- `dual_of`: universal proof (`direct_proof` with a fixed arbitrary `x`).
- `uses`: `free_for`, `nd_rules_quantifier` (`∃I`, `∃E`).
- `contrast`: constructive vs classical mathematics.

## Sources
[velleman_3e] §3.5–3.6; [vandalen_5e] ch. 5 (BHK, intuitionistic `∃`);
[hammack_bop] ch. 7.
