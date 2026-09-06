---
name: formula-tree-tutorial
description: >-
  Turn a physics-formula-tree knowledge capsule (its tsort prerequisite order,
  node entries, and validation scripts) into a tutorial FOR PEOPLE: a plain
  Markdown document that runs under `upmd` (upmd.dev) so the reader executes each
  formula's dimensional check, limiting case, and worked example interactively in
  a real terminal. Use when asked to make a capsule teachable, produce an
  interactive lesson / walkthrough / explainer from a dependency-ordered formula
  graph, or build runnable course material from one. This is a META skill: it
  consumes a `physics-formula-tree` capsule and orchestrates the `bc`, `tsort`,
  and `lean` skills; the deliverable is an `upmd`-executable `.md`.
version: 0.1.0
author: Simon Janes
tags: [tutorial, upmd, executable-markdown, teaching, physics, formula-tree, meta-skill]
---

# Executable Tutorials from a Formula Tree

You take a [`physics-formula-tree`](../physics-formula-tree/SKILL.md) capsule and
produce a **tutorial a person can work through**, where every formula they meet
comes with a calculation they run themselves. The document is plain Markdown; it
executes under [`upmd`](https://upmd.dev) (`rezigned/upmd`), which turns named
fenced code blocks into a dependency-aware, real-terminal workflow.

The capsule already did the hard part — it established a correct prerequisite
order and validated the physics. Your job is to **linearize that graph into a
lesson** and make each validation step something the reader executes and sees
succeed. Seeing `0 0 0` print from a dimensional check, or a limiting case
collapse to the expected number, is the moment the formula becomes real.

## Principles

- **The `tsort` order is the lesson order.** Never introduce a concept before
  everything it depends on. Take the sequence straight from the capsule's
  `indexes/tsort-order.txt` (whole capsule or one layer) or, better for a first
  tutorial, from a single target in `indexes/prerequisite-paths.md`.
- **Every formula the reader meets gets a runnable check.** Reuse the capsule's
  own validated calculations — the dimensional checks in
  `validation/dimensional-checks.bc`, the limiting cases, the Lean instance
  checks. Split them into one named block per concept. Do **not** invent new
  physics or new numbers in the tutorial; if a calculation is not in the capsule,
  it does not belong here (or the capsule needs updating first).
- **Prose is compressed from the node entry, not copied.** Each section answers
  the capsule's five questions — what it says, what the symbols/units mean, when
  it is valid, what must be known first, what breaks it — in a few sentences.
- **Runnable blocks mirror the graph.** Name each block; give it `deps:` on the
  blocks for its prerequisites (same partial order as the capsule edges), plus a
  shared `setup` block for constants. A reader can then run any single check
  (`upmd tutorial.md -b chk_kinetic_energy`) and `upmd` runs its chain.
- **The tutorial must actually run.** `upmd --ci --all tutorial.md` exits 0 for
  every block, and every check block also runs standalone via `-b`. A tutorial
  that does not execute is not shipped.
- **Two deliverables, optionally.** The `upmd` `.md` is the hands-on artifact.
  A static Artifact companion (outputs pre-baked into the text, code shown but
  never run) is for browsing — publish it only if asked, and never let it
  claim to be interactive.

## Workflow

### 1. Choose the tutorial's scope

Point at a capsule directory. Read `scope.md`, `nodes/nodes.tsv`,
`indexes/tsort-order.txt`, `indexes/prerequisite-paths.md`, the `formulas/`
entries, and `validation/`. Then pick one:

- **Minimal path to one target formula** (recommended first tutorial) — e.g.
  "everything you need to compute a pendulum's period". Short, self-contained,
  ends in a satisfying capstone. Take the ordered node list from that target's
  entry in `prerequisite-paths.md`.
- **One layer** — e.g. "the boundary-layer chapter". Use the layer's nodes from
  `topic-index.md`, ordered by `tsort-order.txt`.
- **Whole capsule** — only once the shorter forms work; it is long.

### 2. Extract the ordered node list

Filter `indexes/tsort-order.txt` to the nodes in scope, preserving order.
Drop pure-primitive nodes the audience already knows (say so in a "prerequisites"
note) but keep every assumption/regime node — those are the point.

### 3. Draft one section per node, in order

See [`references/authoring-from-nodes.md`](references/authoring-from-nodes.md).
Each section: a short heading with the plain-language name; 2–5 sentences from
the node entry (statement, symbols + SI units, the regime it is valid in, its
failure modes); then the runnable check and one line on what its output means.

### 4. Build the `setup` block

One `bash [name:setup]` block that exports the constants every later block needs
(`g`, `R`, `gamma`, gas properties, a worked scenario's inputs). Later blocks
`deps:setup`. See [`references/upmd-mechanics.md`](references/upmd-mechanics.md)
for how state persists (shell `export` + cwd carry forward; other languages need
`--capture-state`).

### 5. Convert each capsule check into a named block

For concept `X`, emit `bash [name:chk_X, deps:"setup | chk_<prereq1> | chk_<prereq2>"]`
that runs the `bc` (or `lean`) calculation for `X` from the capsule and prints a
clearly-labelled result. Prefer `bc -l` here-strings/heredocs. Keep each block
**idempotent** and independent of run order beyond its declared `deps`.
Dimensional checks should print the zero-vector; limiting cases should print the
expected number with a `(want …)` annotation.

### 6. Add a capstone

A final `bash [name:capstone, deps:...]` block that chains the path end to end on
one concrete scenario — design a resonator, compute an engine's Carnot fraction,
predict then "measure" a pendulum period. This is where the reader sees the
whole tree pay off.

### 7. Verify it runs

- `upmd --ci --all tutorial.md` — every block exits 0, and no
  `Language not supported` / `failed to start` lines (every fence must be a
  runnable named block — see [`references/upmd-mechanics.md`](references/upmd-mechanics.md)).
- `upmd --ci -b capstone tutorial.md` — capstone runs with its full dep chain.
- `upmd --ci -b chk_<mid_node> tutorial.md` — a middle check runs with only its
  declared deps (catches a missing `deps:`).

Fix until green. A non-zero exit, a stray non-runnable fence, a missing `deps:`
(block fails when run alone), or a check printing the wrong value blocks the
tutorial.

### 8. Place and record

Write to `<capsule>/tutorial/<name>.md`. Add a row to the capsule's `README.md`
pointing at it with the one-line `upmd` command to run it. If a static Artifact
companion was requested, generate it with every code block's real output pasted
in beneath it and a header noting it is read-only.

## References

- [`references/upmd-mechanics.md`](references/upmd-mechanics.md) — block
  attributes (`name`, `deps`, `bin`), the comma-vs-pipe dependency grammar, state
  persistence, the CLI (`--ci --all`, `-b`), install, and the gotchas
  (fresh-shell blocks, cwd reset, `bc -l`, heredocs).
- [`references/authoring-from-nodes.md`](references/authoring-from-nodes.md) —
  the node-entry-field → section-part mapping, choosing which check to surface,
  parameterized "try it yourself" blocks, keeping prose compressed, citing the
  capsule.
- [`references/document-structure.md`](references/document-structure.md) — the
  standard document skeleton, the "how to run this" preamble, block-naming
  convention (`setup`, `chk_<node>`, `try_<node>`, `capstone`), and the static
  Artifact companion format.

## Completion report

Report: the source capsule and release; the tutorial's scope (target formula /
layer / whole) and the ordered node list it covers; the number of sections and
runnable blocks; the `upmd --ci --all` result (all blocks exit 0) and that the
capstone plus at least one middle check were run standalone; which capsule
calculations were reused (and confirmation that no new physics was introduced);
where the file was written and the command to run it; whether a static Artifact
companion was produced. Limitations: the tutorial teaches exactly what the
capsule encodes — same scope, same regimes, same `draft`/`reviewed` status — and
a green `upmd` run confirms the calculations execute, not that the physics is
complete.
