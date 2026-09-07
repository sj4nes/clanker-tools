---
name: theorem-tree-tutorial
description: >-
  Turn a math-theorem-tree knowledge capsule (its tsort prerequisite order, node
  entries, results YAML, and validation scripts) into a tutorial FOR PEOPLE: a
  plain Markdown document that runs under `upmd` (upmd.dev) so the reader
  executes each definition's instance check, each theorem's specialization, and
  each hypothesis-dropped counterexample interactively in a real terminal, and
  runs the capsule's Lean cores through a shell wrapper. Use when asked to make a
  math capsule teachable, produce an interactive lesson / walkthrough / explainer
  / runnable course material from a dependency-ordered theorem graph, or turn a
  proof-dependency map into something a person works through. This is a META
  skill: it consumes a `math-theorem-tree` capsule and orchestrates the `lean`,
  `bc`, and `tsort` skills; the deliverable is an `upmd`-executable `.md`. The
  math analogue of `formula-tree-tutorial` (which does physics).
version: 0.1.0
author: Simon Janes
tags: [tutorial, upmd, executable-markdown, teaching, mathematics, theorem-tree, lean, meta-skill]
---

# Executable Tutorials from a Theorem Tree

You take a [`math-theorem-tree`](../math-theorem-tree/SKILL.md) capsule — real
analysis, set theory, the number systems, logic, probability — and produce a
**tutorial a person can work through**, where every definition and theorem they
meet comes with a calculation or a proof they run themselves. The document is
plain Markdown; it executes under [`upmd`](https://upmd.dev) (`rezigned/upmd`),
which turns named fenced code blocks into a dependency-aware, real-terminal
workflow.

The capsule already did the hard part — a correct prerequisite order, typed
statements, hypotheses as first-class nodes, one specialization and one
hypothesis-dropped counterexample per result, `bc` instance checks, and Lean
cores with an explicit kernel-vs-cited split. **Your job is to linearize a slice
of that graph into a lesson** and make each check something the reader executes
and sees succeed. Seeing a brute search return `0` where a counterexample is
impossible, a bisection collapse onto `√2`, or `lean` print nothing (exit 0) on
a kernel core — that is the moment the theorem becomes real. Then, one section
later, seeing the *same* hypotheses hold and the conclusion **fail** the moment
you move from `ℝ` to `ℚ` — that is the moment the hypothesis becomes real.

This is the math analogue of [`formula-tree-tutorial`](../formula-tree-tutorial/SKILL.md).
Same `upmd` delivery, same "one runnable block per concept wired by `deps:`"
shape. What changes, following `math-theorem-tree`'s own adaptation of
`physics-formula-tree`:

| physics tutorial | math tutorial |
|---|---|
| dimensional check (prints `0 0 0`) | **type / well-formedness check** + a `bc` **instance check** (a definition made concrete, an identity at sample values) |
| limiting case (`v=0 ⇒ K=0`) | **specialization** — the result at a boundary parameter, landing on a memorable value |
| failure mode named in one sentence | **hypothesis-dropped counterexample, made runnable** — the centre of the math lesson, not a footnote |
| exactness label (`exact` / `approx`) | **epistemic status** + **per-node `lean_status`** (`core` / `cited`) + the capsule's **per-result grade** (`choice_grade` / `constructive_grade` / `convergence_mode`) |
| `bc` dimensional-checks file | `validation/proof-checks.lean` (run via a shell wrapper — `upmd` has no Lean runner) + `validation/instance-checks.bc` + the inline `type_check_note` / `specialization_cases` / `counterexamples_when_dropped` in each `results/<id>.yaml` |

## Principles

- **The `tsort` order is the lesson order.** Never introduce a concept before
  everything it depends on. Take the sequence from the capsule's
  `indexes/prerequisite-paths.md` (one headline target — the recommended first
  tutorial) or `indexes/tsort-order.txt` (a layer, or the whole capsule).
- **Every concept the reader meets gets a runnable block.** Reuse the capsule's
  own validated material — the Lean cores in `validation/proof-checks.lean`, the
  `bc` worksheets in `validation/instance-checks.bc`, and each result YAML's
  `specialization_cases` and `counterexamples_when_dropped`. **Invent no new
  mathematics and no new numbers.** If a check is not in the capsule, it does
  not belong in the tutorial — or the capsule needs the check added first (and
  re-validated) before the tutorial can use it.
- **The counterexample is the lesson.** Physics tutorials mention failure modes;
  math tutorials *run* them. For every theorem section, after the "it works"
  check, add the capsule's `counterexamples_when_dropped` as a second runnable
  block that holds every hypothesis but one and shows the conclusion break. This
  is where hypotheses stop being decoration.
- **Lean beats are real and honest.** `upmd` has no native Lean runner, so a
  proof beat is a `bash` block that writes the capsule's Lean snippet to a temp
  file, runs `lean` on it, and checks the exit code — printing `SKIP` and
  exiting 0 if `lean` is not on `PATH`. **Say exactly what the kernel verified**:
  "universal over ℤ by `omega`" vs "an instance at `a=5, b=3` by `decide`" vs
  "cited — not formalised here". Never let a `decide` instance read as a proof of
  the general theorem; the capsule already draws this line, so copy its wording.
- **Surface the grade.** Where the capsule tags a result
  (`choice_grade: needs_full_AC`, `constructive_grade: needs_LEM`,
  `convergence_mode: in_distribution`), make it a one-sentence teaching beat:
  *which assumption does this rest on, and what is the weaker thing that is not
  enough.* This is the capsule's distinctive payload — do not drop it.
- **Prose is compressed from the node entry, not copied.** Each section answers
  the capsule's questions — what it says (the statement, quoted once), what the
  typed symbols mean, its hypotheses (named as the nodes they are), what must be
  known first (implicit in the order), what one dropped hypothesis breaks — in
  ~120–220 words.
- **Runnable blocks mirror the graph.** Name each block with the capsule's exact
  node id (`chk_<id>`, `cx_<id>`, `lean_<id>`); give it `deps:` on the blocks for
  its prerequisites, the same partial order as `edges/dependencies.plan`
  restricted to nodes that have a block; plus a shared `setup` block. A reader
  can then run any single check and `upmd` pulls its chain.
- **The tutorial must actually run.** `upmd --ci --all tutorial.md` exits 0 for
  every block; the capstone and at least one middle check also run standalone
  via `-b`; every Lean block runs (or cleanly `SKIP`s) standalone. A tutorial
  that does not execute is not shipped.
- **Two deliverables, optionally.** The `upmd` `.md` is the hands-on artifact. A
  static Artifact companion (outputs pre-baked, code shown but never run) is for
  browsing — publish only if asked, load `artifact-design` first, and never let
  it claim to be interactive.

## Workflow

### 1. Choose the tutorial's scope

Point at a capsule directory. Read `scope.md` and `conventions.md` (the
foundational stance and the per-result grade policy — you will teach exactly
this), `nodes/nodes.tsv`, `indexes/tsort-order.txt`,
`indexes/prerequisite-paths.md`, the `results/*.yaml` for the target region,
`validation/proof-checks.md` (the kernel-vs-cited table) and
`validation/proof-checks.lean`, and `validation/instance-checks.bc`. Then pick
one:

- **Minimal path to one headline result** (recommended first tutorial) — e.g.
  "Kolmogorov's three axioms and everything that follows in ten lines", "√2 is
  irrational and that is a crisis", "the concentration ladder Markov → …→
  Hoeffding". Take the ordered node list from that target's section in
  `prerequisite-paths.md`. See [`docs/tutorial-map.md`](../../docs/tutorial-map.md)
  for a menu of cuts across every capsule.
- **One thematic band** — e.g. "the four modes of convergence", "quotients and
  well-definedness". Nodes from the band, ordered by `tsort-order.txt`.
- **Whole capsule** — only once the shorter forms work; it is long, and reads as
  a reference walk-through rather than a lesson.

### 2. Extract the ordered node list

Filter `indexes/tsort-order.txt` to the nodes in scope, preserving order. Drop
the discharged-primitive roots the audience already has (name them in a
"prerequisites" note — for a probability tutorial that is "σ-algebras and the
integral, from the two capsules below; here they are cited"). Keep **every**
hypothesis / structure / grade node in scope — those are the point.

### 3. Draft one section per node, in order

See [`references/authoring-from-nodes.md`](references/authoring-from-nodes.md)
for the YAML-field → section-part mapping. Each section: a plain-language
heading; the statement quoted once on its own line; 2–5 sentences (typed
symbols, hypotheses named as nodes, the grade if the node carries one, the one
dropped-hypothesis failure); then the runnable block(s) and one line on what the
output means.

### 4. Build the `setup` block

One `bash [name:setup]` block exporting the constants and scenario inputs every
later block needs (a seed value, a high-precision reference constant, a
tolerance, a worked probability model's parameters). Later blocks `deps:setup`.
See [`references/upmd-mechanics.md`](references/upmd-mechanics.md) for how state
persists (shell `export` + cwd carry forward; nothing else does).

### 5. Convert each capsule check into a named block

For concept `X` (capsule node id `x`):

- **`bash [name:chk_x, deps:"setup | chk_<prereq>"]`** — the "it works" beat: a
  `bc` instance check (definition made concrete, identity at sample values, a
  bisection or brute search demonstrating the theorem), or a `bc` line straight
  from `validation/instance-checks.bc`. Print a **labelled** result with a
  `(want …)` annotation and a hard guard (`exit 1` on a real mismatch — a bare
  `bc` mismatch does not fail the block).
- **`bash [name:cx_x, deps:chk_x]`** — the hypothesis-dropped counterexample
  from the YAML's `counterexamples_when_dropped`: hold every hypothesis but the
  named one, run the thing, show the conclusion break (empty intersection, a
  divergent mean, a sequence with no limit). One `cx_` block per theorem
  section; skip only where the YAML says every hypothesis is essential /
  unconditional (state that instead).
- **`bash [name:lean_x, deps:setup]`** — where the node has `lean_status: core`,
  the Lean wrapper block: heredoc the capsule's exact snippet from
  `validation/proof-checks.lean` (cite the section), run `lean`, check exit;
  `command -v lean || { echo "SKIP: lean not on PATH"; exit 0; }` first. Echo
  precisely what the kernel confirmed. See
  [`references/upmd-mechanics.md`](references/upmd-mechanics.md#lean-beats).

Keep every block **idempotent** and independent of run order beyond its declared
`deps`. Reuse the capsule's numbers verbatim.

### 6. Add a capstone

A final `bash [name:capstone, deps:...]` block that chains the path end to end
on one concrete object — one sequence in two number systems, one probability
model computed from the axioms up, one inequality applied four ways. This is
where the reader sees the whole slice of the tree pay off, and where the grade
lands ("every step here is `choice_free`" / "this delivers convergence in
probability, and no stronger mode").

### 7. Verify it runs

- `upmd --ci --all tutorial.md` — every block exits 0; no
  `Language not supported` / `failed to start` (every fence is a named runnable
  block — no bare or 4-space-indented code fences, formulas inline in prose).
- `upmd --ci -b capstone tutorial.md` — capstone runs with its full dep chain.
- `upmd --ci -b chk_<mid> tutorial.md` and `-b lean_<mid>` — a middle check and
  a Lean beat each run with only their declared deps (catches a missing `deps:`;
  confirms the Lean block `SKIP`s or passes in isolation).

Fix until green. A non-zero exit, a stray non-runnable fence, a missing `deps:`,
a check printing the wrong value, or a Lean block that neither passes nor cleanly
`SKIP`s blocks the tutorial.

### 8. Place and record

Write to `<capsule>/tutorial/<name>.md`. Add a row to the capsule's `README.md`
and `SKILL.md` pointing at it with the one-line `upmd` command. Update
[`docs/tutorial-map.md`](../../docs/tutorial-map.md) — move the row from a
"candidate" tier to "shipped". If a static Artifact companion was requested,
generate it with every block's real captured output pasted beneath it and a
read-only header.

## References

- [`references/upmd-mechanics.md`](references/upmd-mechanics.md) — block
  attributes (`name`, `deps`, `bin`), the comma-vs-pipe dependency grammar,
  state persistence, the CLI, **the Lean-beat wrapper pattern** (temp file, exit
  check, `SKIP` on missing `lean`, the genuine-vs-instance wording), and the
  `bc` / `upmd` gotchas.
- [`references/authoring-from-nodes.md`](references/authoring-from-nodes.md) —
  the `results/<id>.yaml` field → section-part mapping; choosing which check to
  surface (instance vs specialization vs counterexample vs Lean core); writing
  the counterexample beat; surfacing the grade; parameterized "try it yourself"
  blocks; compression rules; citing the capsule.
- [`references/document-structure.md`](references/document-structure.md) — the
  standard document skeleton, the "how to run this" and "what you need first"
  preamble (including the Lean-optional note), the block-naming convention
  (`setup`, `chk_<id>`, `cx_<id>`, `lean_<id>`, `try_<id>`, `capstone`), and the
  static Artifact companion format.

## Completion report

Report: the source capsule and release; the tutorial's scope (target result /
band / whole) and the ordered node list it covers; the number of sections and of
runnable blocks, broken down as `chk_` / `cx_` / `lean_`; the `upmd --ci --all`
result (all blocks exit 0) and that the capstone plus at least one middle check
and one Lean beat were run standalone; which capsule material was reused
(Lean sections, `bc` lines, YAML specializations/counterexamples) and
confirmation that no new mathematics was introduced; for every Lean beat, the
kernel-vs-cited status echoed; where the file was written and the command to run
it; whether a static Artifact companion was produced; the `docs/tutorial-map.md`
row updated. Limitations: the tutorial teaches exactly what the capsule encodes
— same scope, same foundational stance, same `draft`/`reviewed` status, same
grades — and a green `upmd` run confirms the checks execute, not that the
mathematics is complete or that any `cited` result was verified here.
