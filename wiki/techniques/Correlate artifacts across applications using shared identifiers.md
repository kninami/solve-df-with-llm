---
id: DFT-1011
type: technique
name: Correlate artifacts across applications using shared identifiers
description: Correlate shared identifiers (file IDs, folder IDs, account/session IDs, or similar keys) across the local databases of multiple applications that synchronize through a common cloud account or backend, to reconstruct user activity that no single application's own artifacts fully capture.
objective_ids:
  - DFO-1001
weakness_ids:
  - DFW-1012
aliases:
  - Cross-application artifact correlation via shared identifiers
  - Cross-application Google Drive artifact linking
source_refs:
  - DFCite-1006
updated_at: 2026-08-09
status: complete
---

# Correlate artifacts across applications using shared identifiers

## Summary

Where several applications share data through a common account (e.g., 25 Google applications synchronizing through Google Drive), identifiers such as file IDs, folder IDs, and server-assigned permission IDs recur across each app's local SQLite/plist databases. Matching these identifiers across app databases lets an examiner trace a single user action (e.g., downloading a file in a browser and saving it to cloud storage) that would otherwise be invisible from any one application's artifacts alone.

## Details

Each linked pair of applications is joined through a specific identifier: a browser's "saved to Drive" folder ID matches against Drive's own folder IDs; a mail client's attachment permission ID matches Drive's file-sharing identifier; a document editor's document ID cross-references Drive's item table; and calendar/classroom/chat applications reference Drive, Docs, or video-call URLs through their own event or session records. A purpose-built analysis tool can automate this correlation across identified SQLite, plist, and Protobuf sources and present connected results through a unified interface, generalizing beyond any single application family.

## Examples

- Determining whether a file found in Google Drive originated from a Chrome download by matching the "Saved from Chrome" folder ID against Chrome's own download records.
- Confirming that an email attachment in Gmail is the same file as one stored in Google Drive by matching shared permission/file identifiers.

## Related Objectives

- `DFO-1001` Reconstruct events

## Related Weaknesses

- [[weaknesses/Google file-sharing activity untraceable within a single app's own artifacts]]

## References

- [DFCite-1006] Park et al., 2025, "A comprehensive artifact analysis of Google applications on Android and iOS platforms", FSI: Digital Investigation 55.
