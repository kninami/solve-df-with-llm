---
id: DFW-1012
type: weakness
name: Google file-sharing activity untraceable within a single app's own artifacts
description: When a file moves between Google applications (e.g., downloaded via Chrome and saved to Drive, or attached to a Gmail message from Drive), the receiving or sending application's own database does not record the cross-application provenance, so relying on any one app's artifacts in isolation misrepresents how the file reached the user.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1012
source_refs:
  - DFCite-1006
updated_at: 2026-08-09
status: complete
---

# Google file-sharing activity untraceable within a single app's own artifacts

## Summary

Files saved from Chrome to Google Drive are placed in an automatically created "Saved from Chrome" folder, but this provenance is not recorded in Chrome's own artifacts -- it must be identified by comparing the folder ID in Drive's `cello.db` against records obtained from Chrome. The same applies to file attachments shared between Gmail and Drive, files attached in Google Chat, and files linked into Google Classroom or Calendar events: each application records only its own side of the interaction.

## Why It Matters

An examiner working from a single application's artifact set risks concluding a file was created or first appeared within that application, when it actually originated elsewhere -- misattributing the sequence of user actions in an investigation timeline. This weakness is structural (built into how the applications separately log their own activity) rather than a bug in any one tool, so it recurs across every pairwise combination of Google applications sharing files through Drive.

## Related Mitigations

- [[mitigations/Cross-reference File IDs and folder IDs across linked Google application databases]]

## Used By

- [[techniques/Cross-application artifact correlation via shared identifiers]]

## References

- [DFCite-1006] Park et al., 2025, "A comprehensive artifact analysis of Google applications on Android and iOS platforms", FSI: Digital Investigation 55.
