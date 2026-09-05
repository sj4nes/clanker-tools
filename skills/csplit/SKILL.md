---
name: csplit
description: >-
  Use `csplit` to split text files into context-defined sections by line number,
  regex boundary, or repeated marker — producing reviewable, independently
  processable excerpts from large logs, reports, concatenated documents,
  fixtures, changelogs, SQL bundles, or generated output. A partitioning tool
  only: not a source-code parser or a safe way to independently edit
  syntactically connected program fragments. Output is always a derived
  artifact; the original is preserved and every piece is verified.
version: 1.0.0
author: Simon Janes
tags: [text-processing, csplit, splitting, logs, markdown, fixtures, terminal]
---

# Context-Aware File Splitting with `csplit`

You are an autonomous terminal agent that uses `csplit` to split text files into **context-defined sections** based on line numbers, regular-expression boundaries, and repeated section markers.

Use `csplit` to create reviewable, independently processable excerpts from large text files, logs, reports, concatenated documents, fixtures, changelogs, SQL migration bundles, generated output, or other line-oriented artifacts. `csplit` creates output pieces based on line numbers or regular-expression context and, by default, names them `xx00`, `xx01`, and so on.

Treat splitting as a controlled derivation:

    identify source → inspect boundaries → choose split semantics → write to isolated output
    → verify pieces → use pieces for analysis or approved downstream work

`csplit` is a **partitioning tool**, not a source-code parser, refactoring engine, archive extractor, or safe way to independently edit syntactically connected program fragments.

## Core model

`csplit` reads one text input and writes zero or more output files. Each supplied pattern advances through the input and determines where one output piece ends and the next begins.

```sh
csplit [options] INPUT PATTERN...
```

By default it writes files named `xx00`, `xx01`, `xx02`, … and prints the byte count of each produced file to standard output. Use `--prefix`/`-f`, `--suffix-format`/`-b`, `--digits`/`-n`, and `--quiet`/`-s` to make output explicit and auditable.

For a boundary pattern `/REGEXP/`, the preceding piece receives input from the current position **up to, but not including**, the next line that matches `REGEXP`; the matching line begins the next piece (unless an offset or suppression option changes that).

```text
Preamble
# Section One
one
# Section Two
two
```

```sh
csplit input.txt '/^# Section Two$/'
```

→ `xx00` = `Preamble` / `# Section One` / `one`; `xx01` = `# Section Two` / `two`.

## Purpose and appropriate uses

Use `csplit` for: splitting a long Markdown document at headings; separating concatenated reports or fixtures by repeated markers; partitioning logs into sessions/runs/requests/date segments; breaking a large machine-generated artifact into bounded review chunks; splitting multi-document YAML-like streams *only* when separators and downstream parsing rules are verified; extracting sections from exported records, transcripts, or changelogs; partitioning a source-adjacent text corpus before analysis; separating a SQL bundle into migration-sized files when boundaries are explicit and statement semantics understood; creating isolated text excerpts for review, indexing, or fixture inspection; splitting generated output at known verified boundaries; partitioning a large plain-text input for read-only parallel analysis.

Do **not** use `csplit` as the primary tool for: refactoring source code in any language; editing YAML/TOML/JSON/XML/SQL structure; splitting a source file into independently editable units unless each fragment is guaranteed syntactically and semantically independent; reconstructing or modifying binary files; splitting archives, compressed files, databases, images, PDFs, or compiled artifacts; replacing a language parser, AST tool, migration framework, or build system; dividing a file by an arbitrary line count when semantic boundaries matter; producing security boundaries (a split file is not isolated or sanitized merely because it is smaller).

## Required operating principles

- Treat `csplit` output as derived artifacts, never as the source of truth. Preserve the original input unchanged.
- Inspect the source and enumerate candidate boundaries before splitting.
- Write output only to a new, dedicated, empty directory. Never accept default `xx00`/`xx01` names in the project root.
- Use a descriptive prefix, explicit suffix format, and enough suffix digits to avoid collisions. Confirm all output paths before execution.
- Use a dry-run equivalent: inspect boundary matches first with `grep`, `rg`, `awk`, or `sed`.
- Verify the number, names, sizes, boundaries, and contents of all generated pieces. Confirm that concatenating the pieces restores the original content when the operation is intended to be lossless.
- Use `--suppress-matched` only when deliberate removal of boundary lines is required and verified. Use `%REGEXP%` only when deliberate omission of a source region is required and verified.
- Do not use `-k` / `--keep-files` casually; it preserves partial outputs after failure — useful for diagnosis, unsafe to treat as complete.
- Do not feed `csplit` output into destructive downstream actions until pieces are inspected and completeness established.
- Keep boundary expressions narrow, anchored, and based on project-specific evidence.
- Do not assume `csplit` behavior, options, or regex dialect are identical across GNU, BSD, OpenBSD, macOS, BusyBox, and other implementations.

## Capability check

```sh
command -v csplit
csplit --version   # GNU only; BSD/macOS csplit rejects it — use: man csplit
```

Confirm support and behavior for the options you plan to use: `-f PREFIX`, `-n DIGITS`, `-b FORMAT`, `-s`, `-z`, `-k`, `--suppress-matched`. GNU `csplit` supports all of these; platform support can differ. Do not use GNU long options in a portability-sensitive environment until local help confirms they exist.

**GNU vs BSD/macOS `csplit` — verified differences.** The `csplit` on macOS and the BSDs is a different, smaller implementation. It supports only `csplit [-ks] [-f prefix] [-n number] file args...`. Specifically it does **not** support:

| Feature | GNU | BSD/macOS | Portable approach |
|---|---|---|---|
| `{*}` (repeat to exhaustion) | yes | **no** — errors `bad repetition count` | Count the markers first (`grep -c`), then use `{N}` with N = matches − 1 (the first piece plus one per remaining match) |
| `-b FORMAT` / `--suffix-format` | yes | **no** | `-f PREFIX -n DIGITS` → files are `PREFIX00`, `PREFIX01`, … (no extension; rename afterward if a consumer needs one) |
| `--` end-of-options | yes | **no** — treated as a bad option | Put the filename right after the options; guard leading-dash filenames with `./` |
| `--suppress-matched` | yes | **no** | Strip boundary lines in a second pass (`sed`/`grep -v`) after the split, and document the transformation |
| `-z` / `--elide-empty-files` | yes | **no** | Delete zero-byte pieces explicitly after verifying they are spurious |
| `--version` / `--help` | yes | **no** | `man csplit` |

What BSD/macOS `csplit` *does* honor: `-s` (quiet), `-k` (keep files on error — and it does retain partial output on failure), `-f`, `-n`, line-number and `/REGEXP/` and `%REGEXP%` patterns with `+N`/`-N` offsets, and `{N}` numeric repeat. Reconstruction from `cat PREFIX*` is byte-exact when suffixes are zero-padded.

Every command block below marked *(GNU)* uses `{*}`, `-b`, `--`, or `--suppress-matched`; on BSD/macOS translate it using the table above before running.

## Input safety check

```sh
file --brief --mime-type path/to/input
grep -Iq . -- path/to/input          # quick text/binary check
sed -n '1,80p' path/to/input
tail -n 80 path/to/input
wc -l -c path/to/input
sed -n '1,80l' path/to/input         # visible-character output if line endings/control chars matter
```

Do not proceed if the file is: binary or unknown-format data; a compressed archive; a database; a private key, credential file, secret store, or environment file; unapproved sensitive production data; a generated artifact that should be regenerated from its authoritative source; or a source file where fragmenting risks corrupting syntactic or semantic structure.

## Boundary semantics

| Pattern form | Meaning |
|---|---|
| `N` | Write from current position up to, but not including, line `N` |
| `/REGEXP/` | Write through the line before the next match; the match starts the next piece |
| `/REGEXP/+N` / `/REGEXP/-N` | Move the boundary N lines after / before the matching line |
| `%REGEXP%` | Skip from current position up to the next match instead of writing that region |
| `%REGEXP%+N` / `%REGEXP%-N` | Skip with an offset relative to the match |
| `{N}` | Repeat the preceding pattern N additional times |
| `{*}` | Repeat the preceding pattern until input is exhausted or no further match is usable |

`csplit` writes the remaining input after the last successful pattern as a final piece. If a required line number or regex match does not exist, the command fails. Note `csplit input.txt 4` means "split *before* line 4" — `xx00` gets lines 1–3, not "the first four lines".

Full detail — offsets, skip patterns, repetition hazards, and the isolated-output-directory policy — is in [`references/boundary-semantics.md`](references/boundary-semantics.md). Read it before using any offset, `%REGEXP%`, `--suppress-matched`, or `{*}`.

## Required workflow

### 1. Define the split objective

State why the file is being partitioned and what each output piece is for. Specify: the source file; its expected type and encoding; the intended boundary markers; whether the split must be lossless; the expected approximate number of pieces; the output directory; whether pieces are for read-only inspection, indexing, testing, packaging, or an explicitly approved downstream action. Do not proceed on "split it up somehow".

### 2. Inspect the source and candidate boundaries

Print line-numbered candidate boundaries before invoking `csplit`:

```sh
grep -n -- '^## ' README.md
grep -n -- '^=== CASE: .* ===$' fixtures/all-cases.txt
grep -n -- '^---[[:space:]]*$' manifests.yaml
grep -n -C 4 -- '^## ' README.md          # local context around representative matches
```

For a large source, inspect the first, middle, and last candidate boundaries. Confirm: the pattern matches only intended boundaries (not examples, comments, code blocks, quoted text, or data values); first and last sections are handled as intended; boundary lines belong to the intended piece; no malformed or duplicate markers; no mixed line endings or hidden characters altering regex matching; the output count is plausible. If the boundary is not structurally reliable, do not use `csplit` — use a parser or a format-aware tool.

### 3. Choose the split semantics

Decide where the marker line belongs. Preferred for Markdown: keep the heading with the section it introduces (`'/^## /' '{*}'` — heading begins the next piece). For block markers, splitting on the *next start marker* (`'/^BEGIN JOB$/'`) usually avoids complicated end-marker handling. Remove disposable separators with `--suppress-matched` only when markers are intentionally disposable, each piece stays valid for its consumer, first/last pieces behave as intended, and you document that it is not byte-for-byte lossless.

### 4. Build an isolated output plan

Descriptive prefix + suffix (`section-000.md`, `request-000.log`, `case-000.txt`). Suffix width: <100 pieces → 2–3 digits; 100–999 → 3; 1,000–9,999 → 4; ≥10,000 → 5+. Use `-b '%04d.md'` if supported, otherwise `-f "$outdir/section-" -n 4`. Confirm `-b` via local help.

### 5. Execute the split

Use `-s` to suppress byte-count noise once validation data is independently recorded.

```sh
# GNU shorthand:
csplit -s -f "$outdir/section-" -b '%03d.md' -- "$input" '/^## /' '{*}'
```

**Portable form (works on GNU and BSD/macOS): split on the line numbers of the markers.** BSD `csplit`'s regex + `{N}` repetition is fiddly — it errors when the file starts with a marker and the repeat count is implementation-sensitive. Deriving explicit line numbers from `grep -n` sidesteps all of that:

```sh
input=README.md
outdir=.agent-csplit/readme-h2
mkdir -p "$outdir"

# Every marker line number; drop the first only if the file starts with a marker
# (splitting at line 1 would create an empty leading piece).
lines=$(grep -n '^## ' "$input" | cut -d: -f1)
case $(sed -n '1p' "$input") in '## '*) lines=$(printf '%s\n' "$lines" | tail -n +2);; esac

csplit -s -f "$outdir/section-" -n 3 "$input" $lines
for f in "$outdir"/section-[0-9]*; do mv "$f" "$f.md"; done
```

Each numeric argument `L` ends a piece just before line `L`, so the marker line begins the next piece — the same semantics as `/^## /`. Verify the piece count immediately: it is `(number of markers) + 1` when there is a preamble, `(number of markers)` when the file starts with a marker.

Do not add `-k` by default — on failure, default behavior removes output pieces, reducing the chance partial results are mistaken for a complete corpus. Use `-k` only to debug a failed split, and label the directory incomplete. Never consume partial outputs automatically.

### 6. Verify generated pieces (mandatory)

```sh
find "$outdir" -maxdepth 1 -type f | LC_ALL=C sort
find "$outdir" -maxdepth 1 -type f | wc -l          # compare to intended section count
wc -l -c "$outdir"/*                                 # zero-byte / tiny / oversized pieces?

for piece in "$outdir"/*; do
  printf '\n===== %s =====\n' "$piece"; sed -n '1,4p' "$piece"; printf '...\n'; tail -n 4 "$piece"
done

# Lossless reconstruction (only valid without %REGEXP%, --suppress-matched, or downstream filtering)
cat "$outdir"/section-*.md > "$outdir/reconstructed.md"
cmp -s -- "$input" "$outdir/reconstructed.md" || diff -u -- "$input" "$outdir/reconstructed.md"
```

For a simple split at N matched boundaries, expect roughly N+1 pieces — but not if the first split starts at line 1, empty-file elision (`-z`) is on, boundary suppression changes output, skip patterns omit regions, the final remainder is empty, or the source begins/ends with a matching marker. Check actual behavior. Use `-z` only when empty fragments are explicitly irrelevant, never to conceal a boundary-modeling mistake. Rely on zero-padded numeric suffixes so lexical glob order matches numeric order. Then compare each piece's first line against the enumerated source markers; if a piece starts with unexpected text, stop and investigate.

## References

- [`references/boundary-semantics.md`](references/boundary-semantics.md) — worked examples of every pattern form, positive/negative offsets, `%REGEXP%` skip (lossy), `{N}` / `{*}` repetition hazards, and the isolated output-directory policy (`mktemp -d`, dedicated scratch, never repo root).
- [`references/formats-and-template.md`](references/formats-and-template.md) — Markdown, logs, YAML streams, SQL bundles, and Rust/source-code guidance; the failure-mode table; and a transactional lossless-split shell template.

## Error handling

If `csplit` fails: stop downstream processing; record the command, exit status, stderr, source path, output directory, and pattern arguments; determine whether any pieces remain (without `-k`, expect partial outputs removed; with `-k`, treat all output as incomplete diagnostic material); re-inspect candidate boundary matches; check for a pattern that never matches, incorrect quoting/shell expansion, wrong regex syntax for the local implementation, an offset reaching before the current position or beyond the source, a repeat count expecting more markers than exist, output path collisions, an unwritable directory, or encoding/line-ending problems; revise the boundary *model*, not merely command syntax; re-run into a fresh output directory; verify from scratch. Do not continue using pieces from a failed run as a complete partition.

## Completion report

```text
Split objective:
- [Why the source was partitioned.]

Source:
- [Input path and file type. Boundary definition.]

Command:
- [The exact csplit command.]

Output:
- [Directory. Number of pieces. Naming pattern.]

Verification:
- Boundary markers were enumerated before splitting.
- First and last lines of each piece were inspected.
- Piece count and size checks completed.
- Reconstruction was byte-identical / intentionally lossy, with specified omissions.
- [Any downstream parser or format validation run.]

Limitations:
- `csplit` uses line numbers and regular expressions, not language syntax.
- The output is a derived partition, not proof that pieces are independent.
- [Any format-specific caveat.]

Execution status:
- [Read-only analysis / derived artifacts created / approved downstream action performed.]
```

## Completion requirements

Before declaring a `csplit` task complete, confirm that:

- The source was verified as appropriate line-oriented text.
- The split objective and downstream use were explicitly defined.
- Candidate boundaries were enumerated and inspected before splitting.
- The regex pattern was narrow, anchored where appropriate, and tested against representative context.
- The output directory was isolated, new, and free of collisions.
- Output naming was explicit and sufficient for the expected number of pieces.
- No partial output from a failed run is being treated as complete.
- Every piece was counted and inspected at its boundaries.
- A lossless reconstruction was verified when losslessness was required.
- Any intentional omissions from `%REGEXP%` or `--suppress-matched` were documented and verified.
- No source file was changed.
