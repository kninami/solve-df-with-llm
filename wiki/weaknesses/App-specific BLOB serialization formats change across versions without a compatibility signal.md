---
id: LWW-1219
type: weakness
name: App-specific BLOB serialization formats change across versions without a compatibility signal
description: An application's proprietary BLOB object-serialization scheme (class signatures, attribute keys, table layout) can change entirely between major versions with no indication in the BLOB data itself, so a decoder built against one version silently misparses or fails against another without the underlying source code being re-checked for changes.
categories:
  - ASTM_MISINT
  - ASTM_INCOMP
mitigation_ids:
  - LWM-1219
source_refs:
  - LWCite-1230
updated_at: 2026-08-13
status: complete
---

# App-specific BLOB serialization formats change across versions without a compatibility signal

## Summary

Telegram's iOS client underwent a complete rewrite in October 2018 (from a C-based implementation to Swift-based "Telegram X," retaining the original app name), entirely changing both the database directory structure and the internal BLOB serialization scheme; the study's own authors caution that although much of their derived decoding holds from that rewrite onward, "certain deviations are possible in different versions... it is urgently necessary to regularly check the publicly accessible source code of the messenger for changes."

## Why It Matters

A decoder validated against one specific application version can misinterpret or entirely fail to locate class instances in a BLOB produced by an earlier or later version, and — because the BLOB itself carries no explicit format-version marker readable without first successfully decoding it — this failure mode can be silent rather than producing an obvious error, risking incomplete extraction or misattributed field values being presented as if they were correctly decoded.

## Related Mitigations

- [[mitigations/Re-derive and version-verify class-hash BLOB signatures against the target app's current source code before decoding]]

## Used By

- [[techniques/Decode an app's proprietary BLOB-serialized object data using open-source-derived class signatures]]

## References

- [LWCite-1230] Jaeckel, Spranger and Labudde, 2025, "Forensic analysis of Telegram Messenger on iOS smartphones", DFRWS EU 2025; FSI: Digital Investigation 52, 301866.
