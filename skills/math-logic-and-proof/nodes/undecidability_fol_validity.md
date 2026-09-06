# undecidability_fol_validity

## Type
theorem  (epistemic status: **`stated_not_proved`**; `constructive_grade: n/a`)

## Statement
There is no algorithm that, given an arbitrary first-order sentence `φ` (in a
language with at least one binary relation symbol), decides whether `φ` is valid
— equivalently (by `godel_completeness_theorem`), whether `φ` is derivable. The
set of valid sentences is **recursively enumerable but not decidable**
(Church, Turing, 1936; the *Entscheidungsproblem* has no solution).

## Symbols
- `φ`: a first-order sentence in a sufficiently rich language.

## Prerequisites (tsort edges into this node)
`decidability`, `church_turing_thesis`, `derivability_fol`,
`godel_completeness_theorem`.

## Proof (sketch — not formalised here)
**Reduce the `halting_problem`**: for a Turing machine `M` and input `w`,
construct a first-order sentence `φ_{M,w}` (over a language describing tape
configurations and transitions) such that `φ_{M,w}` is **valid** iff `M` halts
on `w`. A decision procedure for validity would then decide halting —
contradiction. (Alternative reductions: Post correspondence, the word problem
for semigroups, tiling.)
**Semidecidability** is from `godel_completeness_theorem`: enumerate all
derivations; `φ` is valid iff a derivation of `φ` eventually appears.

## Constructive grade
`n/a` — a negative result about algorithms.

## Lean status
`lean_status: none`. The TM-encoding apparatus is out of scope.

## Type / well-formedness check
`well_formed`. "Algorithm" via `church_turing_thesis`. The claim is about
**full** first-order logic over a rich enough language; many **fragments** are
decidable (see below) — the theorem locates the boundary.

## Specialization / boundary cases (decidable fragments)
- **monadic** FOL (only unary predicates, no equality, no functions):
  **decidable** (Löwenheim 1915).
- **Bernays–Schönfinkel–Ramsey** class (`∃*∀*` prefix, no function symbols):
  decidable.
- **two-variable** FOL (`FO²`): decidable (NEXPTIME).
- **guarded fragment**: decidable.
- **Presburger arithmetic** `(ℕ, +, <)`: decidable (Presburger 1929).
- **real closed fields** `(ℝ, +, ·, <)`: decidable (Tarski).
- **propositional logic**: decidable (`tautology_decidable`).
The undecidability needs enough power to encode computation — a single binary
relation suffices.

## Consequences (stated)
- the **word problem for groups** (Novikov–Boone), **semigroups** (Post),
  and **Hilbert's 10th problem** (Diophantine solvability, MRDP) are
  undecidable — via or alongside this result.

## Hypothesis-dropped counterexamples / limits
- restrict to a decidable fragment (above) — the negative result does not apply.
- "no algorithm" does **not** mean "no proof": valid sentences are exactly the
  provable ones (completeness); there is just no *decision* procedure. Provers
  succeed on practical inputs via semidecidability + heuristics.
- with **equality but nothing else** in the language: decidable.

## Common misuse
Thinking "undecidable" means valid sentences lack proofs; conflating it with
incompleteness of a theory; assuming SAT/SMT-solver or theorem-prover success
refutes it; applying it to decidable fragments.

## Related nodes (non-prerequisite)
- `reduces_from`: `halting_problem`.
- `uses`: `godel_completeness_theorem` (for semidecidability).
- `contrast_with`: `tautology_decidable`; the decidable fragments.
- `related`: word problems, Hilbert's 10th (MRDP), the arithmetical hierarchy.

## Sources
[bbj_5e] ch. 11; Church (1936); Turing (1936); [enderton_logic_2e] §3.5;
[smith_godel_2e].
