# Sandbox charter — <domain / question>

## The cause/effect question

- **Direction:** forward (what does X cause) | backward (what caused Z / what prevents Z)
- **Question, in one sentence:**
  <e.g. "Does revoking role R from user U while job J holds a lease on R leave J
  able to write after the lease renews, starting from config C?">
- **Why it matters / what a wrong answer costs:**

## The observable

- **Predicate or field to read off each state:** <e.g. `can_write(J, resource)`>
- **How it is read:** <the exact expression over the store>
- **What counts as the outcome of interest:** <e.g. "the step at which it becomes true", "its value at the terminal state">

## Initial state

- **Entities:** <types and counts — 3 users, 1 item, 2 roles>
- **Initial facts:** <the ground facts of `S_0`>
- **Where these come from:** <a real config read? a hypothetical? a spec example?>

## Interventions to compare

| Branch | Label | Changes to `S_0` / injected events |
|---|---|---|
| A | | |
| B | | |

## Bounds (each is a modelling claim)

- **Steps per branch:** <max trace depth>
- **Entity counts:** <fixed, named>
- **Value domains:** <`stock ∈ 0..100`, not ℕ>
- **Branching fan-out:** <max intervention branches; max nondeterministic choices>
- **Scheduler + seed:** <priority | round-robin; seed>

## Backward queries only

- **Target event / predicate transition:** <"stock became 0 at step 5">
- **Change budget:** <max number of `S_0` / intervention changes to search>
- **Levers in scope:** <which initial facts are things the domain owner can actually set>

## Out of scope / not being asked

- <consequences past the step bound — reported as "not observed", never "won't happen">
- <"can the system ever reach a bad state" — that is `tla-checker`, not this>
- <a proof that an invariant always holds — that is `lean`>
