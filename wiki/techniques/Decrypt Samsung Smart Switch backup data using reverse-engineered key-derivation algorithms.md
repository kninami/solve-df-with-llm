---
id: LWT-1266
type: technique
name: Decrypt Samsung Smart Switch backup data using reverse-engineered key-derivation algorithms
description: Recover the plaintext contents of a Samsung Smart Switch PC/Mac backup by combining static analysis (decompiling the mobile APK and PC/Mac binaries to identify each backup file category's encryption function and key-derivation algorithm) with dynamic analysis (tracing actual runtime parameter values during a live backup) to reconstruct the exact per-file-type decryption algorithm and, where the backup was PIN-protected, brute-force the user's PIN using the recovered key-derivation function.
objective_ids:
  - DFO-1018
  - DFO-1016
weakness_ids:
  - LWW-1277
aliases:
  - Smart Switch backup decryption
source_refs:
  - LWCite-1305
updated_at: 2026-08-14
status: complete
---

# Decrypt Samsung Smart Switch backup data using reverse-engineered key-derivation algorithms

## Summary

Samsung's Smart Switch backup program encrypts different categories of backed-up smartphone data (contacts, messages, application data, settings) using up to nine distinct key-derivation-and-encryption algorithm combinations depending on the file type and whether the user chose a PIN-protected or basic (fixed-key) backup, so no single decryption routine works across an entire backup — each file category must be individually classified and matched to its correct algorithm before it can be decrypted.

## Details

Static analysis decompiles the mobile Smart Switch APK (via JEB Decompiler) and the PC/Mac Smart Switch binaries (via IDA Pro on Windows, Hopper Disassembler on macOS) to locate each encryption call site, using the program's use of Java's standard cryptographic provider (`getInstance()` calls revealing the specific algorithm and mode used) as a starting point for Android, and the fact that most PC/Mac library source is open to narrow down encryption entry points; because static analysis alone cannot reveal the actual runtime parameter values (keys, salts, IVs) used at each call site, dynamic analysis (via x64dbg on Windows, Hopper's debugger on macOS) traces live memory and register values during an actual backup operation to recover the concrete key-derivation inputs. Once each file type's decryption algorithm and key-derivation chain is known, decryption proceeds in three steps: acquiring a "dummy" value from the backup's own metadata file (itself decrypted using a fixed key) that seeds all further key derivation; determining the backup type (PIN-based or basic) and, if PIN-based and the PIN is unknown, recovering it via a brute-force search using the recovered PBKDF2-HMAC-SHA1-based PIN-verification algorithm; and finally decrypting each backup file using its file-type-specific algorithm (decompressing first where the file is also compressed, since encryption and compression are sometimes layered).

## Examples

- Reverse-engineering the latest analyzed version (4.2.21,023 for Windows, 4.3.1.21022_5 for macOS, the first published analysis of Smart Switch in the macOS environment) identified nine distinct key-derivation/encryption algorithm pairings, two of which were entirely new since the previously published analysis of an earlier version, and successfully decrypted all backup file categories in both operating-system environments.
- Benchmarking the recovered PBKDF2-HMAC-SHA1 (1000-iteration) PIN-verification algorithm against consumer and enterprise GPU hardware found a single Nvidia RTX 3090 could brute-force a 10-digit PIN in about 1,082 seconds, while a full 16-digit PIN would take roughly one year on a single RTX 3090 but could be completed within a realistic one-month timeframe using 418 parallel RTX 3090 units (or comparable counts of other tested GPU models).

## Related Objectives

- `DFO-1018` Read data from digital evidence storage formats
- `DFO-1016` Overcome protection mechanisms

## Related Weaknesses

- [[weaknesses/Samsung Smart Switch backup encryption changes across app versions, breaking previously built decryption tools]]

## References

- [LWCite-1305] Kang, Kim, Park and Kim, 2021, "Methods for decrypting the data encrypted by the latest Samsung smartphone backup programs in Windows and macOS", FSI: Digital Investigation 39, 301310.
