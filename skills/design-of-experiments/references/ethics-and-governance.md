# Ethics, safety, and governance

Apply a risk tier **before** proposing execution. The tier sets the minimum
safeguards; do not go below them.

| Risk tier | Examples | Minimum safeguards |
|---|---|---|
| **Low** | UI wording, non-sensitive workflow changes, simulation-only tuning | Data-quality checks, reversible rollout, guardrail metrics |
| **Moderate** | Pricing, labor allocation, education, workplace processes, public-facing operations | Stakeholder review, fairness / disparate-impact checks, active monitoring, tested rollback plan |
| **High** | Health, safety, credit, housing, employment, policing, benefits, vulnerable populations | Independent ethics / legal review, informed consent or a documented lawful basis, enhanced monitoring, pre-registration, human oversight, a data-monitoring committee where lives or livelihoods are at stake |
| **Prohibited / escalate** | Exposing people to serious harm, deceptive high-risk manipulation, unlawful discrimination, unsafe system operation | Do not proceed without appropriate authority, review, and safeguards — escalate |

## Governance checklist

- Is there informed consent, or a legitimate documented basis for a waiver?
- Is the control group deprived of necessary care, safety, or an essential
  service? If so, the design is not acceptable as stated.
- Could randomization create inequitable access or concentrate harm on a group?
- Is the intervention reversible? How fast?
- Is there a pre-specified stop / rollback condition, and has the rollback been
  tested?
- Are privacy, retention, and data-minimization requirements met? Is
  personally identifying data necessary, or can the analysis run on aggregates?
- Could the experiment create feedback loops that harm non-participants (e.g.
  marketplace price effects, model-training loops)?
- Is the result likely to be overgeneralized beyond the eligible population? Say
  so in the report.
- Who reviews the plan, and are they independent of the team that benefits from
  a positive result?

## Pre-registration

Pre-register when the experiment is confirmatory, high-stakes, externally
scrutinized, or likely to be cited as evidence. Register, before launch and in a
timestamped record:

- the primary hypothesis and estimand;
- the primary outcome and its operational definition;
- the design and assignment mechanism;
- the sample size and its assumptions;
- the full analysis plan (all fields from
  [`analysis-plan.md`](analysis-plan.md));
- the decision rule.

Anything decided after launch, or after seeing outcomes, is reported as
exploratory and clearly separated from the confirmatory results.

## Priority order when designing

1. Safety, ethics, legality, privacy, reversibility.
2. A clearly defined decision and estimand.
3. Valid causal or model-conditional inference.
4. Measurement integrity and data quality.
5. Practical feasibility and operational simplicity.
6. Statistical efficiency and reproducibility.
7. Transparent uncertainty and limitations.
