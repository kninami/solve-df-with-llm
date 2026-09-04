---
id: LWM-1043
type: mitigation
name: Add an on-screen timestamp signal for low-movement scenes to prevent fingerprint collision
source_refs:
  - LWCite-1033
updated_at: 2026-08-09
status: complete
---

# Add an on-screen timestamp signal for low-movement scenes to prevent fingerprint collision

## Summary

For camera deployments where extended periods of visually static or near-identical footage are expected, add an on-screen timestamp (or other continuously-varying visual signal) to the recorded frames so that every frame's DCT fingerprint remains unique over time, even when the underlying scene content itself does not change.

## Addresses

- [[weaknesses/Static or low-movement surveillance footage produces colliding on-camera DCT fingerprints]]

## How To Apply

In deployments prone to long static periods (e.g., fixed cameras in sterile or low-traffic environments), enable an on-screen timestamp overlay so that every frame's pixel content — and therefore its DCT fingerprint — differs from every other frame, breaking the collision. Where a visible timestamp is undesirable, consider fast indexing operations or other engineered per-frame variation as an alternative mechanism, but note that an unverified/unhashed timestamp alone does not contribute to the integrity-checking mechanism and should be treated purely as a collision-avoidance aid, not an authentication signal in itself.

## References

- [LWCite-1033] Kerr et al., 2023, "A non-invasive method for the cataloguing and authentication of surveillance video using on-camera blockchain participation, machine learning and signal analysis", FSI: Digital Investigation 46.
