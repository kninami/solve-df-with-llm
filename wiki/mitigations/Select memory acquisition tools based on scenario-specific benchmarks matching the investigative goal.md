---
id: LWM-1051
type: mitigation
name: Select memory acquisition tools based on scenario-specific benchmarks matching the investigative goal
source_refs:
  - LWCite-1041
updated_at: 2026-08-09
status: complete
---

# Select memory acquisition tools based on scenario-specific benchmarks matching the investigative goal

## Summary

Choose a memory acquisition tool based on benchmarking data for the specific type of artefact the investigation needs to recover, rather than a single overall quality ranking, and consider using multiple tools when the investigative goal spans several artefact types.

## Addresses

- [[weaknesses/No single memory acquisition tool is reliably best across all forensic artefact types]]

## How To Apply

Before selecting an acquisition tool, identify the specific artefact type(s) most central to the investigative question (e.g., a running process, network connection, encryption key, or opened file), and consult scenario-specific quality benchmarking data for that artefact type rather than a tool's general reputation or speed. Where the investigative goal spans multiple artefact types and no single tool performs best across all of them, consider dual-tool acquisition (as international/legal validation standards for forensic testing already recommend) to cover the gap, and document which tool was selected and why for each specific artefact type sought.

## References

- [LWCite-1041] Rzepka et al., 2025, "A scenario-based quality assessment of memory acquisition tools and its investigative implications", FSI: Digital Investigation 52.
