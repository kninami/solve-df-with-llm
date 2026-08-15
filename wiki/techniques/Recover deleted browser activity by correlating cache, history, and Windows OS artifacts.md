---
id: DFT-2054
type: technique
name: Recover deleted browser activity by correlating cache, history, and Windows OS artifacts
description: The process of recovering a user's deleted Chromium-based browser activity (deleted bookmarks, history entries, downloaded-file records) when the browser's own History SQLite database cannot yield the deleted rows directly, by correlating the browser's Cache and Media History artifacts with wider Windows operating-system artifacts (Windows Search/Desktop Search ESE database, Prefetch, Alternate Data Streams, and Windows System Resource Usage Monitor/SRUM) that independently retain full or partial copies of the same activity.
objective_ids:
  - DFO-1011
weakness_ids:
  - DFW-2054
aliases:
  - Chromium browser cross-artifact correlation (Brave/Chrome)
source_refs:
  - DFCite-2055
updated_at: 2026-08-14
status: partial
---

# Recover deleted browser activity by correlating cache, history, and Windows OS artifacts

## Summary

Chromium-based browsers (Brave, Google Chrome, and any browser built on the same open-source base) store live browsing activity in well-documented locations - a History SQLite database for typed URLs, search terms, and file downloads; a Cache for locally-saved copies of visited web pages and images; Cookies, Bookmarks, and Media History in their own structured files. When a user deletes entries from this history, the deletion is often not directly recoverable from the History database itself, so an investigator instead reconstructs the deleted activity by correlating the browser's own Cache with independent, browser-external Windows OS artifacts that happen to retain overlapping records of the same events.

## Details

DFCite-2055 demonstrates this cross-artifact correlation concretely: starting from a downloaded image file recovered from the Downloads folder (DogLeft.png), the investigator locates its Alternative Data Stream (revealing the download's host URL, not stored in the History database itself), its entry in the Windows Desktop Search ESE database (revealing file metadata and timestamps), its Windows Prefetch entry (confirming when it was opened), and - most significantly - its full deleted download record recovered intact from `SRUDB.dat` (the Windows System Resource Usage Monitor ESE database at `C:\Windows\System32\sru`), which independently logs desktop application activity including GUID, URL, referrer URL, download timestamps, byte counts, and file path. Even where a full record cannot be recovered, partial metadata recoverable from a browser-internal log file (e.g. Chromium's `shared_proto_db` log) or from unallocated space/pagefile.sys can corroborate that the activity occurred and roughly when, sufficient to establish a timeline even without the primary database's cooperation.

## Examples

- DFCite-2055's DogLeft.png case: the deleted download's row (row ID 2) could not be recovered from the History database itself, but was fully recovered - GUID, URL, referrer URL, timestamps, byte counts, download path - from `SRUDB.dat` for the Chrome VM, and from a `shared_proto_db` log file (partial: GUID, URL, referrer URL, timestamp, MIME type, download path) for the Brave VM.
- Cache-based website reconstruction: both browsers' Cache stores allowed full reconstruction of a visited webpage's locally-saved copy (e.g. just-eat.co.uk) even after the corresponding History entry was deleted, since Cache data blocks/files are independent of the History database.

## Related Objectives

- `DFO-1011` Extract artifacts stored by applications

## Related Weaknesses

- [[weaknesses/Deleted Chromium History SQLite records are zeroed out and unrecoverable through database carving alone]]

## References

- [DFCite-2055] Berham and Morris, "A critical comparison of Brave Browser and Google Chrome forensic artefacts", Journal of Digital Forensics, Security and Law, 2022 — source of the cross-artifact correlation methodology and the DogLeft.png case example described above.
