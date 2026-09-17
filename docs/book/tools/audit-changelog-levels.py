#!/usr/bin/env python3
"""Written for chapter II.5 (ledger C-II-32..42) as a report over the changelog
clauses nothing gated. Promoted on 2026-09-17 to tools/check-changelogs.py,
which now gates them from tools/check-skills.sh. This runs it with the report.

    python3 docs/book/tools/audit-changelog-levels.py     # from the repo root
"""
import pathlib
import runpy
import sys

sys.argv = [sys.argv[0], "--report"]
runpy.run_path(str(pathlib.Path(__file__).resolve().parents[3] / "tools/check-changelogs.py"),
               run_name="__main__")
