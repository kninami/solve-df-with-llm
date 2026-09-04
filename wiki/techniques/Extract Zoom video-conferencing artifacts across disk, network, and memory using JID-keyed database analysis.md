---
id: LWT-2127
type: technique
name: Extract Zoom video-conferencing artifacts across disk, network, and memory using JID-keyed database analysis
description: Recover Zoom video-conferencing evidence (contacts, chat messages, exchanged files, meeting history, and account credentials) by locating each user account's Jabber ID (JID)-named data directory on disk across Android, iOS, macOS, and Windows, decrypting captured HTTPS traffic with a TLS-intercepting proxy, and inspecting process memory for residual chat content, then triaging the resulting SQLite databases with a prepared set of investigator queries.
objective_ids:
  - DFO-1011
weakness_ids:
  - LWW-2137
aliases:
  - Zoom forensic artifact analysis
source_refs:
  - LWCite-2158
updated_at: 2026-08-17
status: complete
---

# Extract Zoom video-conferencing artifacts across disk, network, and memory using JID-keyed database analysis

## Summary

Zoom organizes each logged-in account's local data under a directory named after that account's Jabber ID (JID), an Extensible Messaging and Presence Protocol (XMPP) address uniquely identifying the user, with a consistent set of SQLite databases (`*.asyn.db` for chats and devices, `*.us.db` for contacts, `*.idx.db` for cached message/contact indexes, `*.sync.db` for contact requests, `zoommeeting.db` and `zoomus.db` for meeting/account data) recurring across Android, iOS, macOS, and Windows despite differing file-system paths on each platform. Combining disk analysis of these databases with HTTPS traffic decryption (since Zoom encrypts network traffic by default) and process-memory inspection recovers chat content, contact information, credentials, and meeting metadata even when some of it is stored encoded or encrypted in a single artifact type alone.

## Details

A TLS-intercepting proxy configured with a trusted root certificate on the device under test decrypts Zoom's HTTPS traffic, revealing login credentials transmitted for Basic (password-based) accounts and other artifacts fetched over the network at login (account email, JIDs, session cookies, access tokens, device ID, profile picture, meeting room invitation content, and chat history for the Chat feature specifically, though not for in-meeting chat). Volatile memory acquired while Zoom is actively running reliably yields plaintext and encrypted chat messages, contact names/emails/JIDs, and certificate/key material; memory acquired after Zoom has fully exited retains substantially less recoverable data via structured plugin-based analysis (e.g. Volatility's `yarascan`), but a generic string-search tool can still recover some residual chat fragments. To speed up triage of the recovered SQLite databases, a prepared set of parameterized SQL queries against the JID-keyed databases returns recent cached chat messages by timestamp or direction, full contact lists, group-chat participant/owner information, complete chat threads (with file-attachment and emoji-comment joins) for a specific chat session, and each session's start date and last message ID.

## Examples

- Decrypting Fiddler-captured HTTPS traffic during a Basic-account login recovered the account's plaintext username and password submitted via the login form; the same technique against a Licensed (SAML single-sign-on) account login did not recover a password, since credentials never traversed that request in cleartext.
- Running Volatility's `yarascan` plugin against a memory image captured while Zoom was actively open recovered chat sender/receiver names and message bodies in plaintext; string-searching a memory image captured after Zoom had fully exited still recovered a subset of the same chat messages, sender/receiver names, and JIDs that the structured plugin analysis missed.

## Related Objectives

- `DFO-1011` Extract artifacts stored by applications

## Related Weaknesses

- [[weaknesses/Deleting a Zoom contact removes shared chat history from the other party's device without their consent]]

## References

- [LWCite-2158] Mahr et al., 2021, "Zooming into the pandemic! A forensic analysis of the Zoom Application", FSI: Digital Investigation 36.
