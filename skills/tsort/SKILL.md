---
name: tsort
description: >-
  Use `tsort` to construct, validate, and explain dependency-respecting
  execution orders for tasks where items must occur before other items:
  schema/data migrations, staged config rollouts, build and code-generation
  phases, package installation, deployment stages, and multi-file edit plans.
  Covers deriving evidence-backed edges, detecting and resolving cycles,
  handling multiple valid orders, and keeping planning separate from execution.
version: 1.0.0
author: Simon Janes
tags: [planning, tsort, dependencies, topological-sort, migrations, deployment, terminal]
---

# Dependency Planning with `tsort`

You are an autonomous terminal agent that uses `tsort` to construct, validate, and explain dependency-respecting execution orders. Use it for tasks where items must occur before other items: code-generation phases, database migrations, configuration rollouts, package installation, build steps, test prerequisites, deployment stages, and cross-file edit plans.

Your priority is to derive a **correct, evidence-backed order** or to surface a dependency cycle clearly. Never invent an order merely because one is convenient.

Treat dependency planning as a formal process:

    identify items → derive edges → validate graph → topologically sort → review plan → execute or report

`tsort` consumes pairs of items and emits a topological order: for an input pair `A B`, item `A` must appear before item `B`. If the input graph contains a cycle, `tsort` reports that no complete dependency-respecting order exists. GNU Coreutils includes `tsort` as its topological-sorting utility.

## Core model

Represent dependencies as directed edges `A → B`, meaning **A must be completed, available, approved, or applied before B.** In `tsort` input, write that relation as `A B`:

```text
generate_sources compile
compile test
test package
package publish
```

```sh
tsort dependencies.txt
```

The output is *a* valid ordering, not necessarily the only one. When multiple items are independent, `tsort` may choose any relative order consistent with the known constraints. Do not interpret adjacent output lines as proof of a direct dependency unless that edge was explicitly supplied.

## When to use `tsort`

Use `tsort` when the task includes a partial order rather than a simple fixed sequence:

- Ordering schema migrations or data migrations.
- Planning staged configuration changes.
- Sequencing code-generation, compilation, tests, packaging, signing, and publication.
- Resolving prerequisites among scripts or automation steps.
- Planning a multi-file refactor with explicit intermediate requirements.
- Ordering API changes, client updates, compatibility shims, and removal steps.
- Checking whether documented workflow constraints contain contradictions.
- Producing an execution plan from manifest- or configuration-defined dependencies.
- Identifying dependency cycles in a manually constructed set of relationships.

Do not use `tsort` when:

- The relationships are unknown or inferred only from filenames, timestamps, alphabetical order, or intuition.
- Ordering depends on runtime conditions not represented as edges.
- The task needs resource scheduling, durations, retries, concurrency limits, or critical-path optimization.
- Dependencies carry richer semantics than "must happen before" — optionality, version ranges, conditional feature flags, mutual exclusion — unless modeled separately.
- You need to modify a project's dependency manifest; `tsort` can analyze a proposed graph but does not make the underlying semantic change safe.
- A build system, package manager, workflow engine, or migration framework already provides the authoritative order. Then use `tsort` only as an independent diagnostic or planning aid.

## Required operating principles

- Derive every graph edge from concrete evidence: source code, configuration, migration metadata, build rules, API compatibility requirements, user instructions, or validated domain rules.
- State the direction of every relation in words before encoding it.
- Use stable, unambiguous item identifiers.
- Never encode an edge until both endpoints are defined.
- Avoid overconstraining the graph (add only genuine prerequisites) and underconstraining it (omitted prerequisites produce a syntactically valid but operationally unsafe order).
- Treat a `tsort` result as a plan proposal, not automatic permission to perform the actions.
- Inspect and validate the plan before executing any write, deployment, migration, publication, or destructive operation.
- Preserve the original edge list as an audit artifact. Record the exact `tsort` command and resulting order.
- Treat cycles as a design or planning defect that must be explained, not bypassed. Do not manually delete arbitrary edges to make a cycle disappear.

## Terminology

| Term | Meaning |
|---|---|
| Node | A named item in the plan (`generate_sources`, `migration_042`, `deploy_api`) |
| Edge | A directed dependency, written `A B` in `tsort` input |
| Predecessor / Successor | A node that must occur before / after another |
| Root / Leaf | A node with no known predecessors / successors |
| Partial order | Constraints where some items may remain independent |
| Topological order | A sequence satisfying every directed edge |
| Cycle | A circular prerequisite, such as A → B → C → A |

## Input format

`tsort` reads whitespace-separated pairs, `predecessor successor`, one edge per line preferred. Whitespace is the separator, so **identifiers must not contain spaces, tabs, or newlines**.

Safe identifiers: `generate_sources`, `cargo_check`, `test_unit`, `migration_042_add_index`, `deploy_api_v2`.
Avoid: `Step 1`, `latest`, `run it`, `the migration`.

If source objects have spaces or complicated paths, assign a stable logical node name and keep a mapping in comments or a separate manifest:

```text
# migration_042 = db/migrations/042_add_user_index.sql
migration_041 migration_042
migration_042 application_release_2026_09
```

Do not pass user-controlled text directly into a `tsort` edge file without validating it — unexpected whitespace changes node boundaries and alters the graph.

## Required workflow

### 1. Define the planning question

State the exact decision `tsort` will support. Define the plan boundary: which nodes are in scope; which actions are out of scope; whether the plan is analysis-only or leads to execution; whether nodes represent changes, validations, approvals, artifacts, or deployments; whether a node may run more than once; whether a node is idempotent, reversible, or destructive. Do not mix conceptual levels (`schema_migration_042`, `application_binary_built`, `backup_verified`, `production_deployment`) without labeling their roles.

### 2. Inventory nodes

List all nodes before constructing edges. For each, record: stable identifier; real-world action; source evidence; side-effect level (read-only, local write, remote write, destructive, irreversible); reversibility / rollback path; success condition; owner or authority permitted to execute it.

A node may appear without edges only if the installed `tsort` supports isolated-node representation. For portable use, represent an isolated node as a self-pair (`independent_check independent_check`) only after checking local behavior. Do not add fake prerequisites merely to force an isolated item into the output.

### 3. Derive dependencies from evidence

For each dependency, first write a plain-language statement ("The database backup must complete before migration_042 begins."), then encode it (`backup_database migration_042`). Keep a two-column requirement→edge table while designing the graph.

Apply this verbal test to every edge:

> "Can I truthfully say: **the first node must happen before the second node**?"

If not, the edge is wrong, underspecified, or unsupported. Never reverse dependency direction — if compilation requires generated sources, the edge is `generate_sources compile`, not `compile generate_sources`.

**Strong evidence:** explicit dependencies in a build manifest, workflow file, task runner, package metadata, or migration framework; a compiler error or test failure proving a prerequisite; documented deployment or compliance procedures; explicit API compatibility requirements; verified source-level references; user-provided ordering requirements; formal invariants, schemas, or interface contracts.

**Weak evidence** (mark as a hypothesis for review, do not encode as a hard dependency): alphabetical order; file modification times; file names that "sound related"; unconfirmed project conventions; guessing from prior projects; tool output not tied to the actual target system.

### 4. Construct an auditable edge file

Keep a documented source file with comments, then generate a clean edge file (portable `tsort` has no comment syntax):

```sh
grep -Ev '^[[:space:]]*(#|$)' dependencies.plan > dependencies.edges
nl -ba dependencies.edges
LC_ALL=C sort -u dependencies.edges > dependencies.edges.sorted   # deterministic, reviewable
```

Deduplicating identical edges is usually safe *after* inspection; it does not fix missing nodes, reversed dependencies, or wrong relationships. Sorting the file's *lines* is fine for readable diffs. **Never sort nodes within a pair** — `A B` is not `B A`.

### 5. Inspect graph basics before sorting

Cheap consistency checks before calling `tsort`:

```sh
# Every nonempty edge line must have exactly two fields
awk 'NF != 2 { print "Invalid edge at line " NR ": got " NF " fields" > "/dev/stderr"; exit 1 }' dependencies.edges

# List nodes
awk '{ print $1; print $2 }' dependencies.edges | LC_ALL=C sort -u

# Likely roots (no incoming) and leaves (no outgoing)
awk '{ seen[$1]=seen[$2]=1; inn[$2]=1; out[$1]=1 }
     END { for (n in seen) if (!(n in inn)) print "root " n; for (n in seen) if (!(n in out)) print "leaf " n }' dependencies.edges | LC_ALL=C sort

# Self-dependencies (usually a modeling error)
awk '$1 == $2 { print "Self-dependency at line " NR ": " $1 > "/dev/stderr"; bad=1 } END { exit bad }' dependencies.edges
```

Unexpected roots often indicate missing prerequisites. Unexpected leaves may mean the graph omitted a required validation, approval, rollback checkpoint, or final delivery stage.

### 6. Run `tsort`

**Do not rely on exit status alone to detect a cycle.** GNU `tsort` exits non-zero on a cycle, but the BSD `tsort` that ships with macOS prints `tsort: cycle in data` to stderr, still emits a (meaningless) ordering, and exits `0`. Check stderr as well:

```sh
tsort dependencies.edges > execution-order.txt 2> tsort-errors.txt
status=$?

if [ "$status" -ne 0 ] || [ -s tsort-errors.txt ]; then
  printf '%s\n' 'Topological sort failed or reported a cycle; inspect tsort-errors.txt.' >&2
  cat tsort-errors.txt >&2
  exit 1
fi
printf '%s\n' 'Topological sort succeeded.'
```

- Exit `0` **and** empty stderr: `execution-order.txt` is a valid topological ordering *for the supplied graph*.
- Any stderr output (`cycle in data`, `odd data`, parse errors) or non-zero exit: the graph contains a cycle or invalid input.

Do not proceed with execution if `tsort` wrote anything to stderr or returned a non-zero status. A cross-check that catches a cycle on every implementation: a cyclic graph still prints every node, so compare the ordered-node count with the unique-node count *and* scan stderr — if stderr mentions `cycle`, stop.

### 7. Verify the proposed order

A successful sort proves only that the output satisfies the supplied edges — not that the edges are complete or semantically correct.

```sh
# Every declared edge is respected by the resulting order
awk 'NR==FNR { position[$1]=NR; next }
     { if (position[$1] >= position[$2]) { print "Order violation: " $1 " must precede " $2 > "/dev/stderr"; bad=1 } }
     END { exit bad }' execution-order.txt dependencies.edges

# Node coverage
awk '{ print $1; print $2 }' dependencies.edges | LC_ALL=C sort -u > graph-nodes.txt
LC_ALL=C sort -u execution-order.txt > order-nodes.txt
diff -u graph-nodes.txt order-nodes.txt

nl -ba execution-order.txt   # review numbered plan
```

Then ask: does each step have all real-world prerequisites represented? Does each destructive step have a backup, review, approval, or rollback prerequisite? Does a deployment follow its required tests and artifact verification? Does a cleanup step occur only after all consumers are complete? Are independent steps being wrongly treated as mandatory serial work? Are health checks present after each significant change? Are required human approvals modeled explicitly?

### 8. Handle multiple valid orders

A DAG can have more than one correct order. If `generate_docs` and `run_tests` both precede `package` but neither depends on the other, both output orderings are valid. **Do not add a fake edge to force a preferred order.**

If a deterministic presentation order is needed among independent steps: distinguish genuine dependencies from presentation preferences; document the preference separately; add a tie-breaking edge only if serializing is operationally safe and desired; label it as a scheduling preference, not a prerequisite. Do not encode a preference as a hard dependency if it could reduce safe parallelism, delay a rollback, or conceal missing real dependencies.

### 9. Resolve cycles correctly

A cycle means no valid full order exists. When `tsort` reports one:

1. Stop planning execution.
2. Preserve the original edge list and error output.
3. Identify the nodes named in the cycle report.
4. Trace each edge back to its evidence.
5. Determine which relation is: reversed; unsupported; a genuine circular design problem; a missing intermediate compatibility or bootstrap step; conditional but modeled as unconditional; or a conflation of build-time and runtime requirements.
6. Correct the model only when evidence supports the correction.
7. Re-run all graph checks and `tsort`.
8. Record the resolution.

Do not resolve a cycle by arbitrarily deleting an edge, running `tsort` repeatedly to select partial output, executing in alphabetical order, or ignoring the error because the actions "usually work."

| Observed cycle | Likely underlying issue |
|---|---|
| New app version needs new schema; new schema breaks old app | Missing expand/contract migration or compatibility release |
| Code generation needs compiled tool; tool comes from generated code | Bootstrap dependency needing a prebuilt tool or staged build |
| Signing needs publication metadata; publication needs signed artifact | Missing draft-release stage |
| Test env needs deployed service; deployment needs tests to pass | Missing staging deployment or test-double boundary |
| Config rollout needs client support; client deploy needs config change | Need backward-compatible defaults and phased rollout |

A cycle often reveals the most valuable information in the workflow: the system needs a compatibility layer, bootstrap artifact, staged deployment, or a clearer required/optional distinction.

### 10. Separate planning from execution

A valid `tsort` order is not an execution authorization. Classify each node before carrying it out:

| Side-effect class | Examples | Execution policy |
|---|---|---|
| Read-only | Inspect files, `git diff`, compile check, dry-run, query status | May execute after scope review |
| Local reversible write | Generate temp file, build into disposable dir | Verify output, preserve prior state |
| Local persistent write | Modify source, update lockfile, write migration record | Require change review and validation |
| Remote mutable action | Deploy, update CI settings, alter a database, upload artifact | Require explicit target verification and authorization |
| Destructive / irreversible | Delete data, rotate/delete keys, publish public release, destructive migration | Require explicit confirmation, rollback assessment, postcondition checks |

For each executable node define: command or procedure; exact target; preconditions; expected output; timeout; failure condition; rollback or recovery path; postcondition verification. Do not substitute a `tsort` node name for a real operational runbook.

## References

- [`references/planning-patterns.md`](references/planning-patterns.md) — worked graphs: staged Rust release, expand-contract database migration, configuration rollout with explicit approval gates, code-refactor with API add/remove.
- [`references/shell-template.md`](references/shell-template.md) — a small auditable planning script (clean → validate fields → reject self-edges → dedup → `tsort` → verify every edge → numbered plan), plus the failure-mode table and completion-report formats.

## Completion requirements

Before declaring a `tsort` planning task complete, confirm:

- Every node has a stable, unambiguous identifier.
- Every edge can be expressed truthfully as "first node must happen before second node."
- Each edge has concrete evidence.
- The edge file contains exactly two fields per noncomment line.
- Duplicate edges and accidental self-dependencies have been examined.
- `tsort` completed successfully, or the cycle/error is reported clearly.
- Every output node maps back to a real-world action.
- Every supplied edge is satisfied by the output order.
- Missing dependencies, optional conditions, and independent tasks have been considered.
- Execution authorization has been kept separate from planning.
- No node representing a destructive, remote, or irreversible action has been performed merely because it appeared in a valid topological order.
