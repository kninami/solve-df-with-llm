---
id: DFT-1205
type: technique
name: Reconstruct file-system events from ReFS Logfile transaction-opcode replay
description: Parse the Resilient File System (ReFS)'s Logfile and Change Journal transaction records, matching observed sequences of Redo-Record opcodes against known finite-state-machine patterns for file/directory creation, modification, renaming, movement, and deletion, to reconstruct a timestamped and full-path-annotated timeline of past file-system activity on a ReFS volume.
objective_ids:
  - DFO-1001
weakness_ids:
  - DFW-1215
aliases:
  - Awesome ReFS Investigation tool (ARIN)
  - ReFS Logfile and Change Journal forensic methodology
source_refs:
  - DFCite-1227
  - DFCite-1269
updated_at: 2026-08-14
status: complete
---

# Reconstruct file-system events from ReFS Logfile transaction-opcode replay

## Summary

Unlike NTFS's well-studied `$Logfile` and `$UsnJrnl`, ReFS's equivalent journaling artifacts — the Logfile and the Change Journal — use entirely new, previously undocumented record formats (Log Record and `USN_RECORD_V3`); reverse-engineering `ReFS.sys` to document these formats and the opcode sequences each type of file-system event produces enables an investigator to reconstruct past file/directory creation, modification, rename, move, and deletion activity, along with the approximate time each event occurred, from a ReFS volume image.

## Details

The Change Journal, similar in role to NTFS's `$UsnJrnl`, records USN-style change events using the `USN_RECORD_V3` format, but is deactivated by default on ReFS volumes (an investigator must explicitly enable it via `fsutil` to have it available), making it uncommon in the field despite its more intuitive, directly-interpretable structure. The Logfile, activated by default, is the more consistently useful artifact: it uses an Allocate-On-Write transactional model recording only redo (not undo) operations, structured as Logfile Entries containing an Entry Header, Log Record Header, and one or more Redo Records, each carrying a 1-byte opcode (of 28 defined ReFS-specific opcodes, e.g. `Redo Insert Row`, `Redo Delete Row`, `Redo Allocate`) plus a Data Offset Array pointing to the transaction data needed to redo the operation. By experimentally generating file/directory create, update, rename, move, copy, and delete events and observing the resulting opcode sequences, the study derived finite-state-machine patterns that let each event type be recognized from its characteristic opcode sequence (e.g. file creation: `0x01→0x04→0x10→0x00→0x04→0x01→0x00`), with event time bounded by locating the specific Redo Record within the sequence that updates the file/directory's time-metadata fields, and full file/directory path reconstructed by tracing the object ID referenced in the transaction data through the Parent Child Table and Object ID Table back to the root directory. Both the Logfile's Data area and the Change Journal use a circular buffer for storage, so where the Change Journal is available it can be used to cross-verify the Logfile-derived timeline.

## Examples

- The released ARIN (Awesome ReFS Investigation tool) parses both the Change Journal and the Logfile from a ReFS volume image or extracted journaling files and displays a reconstructed event history with inferred timestamps.
- On an experimental ReFS volume, comparing ARIN's Logfile-derived reconstruction of ten known user actions (file creation, content write, copy/paste, rename, directory creation, move, and two deletions) against the same events derived independently from the Change Journal produced an exact match for both event type and timestamp, validating the Logfile-only reconstruction methodology even when the Change Journal (which is disabled by default) is unavailable.
- A later study of ReFS 3.7 volumes (a newer on-disk format version than 3.4) discovered additional Redo-Record opcodes absent from the original opcode catalog, and used opcode-sequence replay to build a reference database distinguishing the deletion patterns of twelve different anti-forensic data-wiping tools and algorithms (see [[techniques/Identify a data-wiping tool from ReFS Logfile deletion opcode patterns]]).

## Related Objectives

- `DFO-1001` Reconstruct events

## Related Weaknesses

- [[weaknesses/ReFS's circular-buffer journal cannot recover file events older than the buffer's retention window]]

## References

- [DFCite-1227] Lee et al., 2021, "Forensic analysis of ReFS journaling", FSI: Digital Investigation 38.
- [DFCite-1269] Kim and Lee, 2026, "Identification of data wiping tools based on deletion patterns in ReFS $Logfile", FSI: Digital Investigation 56, 302069. Extends the opcode catalog to ReFS 3.7 and applies opcode-sequence replay to anti-forensic wiping-tool identification.
