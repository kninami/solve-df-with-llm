# SOLVE-IT Wiki Index

Last updated: 2026-08-17

## Source Snapshot

- Seed source: `raw/` paper corpus (`DI`: 442 papers, `IEEE Access`: 52 papers, `JDFSL`: 24 papers — 518 total)
- **Ingestion complete: 518 / 518 papers ingested (100%).** `raw/DI` 442/442, `raw/IEEE Access` 52/52, `raw/JDFSL` 24/24 — all three source corpora are fully ingested. Raw ingestion is finished; ongoing work is maintenance (reuse-first merges, lint fixes, and any future re-ingestion if the corpus grows).
- References indexed: 513 `DFCite-` entries. This is 5 fewer than 518 raw files because the corpus contains 4 documented pairs of byte-identical duplicate PDFs under different filenames (each pair cited once — see `wiki/log.md` batches covering files 111-120, 151-160, 171-180, and 351-360 for the `pdftotext`-diff verification of each), plus one reference (`DFCite-1065`) that was permanently deleted per explicit user request on 2026-08-12 while its supporting technique/weakness/mitigation pages (`DFT-1070`/`DFW-1075`/`DFM-1075`) were intentionally kept (see the `[2026-08-11] fix | Delete DFCite-1065 per explicit user request` log entry). 442 (DI) − 4 (dup pairs) + 52 (IEEE Access) + 24 (JDFSL) − 1 (deleted) = 513, reconciling exactly.
- Objectives: 23 (fixed hub, from the earlier SOLVE-IT bootstrap; retained as navigation scaffold — all paper-derived techniques map cleanly onto it, and only `DFO-1022` has zero mapped techniques).
- Techniques: 411
- Weaknesses: 441
- Mitigations: 444
- **ID ranges:** single continuous "highest existing ID + 1" sequence across the whole wiki (no reserved blocks; the earlier `raw/DI` 1001+ / `raw/IEEE Access`+`raw/JDFSL` 2001+ split was merged back into one sequence on 2026-08-15/16 — see `wiki/log.md` for the merge commits). Next available IDs as of this entry: `DFT-2128`, `DFW-2138`, `DFM-2139`, `DFCite-2159`.

## Fixed Pages

- [[index]] This catalog page
- [[objectives]] Objective-to-technique map
- [[log]] Chronological wiki maintenance log
- [[references]] BibTeX-style index of ingested source papers (`DFCite-`)

## Entity Categories

- `wiki/techniques/` Technique pages managed by the LLM
- `wiki/weaknesses/` Weakness pages managed by the LLM
- `wiki/mitigations/` Mitigation pages managed by the LLM

## Coverage Status

- Technique pages generated: 411 (every page has `objective_ids` + `weakness_ids`; verified via full-wiki scripted audit, zero missing)
- Weakness pages generated: 441 (every page has `categories` + `mitigation_ids`; verified via full-wiki scripted audit, zero missing)
- Mitigation pages generated: 444
- Objective hub generated: yes (fixed navigation page; technique counts below are recomputed directly from every technique page's `objective_ids` frontmatter)
- Integrity: zero duplicate `DFT-`/`DFW-`/`DFM-`/`DFCite-` IDs anywhere in the wiki; zero broken `[[...]]` wikilinks anywhere in `wiki/` (excluding `wiki/log.md`'s intentionally-preserved historical references to retired/renamed page titles); zero dangling `objective_ids`/`weakness_ids`/`mitigation_ids` cross-references

## Objectives (technique counts recomputed from every technique page's `objective_ids`, descending)

| ID | Name | # Techniques |
| --- | --- | ---: |
| [[objectives#DFO-1019 Detect anti-forensics and other anomalies|DFO-1019]] | Detect anti-forensics and other anomalies | 84 |
| [[objectives#DFO-1001 Reconstruct events|DFO-1001]] | Reconstruct events | 50 |
| [[objectives#DFO-1008 Establish identities|DFO-1008]] | Establish identities | 48 |
| [[objectives#DFO-1004 Conduct research|DFO-1004]] | Conduct research | 37 |
| [[objectives#DFO-1006 Acquire data|DFO-1006]] | Acquire data | 30 |
| [[objectives#DFO-1011 Extract artifacts stored by applications|DFO-1011]] | Extract artifacts stored by applications | 27 |
| [[objectives#DFO-1012 Locate potentially relevant content|DFO-1012]] | Locate potentially relevant content | 27 |
| [[objectives#DFO-1016 Overcome protection mechanisms|DFO-1016]] | Overcome protection mechanisms | 24 |
| [[objectives#DFO-1018 Read data from digital evidence storage formats|DFO-1018]] | Read data from digital evidence storage formats | 21 |
| [[objectives#DFO-1002 Extract data from specific formats|DFO-1002]] | Extract data from specific formats | 18 |
| [[objectives#DFO-1015 Prepare for a digital investigation|DFO-1015]] | Prepare for a digital investigation | 17 |
| [[objectives#DFO-1003 Review content for relevance|DFO-1003]] | Review content for relevance | 14 |
| [[objectives#DFO-1005 Prioritize digital evidence sources|DFO-1005]] | Prioritize digital evidence sources | 12 |
| [[objectives#DFO-1010 Preserve digital evidence|DFO-1010]] | Preserve digital evidence | 11 |
| [[objectives#DFO-1017 Extract artifacts stored by the operating system|DFO-1017]] | Extract artifacts stored by the operating system | 11 |
| [[objectives#DFO-1021 Access device data for acquisition|DFO-1021]] | Access device data for acquisition | 10 |
| [[objectives#DFO-1013 Access partitions, volumes, and file systems data|DFO-1013]] | Access partitions, volumes, and file systems data | 8 |
| [[objectives#DFO-1020 Document digital forensic activities|DFO-1020]] | Document digital forensic activities | 8 |
| [[objectives#DFO-1007 Reduce data under consideration|DFO-1007]] | Reduce data under consideration | 5 |
| [[objectives#DFO-1014 Find potential digital evidence sources|DFO-1014]] | Find potential digital evidence sources | 4 |
| [[objectives#DFO-1009 Create visualizations|DFO-1009]] | Create visualizations | 3 |
| [[objectives#DFO-1023 Extract specific artifact types|DFO-1023]] | Extract specific artifact types | 1 |
| [[objectives#DFO-1022 Store acquired data|DFO-1022]] | Store acquired data | 0 |

The only objective with zero techniques derived from ingested papers is `DFO-1022` (Store acquired data) — the corpus's acquisition-related papers consistently frame their contributions as *how to acquire/read/extract* data rather than *how to store* it once acquired, so no paper mapped cleanly to this objective across the full 518-paper corpus.

## Notes

- The wiki was originally bootstrapped from a `data.json` SOLVE-IT export; that source file and its companion scripts are not present in this repository, and `objectives.md` (23 fixed `DFO-` entries) is the only surviving artifact of that bootstrap, retained as a stable navigation hub.
- All subsequent content — every technique, weakness, mitigation, and reference in the wiki — was produced by ingesting the academic paper corpus under `raw/` (`DI/`, `IEEE Access/`, `JDFSL/`) using the reuse-first process in `AGENT.md`'s "Ingesting from a raw paper corpus" section: before minting a new page, existing pages are searched for a conceptual (not just per-paper) match and reused via extended `source_refs`/Details/Examples/aliases rather than duplicated.
- **Full ingestion of all 518 papers across all three source corpora completed on 2026-08-17.** Detailed, chronological per-batch provenance (which paper produced which page, every reuse-vs-new-page judgment call and its reasoning, every merge/rename, every reference-only judgment, and every provenance/prompt-injection scan result) is preserved in full in `wiki/log.md` and is not repeated here — consult the log for the complete history. A small number of entity pages required manual merges when later papers were found to describe the same underlying category as an earlier one (e.g. dashcam geospatial-mapping, deepfake detection, synthetic dataset generation, memory-forensics classification); each such merge is recorded in `wiki/log.md` at the point it occurred, with the retired page's old title preserved as an `aliases` entry on the surviving page.
- Ongoing/future work on this wiki is now maintenance rather than raw ingestion: periodic lint passes (orphan pages, broken links, stale summaries), reuse-first merges if a future re-read of the corpus surfaces an overlooked conceptual match, and re-ingestion only if the `raw/` corpus itself grows with new papers.
