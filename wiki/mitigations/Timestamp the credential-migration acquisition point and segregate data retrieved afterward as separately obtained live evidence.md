---
id: LWM-1205
type: mitigation
name: Timestamp the credential-migration acquisition point and segregate data retrieved afterward as separately obtained live evidence
source_refs:
  - LWCite-1217
updated_at: 2026-08-13
status: complete
---

# Timestamp the credential-migration acquisition point and segregate data retrieved afterward as separately obtained live evidence

## Summary

Record the exact date/time a migrated credential is first used to access an account, and clearly separate any data retrieved through that migrated session afterward from the data that existed at the point of the original device's seizure, documenting ongoing collection as its own distinct evidentiary episode.

## Addresses

- [[weaknesses/Migrated application credentials can retrieve data generated after the acquisition point, risking misattribution to the original evidence timeframe]]

## How To Apply

Log the precise timestamp of credential migration and the first post-migration login as part of the chain-of-custody record. When reporting content retrieved via the migrated session, check each item's own creation/modification timestamp against the migration timestamp, and label anything created afterward as live, ongoing collection rather than evidence recovered from the original seized device. Where continued collection is not itself an investigative goal, consider disconnecting or invalidating the migrated session promptly after the intended collection to minimize the window in which new, potentially confusing data can accumulate.

## References

- [LWCite-1217] Hur et al., 2023, "Forensic analysis for multi-platform Cisco Webex", FSI: Digital Investigation 47, 301659.
