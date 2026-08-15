---
id: DFW-1288
type: weakness
name: Simulated MFT-transaction data-run history generation can produce spurious intermediate events not representing the file's actual data location
description: Because a single logical file-data modification can be recorded across multiple sequential $LogFile UpdateMappingPairs records, replaying each record individually generates a historical event for every intermediate record, including ones whose data-run value does not correspond to any location where the file's data was ever actually stored, unless the intermediate events are filtered out.
categories:
  - ASTM_INAC_COR
mitigation_ids:
  - DFM-1289
source_refs:
  - DFCite-1319
updated_at: 2026-08-15
status: complete
---

# Simulated MFT-transaction data-run history generation can produce spurious intermediate events not representing the file's actual data location

## Summary

When a single file modification updates data runs via more than one sequential `UpdateMappingPairs` record, applying only the first record in isolation can yield a data-run value describing a cluster range that never actually held the file's data — the documented example recovers "166,388 (48)" from the first record alone, when only after applying both records in sequence does the correct value, "166,388 (9)," emerge; the intervening cluster range implied by the first record's value alone was never part of the file.

## Why It Matters

An investigator using an unfiltered data-run history to identify where a file's data was stored at a given point in time risks citing a cluster range that never actually contained the file's content, potentially leading an examination of unallocated space or carving effort toward the wrong location, or creating a false impression of how many times the file's data actually moved. Because the spurious event carries no obvious internal marker distinguishing it from a genuine one, an investigator unaware of this artifact could unknowingly present it as fact.

## Related Mitigations

- [[mitigations/Apply temporal or checkpoint-record event filtering before relying on NTFS data-run history events]]

## Used By

- [[techniques/Reconstruct a file's complete data history from NTFS $LogFile transaction replay]]

## References

- [DFCite-1319] Oh, Lee, and Hwang, 2021, "NTFS Data Tracker: Tracking file data history based on $LogFile", FSI: Digital Investigation 39, 301309.
