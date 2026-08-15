---
id: DFT-1237
type: technique
name: Harvest WhatsApp profile OSINT by adding a target's number to a contact list
description: Add a target's phone number as a contact on an investigator-controlled device to surface any WhatsApp profile information (profile picture, "About" status text, last-seen presence) the target's privacy settings expose to their contacts, without requiring any account access or interception.
objective_ids:
  - DFO-1004
  - DFO-1012
weakness_ids:
  - DFW-1254
aliases:
  - WhatsApp contact-list OSINT
source_refs:
  - DFCite-1270
updated_at: 2026-08-14
status: complete
---

# Harvest WhatsApp profile OSINT by adding a target's number to a contact list

## Summary

WhatsApp reveals a user's profile picture, "About" text, and last-seen/online presence to anyone whose contact list includes their number, subject to that user's own privacy settings; simply saving a target's known phone number as a contact on an investigator-controlled device is often enough to passively surface this open-source information, with no message sent and no account access required.

## Details

Because this is a passive, non-interactive technique — the target's device makes no outbound record of being added to someone else's contact list — it carries essentially no risk of alerting the target, unlike account-access or interception techniques. The information available depends entirely on the target's own privacy configuration: a target who restricts profile photo, About text, or last-seen visibility to "My Contacts" (or narrower) will not expose that information to an investigator who is not already in the target's own contact list, regardless of whether the investigator has added the target's number.

## Examples

- Adding a suspect's known phone number to a contact list on an investigation device surfaced their WhatsApp profile picture and About text, corroborating the number's ownership and providing an additional identifying image for the case file.

## Related Objectives

- `DFO-1004` Conduct research
- `DFO-1012` Locate potentially relevant content

## Related Weaknesses

- [[weaknesses/WhatsApp privacy settings can hide profile photo, About text, and last-seen from non-contacts, limiting OSINT visibility]]

## References

- [DFCite-1270] van der Meer and Le-Khac, 2026, "Identifying interception possibilities for WhatsApp communication", FSI: Digital Investigation 56, 302070.
