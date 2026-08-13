---
id: DFT-1158
type: technique
name: Recover web application account and content artifacts from browser cache and local storage
description: Parse a Chromium-based browser's SQLite History, Cache, and Web Data files together with its per-origin LevelDB local storage (.ldb/.log) to recover a web-app platform's account settings, authentication tokens, contacts/connections, and content (messages, meeting records, media, calls) after the platform was used through the browser rather than a native app.
objective_ids:
  - DFO-1011
weakness_ids:
  - DFW-1162
aliases:
  - Recover messaging app account and content artifacts from browser cache and local storage
  - Web application (Discord) forensic artifact recovery from Google Chrome
  - Google Meet browser artifact recovery (History, IndexedDB-LevelDB, Cache, Cookies)
source_refs:
  - DFCite-1165
  - DFCite-1235
updated_at: 2026-08-13
status: complete
---

# Recover web application account and content artifacts from browser cache and local storage

## Summary

When a messaging, meeting, or other social/collaboration platform is used through a web browser instead of its native application, the browser's own storage mechanisms — cache, local storage, history, and the web-data form-autofill store — retain a substantial, largely unencrypted record of the user's account and activity, recoverable with standard SQLite/LevelDB parsing tools even after the browser session ends.

## Details

Chrome's local storage (JSON-formatted `.ldb`/`.log` LevelDB files under `Local Storage\leveldb` or, for IndexedDB-backed origins, under `IndexedDB\<origin>.indexeddb.leveldb`) persisted account settings, login/authentication tokens, and application-specific object stores, and these files remain present and readable in a hex editor after the browser is closed — they are not automatically deleted at session end. The browser's cache (parsed via a cache-viewer tool) held the same account-settings data as JSON responses, plus payment method details stored with no encryption at all, third-party account connections with access tokens, message/meeting content with author/participant IDs and timestamps, media/link attachments, and call/session participant and timing metadata. The browser History file separately recorded visited URLs (including third-party OAuth authorization URLs, corroborating account-connection artifacts found elsewhere) and, for a Chromium browser's `Sessions` folder logs, could contain scattered fragments of chat/meeting-chat text following recognizable HTML tag markers even though the platform itself claims not to persist that content anywhere. Testing the same scenarios on both a physical machine and a virtual machine disk found no difference in recoverable artifacts, meaning a suspect's use of a VM does not defeat this recovery approach.

## Examples

- A Discord login token, payment card's last four digits, expiry date, and billing address were all recovered in cleartext from the Chrome cache file `payment_sources.json` after only adding a payment method to the account, with no in-app transaction required.
- Message-reply artifacts (the referenced message ID, timestamps, and reply content) and edited/pinned message timestamps were recovered from cache JSON, letting an investigator reconstruct the exact sequence and content of a multi-party conversation, including messages later edited or deleted from the visible chat.
- Server audit-log entries recovered from cache (`audit_log_entries`) recorded role changes, channel creation, and invite creation with actor and target user IDs, useful for establishing which account performed a given administrative action within a group.
- Google Meet's per-origin IndexedDB-LevelDB folder (`https_meet.google.com_0.indexeddb.leveldb`) contained a `meet_store` object store listing every meeting ID the account had previously held or joined together with the local user's GUID, and — for meetings scheduled via Google Calendar — the meeting's title, even though the object store recorded no timestamps for these entries.
- Google Meet's Chrome cache recovered a scheduled meeting's full metadata (conference ID, name, description, location, creator/attendee email addresses, start/end timestamps, time zone), the join/leave call audio tunes, and location predictions surfaced during meetings that used Google Maps, while its `Sessions` folder logs contained scattered, fragmented in-call chat text following `<chatTextInput>`/`<textarea>` HTML tag markers — a highly manual but usable fallback source when memory capture was not possible.

## Related Objectives

- `DFO-1011` Extract artifacts stored by applications

## Related Weaknesses

- [[weaknesses/Browser cache artifacts are more volatile than local storage and can be lost before acquisition]]

## References

- [DFCite-1165] Gupta et al., 2022, "Digital forensic analysis of discord on google chrome", FSI: Digital Investigation 44, 301479.
- [DFCite-1235] Iqbal, Khalid, Marrington, Shah and Hung, 2022, "Forensic investigation of Google Meet for memory and browser artifacts", DFRWS 2022 APAC; FSI: Digital Investigation 43, 301448.
