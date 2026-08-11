---
id: DFT-1050
type: technique
name: Scenario-based memory acquisition tool quality assessment
description: Evaluate the quality and reliability of memory acquisition tools by running each through multiple concrete investigative scenarios (e.g., detecting a running process, an open network connection, an encryption key, or an opened file), measuring both whether the target artefact is retrievable and how internally consistent the acquired memory dump is (via kernel Virtual Address Descriptor and causal-relationship inconsistency checks), rather than relying on a single generic acquisition-speed or completeness benchmark.
objective_ids:
  - DFO-1004
weakness_ids:
  - DFW-1051
aliases: []
source_refs:
  - DFCite-1041
updated_at: 2026-08-09
status: complete
---

# Scenario-based memory acquisition tool quality assessment

## Summary

Because live memory acquisition unavoidably changes the very system being acquired, and different tools acquire memory pages in different orders and at different speeds, two dumps of the "same" system taken with different tools are not guaranteed to be equally forensically reliable. This technique measures that reliability concretely rather than assuming it, by pairing each tool with several realistic use-case scenarios and checking both artefact retrievability and internal data-structure consistency.

## Details

Each scenario evaluates a distinct artefact type relevant to law enforcement: a specific running process (structured analysis via a process-list plugin, unstructured via pool-tag scanning), an active network connection (structured via a connection-list plugin, unstructured via pool-tag scanning), an encryption key of a mounted encrypted volume (unstructured, scanning memory for high-entropy key-shaped candidates), and an opened file (unstructured, via a file-handle-scanning plugin). Two independent consistency metrics are computed per dump: VAD (Virtual Address Descriptor) inconsistencies, checking whether a process's memory-region tree is internally coherent, and causal inconsistencies, checking whether an artefact's supporting data structures are causally coherent with each other. A tool with a longer acquisition time was found to correlate with a higher number of both types of inconsistency, since more physical memory pages are likely to change while a slower acquisition is still in progress.

## Examples

- Across four tested tools (Belkasoft RAM Capturer, FTK Imager, Magnet RAM Capture, WinPmem) and four scenarios, no single tool ranked best on every scenario: the fastest-acquiring tools were generally most reliable for finding a running process or connection, but a slower, closed-source tool (Tool 3) was the only one able to reliably find the opened image file artefact (99/100 dumps) despite having the highest measured inconsistency rates overall.

## Related Objectives

- `DFO-1004` Conduct research

## Related Weaknesses

- [[weaknesses/No single memory acquisition tool is reliably best across all forensic artefact types]]

## References

- [DFCite-1041] Rzepka et al., 2025, "A scenario-based quality assessment of memory acquisition tools and its investigative implications", FSI: Digital Investigation 52.
