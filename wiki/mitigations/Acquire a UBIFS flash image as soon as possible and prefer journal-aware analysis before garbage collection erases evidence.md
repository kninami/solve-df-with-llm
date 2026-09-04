---
id: LWM-2108
type: mitigation
name: Acquire a UBIFS flash image as soon as possible and prefer journal-aware analysis before garbage collection erases evidence
source_refs:
  - LWCite-2126
updated_at: 2026-08-16
status: complete
---

# Acquire a UBIFS flash image as soon as possible and prefer journal-aware analysis before garbage collection erases evidence

## Summary

Prioritize timely acquisition of a UBIFS-based embedded device's flash image to minimize the window in which the garbage collector can erase freeable blocks holding recoverable deleted-file content, and use a journal-aware analysis tool rather than one that only traverses the committed B+-tree index.

## Addresses

- [[weaknesses/UBIFS deleted-file recovery becomes permanently impossible once the garbage collector erases freeable blocks]]

## How To Apply

Treat an embedded or IoT device suspected to use UBIFS (routers, cameras, drones, OpenWRT-based systems, and similar devices) with the same time-sensitivity generally reserved for volatile memory: acquire a full flash image as soon as practical after seizure, since continued device operation increases the chance the garbage collector reclaims blocks holding deleted-file remnants. Once acquired, analyze the image with [[techniques/Recover deleted files from UBIFS flash file systems using journal-based scanning]] rather than a tool that only parses the committed file-index, since journal-buffered deletions not yet folded into the index can still be recovered from the journal directly even after deletion, provided garbage collection has not already reclaimed the relevant blocks. Where multiple candidate tools are available, prefer one confirmed to support journal-aware scanning, since testing has shown some existing UBI/UBIFS tools miss forensically significant data the journal alone contains.

## References

- [LWCite-2126] Deutschmann and Baier, 2024, "Ubi est indicium? On forensic analysis of the UBI file system", FSI: Digital Investigation 48, 301689.
