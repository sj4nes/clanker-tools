# The optimization loop in detail

This is the practitioner's reference for the `skill-evolution` loop. It follows
SkillAdam (Li, Fan, Liu, Zhang, Fan et al., *SkillAdam: Stable and Efficient
Skill Evolution for Agents*, 2026), which adapts the two principles behind Adam
to the space of natural-language instruction documents.

## The Adam correspondence

The analogy is **functional, not numerical**. Nothing here computes a gradient.
It constructs language-space states that play the same optimization roles.

| Adam | Skill evolution | Functional role |
|---|---|---|
| Parameters `θ_{t-1}` | Current document `S_{t-1}` | The state being optimized |
| Prediction `o_t` | Execution trajectories `T_t` | What the agent did this round |
| Loss `L_t` | Evaluation feedback `F_t^roll` | How the current document scored |
| Gradient `∇_t` | Skill patch `g_t` | The local update signal |
| First moment `m_t` | Issue tracker `M_t` | Stabilize the update *direction* |
| Second moment `v_t` | Improvement volatility `V_t` | Accumulate update *variability* |
| Effective step size `α_eff` | Edit budget `σ_{t+1}` | Adapt the update *magnitude* |
| `θ_t = θ_{t-1} + Δθ_t` | Accept-or-reject the patch | Apply the update through a gate |

The feedback `F_t^roll` plays the loss role (it evaluates current behavior); the
patch `g_t` plays the gradient role (a local edit direction in document space).

## First moment — the issue tracker

`M_t = { I_j }`, each `I_j = (pattern_j, status_j, attempts_j)`.

`attempts_j` is an ordered list of `(round, edit_summary, outcome)`. `outcome` is
concrete: "resolved 5/5", "partial — 2/5", "no effect", "regressed 1 case".

### Update rules (run after the acceptance decision, every round)

1. **Match.** For each failure in this round's candidate feedback, find the issue
   whose `pattern` describes it. Matching is semantic, not string equality —
   "ignored the museum constraint" and "skipped the 2-attraction requirement"
   are the same issue.
2. **Open** a new entry only when no existing pattern matches.
3. **Record the attempt.** Append `(t, patch summary, outcome)` to the issue the
   patch was targeting — whether or not the patch was accepted. A rejected patch
   with outcome "regressed 2 cases" is valuable history.
4. **Resolve.** If an open issue's failures are absent from the candidate
   feedback *and* the candidate was accepted, set `status = resolved`.
5. **Reopen.** If a `resolved` issue's failure reappears in any later round, set
   `status = reopened` and record the round. Two failed attempts on a reopened
   issue → escalate to a structural review of the document, do not add a third
   patch.

### What the patch generator receives

- the current document `S_{t-1}`
- this round's trajectories `T_t` and feedback `F_t^roll`
- **the open and reopened issues with their full `attempts` history**
- the edit budget `σ_t`

The instruction to the generator: *propose a diff of at most `σ_t` <units> that
addresses the highest-priority open issue without contradicting any edit recorded
as "resolved" or "partial" in the attempt histories.*

## Second moment — improvement volatility and the edit budget

After the paired evaluation, for each case `i` in the batch:

```
delta_i = s(candidate, case_i) − s(current, case_i)
```

where `s(·)` extracts the benchmark's scalar score for that case.

```
delta_bar   = mean_i(delta_i)
vhat_t      = (1 / (|B| − 1)) * sum_i (delta_i − delta_bar)^2      if |B| >= 2
vhat_t      = 0                                                    otherwise
V_t         = beta2 * V_{t-1} + (1 − beta2) * vhat_t               V_0 = 0
```

`beta2` is an EMA decay in `[0, 1)`; 0.9 is a reasonable default (a batch's
volatility keeps ~10% weight after one further round... i.e. weight `0.1` on the
newest, `0.9` carried).

### Edit budget

```
budget_{t+1} = max( b_min , floor( b_base * (1 − clip(V_t / V_max, 0, 1)) ) )
```

- `b_base` — the budget when recent evidence is perfectly consistent (`V_t = 0`).
  Example: 8 lines, or 3 bullets, or 1 section.
- `b_min` — the floor; even under maximum volatility you may make a minimal edit.
  Example: 1 line.
- `V_max` — the volatility at which the budget bottoms out. Calibrate from a few
  rounds of observed `vhat_t`; set it near the high end of what you have seen.

`budget_1 = b_base`.

### Worked example

`b_base = 8`, `b_min = 1`, `V_max = 2.0`, `beta2 = 0.9`. Sample variance uses
`n − 1` in the denominator.

| Round | `delta_i` | `vhat_t` | `V_t` | `budget_{t+1}` |
|---|---|---|---|---|
| 1 | `[+1, +1, +1, +1]` | `0 / 3 = 0.000` | `0.9*0 + 0.1*0.000 = 0.000` | `floor(8*(1 − 0)) = 8` |
| 2 | `[+3, −2, +3, −2]` | `25 / 3 = 8.333` | `0.9*0 + 0.1*8.333 = 0.833` | `floor(8*(1 − clip(0.417))) = floor(4.667) = 4` |
| 3 | `[+1, 0, +1, 0]` | `1 / 3 = 0.333` | `0.9*0.833 + 0.1*0.333 = 0.783` | `floor(8*(1 − 0.392)) = floor(4.867) = 4` |
| 4 | `[+1, +1, +1, +1]` | `0 / 3 = 0.000` | `0.9*0.783 + 0.1*0.000 = 0.705` | `floor(8*(1 − 0.353)) = floor(5.180) = 5` |

Round 2 was volatile (big wins and big losses) → the round-3 budget drops from 8
to 4. The EMA carries that volatility forward: round 3 was mild and consistent
but the budget is still suppressed at 4, and only by round 4 does it begin to
recover. One noisy round dampens the edit scope for several rounds — which is the
intended behavior.

The `verification/` harness recomputes exactly this table.

## The acceptance gate

```
accept(candidate) :=
    (∃ m ∈ targets:    metric_m(candidate) − metric_m(current) ≥ threshold_m)
  ∧ (∀ p ∈ protected:  metric_p(current)   − metric_p(candidate) ≤ boundary_p)
```

- **Targets** are the metrics you are trying to move. Each has a positive
  `threshold` — the minimum improvement that counts as progress. An auxiliary
  target clearing its threshold can carry a primary that is flat.
- **Protected** metrics must not regress by more than `boundary_p` (often 0 —
  no regression at all). Cost, latency, a safety-check pass rate, and a
  previously-passing subset are common protected metrics.
- Each protected metric has an **orientation**: cost and latency regress when
  they rise, a pass rate regresses when it falls. State the orientation with the
  boundary so the gate compares in the right direction.
- The gate uses **only the sampled batch** `B_t`. There is no separate
  validation set inside the loop; the held-out set is reserved for the single
  final evaluation.

A candidate with a higher mean score that regresses a protected metric is
**rejected**. Record it in the rejected-candidate log with the regression noted.

## Paired-batch sampling

- Sample `B_t` once per round; run **both** `S_{t-1}` and the candidate on it.
- Use a seeded sampler (`seed + t`) so runs are reproducible and so you can
  re-attribute a regression to a specific batch.
- Batch size trades signal against cost. `|B_t| ≥ 2` is required for a non-zero
  volatility estimate; 5–10 is typical for short-horizon tasks.
- One pass through the optimization pool, or random batches with a round cap —
  either is fine; state which in the charter.

## Stop conditions

Stop when any holds:

- **Round cap** reached (`T_max`).
- **No-improvement streak**: `k` consecutive rounds with no accepted candidate.
- **All target issues resolved** and no new issue opened for `k` rounds.
- **Budget collapse**: `V_t` pinned at `V_max` for `k` rounds means the loop is
  thrashing — stop and review structure.

## Reading the dynamics

Plot two curves over the run (test score is for analysis only — it never drives
acceptance):

1. **Accepted-skill test score vs round.** Healthy: a strong revision in the
   first 1–2 rounds, and every later accepted skill stays above `S_0`.
   Unhealthy: accepted skills fluctuate around or below `S_0` — the gate is too
   loose or the batch is too small to give a reliable signal.
2. **Accepted-skill test score vs cumulative tokens.** Healthy: the score
   plateaus at a good level after a modest token spend. Unhealthy: strong
   candidates appear but keep getting rejected (gate too strict, or protected
   boundary set at an unreachable 0 for a noisy metric), or the curve climbs
   only after a very large spend (no memory — re-discovering failures).

SkillAdam reports ~67% fewer tokens and API calls than a naive loop at *better*
final quality, because the issue tracker stops re-discovery and the volatility
budget stops broad weakly-supported rewrites — roughly 4x the quality gain per
million optimization tokens.

## Trajectory-informed initialization

1. Fix a small **trace set** of tasks (disjoint from the held-out set; it may
   overlap the optimization pool).
2. Run the agent on the trace set with **no skill**, or a one-line stub.
3. Collect, per task: the outcome, the metric score, and the diagnostic
   (evaluator rationale, error, or a short trajectory summary).
4. Write `S_0` from that evidence: each recurring failure in the traces becomes
   an instruction; each thing the agent already did well is left alone.
5. Seed the issue tracker with the failures you saw but did not fully address in
   `S_0`, status `open`.

A blank or generic one-shot `S_0` typically costs several rounds of
rediscovering task basics and starts far below an iterated skill.

## Cross-model / cross-context transfer

If `S_final` will run somewhere other than where it was optimized:

- Deploy `S_final` **verbatim** on each additional model / context — no further
  optimization.
- For each, compute **retention** `= score_target / score_source` on the same
  held-out set.
- Report retention per setting. A skill consolidated through the issue tracker
  tends to retain better because the tracker's reconciliation pushes edits
  toward task procedure and away from source-model phrasing.
- Low retention on one setting → re-run the loop with the patch-generator
  instruction biased toward procedural edits ("describe *what* to do, not
  wording to copy").
