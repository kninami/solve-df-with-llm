---
id: LWW-1225
type: weakness
name: Memory forensics of Electron-based IM apps cannot recover artifacts for channels or features the examined account could not access
description: Because an Electron-based instant-messaging client only receives and holds in memory the data its logged-in account is authorized to see, memory forensics of that process cannot recover content from channels the account was excluded from, or session-state details (such as active voice-chat participant identity) the client never materialized into a retrievable in-memory object.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-1225
source_refs:
  - LWCite-1236
updated_at: 2026-08-13
status: complete
---

# Memory forensics of Electron-based IM apps cannot recover artifacts for channels or features the examined account could not access

## Summary

Testing an account excluded from a restricted Discord server channel found no JSON objects referencing that channel's content anywhere in the excluded account's memory snapshots — the server application simply never pushes data the client is not authorized to see — and testing an active voice-chat session found only a single generic string noting the channel's active-user count, with no JSON object identifying which specific users were connected or for how long, unlike text-channel messages which were fully recoverable.

## Why It Matters

An investigator relying on memory forensics of one account's IM client process cannot assume that account's memory holds a complete record of all activity across every channel or feature of the platform; access-restricted channels require examining a memory dump from an account (or an administrator's export) that actually had visibility into them, and features whose real-time state the client does not persist into a retrievable structured object (such as detailed voice-chat participant/duration data) may be unrecoverable from memory regardless of which account is examined.

## Related Mitigations

- [[mitigations/Acquire memory from an account with full visibility into all channels and voice sessions before relying on IM memory forensics for completeness]]

## Used By

- [[techniques/Recover application artifacts from process memory using unstructured keyword string search]]

## References

- [LWCite-1236] Davis, McInnes and Ahmed, 2022, "Forensic investigation of instant messaging services on linux OS: Discord and Slack as case studies", DFRWS 2022 USA; FSI: Digital Investigation 42, 301401.
