---
id: DFW-1279
type: weakness
name: Chromium IndexedDB memory carving cannot parse partial BLOB-stored records in incognito mode
description: When a Chromium-based browser runs in incognito mode, LevelDB manages some IndexedDB data as partial BLOB (binary large object) fragments in memory rather than as complete, directly deserializable records, and the class-object-carving-and-SkipList-walking methodology does not address this fragmented BLOB storage case, leaving that subset of incognito-mode data unrecovered even when the rest of the IndexedDB record structure is successfully extracted.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1280
source_refs:
  - DFCite-1307
updated_at: 2026-08-14
status: complete
---

# Chromium IndexedDB memory carving cannot parse partial BLOB-stored records in incognito mode

## Summary

The underlying study's own authors state directly: "our methodology has limitations. When the browser in incognito mode, LevelDB manages partial data in BLOB, and the proposed method does not address this issue," identifying it as an explicit gap in an otherwise validated and high-accuracy (near-100% in most tested experiments) methodology.

## Why It Matters

An investigator applying this technique to a Chromium-based browser's incognito-mode memory may recover the majority of IndexedDB records successfully while silently missing the subset of data LevelDB happened to store as partial BLOB fragments during that session, without the tool providing any indication that a category of potentially relevant data (which could include large object data such as images, files, or extended text content) was excluded from the recovered result. This risks an investigator treating the recovered record set as complete when it is not, particularly since the extraction tool's own reported accuracy figures do not account for this specific gap.

## Related Mitigations

- [[mitigations/Disclose the BLOB-record extraction gap and pursue complementary recovery approaches for Chromium incognito-mode memory]]

## Used By

- [[techniques/Recover IndexedDB records from Chromium-based application memory using class-object carving]]

## References

- [DFCite-1307] Jeong, Lee and Park, 2024, "MIC: Memory analysis of IndexedDB data on Chromium-based applications", DFRWS 2024 APAC; FSI: Digital Investigation 50, 301809.
