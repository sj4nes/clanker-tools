# `ptx` corpus selection and discovery workflow

## Corpus selection

### Preferred first-pass corpus

Human-authored guidance and design text — stable vocabulary, few implementation details:

```text
README.md  CONTRIBUTING.md  ARCHITECTURE.md
docs/**/*.md  rfcs/**/*.md  adr/**/*.md
CHANGELOG.md  runbooks/**/*.md
examples/**/*.{yaml,yml,toml}
```

### Second-pass corpus

If documentation is insufficient, add carefully selected text-bearing source material:

```text
src/**/*.rs  tests/**/*.rs  crates/**/*.rs
config/**/*.{yaml,yml,toml}
migrations/**/*.sql  scripts/**/*.sh
```

For source files, prefer extraction of comments, doc comments, strings, error messages, headings, or explicitly chosen files over indiscriminately indexing every token. Raw full-source indexing produces noise from common type names, imports, generic parameters, boilerplate, generated bindings, repeated test scaffolding, dependency metadata, long minified strings, vendored code, and machine-generated identifiers.

### Default exclusions

Exclude at least (adapt to the repo — not exhaustive):

```text
.git/ target/ build/ dist/ out/ node_modules/ vendor/ third_party/
coverage/ .next/ .cache/ .venv/ venv/ __pycache__/
*.lock *.min.js *.map *.class *.jar *.o *.a *.so *.dylib *.dll *.exe *.bin
*.png *.jpg *.jpeg *.gif *.pdf *.zip *.tar *.gz *.zst *.sqlite *.db
.env .env.* *.pem *.key id_*
```

### File-type validation

```sh
file --brief --mime-type path/to/file
# or, where GNU grep behavior is acceptable:
grep -Iq . path/to/file
```

Do not index binary files, archives, databases, compiled artifacts, object files, core dumps, private keys, credential files, environment files, production logs with personal/customer/secret data, or files the project identifies as generated, vendored, or sensitive.

## Corpus construction (provenance-preserving)

A bare concatenation loses source locations. Embed file markers:

```sh
corpus_dir=.agent-ptx
mkdir -p "$corpus_dir"

find . -type f \( -name '*.md' -o -name '*.rst' -o -name '*.txt' -o -name '*.adoc' \) \
  -not -path './.git/*' -not -path './target/*' -not -path './node_modules/*' \
  -not -path './vendor/*' -not -path './third_party/*' -print0 |
while IFS= read -r -d '' file; do
  printf '\n===== FILE: %s =====\n' "$file"
  cat -- "$file"
done > "$corpus_dir/docs-corpus.txt"
```

For a more precise source-location corpus, prefix every line with its path and line number:

```sh
find . -type f \( -name '*.md' -o -name '*.rst' -o -name '*.txt' -o -name '*.adoc' \) \
  -not -path './.git/*' -not -path './target/*' -not -path './node_modules/*' \
  -not -path './vendor/*' -not -path './third_party/*' -print0 |
while IFS= read -r -d '' file; do
  nl -ba "$file" | sed "s|^|$file:|"
done > "$corpus_dir/docs-with-locations.txt"

sed -n '1,100p' "$corpus_dir/docs-with-locations.txt"   # test before indexing
```

Always use `find -print0` and a null-safe read loop for repositories with unusual filenames. `ptx` may not preserve every marker conveniently — after discovering a term, return to the original project with `rg`/`grep`.

## Discovery workflow

### 1. Define the discovery question

State it in terms of *terms and concepts*, not presumed implementation details.

- Good: "Discover how this project describes retry behavior, backoff, request failure, and transient errors."
- Weak: "Find the retry manager implementation." (presupposes a "retry manager" exists; invites false negatives)

Define: scope (docs / source / both); target concepts; exact word candidates; synonyms and morphological variants; desired output (relevant files, terminology map, likely entry points, or source locations).

### 2. Create a term family

`ptx` works best with exact words, so build a deliberate search family. Examples:

- **retry:** retry retries retried retrying backoff delay timeout timeouts transient temporary failure failures attempt attempts
- **caching:** cache caches cached caching invalidate invalidation stale freshness ttl expiry expiration memoize memoization
- **authentication:** auth authentication authenticate authenticated authorization authorize authorized credential credentials token tokens session sessions login logout identity principal permission permissions role roles scope scopes
- **configuration:** config configuration configure configured setting settings option options environment env flag flags parameter parameters default defaults override overrides

Add project-specific naming variants after early inspection (`RetryPolicy retry_policy retry-policy retryPolicy retry_count`). Do not expect one form to find the others automatically.

### 3. Build a narrow first-pass index

```sh
ptx "$corpus_dir/docs-corpus.txt" > "$corpus_dir/docs.ptx"
sed -n '1,200p' "$corpus_dir/docs.ptx"
```

Do not immediately index all repository files. If the result is too large or noisy: reduce the corpus; index one area at a time; exclude changelogs or generated docs; create separate indexes by domain (architecture, operations, API, configuration, migrations, tests); use a verified stop-word list. Avoid solving noise by silently excluding terms that may matter.

### 4. Search the index

Literal matching first (`-F` = literal, not regex):

```sh
grep -inF -- 'retry' "$corpus_dir/docs.ptx"

for term in retry retries retried retrying backoff timeout transient; do
  printf '\n=== %s ===\n' "$term"
  grep -inF -- "$term" "$corpus_dir/docs.ptx" || true
done
```

A match in the `ptx` index is a context clue, not a source location. When output contains a promising phrase, search the original corpus and repository:

```sh
rg -n -i -C 4 -- 'retry|backoff|transient' README.md docs src tests
rg -n -F -C 4 -- 'RetryPolicy' .
```

### 5. Inspect source context

For every promising lead: find the source occurrence with line numbers; print nearby lines; identify the containing document / config block / function / type / module / test; determine whether it is active code, documentation, an example, a comment, a deprecated path, a fixture, or generated material; follow references with a project-aware tool; record the conclusion with its original source location.

```sh
rg -n -C 8 -- 'backoff' src tests docs
sed -n '120,190p' src/client/retry.rs
```

Do not infer that a word in a README means the mechanism currently exists in code.

### 6. Expand only when justified

If doc-level discovery reveals terms like `RetryPolicy` or `exponential backoff`, expand into a *targeted* source corpus — files already identified as likely relevant, not every token in the repo:

```sh
find src crates tests -type f -name '*.rs' -print0 |
xargs -0 grep -IlE 'retry|backoff|timeout|transient|RetryPolicy' |
sort -u > "$corpus_dir/retry-source-files.txt"
nl -ba "$corpus_dir/retry-source-files.txt"

while IFS= read -r file; do
  printf '\n===== FILE: %s =====\n' "$file"
  nl -ba "$file"
done < "$corpus_dir/retry-source-files.txt" > "$corpus_dir/retry-source-corpus.txt"

ptx "$corpus_dir/retry-source-corpus.txt" > "$corpus_dir/retry-source.ptx"
```

This makes `ptx` a second-order discovery tool: it maps the vocabulary around already-likely-relevant files instead of flooding the index.
