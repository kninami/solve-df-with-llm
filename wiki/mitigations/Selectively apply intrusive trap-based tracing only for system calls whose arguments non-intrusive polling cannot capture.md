---
id: DFM-1270
type: mitigation
name: Selectively apply intrusive trap-based tracing only for system calls whose arguments non-intrusive polling cannot capture
source_refs:
  - DFCite-1296
updated_at: 2026-08-14
status: complete
---

# Selectively apply intrusive trap-based tracing only for system calls whose arguments non-intrusive polling cannot capture

## Summary

Run non-intrusive VMI register polling as the default tracing method for its accuracy and negligible overhead, and only fall back to intrusive trap-based tracing for the specific subset of system calls whose argument content is actually needed for the investigation, limiting the resulting performance and detectability cost to just those calls rather than applying it across the entire trace.

## Addresses

- [[weaknesses/Non-intrusive VMI system-call tracing cannot reliably capture system call arguments]]

## How To Apply

Use non-intrusive polling to obtain the full system-call sequence and timing first, since this captures 100% of the call sequence with negligible overhead and minimal risk of tipping off malware to the presence of monitoring. Where the investigation specifically requires the arguments of certain calls (e.g. the file path opened, or the buffer content written), identify those specific call sites from the sequence trace and apply a hybrid approach: place an intrusive trap only on those specific call instances or call types, accepting the resulting localized overhead and detectability risk rather than applying trap-based tracing to the entire execution. Document which portions of a trace were captured non-intrusively (sequence-only, no argument content) versus intrusively (with arguments), since the two portions carry different evidentiary completeness.

## References

- [DFCite-1296] Nguyen, Orenbach and Atamli, 2022, "Live system call trace reconstruction on Linux", DFRWS 2022 USA; FSI: Digital Investigation 42, 301398.
