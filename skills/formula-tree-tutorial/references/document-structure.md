# Tutorial document skeleton

The generated file is plain Markdown, runnable with `upmd`. Standard shape:

```markdown
# <Tutorial title>

> Generated from the `<capsule>` capsule (Release X.Y) with the
> `formula-tree-tutorial` skill. The physics, the prerequisite order, and every
> calculation come from that capsule.

<THE LEAD. One short paragraph, required. What question the tutorial answers
and why the answer is not obvious -- the thing a reader browsing the directory
needs in order to pick this file. Name the destination formula in backticks.
Do NOT open with "This tutorial covers X": say what is at stake, then where it
lands. See "The lead" below.>

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


## The lead

The paragraph between the provenance blockquote and `## How to run this`.
**Required.** `verification/check_beats.py` fails the tutorial without one.

It exists because the file is browsed before it is read. A reader scanning
`<capsule>/tutorial/` sees a title and then, if the lead is missing, install
instructions -- which are identical in every tutorial and so distinguish
nothing.

This beat was added on 2026-09-22, after the first audit of all 24 shipped
tutorials found 19 with a lead and 5 without. The 5 were the ones that followed
this skeleton exactly; the skeleton had no lead in it, and the 19 authors each
added one anyway. **Nineteen independent departures from a skeleton is the
skeleton being wrong**, not nineteen authors being inconsistent, and that is
why the fix is here rather than in the five files.

Shapes that work, taken from the shipped set:

- **The stakes, then the landing.** "No heat engine, however well built, can
  turn all of its heat into work. The ceiling is not an engineering limit that
  better materials will lift ... this tutorial walks the argument from the
  zeroth law to `eta = 1 - T_c/T_h`."
- **The chain, spelled out**, when the path is the point: end the lead with the
  `a` -> `b` -> **`destination`** run of node ids
  (`solving-an-equilibrium.md`).
- **The handoff**, when the tutorial continues another: open by naming the file
  it follows and what it changes (`kwh-per-kilogram.md`,
  `zinc-iron-alternative.md`).

Keep it to two to five sentences. It is a hook, not an abstract, and never a
restatement of the title.
