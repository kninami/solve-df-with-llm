---
id: DFW-1030
type: weakness
name: OBD-based diagnostic acquisition cannot reach in-vehicle components not connected to the diagnostic interface
description: While the OBD-II/UDS/DoIP diagnostic path can enumerate and query all ECUs wired to the vehicle's diagnostic bus, not every relevant in-vehicle component is connected to that interface, so purely diagnostic-interface-based acquisition systematically misses evidence held on components outside its reach.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1030
source_refs:
  - DFCite-1021
updated_at: 2026-08-09
status: complete
---

# OBD-based diagnostic acquisition cannot reach in-vehicle components not connected to the diagnostic interface

## Summary

The study's own gap analysis states plainly: "not all relevant devices are connected to the diagnostic interface." Additionally, low-level hardware debug interfaces (e.g., JTAG) that might exist on specific ECUs could not even be confirmed present or absent without performing separate hardware forensic techniques, since the OBD/DoIP/UDS acquisition path alone provides no visibility into them.

## Why It Matters

An investigator relying solely on OBD-based diagnostic acquisition may conclude that no manipulation occurred (as in the paper's own worked example) while remaining unable to rule out manipulation of components genuinely outside the diagnostic bus's reach — the negative result is only as complete as the diagnostic interface's actual coverage of the vehicle's components, which is not total. This gap is structural to the OBD/UDS/DoIP acquisition approach itself, not a flaw in how it was executed.

## Related Mitigations

- [[mitigations/Supplement OBD-UDS acquisition with embedded hardware forensics for components off the diagnostic bus]]

## Used By

- [[techniques/UDS-DoIP vehicle ECU diagnostic acquisition and manipulation-indicator analysis]]

## References

- [DFCite-1021] Gomez Buquerin et al., 2021, "A generalized approach to automotive forensics", FSI: Digital Investigation 36.
