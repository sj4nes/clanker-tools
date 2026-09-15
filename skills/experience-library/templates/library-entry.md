---
# One retained artifact. Copy per entry; keep beside the library, not inside
# the artifact's own prose -- the record is metadata, not instructions.
id: <short-kebab-case-slug>
rung: text | structured | procedure | executable   # references/distillation-ladder.md §1
admitted: <YYYY-MM-DD>
status: active | archived

provenance:
  produced_by: <trajectory / incident / session id>
  authored_by: <model + version, or person>
  source_tasks: [<task ids the lesson was distilled FROM>]

applicability:
  holds_when: <the conditions under which the evidence holds>
  depends_on: [<tools, schemas, other entries>]
  known_not_to_apply: <where it was tried and did not help>

executor:
  validated_for: <model + harness this was gated under>
  transfer_checked: []      # re-gate before inheriting; see behaviour 6

admission:
  hypothesis: <written BEFORE the run: what improves, on which tasks, by how much>
  control: <library version without the candidate>
  paired_result: <mean paired difference, se, n tasks>
  independent_confirmation: <tasks not used to propose it, and the result>
  displaced: <id of the entry this one pushed out, and its contribution at retirement>

contribution_log:          # APPEND ONLY -- never rewrite a row
  - date: <YYYY-MM-DD>
    retrieved_for: <task id>
    activated: true | false      # was it retrieved when relevant?
    followed: true | false       # once retrieved, was it followed?
    outcome: <what happened>
---

<the artifact itself>
