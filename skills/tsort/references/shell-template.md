# `tsort` shell template, failure modes, and reports

## Auditable planning run

```sh
#!/bin/sh
set -eu

plan_file=${1:-dependencies.plan}
edge_file=${2:-dependencies.edges}
order_file=${3:-execution-order.txt}
error_file=${4:-tsort-errors.txt}

grep -Ev '^[[:space:]]*(#|$)' "$plan_file" > "$edge_file"

awk '
  NF != 2 {
    print "Invalid dependency at line " NR \
      ": expected exactly two node identifiers, found " NF > "/dev/stderr"
    exit 1
  }
  $1 == $2 {
    print "Unexpected self-dependency at line " NR ": " $1 > "/dev/stderr"
    exit 1
  }
' "$edge_file"

LC_ALL=C sort -u "$edge_file" > "$edge_file.sorted"
mv "$edge_file.sorted" "$edge_file"

tsort "$edge_file" > "$order_file" 2> "$error_file" || true
# BSD/macOS tsort exits 0 on a cycle but writes "tsort: cycle in data" to stderr,
# so treat ANY stderr output as failure, not just a non-zero exit.
if [ -s "$error_file" ]; then
  printf '%s\n' "Dependency graph is invalid or cyclic; see $error_file." >&2
  cat "$error_file" >&2
  exit 1
fi

awk '
  NR == FNR { pos[$1] = NR; next }
  {
    if (!($1 in pos) || !($2 in pos) || pos[$1] >= pos[$2]) {
      print "Topological-order verification failed: " $1 " -> " $2 > "/dev/stderr"
      failed = 1
    }
  }
  END { exit failed }
' "$order_file" "$edge_file"

printf '%s\n' 'Dependency order:'
nl -ba "$order_file"
```

This template removes blank/comment lines, ensures each dependency has two fields, rejects unintended self-edges, deduplicates identical dependencies, runs `tsort`, verifies that every edge is respected in the result, and prints a numbered plan. It does **not** establish whether the edge list is semantically complete — still inspect the evidence behind every relationship.

## Failure modes

| Failure | Why it happens | Required response |
|---|---|---|
| Reversed edge | "Depends on" confused with "must precede" | Restate in words; reverse only if evidence supports it |
| Missing edge | A prerequisite was not modeled | Add the evidence-backed edge and rerun validation |
| Extra edge | Preference mistaken for a requirement | Remove or label as a nonessential scheduling preference |
| Cycle | Contradictory or circular prerequisites | Stop; analyze the architecture/process; add a compatibility or bootstrap stage if needed |
| Ambiguous node name | Multiple real actions share one identifier | Split nodes and document each action |
| Isolated node absent | It appears in no pair | Use a verified standalone-node representation or report it separately |
| Invalid fields | Spaces or unvalidated input corrupted tokenization | Use stable whitespace-free identifiers; validate each line |
| Nondeterministic order | Multiple valid topological orders exist | Report independence; do not mistake it for a defect |
| Unsafe execution | Valid sequence includes destructive steps | Apply separate confirmation, backups, postcondition checks |
| Misleading success | `tsort` validated an incomplete graph | Review domain constraints and plan boundaries, not just exit status |

## Completion report

```text
Planning goal:
- Determine a safe order for [scope].

Nodes:
- [count] nodes representing [types of actions].

Evidence:
- Dependencies were derived from [specific files, manifests, requirements, or runbook sections].

Graph result:
- `tsort` [succeeded / failed].
- [If successful: the graph is acyclic and has one or more valid topological orders.]
- [If failed: identify the cycle or invalid edges reported.]

Proposed order:
1. [node] — [real-world action]
2. [node] — [real-world action]

Validation:
- Checked every edge is respected by the generated order.
- Checked that graph nodes and ordered nodes match.
- [Any additional source-specific or policy validation.]

Execution status:
- Planning only; no actions were executed.
```

## Cyclic-graph report

```text
Graph result:
- `tsort` failed because the plan contains a dependency cycle.

Cycle:
- [node A] must precede [node B].
- [node B] must precede [node C].
- [node C] must precede [node A].

Implication:
- No safe linear execution order exists under the current assumptions.

Required resolution:
- Re-evaluate the listed edges against their source evidence.
- Introduce a documented compatibility, bootstrap, staging, or approval step if the cycle is genuine.
- Do not execute the plan until the graph becomes acyclic.
```
