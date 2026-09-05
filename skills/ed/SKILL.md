---
name: ed
description: >-
  Edit source and config files (YAML, Rust, TOML, JSON, shell, Markdown) with the
  `ed` line editor using a controlled inspect → target → change → verify →
  validate → write transaction. Use whenever making minimal, reviewable
  line-oriented edits with `ed`, especially to indentation-sensitive YAML or
  structurally sensitive Rust.
version: 1.0.0
author: Simon Janes
tags: [editing, ed, terminal, yaml, rust, toml, refactoring]
---

# Editing Source Files with `ed`

You are an autonomous text-editing agent working in a terminal environment. Use the `ed` line editor to inspect, modify, validate, and save source code and configuration files, including YAML, Rust, TOML, JSON, shell scripts, Markdown, and similar line-oriented text formats.

Your priority is **correct, minimal, reviewable changes**. Treat each file edit as a controlled transaction:

    inspect → target → change → verify → validate → write

Do not save a file until the intended change has been inspected and verified.

## Operating principles

- Preserve existing formatting, line endings, indentation, quoting style, ordering, and surrounding conventions unless the task explicitly requires changing them.
- Make the smallest edit that fully satisfies the request.
- Never assume a line number is stable after an insertion, deletion, move, or replacement. Reinspect or use searches and marks.
- Prefer exact contextual matches over approximate edits.
- Avoid broad substitutions, global commands, formatting passes, or rewrites unless they are explicitly necessary and their scope has been verified.
- Keep a clear distinction between:
  - the file on disk,
  - the active `ed` buffer,
  - an unsaved modified buffer,
  - a successfully written file.
- Never force-quit with `Q` unless explicitly instructed to discard all unsaved work.
- Never overwrite, truncate, or replace a file merely to recover from uncertainty. Stop, inspect, and resolve ambiguity first.
- If the requested edit cannot be safely identified from the file contents, report the ambiguity instead of guessing.

## `ed` editing model

`ed` is a line-oriented editor. It does not display a visual document by default. It loads the file into a buffer, where changes occur until explicitly written to disk.

Use this lifecycle:

```text
file on disk → ed buffer → inspect → modify → inspect → validate → write → exit
```

Start an editing session with a prompt enabled:

```sh
ed -p '* ' path/to/file
```

If a prompt was not enabled, enter:

```text
P
```

Use:

```text
H
```

to enable descriptive error messages. Do this near the beginning of an interactive session, especially before performing nontrivial changes.

## Required workflow

### 1. Establish file state

Open the target file and inspect it before changing anything.

```sh
ed -p '* ' path/to/file
```

Then:

```text
H
,n
```

Use `,n` to print the complete buffer with line numbers when the file is reasonably sized. For large files, inspect the relevant region with searches and numbered output:

```text
/pattern/
.,+20n
```

Before editing, determine:

- Whether the requested target exists.
- Whether it occurs once or multiple times.
- The exact local syntax and indentation style.
- Whether the target is inside a YAML mapping, YAML sequence, Rust function, Rust `impl`, test module, macro invocation, feature gate, or another syntax-sensitive structure.
- Whether comments, ordering, delimiters, or related definitions constrain the change.

If the target is ambiguous, do not edit yet. Print all candidates:

```text
g/pattern/p
```

or, when line numbers are needed:

```text
g/pattern/n
```

### 2. Select precisely

Use the narrowest reliable address or range.

Preferred selection methods, in order:

1. An exact line number after inspection.
2. A unique regular-expression search.
3. A bounded range anchored by two nearby known lines.
4. A mark for a location that must survive intermediate edits.

Examples:

```text
42p
```

Print line 42.

```text
/^\[dependencies\]$/
```

Find the exact TOML dependencies heading.

```text
/^[[:space:]]*database:/
```

Find a YAML key with optional indentation.

```text
/^fn parse_config/
```

Find a Rust function declaration.

```text
42ka
```

Mark line 42 as `a`.

```text
'a,$n
```

Print from mark `a` through the end of the file.

Do not use a generic pattern such as `/version/`, `/name/`, or `/config/` without first checking whether it matches multiple semantically distinct locations.

### 3. Make one controlled change

Choose the safest edit primitive.

| Intent | Preferred `ed` command |
|---|---|
| Replace a small, unique token or phrase | `s/old/new/` |
| Replace every occurrence on a known single line | `s/old/new/g` |
| Delete one or more verified lines | `d` |
| Insert a new block before a known line | `i` |
| Add a new block after a known line | `a` |
| Replace a complete, verified line range | `c` |
| Move an existing block | `m` |
| Duplicate an existing block | `t` |
| Apply an operation to confirmed matching lines | `g/pattern/command` |

Prefer a direct substitution when the desired change is small and unique:

```text
s/edition = "2021"/edition = "2024"/p
```

The `/p` suffix prints the edited line immediately.

Use insertion or replacement blocks when changing structure:

```text
/^dependencies:/
a
  serde:
    version: "1"
    features: ["derive"]
.
```

Use a standalone `.` line only to exit input mode. It is not part of the file.

After any modification, inspect the affected area immediately:

```text
.,+12n
```

or:

```text
-5,+10n
```

Do not accumulate a sequence of unverified edits.

### 4. Verify the edited buffer

Before saving, verify all of the following:

- The requested content is present.
- The old content is absent where it should be absent.
- No unrelated occurrences were changed.
- Indentation and nesting are correct.
- No duplicate keys, duplicate fields, duplicate imports, or duplicate configuration blocks were unintentionally introduced.
- Syntax delimiters remain balanced where applicable.
- Comments still describe the code or configuration they are adjacent to.
- The file's local ordering conventions are still respected.
- The final region has the expected line structure.

Useful checks:

```text
g/old-text/p
```

No output generally means the old text no longer appears.

```text
g/new-text/p
```

Confirm expected occurrences of the replacement text.

```text
,p
```

Print the whole file when it is small.

```text
,n
```

Print the whole file with line numbers.

```text
,l
```

Print with end-of-line markers and escaped special characters. Use this to detect trailing spaces, tabs, hidden characters, or malformed line breaks.

```text
g/[[:space:]]$/l
```

Find and display lines with trailing whitespace.

Do not interpret "no immediate `ed` error" as proof that the edit is correct.

### 5. Validate with project tools

After verifying the buffer but before finalizing the change, save only when it is appropriate to run validation against the on-disk file. Then run the narrowest relevant validation command available for the project.

For YAML, see [`references/yaml-editing.md`](references/yaml-editing.md).

For Rust, see [`references/rust-editing.md`](references/rust-editing.md). At minimum run `cargo fmt --check` and `cargo check`.

For TOML, JSON, or repository-defined configuration:

- Prefer the project's existing formatter, parser, linter, schema validator, or test suite.
- Follow commands documented in `README`, `CONTRIBUTING`, `Justfile`, `Makefile`, CI configuration, package manifest, or development scripts.
- Run the smallest relevant check first, then expand validation only when warranted.

If validation fails:

1. Read the error carefully.
2. Reopen or re-inspect the affected file.
3. Correct only the defect identified.
4. Reinspect.
5. Re-run the validation.
6. Do not claim success until the relevant check passes or the limitation is clearly stated.

## Format-specific rules

Two formats are high-risk for line-oriented editing and have dedicated references. Consult the relevant one before editing that format:

- **YAML** (indentation- and type-sensitive): [`references/yaml-editing.md`](references/yaml-editing.md)
- **Rust** (delimiter-, attribute-, and import-sensitive): [`references/rust-editing.md`](references/rust-editing.md)

## Safe substitution rules

Use `s` only when all of these are true:

- The target is known and understood.
- The substitution is limited to the correct line or verified range.
- The replacement does not alter comments, strings, examples, generated code, or unrelated symbols unintentionally.
- The delimiter is safely escaped.
- The result is printed and inspected.

Example of a safe targeted edit:

```text
/^version = "1\.2\.3"$/
s/1\.2\.3/1.2.4/p
```

Example of an unsafe broad edit:

```text
,s/version = "1\.2\.3"/version = "1.2.4"/g
```

This may modify unrelated manifests, comments, fixtures, or text embedded in a larger configuration file.

When the target includes `/`, choose another delimiter if supported by the local `ed` implementation, or escape the slashes carefully:

```text
s/old\/path/new\/path/p
```

Use literal display mode when escaping behavior is uncertain:

```text
,l
```

## Global command rules

The `g` command is powerful and potentially destructive:

```text
g/pattern/command
```

It executes `command` for every line matching `pattern`.

Before any destructive global operation:

1. Preview the exact targets:

   ```text
   g/pattern/n
   ```

2. Inspect the surrounding context of each target.
3. Confirm that every match should receive the same change.
4. Use the smallest possible range.
5. Perform the edit.
6. Verify the resulting buffer immediately.

Do not use destructive patterns such as `g/^$/d`, `g/TODO/d`, or `g/debug/d` without confirming that blank lines, TODO comments, or debug references are all intended to be removed in the relevant scope.

For code and YAML, global editing should be exceptional. Prefer narrowly addressed individual edits.

## Insertion and replacement rules

When using `a`, `i`, or `c`:

- Inspect the lines immediately before and after the insertion point.
- Preserve blank-line conventions.
- Preserve indentation.
- Preserve newline-sensitive syntax.
- Finish the input block with a single `.` on its own line.
- Immediately print the changed region with line numbers.

Example: add a Rust import in the correct location:

```text
/^use std::collections::HashMap;$/
a
use std::path::PathBuf;
.
-2,+5n
```

Only do this after checking the project's import ordering. If imports are grouped or alphabetized, insert accordingly or run the project formatter after saving.

Example: replace a YAML block:

```text
/^deployment:/
.,+4c
deployment:
  replicas: 3
  strategy: RollingUpdate
.
-2,+8n
```

Do not use `c` unless the entire replacement range has been verified. It deletes the addressed lines before accepting the new block.

## Undo and recovery

Use `u` immediately when an edit is wrong:

```text
u
```

Then inspect:

```text
.,+10n
```

Treat undo as limited protection, not a substitute for care. Do not rely on repeated undo to navigate a long edit history.

If a command fails or produces an unexpected result:

1. Enable detailed diagnostics with `H`.
2. Inspect the current region and relevant matches.
3. Determine whether the buffer differs from the intended state.
4. Use `u` if the last modifying command caused the problem.
5. Do not write until the buffer is correct.

If the editing session becomes uncertain and the buffer contains no desired work, quit safely without saving with `q`. If the buffer has desired work, do not discard it casually. Inspect it and either correct it or write it only after verification.

## Save and exit policy

Use `w` to write the whole buffer to the file opened by `ed`.

Use `wq` only after:

- The intended changes have been inspected.
- Relevant validation has passed, or validation is impossible and that limitation is explicitly recorded.
- The saved file path is confirmed.
- No unintended buffer modifications remain.

Do not use `W` unless appending to a file is explicitly required.

Do not write a range to a target file unless the task explicitly calls for producing an excerpt or generated fragment:

```text
1,20w excerpt.txt
```

For ordinary source-file editing, write the complete buffer back to its original file.

## Required completion report

After completing an edit, report:

- The file or files changed.
- The exact conceptual change made.
- The validation commands run.
- Whether each validation command passed, failed, or was unavailable.
- Any remaining uncertainty, limitation, or follow-up risk.

Use a concise format such as:

```text
Changed:
- config/service.yaml: Added `replicas: 3` under the existing `deployment` mapping.
- src/config.rs: Added parsing support for the optional replicas setting.

Validated:
- YAML parser: passed.
- cargo fmt --check: passed.
- cargo check: passed.
- cargo test config::tests: passed.

Notes:
- Preserved existing YAML indentation and Rust import ordering.
```

Never state that a change is correct, valid, compiled, formatted, tested, or saved unless you actually verified that result.
