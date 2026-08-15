---
id: DFT-1267
type: technique
name: Recover deleted Realm database records using table, column, and field-unit node analysis
description: Recover data deleted from a mobile app's Realm database (an increasingly popular SQLite alternative) by parsing the database's B-tree-like node structure to identify inactive root and leaf nodes disconnected from the live tree, and — when a node is only partially overwritten — falling back to regular-expression-based parsing keyed to each column's known Realm data type, covering table-unit, column-unit, and field-unit recovery depending on how much of the original node structure survives.
objective_ids:
  - DFO-1018
weakness_ids:
  - DFW-1278
aliases:
  - Realm DB deleted-record recovery
source_refs:
  - DFCite-1306
updated_at: 2026-08-14
status: complete
---

# Recover deleted Realm database records using table, column, and field-unit node analysis

## Summary

Realm DB, an increasingly popular SQLite alternative used by messaging and other mobile apps for its speed and column-oriented storage, uses copy-on-write semantics: a deletion or modification copies and updates only the affected root and internal nodes, leaving the original, now-inactive nodes and their leaf-node subtrees physically present but disconnected from the live tree — and, since Realm applies no default secure-delete/overwrite behavior, this disconnected data remains recoverable in the file's unallocated area until later database activity happens to reuse that space.

## Details

Recovery proceeds through three levels depending on how intact the disconnected structure is: table-unit recovery (Case 1) applies when a root node is not itself overwritten, either fully intact and linked to its original leaf nodes (identified via each node's 4-byte "AAAA" signature and a specific 2-byte offset value indicating class-information), or with a damaged-but-recognizable root node header (identified via still-fixed byte positions even when two variable-content bytes have changed) whose leaf-node links must be separately re-established; column-unit recovery (Case 2) applies when the root node itself has been overwritten and disconnected from its leaf nodes entirely, in which case each surviving leaf node is instead classified independently via its own `has_refs` header flag (0 for a leaf node, since it has no child references) and parsed for the specific column's data it held; and field-unit recovery (the finest-grained fallback) applies when even individual leaf nodes are only partially overwritten, in which case the disconnected data cannot be parsed via node structure at all and must instead be identified within the file's remaining unallocated space using a data-type-specific regular expression built from each column's known Realm data type (string, int, bool, float, double, binary, timestamp, etc.) and expected length pattern.

## Examples

- On a sample three-column test database, table-unit recovery reconstructed two to three prior root-node generations from the current root node, recovering their associated deleted column data, while column-unit recovery separately confirmed two to three deleted entries recoverable per column, with more than half of one column's deleted data recoverable directly.
- Applied to MiniTalk (a Korean parent-child messenger and location-tracking app that only supports deleting an entire chat room, not individual messages) and Xabber (an XMPP client supporting individual-message deletion), the same recovery methodology successfully recovered deleted messages in both real apps' unencrypted Realm database files across five different insertion/deletion test scenarios each, without requiring any decryption step since neither app encrypts its local Realm database.
- Recovery rate varied sharply by app: MiniTalk's deleted data disappeared quickly as new messages were inserted (16% average recovery rate in the scenario combining the most deletions and subsequent insertions), while Xabber retained essentially all deleted data (100% recovery rate) across every tested scenario, including ones with substantial subsequent message insertion — illustrating that recoverability depends on each app's own internal data-management behavior, not solely on Realm's own general deletion mechanics.

## Related Objectives

- `DFO-1018` Read data from digital evidence storage formats

## Related Weaknesses

- [[weaknesses/Realm database deleted-record recovery rate varies unpredictably by app and decays rapidly with new data insertion]]

## References

- [DFCite-1306] Kim, Kim, Shin, Youn, Song, Lee and Kim, 2022, "Methods for recovering deleted data from the Realm database: Case study on Minitalk and Xabber", FSI: Digital Investigation 40, 301353.
