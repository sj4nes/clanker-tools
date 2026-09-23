# The capsule-tutorial contract

The document shape and beat vocabulary shared by **`formula-tree-tutorial`**
(physics and chemistry capsules) and **`theorem-tree-tutorial`** (mathematics
capsules). Both skills implement this contract; neither owns it.

`skills/formula-tree-tutorial/verification/check_beats.py` enforces the
required parts of it against every tutorial in the repository, from both
skills, and `mutation_check.py` demonstrates each guard can fail.

## Why this file exists

The two skills were written separately and kept ~80% of the same method in two
copies. Measured 2026-09-22: **8/8 workflow steps identical by name and order,
4/4 SKILL.md sections identical, 3/3 reference filenames identical** — against
only **22.5%** literal text overlap. The method was shared; the prose was
duplicated.

Duplication had already cost two defects, one in each direction:

- The **lead paragraph** was in the math skeleton and not the physics one.
  Result: five physics tutorials shipped with no lead, while nineteen other
  authors each added one anyway (`de2e22b`).
- The **Lean beat** is prescribed only in the math skill — yet physics and
  chemistry tutorials carry **23 `lean_` blocks to mathematics' 16**. The
  chemistry authors invented the beat themselves, unprescribed.

Drift in both directions, discovered only by auditing the outputs. The skills
stay separate — their check vocabularies genuinely differ, and 24 tutorials
carry provenance naming the skill that generated them — but **the contract is
single-source from here.**

## The document skeleton

```markdown
# <Tutorial title>

> Generated from the `<capsule>` capsule (Release X.Y) with the
> `<skill>` skill. The <domain>, the prerequisite order, and every
> calculation come from that capsule.

<THE LEAD — required. See below.>

## How to run this

<install upmd; the --ci --all line; the -b line>

## What you need first

<the primitive concepts assumed, and any prerequisite capsule tutorial>

---

## 0. Setup

## 1. <first concept, in tsort order>
## 2. <next concept> ...

## Capstone: <the payoff>

## Where to go next
```

Required, and checked: the title, the provenance blockquote naming the capsule,
the lead, `## How to run this`, `## What you need first`, a `## Capstone`
section, `## Where to go next`, a `[name:setup]` block, at least one
`chk_<node>` block, and a `[name:capstone]` block.

## The lead

The paragraph between the provenance blockquote and `## How to run this`.
**Required.**

It exists because the file is browsed before it is read. A reader scanning
`<capsule>/tutorial/` sees a title and then, without a lead, install
instructions — identical in every tutorial, so they distinguish nothing.

Say what question the tutorial answers and why the answer is not obvious. Name
the destination formula or theorem in backticks. Never open with "This tutorial
covers X", and never restate the title. Two to five sentences: a hook, not an
abstract.

Shapes that work, from the shipped set:

- **The stakes, then the landing.** "No heat engine, however well built, can
  turn all of its heat into work. The ceiling is not an engineering limit that
  better materials will lift … this tutorial walks the argument from the zeroth
  law to `eta = 1 - T_c/T_h`."
- **The chain, spelled out**, when the path is the point: end the lead with the
  `a` → `b` → **`destination`** run of node ids (`solving-an-equilibrium.md`).
- **The handoff**, when the tutorial continues another: name the file it
  follows and what it changes (`kwh-per-kilogram.md`).
- **The single object**, when one thing is followed throughout: one sequence in
  two number systems, one inequality applied four ways
  (`hole-in-the-rationals.md`).

## Block vocabulary

| Name | Role | Required |
|---|---|---|
| `setup` | constants and scenario inputs; every other block `deps:` it, directly or transitively | **yes** |
| `chk_<node_id>` | the "it works" beat — the capsule's own check for that node | **yes**, ≥ 1 |
| `capstone` | the whole chain spent end to end on one concrete question | **yes** |
| `lean_<node_id>` | the kernel beat — nodes with `lean_status: core`; heredoc + `lean` + exit check + `SKIP` guard when `lean` is absent | where the node has one |
| `cx_<node_id>` | the hypothesis-dropped / assumption-dropped counterexample: hold everything but the named condition, show the conclusion break | where the capsule names one |
| `app_<node_id>` | the "In the wild" beat — the node's own formula at real parameters from its `applications` entry | milestone nodes only |
| `try_<node_id>` | optional parameterised "change an input" block, `deps:chk_<node_id>` | optional |

Use the capsule's exact node ids so a reader can cross-reference the graph.
`deps:` strings list prerequisite blocks with `|`, mirroring
`edges/dependencies.plan` for that node, restricted to nodes that have a block.

Every block is **idempotent** and independent of run order beyond its declared
`deps`.

## The workflow

Both skills run the same eight steps. The step *names* are the contract; the
bodies are domain-specific and live in each skill's `SKILL.md`.

1. Choose the tutorial's scope
2. Extract the ordered node list (`tsort`)
3. Write the lead, then one section per node, in order
4. Build the `setup` block
5. Convert each capsule check into a named block
6. Add a capstone
7. Verify it runs
8. Place and record

## What is domain-specific, and stays in each skill

This is the part that is *not* shared, and the reason the two skills remain
two.

| | `formula-tree-tutorial` | `theorem-tree-tutorial` |
|---|---|---|
| Source | `physics-formula-tree` capsules | `math-theorem-tree` capsules |
| The `chk_` beat | dimensional check on the `[M, L, T, Θ, N, I]` basis (prints the zero vector), limiting case, worked example | instance check, specialization, identity at sample values, bisection or brute search |
| `cx_` source | the capsule's assumption / regime nodes — drop the regime, show the formula leave its domain of validity | the result YAML's `counterexamples_when_dropped` |
| Grades | — | `choice_grade`, `constructive_grade`, `convergence_mode` surfaced in the section |
| Units | SI units and dimensions are first-class throughout | — |

## Changing this contract

A change here lands on both skills at once, which is the point. Bump the MINOR
version of **both** `formula-tree-tutorial` and `theorem-tree-tutorial` and say
so in both changelogs, then run
`sh skills/formula-tree-tutorial/verification/run.sh` — it checks every
tutorial from both skills.
