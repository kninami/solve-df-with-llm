---
id: DFM-1210
type: mitigation
name: Recover the decrypted-content SQLite datastore alongside LevelDB when parsing Matrix client artifacts
source_refs:
  - DFCite-1223
updated_at: 2026-08-13
status: complete
---

# Recover the decrypted-content SQLite datastore alongside LevelDB when parsing Matrix client artifacts

## Summary

Do not treat the LevelDB store as the sole or complete source of Matrix chat content; also acquire and, where its access password is discoverable in the client's own code, open the client's supplementary decrypted-content SQLite datastore to recover plaintext for messages that are only stored as ciphertext in LevelDB.

## Addresses

- [[weaknesses/Matrix's client-side LevelDB message store retains only ciphertext for end-to-end-encrypted rooms]]

## How To Apply

Acquire both the LevelDB IndexedDB directory and any accompanying SQLite database maintained by the Matrix client for search or caching purposes. For a given client version, check the application's own bundled source code or configuration for a hardcoded database password before assuming the database is inaccessible without the user's credentials. Since this workaround depends on a version-specific implementation detail rather than a documented feature, re-verify its continued availability for each client version examined, and where it is absent, pursue session-key recovery (from device backups, key export, or memory) as an alternative route to the encrypted room's plaintext content.

## References

- [DFCite-1223] Schipper et al., 2021, "Forensic analysis of Matrix protocol and Riot.im application", FSI: Digital Investigation 36.
