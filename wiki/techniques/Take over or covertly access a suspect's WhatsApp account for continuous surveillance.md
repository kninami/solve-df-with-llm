---
id: DFT-1235
type: technique
name: Take over or covertly access a suspect's WhatsApp account for continuous surveillance
description: Gain live, continuous access to a suspect's WhatsApp conversations either by taking over their account using an intercepted SMS/voice verification code, or by covertly pairing a WhatsApp Web session on their unlocked phone, so that messages can be monitored as they arrive rather than only recovered after the fact from a device or backup.
objective_ids:
  - DFO-1006
  - DFO-1016
weakness_ids:
  - DFW-1252
aliases:
  - WhatsApp account takeover via SMS verification interception
  - Covert WhatsApp Web session pairing
source_refs:
  - DFCite-1270
updated_at: 2026-08-14
status: complete
---

# Take over or covertly access a suspect's WhatsApp account for continuous surveillance

## Summary

WhatsApp's own design offers two live-interception vectors distinct from acquiring an already-seized device: registering the suspect's phone number on an investigator-controlled device by intercepting the SMS or voice verification code WhatsApp sends during registration (which logs the suspect out of their own account), or pairing a WhatsApp Web session to the suspect's account while their unlocked phone is briefly accessible (which does not log them out and can persist for weeks unnoticed). Both give an investigator ongoing, real-time visibility into the account's conversations under appropriate legal authority.

## Details

**Account takeover** requires intercepting the six-digit code WhatsApp sends via SMS or an automated voice call when a phone number is newly registered on a device — legally, this typically requires cooperation from a mobile network operator to redirect or duplicate the verification message or call. Once registered on the investigator's device, all subsequent messages route there instead of the suspect's own phone, and existing group memberships and conversation history that WhatsApp itself has not deleted may become visible; however, the suspect's device is simultaneously logged out, which is likely to be noticed. If the suspect has enabled WhatsApp's optional two-step verification (a numeric PIN required in addition to the SMS/voice code), account takeover via this method fails outright.

**WhatsApp Web session pairing** instead requires momentary physical access to the suspect's own unlocked phone: scanning a QR code generated on an investigator-controlled browser or app using the phone's built-in WhatsApp Web scanner links a persistent session that receives a live copy of all messages, without logging the suspect out or requiring the verification code at all. WhatsApp does list active linked sessions and their approximate last-active device/location within its own settings menu, so the technique's persistence depends on the suspect not reviewing that list.

## Examples

- Coordinating with a mobile network operator to intercept an SMS verification code allowed registering a target's phone number on an investigator-controlled device, immediately routing subsequent WhatsApp messages there.
- Scanning a suspect's WhatsApp QR code from their own unlocked phone during a brief opportunistic access window established a linked WhatsApp Web session that continued receiving message copies for an extended period without the suspect logging out or being notified.

## Related Objectives

- `DFO-1006` Acquire data
- `DFO-1016` Overcome protection mechanisms

## Related Weaknesses

- [[weaknesses/Covert WhatsApp account access risks detection through security notifications, and two-step verification blocks SMS-based takeover]]

## References

- [DFCite-1270] van der Meer and Le-Khac, 2026, "Identifying interception possibilities for WhatsApp communication", FSI: Digital Investigation 56, 302070.
