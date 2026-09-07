# Instruction checklist

Copy this block. Verify every line before you publish an instruction, tool
description, or workflow.

## Structure

- [ ] The first sentence states the task or outcome.
- [ ] Each procedural sentence contains one action.
- [ ] Each action has a clear object and target.
- [ ] Conditions appear before the command they govern.
- [ ] Steps that depend on order are numbered, not joined with "and" / "then".

## Vocabulary

- [ ] Every verb names a concrete, observable operation.
- [ ] Similar actions use the same verb everywhere (no synonym drift).
- [ ] Terms with local or business-specific meaning are defined at first use.
- [ ] Active voice; the actor is named or the imperative is unambiguous.

## Scope and policy

- [ ] The text distinguishes requirements ("must") from suggestions ("prefer").
- [ ] Scope, exclusions, and permission boundaries are explicit.
- [ ] The instruction says what NOT to do, not only what to do.

## Verification

- [ ] Completion has observable acceptance criteria, not a quality adjective.
- [ ] Failure, missing data, conflict, and uncertainty each have defined behavior.
- [ ] Output format, fields, and audience are explicit.
- [ ] The agent is told when to stop and when to escalate.

## Modes

- [ ] Each paragraph is one mode: instruction, description, policy, or decision
      rule -- no descriptive sentence that reads as a command.

## Automated pass

- [ ] `verification/run.sh` was run and every finding was reviewed.
