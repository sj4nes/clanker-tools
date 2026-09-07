# Prompt patterns

Reusable shapes for agent-facing instructions. Each resolves the questions an
agent would otherwise guess: source of truth, required fields, no-inference rule,
missing-data behavior, safety boundary, output format.

## Research task

```text
Find the three most recent official announcements about TOPIC.

Use only first-party sources.
For each announcement, record the title, publication date, URL, and a
two-sentence summary.
Do not infer facts that the announcement does not state.
If an official source does not state a publication date, write "date not stated."
Return the results in a table.
```

Why it works: "official" is narrowed to first-party sources; the required fields
define completeness; the no-inference rule controls fabrication; the missing-data
behavior is explicit; the output format is deterministic.

## Code-change task

```text
Add validation for empty email addresses in `src/users/validate.ts`.

Return an error named `EmptyEmailError` when the input is an empty string after
trimming whitespace.
Do not change validation behavior for non-empty addresses.
Add unit tests for an empty string, whitespace-only input, and a valid address.
Run the relevant test suite.
Report the files changed and the test result.
```

Why it works: it names the file, behavior, exception name, boundary cases,
non-goal, validation action, and report format.

## Incident-triage task

```text
Examine API error logs from the last 60 minutes.

Group errors by endpoint and HTTP status code.
Mark an endpoint as affected if it has at least 100 errors or an error rate
above 2 percent.
Do not restart services.
If an endpoint is affected, report its name, error count, error rate, first
error time, and most frequent error message.
```

Why it works: it defines timeframe, grouping keys, threshold, safety boundary,
and exact output fields.

## The two-pass editing method

Do not try to write it controlled on the first pass.

### Pass 1 -- make intent complete

Draft the objective, inputs, boundaries, outputs, and failure behavior.
Prioritize completeness over brevity. Ask:

- What data or tools may the agent use?
- What must it not modify or disclose?
- What result proves the task is complete?
- What should happen when required information is absent?
- Which choices require escalation rather than inference?

### Pass 2 -- make language controlled

Rewrite each sentence against the checklist:

- Does the sentence name an actor or use a clear imperative?
- Does it contain one action?
- Does its verb name a concrete operation?
- Does it use a defined term rather than a synonym?
- Does it put the condition before the action?
- Does it state the exact object, target, and scope?
- Can a reviewer verify completion?
- Does it specify what to do when the action cannot proceed?

Then run `verification/run.sh` over the result and review each flag.
