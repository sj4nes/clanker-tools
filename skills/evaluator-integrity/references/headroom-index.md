# Normalizing and pooling benchmark scores

Reference material for behaviour 6 of [`../SKILL.md`](../SKILL.md). This is
lookup, not guidance: the three equations, the source-weight table, and the
rules for when two numbers may be pooled at all. Every formula here is
asserted in [`../verification/checks.bc`](../verification/checks.bc).

Source: Duan, Liu, Tang, Chen, Zhou et al., *The Last AI Built by Humans:
Toward Genuine Recursive Self-Improvement*, arXiv:2609.11873v1 (Sept 2026),
§2.1 and Eq. 1–3. The paper applies this to 393 model–benchmark observations
across ten capability domains; the machinery generalizes to any pooling of
heterogeneous scores.

---

## 1. When two scores may be pooled at all

Two results belong to the same **protocol-link family** only when:

- the benchmark version **and** the evaluation harness are both stable, or
- evaluations of overlapping models provide a defensible bridge between the
  two protocols.

Results on incompatible versions or harnesses stay in the audit record and are
**excluded from the trajectory** — not silently averaged in. In the paper's own
audit this rule excluded 16 of 33 candidate results.

This is the rule most often broken in practice, and it is prior to everything
below: a normalization applied across an unlinked protocol change produces a
clean number from incomparable inputs.

## 2. Weighted consensus across sources (Eq. 1)

When several sources report the same model on the same benchmark family,
variant, and evaluation mode:

```
sbar_mbh = sum_i( w_i * s_imbh ) / sum_i( w_i )
```

Base weights by source type:

| Source | Base weight |
|---|---|
| Benchmark-owner table | 3 |
| Independent common-harness evaluation | 2.5 |
| Combined benchmark or model report | 2 |
| Model-author table | 1 |

**First-party values are multiplied by a further 0.75.** The paper calls this
a practical sensitivity adjustment; its effect is to keep a self-report in the
pool while limiting its pull.

Worked case (asserted in `checks.bc` §3): an owner table at 80 and a
model-author self-report at 90 give a weighted consensus of **82**, against an
unweighted mean of **85**. The naive mean runs 3 points high.

## 3. Headroom-Closed Index (Eq. 2)

Raw scores from different benchmarks are not on a common scale, so normalize
against what was left to win:

```
H_mbh = 100 * (sbar_mbh - f_b0) / (100 - f_b0)
```

where `f_b0` is the **90th-percentile model score in the benchmark's entry
year**. So `H = 0` is the entry-year frontier and `H = 100` is a perfect
score. `H` may be negative for a model below the frontier.

The quantity to report alongside a score is the **fraction of remaining
headroom closed**:

```
(s_new - s_old) / (100 - s_old)
```

Worked case (`checks.bc` §2): +4 points from 92 closes **50%** of what
remained; +4 points from 40 closes **6.7%**. Identical raw deltas, a **7.5×**
difference in progress. Near the ceiling, a real improvement has almost no
room to register — which is why a flat line on a saturated benchmark is not
evidence of a plateau.

## 4. Domain trajectory across families (Eq. 3)

To combine benchmark families into one domain number for year `y`:

```
T_dy = sum_b( sqrt(n_by) * Q_by ) / sum_b( sqrt(n_by) )
```

where `Q_by` is the 90th-percentile HCI frontier for family `b` in year `y`,
and `n_by` is the number of distinct models contributing to that
family-year frontier.

**Why `sqrt(n)` and not `n`, and not 1:** a family with one reported model
must not weigh the same as a family with sixteen, and must not be erased by
it either. Worked case (`checks.bc` §4), a 16-model family at 60 and a
1-model family at 90:

| Weighting | Domain value | Effect |
|---|---|---|
| naive mean | 75 | the thin family moves the number 9 points |
| `sqrt(n)` | 66 | contributes, does not dominate |
| linear `n` | 61.8 | thin family nearly erased |

## 5. What the index does not fix

- **A trend built from one aggregate benchmark conceals both level and
  shape.** The paper's own example: broad knowledge rose 32.8, 26.9 and 17.6
  HCI points across three annual transitions (decelerating), while advanced
  mathematics rose 32.8 then 53.6 (accelerating). A single pooled number shows
  neither pattern.
- **`f_b0` is a choice.** The entry-year 90th percentile is a defensible
  anchor, not the only one, and it is fixed forever once set. Changing it
  retroactively re-scales history.
- **Normalization cannot repair an unlinked protocol change** — see §1. The
  dashed segments in the paper's own cybersecurity trajectory are exactly this
  caveat drawn on the chart.
