---
name: knap-markdown-rendering
description: >-
  Render structured data into deterministic Markdown with the `knap` CLI
  (templates, filters, YAML front matter, tables, batch output) instead of
  assembling strings in code or prose. Use when turning JSON, CSV, or API
  records into reports, README sections, changelogs, issue summaries, release
  notes, catalogue tables, or Obsidian-compatible notes — anything where one
  repeatable layout is applied to many records. Covers the filter-selection
  map, the verified template patterns, and the failure modes, chiefly that a
  missing variable renders as empty and still exits 0. NOT a writing or
  reasoning aid — compose prose that needs judgement first and pass it in as
  data — and NOT usable for the DOM-dependent filters or host integrations the
  CLI does not supply.
version: 2.0.0
archetype: tool-fact
author: Simon Janes
tags: [markdown, templating, knap, reporting, data-to-document, yaml-front-matter]
---

# Rendering Markdown with knap

`knap` applies a template to a data object and prints Markdown. The value is
that the layout lives in one versioned file instead of being re-improvised per
record, and that the same data always produces the same document.

Verified against **knap 0.6.0**. `sh verification/run.sh`.

## Get the facts from the tool, not from memory

The binary ships its own offline reference, and it cannot drift from itself:

```sh
knap help syntax            # variables, filters, logic, whitespace, ??
knap help filters           # all 80, one line each
knap help filter table      # syntax, parameters, notes, worked examples
knap help tags              # if / elseif / else / for / set
knap validate page.knap     # static check, no data required
```

Read `knap help filter <name>` before using a filter you have not used here
before. Its examples give exact whitespace, which is the part that is wrong when
a table or a YAML block comes out subtly malformed.

## The one fact worth knowing before the first render

**A missing variable renders as the empty string and exits 0.**

```
A[{{ nope }}]B[{{ a.b.c }}]C   ->   A[]B[]C          exit 0
```

There is no strict mode. A typo, a renamed field, or an API that stopped
returning something produces a document with a hole in it and a successful
command. `knap validate` will not catch it either — it says so itself: *"static
checks only; runtime values are not checked."*

So **never treat exit 0 as evidence the document is right.** Check the rendered
text: assert it contains what the data said it should, or diff it against a
snapshot. This is also why `verification/run.sh` diffs output instead of
checking `$?`.

## Procedure

1. **Inspect the data first.** List the keys that are actually present, their
   types, and which are empty. Do not assume a field exists because the template
   wants it — the render will not tell you.
2. **Write the template to a file.** `-t` cannot take a template starting with a
   dash, which is exactly the front-matter case; see
   [`references/failure-modes.md`](references/failure-modes.md).
3. **Guard every optional section** with `{% if field %}`, so absent data leaves
   no empty heading. `[]`, `""`, `0`, `false` and `null` are all false.
4. **Render**, then **read the output** against the data — not the exit status.
5. **Snapshot it** if the layout matters. A committed expected-output file is
   what turns "it looked right once" into something that can fail later.

## Reference material

| | |
|---|---|
| [`references/filters.md`](references/filters.md) | which filter to reach for, by the shape of the job; what the CLI does not supply |
| [`references/recipes.md`](references/recipes.md) | verified templates — front matter, conditional table, batch — each naming its case |
| [`references/failure-modes.md`](references/failure-modes.md) | silent empties, `validate`'s limits, the `-t` dash problem, exit codes |

## What this skill does not do

- **It does not write for you.** Prose needing reasoning, voice, or editorial
  judgement is composed first and passed in as a data value. A template is not a
  place to think.
- **It does not reach the library-only surface.** `html_to_json` and
  `remove_html` are DOM-dependent; markdown conversion, browser selectors and
  prompts are host integrations. None are in the CLI.
- **It does not validate your data.** Nothing here checks that the data is
  correct, only that the render is faithful to it.

## Verification

[`verification/`](verification/) renders every documented template with the real
binary and diffs it against captured output; `check.sh` breaks each guard alone.

The third guard is the interesting one. Version 1.0.0 of this skill documented
`***` as a YAML front-matter fence. It renders deterministically and matches its
own expected output forever — and no front-matter parser accepts it. Diffing
cannot see that. `run.sh` therefore asserts the rendered document *parses* as
front matter, and `check.sh` reproduces the 1.0.0 defect exactly — reverting the
fence and updating the expected file to match — to prove the semantic guard
fires while the diff guard is fully satisfied.
