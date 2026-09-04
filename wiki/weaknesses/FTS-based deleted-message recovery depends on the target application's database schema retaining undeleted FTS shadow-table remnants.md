---
id: LWW-1204
type: weakness
name: FTS-based deleted-message recovery depends on the target application's database schema retaining undeleted FTS shadow-table remnants
description: Recovering a deleted message via its SQLite FTS shadow-table copy only works when the target application's database uses FTS-indexed tables in the first place and when its delete-message implementation happens to leave the shadow-table copy untouched; an application that does not use FTS for that data, or whose delete logic also clears the shadow table, offers no equivalent recovery path through this technique.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-1204
source_refs:
  - LWCite-1217
updated_at: 2026-08-13
status: complete
---

# FTS-based deleted-message recovery depends on the target application's database schema retaining undeleted FTS shadow-table remnants

## Summary

The technique's applicability rests on two application-specific implementation facts that were confirmed only for Webex's `spark_persistent_store.db` schema: that the relevant table is FTS-indexed at all (94 tables exist in that database, and only some — Actor, Content, Conversation, Message — are FTS-backed), and that the application's delete-message logic clears the main table's content column without also clearing the FTS shadow table's corresponding row. Neither property is guaranteed for other applications, or for a future version of the same application that changes its schema or hardens its deletion logic to also purge shadow-table remnants.

## Why It Matters

An investigator who assumes this recovery path will generalize to any chat or messaging application's SQLite storage may find no FTS shadow tables present at all, or may find that a given application's delete function was implemented to also clear them, in which case this specific technique yields nothing and a different deleted-data-recovery approach (unused-page analysis, journal-file recovery) must be attempted instead. Confirming the presence of FTS-backed tables and testing the application's actual delete behavior against a known message, before relying on the technique in casework, avoids incorrectly concluding that no deleted-message evidence exists.

## Related Mitigations

- [[mitigations/Confirm the target application's database schema uses FTS-indexed tables before relying on FTS-based deleted-message recovery]]

## Used By

- [[techniques/Recover deleted chat messages from SQLite FTS shadow-table remnants]]

## References

- [LWCite-1217] Hur et al., 2023, "Forensic analysis for multi-platform Cisco Webex", FSI: Digital Investigation 47, 301659.
