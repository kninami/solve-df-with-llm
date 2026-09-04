---
id: LWW-1043
type: weakness
name: Static or low-movement surveillance footage produces colliding on-camera DCT fingerprints
description: Two frames or entire clips of the same static or near-static scene, captured at different times with no meaningful movement or change, produce identical or near-identical DCT DC-coefficient fingerprints, making it impossible for the correlation-based identification method to distinguish which specific time period a given clip actually corresponds to.
categories:
  - ASTM_INAC_AS
mitigation_ids:
  - LWM-1043
source_refs:
  - LWCite-1033
updated_at: 2026-08-09
status: complete
---

# Static or low-movement surveillance footage produces colliding on-camera DCT fingerprints

## Summary

The authors state plainly: "It is clear that two frames, or even clips, of the same scene at different times with no movement or change would produce the same DCT transform information. There will be high levels of collision within the DCT information stored in the database. Whether or not this is problematic is entirely dependent on the real-world application. For example, a fixed CCTV camera in a sterile corridor environment may produce mostly identical imagery."

## Why It Matters

If a query clip's fingerprint collides with multiple stored blockchain entries from different actual capture times, the identification stage cannot determine which entry genuinely corresponds to the clip in question — the system could return a technically valid match to the wrong time period without any indication of ambiguity to the investigator. This misattribution risk is highest precisely in the low-activity, "nothing happened" scenes that might later become forensically relevant if something unusual is later found to have occurred just outside the collision window.

## Related Mitigations

- [[mitigations/Add an on-screen timestamp signal for low-movement scenes to prevent fingerprint collision]]

## Used By

- [[techniques/Anchor digital evidence integrity and chain of custody on a blockchain]]

## References

- [LWCite-1033] Kerr et al., 2023, "A non-invasive method for the cataloguing and authentication of surveillance video using on-camera blockchain participation, machine learning and signal analysis", FSI: Digital Investigation 46.
