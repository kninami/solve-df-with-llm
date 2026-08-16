---
id: DFW-2092
type: weakness
name: Apple Health provenance timestamps for some data types are delayed by up to a year from the underlying activity
description: The update timestamp recorded in Apple Health's `data_provenances` table for certain data types -- notably distance -- can lag the actual date of the underlying physical activity by as much as a year, so treating a provenance record's timestamp as reflecting when the associated activity occurred, rather than merely when the record was last synced or updated, risks a substantial event-reconstruction error for the affected data types.
categories:
  - ASTM_INAC_COR
  - ASTM_MISINT
mitigation_ids:
  - DFM-2093
source_refs:
  - DFCite-2108
updated_at: 2026-08-16
status: complete
---

# Apple Health provenance timestamps for some data types are delayed by up to a year from the underlying activity

## Summary

Not all Apple Health data types update their `data_provenances` record synchronously with the underlying activity: step-count data was found to update reliably close to the time of activity, but distance data showed provenance timestamps lagging the actual activity date by as much as roughly a year in some cases, apparently due to how and when the underlying distance calculation is finalized and written back to the database relative to the raw sensor data it derives from.

## Why It Matters

An investigator using a `data_provenances` timestamp to place a device's activity (or a specific data point) at a particular point in time risks a substantial timeline error if the data type in question is one, like distance, whose provenance timestamp does not reliably track the actual activity date. Because this delay is not visually obvious or flagged by the Health app's own interface, and because different data types behave differently in this respect, a blanket assumption that "the provenance timestamp is the activity timestamp" is unsafe without first confirming which behavior applies to the specific data type being relied upon.

## Related Mitigations

- [[mitigations/Use only reliably-synchronous Apple Health data types for provenance-based timeline reconstruction]]

## Used By

- [[techniques/Reconstruct a device provenance timeline from Apple Health database synchronization records]]

## References

- [DFCite-2108] "The provenance of Apple Health data: A timeline of update history", FSI: Digital Investigation 48, 2024.
