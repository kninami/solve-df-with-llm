---
id: LWT-1095
type: technique
name: Recover corrupted FIT ride-data files using multi-phase sliding-window carving
description: Recover valid ride-data records from a corrupted bike computer FIT (Flexible and Interoperable Data Transfer) file by combining multiple data-carving phases — including a sliding-window pattern match that locates definition messages via a regular expression signature rather than relying purely on sequential offset-based parsing — so that data located between or after corrupted portions of the file can still be recovered, instead of the recovery process halting entirely at the first undecodable message.
objective_ids:
  - DFO-1018
weakness_ids:
  - LWW-1101
aliases:
  - Multi-phase sliding-window carving recovery of corrupted FIT ride-data files
source_refs:
  - LWCite-1095
updated_at: 2026-08-10
status: complete
---

# Recover corrupted FIT ride-data files using multi-phase sliding-window carving

## Summary

FIT files store ride data as a chain of messages where each data message references a preceding definition message to be correctly interpreted, and existing recovery tools that rely on sequential parsing stop decoding entirely once a corruption is encountered, losing all subsequent valid records even though most of them may be perfectly intact. Because definition messages are not always stored close together, simply skipping to the next definition message's offset after a decode failure risks omitting many valid data messages situated in between — a serious problem since cycling workout data is typically recorded once per second, so even a small skipped region can mean losing substantial accident-relevant information.

## Details

The method locates definition messages using a regular expression signature (`[\x40-\x4F]\x00\x00([\x00-\xFF]\x00|[\x00-\x77]\x01)[\x01-\x64]`) via a sliding-window pattern match across the raw file, rather than depending on successful sequential decoding to reach each definition message in turn. Combining this carving phase with the standard parse-mode decoding recovers substantially more valid ride records from corrupted files than sequential-parsing-only recovery tools, and the location of decode failures during parse mode can itself indicate which portion of a file is corrupted.

## Examples

- Across five real-world corrupted FIT files, the proposed method recovered more RECORD-type ride-data messages than five compared existing recovery tools (GOTOES utility for Strava, RUNALYZE FIT Viewer, the official FIT SDK's activity file repair tool, FIT File Tools, and Garmin's FIT file conversion and repair tool) in every tested case.

## Related Objectives

- `DFO-1018` Read data from digital evidence storage formats

## Related Weaknesses

- [[weaknesses/Sequential FIT-file parsers stop decoding entirely at the first corrupted message, losing all subsequent valid ride data]]

## References

- [LWCite-1095] Song and Oh, 2023, "Bike computer forensics: An efficient and robust method for FIT file recovery", FSI: Digital Investigation 46.
