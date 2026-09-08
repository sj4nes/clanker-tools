# Typst CLI reference

Verified against `typst 0.15.1`. Run `typst help <command>` for the exact flags
of the installed version — options change between releases.

## Commands

| Command | Alias | Purpose |
|---|---|---|
| `typst compile <IN> [OUT]` | `c` | compile once to PDF / PNG / SVG / HTML |
| `typst watch <IN> [OUT]` | `w` | recompile on every change to the file or a dependency |
| `typst init <TEMPLATE> [DIR]` | | scaffold a project from a Universe template |
| `typst fonts` | | list discovered fonts (system + `--font-path`) |
| `typst eval <CODE>` | | evaluate a snippet of Typst code |
| `typst info` | | debugging info about the Typst build |
| `typst completions <SHELL>` | | shell completion script |

## `compile` / `watch`

```sh
typst compile manuscript.typ                       # -> manuscript.pdf (next to input)
typst compile manuscript.typ build/manuscript.pdf  # explicit output
typst watch  manuscript.typ build/manuscript.pdf   # drafting loop
```

Key options (apply to both `compile` and `watch`):

| Flag | Use |
|---|---|
| `-f, --format <pdf\|png\|svg\|html>` | force output format (else inferred from the output extension) |
| `--root <DIR>` | project root for absolute (`/…`) paths; defaults to the input file's directory. `[env: TYPST_ROOT]` |
| `--font-path <DIR>` | extra directory searched recursively for fonts; repeatable / `:`-separated. `[env: TYPST_FONT_PATHS]` |
| `--ignore-system-fonts` | only use `--font-path` + embedded fonts — for reproducible builds |
| `--input <key=value>` | string pair readable in the document via `sys.inputs.key` |
| `--diagnostic-format <human\|short>` | `short` = one-line errors, easier to scan/grep. **Must follow `compile`/`watch`**, not precede it |
| `--pages <SPEC>` | export a subset, e.g. `2,3-6,8-` (physical page numbers, 1-indexed) |
| `--ppi <N>` | PNG resolution, default 144 |
| `--pdf-standard <a-2b\|a-3b\|ua-1\|…>` | enforce a PDF/A or PDF/UA conformance level |
| `--open [VIEWER]` | open the output in the default viewer (or a named program) after compiling |
| `--timings <OUT.json>` | write a compilation performance trace |
| `--deps <PATH> [--deps-format make\|json\|zero]` | write the dependency list (for build systems) |
| `--creation-timestamp <UNIX>` | fix the PDF creation date. `[env: SOURCE_DATE_EPOCH]` — set for byte-reproducible PDFs |
| `-j, --jobs <N>` | parallelism; `1` disables it |

`watch`-only: `--no-serve`, `--no-reload`, `--port <N>` control the live HTTP
server used for HTML export.

### Per-page raster for inspection

```sh
typst compile manuscript.typ "build/page-{p}.png" --ppi 200
# multi-page PNG/SVG output REQUIRES a template: {p} page no, {0p} zero-padded, {t} total
typst compile manuscript.typ "build/p-{0p}-of-{t}.svg"
```

Use this to actually look at what rendered when you cannot open the PDF directly.

### stdin / stdout

```sh
cat manuscript.typ | typst compile - build/out.pdf     # read source from stdin
typst compile manuscript.typ - > build/out.pdf          # write PDF to stdout
```

## `init`

```sh
typst init @preview/charged-ieee:0.1.4 my-paper     # scaffold from a pinned template
typst init @preview/basic-resume:1.5.1 my-cv
```

Touches the package registry on first use (network). Browse templates at
<https://typst.app/universe/>.

## `fonts`

```sh
typst fonts                          # every discovered family
typst fonts --font-path assets/fonts # include a project font dir
typst fonts --ignore-system-fonts --font-path assets/fonts   # exactly what a reproducible build sees
```

A font family named in `#set text(font: …)` that is **not** in this list is
silently substituted — always cross-check after setting fonts.

## Environment variables

| Variable | Effect |
|---|---|
| `TYPST_ROOT` | default `--root` |
| `TYPST_FONT_PATHS` | default `--font-path` (`:`-separated) |
| `TYPST_PACKAGE_PATH` | local package directory |
| `TYPST_PACKAGE_CACHE_PATH` | downloaded-package cache location |
| `SOURCE_DATE_EPOCH` | PDF creation timestamp (reproducible builds) |
| `TYPST_CERT` | custom CA certificate for registry requests |
| `TYPST_FEATURES` | enable in-development features |

## Project layout rationale

```text
my-doc/
├── manuscript.typ     # the ONLY argument you ever pass to compile/watch
├── preamble.typ       # #import-ed by manuscript.typ
├── sections/*.typ     # #include-d
├── figures/*          # local files; Typst never fetches URLs
├── references.bib
├── assets/fonts/*     # bundled faces -> --font-path assets/fonts
└── build/             # output; add to .gitignore
```

- **One entrypoint** means one dependency graph and one command. Paths inside
  the document resolve relative to the file that uses them; keeping the
  entrypoint at the root keeps `figures/x.png` meaning the same thing everywhere.
- `--root` only matters if the document uses absolute paths (`/figures/x.png`);
  prefer relative paths and you can ignore it.
- Compile from a **fresh checkout** before calling a document done — that catches
  an image or font that only exists on your machine.

## CI shape

```yaml
- uses: typst-community/setup-typst@<pinned-sha>
  with:
    typst-version: 0.15.1          # pin exactly
- run: typst fonts --font-path assets/fonts
- run: |
    typst compile --diagnostic-format short \
      --font-path assets/fonts \
      --ignore-system-fonts \
      manuscript.typ build/manuscript.pdf
- uses: actions/upload-artifact@<pinned-sha>
  with: { name: manuscript-pdf, path: build/manuscript.pdf }
```

Pin the Typst version and every `@preview/…` package version. With
`--ignore-system-fonts` + bundled `assets/fonts/`, the CI PDF matches the local
one; with `SOURCE_DATE_EPOCH` set, it is byte-identical run to run.

## Notes on version differences

- `typst 0.15.1` has **no `query` subcommand** (present in some other builds via
  `typst query` for extracting metadata) — do not rely on it without checking
  `typst help`.
- `--diagnostic-format` is a subcommand option (`typst compile --diagnostic-format
  short …`), not a global one — placing it before `compile` errors.
- PDF tagging for accessibility is on by default in 0.15.1; `--no-pdf-tags`
  disables it (smaller output, less accessible).

Source: `typst help`, `typst help compile`, `typst help watch` (0.15.1);
<https://typst.app/docs/>.
