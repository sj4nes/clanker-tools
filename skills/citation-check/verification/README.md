# `citation-check` skill — verification run

The skill is methodology-only (no bespoke CLI). Verification = implement the
`SKILL.md` pipeline (`citecheck.py`) and run it against the **real** authoritative
APIs on a battery of citations with known ground truth, then confirm every
prescribed status, ladder, and API access pattern behaves as documented.

## Run

```
sh skills/citation-check/verification/run.sh
```

Needs network. Python 3 stdlib only. ~60–90 s wall (self-rate-limited).

`citecheck.py` is a deliberately minimal implementation — the similarity model is
crude on purpose. The point is the ladders, the API contracts, and the decision
thresholds, not a production matcher.

## Test battery and results

| # | Citation (ground truth) | Expected | Got |
|---|---|---|---|
| T1 | Dijkstra 1959, correct DOI `10.1007/BF01386390` | `verified` | `verified` (S=0.94) |
| T2 | same, year changed to 1968 | `verified_metadata_correction_needed` | ✅ + correction `year 1968→1959` |
| T3 | fabricated title/author, but Dijkstra's DOI attached | `contradicted` | ✅ "identifier resolves to a different title" |
| T4 | plausible-looking, fabricated venue, no identifier | `unresolved` | ✅ (only weak non-matching hits) |
| T5 | "See the classic paper on quicksort." | `not_applicable` / `unresolved` | `unresolved` |
| T6 | Abelson & Sussman, SICP, real ISBN `0262011530` | `verified` | `verified` (S=0.94, via Open Library) |
| T7 | well-formed but unregistered DOI `10.9999/…` | `unresolved` | ✅ (resolver 404, Crossref+DataCite miss, weak search) |
| T8 | invalid ISBN-13 check digit | `unresolved` + flag (not nonexistence) | ✅ (bad ISBN not used as a key) |
| T9 | Vaswani et al. 2017, `arXiv:1706.03762` | `verified` | `verified` (S=0.94) |
| T10 | CLRS, "Introduction to Algorithms, 3rd ed.", no ISBN | `likely_match` (work found, edition unconfirmed) | ✅ at work level |

All ten land on the intended status.

## API access patterns — confirmed

| Source | Endpoint | Result |
|---|---|---|
| DOI resolver | `HEAD https://doi.org/{doi}` | redirects to publisher host; unknown DOI → 404. Landing pages bounce through `?error=cookies_not_supported` cookie walls — the redirect **host** is the signal, not the page body. |
| Crossref | `GET /works/{doi}`, `GET /works/{doi}/agency` | work as documented; DOI is lower-cased in the response; `agency` routes Crossref vs DataCite |
| DataCite | `GET /dois/{doi}` | clean `404` for unknown; `data.attributes.{titles,creators,publicationYear,publisher}` for real |
| OpenAlex | `GET /works/doi:{doi}?mailto=…` | works keyless; good second pipeline |
| arXiv | `GET https://export.arxiv.org/api/query?id_list=…` | Atom; **must use HTTPS and retry** — first call intermittently returns an empty body |
| Open Library | `/api/books?bibkeys=ISBN:…&jscmd=data`, `/search.json` | works keyless for both ISBN lookup and title/author search |
| Google Books | `/books/v1/volumes?q=isbn:…` | works keyless |
| WorldCat | Search API | **requires OCLC credentials — no keyless path.** Book pipeline fell back to Open Library + Google Books + (LoC), exactly as the ladder prescribes. |

## Findings folded back into the skill

1. **A checksum-failed identifier is a flag, not a lookup key** (correctness
   fix). T8 originally came back `contradicted`: the invalid ISBN-13 was passed
   to Open Library anyway, returned an unrelated Arabic-language history, and the
   title mismatch was misread as "identifier resolves to a different work". Now
   the skill (SKILL step 1 & 2, `source-ladders.md` pseudocode,
   `failure-modes.md`) states: on a failed check digit, record the flag and route
   to the bibliographic ladder as if no identifier were supplied.
2. **`ambiguous` vs `unresolved` boundary** (decision-procedure fix). T4 and T7
   originally fell through to `ambiguous` on weak search noise ("Nothing",
   "Nothing in Particular"). `ambiguous` now requires **≥ 2 candidates that each
   clear a plausibility floor and are genuinely different works**; weak,
   non-matching records → `unresolved` (never a claim of nonexistence). Updated
   in `SKILL.md` step 4 and `matching-and-scoring.md`.
3. **Same-work-different-manifestation → `likely_match` at work level**, not
   `ambiguous`. T10 returns several real "Introduction to Algorithms" records
   (editions/translations); that is "work found, edition unconfirmed", a
   `likely_match`, not a genuine ambiguity between different works. Added to both
   files.
4. **Type inference must not hinge on an ISBN being present.** T10 (CLRS, no
   ISBN) was routed down the *article* ladder and got journal-database noise.
   The skill now prescribes inferring *book* from an edition statement + a
   publisher/"Press" token + the absence of a journal volume(issue).
5. **Strip edition/volume out of the title before a catalog search.**
   "Introduction to Algorithms, 3rd ed." as a literal title string makes Open
   Library's title search miss; edition belongs in its own field. Added to
   SKILL step 1.
6. **arXiv API**: use HTTPS, retry with backoff — documented in
   `source-ladders.md`.
7. **DOI landing pages / cookie walls**: get authoritative fields from
   Crossref/DataCite, not by scraping the landing page — reinforced with the
   concrete `?error=cookies_not_supported` example.
8. **WorldCat needs OCLC credentials** — confirmed no keyless access; the
   prescribed fallback (LoC + Open Library + Google Books) is what the run
   actually used. Caveat sharpened in `source-ladders.md`.

## Known limitation of the harness (not a skill defect)

`citecheck.py`'s parser is crude (regex title extraction, word-count heuristic
for "insufficient information"), so T5 lands on `unresolved` rather than the
ideal `not_applicable`. The skill's step-1 guidance (return `not_applicable`
before running the ladder when there is no title **and** no identifier **and** no
author+year) is correct; a real agent applies judgement the regex cannot.
