---
id: LWM-2054
type: mitigation
name: Correlate Cache and Windows OS artifacts when a Chromium browser's History database yields no deleted-record recovery
source_refs:
  - LWCite-2055
updated_at: 2026-08-14
status: partial
---

# Correlate Cache and Windows OS artifacts when a Chromium browser's History database yields no deleted-record recovery

## Summary

When carving and keyword searching the History SQLite database fails to recover a suspected deleted browsing/search/download entry, do not conclude the evidence is lost; systematically check the browser's own Cache and Media History artifacts alongside wider Windows OS artifacts (Windows Search ESE database, Prefetch, Alternate Data Streams, and SRUDB.dat/SRUM) for corroborating or fully recoverable records of the same activity.

## Addresses

- [[weaknesses/Deleted Chromium History SQLite records are zeroed out and unrecoverable through database carving alone]]

## How To Apply

Follow a structured cross-artifact search: use any known filename, URL, or search term as a starting keyword and search across the full disk image, not just the History database, to surface hits in Cache, browser internal logs (e.g. `shared_proto_db`), Alternate Data Streams, Windows Desktop Search, Prefetch, and pagefile.sys/free space. Prioritize checking `SRUDB.dat` (Windows System Resource Usage Monitor) specifically for downloaded-file and application-activity records, since this artifact was found capable of yielding a complete deleted download record independent of the browser database. Corroborate partial hits across multiple artifact sources to build a defensible timeline even when no single artifact alone provides a full record.

## References

- [LWCite-2055] Berham and Morris, 2022 — Section 4.5 and Figure 3/4 document the full cross-artifact recovery of the deleted DogLeft.png download record from SRUDB.dat and the partial recovery from browser-internal log files.
