# Field matching, scoring, and the decision procedure

Identifier checks are a high-precision path. Everything else needs a
**field-aware similarity model** — not an all-or-nothing string compare.

## Field weighting

| Field | Treatment |
|---|---|
| DOI / PMID / arXiv / OCLC / report number | Exact match expected after normalization |
| ISBN | Exact for the cited manifestation; a different edition is a separate "related edition" status, not a match |
| Title | Strong fuzzy compare, subtitle-aware |
| First / corporate author | Strong; account for initials and name variants |
| Remaining authors | Moderate; allow abbreviated author lists |
| Year | Usually exact; allow a documented ±1 only when online-first vs issue-date conventions genuinely conflict |
| Journal / publisher | Moderate–strong on normalized names and known variants/imprints |
| Volume / issue / pages | Strong for articles; distinguish an article number from a page range |
| Edition / format / language | Critical for books, standards, translations |

## Scoring function

```
S = 0.40*I + 0.25*T + 0.15*A + 0.08*Y + 0.07*C + 0.05*D
```

- `I` identifier agreement
- `T` title agreement
- `A` author agreement
- `Y` year agreement
- `C` container / publisher agreement
- `D` edition / pagination / volume-issue / other type-specific detail

Each component in `[0, 1]`. `S` ranks candidate records; it does **not** by
itself decide status.

## Hard contradictions (override any score)

A weighted score never beats one of these:

- The citation gives DOI A, but DOI A belongs to a different title or author.
- The ISBN resolves to a paperback first edition while the citation claims a
  hardcover revised edition (report as related edition / correction, not match).
- The citation says "journal article", but the verified object is a book review,
  editorial, correction, retraction notice, or conference abstract.
- The cited year / volume / pages map to a *different* work in the same journal.
- A provably impossible field combination (e.g. a publication year before the
  journal existed).

When a hard contradiction is present → status `contradicted`, high confidence.

## Independent-evidence rule

- **Easy cases:** one authoritative identifier record + a matching landing page
  is enough for `verified`.
- **Uncertain / older / obscure / identifier-free:** require **two independent
  records from different data pipelines** (e.g. Crossref *and* the publisher
  page; WorldCat *and* Library of Congress). Copies that all derive from the
  same erroneous source are one piece of evidence — see citation laundering in
  `failure-modes.md`.

## Decision procedure

```python
def assess_citation(citation, records):
    normalized = normalize(citation)
    hard = find_hard_conflicts(normalized, records)
    if hard:
        return {"status": "contradicted", "confidence": 0.98, "conflicts": hard}

    candidates = score_records(normalized, records)
    best = choose_best_nonambiguous(candidates)   # None if top two are close
    if best is None:
        return {"status": "unresolved", "confidence": 0.0,
                "reason": "No sufficiently supported candidate record."}

    corr = independent_source_count(best)
    diffs = field_differences(normalized, best)

    if best.identifier_exact and corr >= 1 and not diffs:
        return {"status": "verified", "confidence": 0.99}

    if best.score >= 0.92 and corr >= 2:
        if diffs:
            return {"status": "verified_metadata_correction_needed",
                    "confidence": 0.95, "corrections": diffs}
        return {"status": "verified", "confidence": 0.95}

    if best.score >= 0.80 and no_close_runner_up(candidates):
        return {"status": "likely_match", "confidence": 0.75,
                "warnings": ["No unique authoritative identifier match."]}

    plausible = [c for c in candidates
                 if c.score >= 0.55 or title_sim(normalized, c) >= 0.7]

    # several records that are the SAME work at different manifestation levels
    # (editions / translations / reprints) -> the work is found, the edition is
    # not. That is likely_match at work level, NOT ambiguous.
    if len(plausible) >= 2 and all_same_work(plausible) and title_sim(normalized, plausible[0]) >= 0.7:
        return {"status": "likely_match", "confidence": 0.7, "frbr_level": "work",
                "warnings": ["Work found; cited edition/manifestation unconfirmed without an identifier."]}

    # ambiguous is for >= 2 plausible candidates that are genuinely DIFFERENT works.
    if len(plausible) >= 2:
        return {"status": "ambiguous", "confidence": 0.40,
                "candidates": top_candidates(plausible)}

    # only weak, non-matching records came back -> unresolved, NOT ambiguous,
    # and NOT a claim of nonexistence (catalog coverage is incomplete).
    return {"status": "unresolved", "confidence": 0.0,
            "reason": "Source ladder returned only weak, non-matching records."}
```

`ambiguous` is never the fall-through for "the search returned noise". If no
candidate comes near the citation, the status is `unresolved`.

`not_applicable` is returned before this runs, when parsing yields too little to
form a candidate (no title, no identifier, no usable author+year).

## FRBR level — report what you actually verified

| Level | What it is |
|---|---|
| Work | The abstract intellectual creation |
| Expression | A translation, revision, or adaptation |
| Manifestation | A specific published edition / format |
| Item | A particular physical or digital copy |

"The work exists" is weaker than "the cited 2017 3rd-edition paperback,
ISBN 978-…, exists". Always state the level.

## Confidence wording

| Status | Agent wording |
|---|---|
| `verified` | "Verified against Crossref and the publisher record." |
| `verified_metadata_correction_needed` | "The work exists, but the citation appears to misstate the publication year (2020 → 2021)." |
| `likely_match` | "A likely match was found; the edition/identifier could not be confirmed." |
| `ambiguous` | "Multiple records match; manual disambiguation is needed." |
| `unresolved` | "No reliable bibliographic record was located using the applicable sources." |
| `contradicted` | "The supplied DOI resolves to a different work." |

Avoid "fake" / "fabricated" / "nonexistent" unless: a claimed DOI resolves to a
different item **and** all other distinctive fields fail, or the citation
contains a provably impossible field combination. Otherwise "unverified" or
"not substantiated" is the accurate phrase.
