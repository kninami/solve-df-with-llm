---
id: DFT-1143
type: technique
name: Identify document data remnants in Windows and Microsoft 365 using differential snapshot analysis
description: Systematically discover application- and OS-generated files that retain data remnants of a deleted or overwritten document by imaging a system before and after a user action, extracting the files that differ between the two snapshots, and classifying each as a studied or previously unstudied data remnants file (DRF).
objective_ids:
  - DFO-1012
weakness_ids:
  - DFW-1146
aliases:
  - Data Remnants File (DRF) framework
  - DRFD/DRFI/DRFA/DRFE framework
source_refs:
  - DFCite-1142
updated_at: 2026-08-12
status: complete
---

# Identify document data remnants in Windows and Microsoft 365 using differential snapshot analysis

## Summary

The Data Remnants File (DRF) framework identifies residual data — a deleted file's name, path, timestamps, size, or content — that persists in system, application, or log files even after the originating document has been deleted or overwritten. It builds a reference dataset by performing a defined set of user actions (create, copy/share, download/upload, open/access, modify) against target applications, imaging the system before and after each action, and using differential analysis (rather than a full disk-wide content search) to isolate the specific files each action changed.

## Details

The framework has four stages: Data Remnants File Dataset creation (DRFD), which installs the target OS/application combination in a VM, performs each user action, and images the disk before and after; Data Remnants File Identification (DRFI), which uses differential analysis to shortlist changed files (reduced to a manageable set via keyword search on filenames/paths/contents, since a full differential pass over an entire disk image is prohibitively slow and noisy); Data Remnants File Analysis (DRFA), which parses each candidate DRF's format and structure and classifies it as a Studied DRF (SDRF, already documented in prior forensic literature, e.g., `$MFT`, `$LogFile`, Jumplists, LNK files) or an Unstudied DRF (UDRF, a previously undocumented artifact whose structure, purpose, and content must be manually reverse-engineered); and Data Remnants File Examination (DRFE), which extracts DRFs from a target disk/image, separates "potential" files (referenced by a DRF) from "existing" files still present on the target, and compares the two lists to identify files that were deleted but leave provable evidence of their prior existence. Applied as a case study to Microsoft 365 (Office, OneDrive, Teams, Outlook, OneNote) on Windows 11, the framework identified several previously unstudied DRFs, including `OfficeFileCache` cache files that record a document's filename, path, size, and content even after the source document is deleted, and `TapCache`/`FileActivityStoreV3` JSON logs that record file access and creation activity synced from OneDrive/SharePoint.

## Examples

- Discovering that the `OfficeFileCache` (`<numeric>.C4`) cache file under `%UserProfile%\AppData\Local\Microsoft\Office\<version>\OfficeFileCache` retains a deleted Office document's filename, full path, and content even after the source file and its normal `$MFT`/`$LogFile` traces have been removed.
- Using differential snapshot comparison (rather than full-disk content search) to isolate the small set of files changed by a single user action such as opening a document via OneDrive on the web.

## Related Objectives

- `DFO-1012` Locate potentially relevant content

## Related Weaknesses

- [[weaknesses/Standard deleted-file recovery misses document data remnants left by Microsoft 365 applications]]

## References

- [DFCite-1142] Joun, Lee and Park, 2023, "Data remnants analysis of document files in Windows: Microsoft 365 as a case study", FSI: Digital Investigation 46.
