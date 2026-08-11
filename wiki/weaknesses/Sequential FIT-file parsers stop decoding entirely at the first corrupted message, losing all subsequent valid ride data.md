---
id: DFW-1101
type: weakness
name: Sequential FIT-file parsers stop decoding entirely at the first corrupted message, losing all subsequent valid ride data
description: Because a FIT file's data messages depend on referencing a preceding definition message to be interpreted, a purely sequential parser that encounters a corrupted or undecodable message stops decoding entirely at that point, losing all subsequent valid ride-data records in the file even if they are otherwise perfectly intact, since the parser has no mechanism to relocate the next valid definition message and resume.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1101
source_refs:
  - DFCite-1095
updated_at: 2026-08-10
status: complete
---

# Sequential FIT-file parsers stop decoding entirely at the first corrupted message, losing all subsequent valid ride data

## Summary

Testing against corrupted real-world FIT files, four of five compared recovery tools "marked the same records due to their reliance on the parsing process, which can cause the process to stop if errors are encountered" — meaning the amount of data recovered by those tools was determined almost entirely by how early in the file the first corruption occurred, not by how much of the file's data was actually intact.

## Why It Matters

Because cycling ride data (including accident-relevant metrics like speed and location) is typically recorded once per second, a sequential parser that stops at an early corruption in an otherwise mostly-intact file can discard a large volume of forensically relevant, recoverable data — potentially including the specific segment of the ride most relevant to an accident reconstruction or criminal investigation, if that segment happens to fall after the corruption point.

## Related Mitigations

- [[mitigations/Use carving-based or multiple FIT recovery tools rather than relying on a single sequential parser]]

## Used By

- [[techniques/Multi-phase sliding-window carving recovery of corrupted FIT ride-data files]]

## References

- [DFCite-1095] Song and Oh, 2023, "Bike computer forensics: An efficient and robust method for FIT file recovery", FSI: Digital Investigation 46.
