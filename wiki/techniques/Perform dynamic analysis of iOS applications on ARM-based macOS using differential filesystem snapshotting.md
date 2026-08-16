---
id: DFT-2079
type: technique
name: Perform dynamic analysis of iOS applications on ARM-based macOS using differential filesystem snapshotting
description: Install and run an iOS application natively on an ARM-based Mac (leveraging Apple Silicon's ability to run iOS apps directly on macOS), and attribute the files it creates or modifies to specific user actions by taking a filesystem snapshot of the app's sandbox immediately before and after each recorded interaction, without needing a jailbroken or emulated iOS device.
objective_ids:
  - DFO-1011
  - DFO-1004
weakness_ids:
  - DFW-1090
aliases:
  - AppTap
source_refs:
  - DFCite-2095
updated_at: 2026-08-16
status: complete
---

# Perform dynamic analysis of iOS applications on ARM-based macOS using differential filesystem snapshotting

## Summary

Dynamic analysis of iOS applications has historically required a jailbroken device, but declining jailbreak availability against modern iOS versions makes this increasingly infeasible. Apple Silicon Macs can install and run many iOS App Store applications natively (since macOS emulates iOS device specifications for this purpose), giving an alternative dynamic-analysis platform: install a decrypted iOS app locally, drive its user interface with an automated-clicking tool, and difference successive filesystem snapshots of the app's sandbox directory to attribute each newly-created or modified artifact to the specific interaction that immediately preceded it.

## Details

The methodology has four stages. Platform setup requires downgrading the ARM Mac to an early enough macOS version (11.2.3 or earlier, in the reference implementation) that installing an IPA bundle still triggers automatic decryption, since macOS 11.3 and later restrict this capability to App-Store-authorized installs only. Application acquisition uses an existing IPA-download tool (ipatool) to pull the application bundle by its App Store identifier. Application analysis then follows a formalized checkpoint-based forensic framework: the analyst's own input to the app's UI is intercepted and withheld from the target application; a filesystem snapshot of the app's sandbox is taken and labeled with the intended action (in string form, e.g. "clicking on the send button"); the withheld input is then forwarded to the application, letting the intended action actually occur; this cycle repeats for each interaction of interest, and a differential comparison between consecutive snapshots (using a directory-comparison tool) reveals exactly which files were created or modified by that specific action. AppTap, an open-source tool, automates this entire pipeline -- acquiring the IPA, installing it, driving UI interaction via an automated-clicking library, and taking/labeling/diffing the sandbox snapshots -- letting an analyst attribute artifacts to actions without manually scripting each step.

## Examples

- A custom-built test iOS application ("NewList") was used to validate the methodology end to end: AppTap took a snapshot before and after an "AddingAnArtifact" interaction, and directory-comparison plus hex-level inspection of the resulting `.plist` file confirmed the newly-added string content was present only in the post-interaction snapshot, correctly attributing its creation to that specific interaction.
- Manual (non-automated) analysis using existing macOS forensic tools on iOS apps run this way successfully recovered chat messages and browsing history from popular applications (e.g. Firefox, Discord), extracted from SQLite databases stored within each app's sandbox using a database-file viewer.
- Evaluated against the top 100 free iPhone apps and top 100 free iPhone games from the US App Store, 92 (46%) installed and ran successfully; the largest single failure category (61 apps, 30.5%) was outright install refusal, primarily because many contemporary apps specify a minimum iOS version newer than the macOS 11.2.3-emulated iOS 14.4 the platform reports.

## Related Objectives

- `DFO-1011` Extract artifacts stored by applications
- `DFO-1004` Conduct research

## Related Weaknesses

- [[weaknesses/Argus-style dynamic file-system monitoring requires root or jailbreak access and loses continuity on device reboot]]
- [[weaknesses/Native ARM-Mac execution of iOS applications fails to install or run a substantial proportion of App Store applications]]

## References

- [DFCite-2095] Seiden, Webb, and Baggili, 2025, "Tapping .IPAs: An automated analysis of iPhone applications using apple silicon macs", FSI: Digital Investigation 52, 301871.
