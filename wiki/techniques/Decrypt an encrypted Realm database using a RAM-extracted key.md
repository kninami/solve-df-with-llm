---
id: DFT-1243
type: technique
name: Decrypt an encrypted Realm database using a RAM-extracted key
description: Recover a mobile app's AES-encrypted Realm database key by searching a live process memory dump for the key string (e.g. via fridump3), converting it to its required hexadecimal form, and using it to open the encrypted .realm file directly in a Realm-aware viewer such as Realm Studio.
objective_ids:
  - DFO-1018
weakness_ids:
  - DFW-1020
aliases:
  - RAM-based Realm database decryption
source_refs:
  - DFCite-1280
updated_at: 2026-08-14
status: complete
---

# Decrypt an encrypted Realm database using a RAM-extracted key

## Summary

Several mobile apps store local data in the Realm database format, which some apps additionally encrypt with a 64-byte key; because that key must be held in the app's process memory to decrypt the database at runtime, dumping the app's RAM while it is running and searching the dump for the key string recovers it without needing the app's source code or any vendor cooperation.

## Details

While the target app is running and logged in (or in a guest/visitor mode that still mounts an encrypted local database), the examiner dumps the app's process memory using a tool such as fridump3, then searches the resulting output for a string adjacent to the known encrypted database's file path — the key is typically stored as a long alphanumeric string near a reference to the corresponding `.realm` file within the dumped memory. Because Realm Studio and similar viewers expect the key in 128-character hexadecimal form rather than the 64-byte string as captured, a hex-conversion step (e.g. via CyberChef) is needed before the key can be supplied to the viewer to open and browse the database's contents. As with any RAM-based key recovery, this only works while the key remains resident in memory; a database created for an account the app user has since logged out of may no longer be openable via this route even though the encrypted file itself remains on disk, since some apps discard the corresponding realm file (or leave it undeletable without the now-unrecoverable key) on logout. Once a Realm database is decrypted (or found to be unencrypted in the first place), deleted records within it can be separately recovered via [[techniques/Recover deleted Realm database records using table, column, and field-unit node analysis]], since decryption and deleted-data recovery address two independent obstacles.

## Examples

- HIKVISION's "Hik-Connect" companion app (Android) encrypts one of its two local Realm databases (`devmgr.user-ID{5}.sec.realm`, storing CCTV system connection details and sharing status) with a 64-byte key; dumping the app's RAM with fridump3 and searching the output located the key adjacent to a reference to the `.sec.realm` file, and converting it to hexadecimal via CyberChef allowed the database to be opened and browsed in Realm Studio. The app's second Realm database (`hc.realm`, storing connected WiFi network history) was left unencrypted by the app and required no key recovery at all.

## Related Objectives

- `DFO-1018` Read data from digital evidence storage formats

## Related Weaknesses

- [[weaknesses/In-memory credential recovery fails once the relevant memory page is overwritten]]

## References

- [DFCite-1280] Dragonas, Lambrinoudakis and Kotsis, 2023, "IoT forensics: Analysis of a HIKVISION's mobile app", DFRWS 2023 USA; FSI: Digital Investigation 45, 301560.
