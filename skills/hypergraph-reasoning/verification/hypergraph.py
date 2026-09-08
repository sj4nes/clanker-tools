"""Workflow checks for the `hypergraph-reasoning` skill (stdlib only).

Each check re-solves a case with a known answer using the operator the SKILL
prescribes, and shows the negative contrast: the naive method that the
guardrail exists to prevent.

  2. context collapse   : n-ary edge denies an out-of-scope query the shattered
                          binary edges wrongly grant
  3. temporal scope     : valid_time denies an expired approval a time-blind
                          check grants
  4. contradiction      : role typing suppresses a false owner-conflict and
                          still catches a genuine same-role one
  5. epistemic gating   : a `proposed` hypothesis and an unsourced edge stay
                          out of the facts list

Run via run.sh, or `python3 hypergraph.py`.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from datetime import date


# --- minimal hyperedge model -------------------------------------------------

@dataclass
class Hyperedge:
    id: str
    type: str
    roles: dict            # role -> node
    valid_start: date | None = None
    valid_end: date | None = None
    epistemic_status: str = "asserted"
    confidence: float = 1.0
    provenance: list = field(default_factory=list)   # list of source spans

    def holds_on(self, when: date) -> bool:
        if self.valid_start and when < self.valid_start:
            return False
        if self.valid_end and when > self.valid_end:
            return False
        return True


# --- operators -------------------------------------------------------------

def query_nary(edges, *, actor, resource, project):
    """Role-aware join: is `actor` authorized to use `resource` for `project`?

    An approval counts only if its scope role matches the project.
    """
    for e in edges:
        if e.type != "Decision":
            continue
        if e.roles.get("actor") == actor and e.roles.get("resource") == resource:
            if e.roles.get("scope") == project:
                return True
    return False


def query_binary_shatter(binary_edges, *, actor, resource, project):
    """The naive decomposition: does a path actor--uses-->resource exist at all?

    Scope was split into its own edge and is not re-checked -- context collapse.
    """
    for (a, rel, b) in binary_edges:
        if a == actor and rel == "uses" and b == resource:
            return True
    return False


def authorized_at(edges, *, action, when, respect_time):
    """Temporal-scope resolution. With respect_time=False the check is time-blind."""
    approvals = [e for e in edges
                 if e.type == "Decision" and e.roles.get("action") == action]
    if not respect_time:
        # naive method: an approval exists somewhere -> authorized. No interval
        # check, no awareness that a later policy supersedes it.
        return len(approvals) > 0
    approvals = [e for e in approvals if e.holds_on(when)]
    # a superseding Requirement in force blocks reliance on an old approval
    reqs = [e for e in edges
            if e.type == "Requirement" and e.roles.get("action") == action
            and e.holds_on(when)]
    if reqs and not any(e.roles.get("extra_signoff") == "done" for e in edges):
        return False
    return len(approvals) > 0


def contradictions(edges, *, role_typed):
    """Pairs of credible, time-overlapping edges with incompatible values.

    role_typed=True compares the full role signature (service + ownership role);
    role_typed=False compares only (service, "owner", *) -- the false-alarm mode.
    """
    out = []
    owners = [e for e in edges if e.type == "Claim" and "service" in e.roles]
    for i in range(len(owners)):
        for j in range(i + 1, len(owners)):
            a, b = owners[i], owners[j]
            if a.roles["service"] != b.roles["service"]:
                continue
            if not (a.holds_on(date(2026, 6, 1)) and b.holds_on(date(2026, 6, 1))):
                continue
            if role_typed:
                same_sig = a.roles.get("ownership_role") == b.roles.get("ownership_role")
            else:
                same_sig = True   # role-blind: any two "owner" claims collide
            if same_sig and a.roles.get("owner") != b.roles.get("owner"):
                out.append((a.id, b.id))
    return out


def synthesize(edges, *, flat):
    """Provenance-aware synthesis. flat=True is the naive method that puts
    everything in one list."""
    facts, uncertain, dropped = [], [], []
    for e in edges:
        claim = e.roles.get("claim", e.id)
        if not e.provenance:
            dropped.append(claim)
            if flat:
                facts.append(claim)
            continue
        if flat:
            facts.append(claim)
        elif e.epistemic_status in ("asserted", "observed"):
            facts.append(claim)
        else:
            uncertain.append(claim)
    return facts, uncertain, dropped


# --- checks --------------------------------------------------------------

def run() -> int:
    fail = 0

    # 2. context collapse ------------------------------------------------
    nary = [Hyperedge(
        id="d1", type="Decision",
        roles={"approver": "Finance", "actor": "Alice", "resource": "gpu-cluster",
               "scope": "project-x", "budget": "q3", "action": "use-gpu"},
        provenance=["Finance approved Alice's use of the GPU cluster for Project X under the Q3 budget"],
    )]
    shattered = [
        ("Alice", "uses", "gpu-cluster"),
        ("Alice", "works-on", "project-x"),
        ("gpu-cluster", "in", "q3"),
        ("Finance", "approved", "q3-budget"),
    ]
    nary_ans = query_nary(nary, actor="Alice", resource="gpu-cluster", project="project-y")
    bin_ans = query_binary_shatter(shattered, actor="Alice", resource="gpu-cluster", project="project-y")
    ok = (nary_ans is False) and (bin_ans is True)
    print(f"2. context collapse: n-ary says {nary_ans} (want False), "
          f"shattered says {bin_ans} (want True)  {'PASS' if ok else 'FAIL'}")
    print("   -> splitting the scope role out of the edge licenses a use the source never approved")
    fail += not ok
    # and the in-scope query must still succeed on the n-ary edge
    ok2 = query_nary(nary, actor="Alice", resource="gpu-cluster", project="project-x") is True
    print(f"   in-scope query on n-ary edge: {ok2 and 'True'}  {'PASS' if ok2 else 'FAIL'}")
    fail += not ok2

    # 3. temporal scope ------------------------------------------------
    tedges = [
        Hyperedge(id="appr", type="Decision",
                  roles={"action": "export-dataset", "approver": "DPO"},
                  valid_start=date(2025, 1, 1), valid_end=date(2025, 6, 30),
                  provenance=["one-off export approved Jan-Jun 2025"]),
        Hyperedge(id="pol", type="Requirement",
                  roles={"action": "export-dataset", "extra_signoff": "required"},
                  valid_start=date(2025, 4, 1), valid_end=None,
                  provenance=["from Apr 2025 all exports need a second sign-off"]),
    ]
    when = date(2026, 1, 1)
    time_aware = authorized_at(tedges, action="export-dataset", when=when, respect_time=True)
    time_blind = authorized_at(tedges, action="export-dataset", when=when, respect_time=False)
    ok = (time_aware is False) and (time_blind is True)
    print(f"3. temporal scope: time-aware says {time_aware} (want False), "
          f"time-blind says {time_blind} (want True)  {'PASS' if ok else 'FAIL'}")
    print("   -> the 2025 approval is expired and superseded by the policy; only valid_time catches it")
    fail += not ok

    # 4. contradiction with role typing --------------------------------
    now = (date(2026, 1, 1), None)
    cedges = [
        Hyperedge(id="o1", type="Claim",
                  roles={"service": "payments", "ownership_role": "operational", "owner": "team-a",
                         "claim": "payments operational owner = team-a"},
                  valid_start=now[0], provenance=["runbook"]),
        Hyperedge(id="o2", type="Claim",
                  roles={"service": "payments", "ownership_role": "budget", "owner": "team-b",
                         "claim": "payments budget owner = team-b"},
                  valid_start=now[0], provenance=["finance sheet"]),
        Hyperedge(id="o3", type="Claim",
                  roles={"service": "payments", "ownership_role": "operational", "owner": "team-c",
                         "claim": "payments operational owner = team-c"},
                  valid_start=now[0], provenance=["oncall wiki"]),
    ]
    typed = contradictions(cedges, role_typed=True)
    blind = contradictions(cedges, role_typed=False)
    # role-typed: only o1 vs o3 (both operational). role-blind: also o1-o2, o2-o3.
    ok = (set(typed) == {("o1", "o3")}) and (("o1", "o2") in blind)
    print(f"4. contradiction: role-typed finds {typed} (want [('o1','o3')]), "
          f"role-blind also flags o1-o2  {'PASS' if ok else 'FAIL'}")
    print("   -> operational-owner vs budget-owner is not a conflict; same-role clash is")
    fail += not ok

    # 5. epistemic-status / provenance gating -------------------------
    sedges = [
        Hyperedge(id="s1", type="Decision",
                  roles={"claim": "Maya chose managed PostgreSQL"},
                  epistemic_status="asserted", provenance=["meeting notes"]),
        Hyperedge(id="s2", type="CausalHypothesis",
                  roles={"claim": "PostgreSQL will cut cost 30%"},
                  epistemic_status="proposed", provenance=["agent inference"]),
        Hyperedge(id="s3", type="Claim",
                  roles={"claim": "the DBA team was disbanded in 2024"},
                  epistemic_status="asserted", provenance=[]),   # no source span
    ]
    facts, uncertain, dropped = synthesize(sedges, flat=False)
    flat_facts, _, _ = synthesize(sedges, flat=True)
    ok = ("Maya chose managed PostgreSQL" in facts
          and "PostgreSQL will cut cost 30%" in uncertain
          and "PostgreSQL will cut cost 30%" not in facts
          and "the DBA team was disbanded in 2024" in dropped
          and "the DBA team was disbanded in 2024" not in facts)
    ok_contrast = "PostgreSQL will cut cost 30%" in flat_facts and \
                  "the DBA team was disbanded in 2024" in flat_facts
    print(f"5. epistemic gating: facts={facts}")
    print(f"   uncertain={uncertain}  dropped(no provenance)={dropped}  "
          f"{'PASS' if ok else 'FAIL'}")
    print(f"   -> flat synthesis wrongly promotes proposed + unsourced claims to facts: "
          f"{'PASS' if ok_contrast else 'FAIL'}")
    fail += not ok
    fail += not ok_contrast

    print()
    print("ALL CHECKS PASS" if fail == 0 else f"{fail} CHECK(S) FAILED")
    return 1 if fail else 0


if __name__ == "__main__":
    raise SystemExit(run())
