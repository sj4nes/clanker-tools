#!/usr/bin/env python3
"""Reference model for the local-first-backup skill.

A small, standard-library-only model of a versioned, encrypted, append-only
backup repository. It exists to make the skill's load-bearing claims executable:

  1. a restore reproduces the source byte-for-byte
  2. a file deleted from the source is still restorable from an earlier snapshot
  3. a snapshot taken after "ransomware" does not overwrite clean history, and a
     rollback to the pre-event snapshot recovers the plaintext
  4. the append-only WRITER credential can add a snapshot but cannot prune/delete
  5. pruning with the PRUNE credential honours the retention tiers and no more
  6. the staleness monitor fires when a device's last-success ages past its
     threshold even though nothing logged an error

Run: python3 runner.py   (exits non-zero on any failed assertion)
"""

from __future__ import annotations

import hashlib
import sys
from dataclasses import dataclass, field
from datetime import datetime, timedelta

# --------------------------------------------------------------------------- #
# tiny test harness
# --------------------------------------------------------------------------- #

_PASS = 0
_FAIL = 0


def check(desc: str, cond: bool) -> None:
    global _PASS, _FAIL
    if cond:
        _PASS += 1
        print(f"  ok   {desc}")
    else:
        _FAIL += 1
        print(f"  FAIL {desc}")


def expect_denied(desc: str, fn) -> None:
    try:
        fn()
    except PermissionError:
        check(desc, True)
    except Exception as exc:  # noqa: BLE001
        check(f"{desc} (raised {type(exc).__name__}, expected PermissionError)", False)
    else:
        check(f"{desc} (call succeeded, expected denial)", False)


# --------------------------------------------------------------------------- #
# model
# --------------------------------------------------------------------------- #

# capabilities a credential may carry
WRITE = "write"      # create a new snapshot
PRUNE = "prune"      # forget + delete snapshots per policy
RESTORE = "restore"  # read snapshots
ADMIN = "admin"      # re-key / destroy


@dataclass(frozen=True)
class Credential:
    name: str
    caps: frozenset


WRITER_CRED = Credential("laptop-a-writer", frozenset({WRITE, RESTORE}))
PRUNE_CRED = Credential("maintenance-prune", frozenset({PRUNE, RESTORE}))
RESTORE_CRED = Credential("operator-restore", frozenset({RESTORE}))
ADMIN_CRED = Credential("sealed-admin", frozenset({WRITE, PRUNE, RESTORE, ADMIN}))


class DecryptionError(Exception):
    pass


@dataclass
class Snapshot:
    id: str
    time: datetime
    # path -> content hash
    tree: dict = field(default_factory=dict)


class Repo:
    """Content-addressed, 'encrypted', append-only-capable snapshot store."""

    def __init__(self, passphrase: str):
        self._passphrase = passphrase
        self._blobs: dict[str, bytes] = {}      # hash -> ciphertext
        self.snapshots: list[Snapshot] = []
        self._counter = 0

    # --- crypto stand-in ------------------------------------------------- #
    def _seal(self, data: bytes) -> bytes:
        # not real crypto - a reversible transform keyed by the passphrase,
        # enough to model "wrong key => cannot read"
        k = hashlib.sha256(self._passphrase.encode()).digest()
        return bytes(b ^ k[i % len(k)] for i, b in enumerate(data))

    def _open(self, blob: bytes, passphrase: str) -> bytes:
        k = hashlib.sha256(passphrase.encode()).digest()
        return bytes(b ^ k[i % len(k)] for i, b in enumerate(blob))

    # --- writes -------------------------------------------------------- #
    def backup(self, cred: Credential, source: dict, when: datetime) -> Snapshot:
        if WRITE not in cred.caps:
            raise PermissionError(f"{cred.name} may not create snapshots")
        tree = {}
        for path, content in source.items():
            h = hashlib.sha256(content).hexdigest()
            if h not in self._blobs:
                self._blobs[h] = self._seal(content)
            tree[path] = h
        self._counter += 1
        snap = Snapshot(id=f"snap{self._counter:03d}", time=when, tree=dict(tree))
        self.snapshots.append(snap)
        return snap

    def forget_and_prune(self, cred: Credential, keep: dict, now: datetime) -> list[str]:
        if PRUNE not in cred.caps:
            raise PermissionError(f"{cred.name} may not prune")
        keepset = _apply_retention(self.snapshots, keep, now)
        removed = [s.id for s in self.snapshots if s.id not in keepset]
        self.snapshots = [s for s in self.snapshots if s.id in keepset]
        # blob GC
        live = {h for s in self.snapshots for h in s.tree.values()}
        self._blobs = {h: b for h, b in self._blobs.items() if h in live}
        return removed

    # --- reads -------------------------------------------------------- #
    def restore(self, cred: Credential, snap_id: str, passphrase: str) -> dict:
        if RESTORE not in cred.caps:
            raise PermissionError(f"{cred.name} may not restore")
        snap = next((s for s in self.snapshots if s.id == snap_id), None)
        if snap is None:
            raise KeyError(snap_id)
        if hashlib.sha256(passphrase.encode()).digest() != hashlib.sha256(
            self._passphrase.encode()
        ).digest():
            raise DecryptionError("wrong repository passphrase")
        return {p: self._open(self._blobs[h], passphrase) for p, h in snap.tree.items()}

    def check(self) -> bool:
        """Repository integrity: every referenced blob is present and intact."""
        for snap in self.snapshots:
            for path, h in snap.tree.items():
                if h not in self._blobs:
                    return False
                if hashlib.sha256(self._open(self._blobs[h], self._passphrase)).hexdigest() != h:
                    return False
        return True


def _apply_retention(snaps: list[Snapshot], keep: dict, now: datetime) -> set[str]:
    """Keep the last N of each bucket (hourly/daily/monthly/yearly)."""
    ordered = sorted(snaps, key=lambda s: s.time, reverse=True)
    keepset: set[str] = set()

    def bucket_key(dt: datetime, unit: str) -> str:
        if unit == "hourly":
            return dt.strftime("%Y-%m-%d-%H")
        if unit == "daily":
            return dt.strftime("%Y-%m-%d")
        if unit == "monthly":
            return dt.strftime("%Y-%m")
        return dt.strftime("%Y")

    for unit in ("hourly", "daily", "monthly", "yearly"):
        want = keep.get(unit, 0)
        if want <= 0:
            continue
        seen: set[str] = set()
        for s in ordered:
            bk = bucket_key(s.time, unit)
            if bk not in seen:
                seen.add(bk)
                keepset.add(s.id)
                if len(seen) >= want:
                    break
    return keepset


# --------------------------------------------------------------------------- #
# staleness monitor (silence detection)
# --------------------------------------------------------------------------- #

@dataclass
class DeviceStatus:
    device: str
    last_success: datetime
    last_error: str | None = None


def staleness_alerts(statuses: list[DeviceStatus], now: datetime,
                     interval: timedelta, page_multiple: int = 4) -> list[str]:
    alerts = []
    for st in statuses:
        age = now - st.last_success
        if age > interval * page_multiple:
            alerts.append(f"PAGE {st.device}: no successful backup in {age}")
        elif age > interval * 2:
            alerts.append(f"WARN {st.device}: last backup {age} ago")
    return alerts


# --------------------------------------------------------------------------- #
# scenarios
# --------------------------------------------------------------------------- #

def sha(d: dict) -> dict:
    return {p: hashlib.sha256(c).hexdigest() for p, c in d.items()}


def main() -> int:
    t0 = datetime(2026, 9, 1, 2, 0, 0)
    PASS = "correct horse battery staple"
    repo = Repo(passphrase=PASS)

    # --- day 1: initial source, first backup ------------------------------
    source = {
        "home/docs/taxes-2025.pdf": b"TAX RETURN 2025 ... lots of numbers",
        "home/photos/IMG_0001.jpg": b"\xff\xd8\xff\xe0 jpeg bytes one",
        "home/photos/IMG_0002.jpg": b"\xff\xd8\xff\xe0 jpeg bytes two",
        "home/projects/app/main.py": b"print('v1')\n",
    }
    snap1 = repo.backup(WRITER_CRED, source, t0)

    # (1) restore reproduces the source byte-for-byte
    restored = repo.restore(RESTORE_CRED, snap1.id, PASS)
    check("restore reproduces the source byte-for-byte", restored == source)
    check("integrity check passes after first backup", repo.check())

    # wrong passphrase cannot read
    try:
        repo.restore(RESTORE_CRED, snap1.id, "guess")
        check("wrong passphrase is rejected", False)
    except DecryptionError:
        check("wrong passphrase is rejected", True)

    # --- day 2: user edits code, deletes a photo -------------------------
    t1 = t0 + timedelta(days=1)
    source2 = dict(source)
    source2["home/projects/app/main.py"] = b"print('v2 - refactored')\n"
    del source2["home/photos/IMG_0002.jpg"]  # user deletes it from the source
    snap2 = repo.backup(WRITER_CRED, source2, t1)

    # (2) the deleted file is still restorable from the earlier snapshot
    r1 = repo.restore(RESTORE_CRED, snap1.id, PASS)
    check(
        "file deleted from source is still restorable from snap1",
        r1["home/photos/IMG_0002.jpg"] == b"\xff\xd8\xff\xe0 jpeg bytes two",
    )
    r2 = repo.restore(RESTORE_CRED, snap2.id, PASS)
    check("snap2 reflects the edit", r2["home/projects/app/main.py"] == b"print('v2 - refactored')\n")
    check("snap2 no longer contains the deleted photo", "home/photos/IMG_0002.jpg" not in r2)

    # --- day 3: ransomware encrypts everything, backup job still runs -----
    t2 = t0 + timedelta(days=2)
    ransomed = {p: b"!!ENCRYPTED-BY-RANSOMWARE!!" for p in source2}
    snap3 = repo.backup(WRITER_CRED, ransomed, t2)  # a "bad" snapshot lands

    # (3) the bad snapshot did not overwrite clean history
    check("clean snapshots survive the post-ransomware backup",
          {s.id for s in repo.snapshots} >= {snap1.id, snap2.id})
    pre_event = max((s for s in repo.snapshots if s.time < t2), key=lambda s: s.time)
    check("last-good snapshot is identifiable by timestamp", pre_event.id == snap2.id)
    rollback = repo.restore(RESTORE_CRED, pre_event.id, PASS)
    check("rollback to pre-event snapshot recovers plaintext",
          rollback["home/docs/taxes-2025.pdf"] == source["home/docs/taxes-2025.pdf"]
          and all(v != b"!!ENCRYPTED-BY-RANSOMWARE!!" for v in rollback.values()))

    # (4) the append-only writer credential cannot prune or delete
    expect_denied("WRITER credential is denied prune",
                  lambda: repo.forget_and_prune(WRITER_CRED, {"daily": 1}, t2))
    expect_denied("RESTORE credential is denied prune",
                  lambda: repo.forget_and_prune(RESTORE_CRED, {"daily": 1}, t2))
    expect_denied("RESTORE credential is denied write",
                  lambda: repo.backup(RESTORE_CRED, source, t2))
    check("all three clean/bad snapshots still present (nothing was deletable)",
          len(repo.snapshots) == 3)

    # --- retention: many daily snapshots, prune to policy ----------------
    repo2 = Repo(passphrase=PASS)
    base = datetime(2026, 1, 1, 3, 0, 0)
    made = []
    for day in range(40):  # 40 consecutive daily snapshots
        s = repo2.backup(WRITER_CRED, {"f": f"day {day}".encode()}, base + timedelta(days=day))
        made.append(s)
    for month in range(6):  # plus older monthly-spaced points
        repo2.backup(WRITER_CRED, {"f": f"old {month}".encode()},
                     base - timedelta(days=35 * (month + 1)))
    now = base + timedelta(days=39, hours=1)
    keep = {"daily": 30, "monthly": 12, "yearly": 3}
    removed = repo2.forget_and_prune(PRUNE_CRED, keep, now)

    kept_times = sorted((s.time for s in repo2.snapshots), reverse=True)
    # (5a) the 30 most recent days are kept
    newest_30 = {(base + timedelta(days=d)).date() for d in range(10, 40)}
    check("prune keeps the 30 most recent daily snapshots",
          newest_30.issubset({t.date() for t in kept_times}))
    # (5b) it does not keep more than the policy allows (30 daily + <=6 monthly here)
    check("prune does not retain beyond the tier policy",
          len(repo2.snapshots) <= 30 + 6,
          )
    check("prune actually removed the out-of-policy snapshots", len(removed) > 0)
    check("integrity check passes after prune (blob GC left refs intact)", repo2.check())

    # (5c) a prune re-run is idempotent
    removed2 = repo2.forget_and_prune(PRUNE_CRED, keep, now)
    check("prune re-run is a no-op", removed2 == [])

    # --- (6) staleness / silence detection ------------------------------
    interval = timedelta(days=1)
    mon_now = datetime(2026, 9, 9, 9, 0, 0)
    statuses = [
        DeviceStatus("laptop-a", mon_now - timedelta(hours=7)),          # fresh
        DeviceStatus("laptop-b", mon_now - timedelta(days=3)),           # warn
        DeviceStatus("laptop-c", mon_now - timedelta(days=19),
                     last_error=None),                                    # stale, NO error
    ]
    alerts = staleness_alerts(statuses, mon_now, interval)
    check("fresh device raises no alert", not any("laptop-a" in a for a in alerts))
    check("3-day-stale device raises a WARN", any(a.startswith("WARN") and "laptop-b" in a for a in alerts))
    check("19-day-silent device raises a PAGE despite no logged error",
          any(a.startswith("PAGE") and "laptop-c" in a for a in alerts))

    # --- admin can do everything (sanity) ------------------------------
    repo.forget_and_prune(ADMIN_CRED, {"daily": 2, "monthly": 1}, t2)
    check("admin credential may prune", True)

    print(f"\n{_PASS} passed, {_FAIL} failed")
    return 1 if _FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
