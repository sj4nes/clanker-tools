# `csplit` format-specific guidance, failure modes, and template

## Markdown

Good candidates: `'/^# /'`, `'/^## /'`, `'/^### /'`. Before splitting, check whether headings appear inside fenced code blocks; whether Setext headings are used; whether headings are escaped, quoted, generated, or duplicated; whether the document begins with a title that should stay in a preamble piece; and whether the preamble should become its own output piece.

```sh
grep -n '^## ' docs/architecture.md
csplit -s -f "$outdir/h2-" -b '%03d.md' -- docs/architecture.md '/^## /' '{*}'
```

Do not use `csplit` to restructure Markdown — only to create read-only discovery or review pieces.

## Logs

Good boundaries are stable, machine-generated record markers: `BEGIN REQUEST <id>`, `END REQUEST <id>`, `=== Test run <id> ===`, timestamped session-start records. Avoid ordinary words like `ERROR`, `WARN`, `request`, `done` — they occur inside records and create invalid fragments. Prefer start markers over end markers:

```sh
csplit -s -f "$outdir/request-" -b '%05d.log' \
  -- service.log '/^BEGIN REQUEST [A-Za-z0-9._-][A-Za-z0-9._-]*$/' '{*}'
```

After splitting: verify each chunk has one start marker; verify end-marker pairing if applicable; check for exceptions, multiline stack traces, and interleaved concurrent request logs. Do not assume one request equals one contiguous block in concurrent logging systems.

## YAML streams

```sh
csplit -s -f "$outdir/document-" -b '%03d.yaml' \
  -- manifests.yaml '/^---[[:space:]]*$/' '{*}'
```

Safe only after verifying: separators occur only at YAML document boundaries; a separator cannot occur in a block scalar or generated embedded text; each output piece is valid YAML for the consuming parser; preambles, directives, and trailing `...` markers are handled correctly; anchors, aliases, cross-document assumptions, templating, and tool-specific preprocessing do not create coupling; the target system accepts each split document independently. Prefer a YAML-aware tool for semantic transformation or validation — `csplit` does not understand YAML nesting or validity.

## SQL bundles

Use `csplit` only when an authoritative delimiter convention is present and known not to occur within string literals, comments, stored procedures, or dialect-specific constructs.

```sh
csplit -s -f "$outdir/migration-" -b '%03d.sql' \
  -- migrations-bundle.sql '/^-- migration: [0-9][0-9]*$/' '{*}'
```

Do **not** split SQL on `;` — semicolons appear in strings, procedural code, comments, and dialect-specific statements. Use the migration framework or a SQL parser for semantic extraction.

## Rust and source code

Do not split `.rs` files for editing merely because they contain `fn`, `struct`, `impl`, or `mod` lines. Attributes and docs can belong to the following item; macros can generate or consume multiple apparent items; braces, generic bounds, `where` clauses, comments, and nested modules make line regexes incomplete; `impl` blocks and modules contain multiple dependent items; a split point can sever a syntactically coupled construct; full-file imports, module-level attributes, feature gates, and formatting context may be required.

Permissible read-only use: split an intentionally generated, line-delimited Rust report; partition a corpus of already independent snippets; split a documentation export at verified headings; create rough review chunks from a very large source file only when fragments will not be compiled, edited independently, or treated as valid Rust units. For source navigation, prefer `rg`, `git grep`, language-server queries, compiler diagnostics, `rustdoc`, and AST-aware tooling.

## Common failure modes

| Failure mode | Cause | Required response |
|---|---|---|
| Unexpected `xx00` files in repo root | Default output prefix used | Stop; move/remove only confirmed generated artifacts; rerun into a dedicated directory |
| Too many fragments | Pattern matched ordinary content, examples, or comments | Narrow and anchor the regex; inspect all candidate matches |
| Too few fragments | Markers missing, differently formatted, hidden by CRLF, or excluded by pattern | Inspect visible bytes and actual markers; revise the pattern |
| Boundary line in wrong piece | Misunderstood `/REGEXP/` semantics or offset behavior | Test on a small sample; inspect first/last lines |
| Empty output files | Adjacent boundaries or split at first line | Diagnose whether empties are valid; use `-z` only if explicitly appropriate |
| Missing text after reconstruction | Used `%REGEXP%`, `--suppress-matched`, wrong output glob, or a failed run | Identify and document omissions; rerun losslessly if required |
| Duplicate/overlapping content | Incorrect offset or manual postprocessing | Compare reconstructed file with source; inspect boundary windows |
| Partial output after error | Used `-k` or implementation retained files | Mark output incomplete; do not consume; rerun in fresh directory |
| Wrong suffix or extension | Output naming did not match downstream format | Correct naming; do not imply a fragment is valid merely from its extension |
| Pattern breaks on CRLF | Regex saw carriage returns at line end | Inspect with `od` or literal mode; normalize only through a deliberate, verified process |
| Output collision | Existing files share prefix/suffix names | Use an empty unique directory and a unique prefix |
| Source syntax broken after splitting | Used `csplit` as a source-code restructuring tool | Revert to original source; use parser-aware tooling |

## Transactional split template

Lossless, review-oriented split:

```sh
#!/bin/sh
set -eu

input=${1:?usage: split-sections.sh INPUT OUTPUT_DIR}
outdir=${2:?usage: split-sections.sh INPUT OUTPUT_DIR}

test -f "$input"
test ! -e "$outdir"
mkdir -p -- "$outdir"

grep -n -- '^## ' "$input" > "$outdir/boundaries.txt"

csplit -s -f "$outdir/section-" -b '%03d.md' -- "$input" '/^## /' '{*}'

find "$outdir" -maxdepth 1 -type f -name 'section-*.md' -print |
  LC_ALL=C sort > "$outdir/pieces.txt"
test -s "$outdir/pieces.txt"

while IFS= read -r piece; do
  printf '%s: ' "$piece"
  head -n 1 "$piece"
done < "$outdir/pieces.txt" > "$outdir/piece-starts.txt"

cat "$outdir"/section-*.md > "$outdir/reconstructed.md"
cmp -s -- "$input" "$outdir/reconstructed.md"

printf '%s\n' 'Split completed and reconstruction is byte-identical.'
```

This template refuses to overwrite an existing output directory, records candidate boundaries, splits into a dedicated location, records output pieces, captures each piece's first line for review, reconstructs the original file, and uses `cmp` to require byte-for-byte equivalence. Adapt the boundary pattern, suffix, extension, and validation criteria to the input format. Do not copy it blindly into a non-GNU environment without checking `csplit` option support.
