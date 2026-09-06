# incompleteness_of_PA_ZFC

## Type
corollary  (epistemic status: **`stated_not_proved`** — immediate from the Gödel
theorems; `constructive_grade: n/a`)

## Statement
If **Peano arithmetic** `PA` is consistent, it is **incomplete**: there is an
arithmetical sentence `G` with `PA ⊬ G` and `PA ⊬ ¬G` (and `G` is true in `ℕ`);
and `PA ⊬ Con(PA)`. The same holds for **`ZFC`** (if consistent): `ZFC ⊬ Con(ZFC)`,
and `ZFC` does not decide `CH`, `¬CH`, the existence of large cardinals, and
much else.

## Symbols
- `PA`: first-order Peano arithmetic; `ZFC`: Zermelo–Fraenkel + Choice.
- `G`: a Gödel sentence; `Con(·)`: the consistency statement.

## Prerequisites (tsort edges into this node)
`godel_incompleteness_first`, `godel_incompleteness_second`.

## Content
The concrete instantiation of the Gödel theorems for the two theories
mathematics actually runs on. Both `PA` and `ZFC` are **consistent** (widely
believed; provable in stronger systems), **recursively axiomatised** (their
axiom sets are decidable — `PA` has an axiom **schema** of induction, still
decidable; `ZFC` similarly), and **interpret arithmetic** — so both incompleteness
theorems apply.

## Constructive grade
`n/a` — a boundary corollary.

## Lean status
`lean_status: none`. Cited: [smith_godel_2e], [bbj_5e].

## Type / well-formedness check
`well_formed` — the three hypotheses of `godel_incompleteness_first`
(consistency, recursive axiomatisation, interpreting `Q`) are met by both `PA`
and `ZFC`; the second theorem's stronger arithmetic hypothesis (HBL conditions)
is also met.

## Specialization / boundary cases — natural independent statements
- **`PA`**: Goodstein's theorem; the Paris–Harrington principle (a strengthened
  finite Ramsey theorem); Kruskal's tree theorem; termination of the hydra
  game — all true, all `PA`-independent (provable using transfinite induction
  past `ε₀`).
- **`ZFC`**: the **Continuum Hypothesis** (`math-sets-functions-cardinality`
  states its independence — Gödel `L` + Cohen forcing); Suslin's hypothesis;
  the existence of inaccessible / measurable / … cardinals; Whitehead's problem;
  Borel conjecture. (Mechanism: **forcing**, not Gödel-style diagonalisation —
  but the *headline* "`ZFC` is incomplete" is the same.)
- **`PA + Con(PA)`**, **`ZFC + Con(ZFC)`**: strictly stronger consistent
  theories, themselves incomplete.

## Hypothesis-dropped counterexamples
- **`PA` inconsistent**: then it is trivially "complete" (proves everything) —
  the "if consistent" is doing real work.
- **drop first-order** (second-order `PA` with standard semantics): categorical,
  hence "complete" in the sense of having one model — but **no complete proof
  system** (`godel_completeness_theorem` fails for SOL). You trade incompleteness
  of the theory for incompleteness of the logic.
- **true arithmetic `Th(ℕ)`**: complete, but not recursively axiomatised.

## Common misuse
"Gödel proved arithmetic / set theory is inconsistent" — no, incomplete
(assuming consistent). "There are true statements we can never prove" — `G` is
provable in stronger systems; "never" would need a fixed system. Conflating
`ZFC`'s incompleteness mechanism (forcing, for `CH`) with Gödel's
diagonalisation (for `Con(ZFC)`). Assuming *every* undecided statement is a
weird self-referential one (Goodstein, `CH` are natural).

## Related nodes (non-prerequisite)
- `instance_of`: `godel_incompleteness_first`, `godel_incompleteness_second`.
- `related`: `continuum_hypothesis` (`math-sets-functions-cardinality`, stated
  independent), forcing, the constructible universe `L`, Goodstein /
  Paris–Harrington.

## Sources
[smith_godel_2e]; [bbj_5e] ch. 17–18; Paris & Harrington (1977);
[enderton_logic_2e] §3.5.
