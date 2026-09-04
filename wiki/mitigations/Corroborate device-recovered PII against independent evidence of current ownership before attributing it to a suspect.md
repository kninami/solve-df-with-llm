---
id: LWM-2055
type: mitigation
name: Corroborate device-recovered PII against independent evidence of current ownership before attributing it to a suspect
source_refs:
  - LWCite-2056
updated_at: 2026-08-14
status: partial
---

# Corroborate device-recovered PII against independent evidence of current ownership before attributing it to a suspect

## Summary

Before attributing PII recovered from a mobile device to its current possessor, independently corroborate current ownership (purchase records, active account logins, recent activity timestamps, physical possession context) rather than assuming that any recoverable identity information reflects the device's present user.

## Addresses

- [[weaknesses/PII recovered from a used mobile device may belong to a previous owner rather than the current possessor]]

## How To Apply

Check for indicators the device may have changed hands: multiple distinct identity profiles present, activity timestamps that stop abruptly and do not continue up to the seizure/acquisition date, factory-reset artifacts followed by minimal new activity, or accounts/apps that do not match the current possessor's known identity. Where a device shows signs of prior ownership, treat older recovered PII as historical rather than attributing it to the current suspect, and prioritize the most recent, actively-used account and activity data as the more reliable indicator of current possession.

## References

- [LWCite-2056] Angelopoulou et al., 2022 — several of the study's case examples (Section 6) show clearly dated prior-owner activity (e.g. calls and photos from 2010-2013, or 2015-2018) that a subsequent possessor's own activity could be mistakenly conflated with without careful timeline review.
