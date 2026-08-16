---
id: DFT-1288
type: technique
name: Acquire a PLC's complete volatile memory remotely by injecting a memory-duplicator into its control logic
description: Remotely acquire the entire volatile memory contents of a programmable logic controller (PLC) — while it continues controlling its physical process without interruption — by appending a harmless memory-duplicator routine to the PLC's own running control logic, which copies memory regions normally unreachable through the ICS communication protocol into a protocol-mapped address space that can then be read out over the network.
objective_ids:
  - DFO-1021
weakness_ids:
  - DFW-1298
aliases:
  - PEM (PLC mEMory extractor)
source_refs:
  - DFCite-1331
updated_at: 2026-08-15
status: complete
---

# Acquire a PLC's complete volatile memory remotely by injecting a memory-duplicator into its control logic

## Summary

Existing PLC memory-acquisition methods are each deficient for real-world forensic use: built-in vendor support is not universally available and typically cannot dump memory while the PLC is actively controlling a process; a hardware debug port (JTAG) requires physical access, PCB disassembly, and power cycling that itself destroys the very volatile evidence being sought, and manufacturers frequently hide or remove debug pins from production boards; and standard ICS protocol-based memory reads can only access the limited memory addresses the protocol itself maps, missing most of the PLC's actual memory. PEM (PLC mEMory extractor) instead appends a memory-duplicator to the PLC's own control logic — the program the PLC is already running — which copies otherwise-unreachable memory regions into the protocol-mapped address space, making the entire memory readable over the network without disrupting the PLC's operation.

## Details

The framework satisfies three requirements the authors establish as necessary for realistic ICS forensic acquisition: **nondisruptive** (memory acquisition occurs while the PLC continues controlling its physical process, essential given the very high availability expectations of most ICS environments), **remote** (acquisition occurs over the network rather than requiring physical presence at a field site, which may be geographically dispersed), and **complete** (the entire PLC memory is acquired, not just the subset mapped to an ICS protocol's own address space). The memory duplicator is injected into the running control logic and copies local memory contents — including regions never exposed by the PLC's native ICS protocol — into a region of memory that is protocol-mapped and therefore externally readable, effectively using the PLC's own legitimate control-logic-update mechanism as the acquisition channel.

## Examples

- A case study on a gas pipeline testbed using a Schneider Electric Modicon M221 PLC demonstrated PEM identifying evidence of a companion control-logic attack (introduced in the same paper) that modifies the PLC's in-memory firmware to be more stealthy and persistent than prior attack techniques — evidence that was recoverable specifically because PEM's memory dump was complete, including the in-memory firmware regions the attack targeted.

## Related Objectives

- `DFO-1021` Access device data for acquisition

## Related Weaknesses

- [[weaknesses/PEM's memory-duplicator injection modifies a PLC's running control logic before memory can be acquired]]

## References

- [DFCite-1331] Zubair, Ayub, Yoo, and Ahmed, 2022, "PEM: Remote forensic acquisition of PLC memory in industrial control systems", FSI: Digital Investigation 40, 301336.
