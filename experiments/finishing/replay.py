#!/usr/bin/env python3
"""Reconstruct one subject's work tree from its transcript.

Run 2's work copies were destroyed by the tmp reaper before they were scored
(recovery.md). The transcripts survived. This replays the fixture at HEAD
forward through the subject's deterministic file mutations.

    replay.py <run-dir> <dest> [--verify <surviving-out>] [--json]

Only `patch` and `write_file` are replayed. `terminal` and `execute_code` are
deliberately NOT: 66 of the shell commands mutate, and the set includes curl,
kill and pkill. What that omission costs is measured by --verify, not argued.
"""

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

REPLAYED = ("patch", "write_file")


def fixture_from_git(dest):
    """Materialise subject/ at HEAD -- never the working tree (amendment 1)."""
    repo = Path(__file__).resolve().parent
    proc = subprocess.run(
        ["git", "-C", str(repo), "archive", "HEAD", "subject"],
        capture_output=True, check=True,
    )
    tmp = Path(tempfile.mkdtemp(prefix="sitegen-replay-src-"))
    subprocess.run(["tar", "-x", "-C", str(tmp)], input=proc.stdout, check=True)
    shutil.copytree(tmp / "subject", dest)
    shutil.rmtree(tmp, ignore_errors=True)
    shutil.rmtree(dest / "out", ignore_errors=True)


def events(run_dir):
    """Tool-use events in file order, which is the order they were issued."""
    for line in (run_dir / "events.jsonl").open():
        try:
            event = json.loads(line)
        except ValueError:
            continue
        if event.get("type") == "tool_use" and event.get("name") in REPLAYED:
            yield event


def resolve(raw, dest):
    """Map a subject's absolute path back into the reconstruction.

    The subject worked in $TMPDIR/sitegen-runs/<id>. Anything outside that
    is a path the subject reached for beyond its work copy; it is refused
    rather than written, so a wandering subject cannot corrupt the tree.
    """
    path = Path(raw)
    if not path.is_absolute():
        return dest / path
    parts = path.resolve().parts
    if "sitegen-runs" not in parts:
        return None
    tail = parts[parts.index("sitegen-runs") + 2:]
    return dest.joinpath(*tail) if tail else None


def apply(event, dest):
    name, inp = event["name"], event.get("input") or {}
    target = resolve(inp.get("path", ""), dest)
    if target is None:
        return "outside"
    if name == "write_file":
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(inp.get("content", ""))
        return "ok"
    old, new = inp.get("old_string", ""), inp.get("new_string", "")
    if not target.exists():
        return "missing-file"
    text = target.read_text()
    if old == "":
        return "empty-old"
    if text.count(old) == 0:
        return "no-match"
    if text.count(old) > 1 and not inp.get("replace_all"):
        return "ambiguous"
    target.write_text(text.replace(old, new) if inp.get("replace_all")
                      else text.replace(old, new, 1))
    return "ok"


def tree_hashes(root):
    """Sorted relative path -> bytes digest, for every file under root."""
    import hashlib
    out = {}
    for path in sorted(Path(root).rglob("*")):
        if path.is_file():
            rel = str(path.relative_to(root))
            out[rel] = hashlib.sha256(path.read_bytes()).hexdigest()
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("run_dir", type=Path)
    ap.add_argument("dest", type=Path)
    ap.add_argument("--verify", type=Path,
                    help="surviving out/ to check the rebuild against")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    dest = args.dest.resolve()
    shutil.rmtree(dest, ignore_errors=True)
    dest.parent.mkdir(parents=True, exist_ok=True)
    fixture_from_git(dest)

    outcomes = []
    for event in events(args.run_dir):
        outcomes.append({"tool": event["name"],
                         "path": (event.get("input") or {}).get("path", ""),
                         "outcome": apply(event, dest)})

    applied = sum(1 for o in outcomes if o["outcome"] == "ok")
    result = {
        "subject": args.run_dir.name,
        "events_replayed": len(outcomes),
        "applied": applied,
        "failed": [o for o in outcomes if o["outcome"] != "ok"],
    }

    if args.verify:
        build = subprocess.run([sys.executable, "build.py"], cwd=dest,
                               capture_output=True, text=True, timeout=120)
        result["build_ok"] = build.returncode == 0
        result["build_output"] = (build.stdout + build.stderr)[-400:]
        if build.returncode == 0 and (dest / "out").is_dir():
            got, want = tree_hashes(dest / "out"), tree_hashes(args.verify)
            result["fidelity"] = "RECONSTRUCTED" if got == want else "UNRECONSTRUCTED"
            result["mismatch"] = sorted(
                set(got) ^ set(want)
                | {k for k in set(got) & set(want) if got[k] != want[k]})
        else:
            result["fidelity"] = "UNRECONSTRUCTED"
            result["mismatch"] = ["build failed"]

    print(json.dumps(result, indent=2) if args.json
          else f"{result['subject']}: {applied}/{len(outcomes)} applied, "
               f"{result.get('fidelity', 'not verified')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
