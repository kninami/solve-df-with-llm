---
id: DFW-2126
type: weakness
name: Non-rooted local-data extraction from a stalkerware app fails when its manifest disables Android backup
description: A stalkerware evidence-collection technique that reads an app's local storage via the non-rooted Android application-backup mechanism recovers no data at all when the app's manifest sets allowBackup to false, leaving the investigator without a non-rooted fallback for that app.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-2127
source_refs:
  - DFCite-2148
updated_at: 2026-08-16
status: complete
---

# Non-rooted local-data extraction from a stalkerware app fails when its manifest disables Android backup

## Summary

Android's application-backup functionality lets a connected workstation pull an app's internal storage (databases, cached files, shared preferences) without root privileges, but only if the app's manifest permits it. Because stalkerware developers control this flag like any other app developer, some stalkerware apps explicitly disable backup, and for those apps the non-rooted extraction path recovers nothing regardless of how much identifying data the app actually cached locally.

## Why It Matters

An investigator who relies solely on the non-rooted backup path will conclude, incorrectly, that a backup-disabled stalkerware app stores no useful local evidence, when in practice the same locally cached credentials, tokens, and stolen data may still be present and simply inaccessible without root. In a field or on-scene setting where rooting the device is not immediately feasible, this creates a gap between what evidence exists on the device and what the technique can actually recover, directly reducing the completeness of the abuser-identifying evidence gathered.

## Related Mitigations

- [[mitigations/Root the target device before local-data extraction when a stalkerware app disables Android backup]]

## Used By

- [[techniques/Identify a stalkerware abuser by exploiting insecure local storage and web-dashboard vulnerabilities]]

## References

- [DFCite-2148] Mangeard et al., 2024, "WARNE: A stalkerware evidence collection tool", FSI: Digital Investigation 48.
