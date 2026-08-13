---
id: DFM-1225
type: mitigation
name: Acquire memory from an account with full visibility into all channels and voice sessions before relying on IM memory forensics for completeness
source_refs:
  - DFCite-1236
updated_at: 2026-08-13
status: complete
---

# Acquire memory from an account with full visibility into all channels and voice sessions before relying on IM memory forensics for completeness

## Summary

Before treating a single account's IM-client memory dump as a complete record, confirm that account's permission level within the platform, and where possible use an administrator or full-member account's session (or a server export) to cover restricted channels and supplement memory forensics with alternate evidence sources for real-time features like voice chat.

## Addresses

- [[weaknesses/Memory forensics of Electron-based IM apps cannot recover artifacts for channels or features the examined account could not access]]

## How To Apply

Identify the permission level and channel membership of the account whose device memory is being examined, and note explicitly which server/workspace channels that account could not see, since those channels' content will not be recoverable from that account's memory regardless of acquisition timing or technique. Where legally and operationally feasible, obtain a memory dump from an administrator account or a server-side export instead of, or in addition to, a restricted member account's device. For voice-chat or other real-time session features that a client does not persist into a retrievable structured object, rely on complementary evidence sources (server-side logs, network capture of the voice connection, or witness/participant testimony) rather than expecting client-process memory forensics to supply participant identity or duration.

## References

- [DFCite-1236] Davis, McInnes and Ahmed, 2022, "Forensic investigation of instant messaging services on linux OS: Discord and Slack as case studies", DFRWS 2022 USA; FSI: Digital Investigation 42, 301401.
