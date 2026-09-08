# Verifying the `typst` skill

## What verification means for this skill

`typst` wraps a real CLI, so verification runs the mechanics `SKILL.md`
prescribes against the actual `typst` binary in a throwaway directory and
asserts each behaves as claimed — including the negative contrasts (a broken
cross-reference *must* fail the build; pasted LaTeX math *must not* compile).

## Case

The shipped [`../templates/`](../templates/) tree — one `manuscript.typ`
entrypoint, a `preamble.typ` of `#set`/`#show` rules, two `#include`-d section
files, a labelled figure and table, native math, and a one-entry
`references.bib` — plus four tiny synthetic documents for the isolated checks.
Small, deterministic, no network (no `@preview` imports).

## Run

```sh
sh skills/typst/verification/run.sh
```

`typst 0.15.1`, macOS `/bin/sh`. Wall time a few seconds.

## What each step demonstrates

| SKILL claim | Prescribed check | Result |
|---|---|---|
| §2 scaffold / one entrypoint | the template's split-body `#include` entrypoint compiles to a PDF | PASS |
| §6 verify by page count | it renders ≥ 2 pages (body split + back matter) | PASS — 4 pages |
| §5 wire references / §6 verify | an unresolved `@eq:does-not-exist` is a **hard compile error**, not a silent blank | PASS — non-zero exit, diagnostic names the reference |
| principle: translate math by meaning | `$ \frac{a}{b} $` (LaTeX) **fails to compile**; `$ a / b $` and `$ frac(a, b) $` (native) compile | PASS both |
| principle: separate content from formatting | editing one line of a preamble `#show heading` rule changes the semantic-heading document's output; the **same edit leaves an inline-`#text`-styled document byte-identical** | PASS both — the anti-pattern provably isolates styling from the preamble |
| principle: assets/fonts self-contained; §6 fonts loaded | the resolved font set is path-dependent — `--ignore-system-fonts` sees far fewer families (4 embedded vs 496) | PASS |

## Findings folded back into the skill

- `typst` does **not** create the output's parent directory (`build/`) — it
  errors with `failed to write PDF file`. The verification `mkdir -p build`
  first; the SKILL's project layout lists `build/` as a real directory to
  create, and the CLI reference notes output paths are not auto-created.
- `--diagnostic-format` is rejected before the subcommand
  (`typst --diagnostic-format short compile …` errors); it must follow
  `compile`/`watch`. Recorded in `references/cli-reference.md`.
- Equation cross-references require `#set math.equation(numbering: …)` — without
  it, `@eq:…` fails with "cannot reference equation without numbering". The
  template preamble sets it; noted in `references/authoring-patterns.md`.
- `typst 0.15.1` has no `query` subcommand. The CLI reference says so explicitly.

## The gates are necessary, not sufficient

The run confirms mechanics (the entrypoint compiles, broken refs fail, LaTeX
math fails, a `#show` rule propagates where inline styling does not, fonts are
path-dependent). It does not check judgement: whether Typst is the right medium
for the deliverable, whether the layout *looks* right, whether a migration
preserved meaning, or whether the preamble matches a target template. Those stay
with the agent and the SKILL body — which is why the completion report requires
looking at the compiled PDF.
