---
id: DFT-1201
type: technique
name: Extract Matrix protocol chat artifacts from Riot.im's LevelDB and SQLite local data stores
description: Locate and parse the LevelDB IndexedDB store and hardcoded-password-protected SQLite database that the Riot.im Matrix client uses for local chat storage, recovering message events, room membership, device/user identifiers, and cached media even for end-to-end-encrypted conversations.
objective_ids:
  - DFO-1011
weakness_ids:
  - DFW-1210
aliases:
  - Riot.im LevelDB and events.db extraction
source_refs:
  - DFCite-1223
updated_at: 2026-08-13
status: complete
---

# Extract Matrix protocol chat artifacts from Riot.im's LevelDB and SQLite local data stores

## Summary

The Riot.im desktop Matrix client stores chat data in two separate local locations with different characteristics: a LevelDB IndexedDB store holding raw message events (encrypted and unencrypted) and application logs, and a separate SQLite database intended to hold a searchable, decrypted copy of message content and protected by a password hardcoded in the application's own source code. Parsing both, rather than either alone, recovers the fullest available set of Matrix chat artifacts from a Windows Riot.im installation.

## Details

Riot.im installs to `<user>\AppData\Local\riot-desktop\` and stores data in `<user>\AppData\Roaming\Riot\`. The LevelDB store at `IndexedD\vector_vector_0.indexeddb.leveldb` can be parsed with standard LevelDB recovery tools (e.g. `leveldb-tools`) to recover all messages sent in unencrypted rooms, plus device/session-key-synchronization log entries (containing full username, device ID, and Matrix homeserver URL) and a log entry naming the Matrix server used. Because Riot.im's decrypted-message search feature was, at the time of study, still under development, its accompanying `events.db` SQLite database (at `<user>\AppData\Roaming\Riot\EventStore\`) had its password hardcoded in plaintext directly in the application's own source code; using this password to open the database exposes an `event` table holding the unencrypted parts of encrypted message events, alongside `room` and `profile` tables, giving access to decrypted content the LevelDB store alone cannot provide. Riot.im's use of Electron/Chromium also means its cache directory follows the standard Chrome cache layout, from which thumbnails and complete cached images can be recovered with standard browser-cache-viewer tools, and a plaintext `preferences` file in the data directory records the default download directory, last upload directory, and spellcheck language.

## Examples

- Recovering all messages sent in an unencrypted Matrix room, plus the device identifier, username, and homeserver URL of the account that sent them, by parsing the `vector_vector_0.indexeddb.leveldb` LevelDB store with `leveldb-tools`.
- Opening `events.db` with its hardcoded application password to read the decrypted `content` of messages sent in an end-to-end-encrypted room, which the encrypted LevelDB copy alone does not expose.

## Related Objectives

- `DFO-1011` Extract artifacts stored by applications

## Related Weaknesses

- [[weaknesses/Matrix's client-side LevelDB message store retains only ciphertext for end-to-end-encrypted rooms]]

## References

- [DFCite-1223] Schipper et al., 2021, "Forensic analysis of Matrix protocol and Riot.im application", FSI: Digital Investigation 36.
