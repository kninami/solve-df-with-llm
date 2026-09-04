---
id: LWM-1111
type: mitigation
name: Perform deeper save-state internal-structure analysis to reconstruct fine-grained user interaction timelines
source_refs:
  - LWCite-1105
updated_at: 2026-08-12
status: complete
---

# Perform deeper save-state internal-structure analysis to reconstruct fine-grained user interaction timelines

## Summary

When session-level detail matters beyond a coarse usage window, parse the internal contents of each save-state file (log, structured data, version, and embedded screenshot components) rather than relying solely on the file's creation timestamp, to reconstruct a more precise timeline of user actions within each session.

## Addresses

- [[weaknesses/Save-state creation-timestamp sorting alone cannot reconstruct fine-grained user interaction within an application session]]

## How To Apply

Extract and parse each save-state archive's internal components (e.g. a Ren'Py `.sav` file's log file, JSON state data, engine version file, and embedded screenshot) rather than treating the file as opaque. Use the structured internal data to identify which specific in-application content or progression point each save corresponds to, and combine this with the file's timestamp to build a more granular per-session timeline than creation-time sorting alone provides.

## References

- [LWCite-1105] Jaeckel and Labudde, 2026, "Case note: Digital forensic challenges through synthetic CSAM in video games", FSI: Digital Investigation 57.
