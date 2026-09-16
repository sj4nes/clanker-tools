# Verification — knap-markdown-rendering

`sh run.sh` — every documented template, rendered by the real `knap` and diffed
against output captured from it.
`sh check.sh` — breaks each of run.sh's guards alone.

## Why a tool-fact skill needs a harness at all

A tool-fact skill's payload is reference material, and reference material rots
in a way prose about a method does not: the tool ships a new version and the
document silently becomes fiction. Every template in `references/` therefore has
a case here, and a claim no case covers is a claim nobody checked.

## The three guards, and why the third exists

| guard | catches |
|---|---|
| `G-render` | a case's output drifts from its `.expected` |
| `G-exit` | a case's exit status drifts from its `.rc` |
| `G-semantic` | a property of the output that diffing cannot see |

`G-semantic` is not defensive padding. Version 1.0.0 of this skill documented
`***` as a YAML front-matter fence. That renders deterministically, is stable
across versions, and matches its own expected output forever — and no
front-matter parser on earth accepts it. A diff-only harness would have
certified the defect indefinitely. `check.sh` reproduces exactly that shape:
it reverts the fence to `***` **and** updates the `.expected` to match, so
section 1 goes fully green, and asserts the semantic guard still fires.

## On the version check

`run.sh` prints a note when the installed knap is not `0.6.x`, and does **not**
fail. That is deliberate and should stay that way: every expected file here was
captured from 0.6.0, so on a different version a passing run means "the
assumptions still hold" and a failing one means "an assumption changed" — both
of which are information. Turning the note into a hard failure would convert
every upgrade into a red harness before anyone had looked at whether anything
actually broke.

The note exists because the assumptions *can* change on a version bump. When one
does, the fix is to re-capture the affected `.expected` file and correct the
prose in `references/` that quoted it — never to relax the case.

## Adding a case

Batch-row templates live in `cases/batch/` and are exercised in section 2. A row
template rendered against the movie data is meaningless — which section 1 said,
by failing, the first time one was put in `cases/`.


1. `cases/<name>.knap` — the template.
2. `cases/<name>.expected` — output captured from the real tool.
3. `cases/<name>.rc` — expected exit status, if not `0`.

Data comes from `cases/movie.json`. Capture `.expected` by running the tool,
then **read it** — capturing output is how a harness comes to assert a bug.
