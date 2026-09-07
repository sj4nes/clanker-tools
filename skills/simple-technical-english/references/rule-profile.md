# The STE-derived rule profile

You do not need full ASD-STE100 conformance to get most of the benefit. This is
the profile to apply to agent instructions, system prompts, tool contracts,
runbooks, and any text where a misread instruction produces a wrong action.

ASD-STE100 Issue 9 (January 2025) has 53 writing rules and a controlled
dictionary of about 900 approved words, each with one defined meaning and part of
speech. The rules below are the subset that maps directly to reliable execution.

## 1. Use concrete verbs

Prefer verbs that name an observable operation: **create, read, list, find,
compare, copy, delete, send, stop, record, return, ask, verify, report**.

Avoid broad verbs unless you define their exact meaning: **handle, manage,
address, leverage, optimize, facilitate, ensure, process**.

Do not switch verbs for variety. If `delete` means permanent removal, do not
later call it `clear`, `purge`, or `clean up`.

## 2. Make the actor explicit

Active voice forces ownership.

| Form | Example |
|---|---|
| Ambiguous | "The cache should be cleared." |
| Explicit | "The maintenance task clears the cache." |
| Best for a human-agent workflow | "Ask the administrator to clear the production cache. Do not clear it yourself." |

Passive voice hides the operational question: who is responsible?

## 3. Put conditions before commands

A condition belongs at the start of the instruction, where it governs the whole
action.

- Less safe: "Delete the temporary files if the backup completes."
- Better: "If the backup completes, delete the temporary files."
- Best: "If the backup completes, delete the temporary files. If the backup
  fails, keep the files and report the failure."

## 4. Give one instruction per sentence

Do not join steps with `and`, `then`, or `while` when sequence matters.

Dense: "Fetch the records, filter inactive accounts, update the spreadsheet, and
notify Finance."

Operational:

1. Fetch the records from the billing database.
2. Keep records whose status is `inactive`.
3. Update the spreadsheet with those records.
4. Send the spreadsheet link to Finance.

## 5. Define terms that have local meaning

An agent cannot infer what you mean by "active customer", "high risk",
"production-ready", or "sensitive data". Define the predicate at first use:

- "A **high-risk account** is an account with a fraud score of 80 or higher."
- "A **release candidate** is a build that passed unit, integration, and
  security tests."

## 6. State boundaries and exclusions

Many harmful failures come from unbounded scope, not unclear action.

- "Use only repositories in the `acme-platform` organization."
- "Do not change files outside `services/payments/`."
- "Do not send messages, create tickets, or modify external records."
- "Do not infer missing values. Mark them as `unknown`."

A rule is more useful when it says what to do **and** what not to do.

## 7. Replace quality claims with acceptance criteria

Words like "good", "correct", "clean", "safe", "complete", and "robust" hide the
test. Replace them with the test.

| Instead of | Write |
|---|---|
| "Write robust code" | "Return a typed error for invalid input. Add tests for empty input, duplicate input, and network timeout." |
| "Summarize accurately" | "Do not add claims absent from the source. Preserve all dates, quantities, names, and stated uncertainty." |
| "Make it concise" | "Use no more than five bullets. Include only decisions, owners, due dates, and blockers." |

## Weak versus strong instructions

| Weak | Why it fails | Better |
|---|---|---|
| "Clean up the customer records." | "Clean up" has no defined operation | "Delete duplicate contacts that have the same normalized email address. Do not delete contacts that have different account IDs." |
| "Use the latest report." | "Latest" = created, published, or modified? | "Use the report with the most recent `published_at` timestamp." |
| "Investigate unusual activity." | No threshold, scope, or output | "Find login events from IP addresses that appear in more than 20 accounts within 24 hours. Return a table with the IP address, account count, and first and last event times." |
| "Do not make breaking changes." | "Breaking" is undefined | "Do not change public API paths, request fields, response fields, or status codes." |
| "Escalate when appropriate." | Escalation condition missing | "Escalate to the on-call engineer if the error rate exceeds 2 percent for 10 consecutive minutes." |
| "Improve the copy." | Goal is aesthetic, not observable | "Rewrite the error message in plain English. State the failed action, the likely cause, and one recovery step." |

## Sentence-length guidance

About **20 words** per procedural sentence and about **25 words** per descriptive
sentence, as warning thresholds, not laws. Length is a proxy for cognitive load;
the real target is low ambiguity. "Fix it now" is short and underspecified.

## Source

- ASD-STE100: https://www.asd-ste100.org/about_STE.html
- ASD-Europe basics: https://www.asd-europe.org/standards-specifications/simplified-technical-english/what-are-the-basics-of-simplified-technical-english/
