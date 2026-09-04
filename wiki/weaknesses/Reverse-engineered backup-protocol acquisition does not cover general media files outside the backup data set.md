---
id: LWW-1057
type: weakness
name: Reverse-engineered backup-protocol acquisition does not cover general media files outside the backup data set
description: A reverse-engineered manufacturer backup protocol reproduces only the specific structured data categories the vendor's own backup feature transmits (contacts, messages, calendar, app data, and similar database-backed items); general media files such as photos and documents typically exist outside this backup data set entirely and are not obtainable through this technique.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-1057
source_refs:
  - LWCite-1047
updated_at: 2026-08-09
status: complete
---

# Reverse-engineered backup-protocol acquisition does not cover general media files outside the backup data set

## Summary

The authors note this directly: "Multimedia files such as documents and photos are not mentioned, because they do not exist within the backup data and can be extracted without special permission, regardless of the area of backup." In other words, the backup protocol itself was never designed to transmit these file types, so no amount of protocol reverse engineering will surface them through this acquisition path.

## Why It Matters

An investigator relying solely on a reverse-engineered backup-protocol tool for full-device acquisition would systematically miss photo and document evidence, since this data category falls categorically outside the protocol's scope rather than merely being harder to access. Because these files are described as extractable without special permission by other means, this is a scope limitation of the specific technique rather than an unrecoverable evidence gap overall.

## Related Mitigations

- [[mitigations/Supplement backup-protocol acquisition with standard file-system extraction for media files]]

## Used By

- [[techniques/Acquire data by reverse-engineering a proprietary backup protocol]]

## References

- [LWCite-1047] Park et al., 2022, "A study on data acquisition based on the Huawei smartphone backup protocol", FSI: Digital Investigation 41.
