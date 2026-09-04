---
id: LWW-1227
type: weakness
name: Fault-assisted eMMC access restoration produces byte-level divergence that invalidates hash-equality verification
description: A voltage-fault-injection-restored eMMC extraction can complete without error yet still differ from a nominal acquisition at the byte level, invalidating SHA-256 hash-equality verification, while the same fault-injection parameter range that restores access can also drive the component to complete, irreversible failure before extraction finishes.
categories:
  - ASTM_INAC_COR
  - ASTM_INAC_ALT
mitigation_ids:
  - LWM-1227
source_refs:
  - LWCite-1238
updated_at: 2026-08-13
status: complete
---

# Fault-assisted eMMC access restoration produces byte-level divergence that invalidates hash-equality verification

## Summary

Across ten CMD42-locked eMMC references, crowbar voltage fault injection produced fault-induced access restoration on 5/10 and complete extraction on 3/10, but two of the ten sustained irreversible damage before extraction completed, and the single completed post-unlock acquisition retained for integrity analysis showed a measurable ~0.1% (≈2.3 MB over 1824 MB) byte-level divergence from a nominal reference image acquired via a genuine password unlock, with the divergent bytes spatially concentrated rather than uniformly distributed.

## Why It Matters

A fault-assisted extraction that completes without an interface-level error can look forensically indistinguishable from a nominal acquisition unless it is explicitly compared byte-for-byte against a baseline, yet the underlying perturbation that restored access operated in the same narrow parameter corridor that also produced complete, irreversible component failure on other references — meaning "the extraction finished" is not evidence that the process left the data unaltered. Treating a fault-assisted image as equivalent to a standard acquisition without this qualification risks presenting altered or corrupted data as an authentic representation of the device's original contents, and the destructive-failure risk means the technique can also consume the only copy of the evidence before any image is obtained at all.

## Related Mitigations

- [[mitigations/Qualify fault-assisted eMMC extraction integrity with byte-level comparison and log every injection parameter and outcome]]

## Used By

- [[techniques/Bypass a mobile device lock using vulnerability exploitation]]

## References

- [LWCite-1238] Hugget et al., 2026, "Forensic qualification of fault-assisted access restoration on CMD42-locked eMMC: A case study", FSI: Digital Investigation 57, 302109.
