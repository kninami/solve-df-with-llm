---
id: LWW-1252
type: weakness
name: Covert WhatsApp account access risks detection through security notifications, and two-step verification blocks SMS-based takeover
description: An investigator relying on SMS-verification-code account takeover or WhatsApp Web session pairing for live surveillance can lose access without warning — takeover fails outright if two-step verification is enabled, and a covert Web session remains discoverable at any time through WhatsApp's own linked-devices list.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-1253
source_refs:
  - LWCite-1270
updated_at: 2026-08-14
status: complete
---

# Covert WhatsApp account access risks detection through security notifications, and two-step verification blocks SMS-based takeover

## Summary

WhatsApp surfaces both interception vectors to the account owner by design: taking over an account via an intercepted SMS/voice verification code immediately logs the suspect's own device out, which is very likely to be noticed, and fails entirely if the suspect has enabled the optional two-step verification PIN; a covertly paired WhatsApp Web session does not log the suspect out, but remains permanently visible and revocable from within the suspect's own "Linked Devices" settings menu at any time.

## Why It Matters

An investigation plan that assumes either vector will remain silently available for a planned monitoring period risks abrupt, unannounced loss of access — and worse, tips off the suspect that they are under investigation, potentially prompting evidence destruction or a change in communication channel. Because the level of risk and mode of failure differ by vector (verification-PIN lockout vs. discovery via a settings screen the suspect may never open), the investigator needs distinct contingency planning for each.

## Related Mitigations

- [[mitigations/Time covert WhatsApp account access to minimize detection risk and plan a legal-process contingency for two-step verification]]

## Used By

- [[techniques/Take over or covertly access a suspect's WhatsApp account for continuous surveillance]]

## References

- [LWCite-1270] van der Meer and Le-Khac, 2026, "Identifying interception possibilities for WhatsApp communication", FSI: Digital Investigation 56, 302070.
