---
id: DFW-1263
type: weakness
name: PLC memory acquisition via JTAG risks crashing or hanging the controller when acquisition parameters or address ranges are untested
description: JTAG was designed for hardware fault debugging, not forensic memory acquisition, so reading an untested address range or using overly aggressive timing parameters against a live PLC can crash or hang the controller — an unacceptable outcome for a device directly controlling a physical industrial process, and one that is not knowable in advance without prior testing.
categories:
  - ASTM_INCOMP
  - ASTM_INAC_COR
mitigation_ids:
  - DFM-1264
source_refs:
  - DFCite-1284
updated_at: 2026-08-14
status: complete
---

# PLC memory acquisition via JTAG risks crashing or hanging the controller when acquisition parameters or address ranges are untested

## Summary

Attempting to read certain address ranges on a PLC's JTAG interface immediately halts the controller, and disconnection from engineering software or debugger crashes can occur if acquisition parameters (read block size, clock speed, inter-read wait time) are set too aggressively for a given memory IC's specifications, none of which is documented by PLC vendors in advance and which can only be discovered through iterative, potentially destructive trial-and-error testing.

## Why It Matters

A PLC directly controls a physical industrial process (e.g. a power grid station, water treatment system, or manufacturing line), so crashing or hanging it during forensic acquisition is not merely an inconvenience — in a live deployment it could itself cause the physical disruption the investigation is meant to explain, and even on a decommissioned or isolated unit a crash can interrupt or corrupt the acquisition in progress. Discovering safe address ranges and parameters requires deliberately risking exactly this outcome, making it unsafe to perform this discovery process directly against the actual suspect PLC.

## Related Mitigations

- [[mitigations/Build and verify a JTAG acquisition profile against a test PLC of the same model before acquiring a suspect PLC's memory]]

## Used By

- [[techniques/Acquire a PLC's memory contents using a JTAG acquisition profile]]

## References

- [DFCite-1284] Rais, Awad, Lopez and Ahmed, 2021, "JTAG-based PLC memory acquisition framework for industrial control systems", DFRWS 2021 USA; FSI: Digital Investigation 37, 301196.
