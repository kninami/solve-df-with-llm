---
id: LWM-2138
type: mitigation
name: Acquire Zoom evidence promptly from all involved devices before a contact deletion can propagate
source_refs:
  - LWCite-2158
updated_at: 2026-08-17
status: complete
---

# Acquire Zoom evidence promptly from all involved devices before a contact deletion can propagate

## Summary

Prioritize acquisition of Zoom application data from every device involved in a relevant contact relationship or chat as early as possible in an investigation, since a contact deletion performed by any one party can silently clear the corresponding chat interface and, on some platforms, the underlying local databases on the other party's device the next time it connects, without either party's awareness.

## Addresses

- [[weaknesses/Deleting a Zoom contact removes shared chat history from the other party's device without their consent]]

## How To Apply

Where a case involves communication between two or more identified Zoom users, seize and forensically acquire all involved devices as close together in time as feasible, rather than sequentially over an extended period during which one party could remove the other as a contact. When only one party's device is available, note explicitly in the examination report that the counterpart's copy of the shared chat/contact data may no longer reflect what was originally present, since it could have been cleared by an action outside the examined device's own control, and cross-reference network-traffic captures or server-side records where available to corroborate what a since-deleted local record originally contained.

## References

- [LWCite-2158] Mahr et al., 2021, "Zooming into the pandemic! A forensic analysis of the Zoom Application", FSI: Digital Investigation 36.
