# ste-check -- advisory Simplified Technical English checker

A self-contained `awk` script plus a POSIX `sh` wrapper. No dependencies beyond
a POSIX `awk` (tested on macOS `awk` 20200816 and `gawk`).

## What it does

It flags surface patterns that STE discipline tells you to inspect. It cannot
read meaning, so **every finding is a candidate for human review, not an error**.
Treat it like `ptx`: a discovery aid. It never rewrites your text.

| Tag | What it flags | Confidence |
|---|---|---|
| `LENGTH` | Sentence over 20 words (procedural) or 25 (descriptive) | high |
| `VAGUE-VERB` | `handle`, `manage`, `ensure`, `process`, `leverage`, `robust`, ... | high |
| `PASSIVE?` | be-verb + past participle | low -- false positives expected |
| `MULTI-ACTION?` | one sentence joins actions with `, and` / `then` | medium |
| `CONDITION-LAST` | an `if` / `when` / `unless` clause trails the command | medium |
| `SYNONYM-DRIFT` | one operation is written with two or more verbs (`check` vs `verify` vs `confirm`) | medium |

## Use

```sh
./run.sh path/to/instructions.md
./run.sh --strict --canon "verify,delete,create" runbook.md   # exit 1 on any finding
./run.sh --max 18 --hard 22 prompt.txt                        # tighten thresholds
```

One file per invocation. Pass several and each is checked in turn; `--strict`
makes the wrapper exit non-zero if any file produced a finding, for CI use.

With `--canon`, you declare the verbs you have standardized on. The checker then
flags every *other* member of the same synonym group as drift, at the exact line.
Without `--canon`, it reports drift once per document in the summary.

## What it skips

Fenced code blocks, ATX headings, Markdown table rows, HTML comment lines. It
strips list markers, inline code spans, and link syntax before checking, so list
items -- where instructions usually live -- are checked.

## Self-test

```sh
./test.sh
```

Runs `ste-check.awk` against `fixtures/` with known expected findings: 18
assertions covering every tag (positive and negative cases), the code-fence
skip, the `--canon` per-line drift flags, and the `--strict` exit codes. No
network. Exit 0 if all pass.

## Known limits

- Sentence splitting is naive: `e.g.`, `i.e.`, `vs.`, and `No. 5` over-split.
- `PASSIVE?` matches any `is/are/was/were/be/been/being` + `-ed`/`-en` word,
  including legitimate uses ("the file is deleted" as a state description).
- It does not know procedural from descriptive text; it reports both length
  tiers and lets you decide which applies.
- Phrase-level vagueness ("make sure", "as needed", "if appropriate") is only
  partly covered.

## Scaling up

For a maintained CI-grade controlled-language linter, use
[Vale](https://vale.sh) (MIT, Go). Vale is syntax-aware and rule-driven, but
there is **no canonical ASD-STE100 style** in its registry -- you would curate
the word lists and rules yourself, the same lists this script bundles. This
script exists so the skill has a zero-install check; Vale is the upgrade path.
