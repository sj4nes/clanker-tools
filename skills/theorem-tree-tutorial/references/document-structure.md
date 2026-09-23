# Tutorial document skeleton (theorem-tree)

The shape, the lead, and the block vocabulary are the **shared contract**:
[`docs/capsule-tutorial-contract.md`](../../../docs/capsule-tutorial-contract.md).
Read it first — it is the same document `formula-tree-tutorial` implements, and
it is what `formula-tree-tutorial/verification/check_beats.py` enforces across
every tutorial in the repository, this skill's included.

This file holds only what is specific to a **mathematics** capsule: how a
section is filled from a result YAML, and the section rhythm.

## Section templates, for a theorem tree

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
