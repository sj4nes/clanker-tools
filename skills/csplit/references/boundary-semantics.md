# `csplit` boundary semantics

`csplit` writes the remaining input after the last successful pattern as a final output piece. If a required line number or regex match does not exist, the command fails.

## Line-number boundary

```text
1: alpha   2: bravo   3: charlie   4: delta   5: echo
```

```sh
csplit input.txt 4
```

→ `xx00` = lines 1–3, `xx01` = lines 4–5. The argument `4` means "split before line 4", **not** "make a file containing the first four lines". A positive line-number pattern copies input up to, but not including, that line.

## Regular-expression boundary

```text
Preamble
## Install
Install content
## Configuration
Configuration content
```

```sh
csplit input.txt '/^## Configuration$/'
```

→ `xx00` = `Preamble` / `## Install` / `Install content`; `xx01` = `## Configuration` / `Configuration content`.

Always anchor: `'/^## Configuration$/'` is far safer than `'/Configuration/'`, which might match a paragraph, inline example, link text, comment, or unrelated heading.

## Positive offset

Places the split after a fixed number of lines following the matched line.

```text
BEGIN BLOCK
metadata
payload line 1
payload line 2
END BLOCK
```

```sh
csplit input.txt '/^BEGIN BLOCK$/+1'
```

ends the first piece after the line immediately following `BEGIN BLOCK`. Use offsets only after printing enough surrounding source context to verify exactly which lines move into each piece.

## Negative offset

Places the split before a specified number of lines preceding the match.

```sh
csplit input.txt '/^END BLOCK$/-1'
```

can end the prior piece one line before the `END BLOCK` marker. Negative offsets are easy to misread — always preview the candidate match and the full offset window:

```sh
grep -n -C 4 -- '^END BLOCK$' input.txt
```

Do not use a negative offset where a clearer two-stage extraction or parser-based approach is available.

## Skip pattern (`%REGEXP%`) — lossy

Advances through input without writing the skipped portion.

```sh
csplit input.txt '%^BEGIN GENERATED$%' '/^END GENERATED$/'
```

deliberately excludes a header, preamble, or generated segment. Because `%REGEXP%` discards part of the input, treat it as a **lossy transformation**. It requires: a stated reason for the omission; prior inspection of the skipped region; a record of the exact pattern; post-split verification that the remaining output is complete for its intended use. Do not use `%REGEXP%` to silently hide malformed, confidential, inconvenient, or unexplained content.

## Repetition (`{N}`, `{*}`)

A repeat count applies to the immediately preceding pattern.

```sh
csplit input.txt '/^---$/' '{3}'      # split on '---', repeat the regex 3 more times
csplit input.txt '/^## /' '{*}'       # repeat as long as possible — many H2 sections
```

Repetition is dangerous when: the marker also occurs inside code blocks, examples, or prose; the file does not begin with an expected preamble; the final section lacks a trailing marker; an unexpected match creates many tiny fragments; the output count is not checked; or a repeated pattern eventually fails, leaving partial outputs if `-k` is enabled.

Use `{*}` only after enumerating all matches and checking that every match is a valid boundary:

```sh
grep -n -- 'PATTERN' "$input"
```

Good: `'/^# Chapter [0-9][0-9]*$/' '{*}'`. Potentially unsafe: `'/^---$/' '{*}'` on Markdown — a horizontal rule appears in prose, templates, examples, tables, and generated content and may not be a stable semantic boundary.

If the repeated marker is optional or malformed in some sections: do not assume `{*}` recovers gracefully; split a smaller known range; use a parser or custom script with explicit error handling; report the inconsistency instead of silently producing partial output.

## Output directory policy

**Never** run `csplit` in the repository root with default filenames — it creates `xx00`, `xx01`, … in the current directory, colliding with existing files or creating untracked clutter.

Required pattern:

```sh
input=README.md
outdir=.agent-csplit/readme-sections

rm -rf -- "$outdir"      # only against a resolved, reviewed path
mkdir -p -- "$outdir"

csplit -f "$outdir/section-" -b '%03d.md' -s -- "$input" '/^## /' '{*}'
```

Before using it: confirm the local `csplit` supports `-b`; confirm the output directory is agent scratch space, not a source directory; confirm it is safe to remove/recreate; never run `rm -rf` against an unresolved path. Prefer a unique directory when persistent names are unnecessary:

```sh
outdir=$(mktemp -d "${TMPDIR:-/tmp}/agent-csplit.XXXXXX") || exit 1
```

For a project-local review artifact:

```sh
outdir=.agent-csplit/$(date +%Y%m%d-%H%M%S)-sections
mkdir -p -- "$outdir"
```

Do not write generated sections into `src/`, `docs/`, `config/`, `migrations/`, or another source-controlled directory unless the task explicitly requires committed output.
