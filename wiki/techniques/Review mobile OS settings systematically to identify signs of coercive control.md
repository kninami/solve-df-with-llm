---
id: DFT-1104
type: technique
name: Review mobile OS settings systematically to identify signs of coercive control
description: Systematically inspect a mobile device's proprietary iOS or Android operating-system settings (account/ID, screen-time, family-sharing, notification, lock, and backup configuration) against a documented reference list to identify subtle, non-app-based indicators that a device is being monitored, restricted, or controlled by a perpetrator of technology-facilitated domestic abuse.
objective_ids:
  - DFO-1003
weakness_ids:
  - DFW-1109
aliases:
  - Digital coercive control (DCC) settings review
source_refs:
  - DFCite-1104
updated_at: 2026-08-12
status: complete
---

# Review mobile OS settings systematically to identify signs of coercive control

## Summary

Investigative attention in digital coercive control (DCC) cases has historically centered on identifying third-party stalkerware apps or reviewing communication content for direct threats, but perpetrators can also exert control purely through a device's own built-in operating-system settings — a form of abuse that requires no app installation and can be easy to overlook without deliberate, structured review.

## Details

The technique catalogues 70 named settings across iOS and Android (covering roughly 91% of the mobile OS market between them), each assigned a reference ID, path, and a description of how it could be used to exert control, provide oversight, or restrict a device's operation. Categories include: account/ID details (whether the signed-in account belongs to the victim or a perpetrator, and whether email alerts on account changes could tip off a perpetrator); Screen Time / Digital Balance (app usage limits, downtime scheduling, and content restrictions, several of which are enforceable only via a passcode the user may not control); Family Sharing (location sharing and remote screen-time control by an "organiser" or "parent/guardian" role, which may in fact be a perpetrator's device); notification and lock-screen configuration (whether message previews are visible when locked, and whether Face ID / passcode / Guided Access is disabled in a way that leaves the device open); and backup/account settings (whether device data is being synced to an account the victim does not control). A first responder can use the catalogue during a manual, non-forensic-lab interrogation of a device offered by an alleged victim, without needing to identify a malicious third-party app.

## Examples

- On a test iPhone, the Apple ID's associated devices list (settings ID 13) and Family Sharing membership (ID 41) were checked to determine whether an unfamiliar device or family member could exert location-tracking or Screen-Time-based control over the handset.
- On an Android device, Digital Balance's screen-time management pin (ID 66) was checked to determine whether app-access restrictions were password-locked by someone other than the device's primary user.

## Related Objectives

- `DFO-1003` Review content for relevance

## Related Weaknesses

- [[weaknesses/Device settings indicating parental-control-like restrictions can be misinterpreted as evidence of coercive control]]

## References

- [DFCite-1104] Horsman, 2023, "Can signs of digital coercive control be evidenced in mobile operating system settings? - A guide for first responders", FSI: Digital Investigation 44.
