# Writing modes and execution states

## Separate the four modes

A major source of confusion is mixing four kinds of content in one paragraph. A
descriptive statement that sounds like a command is a trap. Keep them distinct.

| Mode | Purpose | Preferred form | Example |
|---|---|---|---|
| Instruction | Tell an agent what to do | Imperative verb, one action, explicit condition | "Read the issue comments." |
| Description | Explain how something works | Present tense, one topic per paragraph | "The issue tracker stores comments in chronological order." |
| Policy | Specify what is allowed or forbidden | "must" / "must not", scope, exceptions | "Do not post a public comment that contains customer data." |
| Decision rule | Let an agent choose between actions | If-then with thresholds and tie-breakers | "If two issues have the same severity, work on the one with the earlier due date." |

When you draft, label each paragraph with its mode in your head. If a paragraph
serves two modes, split it.

## The five execution states

Agents do not only need happy-path directions. For every important procedure,
define these five states.

| State | What to write |
|---|---|
| Entry | What must be true before starting |
| Action | The exact operation to perform |
| Success | The observable result that permits continuation |
| Failure | The stop, retry, rollback, or escalation behavior |
| Exit | What output, record, or final state is required |

### Weak workflow

> Review the deployment and fix any problems. If everything looks good, release
> it. Let the team know.

Every execution decision is left open.

### Agent-ready workflow

1. Confirm that the deployment target is the staging environment.        (entry)
2. Run the integration test suite.                                       (action)
3. If any required test fails, stop the release process.                 (failure)
4. Record the failing test names and error output.                       (failure)
5. If all required tests pass, deploy build `BUILD_ID` to staging.       (action)
6. Confirm that the deployment status is `healthy`.                      (success)
7. Send the release summary to the engineering channel.                  (exit)
8. Include the build ID, deployment time, test result, and status.       (exit)

## The seven questions an instruction must resolve

- **Who** performs the action?
- **What** exact object or resource does it affect?
- **What action** occurs?
- **When** is the action allowed, required, or forbidden?
- **What constraints** limit the action?
- **What evidence** proves completion?
- **What happens** on failure, uncertainty, or conflict?

## Where strictness helps -- and where it hurts

Apply this discipline where a misread instruction produces a wrong action:
system prompts and agent policies, tool definitions and API contracts, runbooks
and incident response, data transformations and compliance workflows, evaluation
criteria, agent-to-human handoffs, and prompts reused at scale.

Do not apply it to brainstorming, exploratory analysis, relationship-building,
nuanced persuasion, or creative work. There, over-constraint removes useful
context, personality, and uncertainty. The goal is not to make every response
read like an aircraft maintenance manual -- only the ones where a wrong reading
is expensive.

## Misconceptions

- **"Simple means dumbed down."** No. A controlled language removes linguistic
  complexity, not domain complexity. You can describe a complex deployment in
  simple English with named components, explicit states, and ordered steps.
- **"Short sentences are automatically clear."** No. Sentence length is a proxy
  for cognitive load, not the target.
- **"More detail always makes an agent safer."** No. Excess detail introduces
  conflicting rules and dilutes priority. Add information only if it resolves a
  decision, sets a boundary, defines a term, or enables verification.
- **"Strict vocabulary prevents all errors."** No. A well-written instruction can
  still rest on a false assumption. STE improves interpretation; it does not
  replace domain expertise, access control, validation, or human approval.
