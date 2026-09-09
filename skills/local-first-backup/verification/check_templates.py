#!/usr/bin/env python3
"""Structural check on the skill's templates and references.

Confirms each template/reference exists, is non-trivial, and contains the
sections the SKILL.md promises. Standard library only.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

REQUIRED = {
    "templates/protection-charter.md": ["Sources and data classes", "Difficult sources",
                                        "Required copies per data class", "RPO", "RTO"],
    "templates/topology-map.md": ["Copy inventory", "3-2-1(+1) tally", "Credential map"],
    "templates/retention-policy.md": ["Retention tiers", "Repository sizing", "Encryption",
                                      "Sealed recovery record", "Key rotation"],
    "templates/restore-drill-report.md": ["Method", "Results", "Verdict", "PASS", "FAIL"],
    "templates/recovery-runbook.md": ["before touching anything", "list what is available",
                                      "restore, by scenario", "verify the restore",
                                      "Ransomware"],
    "references/topology-and-3-2-1.md": ["layer model", "3-2-1", "+1", "sync is not backup"],
    "references/tool-selection.md": ["Borg", "Restic", "Kopia", "full-disk imaging",
                                     "one tool across the fleet"],
    "references/retention-and-sizing.md": ["cost-of-loss", "repo_size", "bc", "headroom"],
    "references/encryption-and-keys.md": ["client-side", "sealed recovery record",
                                          "recovery contact", "Key rotation",
                                          "lost passphrase"],
    "references/credential-separation.md": ["Writer", "Prune", "Restore", "Admin",
                                            "append-only", "object-lock"],
    "references/difficult-sources.md": ["Databases", "Virtual machines", "Mail stores",
                                        "Password-manager vaults", "Cloud-only files"],
    "references/monitoring.md": ["silence", "dead-man", "Last successful backup",
                                 "Repository verification", "calibrated"],
    "references/restore-drills.md": ["sampled restore", "full drill", "rollback drill",
                                     "written runbook", "PASS"],
    "references/checklist.md": ["Pre-launch checklist", "drift review", "3-2-1",
                                "sealed recovery record"],
}

fails = 0
for rel, needles in REQUIRED.items():
    p = ROOT / rel
    if not p.is_file():
        print(f"  FAIL missing: {rel}")
        fails += 1
        continue
    text = p.read_text()
    if len(text) < 400:
        print(f"  FAIL too short: {rel} ({len(text)} bytes)")
        fails += 1
        continue
    missing = [n for n in needles if n.lower() not in text.lower()]
    if missing:
        print(f"  FAIL {rel}: missing {missing}")
        fails += 1
    else:
        print(f"  ok   {rel}")

# SKILL.md sanity
skill = (ROOT / "SKILL.md").read_text()
for needle in ["unattended-automation", "agent-automation", "3-2-1", "restore drill",
               "backup job succeeded", "credential"]:
    if needle.lower() not in skill.lower():
        print(f"  FAIL SKILL.md missing: {needle!r}")
        fails += 1
if fails == 0:
    print("  ok   SKILL.md references its siblings and core concepts")

print(f"\n{'FAILED' if fails else 'PASSED'}: {fails} problem(s)")
sys.exit(1 if fails else 0)
