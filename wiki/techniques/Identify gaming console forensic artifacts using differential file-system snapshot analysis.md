---
id: DFT-2122
type: technique
name: Identify gaming console forensic artifacts using differential file-system snapshot analysis
description: Systematically discover which files a gaming console's operating system and platform client create, delete, or modify for a given user action by imaging the device's storage before and after each of a sequence of scripted actions and computing the file-system differences between successive images.
objective_ids:
  - DFO-1017
  - DFO-1011
weakness_ids:
  - DFW-2131
aliases:
  - Steam Deck Analyzer
  - idifference2.py-based differential forensic analysis
source_refs:
  - DFCite-2151
updated_at: 2026-08-16
status: complete
---

# Identify gaming console forensic artifacts using differential file-system snapshot analysis

## Summary

Rather than manually and exploratively searching a gaming console's file system for artifacts, define a sequence of representative user action sets (e.g., first login, installing and playing a game, adding a friend, using text/voice chat, factory reset), take a full bitwise image of the device's internal storage before and after each action set, and compute the per-file differences (created, deleted, content-modified, or timestamp-only-modified) between each pair of consecutive images to isolate exactly which files each action affects.

## Details

Differential analysis tooling (e.g., `idifference2.py` from the DFXML toolset) parses two file-system images and reports every file path affected by a change, categorized by change type. Because a single action set can affect a very large number of unrelated file paths (system logging, caches, package-manager metadata), a filter list excluding files/directories not plausibly related to the tested action set substantially reduces the number of paths requiring manual review. Findings are then compiled into a device- and platform-specific artifact catalog (file paths and their forensic meaning) and can be operationalized as automated extraction plugins for a forensic platform such as Autopsy, categorized by artifact type (e.g., boot/partition state, device identity, Wi-Fi credentials, user accounts, installed games/apps, screenshots, friends list, in-app wallet/purchase traces, activity logs, factory-reset indicators).

## Examples

- Applied to Valve's Steam Deck (SteamOS 3.0/"holo") across 10 sequential action sets, this yielded a documented catalog of file paths for Wi-Fi credentials, Steam account/login artifacts, installed-game state, screenshot metadata, friends-list history, in-app-wallet purchase traces (via WebView cache artifacts), and activity logs, operationalized as the "Steam Deck Analyzer" Autopsy plugin collection and validated against a second, independently generated device image.

## Related Objectives

- `DFO-1017` Extract artifacts stored by the operating system
- `DFO-1011` Extract artifacts stored by applications

## Related Weaknesses

- [[weaknesses/Gaming console chat and voice communication content is not stored locally, only remotely with limited retention]]

## References

- [DFCite-2151] Eichhorn et al., 2024, "Well Played, Suspect! - Forensic examination of the handheld gaming console 'Steam Deck'", FSI: Digital Investigation 48.
