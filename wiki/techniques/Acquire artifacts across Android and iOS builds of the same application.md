---
id: DFT-1012
type: technique
name: Acquire artifacts across Android and iOS builds of the same application
description: Acquire and analyze the same cloud-synchronized application on both its Android and iOS builds when both are available, since each OS variant retains a different subset of Google Account Information, Device Information, Attachment, and User Activity History artifacts for the same underlying account.
objective_ids:
  - DFO-1011
weakness_ids:
  - DFW-1011
aliases:
  - Cross-platform Android-iOS artifact acquisition
source_refs:
  - DFCite-1006
updated_at: 2026-08-09
status: complete
---

# Acquire artifacts across Android and iOS builds of the same application

## Summary

Across 25 examined Google applications, single-OS analysis acquired only 94/175 (Android, ~61%) or 101/175 (iOS, ~65%) of the seven artifact-category-by-application combinations catalogued in the study, but combining both platforms' recoverable artifacts raised the integrated acquisition rate to 109/175 (71%), including 34 artifact combinations unique to the cross-platform analysis and unobtainable from either OS alone.

## Details

Artifact availability differs by category and platform: Android retained more account-identification data overall, while iOS retained more device-information and broader user-activity-history detail, including tab history and profile details not present on Android. For example, Google Keep on iOS provided only basic saved-content and cache artifacts, while its Android counterpart yielded richer account-created-note revision history and internal app behavior. Because the artifact differences are systematic rather than random, examining only one platform's build of a synced application understates the total forensically relevant evidence recoverable for that user account.

## Examples

- Google Chat's `dynamite.db` is identical in structure and content on Android and iOS, but Android additionally exposes `/cache/voice_messages` and `/files/Pictures` as separate artifact paths not itemized the same way on iOS.

## Related Objectives

- `DFO-1011` Extract artifacts stored by applications

## Related Weaknesses

- [[weaknesses/Single-platform Google app analysis misses artifacts only present on the other OS]]

## References

- [DFCite-1006] Park et al., 2025, "A comprehensive artifact analysis of Google applications on Android and iOS platforms", FSI: Digital Investigation 55.
