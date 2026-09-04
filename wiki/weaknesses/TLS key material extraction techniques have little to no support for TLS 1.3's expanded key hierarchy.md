---
id: LWW-2097
type: weakness
name: TLS key material extraction techniques have little to no support for TLS 1.3's expanded key hierarchy
description: The large majority of published TLS key-material identification and extraction techniques were developed for and validated against TLS 1.2, which needs only the single master secret to decrypt an entire session; TLS 1.3 replaced this with an expanded hierarchy of multiple distinct secrets (early, handshake, and per-connection application traffic secrets, derived via HKDF rather than the older PRF), and most existing techniques have not been adapted or re-validated to identify and extract this different set of secrets.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-2098
source_refs:
  - LWCite-2114
updated_at: 2026-08-16
status: complete
---

# TLS key material extraction techniques have little to no support for TLS 1.3's expanded key hierarchy

## Summary

A systematic comparison of published TLS key-extraction methods against the TLS libraries and versions they actually support found that dead-forensics approaches relying on a single master-secret target (brute-force search, most structure-identification and pattern-matching work) are fundamentally limited to TLS 1.2, since TLS 1.3 no longer uses a single master secret sufficient to decrypt all traffic and instead derives a chain of distinct handshake and per-connection application traffic secrets via HKDF. Of the approaches evaluated, hooking-based live-session techniques (particularly `SSL_read`/`SSL_write` hooking and TLS-keylog-callback hooking) show the broadest current TLS 1.3 support, but even these do not cover the full range of TLS libraries in production use, and no research was identified specifically addressing TLS 1.3 key material identification in the dead-forensics (memory-dump) context at all.

## Why It Matters

An investigator who applies a TLS-1.2-oriented key-extraction technique against a TLS 1.3 session -- an increasingly common scenario, since TLS 1.3 adoption is already the preferred protocol version for a majority of major web servers -- risks failing to recover any usable key material at all, or worse, may not recognize that the technique's silent failure reflects an unsupported protocol version rather than an absence of extractable secrets. Because TLS 1.3's application traffic secrets, unlike TLS 1.2's master secret, are specific to a single connection direction and can themselves be periodically updated during a long-lived connection, a technique validated only against TLS 1.2's simpler, connection-spanning master secret cannot be assumed to generalize without substantial redesign.

## Related Mitigations

- [[mitigations/Confirm a TLS key-extraction technique's TLS-version and library support before relying on it to decrypt captured traffic]]

## Used By

- [[techniques/Extract TLS session keys from a memory image using structure identification, hooking, or memory-diffing techniques]]

## References

- [LWCite-2114] Baier, Basse, Hilgert, and Lambertz, 2024, "TLS key material identification and extraction in memory: Current state and future challenges", FSI: Digital Investigation 49, 301766.
