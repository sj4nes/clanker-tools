# `ptx` search protocol, language notes, and command patterns

## Exact-word search protocol

Explicitly account for the ways a concept may be written.

### Word forms

For `cache`, search `cache caches cached caching`. Do not assume `cache` finds the others.

### Case variants

For `retry`, search `retry Retry RETRY RetryPolicy`. Test whether the local `ptx` normalizes case before deciding whether separate queries are needed.

### Separator variants

For the phrase `cache key`, search `cache key cache_key cache-key cacheKey CacheKey`. Because `ptx` may tokenize separators, a word-level match identifies nearby vocabulary but not a specific identifier. Confirm identifier forms with literal search:

```sh
rg -n -F -- 'cache_key' .
rg -n -F -- 'cache-key' .
rg -n -F -- 'cacheKey' .
rg -n -F -- 'CacheKey' .
```

### Stems and abbreviations

For `authentication`, also search `auth authenticate authenticated authorization authorize authorized oauth oidc jwt token session credential`. Absence of `authentication` is not evidence that authentication is absent — the project may use `auth`, `login`, `identity`, a protocol acronym, or a vendor name.

### Synonyms

For "deployment", also consider `deploy deployment release rollout publish promotion staging production canary activate provision install`. `ptx` does not understand semantic equivalence, so synonym expansion must be explicit.

## Rust-specific use

Use `ptx` primarily on: crate-level documentation, module documentation, Rust doc comments, README and architecture documents, error strings, test names and descriptions, examples, configuration documentation. **Do not use `ptx` as a Rust symbol index.**

Good sequence:

```sh
rg -n -i --glob '*.md' --glob '*.rs' 'retry|backoff|transient|timeout' \
  README.md docs src crates tests
# → build a targeted corpus from the resulting files, then:
ptx .agent-ptx/retry-source-corpus.txt > .agent-ptx/retry-source.ptx
grep -inF -- 'backoff' .agent-ptx/retry-source.ptx
# → return to code-aware inspection:
rg -n -C 10 -- 'RetryPolicy|retry|backoff' src crates tests
cargo test retry
```

The final inspection must establish source-level facts; `ptx` merely accelerates the path from vague concept to likely files and terminology.

### Identifier limitations

Rust identifiers use `snake_case`, `CamelCase`, `SCREAMING_SNAKE_CASE` — not reliably searchable through word-permutation indexing as complete semantic units. `struct ExponentialBackoffPolicy;` might make `backoff` discoverable, but `ExponentialBackoffPolicy` itself may not be an exact `ptx` word. Use:

```sh
rg -n -F -- 'ExponentialBackoffPolicy' .
rg -n -F -- 'exponential_backoff_policy' .
```

Do not claim a Rust type does not exist merely because it is absent from a `ptx` index.

## YAML and configuration use

Use `ptx` on YAML to discover human-readable keys, comments, descriptions, values, and documentation vocabulary — **not** to prove hierarchical structure. `ptx` cannot safely establish whether `max_attempts` belongs under `retry`, whether a key is valid for the deployed schema, whether a value is overridden elsewhere, whether anchors/aliases/merges/templates/env interpolation alter behavior, or whether a setting is active in the target environment.

After finding a term:

```sh
rg -n -C 6 -- 'retry|backoff|max_attempts' config deploy charts
```

Then validate with the project's schema checker, parser, linter, test suite, or deployment tooling.

## Index quality controls

### Noise reduction

Prefer: documentation-first indexing; separate indexes per project area; carefully selected source directories; relevant extensions only; exclusion of generated/vendored material; human-written strings and comments over full source token streams; domain-specific term families.

Avoid: indexing all dependencies; indexing build artifacts; indexing compressed/binary content; combining unrelated repositories into one unmarked corpus; treating a full-codebase index as a replacement for source navigation.

### Stop words

Stop words can make an index more readable but can also hide domain-relevant terms. Do not remove terms such as `error request response config file key user token test build service version` without checking whether they are central to the discovery question. Keep any stop-word file under recorded control:

```text
# ptx-stopwords.txt
a
an
and
the
of
to
in
for
with
```

Before using implementation-specific options such as `-W`, `-f`, `-i`, `-o`, or `-r`, confirm their exact meaning via `ptx --help` / `man ptx`. Do not copy options from an unrelated GNU/Linux environment into a different Unix implementation without verification.

### Separate indexes by role

```text
.agent-ptx/
  docs-corpus.txt          docs.ptx
  architecture-corpus.txt  architecture.ptx
  config-corpus.txt        config.ptx
  retry-source-corpus.txt  retry-source.ptx
```

This prevents an operational term from being buried among source-code boilerplate and makes provenance and cleanup easier.

## Command patterns

```sh
# Minimal indexing
ptx input.txt > index.ptx

# Inspect a narrow index area
grep -inF -- 'authentication' index.ptx

# Search a word family
for term in auth authentication authorization token session credential; do
  printf '\n=== %s ===\n' "$term"
  grep -inF -- "$term" index.ptx || true
done

# Build a documentation corpus (verify every listed root exists first)
mkdir -p .agent-ptx
find README.md docs adr rfcs -type f \
  \( -name '*.md' -o -name '*.rst' -o -name '*.txt' -o -name '*.adoc' \) -print0 2>/dev/null |
while IFS= read -r -d '' file; do
  printf '\n===== FILE: %s =====\n' "$file"
  cat -- "$file"
done > .agent-ptx/docs-corpus.txt
ptx .agent-ptx/docs-corpus.txt > .agent-ptx/docs.ptx

# Search source after a ptx lead
rg -n -i -C 5 -- 'authentication|authorization|credential|token|session' README.md docs src tests

# Preserve line-oriented provenance
find docs -type f -name '*.md' -print0 |
while IFS= read -r -d '' file; do
  nl -ba "$file" | sed "s|^|$file:|"
done > .agent-ptx/docs-located.txt
ptx .agent-ptx/docs-located.txt > .agent-ptx/docs-located.ptx
```

Treat output line-number prefixes as helpers only. Confirm the final location with `rg -n` or direct inspection, because `ptx` may rearrange visible text.
