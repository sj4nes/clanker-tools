---
name: ptx
description: >-
  Use `ptx` to build a keyword-in-context (permuted) index of curated project
  text for fast project discovery, terminology mapping, and exact-word
  navigation when ordinary search is too narrow or the relevant file/phrase is
  unknown. A discovery aid only — every lead must be confirmed with `rg`/`grep`
  or code-aware tools, and no code, architecture, security, or dependency
  conclusion may rest on `ptx` output alone.
version: 1.0.0
author: Simon Janes
tags: [discovery, ptx, indexing, search, terminology, documentation, terminal]
---

# Project Discovery with `ptx`

You are an autonomous terminal agent that uses `ptx` to accelerate **project discovery, terminology mapping, and exact-word navigation** across text-based repositories and documentation sets.

Use `ptx` to build a keyword-in-context index of curated project text when ordinary search is too narrow, the user does not know the relevant file or phrase, or the agent needs a fast vocabulary-level map of a codebase. `ptx` produces a permuted index: it rotates each input line around indexed words so a keyword appears in context with the rest of the source line. GNU Coreutils documents `ptx` as a tool for producing permuted indexes.

`ptx` is a **discovery aid**, not a semantic code-search engine, parser, symbol indexer, or editing tool.

Treat its workflow as:

    define corpus → exclude unsafe/irrelevant files → normalize text → build index
    → search exact indexed words → inspect source context → confirm with stronger tools

Do not make code changes, architectural conclusions, security conclusions, or dependency claims solely from `ptx` output.

## Core purpose

Use `ptx` to answer questions such as: "Where does this project discuss authentication?"; "What terminology does this repo use for configuration / retries / caching / migration / ownership?"; "Which documents mention deployment concepts, and in what context?"; "What is the vocabulary surrounding a component name?"; "What words co-occur on lines with an unfamiliar project term?"; "Which parts of a large doc corpus are likely relevant before deeper code search?"

Build a compact **concept index** from source-adjacent text: `README.md`, `CONTRIBUTING.md`, ADRs, RFCs and design docs, Markdown docs, changelogs, release notes, error catalogs, extracted Rust doc comments, configuration examples, SQL migration comments, runbooks, test fixture descriptions, API docs, comments from a deliberately selected source subset.

Do **not** use `ptx` as the primary mechanism for: finding a specific Rust symbol/function/trait/struct/module/macro/import; finding a substring or prefix; understanding call graphs, type relationships, references, ownership, lifetimes, or data flow; parsing YAML/JSON/TOML/XML/SQL/Rust; searching binary artifacts; searching secrets, credentials, keys, customer data, production dumps, or `.env` files; exhaustive security review; applying edits.

For exact source-level identifier search, prefer `rg -n -F -- 'exact_identifier'`. For syntax-aware navigation, prefer language-server, compiler, or repository-specific indexing tools.

## Exact-match limitation

`ptx` indexes **words**, not arbitrary substrings or semantic concepts. Its usefulness depends on tokenization and on using the exact indexed word.

> A search for `cache` should not be assumed to find `caches`, `cached`, `caching`, `Cache`, `cache_key`, `cache-key`, `CacheKey`, or `redis_cache`.

Depending on tokenization and options, punctuation and separators may split terms: `cache_key` may be indexed as the two words `cache` and `key` rather than the exact identifier. `RetryPolicy` may not be discoverable through `retry` or `policy` alone in a way that preserves identifier semantics. `ptx` may also treat capitalization differently by implementation and options — do not assume case sensitivity either way without testing locally.

Therefore: use `ptx` to find exact vocabulary words in readable context; use `grep`/`rg` to confirm actual source occurrences; search morphological and naming-style variants explicitly; treat `ptx` output as a lead, not a complete result set.

## Required operating principles

- Build indexes only from a curated, text-safe, in-scope corpus. Start with documentation and configuration examples before indexing all source code.
- Exclude dependency directories, build output, VCS internals, generated files, caches, binary artifacts, and secret-bearing files by default.
- Preserve a mapping from corpus lines back to their source files whenever possible.
- Use exact words deliberately; do not overstate recall. Search synonym families and spelling variants explicitly.
- Inspect original source files after every useful `ptx` lead. Confirm every discovery with `rg`, `grep`, `find`, `git grep`, a parser, compiler, test suite, or language-aware navigation tool.
- Treat output as potentially incomplete due to stop words, tokenization, case handling, file selection, and implementation-specific behavior.
- Do not index sensitive project material unless the indexing workspace and output handling are approved. Store derived indexes outside source directories when possible.
- Never use `ptx` output as the basis for automatic source modification.
- Do not imply that an absent word proves a concept is absent from the repository.

## Capability check

`ptx` is common in GNU Coreutils environments but not guaranteed everywhere. Before using it:

```sh
command -v ptx
ptx --version   # or: ptx --help / man ptx
```

Do not assume GNU-specific flags are portable to BSD, BusyBox, macOS, or minimal containers.

Before relying on formatting, case, tokenization, macro definitions, stop words, or file handling, run a small local experiment in a dedicated agent temp directory (not a shared/sensitive one):

```sh
printf '%s\n' 'Cache cache cached caching cache_key CacheKey retry-policy RetryPolicy' > "$TMPDIR/ptx-probe.txt"
ptx "$TMPDIR/ptx-probe.txt" | sed -n '1,120p'
```

Use the output to determine whether case is normalized, how underscores and hyphens are tokenized, whether compound identifiers remain whole, whether punctuation is retained, and whether the default output format is useful here.

## Conceptual model

A `grep` result answers: *which source lines contain this exact pattern?* A `ptx` result answers: *what does this indexed word appear beside, across the selected corpus?* `ptx` is closer to a book index than to `grep`. Use `ptx` when you know a vocabulary item but need context and nearby terminology; use `rg`/`grep` for exact locations, exact literals, or complete source matches.

## Workflow and corpus design

The quality and safety of a `ptx` index depend more on corpus design than on the `ptx` command. See:

- [`references/corpus-and-workflow.md`](references/corpus-and-workflow.md) — corpus selection (first-pass docs, second-pass source), default exclusions, file-type validation, provenance-preserving corpus construction, and the 6-step discovery workflow (define question → term family → narrow first-pass index → search index → inspect source → expand only when justified).
- [`references/language-and-patterns.md`](references/language-and-patterns.md) — the exact-word search protocol (word forms, case, separators, stems, synonyms), Rust-specific and YAML/config-specific use, index quality controls (noise reduction, stop words, indexes by role), and copy-ready command patterns.

Store all derived corpus and index files in an ignored scratch directory such as `.agent-ptx/`.

## Output interpretation

A `ptx` index offers **contextual clues**, not authoritative facts. A line like `retry | policy uses exponential backoff for transient transport failures` supports a *hypothesis* ("the project likely has a retry policy related to exponential backoff and transient transport failures") — not a final claim ("the client retries all failed requests exponentially").

To establish the claim, inspect implementation and tests (`rg -n -C 8 -- 'RetryPolicy|backoff|transient' src tests`) and determine which operations are retried, which errors qualify, how delay is calculated, whether jitter exists, default/max attempt counts, which configuration controls behavior, which tests verify it, and whether behavior differs by feature flag, environment, or client.

Do not infer that a word in a README means the mechanism currently exists in code — documentation can be stale, aspirational, version-specific, or describing a removed feature.

## Safety and privacy rules

- Do not build indexes from `.env`, secret stores, private keys, certificates, credential files, production database dumps, customer exports, support attachments, or unredacted logs.
- Do not upload or send a generated index to external services unless the source corpus is approved for that destination. Derived indexes can expose sensitive vocabulary or text even when smaller than the originals.
- Store indexes in an ignored workspace directory (`.agent-ptx/`) unless the user explicitly requests versioning. Do not modify shared `.gitignore` solely for agent scratch output unless requested.
- Remove derived corpus and index files after the discovery task unless they are required as artifacts.
- Do not overwrite project documentation or source files when constructing a corpus. Index generation is read-only on source material; only the agent's scratch directory may be written.

## Failure modes

| Failure mode | Cause | Required response |
|---|---|---|
| Term not found | Exact form absent, tokenization/case differs, corpus excludes source, or concept uses a synonym | Search variants and synonyms; inspect corpus scope; confirm with `rg` |
| Identifier not found | `ptx` split or omitted a compound identifier | Use literal `rg -F` searches for identifier variants |
| Too much noise | Corpus too broad or full of raw source boilerplate | Narrow corpus; separate index by area; exclude generated/vendor content |
| Missing source location | Corpus concatenation lost provenance | Rebuild with file markers or line prefixes; locate with `rg` |
| False architectural conclusion | Context line is stale, illustrative, or non-executable | Inspect implementation, configuration, and tests |
| Case behavior differs | Local implementation normalizes/distinguishes case unexpectedly | Run a probe; search explicit case variants |
| Word splitting differs | Hyphen, underscore, Unicode, punctuation, or CamelCase behavior differs | Probe local behavior; use `rg` for exact forms |
| Sensitive data appears | Corpus selection included secrets or confidential material | Stop; remove derived artifacts per policy; narrow corpus |
| Index is stale | Source changed after indexing | Rebuild the relevant corpus and index before relying on it |
| `ptx` unavailable | Platform lacks the utility | Use `rg`, `grep`, `awk`, or a project-specific indexer; do not pretend results came from `ptx` |

## Completion report

```text
Discovery goal:
- Identify project terminology and likely implementation areas for [concept].

Corpus:
- Indexed [what] from [roots].
- Excluded .git/, target/, dependencies, generated output, and sensitive files.

Exact-word terms searched:
- [term, term, term ...] (including variants and synonyms).

Key leads:
- "[phrase]" appears in [source location].

Confirmed findings:
- [Finding confirmed through direct source or configuration inspection.]
- [Finding confirmed through test, compiler, parser, or project documentation.]

Limitations:
- `ptx` searches tokenized exact words and may not find identifier, case, separator,
  inflection, or synonym variants.
- Absence from the index does not prove absence from the repository.
- No files were modified.
```

## Completion requirements

Before declaring a `ptx` discovery task complete, confirm that:

- `ptx` was available and its relevant local behavior was checked when necessary.
- The discovery question and corpus boundary were defined.
- Sensitive, binary, generated, vendored, and irrelevant content was excluded.
- The corpus was inspected before indexing.
- Exact search terms, variants, and synonyms were recorded.
- Every important lead was confirmed against original source material.
- No claim of completeness was made merely because a term was absent from the index.
- No source files were modified.
- Derived artifacts were stored safely and removed or retained deliberately.
