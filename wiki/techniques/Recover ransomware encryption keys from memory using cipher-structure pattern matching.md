---
id: LWT-1180
type: technique
name: Recover ransomware encryption keys from memory using cipher-structure pattern matching
description: Identify and extract a stream cipher's key and nonce from a live memory capture by searching for the cipher algorithm's own fixed constant byte pattern (rather than a target-application-specific marker), then use the recovered key/nonce pairs to decrypt ransomware-encrypted victim files without needing the attacker's master key.
objective_ids:
  - DFO-1016
weakness_ids:
  - LWW-1020
aliases:
  - Salsa20 key/nonce extraction from memory
  - Salsa20 initialization-matrix identification
source_refs:
  - LWCite-1191
updated_at: 2026-08-13
status: complete
---

# Recover ransomware encryption keys from memory using cipher-structure pattern matching

## Summary

Current ransomware increasingly uses the fast stream cipher Salsa20 (or its variant ChaCha20), often with a distinct key and nonce generated per victim file, wrapped in a hybrid scheme whose asymmetric private key never appears on the victim machine. Because Salsa20's internal 64-byte initialization matrix contains four fixed 4-byte constant values at known offsets regardless of the key in use, a memory dump can be scanned for that constant pattern to locate and extract every key/nonce pair present at capture time, then used directly to decrypt the corresponding encrypted files.

## Details

Salsa20 organizes its key, nonce, block-counter, and four constant words into a fixed 4x4 array layout; the ASCII constants `expa`, `nd 3`, `2-by`, and `te k` (little-endian hex `0x65787061`, `0x6e642033`, `0x322d6279`, `0x7465206b`) always occupy the same byte offsets (1, 21, 41, 61) within the 64-byte matrix regardless of the actual key value, making the matrix reliably locatable by direct byte-pattern search across binary memory-dump formats (`.dmp`, `.vmem`, `.core`). Unlike block ciphers such as AES/RSA, whose key material can be located via key-schedule or entropy-based heuristics, no prior published method could identify Salsa20 keys in memory before this technique. Once a candidate matrix is found, the embedded 32-byte key and 8-byte nonce are extracted directly from their fixed positions within it and applied to decrypt the file(s) associated with that key/nonce pair, without needing the ransomware's master (asymmetric) private key at all. Because modern ransomware often generates a unique key/nonce per victim file, recovering a useful fraction of victim files requires repeated memory captures across the ransomware's execution window, since each file's key exists in memory only briefly around the time that file is encrypted.

## Examples

- Against a synthetic Salsa20-encrypting program, the extraction tool located and validated 100% of the generated key/nonce pairs from a single memory snapshot.
- Against a real-world Sodinokibi ransomware sample (which uses complex multilevel hybrid cryptography protecting per-file Salsa20 keys with an asymmetric public key never present in decryptable form on the victim machine), periodic memory captures during encryption of a 4,000-file NapierOne mixed dataset recovered over 90% of the Salsa20 key/nonce pairs, each independently validated by successfully decrypting its corresponding victim file.

## Related Objectives

- `DFO-1016` Overcome protection mechanisms

## Related Weaknesses

- [[weaknesses/In-memory credential recovery fails once the relevant memory page is overwritten]]

## References

- [LWCite-1191] Fernandez de Loaysa Babiano, Macfarlane and Davies, 2023, "Evaluation of live forensic techniques, towards Salsa20-Based cryptographic ransomware mitigation", FSI: Digital Investigation 46, 301572.
