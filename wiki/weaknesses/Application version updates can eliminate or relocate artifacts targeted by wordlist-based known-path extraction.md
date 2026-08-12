---
id: DFW-1072
type: weakness
name: Application version updates can eliminate or relocate artifacts targeted by wordlist-based known-path extraction
description: A wordlist of known filenames and paths built from manually analyzing one version of a mobile application can become substantially wrong after the application is updated, since an update can move, rename, or entirely remove the artifacts the wordlist targets, causing an automated extraction run against a newer version to silently recover little or none of the previously-available evidence.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1072
source_refs:
  - DFCite-1062
updated_at: 2026-08-10
status: complete
---

# Application version updates can eliminate or relocate artifacts targeted by wordlist-based known-path extraction

## Summary

During testing, the authors observed this directly for one of the nine applications studied: preliminary testing of an earlier version of Parler recovered media posted by the account owner, cached media, and a `cache.json` file with user activity/account information, but "little to no data was recovered from the newer version of the application which was updated when the application returned to the Apple store" — the same wordlist-based extraction approach that worked before the update recovered almost nothing afterward.

## Why It Matters

An investigator running a wordlist-based extraction tool against a device with an application version the wordlist was not built or validated against risks a false negative that looks like "the application stores nothing forensically relevant" but is actually "the wordlist no longer matches this version's file layout" — a distinction that matters significantly for how the absence of expected evidence should be interpreted and reported.

## Related Mitigations

- [[mitigations/Validate and update application wordlists per app version before relying on known-path extraction results]]

## Used By

- [[techniques/Discover and extract mobile application artifact locations]]

## References

- [DFCite-1062] Johnson et al., 2022, "Alt-tech social forensics: Forensic analysis of alternative social networking applications", FSI: Digital Investigation 42.
