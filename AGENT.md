# SOLVE-IT LLM Wiki — Schema

Read this file before modifying the wiki.

This repository maintains a persistent, LLM-written wiki for digital forensics knowledge.
The current seed source is the academic paper corpus under `raw/` (`raw/DI/`, `raw/IEEE Access/`,
`raw/JDFSL/`). The wiki's fixed objective list (`wiki/objectives.md`, 23 `DFO-` entries) and its
`DFO-`/`DFT-`/`DFW-`/`DFM-`/`DFCite-` ID scheme originate from an earlier one-time bootstrap
against a SOLVE-IT knowledge-base export (`data.json`); that file, and its companion
`scripts/bootstrap-wiki.mjs` and `title-overrides.json`, are not present in this repository and
are not used for ingestion. See "Ingesting from a raw paper corpus" below for the live workflow.

## Core Model

- Treat anything under `raw/` as immutable source material.
- Treat `wiki/` as the LLM-maintained reading layer.
- The only entity page categories are:
  - `wiki/techniques/`
  - `wiki/weaknesses/`
  - `wiki/mitigations/`
- `wiki/objectives.md` is a fixed hub page, not an entity folder.
- Do not create separate relation files. Relationships live inside page frontmatter and body links.

## Directory Structure

```text
solve-with-llm/
├── AGENT.md
├── raw/
│   ├── DI/                      # Forensic Science International: Digital Investigation papers
│   ├── IEEE Access/
│   └── JDFSL/
├── templates/
│   ├── technique-page.md
│   ├── weakness-page.md
│   └── mitigation-page.md
└── wiki/
    ├── index.md
    ├── log.md
    ├── objectives.md
    ├── references.md
    ├── techniques/
    ├── weaknesses/
    └── mitigations/
```

If an old `wiki/objectives/` directory exists from earlier experiments, ignore it.
The canonical objective view is `wiki/objectives.md`.

## Ownership Rules

Keep relationship metadata simple and directional.

- Technique pages own:
  - `objective_ids`
  - `weakness_ids`
- Weakness pages own:
  - `mitigation_ids`
- Mitigation pages do not need reverse-ID metadata by default.
- Reverse relationships should usually appear as normal wiki links in the page body.

This keeps the wiki readable without introducing a separate graph layer.

## Titles

- `name` is the canonical label for an entity. Use it for:
  - filenames
  - page H1 headings
  - wiki links (`[[techniques/Triage]]`)
  - provenance checks against the source material (the ingested paper, cited via `source_refs`)
- If an auto-generated filename from `name` is awkward, rename the file directly and keep `name`
  as the display title (there is no `title-overrides.json` mechanism in active use).

### Technique Naming Rules

- Per `STYLE_GUIDE.md`, technique names begin with a present-tense imperative verb (e.g. "Locate", "Connect", "Use") and use sentence case. Every technique name must pass the investigator test: "As an investigator, I want to [technique name]..." must read naturally.
- Prefer the narrowest directly executable or directly describable technique over an umbrella capability, expressed as a verb phrase — e.g. `Perform a dictionary attack`, `Verify a disk image's hash` rather than the umbrella `Crack passwords`.
- Avoid broad umbrella names such as `Crack passwords` when the source material supports one or more narrower technique pages instead.
- If a source discusses several sibling techniques, split them into separate technique pages when practical rather than collapsing them into one broad page.
- Use an umbrella technique name only when the source does not distinguish the component methods clearly, or when the user explicitly asks for the broader page.

### Weakness Naming Rules

- Name weaknesses as explicit failure, defect, or missing-outcome statements, not as short analyst shorthand.
- Prefer source-faithful wording that states what went wrong and where it went wrong, even when the resulting title is long.
- Good weakness names usually stand alone without needing the summary to explain the defect.
- Preferred naming patterns include:
  - `Failure to <verb> ...`
  - `<Artifact/process> is incorrectly <verb phrase>`
  - `Missing <expected data/artifact> ...`
  - `<Parsing/validation/acquisition step> fails to <expected behavior> ...`
- Examples of the preferred weakness style:
  - `Missing deleted but recoverable partitions from unpartitioned space`
  - `Image format parsing presents incorrect forensic image metadata`
  - `Failure to validate hash properly during disk image verification`
  - `File type is incorrectly identified`
- Avoid abstract labels such as `Hash-blind brute-force planning` unless the source itself uses that phrase. Put interpretation in the `description` and body, and keep the `name` focused on the concrete defect.

## Operations

### Ingest

When the user asks to ingest a new source:

1. Read the source material.
2. Create or update affected pages in `wiki/techniques/`, `wiki/weaknesses/`, and `wiki/mitigations/`
   (see "Ingesting from a raw paper corpus" below for the reuse-first process this wiki actually uses).
3. Update `wiki/objectives.md` when objective-to-technique mappings change.

### Ingesting from a raw paper corpus (`raw/` academic papers)

The narrowest-technique-name rule under Technique Naming Rules assumes a curated, pre-taxonomized
source where splitting into narrow sibling pages is bounded by the source's own structure. It does
not apply the same way when the source is an open-ended corpus of individual papers
(e.g. `raw/DI`, `raw/IEEE Access`, `raw/JDFSL`): naming each paper's specific method narrowly
causes one new page per paper, so page count grows linearly with corpus size instead of
converging toward a reusable knowledge base. When ingesting from a raw paper corpus, apply this
reuse-first process instead:

1. Before minting any new technique/weakness/mitigation page, search `wiki/techniques/`,
   `wiki/weaknesses/`, and `wiki/mitigations/` for an existing page that already covers the same
   underlying method, defect, or fix at a category level (not the same paper — the same concept).
2. If a matching page exists, reuse it: append the new paper's ID to its `source_refs`, and only
   if the new paper adds meaningfully new detail, extend `Details`/`Examples` (and note the
   specific variant in `aliases` if it has a distinct name in that paper). Do not create a second
   page for the same concept.
3. If no matching page exists, create one, but name and describe it at the level of a reusable
   method/defect *category* rather than that paper's specific implementation — e.g. prefer
   `Detect deepfakes using frequency-domain artifacts` over `Detect deepfakes via high-frequency
   DCT reconstruction`, and prefer `Identify file types using n-gram analysis` over `Identify file
   types using an n-gram SVM`. As elsewhere, the name itself is still a present-tense imperative
   verb phrase per `STYLE_GUIDE.md` — only the *specificity level* (category vs. paper-specific
   implementation) changes for corpus ingestion. Put the paper's specific implementation detail in
   `Details`/`Examples`, and record the narrower original phrasing in `aliases` so it stays
   searchable.
4. A single paper does not need to produce a fixed number of pages. A narrow, single-purpose
   paper may reuse existing pages entirely (source_refs-only update, no new page); a broad survey
   paper may justify several new pages. Do not target a fixed "N pages per paper" ratio.
5. When two or more existing pages turn out to describe the same category (discovered while
   ingesting a later paper, or during a periodic review), merge them: keep the lower/older ID,
   fold the other's content and `source_refs` in as `Details`/`Examples`/`aliases`, update every
   page that links to the retired page's old title, and delete the retired file. Never reuse the
   retired page's ID for a new entity (see ID Numbering Conventions). Record the merge in
   `wiki/log.md`.
5. Update `wiki/index.md`.
6. Append an entry to `wiki/log.md`.

### Query

When answering a question:

1. Read `wiki/index.md` first.
2. Read `wiki/objectives.md` if the question is goal-oriented.
3. Read the smallest relevant set of entity pages.
4. Answer with citations to page IDs and source refs when possible.
5. If the answer creates durable knowledge, propose filing it back into the wiki.

### Lint

When asked to health-check the wiki, look for:

- orphan technique, weakness, or mitigation pages
- missing or broken wiki links
- mismatches between frontmatter IDs and body links
- stale summaries that no longer match the source data
- techniques missing objectives or weaknesses
- weaknesses missing mitigations when the source data contains them

## ID Numbering Conventions

Each entity type has a fixed prefix and starts numbering from 1001, incrementing by 1.

| Entity type | Prefix    | Example       |
|-------------|-----------|---------------|
| Objective   | `DFO-`    | `DFO-1001`    |
| Technique   | `DFT-`    | `DFT-1001`    |
| Weakness    | `DFW-`    | `DFW-1001`    |
| Mitigation  | `DFM-`    | `DFM-1001`    |
| Reference   | `DFCite-` | `DFCite-1001` |

Rules:
- Never reuse a retired ID.
- Assign the next available integer in sequence; do not skip numbers.
- Check existing pages to find the current highest ID before assigning a new one.
- Store the ID in the `id` frontmatter field of every entity page.
- References use `DFCite-` IDs and are indexed in `wiki/references.md` in BibTeX-style format (see References section below).

## Page Naming

- Technique page path: `wiki/techniques/<Short Title>.md`
- Weakness page path: `wiki/weaknesses/<Short Title>.md`
- Mitigation page path: `wiki/mitigations/<Short Title>.md`

Prefer concise, graph-friendly filenames built from `title`.
Avoid IDs in filenames unless they are needed as a collision fallback.
Always keep the ID in frontmatter.

## Link Style

Prefer folder-qualified links using the filename derived from `name`:

- `[[techniques/Triage]]`
- `[[weaknesses/Triage media changes]]`
- `[[mitigations/Use hardware write blocker]]`

Use plain objective IDs inside body text when helpful, but keep the canonical objective listing in
`wiki/objectives.md`.

## Frontmatter Rules

Use YAML frontmatter on every entity page.

Common fields:

- `id`
- `type`
- `name`
- `description`
- `source_refs`
- `updated_at`
- `status`

Allowed `status` values:

- `stub`
- `partial`
- `complete`

## Technique Template

See `templates/technique-page.md`.

Required fields:

- `id`
- `type: technique`
- `name`
- `description`
- `objective_ids`
- `weakness_ids`

Optional fields:

- `aliases`
- `source_refs`
- `updated_at`
- `status`

Recommended sections:

- `Summary`
- `Details`
- `Examples`
- `Related Objectives`
- `Related Weaknesses`
- `References`

Optional sections when source data exists:

- `CASE Input Classes`
- `CASE Output Classes`
- `Notes`

## Weakness Template

See `templates/weakness-page.md`.

Required fields:

- `id`
- `type: weakness`
- `name`
- `description`
- `categories`
- `mitigation_ids`

Allowed `categories` values (ASTM E2916 quality defect taxonomy):

| Value | Meaning |
|-------|---------|
| `ASTM_INCOMP` | Incompleteness — evidence missing or not fully collected |
| `ASTM_INAC_ALT` | Inaccuracy: Alteration — original data changed during the process |
| `ASTM_INAC_COR` | Inaccuracy: Corruption — data transferred or stored incorrectly |
| `ASTM_INAC_EX` | Inaccuracy: Extra Data — data added that was not in the original |
| `ASTM_INAC_AS` | Inaccuracy: Incorrect Association — activity misattributed to wrong entity |
| `ASTM_MISINT` | Misinterpretation — correct data, but meaning interpreted incorrectly |

A weakness may have more than one category.

Recommended sections:

- `Summary`
- `Why It Matters`
- `Related Mitigations`
- `Used By`
- `References`

## Mitigation Template

See `templates/mitigation-page.md`.

Required fields:

- `id`
- `type: mitigation`
- `name`

Recommended sections:

- `Summary`
- `Addresses`
- `How To Apply`
- `References`

## objectives.md Format

`wiki/objectives.md` is the stable navigation page for all objectives.

For each objective include:

- objective ID and name
- description
- sort order

Do not split objectives into separate pages unless the user explicitly asks for that refactor.

## index.md Format

`wiki/index.md` is the first page to read during query operations.

Keep it compact and content-oriented:

- last updated date
- source snapshot counts
- fixed-page links
- category status summary
- objective table
- optional notes on wiki coverage

## log.md Format

`wiki/log.md` is append-only.
Never rewrite old entries unless the user explicitly asks.

Entry format:

```markdown
## [YYYY-MM-DD] <operation> | <brief description>
- Pages affected: <comma-separated list>
- Summary: <one or two sentences>
```

Recommended operation tokens:

- `bootstrap`
- `ingest`
- `update`
- `query`
- `lint`
- `fix`

## References Format

All references are indexed in `wiki/references.md`.
Each entry uses a `DFCite-` ID and BibTeX-style fields.

Entry format:

```markdown
### DFCite-1001

- type: article | book | inproceedings | techreport | misc
- author: Last, First and Last, First
- title: Full title of the work
- year: YYYY
- journal / booktitle / institution: (use whichever applies)
- url: https://... (optional)
- note: (optional free-text)
```

Rules:
- One `###` heading per entry, using the `DFCite-` ID.
- Cite a reference in entity pages as `[[references#DFCite-1001]]` or inline as `DFCite-1001`.
- Keep `wiki/references.md` sorted by ID ascending.
- Never delete an entry; mark retired entries with `status: retracted` instead.

## Editing Discipline

- Preserve the user's simplified architecture.
- Do not invent extra storage layers unless the user asks.
- Prefer updating existing pages over creating new top-level wiki structures.
- Keep pages readable to humans first, machine-friendly second.
- When there is a tradeoff, favor explicit links and concise frontmatter over hidden indirection.
