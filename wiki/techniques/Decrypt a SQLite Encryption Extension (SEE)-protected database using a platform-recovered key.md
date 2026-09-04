---
id: LWT-1195
type: technique
name: Decrypt a SQLite Encryption Extension (SEE)-protected database using a platform-recovered key
description: Decrypt a SQLite database protected with the paid, previously-undisclosed SQLite Encryption Extension (SEE) by recovering its DB key from the host OS's platform key-protection store, then decrypting each page of the database individually with AES-256-OFB using page-size and nonce values read from the database's own plaintext header bytes.
objective_ids:
  - DFO-1018
weakness_ids:
  - LWW-1158
aliases:
  - SEE database decryption
  - Webex SEE-AES-256-OFB database decryption
source_refs:
  - LWCite-1217
updated_at: 2026-08-13
status: complete
---

# Decrypt a SQLite Encryption Extension (SEE)-protected database using a platform-recovered key

## Summary

Unlike SQLCipher and wxSQLCipher, whose encryption mechanisms are open-source and well-documented, SEE is provided commercially with its detailed encryption/decryption mechanism undisclosed; this technique reconstructs that mechanism (AES-256-OFB applied per database page, with page size and nonce derived from an unencrypted header region) and applies it once the database's DB key has been separately obtained from the host OS's own key-protection API.

## Details

A SEE-encrypted SQLite database is identifiable by checking bytes at header offsets 16-23, which SEE deliberately leaves in plaintext even though the rest of the file is encrypted: bytes 16-18 give the database's page size and byte 20 gives the number of unused bytes at the end of each page, which is used as the AES-OFB nonce for that page. Decryption proceeds page-by-page: for each page, the last 8 bytes (the unused/nonce region) are read as the nonce, and the remaining bytes of that page are decrypted with AES-256-OFB using the recovered DB key and that nonce, with the original 24-byte SQLite file header restored at the start of the output so the result opens as a standard, tool-readable SQLite database (e.g. in DB Browser for SQLite). The DB key itself is protected by whichever key-protection API the host OS provides (Windows DPAPI, macOS/iOS Keychain, Android KeyStore); see [[weaknesses/Platform-protected app database decryption fails without access to the original device's account key material]] for how that key is recovered per platform. Because this decryption method targets SEE's page-based cipher structure directly rather than any application-specific detail, it generalizes to any application that uses SEE for its local SQLite storage, not just the Webex application it was originally demonstrated against.

## Examples

- Cisco Webex (Hur et al., 2023): decrypting all four of Webex's SEE-protected databases (`spark_persistent_store.db`, `spark_roaming_store.db`, `Webex_pre_login_store.db`, on Windows, macOS, iOS, and Android) recovered chat/calendar/profile data, credential tokens, and login history that had previously only been analyzable via memory or network-traffic analysis.

## Related Objectives

- `DFO-1018` Read data from digital evidence storage formats

## Related Weaknesses

- [[weaknesses/Platform-protected app database decryption fails without access to the original device's account key material]]

## References

- [LWCite-1217] Hur et al., 2023, "Forensic analysis for multi-platform Cisco Webex", FSI: Digital Investigation 47, 301659.
