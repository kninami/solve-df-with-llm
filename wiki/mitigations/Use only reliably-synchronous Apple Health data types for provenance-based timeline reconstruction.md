---
id: DFM-2093
type: mitigation
name: Use only reliably-synchronous Apple Health data types for provenance-based timeline reconstruction
source_refs:
  - DFCite-2108
updated_at: 2026-08-16
status: complete
---

# Use only reliably-synchronous Apple Health data types for provenance-based timeline reconstruction

## Summary

When reconstructing a device provenance timeline from Apple Health's `data_provenances` table, rely on data types (such as step counts) empirically shown to update their provenance timestamp close to the time of the underlying activity, and treat data types shown to lag (such as distance) as unreliable for precise timeline placement pending further validation.

## Addresses

- [[weaknesses/Apple Health provenance timestamps for some data types are delayed by up to a year from the underlying activity]]

## How To Apply

Before using a specific health data type's provenance timestamp to place an activity or device-usage event in time, confirm that data type has been empirically validated to update synchronously with the underlying activity (e.g. step counts), rather than assuming all Apple Health data types behave the same way. Where a case depends on a data type known or suspected to lag (e.g. distance), cross-validate the resulting timeline against an independently synchronous data type or an entirely separate evidence source (e.g. GPS logs, photo EXIF metadata) before relying on the conclusion. Document which specific data type's provenance timestamp supported a given timeline conclusion, so the reliability caveat travels with the finding.

## References

- [DFCite-2108] "The provenance of Apple Health data: A timeline of update history", FSI: Digital Investigation 48, 2024.
