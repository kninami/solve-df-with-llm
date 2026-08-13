---
id: DFW-1205
type: weakness
name: Migrated application credentials can retrieve data generated after the acquisition point, risking misattribution to the original evidence timeframe
description: A migrated credential remains valid on the investigator's device after collection, so the application can continue to synchronize newly created cloud data (new messages, meetings, or files) generated after the point of collection; if this ongoing collection is not clearly separated from the original device's data, later-arriving content risks being conflated with evidence that existed at the time of seizure.
categories:
  - ASTM_INAC_AS
mitigation_ids:
  - DFM-1205
source_refs:
  - DFCite-1217
updated_at: 2026-08-13
status: complete
---

# Migrated application credentials can retrieve data generated after the acquisition point, risking misattribution to the original evidence timeframe

## Summary

The Webex credential-migration study's own authors state that "the proposed credential utilization method can successfully collect data generated after the point of collection by connecting with the server," presenting this as a capability (the migrated device continues operating as a live instance of the suspect's account) rather than a limitation of the technique to a single, fixed point-in-time snapshot.

## Why It Matters

Unlike a conventional disk or memory acquisition, which captures a fixed point-in-time state, a migrated-credential cloud session keeps collecting new data for as long as the migrated device remains connected and the credential remains valid, meaning the "collection" is really an open-ended window rather than a single timestamped event. If an investigator does not clearly timestamp when migration occurred and treat anything retrieved afterward as separately-obtained, ongoing evidence, a report could implicitly suggest that content generated after the suspect's device was seized existed at the time of seizure, misattributing its origin in the evidentiary timeline.

## Related Mitigations

- [[mitigations/Timestamp the credential-migration acquisition point and segregate data retrieved afterward as separately obtained live evidence]]

## Used By

- [[techniques/Access a cloud account using captured credentials]]

## References

- [DFCite-1217] Hur et al., 2023, "Forensic analysis for multi-platform Cisco Webex", FSI: Digital Investigation 47, 301659.
