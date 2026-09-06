# church_turing_thesis

## Type
regime  (epistemic status: **`heuristic`** — a thesis, not a theorem;
`constructive_grade: n/a`)

## Statement
The **informally computable** functions (those computable by *any* effective,
mechanical procedure) are **exactly** the **Turing-computable** functions
(equivalently: the general recursive functions, the λ-definable functions, the
functions computed by register machines, …).

## Symbols
- "effectively computable" — the informal notion; "Turing-computable" — a
  precise mathematical class.

## Prerequisites (tsort edges into this node)
`decidability`.

## Content
Not provable (it equates a **precise** class with an **informal** one), but
overwhelmingly supported: (i) every independently proposed formalisation of
"algorithm" (Turing 1936, Church's λ-calculus 1936, Gödel–Herbrand recursive
functions, Post systems, register machines, while-programs) defines the **same**
class; (ii) no counterexample in 90 years. It is the licence for stating
`decidability` / `undecidability` results in terms of a formal model while
meaning "no algorithm whatsoever".

## Constructive grade
`n/a` — a thesis about the scope of a definition.

## Lean status
`lean_status: none`. A meta-mathematical thesis; nothing to formalise (though
the *equivalence* of specific models — TMs ≡ λ-calculus — is a theorem, and has
been formalised).

## Type / well-formedness check
`well_formed` as a `heuristic`. It is used, in the boundary block, to upgrade
"no Turing machine decides `X`" to "no algorithm decides `X`" — e.g. in
`undecidability_fol_validity`, `halting_problem`, and the "recursively
axiomatised" hypothesis of `godel_incompleteness_first`.

## Specialization / boundary cases
- **physical Church–Turing thesis** (a stronger, contested claim: no physical
  process computes more than a TM) — out of scope; the mathematical thesis is
  about *procedures*, not physics.
- **feasibility** version (polynomial-time) — the "extended" or "strong" thesis,
  about complexity — separate and also contested.
- **hypercomputation** models (oracle machines, infinite-time TMs) deliberately
  go *beyond* — they are not counterexamples (they are not "effective").

## Hypothesis-dropped counterexamples / caveats
- it is **not a theorem** — one cannot "prove" it without a prior formal
  definition of "effective", which is exactly what it is about.
- restricting to a **weaker** model (finite automata, primitive recursive
  functions) gives a strictly smaller class — those are not "all algorithms".
- the thesis says nothing about **which** functions are computable in a *useful*
  time.

## Common misuse
Calling it a theorem; conflating it with the physical or feasibility versions;
using it to argue about what brains/physics can compute; treating
hypercomputation models as refutations.

## Related nodes (non-prerequisite)
- `makes_precise`: `decidability`.
- `licenses`: `undecidability_fol_validity`, `halting_problem`,
  `godel_incompleteness_first` (the "recursively axiomatised" step).
- `related`: the model-equivalence theorems (TM ≡ λ ≡ recursive), the
  extended/physical theses.

## Sources
[bbj_5e] ch. 3; Turing (1936); Church (1936); [smith_godel_2e] ch. on
computability; Copeland, *SEP*: "The Church–Turing Thesis".
