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

## Adding a case

1. `cases/<name>.knap` — the template.
2. `cases/<name>.expected` — output captured from the real tool.
3. `cases/<name>.rc` — expected exit status, if not `0`.

Data comes from `cases/movie.json`. Capture `.expected` by running the tool,
then **read it** — capturing output is how a harness comes to assert a bug.
