---
id: LWT-2063
type: technique
name: Recover hidden photos from an iOS vault application's residual artifacts
description: Recover photos a user has hidden inside an iOS "vault" or photo-vault application by examining residual artifacts the app leaves behind outside its own password-protected view — thumbnails, embedded SQLite database BLOBs, duplicate image copies, custom-extension preview files, and camera-roll live-preview videos — rather than trying to defeat the vault's own password/authentication mechanism.
objective_ids:
  - DFO-1011
weakness_ids:
  - LWW-2063
aliases:
  - iOS photo vault forensic recovery
source_refs:
  - LWCite-2066
updated_at: 2026-08-15
status: complete
---

# Recover hidden photos from an iOS vault application's residual artifacts

## Summary

iOS vault applications advertise that they securely conceal a user's private photos behind a password, PIN, or disguised app icon. In practice, most of the tested vault apps store additional, unprotected copies of the same images elsewhere on the device — as thumbnails, database-embedded BLOBs, duplicate files with modified names/extensions, or camera-generated preview videos — that a standard mobile forensic tool can recover without ever needing the vault's own password.

## Details

A basic imaging processor can reveal a "hidden" photo as a readable object even when the app's own view requires authentication, because most vault apps do not encrypt every copy they create of an imported photo: copying a sensitive photo into the vault for in-app viewing frequently generates additional forensic evidence (e.g., a custom-extension thumbnail file, a duplicate `.png` copy, or an app-specific SQLite database storing the image as an embedded BLOB in a `ZPHOTO`/`ZTHUMBNAIL`-style column) rather than reducing it, and a live-preview `.mov` video is separately created by iOS's camera app itself whenever a photo is captured directly through the vault app's in-app camera. Some apps additionally leave their own unlock PIN recoverable in plaintext by a forensic tool even when the PIN is not visible in the file names or database it uses to store hidden images. Because acquisition and parsing support for these artifacts varies by forensic toolkit, this technique is most effective combined with [[techniques/Assess and design for digital forensic readiness]]-style multi-tool acquisition rather than a single tool's output (see the related mitigation on cross-validating with multiple toolkits).

## Examples

- Testing five popular App-Store vault apps (KeepSafe, Photo Vault/"enchanted cloud", Calculator+/"secret Calculator", Secret Safe/"loveyouchenapp", and Purple photo vault/"galaxy studio") on an iOS 11.3 iPhone SE found that every app left recoverable evidence: KeepSafe left `.thumb`-extension thumbnails; Photo Vault created a `.mov` live-preview video and a same-format duplicate jpeg thumbnail without a distinguishing extension; Calculator+ stored each private photo as an SQLite `Store.sqlite` BLOB entry (`ZPHOTO`/`ZTHUMBNAIL` columns) using a non-`.thumb` custom filename (`...ZTHUMBNAIL`) specifically to evade tools that only recognize the standard thumbnail extension; and Secret Safe stored images under randomly-generated UUID-style filenames with a `_110`-suffixed thumbnail variant.
- Cellebrite Physical Analyzer recovered Private Photo Vault's four-digit unlock PIN in plaintext during acquisition and it was independently verified as the correct PIN to unlock the app, despite the PIN not being visible in any of the app's own image-storage artifacts.

## Related Objectives

- `DFO-1011` Extract artifacts stored by applications

## Related Weaknesses

- [[weaknesses/Forensic toolkit completeness in recovering iOS vault-app hidden photos varies unpredictably by app and tool]]

## References

- [LWCite-2066] Gilbert & Seigfried-Spellar, 2022, "Forensic Discoverability of iOS Vault Applications", JDFSL 17(1). Source of the five-vault-app comparative study, its per-app residual-artifact findings, and the recovered-PIN case.
