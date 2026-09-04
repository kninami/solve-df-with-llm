---
id: LWT-1198
type: technique
name: Roll back a device's clock to prevent ephemeral messages from expiring before extraction
description: Set a seized device's local date/time backward to before a disappearing message's expiry point, exploiting the fact that some apps evaluate message expiry against the device's local clock rather than a server timestamp, to keep the message readable and captureable until extraction can occur.
objective_ids:
  - DFO-1010
weakness_ids:
  - LWW-1207
aliases:
  - "\"Pausing the clock\" to preserve disappearing messages"
source_refs:
  - LWCite-1218
updated_at: 2026-08-13
status: complete
---

# Roll back a device's clock to prevent ephemeral messages from expiring before extraction

## Summary

Where a messaging app's disappearing-message timer is evaluated against the device's own local system clock rather than a live server check, manually setting the device's date/time backward to before the message's expiry point prevents the app from deleting the message, buying time for the message to be viewed, photographed, or extracted before it is lost.

## Details

Testing WhatsApp's disappearing-message feature on a network-isolated (airplane-mode) device confirmed the timer is evaluated locally: rolling the local clock forward past the disappearing date caused the app to sanitize the database on next refresh, while rolling the clock backward to before the original send date preserved 100% of the test data, both pre- and post-nominal-expiry, across both an Android and an iOS test device. This gives an investigator a way to "freeze" or reverse the countdown on a seized device that still has messages pending expiry, provided the device can be kept network-isolated so no external time source overrides the local setting. The technique only works while the app has not already processed the expiry event; once a disappearing message has been sanitized from the local database, rolling the clock back does not restore it.

## Examples

- Rolling an iPhone 6s and a Samsung S6's local date back to the original message-send date, after WhatsApp disappearing messages had already passed their nominal 7-day expiry, resulted in 100% of the test dataset remaining extractable via Cellebrite on both devices — the only test condition in the study where full recovery was achieved.
- Rolling the local date forward instead (to simulate the passage of time faster than real-time) triggered WhatsApp to wipe the disappearing messages from its database once the app was closed and reopened, demonstrating the same local-clock dependency can be used destructively as well as preservatively.

## Related Objectives

- `DFO-1010` Preserve digital evidence

## Related Weaknesses

- [[weaknesses/Rolling back a device's clock to preserve expiring evidence alters the device's original state]]

## References

- [LWCite-1218] Heath et al., 2023, "Forensic analysis of ephemeral messaging applications: Disappearing messages or evidential data?", FSI: Digital Investigation 46.
