---
id: DFT-1054
type: technique
name: Acquire data by reverse-engineering a proprietary backup protocol
description: Reconstruct a smartphone manufacturer's undocumented, proprietary device-backup protocol — its connection handshake, authentication/key-exchange sequence, and serialized backup-data message format — through a combination of USB packet capture, static and dynamic reverse engineering of the vendor's backup application, and log-based reconstruction of the serialization schema, in order to build an independent acquisition tool that does not depend on the vendor's own backup software.
objective_ids:
  - DFO-1006
weakness_ids:
  - DFW-1057
aliases:
  - Reverse-engineered proprietary backup-protocol data acquisition
source_refs:
  - DFCite-1047
updated_at: 2026-08-09
status: complete
---

# Acquire data by reverse-engineering a proprietary backup protocol

## Summary

Smartphone manufacturers provide their own backup programs (e.g., Huawei's HiSuite), but forensic investigators dealing with many device manufacturers benefit from consolidating acquisition into a single framework rather than installing and learning a separate tool per manufacturer; doing so requires first understanding each manufacturer's undocumented backup protocol well enough to reimplement it independently.

## Details

The analysis proceeds in three coordinated parts: USB packet analysis (capturing the backup traffic with a packet analyzer such as Wireshark plus a USB-capture plugin, filtered to the relevant transfer type and direction to isolate backup-related packets) reveals the wire-level message structure; static and dynamic reverse engineering of the client-side backup application (decompiling to identify cryptographic primitives and constants, then debugging with breakpoints at the protocol's execution points to observe plaintext values before encryption) reveals the authentication and key-exchange logic; and serialized-data analysis reconstructs the message schema (e.g., a Protocol Buffers `.proto` file) needed to interpret structured backup payloads, which is difficult since manufacturers do not publish this schema — inferred indirectly from a client-side log viewer that records the same key-value pairs the serialized messages encode, letting the schema be regenerated from the logged values rather than guessed.

## Examples

- Reverse-engineering Huawei's HiSuite backup protocol (an HDB handshake and authentication stage using RSA-2048/AES-128, followed by a HiSuite-layer verification-code, key-exchange, and backup-communication stage serialized with Protocol Buffers) enabled a replacement tool that could authenticate with and extract SMS/MMS, call logs, contacts, calendar, and third-party app (WeChat, Telegram, WhatsApp) backup data directly from a Huawei smartphone without using HiSuite itself.

## Related Objectives

- `DFO-1006` Acquire data

## Related Weaknesses

- [[weaknesses/Reverse-engineered backup-protocol acquisition does not cover general media files outside the backup data set]]

## References

- [DFCite-1047] Park et al., 2022, "A study on data acquisition based on the Huawei smartphone backup protocol", FSI: Digital Investigation 41.
