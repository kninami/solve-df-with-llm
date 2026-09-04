---
id: LWM-1207
type: mitigation
name: Document and justify device-clock manipulation before using it to preserve expiring evidence
source_refs:
  - LWCite-1218
updated_at: 2026-08-13
status: complete
---

# Document and justify device-clock manipulation before using it to preserve expiring evidence

## Summary

Treat local-clock rollback as a last-resort preservation measure: use it only when non-invasive alternatives (screenshotting, photographing the screen, or an immediate on-scene triage extraction) are not feasible before the message would otherwise expire, and record the justification and exact change made.

## Addresses

- [[weaknesses/Rolling back a device's clock to preserve expiring evidence alters the device's original state]]

## How To Apply

Before changing a device's clock, first attempt to capture the at-risk content through non-invasive means (photograph the on-screen message, or perform an immediate on-scene extraction/RAM capture while the app is open) and only fall back to clock manipulation if those options are unavailable and the message would otherwise be lost before a proper extraction can occur. Log the device's original date/time, the new value set, the exact timestamp of the change, and the reasoning, and note the deviation prominently in the examination report so any downstream analyst or reviewer is aware the device's state was altered prior to acquisition. Where organizational policy allows, obtain sign-off from a second examiner before applying the technique, given it departs from the standard "do not change data" acquisition principle.

## References

- [LWCite-1218] Heath et al., 2023, "Forensic analysis of ephemeral messaging applications: Disappearing messages or evidential data?", FSI: Digital Investigation 46.
