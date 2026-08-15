---
id: DFW-1254
type: weakness
name: WhatsApp privacy settings can hide profile photo, About text, and last-seen from non-contacts, limiting OSINT visibility
description: A target who has restricted their WhatsApp profile photo, About text, or last-seen visibility below "Everyone" will not expose that information to an investigator's contact-list-based OSINT probe, so the technique's yield depends entirely on a privacy configuration the investigator cannot observe or control in advance.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1255
source_refs:
  - DFCite-1270
updated_at: 2026-08-14
status: complete
---

# WhatsApp privacy settings can hide profile photo, About text, and last-seen from non-contacts, limiting OSINT visibility

## Summary

WhatsApp lets each user independently restrict who can see their profile photo, About text, and last-seen/online status to "Everyone," "My Contacts," "My Contacts Except…," or "Nobody"; a target using any setting narrower than "Everyone" will not display that information to an investigator's device merely because the investigator added the target's number as a contact, since visibility depends on the target's own contact-list configuration, not the investigator's.

## Why It Matters

Because the investigator cannot inspect a target's privacy settings in advance, a failed attempt to harvest profile OSINT this way is indistinguishable from a target who genuinely has no profile picture or About text set — the investigator has no signal to distinguish "hidden by privacy setting" from "not present," which can lead to an incomplete open-source profile without the investigator realizing information may exist but be inaccessible through this passive method.

## Related Mitigations

- [[mitigations/Accept the alerting risk of an active WhatsApp OSINT probe only when passive contact-list observation is insufficient and legally justified]]

## Used By

- [[techniques/Harvest WhatsApp profile OSINT by adding a target's number to a contact list]]

## References

- [DFCite-1270] van der Meer and Le-Khac, 2026, "Identifying interception possibilities for WhatsApp communication", FSI: Digital Investigation 56, 302070.
