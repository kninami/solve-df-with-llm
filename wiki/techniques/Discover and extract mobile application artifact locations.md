---
id: DFT-1067
type: technique
name: Discover and extract mobile application artifact locations
description: Locate and extract a mobile application's forensically relevant files, even for apps not yet supported by commercial forensic tools, using two complementary approaches — dynamically discovering exactly which files an app action creates, modifies, or deletes by diffing file-system metadata snapshots taken before and after that action on a physical or emulated device, and/or applying a manually- or dynamically-derived wordlist of known filenames and paths to extract matching artifacts automatically across a batch of device images.
objective_ids:
  - DFO-1012
  - DFO-1011
weakness_ids:
  - DFW-1072
  - DFW-1090
aliases:
  - Mobile application artifact location discovery and extraction
  - ASNAAT
  - Argus
source_refs:
  - DFCite-1062
  - DFCite-1082
updated_at: 2026-08-10
status: complete
---

# Discover and extract mobile application artifact locations

## Summary

Commercial forensic tools mostly support widely-used apps, leaving country-specific or niche apps under-documented and difficult to analyze under time pressure. Two complementary techniques address this: dynamically discovering an app's artifact locations by diffing file-system snapshots around a specific action, and then encoding that knowledge (or knowledge from prior manual analysis) as a wordlist that can be applied automatically at scale to extract matching artifacts from a batch of device images.

## Details

**Dynamic discovery (Argus)**: monitors the file system on a physical or emulated Android/iOS device, diffing metadata snapshots taken before and after performing a specific action (e.g. using a particular app feature) to quickly narrow down exactly which files that action touched. Results can optionally be published to a shared forensic artifacts reference database (Aardwolf) so other investigators benefit from previously-run experiments without repeating them. Validated against artifact locations already documented in prior published literature (e.g. WhatsApp, Calculator-based hide apps), Argus successfully identified matching file paths in the great majority of tested cases.

**Wordlist-driven extraction (ASNAAT)**: takes a tar-archived forensic image of an Android or iOS device and, using a per-application wordlist of known filenames and paths (built from prior manual analysis, or from a tool like Argus), extracts artifacts such as SQLite databases, XML files, and cache-directory files at the known paths, run automatically across a batch of imaged devices/apps. Applied to nine alternative-tech social networking applications (Parler, MeWe, CloutHub, Wimkin, Minds, Minds Chat, SafeChat, 2nd1st, GETTR) across Android and iOS, this recovered usernames, emails, phone numbers, profile pictures, posts, comments, and private messages, and in the course of testing also surfaced application-side authorization vulnerabilities (some private content could be downloaded without authentication).

## Examples

- Running an Argus experiment on a "Calculator - Hide" app (which conceals photos and text files behind a calculator interface) correctly identified the artifact locations for storing and deleting hidden pictures and text files, matching locations independently documented in prior literature.
- ASNAAT recovered unencrypted user information and private chat messages from several of the nine tested alt-tech applications' known SQLite and cache file locations.

## Related Objectives

- `DFO-1012` Locate potentially relevant content
- `DFO-1011` Extract artifacts stored by applications

## Related Weaknesses

- [[weaknesses/Application version updates can eliminate or relocate artifacts targeted by wordlist-based known-path extraction]]
- [[weaknesses/Argus-style dynamic file-system monitoring requires root or jailbreak access and loses continuity on device reboot]]

## References

- [DFCite-1062] Johnson et al., 2022, "Alt-tech social forensics: Forensic analysis of alternative social networking applications", FSI: Digital Investigation 42.
- [DFCite-1082] Boztas et al., 2025, "Argus: A new approach for forensic analysis of apps on mobile devices", FSI: Digital Investigation 53.
