---
id: DFT-1208
type: technique
name: Decode an app's proprietary BLOB-serialized object data using open-source-derived class signatures
description: Recover structured, forensically relevant data from an application's SQLite BLOB columns by deriving each internal class's hash-based signature and per-attribute key/data-type encoding from the application's own open-source code, then locating and parsing matching class instances directly within the raw BLOB bytes.
objective_ids:
  - DFO-1011
weakness_ids:
  - DFW-1219
aliases:
  - Telegram iOS BLOB decoding via MurmurHash3 class signatures
  - PostboxEncoder BLOB decoding
source_refs:
  - DFCite-1230
updated_at: 2026-08-13
status: complete
---

# Decode an app's proprietary BLOB-serialized object data using open-source-derived class signatures

## Summary

Some applications store their local database's most forensically valuable content — contacts, conversations, group membership — as a proprietary serialized binary format inside generic SQLite BLOB columns rather than as directly queryable relational fields, so recovering it requires deriving the application's own object-encoding scheme from its open-source client code rather than treating the column as opaque binary data.

## Details

The method examines the application's serialization source file (e.g. an object encoder class) to learn the general encoding grammar: each serialized object begins with a fixed-size hash of its class name, followed by a sequence of class-specific attributes, each itself encoded as a short attribute key, a one-byte data-type identifier, and a type-dependent value (fixed-size integers/booleans, length-prefixed strings, or nested length-prefixed objects/arrays). The class-name hash is computed with a known, fast, non-cryptographic hash function (e.g. MurmurHash3 with a fixed seed) and can be recomputed for any class defined in the source code, yielding a reusable 4-byte signature that a byte-level scan of a BLOB (or an entire memory/disk image) can search for directly. Once a class instance is located via its signature, its attributes are decoded sequentially using their known key/type pairs, and any attribute holding an identifier that is itself a foreign key (e.g. a peer/user ID) can be followed into other tables' BLOB columns to reconstruct cross-referenced records — for instance, resolving which peer a message belongs to, or which parent object a nested array element represents. The primary maintenance cost is that the encoding is tied to a specific application version: a major client rewrite (e.g., a full language/architecture migration) can invalidate the entire derived signature set, and even minor releases can add, remove, or reorder attributes.

## Examples

- Telegram-iOS's central `db_sqlite` database stores contacts, chats, channels, and secret chats as `RootObject`-encoded BLOBs in table `t2`; each object's 4-byte MurmurHash3 class signature (e.g. `0x2BA5689E` for `TelegramUser`) was recomputed directly from the corresponding open-source Swift class definition and used to locate and decode a user's first name, username, and phone number from raw BLOB bytes.
- Message records in table `t7`'s `value` column were decoded attribute-by-attribute using a chronological attribute table derived from the `justInsertMessage()` function, recovering message text, sender ID, forwarding metadata, and attached media references even though the BLOB in this specific table omits the usual `RootObject` class-signature header.
- The local user's own peer ID was located within the `MetadataTable` by searching for the fixed byte sequence `0x0670656572496401` (the encoded attribute key `peerId` followed by its Int64 data-type marker), rather than by parsing the entire table structure.

## Related Objectives

- `DFO-1011` Extract artifacts stored by applications

## Related Weaknesses

- [[weaknesses/App-specific BLOB serialization formats change across versions without a compatibility signal]]

## References

- [DFCite-1230] Jaeckel, Spranger and Labudde, 2025, "Forensic analysis of Telegram Messenger on iOS smartphones", DFRWS EU 2025; FSI: Digital Investigation 52, 301866.
