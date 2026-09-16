# Changelog — knap-markdown-rendering

Versions follow [`docs/skill-versioning.md`](../../docs/skill-versioning.md):
`1.0.0` means "as verified at release"; **MAJOR** = the skill was wrong (re-do
work done under the old text), **MINOR** = a statement changed or grew (re-read
it), **PATCH** = nothing semantic.

    git log -- skills/knap-markdown-rendering/

## 2.1.0 — 2026-09-16

**MINOR: the filter reference grew from a selection map into verified output.**
knap is new enough that an agent has no prior about it, which is the whole
reason this is a `tool-fact` skill — so 2.0.0's decision to document only *which
filter to reach for* was too thin. `references/filters.md` now shows what ~50
filters actually produce, every line copied from a verification case.

Three cases added (`c08-text`, `c09-collections`, `c10-markdown`), so the new
material is pinned rather than asserted. Cases may now name their data in a
`.data` sidecar instead of one fixture being copied per case.

Gotchas the probing turned up, none of which were guessable:

- **Parameter syntax is not uniform** — `truncate:(10, "...")` takes a tuple,
  `replace:"a":"b"` repeated colons, `nth:2` a bare number.
- **`compact` and `unique` are complementary** — `compact` drops `null`/`""` and
  keeps duplicates; `unique` does the reverse. Chain both.
- **`merge:4` yields the string `"4"`**, not the number.
- **`template` returns text, not an array**, so a following `join` silently does
  nothing.
- **`highlight`, `comment`, `callout`, `wikilink`, `embed` emit Obsidian-only
  syntax** that does not render on GitHub or under CommonMark.
- `capitalize` lowercases the rest; `safe_name` keeps spaces; `link`/`image`
  already percent-encode, so `encode_uri` on top double-encodes.

**CSV coverage, which 2.0.0 listed as an unverified claim in its own
description.** `--data <file>.csv` now has a case. It also exposed a real trap:
knap documents that "CSV values stay strings", and the consequence is not that
comparisons break — they coerce — but that **truthiness diverges**. The string
`"0"` is true where the number `0` is false, so `{% if Count %}` guards a
section for a CSV row and drops it for the equivalent JSON record. Pinned in
`run.sh` section 2.

## 2.0.0 — 2026-09-16

**MAJOR: the skill was wrong, and it was wrong about the thing it was most
likely to be used for.** 1.0.0 documented `***` as the delimiter for YAML front
matter, in two of its four template patterns. `***` renders perfectly and is
recognised as front matter by nothing. Any note produced under the old text has
unparseable metadata and must be re-rendered with a `---` fence.

1.0.0 was also unverified in the ordinary sense: it had no `verification/`, so
none of its templates had been run against the binary. They were written from
knowledge of the tool rather than from its output. Three of the four happened to
be correct.

Added, built fixture-first against **knap 0.6.0**:

- `verification/` — every documented template rendered by the real `knap` and
  diffed against captured output, with three guards (`G-render`, `G-exit`,
  `G-semantic`) and `check.sh` breaking each alone.
- `references/failure-modes.md` — chiefly that **a missing variable renders
  empty and exits 0**, so exit status is not evidence a document is right, and
  that `knap validate` is static and says so. Also the `-t` ambiguity that bites
  precisely on front matter.
- `references/recipes.md`, `references/filters.md`.

`archetype: tool-fact` declared. 1.0.0 declared `primitive`, which is not one of
the corpus's four archetypes, so no gate could tell which standard applied — the
skill was invisible to the authoring ratchet's real checks and failed only on
the archetype name.

The filter catalogue is deliberately **not** reproduced here: `knap help filter
<name>` ships with the binary and cannot drift from it. A second copy could.
