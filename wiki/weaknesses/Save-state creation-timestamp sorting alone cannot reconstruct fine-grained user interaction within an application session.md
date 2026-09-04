---
id: LWW-1111
type: weakness
name: Save-state creation-timestamp sorting alone cannot reconstruct fine-grained user interaction within an application session
description: Sorting save-state files by their creation timestamp only establishes a coarse window during which an application was used; it does not by itself reveal what the user did within each session, requiring deeper analysis of each save-state file's internal structure to reconstruct fine-grained interaction detail.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-1111
source_refs:
  - LWCite-1105
updated_at: 2026-08-12
status: complete
---

# Save-state creation-timestamp sorting alone cannot reconstruct fine-grained user interaction within an application session

## Summary

The authors identify this explicitly as unaddressed by their timestamp-sorting analysis and flag it as future work: "further information could be extracted by a more detailed analysis of such files. User actions could be reconstructed and visualized precisely over time by deriving a timeline from this data," noting that a Ren'Py `.sav` file is itself an archive containing a log file, a JSON file, a version file, and a screenshot of the saved game state — internal structure the coarse timestamp-sorting pass does not examine.

## Why It Matters

An investigator relying only on save-state creation-timestamp sorting can establish that an application was used during a given period and estimate overall duration, but cannot without further work characterize what specifically occurred during each session (e.g. which in-application content was reached, in what order, or how much active interaction occurred versus idle time) — a distinction that can matter when the specific content consumed, not merely the usage window, is evidentially significant.

## Related Mitigations

- [[mitigations/Perform deeper save-state internal-structure analysis to reconstruct fine-grained user interaction timelines]]

## Used By

- [[techniques/Reconstruct application usage timeline from save-state file timestamps]]

## References

- [LWCite-1105] Jaeckel and Labudde, 2026, "Case note: Digital forensic challenges through synthetic CSAM in video games", FSI: Digital Investigation 57.
