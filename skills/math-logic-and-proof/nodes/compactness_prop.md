# compactness_prop

## Type
metatheorem  (epistemic status: `metatheorem`; `constructive_grade:
needs_full_classical` for an arbitrary atom set)

## Statement
A set of propositional wffs `Γ` is **satisfiable** if and only if **every finite
subset** of `Γ` is satisfiable.

## Symbols
- `Γ`: a (possibly infinite) set of wffs; `Γ₀`: a finite subset.

## Prerequisites (tsort edges into this node)
`post_completeness_theorem`, `derivability`, `satisfiability`, `soundness_prop`.

## Proof
**Via completeness** (the capsule's route): if `Γ` is unsatisfiable then
(`post_completeness_theorem`, model-existence contrapositive) `Γ` is
inconsistent, so `Γ ⊢ ⊥`; a derivation uses finitely many premises `Γ₀ ⊆ Γ`, so
`Γ₀ ⊢ ⊥`; (`soundness_prop`) `Γ₀` is unsatisfiable.
**Direct routes**: König's lemma on the binary tree of partial assignments; or
Tychonoff / an ultrafilter argument on `2^Atom`.

## Constructive grade
`needs_full_classical` for an arbitrary atom set (inherits from
`post_completeness_theorem`, or needs the Boolean prime ideal theorem via the
ultrafilter route). For a **countable** atom set the König-lemma route needs
only weak König's lemma (`needs_LEM` + `metatheoretic_induction`, choice-free).

## Lean status
`lean_status: cited`. Inherits the status of the propositional completeness
proof. The König-lemma route is the more Lean-tractable one for a countable atom
set.

## Type / well-formedness check
`well_formed`. "Satisfiable" for infinite `Γ` is `∃ v, ∀ φ ∈ Γ, v ⊨ φ` — a
single assignment for **all** of `Γ`. The theorem says finite satisfiability
delivers exactly that.

## Specialization / boundary cases
- **graph colouring**: an infinite graph is `k`-colourable iff every finite
  subgraph is (de Bruijn–Erdős) — a direct corollary (one atom per
  vertex-colour pair).
- `Γ` finite: trivial (`Γ` is its own finite subset).
- **first-order lift**: `compactness_fol`, proved the same way from
  `godel_completeness_theorem`.

## Hypothesis-dropped counterexamples
- **drop finite satisfiability** — the sole nontrivial hypothesis, essential:
  `{p, ¬p}` has an unsatisfiable finite subset and is unsatisfiable. The
  theorem's whole force is that finite satisfiability *suffices*; a set all of
  whose finite subsets are satisfiable but which is itself unsatisfiable would
  be the counterexample, and compactness is exactly the assertion that none
  exists.
- **infinitary logic `L_{ω₁,ω}`**: compactness **fails** — an infinite
  conjunction can be finitely-satisfiable-in-parts yet unsatisfiable.

## Common misuse
Thinking finite satisfiability of each subset does not yield a *single* global
assignment (it does — that is the theorem); expecting an effective/computable
assignment (generally none); applying the finite-character conclusion to
properties that are not expressible by a set of propositional wffs.

## Related nodes (non-prerequisite)
- `special_case_of`: `post_completeness_theorem` (model-existence corollary).
- `generalised_by`: `compactness_fol`.
- `equivalent_to` (arbitrary atom set, over ZF): the Boolean prime ideal
  theorem.
- `related`: König's lemma, de Bruijn–Erdős, Tychonoff.

## Sources
[enderton_logic_2e] §1.7 (Compactness); [chiswell_hodges] §2.5;
[vandalen_5e] §1.5.
