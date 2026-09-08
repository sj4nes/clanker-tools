#!/usr/bin/env python3
"""Gate checker for a nonfiction-book project system.

Validates the three machine-checkable artifacts (positioning brief, claim
ledger, fat outline) against the phase gates in the SKILL. Every finding is an
ERROR (a gate is not met) or a WARN (worth a human look). Exit status is 1 if
any ERROR is found, else 0.

Fixtures are JSON here so the check runs on the Python standard library alone;
the shipped templates are YAML with the same field names.

Usage:  check.py DIR        # DIR holds positioning-brief.json, claim-ledger.json,
                            #   fat-outline.json
"""
import json
import pathlib
import re
import sys

BOOK_TYPES = {"prescriptive", "explanatory", "narrative", "argument-driven",
              "memoir", "reference"}
CLAIM_TYPES = {"fact", "statistic", "interpretation", "recommendation",
               "quote", "anecdote", "prediction"}
SOURCE_TIERS = {"primary", "secondary-high-quality", "tertiary", "discovery"}
CITED_STATUSES = {"footnote", "endnote", "footnote/endnote", "bibliography"}
CITECHECK_OK = {"verified", "verified-with-correction"}
STRUCTURES = {"problem->solution", "beginner->advanced", "past->present->future",
              "myth->evidence->action", "case-study->principle",
              "journey/chronology"}
VAGUE_OUTCOME = re.compile(
    r"know more about|learn about|understand the topic|be aware of|"
    r"get an overview|familiar with the subject", re.I)

findings = []


def err(code, msg):
    findings.append(("ERROR", code, msg))


def warn(code, msg):
    findings.append(("WARN", code, msg))


def load(d, name):
    p = pathlib.Path(d) / name
    if not p.exists():
        err("missing-artifact", f"{name} not found in {d}")
        return None
    try:
        return json.loads(p.read_text())
    except json.JSONDecodeError as e:
        err("bad-json", f"{name}: {e}")
        return None


def check_positioning(b):
    if b is None:
        return
    promise = b.get("one_sentence_promise", "").strip()
    if not promise:
        err("promise-empty", "positioning: one_sentence_promise is empty")
    else:
        low = promise.lower()
        if not (("for " in low) and
                ("help" in low) and
                (" by " in low or " through " in low)):
            warn("promise-shape",
                 "positioning: promise does not read as "
                 "'For [reader], this book helps them [outcome] by [approach]'")
    pc = b.get("promise_check", {})
    for k in ("who_is_it_for", "what_problem", "what_outcome",
              "unique_angle", "why_a_book"):
        if not str(pc.get(k, "")).strip():
            err("promise-check-incomplete",
                f"positioning: promise_check.{k} is empty")
    who = str(pc.get("who_is_it_for", ""))
    if re.search(r"everyone (interested|who)|anyone interested|all readers", who, re.I):
        err("reader-not-concrete",
            "positioning: who_is_it_for is not a concrete primary reader "
            f"({who!r})")
    bt = b.get("book_type", "")
    if bt not in BOOK_TYPES:
        err("book-type-invalid",
            f"positioning: book_type {bt!r} is not one of {sorted(BOOK_TYPES)}")
    if not str(b.get("mode_mixing_risk", "")).strip():
        warn("mode-mixing-unstated",
             "positioning: mode_mixing_risk is empty")
    comps = b.get("comparable_titles", [])
    if len(comps) < 3:
        err("too-few-comps",
            f"positioning: {len(comps)} comparable titles, need >= 3")
    if not b.get("will_not_cover"):
        err("no-exclusions",
            "positioning: will_not_cover is empty -- disciplined exclusion is "
            "required to pass the gate")
    if b.get("blocking_questions"):
        err("open-blocking-questions",
            f"positioning: {len(b['blocking_questions'])} blocking question(s) "
            "unanswered")


def check_ledger(l):
    if l is None:
        return set()
    ids = set()
    types_seen = set()
    for c in l.get("claims", []):
        cid = c.get("id", "<no-id>")
        ids.add(cid)
        ct = c.get("claim_type")
        types_seen.add(ct)
        if ct not in CLAIM_TYPES:
            err("claim-type-invalid",
                f"ledger {cid}: claim_type {ct!r} invalid")
        tier = c.get("source_tier")
        if tier not in SOURCE_TIERS:
            err("source-tier-invalid",
                f"ledger {cid}: source_tier {tier!r} invalid")
        conf = c.get("confidence")
        if conf == "high" and tier == "discovery":
            err("discovery-load-bearing",
                f"ledger {cid}: high-confidence claim rests on a discovery-tier "
                "source")
        cs = str(c.get("citation_status", "")).lower()
        if conf == "high" and cs in CITED_STATUSES:
            if c.get("citation_check") not in CITECHECK_OK:
                err("citation-unverified",
                    f"ledger {cid}: high-confidence formally-cited claim has "
                    f"citation_check={c.get('citation_check')!r} "
                    f"(need one of {sorted(CITECHECK_OK)})")
        if not str(c.get("date_checked", "")).strip():
            warn("no-date-checked", f"ledger {cid}: date_checked is empty")
        if c.get("drafting_status") not in {"resolved", "draft-anyway",
                                            "blocking"}:
            warn("drafting-status-odd",
                 f"ledger {cid}: drafting_status {c.get('drafting_status')!r}")
        if c.get("drafting_status") == "blocking":
            err("claim-blocking",
                f"ledger {cid}: drafting_status is 'blocking' -- cannot enter "
                "drafting")
    if {"fact", "interpretation"} - types_seen == {"interpretation"} and \
            "recommendation" in types_seen:
        warn("no-interpretation-rows",
             "ledger: recommendations present but no interpretation rows -- "
             "check fact/interpretation/recommendation are genuinely separated")
    return ids


def toposort(edges):
    """Kahn's algorithm. Returns (order, cycle_nodes)."""
    succ = {}
    indeg = {}
    for a, b in edges:
        succ.setdefault(a, set())
        succ.setdefault(b, set())
        indeg.setdefault(a, 0)
        indeg.setdefault(b, 0)
    for a, b in edges:
        if b not in succ[a]:
            succ[a].add(b)
            indeg[b] += 1
    queue = sorted(n for n, d in indeg.items() if d == 0)
    order = []
    while queue:
        n = queue.pop(0)
        order.append(n)
        for m in sorted(succ[n]):
            indeg[m] -= 1
            if indeg[m] == 0:
                queue.append(m)
        queue.sort()
    cycle = [n for n, d in indeg.items() if d > 0]
    return order, cycle


def check_outline(o, ledger_ids):
    if o is None:
        return
    if o.get("governing_structure") not in STRUCTURES:
        err("structure-invalid",
            f"outline: governing_structure {o.get('governing_structure')!r} "
            f"not one of {sorted(STRUCTURES)}")
    edges = [tuple(e) for e in o.get("concept_edges", [])]
    if edges:
        order, cycle = toposort(edges)
        if cycle:
            err("concept-cycle",
                f"outline: concept_edges contain a cycle through {sorted(cycle)}")
        else:
            print(f"  concept order: {' -> '.join(order)}")
    chapters = o.get("chapters", [])
    if not chapters:
        err("no-chapters", "outline: no chapters")
    for ch in chapters:
        n = ch.get("number", "?")
        rcn = str(ch.get("reader_can_now", "")).strip()
        if not rcn:
            err("reader-can-now-empty",
                f"outline ch{n}: reader_can_now is empty")
        elif VAGUE_OUTCOME.search(rcn):
            err("reader-can-now-vague",
                f"outline ch{n}: reader_can_now is vague ({rcn!r}) -- name a "
                "capability, not 'know more about X'")
        if not str(ch.get("distinct_from_neighbours", "")).strip():
            err("chapter-not-distinct",
                f"outline ch{n}: distinct_from_neighbours is empty")
        if not str(ch.get("through_line_transition", "")).strip():
            err("no-through-line",
                f"outline ch{n}: through_line_transition is empty")
        for rid in ch.get("key_evidence", []):
            if rid not in ledger_ids:
                err("dangling-evidence",
                    f"outline ch{n}: key_evidence {rid} has no claim-ledger row")
    # neighbour repetition: identical central claims
    claims = [(_c.get("number"), str(_c.get("central_claim_or_skill", "")).strip().lower())
              for _c in chapters]
    for i in range(1, len(claims)):
        if claims[i][1] and claims[i][1] == claims[i - 1][1]:
            err("chapter-repeats-neighbour",
                f"outline ch{claims[i][0]}: central claim identical to "
                f"ch{claims[i-1][0]}")


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    d = sys.argv[1]
    print(f"== checking {d} ==")
    b = load(d, "positioning-brief.json")
    l = load(d, "claim-ledger.json")
    o = load(d, "fat-outline.json")
    check_positioning(b)
    ledger_ids = check_ledger(l)
    check_outline(o, ledger_ids)

    errs = [f for f in findings if f[0] == "ERROR"]
    for level, code, msg in findings:
        print(f"  {level:5} [{code}] {msg}")
    if errs:
        print(f"FAIL: {len(errs)} error(s), {len(findings) - len(errs)} warning(s)")
        sys.exit(1)
    print(f"PASS: 0 errors, {len(findings)} warning(s)")
    sys.exit(0)


if __name__ == "__main__":
    main()
