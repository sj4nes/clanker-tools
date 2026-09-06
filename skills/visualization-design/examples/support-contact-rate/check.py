#!/usr/bin/env python3
"""Worked end-to-end example for the `visualization-design` skill.

Takes the messy `data.csv`, runs the cleaning and the graphical-integrity
checks the skill prescribes, and confirms the numbers quoted in
`walkthrough.md`. Also emits `chart_data.json` (the tidy series the
Vega-Lite spec binds to).

Pure stdlib. Run:  python3 check.py
Exit 0 iff every prescribed check behaves as `walkthrough.md` claims.
"""
from __future__ import annotations

import csv
import json
import pathlib
import re

HERE = pathlib.Path(__file__).parent
MONTHS = {m: i + 1 for i, m in enumerate(
    ["jan", "feb", "mar", "apr", "may", "jun",
     "jul", "aug", "sep", "oct", "nov", "dec"])}


def parse_period(raw: str) -> str:
    """Normalise the inconsistent month strings to YYYY-MM."""
    raw = raw.strip()
    m = re.fullmatch(r"(\d{4})[-/](\d{1,2})", raw)
    if m:
        return f"{int(m.group(1)):04d}-{int(m.group(2)):02d}"
    m = re.fullmatch(r"([A-Za-z]{3,})\s+(\d{4})", raw)
    if m:
        return f"{int(m.group(2)):04d}-{MONTHS[m.group(1)[:3].lower()]:02d}"
    raise ValueError(f"unrecognised period: {raw!r}")


def load() -> list[dict]:
    rows = []
    with (HERE / "data.csv").open() as fh:
        for r in csv.DictReader(fh):
            rows.append({
                "period": parse_period(r["period"]),
                "received": int(r["tickets_received"]) if r["tickets_received"] else None,
                "resolved": int(r["tickets_resolved"]) or None,
                "customers": int(r["active_customers"]),
                "note": r["note"].strip(),
                "partial": "partial month" in r["note"],
            })
    return rows


def approx(a: float, b: float, tol: float = 0.05) -> bool:
    return abs(a - b) <= tol


def main() -> int:
    rows = load()
    ok = True

    def check(label: str, cond: bool, detail: str = "") -> None:
        nonlocal ok
        ok &= cond
        print(f"  [{'ok' if cond else 'XX'}] {label}" + (f"  ({detail})" if detail else ""))

    print("=== 1. date normalisation ===")
    periods = [r["period"] for r in rows]
    check("12 months, sorted, unique",
          periods == sorted(set(periods)) and len(periods) == 12,
          ", ".join(periods[:4]) + ", ...")

    print("\n=== 2. missing / partial data is carried, not silently filled ===")
    may = next(r for r in rows if r["period"] == "2024-05")
    dec = next(r for r in rows if r["period"] == "2024-12")
    check("May received is None (system migration)", may["received"] is None,
          may["note"])
    check("December flagged partial", dec["partial"], dec["note"])

    print("\n=== 3. the confound: raw counts vs contact rate ===")
    complete = [r for r in rows if r["received"] is not None and not r["partial"]]
    first, last = complete[0], complete[-1]
    raw_growth = last["received"] / first["received"] - 1
    rate = lambda r: r["received"] / r["customers"] * 100
    rate_change = rate(last) / rate(first) - 1
    print(f"     {first['period']}: {first['received']} tickets / "
          f"{first['customers']} customers = {rate(first):.1f} per 100")
    print(f"     {last['period']}: {last['received']} tickets / "
          f"{last['customers']} customers = {rate(last):.1f} per 100")
    check("raw ticket volume rose ~53%", approx(raw_growth, 0.527, 0.02),
          f"{raw_growth:+.1%}")
    check("contact RATE fell ~18% over the same period",
          rate_change < -0.15 and rate_change > -0.22, f"{rate_change:+.1%}")
    check("the two tell opposite stories (sign flip)",
          raw_growth > 0 > rate_change)

    print("\n=== 4. naive quarterly bar chart is doubly wrong ===")
    # a naive analyst sums whatever months are present per quarter
    q = {1: [1, 2, 3], 2: [4, 5, 6], 3: [7, 8, 9], 4: [10, 11, 12]}
    by_month = {int(r["period"][-2:]): r for r in rows}
    naive_q = {k: sum(by_month[m]["received"] or 0 for m in v) for k, v in q.items()}
    print(f"     naive quarterly received: {naive_q}")
    check("Q2 total understated: only 2 of 3 months have data",
          naive_q[2] < naive_q[1], f"Q2={naive_q[2]} < Q1={naive_q[1]}")
    check("Q4 total dragged down by the partial December",
          naive_q[4] < naive_q[3], f"Q4={naive_q[4]} < Q3={naive_q[3]}")

    print("\n=== 5. truncated-baseline lie factor on the naive bars ===")
    # y-axis starts at 2000 (a 'zoom in on the interesting part' choice)
    base = 2000
    lo_q, hi_q = naive_q[2], naive_q[3]      # smallest vs largest *complete-ish*
    data_ratio = hi_q / lo_q
    shown_ratio = (hi_q - base) / (lo_q - base)
    lie = shown_ratio / data_ratio
    print(f"     data ratio Q3/Q2 = {data_ratio:.2f}; "
          f"shown (bars from {base}) = {shown_ratio:.2f}")
    check("truncated bars exaggerate the gap by > 2x", lie > 2.0,
          f"lie factor = {lie:.1f}")

    print("\n=== 6. December, pro-rated, is consistent with the falling trend ===")
    dec_rate_partial = dec["received"] / dec["customers"] * 100
    dec_rate_annualised = (dec["received"] * 31 / 20) / dec["customers"] * 100
    print(f"     Dec as-reported rate = {dec_rate_partial:.1f} per 100 "
          f"(20/31 days) -> looks like a crash")
    print(f"     Dec pro-rated to 31 days = {dec_rate_annualised:.1f} per 100 "
          f"-> on trend below Nov's {rate(last):.1f}")
    check("as-reported December would mislead (>25% below trend)",
          dec_rate_partial < rate(last) * 0.75)
    check("pro-rated December is on trend (within 5% of Nov)",
          approx(dec_rate_annualised, rate(last), rate(last) * 0.05))

    print("\n=== 7. emit tidy chart data ===")
    series = []
    for r in rows:
        rec = {"period": r["period"] + "-01",
               "customers": r["customers"],
               "received": r["received"],
               "status": "partial" if r["partial"]
                         else ("missing" if r["received"] is None else "observed")}
        rec["contact_rate"] = (round(r["received"] / r["customers"] * 100, 2)
                               if r["received"] is not None else None)
        series.append(rec)
    (HERE / "chart_data.json").write_text(json.dumps(series, indent=2) + "\n")
    check("chart_data.json written", (HERE / "chart_data.json").exists())

    spec = json.loads((HERE / "chart.vl.json").read_text())
    check("chart.vl.json is valid JSON with a description (alt text)",
          bool(spec.get("description")) and len(spec["description"]) > 120)
    check("chart.vl.json y-scale starts at zero",
          spec["encoding"]["y"]["scale"]["domain"][0] == 0)
    embedded = {r["month"]: r for r in spec["data"]["values"]
                if r.get("status") == "observed"}
    check("spec's embedded rates match the computed series",
          all(approx(embedded[int(r["period"][5:7])]["contact_rate"],
                     r["contact_rate"], 0.01)
              for r in series
              if r["status"] == "observed"))

    print("\n=== summary ===")
    print("  ALL CHECKS PASS" if ok else "  SOME CHECKS FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
