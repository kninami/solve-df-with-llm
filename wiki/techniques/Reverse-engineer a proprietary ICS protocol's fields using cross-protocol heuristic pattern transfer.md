---
id: LWT-1292
type: technique
name: Reverse-engineer a proprietary ICS protocol's fields using cross-protocol heuristic pattern transfer
description: Identify the meaning and location of message fields (function code, message length, PLC memory address, session/transaction ID, checksum) in an unfamiliar proprietary industrial control system (ICS) protocol's captured network traffic by applying heuristics — rolling-window, vertical-window, and frequency-table analysis — built from an analyst's knowledge of a different, already-understood ICS protocol, on the hypothesis that ICS protocols share substantially overlapping field conventions due to their common underlying functions.
objective_ids:
  - DFO-1002
weakness_ids:
  - LWW-1302
aliases:
  - PREE (Protocol Reverse Engineering Engine)
source_refs:
  - LWCite-1337
updated_at: 2026-08-15
status: complete
---

# Reverse-engineer a proprietary ICS protocol's fields using cross-protocol heuristic pattern transfer

## Summary

Investigating an ICS cyberattack often requires interpreting proprietary, undocumented protocol traffic between a control center and field-site PLCs, but existing reverse-engineering approaches (tedious manual analysis, complex binary analysis, or generic pre-built network-traffic-analysis tools) do not scale well to the proliferation of vendor-specific protocols in modern heterogeneous ICS networks. PREE's central hypothesis is that because ICS protocols share substantially overlapping functionality — uploading/downloading control logic to a PLC, reading/writing memory, reporting status — they also share standard field types (function code, PLC memory address, and similar), so heuristics an analyst builds from their existing knowledge of one protocol can be applied to identify the corresponding fields in a different, unfamiliar proprietary protocol.

## Details

PREE provides a data-analytics layer of message-level functions (find similarity/difference between two messages, search for a byte sequence, generate all substrings of a message) and session-level functions (find the longest common substring across messages, build a per-index byte-frequency table across a capture, find messages/indices matching a frequency threshold) that a control engineer with ICS protocol knowledge combines into custom field-identification heuristics. Three underlying techniques were used to build eight heuristic variants for finding "variable fields" (fields like Transaction ID, Length, CRC, and Session ID whose values change per-message in protocol-specific ways): the **rolling window** technique slides windows of varying byte-widths across a message and applies a user-defined function (e.g. computing a length or checksum) to each substring, flagging a location as a potential field only when the computed value matches consistently across multiple similar messages (minimizing false positives from a single coincidental match); **vertical window** and **frequency table** techniques instead analyze byte value/position statistics across an entire session of captured messages. The resulting heuristics were tested on six ICS protocols (Modbus TCP, UMAS, ENIP, Omron FINS, CLICK, PCCC) across five PLCs from four vendors, and PREE was shown to outperform existing reverse-engineering tools (NetPlier, Netzob, Discoverer) on accuracy, conciseness, completeness, and consistency of the identified fields.

## Examples

- PREE successfully identified common fields across the six tested protocols — function code, message type, message length, PLC memory address, data size, and session/transaction IDs — using heuristics that did not need to be redeveloped from scratch for each new protocol.
- A vulnerability study applying PREE-derived protocol knowledge to a CLICK Koyo PLC produced SNORT intrusion-detection rules capable of investigating and discovering several classes of attack on that PLC, demonstrating a direct forensic/security application of the reverse-engineered field knowledge beyond passive traffic interpretation.

## Related Objectives

- `DFO-1002` Extract data from specific formats

## Related Weaknesses

- [[weaknesses/Cross-protocol heuristic transfer cannot identify an ICS protocol field with no analog in any previously-known protocol]]

## References

- [LWCite-1337] Qasim, Jo, and Ahmed, 2023, "PREE: Heuristic builder for reverse engineering of network protocols in industrial control systems", FSI: Digital Investigation 45, 301565.
