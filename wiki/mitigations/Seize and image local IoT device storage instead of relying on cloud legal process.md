---
id: LWM-1003
type: mitigation
name: Seize and image local IoT device storage instead of relying on cloud legal process
source_refs:
  - LWCite-1002
updated_at: 2026-08-09
status: complete
---

# Seize and image local IoT device storage instead of relying on cloud legal process

## Summary

Treat cloud-hosted subpoena/warrant responses and physical device seizure as complementary, not interchangeable: for IoT devices whose vendor processes and stores biometric or presence data locally (by design), plan to obtain a search warrant for the physical device itself rather than expecting the manufacturer's cloud service to hold that content.

## Addresses

- [[weaknesses/Visual ID facial recognition metadata is unavailable from provider cloud services]]

## How To Apply

At a scene involving Amazon Echo Show or similar locally-processing smart-display devices, identify and secure the physical hardware immediately, since content information (facial recognition data) will not be available from the vendor's cloud regardless of legal process used. Establish probable cause for seizing the device itself, then use a non-destructive ISP/eMMC extraction procedure to obtain a forensically sound image before conducting analysis, preserving device integrity for potential re-examination.

## References

- [LWCite-1002] Lorenz et al., 2026, "A case study on the use of Amazon visual ID facial recognition metadata in investigation", FSI: Digital Investigation 57.
