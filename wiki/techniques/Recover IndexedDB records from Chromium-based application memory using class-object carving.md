---
id: DFT-1268
type: technique
name: Recover IndexedDB records from Chromium-based application memory using class-object carving
description: Extract a Chromium-based browser or desktop application's IndexedDB records (databases, object stores, and their normal/deleted/modified key-value data) directly from a process memory dump by carving for the LevelDB backend's stable internal C++ class objects (starting from the least-frequently-changed DBImpl class), validating candidates against known field-type/offset constraints, then reconstructing and deserializing the in-memory MemTable's SkipList structure — recovering data that, in incognito/private mode, exists nowhere on disk at all.
objective_ids:
  - DFO-1011
weakness_ids:
  - DFW-1279
aliases:
  - MIC (Memory analysis of IndexedDB on Chromium)
source_refs:
  - DFCite-1307
updated_at: 2026-08-14
status: complete
---

# Recover IndexedDB records from Chromium-based application memory using class-object carving

## Summary

Chromium-based browsers (Chrome, Edge) and Chromium-embedding desktop applications (e.g. Microsoft Teams via WebView2) use IndexedDB, backed by Google's LevelDB key-value store, to hold structured web-service data such as chat logs, contacts, and file lists; when a Chromium-based browser runs in incognito/private mode, this data is held only in volatile memory and is never written to disk, so recovering it forensically requires locating and reconstructing LevelDB's own internal C++ objects directly from a memory dump rather than parsing an on-disk `.ldb` file.

## Details

Because LevelDB's own wrapper classes update frequently across Chromium releases while its lower-level implementation classes remain comparatively stable, carving begins from the `DBImpl` class (chosen for its low update frequency) using its known fixed size for eight-byte-aligned candidate scanning, then validates each candidate by checking that its member fields' data types match their expected type/offset layout (e.g. the nested `Options` class's `create_if_missing`/`error_if_exists` booleans, `block_size` integer, and `dbname_` string fields) — invalid candidates are discarded and the scan continues. Once validated, the `MemTable`'s in-memory `SkipList` (a multi-level linked-list structure LevelDB uses for fast key-ordered lookup and insertion) is walked node-by-node across every level, starting from a header block's list of per-level next-node pointers, to extract every stored key-value record — each of which carries a key, sequence number (used to determine the most recent version if a key was modified more than once), and a "live" or "deleted" state marker. Because IndexedDB itself layers reserved key-prefix conventions and a V8-object-serialized value format on top of LevelDB's raw key-value pairs, the recovered records are further decoded (deserializing the IDBKey-prefixed metadata and V8-serialized values) and classified by which database and object store they belong to, then normalized into a queryable integrated schema.

## Examples

- Across four experiments (Chrome database/object-store metadata creation, Chrome message insertion-then-modification, Edge Telegram-web-app incognito-mode browsing, and a Microsoft Teams desktop-app conversation), the proof-of-concept tool correctly identified 100% of database and object-store metadata records and successfully extracted normal, deleted, and modified IndexedDB records, including both the original and modified versions of records changed after insertion (distinguished by their sequence numbers).
- In Microsoft Edge's incognito mode, the technique successfully extracted a full Telegram web-app conversation (one channel, two dialogs, and three users) directly from memory, despite incognito mode's guarantee that no corresponding data would be written to disk — directly relevant to investigating a suspect's use of incognito mode to avoid leaving a local browsing trace.
- Applied to Microsoft Teams (a Chromium-WebView2-based desktop application, not a browser), the technique recovered 7 of 8 sent chat messages directly from the application's process memory, along with sender display name, timestamp, and message content, demonstrating the methodology generalizes beyond web browsers to any Chromium-embedding application.

## Related Objectives

- `DFO-1011` Extract artifacts stored by applications

## Related Weaknesses

- [[weaknesses/Chromium IndexedDB memory carving cannot parse partial BLOB-stored records in incognito mode]]

## References

- [DFCite-1307] Jeong, Lee and Park, 2024, "MIC: Memory analysis of IndexedDB data on Chromium-based applications", DFRWS 2024 APAC; FSI: Digital Investigation 50, 301809.
