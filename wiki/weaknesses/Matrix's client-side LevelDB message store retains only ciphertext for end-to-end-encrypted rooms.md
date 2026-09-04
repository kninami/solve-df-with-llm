---
id: LWW-1210
type: weakness
name: Matrix's client-side LevelDB message store retains only ciphertext for end-to-end-encrypted rooms
description: The Riot.im client's primary LevelDB local storage records message events for encrypted rooms only in their encrypted form, so message content cannot be searched or read from this store alone without also recovering the relevant Megolm session/device keys, leaving investigators dependent on a secondary, less consistently available data source.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-1210
source_refs:
  - LWCite-1223
updated_at: 2026-08-13
status: complete
---

# Matrix's client-side LevelDB message store retains only ciphertext for end-to-end-encrypted rooms

## Summary

Because the LevelDB store only stores the encrypted version of message events for encrypted rooms, it is not possible to search these messages, and their plaintext content is unavailable from this store without independently obtaining the encryption session keys used to protect the room's Megolm ratchet.

## Why It Matters

An investigator who parses only the LevelDB store will recover a complete record of encrypted-room activity's existence and metadata (timestamps, sender, room ID) but not its content, and may either wrongly conclude the content is entirely unrecoverable or fail to check the separate `events.db` datastore that, in some client versions, incidentally retains decrypted content for search-indexing purposes. Because that secondary datastore's availability depends on an undocumented, version-specific implementation detail (a hardcoded password left in place during feature development) rather than a stable, intended forensic access path, this workaround cannot be relied upon to persist across future client versions.

## Related Mitigations

- [[mitigations/Recover the decrypted-content SQLite datastore alongside LevelDB when parsing Matrix client artifacts]]

## Used By

- [[techniques/Extract Matrix protocol chat artifacts from Riot.im's LevelDB and SQLite local data stores]]

## References

- [LWCite-1223] Schipper et al., 2021, "Forensic analysis of Matrix protocol and Riot.im application", FSI: Digital Investigation 36.
