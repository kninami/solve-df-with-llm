---
id: DFM-1300
type: mitigation
name: Document and validate the memory-duplicator's footprint before and after PLC control-logic injection
source_refs:
  - DFCite-1331
updated_at: 2026-08-15
status: complete
---

# Document and validate the memory-duplicator's footprint before and after PLC control-logic injection

## Summary

Before deploying a control-logic memory-duplicator against a live PLC, validate on an identical or matched test PLC that the injection does not alter the physical process's behavior, and thoroughly document the duplicator's own code, its memory footprint, and its expected effect on the running control logic so the alteration can be fully accounted for when the acquired evidence is presented.

## Addresses

- [[weaknesses/PEM's memory-duplicator injection modifies a PLC's running control logic before memory can be acquired]]

## How To Apply

Before using [[techniques/Acquire a PLC's complete volatile memory remotely by injecting a memory-duplicator into its control logic]] on a live target, first validate the memory-duplicator injection against a matched test PLC and control-logic program (same model, firmware, and program where possible) to confirm it does not alter the physical process's output or introduce timing changes to the scan cycle. Retain a copy of the exact duplicator code injected, the injection timestamp, and a description of its expected memory footprint as part of the case record. Where the alteration's forensic-soundness implications may be challenged, be prepared to demonstrate — via the test-PLC validation — that the injected code's own effect on memory state is well-understood, bounded, and clearly separable from the evidence of interest.

## References

- [DFCite-1331] Zubair, Ayub, Yoo, and Ahmed, 2022, "PEM: Remote forensic acquisition of PLC memory in industrial control systems", FSI: Digital Investigation 40, 301336.
