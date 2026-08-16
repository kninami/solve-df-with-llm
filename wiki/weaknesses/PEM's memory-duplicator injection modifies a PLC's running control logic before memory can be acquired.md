---
id: DFW-1298
type: weakness
name: PEM's memory-duplicator injection modifies a PLC's running control logic before memory can be acquired
description: Because PEM's acquisition method works by appending a memory-duplicator routine to the target PLC's own running control logic, the acquisition process itself alters the state of the evidence device (its running program and, consequently, some memory contents and execution behavior) before any memory is read out, which is in tension with the general forensic principle of acquiring evidence without altering it.
categories:
  - ASTM_INAC_ALT
mitigation_ids:
  - DFM-1300
source_refs:
  - DFCite-1331
updated_at: 2026-08-15
status: complete
---

# PEM's memory-duplicator injection modifies a PLC's running control logic before memory can be acquired

## Summary

Unlike passive memory-acquisition methods that read state without modifying it, PEM's core mechanism requires writing new code (the memory duplicator) into the PLC's active control logic before any memory contents can be extracted. This is a deliberate, necessary trade-off to achieve nondisruptive, remote, complete acquisition (avoiding the alternative of a JTAG debug-port connection, which itself destroys volatile evidence via forced power cycling and physical disassembly) — but it is nonetheless an alteration of the running system, made before acquisition rather than during a passive read.

## Why It Matters

An investigator relying on a PEM-acquired memory dump should be prepared to explain and justify this alteration if evidentiary integrity is challenged, since strict readings of forensic soundness principles favor acquisition methods that do not modify the source. Failing to document exactly what was injected, when, and its expected memory/execution footprint could weaken the acquired evidence's credibility in proceedings, or could — if the injected duplicator has any unintended side effect on the physical process being controlled — introduce genuine risk to the ICS environment being investigated, which is precisely the disruption the technique otherwise avoids.

## Related Mitigations

- [[mitigations/Document and validate the memory-duplicator's footprint before and after PLC control-logic injection]]

## Used By

- [[techniques/Acquire a PLC's complete volatile memory remotely by injecting a memory-duplicator into its control logic]]

## References

- [DFCite-1331] Zubair, Ayub, Yoo, and Ahmed, 2022, "PEM: Remote forensic acquisition of PLC memory in industrial control systems", FSI: Digital Investigation 40, 301336.
