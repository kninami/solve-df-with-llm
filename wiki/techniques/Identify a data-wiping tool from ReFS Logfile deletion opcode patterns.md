---
id: LWT-1234
type: technique
name: Identify a data-wiping tool from ReFS Logfile deletion opcode patterns
description: Compare the sequence of Redo-Record opcodes a deletion operation produced in a ReFS volume's Logfile against a reference database of opcode patterns characteristic of specific anti-forensic data-wiping tools and algorithms, to identify which tool (and often which wiping algorithm) was used.
objective_ids:
  - DFO-1019
weakness_ids:
  - LWW-1215
aliases:
  - ReFS $Logfile-based data-wiping-tool identification
source_refs:
  - LWCite-1269
updated_at: 2026-08-14
status: complete
---

# Identify a data-wiping tool from ReFS Logfile deletion opcode patterns

## Summary

Different anti-forensic data-wiping tools and algorithms (single-pass zero-fill, multi-pass DoD/Gutmann-style overwrite, secure-delete utilities, etc.) each produce a distinguishable, repeated sequence of ReFS Logfile Redo-Record opcodes as they overwrite and then delete a file, so comparing an observed opcode sequence against a reference database built from known tools lets an investigator determine which wiping tool — and often which specific wiping algorithm or pass count — was used, rather than only knowing that deletion occurred.

## Details

This builds on the same underlying artifact and parsing methodology as [[techniques/Reconstruct file-system events from ReFS Logfile transaction-opcode replay]] — parsing the ReFS Logfile's Redo Records and their 1-byte opcodes — but applies it to a distinct forensic question: rather than reconstructing ordinary file activity, the analysis specifically targets the repeated overwrite-then-delete opcode bursts that a wiping tool's multi-pass behavior produces, which differ measurably in count, ordering, and inter-burst timing from a single ordinary user deletion. Building the reference database requires running each candidate wiping tool against a controlled ReFS test volume and cataloging the resulting opcode sequence as that tool's signature; testing against ReFS 3.7 (a newer on-disk version than the 3.4 volumes studied in earlier ReFS journaling research) surfaced additional previously undocumented opcodes not present in the earlier opcode catalog, which had to be incorporated into the parser before wiping-tool patterns could be recognized reliably. Because the Logfile's Data area is a circular buffer, only wiping activity recent enough not to have been overwritten by subsequent transactions can be recovered this way — see [[weaknesses/ReFS's circular-buffer journal cannot recover file events older than the buffer's retention window]].

## Examples

- Twelve data-wiping tools and algorithms tested against a ReFS 3.7 volume each produced a distinguishable repeated opcode pattern, allowing the specific tool used in a given case to be identified from Logfile analysis alone.
- Three additional Redo-Record opcodes not documented in prior ReFS 3.4 journaling research were identified while building the ReFS 3.7 wiping-tool reference database, extending the opcode catalog used by opcode-replay-based ReFS analysis generally.

## Related Objectives

- `DFO-1019` Detect anti-forensics and other anomalies

## Related Weaknesses

- [[weaknesses/ReFS's circular-buffer journal cannot recover file events older than the buffer's retention window]]

## References

- [LWCite-1269] Kim and Lee, 2026, "Identification of data wiping tools based on deletion patterns in ReFS $Logfile", FSI: Digital Investigation 56, 302069.
