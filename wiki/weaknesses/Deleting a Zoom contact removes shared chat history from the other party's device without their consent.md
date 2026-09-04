---
id: LWW-2137
type: weakness
name: Deleting a Zoom contact removes shared chat history from the other party's device without their consent
description: When one Zoom user removes another user from their contact list, the shared chat interface, and on some platforms the underlying chat and contact databases, are also cleared on the other (non-deleting) party's device the next time it connects, destroying that party's copy of the shared evidence without their knowledge or permission.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-2138
source_refs:
  - LWCite-2158
updated_at: 2026-08-17
status: complete
---

# Deleting a Zoom contact removes shared chat history from the other party's device without their consent

## Summary

Testing contact deletion across Android, iOS, macOS, and Windows found that when a user deletes a contact, the effect is not confined to the deleting user's own device: on the removed contact's own device, the chat interface and, on Android and macOS specifically, the underlying chat/contact databases and files are also cleared, even though that user never deleted anything themselves and has no way to prevent or detect it happening. The Android device's underlying data was found to repopulate from the server the next time the app was reopened, but macOS's database-level deletion persisted, and neither device's user consented to or was notified of the removal.

## Why It Matters

An investigator relying on the Zoom application data of the party who did not initiate the deletion could still find that their evidence of the prior contact relationship, shared chat history, or exchanged files has been unilaterally erased by an action taken entirely on someone else's device, with no local record of why. Because this can happen without any wrongdoing or anti-forensic intent by the affected user, and without any visible warning in the application interface, it functions as an unintentional but real vector for critical evidence to disappear from a device before it is ever collected.

## Related Mitigations

- [[mitigations/Acquire Zoom evidence promptly from all involved devices before a contact deletion can propagate]]

## Used By

- [[techniques/Extract Zoom video-conferencing artifacts across disk, network, and memory using JID-keyed database analysis]]

## References

- [LWCite-2158] Mahr et al., 2021, "Zooming into the pandemic! A forensic analysis of the Zoom Application", FSI: Digital Investigation 36.
