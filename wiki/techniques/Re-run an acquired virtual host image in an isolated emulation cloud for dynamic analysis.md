---
id: DFT-1117
type: technique
name: Re-run an acquired virtual host image in an isolated emulation cloud for dynamic analysis
description: Load a preserved virtual host image or snapshot into cloud compute resources provisioned specifically as an isolated emulation environment and boot it, reconstructing the target's live running state so that run-time behavior — active processes, network interactions, and other dynamic activity never captured by static log or file analysis — can be directly observed and analyzed, complementing static analysis of the stored image files.
objective_ids:
  - DFO-1001
weakness_ids:
  - DFW-1122
aliases:
  - CETS emulation procedure
  - Cloud virtual host emulation for run-time forensic analysis
source_refs:
  - DFCite-1116
updated_at: 2026-08-12
status: complete
---

# Re-run an acquired virtual host image in an isolated emulation cloud for dynamic analysis

## Summary

Static analysis of an acquired virtual host image can only recover what was written to disk — system logs, database contents, configuration files — and cannot reveal system-process behavior, network interactions, or other dynamic activity that was never persisted. Loading the preserved image into dedicated emulation-cloud compute resources and booting it reconstructs the host's actual running state, enabling run-time (dynamic) analysis alongside static analysis of the same evidence.

## Details

The emulation procedure sits between acquisition/preservation and investigative analysis in the forensic workflow: an investigator requests virtual resources from a dedicated emulation cloud (kept separate from the preservation cloud holding the verified original images) and loads a chosen image or snapshot version into it, examining, planning, and reconstructing the relevant past state before rerunning it. Investigative analysis is then explicitly split into two types operating on the same evidence: static analysis of the stored image files (recovering database contents, system logs, and other on-disk data), and run-time analysis of the emulated, running VM (observing process behavior, network interactions, and other dynamic behavior that static analysis alone cannot surface). Because the emulation cloud can be built from the same range of CSP-agnostic compute resources used for acquisition and preservation, and because a case's images/snapshots are already indexed in the file-traceability database, an investigator can provision, use, and tear down emulation resources on demand — supporting multiple concurrent cases and resuming a halted investigation at any point.

## Examples

- In a case investigating an illegal online platform, the seized virtual host's preserved image was loaded into the emulation cloud and rerun so investigators could directly observe the running service's process and network behavior, supplementing the static-file analysis of its stored system and application logs.

## Related Objectives

- `DFO-1001` Reconstruct events

## Related Weaknesses

- [[weaknesses/API-based cloud host acquisition depends on cooperative authorization from the target owner or CSP]]

## References

- [DFCite-1116] Wu et al., 2022, "Cloud Evidence Tracing System: An integrated forensics investigation system for large-scale public cloud platform", FSI: Digital Investigation 41.
