---
id: DFW-1003
type: weakness
name: Visual ID facial recognition metadata is unavailable from provider cloud services
description: Amazon processes and stores Visual ID facial-recognition vectors and presence logs entirely on-device, so this content information cannot be obtained from Amazon's cloud infrastructure via legal process and is recoverable only by seizing and imaging the physical device.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1003
source_refs:
  - DFCite-1002
updated_at: 2026-08-09
status: complete
---

# Visual ID facial recognition metadata is unavailable from provider cloud services

## Summary

Amazon's Echo Show devices compute facial detection/recognition locally using on-device Neural Edge processing and never transmit the facial feature vectors or presence logs to the cloud. Amazon classifies this as "content information," which the company can lawfully decline to produce because it states it simply does not possess the data, rather than because a request was overbroad.

## Why It Matters

Investigators who submit a subpoena or search warrant to Amazon's cloud services expecting Visual ID evidence will find that data is not held there at all -- 99% of Amazon's processed law-enforcement requests in its transparency report involved only non-content subscriber information. If the physical IoT device at the scene is not identified, seized, and forensically imaged, this potentially case-critical presence evidence (e.g., last confirmed recognition of a victim or suspect) is permanently lost to the investigation.

## Related Mitigations

- [[mitigations/Seize and image local IoT device storage instead of relying on cloud legal process]]

## Used By

- [[techniques/In-system programming eMMC extraction]]

## References

- [DFCite-1002] Lorenz et al., 2026, "A case study on the use of Amazon visual ID facial recognition metadata in investigation", FSI: Digital Investigation 57.
