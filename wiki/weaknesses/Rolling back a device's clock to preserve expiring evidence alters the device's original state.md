---
id: DFW-1207
type: weakness
name: Rolling back a device's clock to preserve expiring evidence alters the device's original state
description: Manually changing a seized device's system date/time to prevent a disappearing message from expiring modifies the device's data before acquisition, which conflicts with the principle that no action taken by an investigator should change data held on a device that may subsequently be relied upon as evidence.
categories:
  - ASTM_INAC_ALT
mitigation_ids:
  - DFM-1207
source_refs:
  - DFCite-1218
updated_at: 2026-08-13
status: complete
---

# Rolling back a device's clock to preserve expiring evidence alters the device's original state

## Summary

The clock-rollback technique deliberately writes to the device's system time before any forensic image is captured, which is itself an alteration of the device's state at the point of seizure and breaks the "do not change data" principle that acquisition procedures normally follow, even though the intent is to prevent a greater loss of evidential content.

## Why It Matters

If challenged, an investigator must be able to account for every change made to a device prior to acquisition; an unexplained or undocumented time change discovered later in analysis can undermine confidence in the timeline reconstructed from the device and invite a defense argument that other data may also have been altered. Because the technique trades one integrity risk (message loss) for another (state alteration), it should not be applied routinely or without a documented, case-specific justification.

## Related Mitigations

- [[mitigations/Document and justify device-clock manipulation before using it to preserve expiring evidence]]

## Used By

- [[techniques/Roll back a device's clock to prevent ephemeral messages from expiring before extraction]]

## References

- [DFCite-1218] Heath et al., 2023, "Forensic analysis of ephemeral messaging applications: Disappearing messages or evidential data?", FSI: Digital Investigation 46.
