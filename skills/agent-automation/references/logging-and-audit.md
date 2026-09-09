# Logging that supports operations and forensics

Logging should answer five questions after any run:

1. **Who/what initiated it?**
2. **What did the agent believe it was doing?**
3. **Which policy and authorization checks ran?**
4. **Which tools changed or read what?**
5. **What was the verified outcome?**

Use structured logs — not prose-only logs — so you can query, alert, and
reconstruct incidents. Log agent decisions, tool calls, outcomes, and high-risk
decision metadata: action classification, authorization outcome, approval
identifier, execution result, policy version.

## Minimum event schema

```json
{
  "timestamp": "2026-09-09T22:37:15.124Z",
  "event_id": "evt_01J...",
  "trace_id": "trace_01J...",
  "run_id": "run_01J...",
  "tenant_id": "tenant_acme",
  "actor": { "type": "human", "id": "user_123", "role": "operations_manager" },
  "agent": { "id": "invoice-reconciliation-agent", "version": "2026.09.2", "model": "provider/model-version" },
  "event_type": "tool_execution_completed",
  "action": { "name": "create_credit_note", "risk_tier": "high", "idempotency_key": "invoice-8821-credit-note-v1" },
  "policy": { "version": "policy-2026-09-01", "decision": "allowed_with_approval", "rules_matched": ["FIN-17", "APPROVAL-HIGH-RISK"] },
  "approval": { "required": true, "approval_id": "apr_789", "approver_id": "user_456" },
  "tool": { "name": "billing.create_credit_note", "request_fingerprint": "sha256:...", "response_fingerprint": "sha256:...", "latency_ms": 842, "status": "success" },
  "outcome": { "verified": true, "verification_method": "read_after_write", "resource_id": "cn_10293" },
  "error": null
}
```

The machine-readable copy lives in
[`../templates/audit-event.schema.json`](../templates/audit-event.schema.json).

## Fields to retain

- **Correlation IDs**: `trace_id`, `run_id`, `parent_run_id`
- **Identities**: human initiator, service account, agent identity, tenant
- **Agent versioning**: model, prompt/template version, tool schema version,
  policy version
- **Intent**: proposed plan, risk tier, confidence only if it has operational
  meaning
- **Authorization**: policy decision, denials, permissions checked, approval ID
- **Execution**: tool name, sanitized parameters or a parameter fingerprint,
  retries, latency, result
- **Verification**: expected postcondition, actual observation, rollback status
- **Costs and limits**: tokens, execution time, tool-call count, spending budget
  consumed

## Denials matter as much as successes

A blocked tool call may be evidence of an attempted prompt injection, a stale
permission, a broken integration, or a bad policy. Record the policy rule and the
risk rationale — without logging unsafe prompt contents verbatim.

## Log safely

Do not turn observability into a data leak. Keep out of application logs: raw
secrets, bearer tokens, full payment details, unmasked PII, full confidential
documents. Prefer metadata plus content hashes, redacted excerpts, and resource
identifiers. Log document metadata/hashes instead of large payloads.

## Tamper-evidence for regulated systems

Make audit logs tamper-evident (e.g. hash-chained or write-once storage), store
them separately from the application's primary database, restrict log access, and
retain them per policy. Keep enough to reconstruct the trigger, context, action,
and outcome — and treat the logs themselves as sensitive data.

Sources: OWASP AI Agent Security Cheat Sheet —
https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html ;
LoginRadius, "Auditing and logging AI agent activity" —
https://www.loginradius.com/blog/engineering/auditing-and-logging-ai-agent-activity ;
M3AAWG comments on security considerations for AI agents —
https://www.m3aawg.org/sites/default/files/doc_files/m3aawg_comments_rfi_regarding_security_considerations_for_artificial_intelligence_agents.pdf
