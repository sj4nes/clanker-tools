# Tutorial document skeleton

The shape, the lead, and the block vocabulary are the **shared contract**:
[`docs/capsule-tutorial-contract.md`](../../../docs/capsule-tutorial-contract.md).
Read it first — it is the same document `theorem-tree-tutorial` implements, and
it is what `verification/check_beats.py` enforces.

This file holds only what is specific to a **physics or chemistry** capsule.

## The `chk_` beat, for a formula tree

The contract requires one `chk_<node_id>` block per concept. For a formula tree
it is one of:

- a **dimensional check** — print the exponent vector of (left side − right
  side) on the `[M, L, T, Θ, N, I]` basis; a consistent formula prints the zero
  vector (`0 0 0`, or as many zeros as the capsule's basis carries);
- a **limiting case** — the formula at a regime boundary, printed with a
  `(want …)` annotation;
- a **worked example** — the capsule's own numbers, reused verbatim.

Prefer `bc -l` here-strings and heredocs. Never introduce a number the capsule
does not carry.

## The `cx_` beat, for a formula tree

The contract's `cx_<node_id>` is the assumption-dropped counterexample. A
physics capsule keeps its assumptions and regimes as first-class nodes (step 2
says to keep every one of them), and those nodes are where this beat comes
from: hold everything else, leave the stated regime, and show the formula
depart from reality.

The pendulum is the worked case — `small_angle_approximation` holds to a
fraction of a percent at 5°, and a 30° swing puts the true period about 1.7%
above `2*pi*sqrt(L/g)`. Print both and the gap.

Emit one where the capsule names a regime the formula depends on. Where a
relation is exact and unconditional, say so in the prose instead.

## The `lean_` beat, for a formula tree

Where a node carries `lean_status: core`, heredoc the capsule's exact snippet
from `validation/proof-checks.lean` (citing the section), run `lean`, and check
the exit status. Guard it so a reader without Lean is not blocked:

    command -v lean >/dev/null || { echo "SKIP: lean not on PATH"; exit 0; }

Echo precisely what the kernel confirmed — not "the physics is correct", but
the statement that was checked. This beat was in use in chemistry tutorials (23
`lean_` blocks) before it was written down here.

## Static Artifact companion (only if requested)

A second file, `<name>.artifact.html` or `.md`, for reading without upmd:

- Header: *"Read-only companion to `<name>.md`. The code blocks below are shown
  with the output from a real `upmd --ci --all` run; this page does not execute
  anything."*
- Every `bash` block followed by its actual captured stdout in an output block.
- No `[name:]` / `deps:` attributes (they are noise for a reader) — but keep the
  block order identical to the runnable file.
- Publish via the Artifact tool only on request; load `artifact-design` first.
- Never describe it as interactive, and never let it collect input.
