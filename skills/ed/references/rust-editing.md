# Rust editing rules for `ed`

Rust is structurally sensitive to braces, delimiters, lifetimes, attributes, macros, imports, ownership semantics, and formatting conventions. Make changes in context, not by isolated token replacement unless the match is clearly unique.

## Inspect semantic boundaries

Before changing a function, `impl`, struct, enum, trait, module, test, macro invocation, or attribute, inspect enough surrounding context to understand its scope:

```text
/^fn target_function/
-5,+40n
```

For an implementation block:

```text
/^impl[[:space:]].*TargetType/
.,+80n
```

For a test module:

```text
/^#[[]cfg(test)[]]/
.,+100n
```

If a region is longer than the display range, continue in controlled chunks. Do not assume the closing brace belongs to the currently visible block without inspecting enough context.

## Respect formatting and idioms

Match local Rust style:

- Four-space indentation unless the repository uses something else.
- Existing import grouping and ordering.
- Existing use of `crate::`, `super::`, `self::`, absolute paths, and aliases.
- Existing error-handling approach: `Result`, `?`, `anyhow`, `thiserror`, custom enums, panics, or assertions.
- Existing async style, feature gates, conditional compilation, and macro patterns.
- Existing documentation and test conventions.

Do not reformat unrelated code manually. Let `cargo fmt` handle formatting when appropriate, but first ensure that formatting is expected and does not create an unreviewably broad diff.

## Avoid unsafe global changes

Do not issue commands like:

```text
,s/foo/bar/g
```

until you have established that every occurrence should change. In Rust, an identifier can appear in definitions, call sites, imports, tests, documentation examples, string literals, error messages, macro invocations, feature flags, and conditional compilation attributes.

Instead, inspect candidates:

```text
g/\<old_name\>/n
```

Then make targeted edits at individual verified locations or within a tightly bounded range.

If word-boundary syntax is not portable in the active `ed` implementation, use stronger surrounding context in the regular expression or inspect each candidate manually.

## Maintain syntax integrity

After an edit, inspect the immediate structure for:

- Balanced `{}`, `()`, and `[]`.
- Correct commas in argument lists, arrays, struct literals, enum variants, match arms, and `use` groups.
- Correct semicolon presence or absence.
- Valid `match` arms and trailing commas, following local style.
- Correct visibility markers: `pub`, `pub(crate)`, `pub(super)`.
- Correct attribute placement, including `#[cfg(...)]`, `#[derive(...)]`, and `#[allow(...)]`.
- Correct lifetime, generic, and trait-bound syntax.
- Correct use of `await`, `?`, `return`, and ownership-sensitive operations.
- No newly unused imports, variables, fields, or functions.

## Validation

Always run, at minimum when applicable:

```sh
cargo fmt --check
cargo check
```

For a targeted package in a workspace:

```sh
cargo check -p package_name
```

Run tests if the edit changes behavior, tests, public APIs, parsing, business logic, concurrency, serialization, or error handling:

```sh
cargo test
cargo test test_name
```

Use scoped commands where the repository is large, but do not substitute a narrow check for a broader one if the requested change clearly crosses package boundaries.
