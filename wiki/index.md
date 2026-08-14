# SOLVE-IT Wiki Index

Last updated: 2026-08-14

## Source Snapshot

- Seed source: `raw/` paper corpus (DI: 442 papers, IEEE Access: 52 papers, JDFSL: 24 papers — 518 total)
- Ingestion progress (this worktree): 100/518 `raw/DI` papers (files 1-100, alphabetical) + 30/52 `raw/IEEE Access` papers (files 1-30, alphabetical) = 130 papers ingested from this worktree's starting point
- References indexed: 130
- Objectives: 23 (fixed hub, from earlier SOLVE-IT bootstrap; retained as navigation scaffold)
- Techniques: 115
- Weaknesses: 130
- Mitigations: 130
- **Note on worktree state:** this worktree branched before the main checkout's STYLE_GUIDE.md-alignment and further DI-ingestion commits landed, so its starting entity set (90/103/103, `raw/DI` files 1-100 only) is behind the main checkout's later state. New entity IDs from `raw/IEEE Access` ingestion in this worktree use a reserved 2001+ ID block (DFT-2001+, DFW-2001+, DFM-2001+, DFCite-2001+) specifically to avoid collision with the main worktree's concurrently-assigned sequential IDs when the branches are merged. See wiki/log.md entries dated 2026-08-14 for details.

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

- Technique pages generated: 115
- Weakness pages generated: 130
- Mitigation pages generated: 130
- Objective hub generated: yes (fixed navigation page, not yet re-derived from paper corpus)

## Objectives (technique counts reflect current paper-derived techniques only)

| ID | Name | # Techniques |
| --- | --- | ---: |
| [[objectives#DFO-1019 Detect anti-forensics and other anomalies|DFO-1019]] | Detect anti-forensics and other anomalies | 19 |
| [[objectives#DFO-1001 Reconstruct events|DFO-1001]] | Reconstruct events | 14 |
| [[objectives#DFO-1018 Read data from digital evidence storage formats|DFO-1018]] | Read data from digital evidence storage formats | 10 |
| [[objectives#DFO-1008 Establish identities|DFO-1008]] | Establish identities | 10 |
| [[objectives#DFO-1015 Prepare for a digital investigation|DFO-1015]] | Prepare for a digital investigation | 9 |
| [[objectives#DFO-1012 Locate potentially relevant content|DFO-1012]] | Locate potentially relevant content | 9 |
| [[objectives#DFO-1004 Conduct research|DFO-1004]] | Conduct research | 8 |
| [[objectives#DFO-1016 Overcome protection mechanisms|DFO-1016]] | Overcome protection mechanisms | 7 |
| [[objectives#DFO-1006 Acquire data|DFO-1006]] | Acquire data | 6 |
| [[objectives#DFO-1017 Extract artifacts stored by the operating system|DFO-1017]] | Extract artifacts stored by the operating system | 4 |
| [[objectives#DFO-1011 Extract artifacts stored by applications|DFO-1011]] | Extract artifacts stored by applications | 4 |
| [[objectives#DFO-1003 Review content for relevance|DFO-1003]] | Review content for relevance | 3 |
| [[objectives#DFO-1010 Preserve digital evidence|DFO-1010]] | Preserve digital evidence | 3 |
| [[objectives#DFO-1021 Access device data for acquisition|DFO-1021]] | Access device data for acquisition | 3 |
| [[objectives#DFO-1014 Find potential digital evidence sources|DFO-1014]] | Find potential digital evidence sources | 2 |
| [[objectives#DFO-1005 Prioritize digital evidence sources|DFO-1005]] | Prioritize digital evidence sources | 2 |
| [[objectives#DFO-1002 Extract data from specific formats|DFO-1002]] | Extract data from specific formats | 2 |
| [[objectives#DFO-1007 Reduce data under consideration|DFO-1007]] | Reduce data under consideration | 2 |
| [[objectives#DFO-1023 Extract specific artifact types|DFO-1023]] | Extract specific artifact types | 1 |
| [[objectives#DFO-1020 Document digital forensic activities|DFO-1020]] | Document digital forensic activities | 1 |

All other objectives currently have 0 techniques derived from ingested papers.

## Notes

- The wiki was previously bootstrapped from a `data.json` SOLVE-IT export, but that source file, `scripts/bootstrap-wiki.mjs`, and `title-overrides.json` are not present in this repository snapshot, and no corresponding entity pages existed on disk. This index was reset on 2026-08-09 to reflect actual on-disk state.
- The current ingestion source is the academic paper corpus under `raw/` (folders `DI/`, `IEEE Access/`, `JDFSL/`), not `data.json`. Each ingested paper is recorded as a `DFCite-` reference in `wiki/references.md`.
- **Ingestion policy (2026-08-09):** entity pages are named and scoped as reusable method/defect *categories*, not per-paper implementations. Before creating a new page, existing pages are searched for a conceptual match and reused (new `source_refs` appended) rather than duplicated. See "Ingesting from a raw paper corpus" in AGENT.md. Confirmed multi-paper technique merges so far: [[weaknesses/In-memory credential recovery fails once the relevant memory page is overwritten]] (rclone + Bitcoin wallet papers); [[techniques/Unsupervised deep-learning behavioral anomaly detection]] (ICS telemetry + video surveillance); [[techniques/Captured-credential-based cloud account access]] (token-API + browser-credential migration); [[techniques/Blockchain-anchored digital evidence integrity and chain-of-custody management]] (on-camera video fingerprinting + general IoT evidence chain-of-custody + a second blockchain-IoT-forensics SLR); [[techniques/Structured IoT-specific digital forensic process model application]] (IoT process-model SLR + an interconnectivity-identification phase extension); [[techniques/Reverse-engineered weak app-level lock defeat and content decryption]] (LG Content Lock + WhatsApp Web/UWP decryption); [[techniques/Similarity-based Android malware family detection]] (class-level fuzzy hashing + NLP control-flow similarity); [[techniques/Automated synthesis of digital forensic training and validation datasets]] (LLM-storyboard mobile synthesis + AKF declarative-scripting VM synthesis); [[techniques/Digital forensic readiness assessment and by-design frameworks]] (DFRCF/DFMM maturity assessment + SE-integrated forensic-by-design); [[techniques/Mobile application artifact location discovery and extraction]] (Argus dynamic snapshot discovery + ASNAAT wordlist-driven extraction); [[techniques/Android system-log-based automotive forensic reconstruction]] (IVI ring-buffer/log acquisition + OBD-II app/Bluetooth/log-buffer correlation, which also merged their near-identical volatile-log weaknesses into one); [[techniques/Dictionary attack password recovery via mangling-rule generation and cloud GPU execution]] (RuleForge rule generation + cloud GPU dictionary-attack execution). **2026-08-10 consolidation pass:** after user feedback that the technique/weakness/mitigation counts were growing too close to 1:1 with papers ingested, performed a dedicated review of all pages added in this session (papers 51-95) and merged 6 technique pairs (listed above, from a starting 93 down to 87) plus 1 weakness/mitigation pair (the two automotive volatile-log pages), following the same reuse-first, keep-the-lower-ID convention used for cross-batch merges; each merge required a genuinely shared underlying mechanism, not just a shared objective or theme (candidate pairs sharing only a theme, e.g. different forensic-tool-validation methodologies, were deliberately left separate per AGENT.md's guidance against forcing merges that would reduce precision). Not every paper produces new entity pages: DFCite-1079 ("Another brick in the wall") and DFCite-1089 ("Avoiding Burnout at the Digital Forensics Coalface") were cited in references.md with no technique/weakness/mitigation page, since neither is about an investigative technique (a DF-curricula survey and an occupational-stress-management paper, respectively). **Provenance anomaly:** DFCite-1090's source PDF (`raw/DI/Benford_s law applied to digital forensic analysis..pdf`) does not actually contain a paper about Benford's law applied broadly to digital forensic analysis — its real content is "Benford's Law as a Forensic Tool for Identifying Anomalous Chat Behavior in Instant Messaging" (Mahindra & Karabiyik, IEEE SmartNets 2026); it was ingested and cited under its true title per the actual PDF content, with the discrepancy flagged in its references.md note. Across the first 95 papers, technique/weakness/mitigation counts (87/99/99) reflect this post-consolidation state.
- `objectives.md` (the 23 DFO- objectives) was retained as-is as a stable navigation hub, since paper-derived techniques still map cleanly onto it.
- **Requested ingestion of 50 additional papers (files 51-100) is now complete** as of this entry (2026-08-10), bringing total progress to 100/518. Next batch, if ingestion continues: `raw/DI`, files 101-105 (alphabetical): "Busting up Monopoly- Methods for modern darknet marketplace forensics", "Camera Obscura- Exploiting in-camera processing for image counter forensics", "CAMID- An assuasive approach to reveal source camera through inconspicuous evidence", "Can signs of digital coercive control be evidenced in mobile operating system settings? - A guide for first responders", "Case note- Digital forensic challenges through synthetic CSAM in video games" — continue in file-name alphabetical order within `raw/DI` before moving to `raw/IEEE Access` and `raw/JDFSL`.
- **2026-08-14: parallel-worktree `raw/IEEE Access` ingestion begins.** This worktree (a separate isolated git worktree from the main checkout) was tasked with ingesting all 52 `raw/IEEE Access` papers and, time permitting, the 24 `raw/JDFSL` papers, while a separate concurrent agent continues `raw/DI` ingestion past file 100 in the main checkout/worktree. Because this worktree's branch point predates that later `raw/DI` progress and the STYLE_GUIDE.md-alignment commit, all reuse-first searches in this session were performed only against this worktree's own on-disk pages (90/103/103 techniques/weaknesses/mitigations, 100 references, from `raw/DI` files 1-100), not the main checkout's later state — this is expected and intentional per the task's ID-reservation design, not an oversight. All new entity IDs from this point use the reserved 2001+ block (DFT-2001+, DFW-2001+, DFM-2001+, DFCite-2001+) to avoid collision at merge time with the main worktree's concurrently-assigned sequential 1101+ IDs. New technique names follow the current (STYLE_GUIDE.md) present-tense-imperative-verb convention even though this worktree's pre-existing 90 technique pages still use the earlier noun-phrase convention, since STYLE_GUIDE.md and the current AGENT.md (read directly from the main checkout path per the task instructions) govern all new content regardless of this worktree's stale docs.
