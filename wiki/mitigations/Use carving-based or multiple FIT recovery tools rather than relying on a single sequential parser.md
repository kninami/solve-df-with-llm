---
id: LWM-1101
type: mitigation
name: Use carving-based or multiple FIT recovery tools rather than relying on a single sequential parser
source_refs:
  - LWCite-1095
updated_at: 2026-08-10
status: complete
---

# Use carving-based or multiple FIT recovery tools rather than relying on a single sequential parser

## Summary

When recovering data from a corrupted FIT file, use a carving-based recovery method (or run multiple independent recovery tools and combine their results) rather than relying on a single sequential parser that will stop at the first corruption point.

## Addresses

- [[weaknesses/Sequential FIT-file parsers stop decoding entirely at the first corrupted message, losing all subsequent valid ride data]]

## How To Apply

Apply a sliding-window/signature-based carving pass to locate definition messages independent of successful sequential parsing, in addition to (not instead of) standard parse-mode decoding, and treat the location of parse failures as an indicator of where corruption begins rather than the end of usable data. Where the case is significant, run multiple available recovery tools against the same file and merge their recovered record sets, since different tools' underlying assumptions can recover different, only partially-overlapping subsets of the valid data.

## References

- [LWCite-1095] Song and Oh, 2023, "Bike computer forensics: An efficient and robust method for FIT file recovery", FSI: Digital Investigation 46.
