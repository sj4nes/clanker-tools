# Protection charter: <household / person / site>

> What must be protected, how well, and where the copies live.
> Fill every field. Mark unknowns `ASSUMPTION:` and confirm before building.

## Scope and ownership

- **Who / what this covers**:
- **Owner (accountable for recovery)**:
- **Recovery contact (could recover if owner unavailable)**:
- **Explicitly out of scope**:
- **Budget ceiling** (hardware + any off-site hosting):

## Devices

| Device | OS | Internal storage | Role | On often enough to back up? |
|---|---|---|---|---|
|  |  |  |  |  |

## Sources and data classes

| Source (path / system) | Device | Size | Daily churn | Data class | RPO (work you can lose) | RTO (must be back within) |
|---|---|---|---|---|---|---|
|  |  |  |  | photos / financial / documents / projects / system / regenerable |  |  |

Data-class defaults (adjust): see
[`../references/retention-and-sizing.md`](../references/retention-and-sizing.md).

## Difficult sources

| Source | Type (DB / VM / mail / vault / encrypted vol / cloud-only) | Capture method | Hook that performs it | Run fails if capture fails? | Last restore-tested |
|---|---|---|---|---|---|
|  |  |  |  | yes/no |  |

## Exclusions

| Pattern | Why it's safe to exclude (regenerable how?) |
|---|---|
|  |  |

## Available targets

| Target | Type | Capacity | Location | Connectivity | Administered by |
|---|---|---|---|---|---|
|  | USB HDD / NAS / spare PC / relative's NAS / object storage |  | this building / other building |  |  |

## Required copies per data class

| Data class | Fast local | Independent repo | Offline | Off-site | Meets 3-2-1(+1)? |
|---|---|---|---|---|---|
| photos / authored | ✔ | ✔ | ✔ | ✔ |  |
| financial / legal | ✔ | ✔ | ✔ | ✔ |  |
| documents | ✔ | ✔ | one of | one of |  |
| projects / code | ✔ | ✔ | — | ✔ |  |
| system | image | — | — | — |  |

## Assumptions to confirm

- ASSUMPTION:
- ASSUMPTION:

## Sign-off

- [ ] Owner agrees these are the sources and the RPO/RTO per class.
- [ ] Every difficult source has a capture method.
- [ ] The required-copies table satisfies 3-2-1(+1) for every class.
- [ ] Recovery contact named and has agreed.
