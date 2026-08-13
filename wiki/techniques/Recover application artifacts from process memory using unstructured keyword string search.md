---
id: DFT-1212
type: technique
name: Recover application artifacts from process memory using unstructured keyword string search
description: Extract an application's account, meeting, or conversation artifacts from a process memory dump by grepping for application- and account-specific keywords in raw extracted strings, without deriving the application's internal object/structure layout, recovering data that logging and disk-based storage do not retain.
objective_ids:
  - DFO-1011
weakness_ids:
  - DFW-1224
  - DFW-1225
aliases:
  - Google Meet browser-tab process memory string forensics
  - Discord/Slack Electron process memory string forensics
source_refs:
  - DFCite-1235
  - DFCite-1236
updated_at: 2026-08-13
status: complete
---

# Recover application artifacts from process memory using unstructured keyword string search

## Summary

Web and Electron-framework applications often keep no local disk record of session content — a web-based video-conferencing client may claim in-call messages are deleted at call end, and neither category of application stores a native on-disk file structure a general forensic tool understands — but because the running process must still hold that content in memory, a plain keyword-driven string search (rather than a structure-signature-based parse) can recover it directly from a process memory dump.

## Details

The method captures a memory image of the target process (a browser tab's renderer process for a web application, or the Electron app's own process on the host OS), extracts printable strings, and greps for a small set of application- and account-specific keywords (an application name, the test account's username/email, or a protocol-specific tag such as a JSON field name) to narrow a large memory dump down to a manageable set of candidate lines before manual or scripted extraction of the surrounding JSON-like structured data. Because the target applications transmit and cache their internal state as JSON objects rather than opaque binary structures, the recovered string fragments are often directly human-readable once located, without needing to reverse-engineer a byte-level object layout the way structure-signature-based memory forensics does. The same underlying approach — process identification via a keyword-anchored search (e.g. `yarascan` for a browser tab's title, or `linux_pslist` for a native process), followed by memory-page dumping and grep-based filtering — applies whether the target is a browser rendering a web application or a native Electron desktop client, though the specific process(es) to target and the exact JSON schema recovered differ per application.

## Examples

- Searching Chrome/Firefox/Edge memory dumps of Google Meet for the account's Gmail address (after excluding matches inside Google Meet's own open-source JavaScript) recovered meeting names, the account's device ID, and sent/received in-call chat messages with timestamps, in a format that was identical across all three browsers and both Windows and Linux, confirming the recovered format depends on the application rather than the browser or OS.
- Running a modified `linux_dump_map` Volatility plugin against Discord's and Slack's Ubuntu Linux processes and grepping the output for account usernames, `gmail`, `password`, and application names recovered a plaintext Discord login-credential JSON object, direct-message and server-channel text content, gif/image/text-file attachment CDN URLs, and bot interaction records.
- On Discord, uploaded-file CDN URLs recovered from memory (`https://cdn.discordapp.com/attachments/...`) were directly accessible without authentication in a separate browser, while equivalent Slack file URLs redirected to a workspace sign-in page, illustrating that the two applications' differing access-control models affect how far the recovered evidence can be corroborated without further credentials.

## Related Objectives

- `DFO-1011` Extract artifacts stored by applications

## Related Weaknesses

- [[weaknesses/Unstructured string-search recovery of application memory artifacts is incomplete and its format varies with available RAM]]
- [[weaknesses/Memory forensics of Electron-based IM apps cannot recover artifacts for channels or features the examined account could not access]]

## References

- [DFCite-1235] Iqbal, Khalid, Marrington, Shah and Hung, 2022, "Forensic investigation of Google Meet for memory and browser artifacts", DFRWS 2022 APAC; FSI: Digital Investigation 43, 301448.
- [DFCite-1236] Davis, McInnes and Ahmed, 2022, "Forensic investigation of instant messaging services on linux OS: Discord and Slack as case studies", DFRWS 2022 USA; FSI: Digital Investigation 42, 301401.
