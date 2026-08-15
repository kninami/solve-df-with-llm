---
id: DFW-1278
type: weakness
name: Realm database deleted-record recovery rate varies unpredictably by app and decays rapidly with new data insertion
description: The proportion of deleted Realm database data actually recoverable depends heavily on the specific app's own internal data-management behavior, not just Realm's generic deletion mechanics, and recovery rate drops sharply the more new data is inserted after a deletion occurs — with the two apps tested in the same study showing opposite extremes (near-total loss versus near-total retention) under otherwise comparable test scenarios.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1279
source_refs:
  - DFCite-1306
updated_at: 2026-08-14
status: complete
---

# Realm database deleted-record recovery rate varies unpredictably by app and decays rapidly with new data insertion

## Summary

Testing the same recovery methodology against two real Realm-DB-based messaging apps found MiniTalk's deleted message data disappeared quickly as new messages were inserted (dropping to a 16% average recovery rate in the most insertion-heavy tested scenario), while Xabber retained deleted data almost indefinitely (100% recovery rate across every tested scenario, including ones with substantial subsequent insertion) — a stark divergence the study attributes to each app's own internal data-management characteristics rather than to any difference in the underlying Realm database engine. Sample-app testing separately confirmed that recovery rate depends on how many deletion-then-insertion cycles have occurred and which column a piece of data is stored in, with later-inserted data and earlier-position columns recovering at markedly lower rates than data in later columns.

## Why It Matters

An investigator cannot assume a Realm-database deleted-record recovery result obtained against one app will transfer to a different app, even one using the same underlying database engine and even under superficially similar usage patterns — a recovery rate validated on one messaging app could mean anything from near-complete to near-zero recovery on another, and the amount of subsequent app usage between the deletion and the acquisition materially affects how much is still recoverable. Presenting a recovery finding without accounting for the specific app's own retention behavior risks either an overstated claim of completeness or premature abandonment of an attempt that a different app or an earlier acquisition timing would have succeeded at.

## Related Mitigations

- [[mitigations/Validate Realm deleted-record recovery rate against the specific target app and acquire promptly to minimize post-deletion data insertion]]

## Used By

- [[techniques/Recover deleted Realm database records using table, column, and field-unit node analysis]]

## References

- [DFCite-1306] Kim, Kim, Shin, Youn, Song, Lee and Kim, 2022, "Methods for recovering deleted data from the Realm database: Case study on Minitalk and Xabber", FSI: Digital Investigation 40, 301353.
