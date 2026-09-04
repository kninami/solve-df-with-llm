---
id: LWW-1180
type: weakness
name: Memory-carved JSON reconstruction fails to recover structures overwritten in their middle
description: The reconstruction algorithm used to repair partially overwritten JSON telemetry structures carved from memory only handles truncation at the start or end of the structure, so a structure that is intact at both ends but overwritten somewhere in its middle cannot be recovered.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-1180
source_refs:
  - LWCite-1182
updated_at: 2026-08-12
status: complete
---

# Memory-carved JSON reconstruction fails to recover structures overwritten in their middle

## Summary

The authors state this directly as a scope limitation of the `usbhunt` reconstruction algorithm: "this work does not cover the cases in which the data was intact at the beginning and end but overwritten in the middle." As physical memory pages are reallocated and overwritten over time by normal system activity, a JSON telemetry structure can be damaged in any pattern, not only at its edges, and the current reconstruction logic only addresses the edge-truncation case.

## Why It Matters

An investigator who fails to find a usable device-identification structure via memory carving should not conclude that no evidence of USB attack platform usage exists; the underlying structure may still be present in memory but damaged in a pattern the current reconstruction algorithm cannot repair, meaning a negative result from this technique alone does not establish the artifact's absence.

## Related Mitigations

- [[mitigations/Cross-validate partially overwritten memory-carved JSON structures against redundant registry or event-log copies]]

## Used By

- [[techniques/Detect USB attack platform usage from memory-resident diagnostic telemetry and DHCP artifacts]]

## References

- [LWCite-1182] Thomas et al., 2021, "Duck Hunt: Memory forensics of USB attack platforms", FSI: Digital Investigation 37. States that the reconstruction algorithm does not cover JSON structures overwritten in the middle while intact at the beginning and end.
