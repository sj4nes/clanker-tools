# Pre-launch checklist and recurring drift review

## Pre-launch checklist

Before you rely on the system, confirm all of:

**Sources**

- [ ] Every folder/library/system whose loss would hurt is in the charter with
      size, churn, RPO, and RTO.
- [ ] Every difficult source (DB, VM, mail, vault, encrypted volume, cloud-only)
      has a named capture method and a hook that fails the run if capture fails.
- [ ] Exclusions are listed and reviewed; nothing irreplaceable is behind a
      broad glob.

**Copies (3-2-1 +1)**

- [ ] ≥ 3 copies of each data class, on ≥ 2 media types, with ≥ 1 off-site.
- [ ] ≥ 1 copy the everyday machine cannot alter or delete (offline OR
      append-only OR object-lock).
- [ ] The topology map shows every source → every copy, with medium, location,
      and which credential writes it.
- [ ] No file sharing (SMB/NFS/AFP) exposed to the public internet.

**Policy**

- [ ] Retention tiers per data class, derived from cost-of-loss, sized with
      `bc`, with ≥ 2× headroom provisioned.
- [ ] Client-side encryption on every portable and remote target.
- [ ] Four credential roles separated: writer (append-only), prune, restore,
      admin. Writer verified unable to prune/delete.
- [ ] Sealed recovery record exists for every repository (passphrase, location,
      access, tool+version, restore commands, disk keys) — stored physically
      separate from every everyday device.
- [ ] A named recovery contact who can actually retrieve the record and follow
      (or delegate) the runbook.

**Jobs & monitoring**

- [ ] Every recurring piece is an `unattended-automation` job: idempotent,
      locked, bounded, postcondition-verified, alert on failure AND silence.
- [ ] Any LLM-driven setup/recovery agent is an `agent-automation` build with
      init/format/re-key/retention-change/prune-beyond-policy/add-offsite/
      export-key/restore-over-existing all behind human approval.
- [ ] Last-success tracked per device and per copy, with staleness thresholds.
- [ ] Repository verification scheduled (metadata weekly, full-read monthly/
      quarterly); FS-snapshot layer scrubs monthly.
- [ ] Capacity alerts at 75 % and 90 %; SMART/pool health monitored.

**Proof**

- [ ] Monthly sampled-restore job runs and byte-verifies.
- [ ] A full drill has been performed from the written runbook.
- [ ] A ransomware/rollback drill has confirmed good snapshots survive a bad
      one and the writer credential cannot prune.
- [ ] The recovery runbook has been executed by someone other than its author.

## Recurring drift review (quarterly)

The environment changes under the backup. Each quarter:

- [ ] **Re-inventory**: new data locations? A project that moved to a cloud app?
      A new machine? A source that grew 10×? Update the charter.
- [ ] **Cloud-stub check**: any source where a growing fraction of bytes is
      "online only" and therefore not actually backed up?
- [ ] **Credential re-confirm**: does each credential still have *only* its
      role's scope? Any temporary elevation that never got reverted?
- [ ] **Retention re-size**: actual repo-size ÷ source-size vs the estimate;
      correct the model; re-provision if trending toward the cap.
- [ ] **Freshness audit**: any device or copy that has been quietly stale?
      Any offline disk overdue for rotation?
- [ ] **Hardware age**: any target disk past ~5 years or showing SMART warnings?
      Plan replacement before it fails.
- [ ] **Sealed record currency**: does it match the current tools, versions,
      locations, and keys? Did a key rotation get propagated to every copy?
- [ ] **Drill log**: sampled restores passing every month? Full drill done this
      half-year? Runbook gaps from the last drill actually fixed?
- [ ] **Recovery contact**: still reachable, still willing, still able?
