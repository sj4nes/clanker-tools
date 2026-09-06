# halting_problem

## Type
theorem  (epistemic status: **`stated_not_proved`** — the proof is in scope only
as a sketch; `constructive_grade: n/a`)

## Statement
There is no algorithm `H` that, given (a description of) a program `P` and an
input `w`, decides whether `P` halts on `w`. The set
`K = { ⟨P, w⟩ : P halts on w }` is **recursively enumerable but not decidable**
(Turing 1936).

## Symbols
- `P`: a program / Turing machine; `w`: an input; `⟨P, w⟩`: an encoding.

## Prerequisites (tsort edges into this node)
`decidability`, `church_turing_thesis`.

## Proof (sketch — not formalised here)
Diagonalisation. Suppose `H(P, w)` decides halting. Define `D(P)`: run
`H(P, P)`; if it says "halts", loop forever; else halt. Then `D(D)` halts iff
`H(D, D)` says "does not halt" iff `D(D)` does not halt — contradiction. So no
such `H`. (`K` is r.e.: simulate `P` on `w` and halt "yes" if it does.)

## Constructive grade
`n/a` — a negative result about algorithms. The proof is itself constructive
(it exhibits the diagonal program `D`).

## Lean status
`lean_status: none`. Formalisable (and has been, in various systems) but the
Turing-machine / computability apparatus is **out of scope** for this capsule.

## Type / well-formedness check
`well_formed`. "Algorithm" via `church_turing_thesis`. The result is about the
**general** problem — halting is trivially decidable for *specific* programs, and
for many restricted classes (primitive-recursive programs, loop programs
without `while`).

## Specialization / boundary cases
- **bounded halting** ("does `P` halt within `n` steps?"): **decidable** (just
  simulate `n` steps) — the undecidability is entirely in the unbounded case.
- **totality** ("does `P` halt on *all* inputs?"): worse — `Π₂`-complete, not
  even r.e.
- **Rice's theorem**: *every* non-trivial semantic property of programs is
  undecidable — halting is the prototype.
- the **busy beaver** function `BB(n)` (max steps a halting `n`-state TM takes)
  is **non-computable** and grows faster than any computable function.

## Relation to the rest of the boundary block
- `undecidability_fol_validity` is proved by **reducing** the halting problem
  (encode a TM computation as a first-order sentence, valid iff the machine
  halts).
- `godel_incompleteness_first` and the halting problem are two faces of
  diagonalisation; incompleteness can be *derived* from the halting problem
  (a consistent, recursively axiomatised, sound arithmetic theory could
  otherwise decide halting).

## Hypothesis-dropped counterexamples / limits
- **bounded** or **step-limited** halting: decidable.
- **restricted program class** (no unbounded loops): decidable.
- the result needs the programming model to be **Turing-complete** — for
  finite automata "does it halt" is trivially decidable.

## Common misuse
"No program can ever be proved to halt" — false; termination is provable for
specific programs (and whole verified codebases). "Undecidable" ≠ "we don't
know"; it means no single algorithm works for **all** cases. Confusing with
totality or with bounded halting.

## Related nodes (non-prerequisite)
- `uses`: `decidability`, `church_turing_thesis`.
- `reduces_to`: `undecidability_fol_validity`.
- `sibling_of`: `godel_incompleteness_first` (shared diagonalisation).
- `related`: Rice's theorem, busy beaver, the arithmetical hierarchy.

## Sources
[bbj_5e] ch. 4; Turing (1936); [smith_godel_2e]; Sipser, *Theory of
Computation* ch. 5.
