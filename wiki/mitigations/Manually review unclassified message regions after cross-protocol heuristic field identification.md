---
id: LWM-1304
type: mitigation
name: Manually review unclassified message regions after cross-protocol heuristic field identification
source_refs:
  - LWCite-1337
updated_at: 2026-08-15
status: complete
---

# Manually review unclassified message regions after cross-protocol heuristic field identification

## Summary

After running cross-protocol heuristics against a captured protocol, treat any byte ranges left unclassified as requiring manual investigation rather than assuming they are unimportant, since they may represent vendor-unique fields with no analog among the protocols the heuristics were built from.

## Addresses

- [[weaknesses/Cross-protocol heuristic transfer cannot identify an ICS protocol field with no analog in any previously-known protocol]]

## How To Apply

After applying [[techniques/Reverse-engineer a proprietary ICS protocol's fields using cross-protocol heuristic pattern transfer]] to a target protocol, explicitly map which byte ranges of a representative message were successfully classified into a known field type, and treat the remaining, unclassified byte ranges as candidates for manual analysis (message diffing across varied operational scenarios, vendor documentation review, or targeted binary analysis of the PLC's communication stack, where available) rather than assuming they carry no forensic significance. Where the investigation's outcome may hinge on a specific unclassified region, seek additional protocol knowledge (from the vendor, from public vulnerability research, or from an analyst experienced with that specific vendor's product line) before concluding the field is not relevant.

## References

- [LWCite-1337] Qasim, Jo, and Ahmed, 2023, "PREE: Heuristic builder for reverse engineering of network protocols in industrial control systems", FSI: Digital Investigation 45, 301565.
