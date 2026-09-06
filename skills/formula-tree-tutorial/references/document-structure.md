# Tutorial document skeleton

The generated file is plain Markdown, runnable with `upmd`. Standard shape:

```markdown
# <Tutorial title>

> Generated from the `<capsule>` capsule (Release X.Y) with the
> `formula-tree-tutorial` skill. The physics, the prerequisite order, and every
> calculation come from that capsule.

## How to run this

Install upmd (https://upmd.dev), then run `upmd <name>.md` for the interactive
walk or `upmd --ci --all <name>.md` to run every calculation top to bottom. Each
section ends with a code block you run yourself; blocks depend on earlier ones,
so `upmd --ci -b chk_<x> <name>.md` runs a single check with its whole chain.

## What you need first

<one paragraph: the primitive concepts assumed (calculus, SI units, ...), and a
pointer to any prerequisite capsule tutorial>

---

## 0. Setup

<one sentence: these constants feed every calculation below>

```bash [name:setup]
export G=9.81            # m/s^2, standard gravity
export PENDULUM_L=1.00   # m, the worked example
echo "constants loaded"
```

## 1. <first concept, in tsort order>

<120–200 words from the node entry: statement, symbols+units, when it holds,
where it breaks>

    <formula on its own line>

```bash [name:chk_<node1>, deps:setup]
<the capsule's check for this node; prints a labelled result>
```

<one line: what the output means>

## 2. <next concept> ...

   ... one section per node, each `deps:` its prerequisites' blocks ...

---

## Capstone: <the payoff>

<what the whole path lets you compute now>

```bash [name:capstone, deps:"chk_<last_node> | chk_<other_needed>"]
<end-to-end worked example on the setup scenario; predicts a number and checks
it against a stated "measured" value or a known result>
```

## Where to go next

- The full `<capsule>` capsule: `skills/<capsule>/` — every formula, all regimes.
- Next concepts not covered here: <list from the capsule's tsort order past this
  path's endpoint>.
```

**Every fenced block in the file must be a runnable `[name:…]` block.** `upmd`
tries to execute all of them. Show formulas inline as `` **`formula`** ``; give
the run commands as inline `code` in a sentence (never a ` ```bash ` fence — that
runs `upmd` recursively); never use 4-space indented code blocks.

## Block-naming convention

| Name | Role |
|---|---|
| `setup` | constants; every other block `deps:` it (directly or transitively) |
| `chk_<node_id>` | the fixed calculation for a concept — dimensional check or limiting case |
| `try_<node_id>` | optional parameterized "change an input" block, `deps:chk_<node_id>` |
| `capstone` | end-to-end worked example |

Use the capsule's exact node ids so a reader can cross-reference the capsule
graph. `deps:` strings list the prerequisite blocks with `|` (same stage) —
mirror the capsule's `edges/dependencies.plan` for that node, restricted to
nodes that have a `chk_` block.

## Static Artifact companion (only if requested)

A second file, `<name>.artifact.html` or `.md`, for reading without upmd:

- Header: *"Read-only companion to `<name>.md`. The code blocks below are shown
  with the output from a real `upmd --ci --all` run; this page does not execute
  anything."*
- Every `bash` block followed by its actual captured stdout in an output block.
- No `[name:]` / `deps:` attributes (they are noise for a reader) — but keep the
  block order identical to the runnable file.
- Publish via the Artifact tool only on request; load `artifact-design` first.
- Never describe it as interactive, and never let it collect input.
