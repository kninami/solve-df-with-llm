---
id: DFM-1030
type: mitigation
name: Supplement OBD-UDS acquisition with embedded hardware forensics for components off the diagnostic bus
source_refs:
  - DFCite-1021
updated_at: 2026-08-09
status: complete
---

# Supplement OBD-UDS acquisition with embedded hardware forensics for components off the diagnostic bus

## Summary

Treat OBD/UDS/DoIP diagnostic acquisition as covering only the subset of in-vehicle components wired to the diagnostic bus, and use embedded/hardware forensic techniques for any component of investigative interest that is confirmed or suspected to sit outside that reach.

## Addresses

- [[weaknesses/OBD-based diagnostic acquisition cannot reach in-vehicle components not connected to the diagnostic interface]]

## How To Apply

During the forensic readiness phase, explicitly document which in-vehicle components are and are not reachable via the diagnostic interface for the target vehicle's architecture, rather than assuming the diagnostic bus provides full coverage. For components confirmed outside that reach — or where hardware debug interfaces like JTAG cannot be confirmed absent without direct inspection — apply non-destructive [[techniques/Extract eMMC storage using in-system programming]] where feasible, or destructive [[techniques/Extract flash chip contents using X-ray-guided chip-off]] where ISP access is unavailable, following the same preference-order documented for those techniques.

## References

- [DFCite-1021] Gomez Buquerin et al., 2021, "A generalized approach to automotive forensics", FSI: Digital Investigation 36.
