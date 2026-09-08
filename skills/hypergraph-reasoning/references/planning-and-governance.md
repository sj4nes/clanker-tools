# Planning and governance

The language model drafts hypotheses and plans; the hypergraph is the stateful,
attributable substrate used to validate them.

## The proposed-action hyperedge

Represent every candidate action as an **uncommitted** hyperedge:

```yaml
type: ProposedAction
participants:
  - {node: "agent:ops",           role: actor}
  - {node: "action:deploy",       role: subject}
  - {node: "artifact:release_4_2", role: input}
  - {node: "env:production",       role: target}
  - {node: "artifact:release_4_1", role: rollback}
preconditions:
  - ci-green(release_4_2.sha)
  - security-signoff(change_ticket)
  - deploy-window-open(now)
  - permission(agent:ops, deploy, production)
  - no-blocking-incident(production)
expected_effect: "p99 latency returns to baseline"
reversible: true            # rollback path exists
evidence_basis: "requirement:prod_deploy_policy_v3"
epistemic_status: proposed
```

## Precondition conjunction and constraint classification

```
Allowed = AND over preconditions, each evaluated against the time-valid context
```

For each precondition, find the supporting edge and classify it `satisfied` /
`violated` / `unknown` / `conflicting` (see
`references/retrieval-and-reasoning.md` §3). Rules:

- **`violated` → block.** Report the edge that shows the failure.
- **`unknown` on a high-impact or irreversible step → refuse or escalate.** Do
  one targeted retrieval or ask one narrow question. Never substitute an
  assumption for an unknown precondition.
- **`conflicting` → run contradiction detection**, surface both sources, do not
  proceed on a silent pick.
- **All `satisfied` → the model permits the action.** It does not authorize it
  (next section).

The naive failure mode: treating one satisfied conjunct — a green CI badge, a
"ready" status field, a release note — as a partial or full yes. It is one
term of the conjunction.

## Execution-time authorization

Even when `Allowed` is true, obtain **explicit approval at the moment of
execution** for any action that is irreversible or outward-facing (sends
external content, changes production, spends money, alters records). The
knowledge model informs the decision; it does not pre-authorize it. A stored
"deploys are allowed in this window" edge is context, not consent for *this*
deploy.

## The outcome edge and belief revision

After execution, write an `Outcome` hyperedge:

```yaml
type: Outcome
participants:
  - {node: "action:deploy_4_2_20260913", role: subject}
  - {node: "context:sub_hypergraph_ref", role: evidence}
  - {node: "metric:p99_latency",         role: output}
result: "p99 240ms -> 130ms over 6 min; no error-rate change"
valid_time: {start: "2026-09-13T10:12Z", end: null}
epistemic_status: observed
```

Then:

- Update the `confidence` of edges the outcome bears on — do not overwrite them.
- Mark any edge the outcome **contradicts** as `superseded` and add the new
  edge; keep the old one for history.
- Preserve the history of prior beliefs, sources, and decisions. The model must
  answer "what did we believe, from which source, when?".

## Evaluation metrics

Do not evaluate with QA accuracy alone. Measure whether the agent is becoming a
more reliable *actor*:

| Metric | Tests |
|---|---|
| N-ary extraction precision / recall | Correct entities, roles, qualifiers, and time per edge |
| Provenance coverage | Fraction of material assertions with a source span |
| Constraint recall | Whether all applicable restrictions are retrieved before action |
| Contradiction detection | Surfacing incompatible active claims (and *not* false ones) |
| Temporal accuracy | Correct handling of superseded / expired facts |
| Precondition accuracy | Predicted requirements match actual execution requirements |
| Grounded action rate | Fraction of actions tied to verified evidence |
| Correction efficiency | How fast new evidence updates the working model |
| Calibration | Whether stated confidence matches observed reliability |

**Adversarial test.** Put an old approval, a new policy, and a superficially
similar prior incident in the corpus. Verify the agent refuses to generalize
the old approval to the new situation.

## Failure modes to reject

- **Context collapse** — a scope, window, budget, or condition detached from
  the fact it qualified, then re-asserted unqualified.
- **Hypothesis laundering** — a `proposed` edge cited later as an `asserted`
  fact.
- **Provenance gaps** — a material edge with no source span in the model.
- **The self-authorizing model** — "we built the situation model, so the action
  is safe", skipping the precondition conjunction and execution-time approval.
- **In-place edits** — history overwritten instead of `superseded` + append.
- **Over-fragmentation** — a decision shattered into binary edges that look
  structured but have lost the joint meaning.
- **Silent conflict resolution** — picking one of two credible contradictory
  edges without surfacing the other.
