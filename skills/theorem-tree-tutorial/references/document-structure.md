# Tutorial document skeleton (theorem-tree)

The generated file is plain Markdown, runnable with `upmd`. Standard shape,
following `skills/math-real-analysis/tutorial/hole-in-the-rationals.md`:

```markdown
# <Tutorial title>

> Generated from the `<capsule>` capsule (Release X.Y) with the
> `theorem-tree-tutorial` skill. The mathematics, the prerequisite order, and
> every calculation and proof come from that capsule —
> `validation/proof-checks.lean` and `validation/instance-checks.bc` in
> particular.

<one paragraph: the narrative hook. What single object or question the whole
tutorial follows — one sequence in two number systems, one probability model
from the axioms up, one inequality applied four ways.>

## How to run this

Install [`upmd`](https://upmd.dev), then from the repository root:

- `upmd <path>.md` — the interactive walk (needs a real terminal).
- `upmd --ci --all <path>.md` — run every check top to bottom (the gate).
- `upmd --ci -b capstone <path>.md` — the final verdict and everything it needs.

Each section ends with a block you run; blocks `deps:` earlier ones in the same
partial order as the capsule's dependency graph, so `upmd --ci -b chk_<x>` runs
one check with its whole chain.

The `lean_<…>` blocks call the Lean 4 kernel through a shell wrapper (`upmd` has
no native Lean runner). They need `lean` on your `PATH`; if it is missing they
print `SKIP` and still exit 0, so the tutorial goes green without it.

## What you need first

<one paragraph: the primitive concepts assumed — sets and functions, the ε–N
idiom, rational arithmetic, whatever the audience already has — and a pointer to
the prerequisite capsule tutorial(s). For a probability tutorial: "σ-algebras
and the abstract integral, from `math-sets-functions-cardinality` and
`math-real-analysis`; here they are cited, not built.">

<if the capsule tags results with a grade, one sentence naming it: "Every result
below carries a **convergence-mode tag** — the mode it delivers, which is the
hypothesis-sensitive fact people get wrong.">

---

## 0. Setup

<one sentence: these values feed every calculation below>

```bash [name:setup]
export SEED=2
export SQRT2="$(echo 'scale=60; sqrt(2)' | bc -l)"
export EPS="$(echo 'scale=60; 1/10^12' | bc -l)"
echo "seed, reference constant, tolerance loaded"
```

## 1. <first concept, in tsort order>

<~120–220 words from the YAML entry: the statement (quoted once, on its own
line), typed symbols, hypotheses named as nodes, the grade if it carries one,
the one dropped-hypothesis failure>

    <statement / definition on its own line>

```bash [name:chk_<node1>, deps:setup]
<the capsule's instance check / specialization for this node; labelled result>
```

<one line: what the output means>

## 2. <first theorem>

<prose>

```bash [name:chk_<node2>, deps:"chk_<node1> | ..."]
<it-works check on the capsule's worked object>
```

```bash [name:cx_<node2>, deps:chk_<node2>]
<hypothesis-dropped counterexample from counterexamples_when_dropped: hold every
hypothesis but one, run the object, show the conclusion fail>
```

### In the wild                       <!-- milestone nodes only -->

<one paragraph from the node's `applications` field: 2-4 named systems/results
and the mechanism>

```bash [name:app_<node2>, deps:chk_<node2>]
<the node's OWN formula at parameters from an applications entry -- e.g. the PAC
bound at |H| = 1e6, the polling half-width at n = 1000; print it labelled,
name the system. bc -l; tolerance comparisons, never `=`>
```

## 3. <a result with a machine-checked core>

<prose; one sentence on genuine-vs-instance>

```bash [name:lean_<node3>, deps:setup]
command -v lean >/dev/null || { echo "SKIP: lean not on PATH"; exit 0; }
d=$(mktemp -d)
cat > "$d/x.lean" <<'LEAN'
-- <capsule>/validation/proof-checks.lean, section N
<the capsule's exact snippet>
LEAN
if lean "$d/x.lean" 2>/dev/null; then
  echo "kernel accepted: <precisely what was verified, genuine-vs-instance>"
else
  echo "FAIL: lean rejected it"; rm -rf "$d"; exit 1
fi
rm -rf "$d"
```

   ... one section per node in `tsort` order ...

---

## Capstone: <the payoff>

<what the whole slice of the tree lets you do now; where the grade lands>

```bash [name:capstone, deps:"chk_<last> | cx_<key> | lean_<key>"]
<end-to-end on the tutorial's single object: state what was established and in
which sections, run the final computation, guard it, deliver the verdict>
```

## Where to go next

- The full `<capsule>` capsule: `skills/<capsule>/` — every result, all
  hypotheses, the counterexample and grade indexes.
- Concepts past this path's endpoint: <list from `tsort-order.txt`>.
- Related cuts: <other rows from `docs/tutorial-map.md` for this capsule>.
```

**Every fenced block in the file must be a runnable `[name:…]` block.** `upmd`
tries to execute all of them. Show statements and formulas inline as
`` **`statement`** ``; give run commands as inline `code` in a sentence (never a
` ```bash ` fence — that runs `upmd` recursively); never use 4-space-indented
code blocks.

## Block-naming convention

| Name | Role |
|---|---|
| `setup` | constants and scenario inputs; every other block `deps:` it (directly or transitively) |
| `chk_<node_id>` | the "it works" beat — instance check, specialization, or a `bc` line from the capsule's worksheet |
| `cx_<node_id>` | the hypothesis-dropped counterexample — one per theorem/lemma/proposition section |
| `lean_<node_id>` | the kernel beat — for nodes with `lean_status: core`; heredoc + `lean` + exit check + `SKIP` guard |
| `app_<node_id>` | the "In the wild" beat — *milestone nodes only*; the node's own formula at parameters from an `applications` entry, `deps:chk_<node_id>` |
| `try_<node_id>` | optional parameterised "change an input" block, `deps:chk_<node_id>` |
| `capstone` | end-to-end on the tutorial's single object |

Use the capsule's exact node ids so a reader can cross-reference the graph.
`deps:` strings list prerequisite blocks with `|` (same stage), mirroring
`edges/dependencies.plan` for that node, restricted to nodes that have a block.

## The section rhythm

A theorem section is usually **three blocks**: `chk_` (it works), `cx_` (drop a
hypothesis, it breaks), and — if `lean_status: core` — `lean_` (the kernel
confirms the algebraic heart). A definition section is usually **one** `chk_`
(the object made concrete). A `notation_convention` or `bridge` node folds into
the next real section or gets a one-line `echo` block.

**Milestone sections** (a `role: headline` node, a named rung, or the capstone)
add, after the `cx_`/`lean_` blocks, a `### In the wild` heading with a short
paragraph from the node's `applications` field, and — when an application is the
node's own formula at real parameters — an `app_<node_id>` block that computes
it. See [`references/authoring-from-nodes.md`](authoring-from-nodes.md#the-in-the-wild-beat-in-the-wild--optional-app_id).

## Static Artifact companion (only if requested)

A second file, `<name>.artifact.html` or `.md`, for reading without `upmd`:

- Header: *"Read-only companion to `<name>.md`. The code blocks below are shown
  with the output from a real `upmd --ci --all` run; this page does not execute
  anything. The Lean blocks show output from a machine with `lean` installed."*
- Every block followed by its actual captured stdout in an output block.
- No `[name:]` / `deps:` attributes (noise for a reader) — but keep block order
  identical to the runnable file.
- Publish via the Artifact tool only on request; load `artifact-design` first.
- Never describe it as interactive; never let it collect input.
