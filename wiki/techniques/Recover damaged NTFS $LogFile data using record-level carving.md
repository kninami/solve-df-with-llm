---
id: DFT-2032
type: technique
name: Recover damaged NTFS $LogFile data using record-level carving
description: The process of reconstructing file system change history from a damaged or partially corrupted NTFS $LogFile - whose restart-page or logging-page headers have been destroyed by an accident, disaster, or cyber-terrorism attack - by deriving a page-specific record-carving signature from each page's own sequence number rather than relying on a fixed magic-number value at the start of each record.
objective_ids:
  - DFO-1013
weakness_ids:
  - DFW-2032
aliases:
  - Record carving-based $LogFile recovery
  - NTFS Data Tracker
source_refs:
  - DFCite-2032
updated_at: 2026-08-14
status: partial
---

# Recover damaged NTFS $LogFile data using record-level carving

## Summary

When a Windows system's file system is damaged by physical disaster (fire, flooding, sudden power loss) or a destructive cyber-terrorism attack that overwrites disk structures, existing $LogFile recovery tools that carve at the file or page level fail once a page's header (its "RSTR"/"RCRD" magic-number signature) is destroyed, because they have no way to locate records within an unrecognized page. An investigator instead recovers at the record level: since every record within a given logging page shares the same sequence number (derivable from the page header's Last LSN field, or reconstructed from surrounding pages if that header is also damaged), a page-specific 8-byte-aligned signature can be generated and used to carve individual records directly from the page's raw bytes, salvaging data that page-level carving would discard entirely.

## Details

DFCite-2032's five-step method first carves all recognizable restart and logging pages using their magic numbers, then determines the $LogFile's internal structure (LFS version, and the boundary between the buffer and normal logging areas) from the recovered restart page(s) - or, if no restart page survived, by detecting where logging-page offset numbers begin a continuous increasing sequence. Uncarved (header-damaged) pages within the now-known logging-area ranges are recovered by generating a virtual header, using either the last valid LSN found by scanning forward from the page, or the page's expected position in the LSN sequence. Recovered logging pages are sorted into correct order (since the physical order on disk does not always match logical journal order, especially after unmount/remount events fragment the buffer-to-normal-area circulation), and finally, record carving is performed within each sorted page using its page-specific sequence-number-derived signature, extracting Redo/Undo timestamp and MFT-operation data even from pages whose own headers were destroyed.

## Examples

- DFCite-2032's 12-image damage-scenario evaluation (LFS 1.1 and 2.0, with restart-page, buffer-logging-page, and normal-logging-page header corruption individually and combined): the proposed tool (integrated into NTFS Log Tracker/NTFS Data Tracker) recovered all undamaged records in every scenario, while X-Ways Forensics v19.9 SR-4 and Bulk Extractor v2.0 failed file/page carving entirely once any restart-page or logging-page header was corrupted.
- Real-case application: recovering $LogFile data from the 2014 MV Sewol ferry's Windows XP CCTV system after it sank, confirming from the recovered journal's data-run history that the CCTV system had recorded video through 08:32 but that the metadata for its next two one-minute recording intervals (08:33, 08:34) was in memory but never written to $MFT before the system stopped - not, as initially unclear, evidence the files never existed.

## Related Objectives

- `DFO-1013` Access partitions, volumes, and file systems data

## Related Weaknesses

- [[weaknesses/NTFS $LogFile recovery cannot retrieve metadata changes never flushed from memory before a sudden system stop]]

## References

- [DFCite-2032] Oh et al., "Forensic recovery of file system metadata for digital forensic investigation", IEEE Access, 2022 — source of the record-carving recovery method, the 12-scenario evaluation, and the MV Sewol case study described above.
