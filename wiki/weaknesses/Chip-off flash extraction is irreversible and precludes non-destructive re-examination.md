---
id: DFW-1023
type: weakness
name: Chip-off flash extraction is irreversible and precludes non-destructive re-examination
description: Desoldering a flash chip via infrared reflow to perform chip-off extraction permanently alters the device's physical state — the chip cannot be reliably resoldered to a fully original functional condition — foreclosing any later non-destructive re-examination of the device as it existed at seizure.
categories:
  - ASTM_INAC_ALT
mitigation_ids:
  - DFM-1023
source_refs:
  - DFCite-1016
updated_at: 2026-08-09
status: complete
---

# Chip-off flash extraction is irreversible and precludes non-destructive re-examination

## Summary

Chip-off extraction is a destructive procedure by design: the target chip is physically removed via reflow heating and then either reballed onto an adapter or wired pin-by-pin to a reader. Even a technically successful extraction leaves the source device in a functionally altered state, and the process itself carries some risk of fracturing the chip or the board if the thermal or mechanical steps are not executed precisely.

## Why It Matters

Because the alteration is irreversible, any subsequent need to re-examine the device in its original assembled and functional state — whether for a second independent forensic opinion, a different extraction method, or physical/tool-mark evidence — is foreclosed once chip-off has been performed. Unlike non-destructive extraction methods, there is no possibility of restoring the device to allow a defense expert or second examiner to independently repeat the acquisition on the same physical unit in its original configuration.

## Related Mitigations

- [[mitigations/Prefer non-destructive ISP extraction and reserve chip-off for when ISP access is unavailable]]

## Used By

- [[techniques/X-ray guided chip-off flash extraction]]

## References

- [DFCite-1016] Barral et al., 2022, "A forensic analysis of the Google Home: repairing compressed data without error correction", FSI: Digital Investigation 42-43.
