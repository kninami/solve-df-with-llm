---
id: DFM-2085
type: mitigation
name: Verify each artifact's temporal, syntactic, and semantic integrity by default rather than only when suspicion arises
source_refs:
  - DFCite-2098
updated_at: 2026-08-16
status: complete
---

# Verify each artifact's temporal, syntactic, and semantic integrity by default rather than only when suspicion arises

## Summary

Make it standard practice to verify every case-critical artifact's temporal, syntactic, and semantic integrity as a matter of routine, rather than only investigating integrity when something already looks suspicious.

## Addresses

- [[weaknesses/Digital forensic investigations implicitly extend default trust to artifacts, tools, and process steps without explicit verification]]

## How To Apply

For each artifact expected to bear significant weight in an investigation's conclusions, explicitly check and document all three integrity dimensions rather than assuming one implies the others: temporal integrity (do the artifact's timestamps hold up against independent corroboration and internal consistency checks), syntactic integrity (does the artifact's structure/format validate against its expected specification, checked via hash/checksum comparison or format-conformance validation where available), and semantic integrity (does the artifact's actual content plausibly represent what it purports to, checked via cross-referencing against independent sources or artifact-specific tampering-detection techniques such as [[techniques/Recognize artefact tampering using inductive reasoning over temporal-logic system-state features]]). Apply this checklist as a default step in casework, not only when a specific reason to suspect tampering has already surfaced, since undetected tampering is by definition tampering that has not yet triggered suspicion.

## References

- [DFCite-2098] "The case for Zero Trust Digital Forensics", FSI: Digital Investigation 48, 2024.
