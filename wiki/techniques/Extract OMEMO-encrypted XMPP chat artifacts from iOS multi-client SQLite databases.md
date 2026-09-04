---
id: LWT-1204
type: technique
name: Extract OMEMO-encrypted XMPP chat artifacts from iOS multi-client SQLite databases
description: Locate and parse the SQLite databases (sworim.sqlite for Monal, siskinim_main.db for Siskin IM) that decentralized, open-source OMEMO-encrypted XMPP multi-client apps maintain on iOS, recovering local user and contact XMPP account identifiers, encrypted and unencrypted message content in plaintext, and cached multimedia files, from an advanced logical (iTunes-backup-based) acquisition.
objective_ids:
  - DFO-1011
weakness_ids:
  - LWW-1213
  - LWW-1214
aliases:
  - Monal and Siskin IM iOS artifact extraction
source_refs:
  - LWCite-1225
updated_at: 2026-08-13
status: complete
---

# Extract OMEMO-encrypted XMPP chat artifacts from iOS multi-client SQLite databases

## Summary

Although Monal and Siskin IM are open-source, decentralized XMPP clients that use OMEMO end-to-end encryption for message transport, both store the decrypted conversation history locally in plaintext within an app-specific SQLite database, so a standard advanced logical (iTunes-backup-based) iOS acquisition followed by manual review of these databases recovers the full local user's account list, contacts (including blocked/deleted ones), and complete message content regardless of whether individual messages were sent OMEMO-encrypted or not.

## Details

Because neither Cellebrite UFED Physical Analyzer's built-in parser (at the time of study) understood either app's data format, both databases required manual, in-depth review rather than relying on the tool's automated report. Monal stores conversation data in `sworim.sqlite` under `/private/var/mobile/Containers/Data/Application/<APP_GUID>/Documents`, with the `account` table holding each of the local user's distinct XMPP accounts, `activechats`/`buddylist` jointly recording active and deleted contacts, and `message_history` holding all messages (sent and received, encrypted and unencrypted) in plaintext along with an `encrypted` status flag, sender/recipient, and timestamp. Siskin IM stores data in `siskinim_main.db` under a shared app-group folder, with `omemo_identities`/`omemo_sessions` recording OMEMO encryption session and device-ID information for active contacts, `roster_items` recording contact-subscription history, and `chat_history` — the app's primary evidential table — holding all one-to-one and group chat messages (again including OMEMO-encrypted ones, decrypted and stored in plaintext) with per-message state, encryption, and file-attachment metadata. For both apps, images sent without OMEMO encryption can be retrieved directly from the XMPP server by requesting the plaintext HTTPS URL stored in the message record, while OMEMO-encrypted media instead resolves to an `aesgcm://` URL whose symmetric key/IV travel with the encrypted message body itself, and locally cached copies of received/sent images (including deleted ones, until the user clears the image cache) can be recovered directly from each app's image-cache subdirectory.

## Examples

- Reconstructing the full chronology of a local user's OMEMO-encrypted and unencrypted one-to-one conversation with a contact, including the plaintext content of encrypted messages, by parsing the `message_history` table of Monal's `sworim.sqlite`.
- Recovering group-chat creation, membership changes, and all exchanged messages (which remain in the `chat_history` table even after the group and its members are later deleted) from Siskin IM's `siskinim_main.db`.

## Related Objectives

- `DFO-1011` Extract artifacts stored by applications

## Related Weaknesses

- [[weaknesses/SQLite VACUUM overwrites freed record data with null bytes, preventing deleted-message recovery]]
- [[weaknesses/VoIP call activity within a messaging app is not recorded in the app's local chat database]]

## References

- [LWCite-1225] Akinbi and Ojie, 2021, "Forensic analysis of open-source XMPP multi-client social networking apps on iOS devices", FSI: Digital Investigation 36.
