---
id: LWT-1106
type: technique
name: Reconstruct application usage timeline from save-state file timestamps
description: Locate an application's per-session save-state files in its OS-standard data directory and sort them by creation timestamp to reconstruct the specific time period during which the application was actively used, providing evidence of consumption rather than mere possession.
objective_ids:
  - DFO-1001
weakness_ids:
  - LWW-1111
aliases:
  - RenPy save-state timestamp analysis
source_refs:
  - LWCite-1105
updated_at: 2026-08-12
status: complete
---

# Reconstruct application usage timeline from save-state file timestamps

## Summary

Many applications persist a per-session or per-save-slot state file each time a user saves progress, and these files are typically written to a predictable, OS-standard local user-data directory rather than alongside the application itself. Recovering and sorting these files by creation time reconstructs when the application was actually used, which is stronger evidence of consumption than the mere presence of the application's installation files.

## Details

In the source case, the Ren'Py game engine was found to create a per-game subdirectory (named after the game) under the local user directory at `%USERPROFILE%/AppData/Roaming/RenPy`, containing multiple `.sav` files recording each saved game state, written automatically by the engine when the game state was saved. A recursive search in X-Ways Forensics located this directory even though the corresponding game archives had only been found in compiled, downloaded form (not unzipped), which by itself would not prove the games had been run. Sorting the recovered `.sav` files by creation time reconstructed the exact time period over which each game had been played, supporting a conclusion of active consumption (playing time and preference) rather than only possession, since no save-state files with timestamps would exist had the games never been started.

## Examples

- Recursive directory search under `%USERPROFILE%/AppData/Roaming/RenPy` recovered per-game save-state (`.sav`) subdirectories; sorting these by X-Ways-reported creation time reconstructed the specific period during which each synthetic-CSAM visual novel was played, supporting a finding of active consumption.

## Related Objectives

- `DFO-1001` Reconstruct events

## Related Weaknesses

- [[weaknesses/Save-state creation-timestamp sorting alone cannot reconstruct fine-grained user interaction within an application session]]

## References

- [LWCite-1105] Jaeckel and Labudde, 2026, "Case note: Digital forensic challenges through synthetic CSAM in video games", FSI: Digital Investigation 57.
