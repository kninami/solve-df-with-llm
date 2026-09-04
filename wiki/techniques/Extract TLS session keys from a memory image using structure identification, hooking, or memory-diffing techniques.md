---
id: LWT-2093
type: technique
name: Extract TLS session keys from a memory image using structure identification, hooking, or memory-diffing techniques
description: Recover the cryptographic key material (master secret, or TLS 1.3 handshake/application traffic secrets) needed to decrypt a captured TLS session, from either a static memory dump (dead forensics) or a live running process (live forensics), by selecting an extraction approach appropriate to the target TLS library and version -- brute-force search, pattern matching on high-entropy regions, targeted searches for known library-specific data structures, debugger-based structure parsing, commencement-based path traversal, memory-diffing around the handshake, or function hooking of key-derivation/read-write calls.
objective_ids:
  - DFO-1019
  - DFO-1017
weakness_ids:
  - LWW-2097
aliases:
  - TLS key material identification and extraction in memory
source_refs:
  - LWCite-2114
updated_at: 2026-08-16
status: complete
---

# Extract TLS session keys from a memory image using structure identification, hooking, or memory-diffing techniques

## Summary

Because around 85% of internet traffic is now TLS-encrypted, an investigator examining captured network traffic (e.g. during malware or cybercrime analysis) frequently needs the corresponding TLS key material to decrypt it, and that key material is not present anywhere on disk by default -- it exists only in the memory of the client or server process during and after the TLS handshake. A range of complementary techniques, differing in whether they require a static memory dump or a live running process, and in how much prior knowledge of the target TLS library's internals they require, address this identification-and-extraction problem for TLS versions up to and including 1.2 (TLS 1.3's revised key hierarchy is comparatively unaddressed by existing methods -- see this technique's related weakness).

## Details

**Dead-forensics (memory-dump) approaches**: brute-force search (e.g. TLSkex) slides a candidate-master-secret-sized window across the entire dump, applying heuristics (4-byte alignment, expected bit-density range) to prune the search space, at the cost of being computationally intensive and effective only up to TLS 1.2 (where the master secret alone suffices to decrypt traffic); pattern matching searches for high-entropy byte regions characteristic of cryptographic key material, since keys are essentially random while surrounding code/data structures are not; structure identification (e.g. work by Anderson et al.) targets library-specific data structures (such as OpenSSL's `ssl_session_st`) known to store the master secret at a predictable offset, enabling a searchable regular-expression-style pattern that extracts all matching master secrets from a dump in seconds, with published structure offsets for OpenSSL, BoringSSL, NSS, and Schannel; debugging-based extraction parses TLS objects directly via a debugger when the target library was compiled with debug symbols, though this is impractical for most production deployments; commencement-based structure traversal (e.g. DroidKex for Android) computes, in a training phase, the exact stack-to-secret path from a known starting point (a hooked network function call) to the master secret's memory location, then reuses that path to extract secrets from any snapshot of the same application without repeating the training; and machine learning (e.g. work by Sentanoe et al.) predicts which memory-heap slices are likely to contain session keys based on learned entropy/structural features, still requiring a final brute-force pass to pinpoint exact key locations within the predicted slices. **Live-session approaches**: SSLKEYLOGFILE leverages a standard environment-variable-triggered logging feature supported by widely-used libraries (OpenSSL, NSS) to have the library itself write master secrets and client randoms to a file, though many library builds now disable this callback by default and it depends on runtime enablement; memory-diffing techniques (e.g. Caragea's method, or X-Ray-TLS) capture only the memory pages that changed ("dirty pages") during the handshake to substantially reduce dump size and search space, at some cost in generality across TLS versions/libraries; and function hooking intercepts specific TLS-library function calls at runtime -- either the key-derivation function itself (extracting the master secret and randoms directly from its arguments), or the `SSL_read`/`SSL_write` plaintext encryption/decryption functions (e.g. friTap), or the callback functions responsible for keylog-file writing -- with hooking-based approaches, particularly `SSL_read`/`SSL_write` hooking and TLS-keylogger-callback hooking, showing the broadest current support across both TLS 1.2 and TLS 1.3 and across multiple TLS libraries.

## Examples

- Anderson et al.'s structure-identification patent demonstrates extracting all OpenSSL master secrets from an entire memory dump in mere seconds using a searchable regular-expression pattern derived from the known `ssl_session_st` structure layout.
- DroidKex, evaluated across 86 Android applications, found that once a unique extraction path is identified for a given application during a training phase, it can subsequently be reused to extract master secrets during runtime in under 1 second per extraction, without needing to interrupt the target application's execution for more than a brief moment.
- friTap's `SSL_read`/`SSL_write` hooking approach, per the paper's own comparison table (Table 1), is one of only two hooking approaches evaluated as supporting both TLS 1.2 and TLS 1.3 across the widest range of TLS libraries tested (OpenSSL, BoringSSL, NSS, GnuTLS, wolfSSL, CoreTLS, Schannel, and others), in contrast to PRF-hooking or Choi-and-Lee-style key-derivation-function hooking, which are each limited to TLS 1.2 and a narrower library set.

## Related Objectives

- `DFO-1019` Detect anti-forensics and other anomalies
- `DFO-1017` Extract artifacts stored by the operating system

## Related Weaknesses

- [[weaknesses/TLS key material extraction techniques have little to no support for TLS 1.3's expanded key hierarchy]]

## References

- [LWCite-2114] Baier, Basse, Hilgert, and Lambertz, 2024, "TLS key material identification and extraction in memory: Current state and future challenges", FSI: Digital Investigation 49, 301766.
