---
id: DFT-1265
type: technique
name: Reverse-engineer a PLC's memory dump to extract control-logic, IO states, and logs using differential analysis
description: Recover a programmable logic controller's running control-logic program, physical/logical I/O tag states, firmware, configuration data, and operational event logs from an otherwise-undocumented raw memory dump, by iteratively reprogramming a same-model test PLC with a series of designed test cases and observing the resulting memory changes to reverse-engineer each internal data structure's format before formalizing the findings into a reusable extraction rule set.
objective_ids:
  - DFO-1018
weakness_ids:
  - DFW-1276
aliases:
  - PLC memory analysis profile methodology
source_refs:
  - DFCite-1304
updated_at: 2026-08-14
status: complete
---

# Reverse-engineer a PLC's memory dump to extract control-logic, IO states, and logs using differential analysis

## Summary

Because PLC vendors do not publish memory-layout documentation and each model's proprietary hardware, firmware, and control-application format is potentially unique, a raw PLC memory dump (however it was acquired — see [[techniques/Acquire a PLC's memory contents using a JTAG acquisition profile]]) is not directly interpretable without first reverse-engineering the vendor's internal data structures; dynamic differential analysis — setting a unique, recognizable pattern via the vendor's own engineering software, dumping memory, and comparing successive dumps to localize where and how that pattern's data structure is represented — builds this understanding empirically without needing firmware disassembly, and the resulting understanding is formalized into a reusable "memory analysis profile" applicable to every controller of the same model.

## Details

The methodology proceeds through five stages: exploring the vendor's engineering/control software to understand project organization (task/program/routine/rung hierarchy), named-structure conventions, unique I/O bit-pattern configuration options, and available logs and configuration settings; generating a graduated series of test cases (from a minimal single-instruction project up to multiple programs/routines/rungs) and acquiring a memory dump after each; identifying each named or targeted data structure's definition by locating its configured name string in the dump and analyzing the surrounding bytes for structural boundary markers, forward/reverse pointer links, and length fields (e.g. the general-purpose 40-byte "Asg_DT" assignment structure used for every task, program, routine, and physical/logical I/O tag, found reliably bounded by a fixed `80 00 00 0A` start/end marker); identifying instances of each defined structure in an unknown dump by walking the discovered pointer chains and boundary markers (list-walking, preferred over pure data-carving since a walk that reaches the same destination through multiple paths cross-validates the walk's reliability, with data-carving reserved as a fallback for stale/de-linked historical data list-walking cannot reach); and formalizing the resulting knowledge into a verified rule set, packaged as a reusable Python library, that a subsequent examiner can apply directly against a same-model controller's memory dump without repeating the reverse-engineering process.

## Examples

- Applying the finalized profile to an unknown test dump correctly reconstructed the exact control-logic (programs, routines, rungs, instructions, and tag operands) shown in the engineering software's own project view, and separately located a decoy attacker's machine name and username (`I-AM-ATTACKER\unsafe`) recorded in the controller's licensing/connection metadata, differing from the expected legitimate operator's machine recorded elsewhere in the same dump.
- Comparing controller mode-change logs recovered from memory against the reconstructed user-activity timeline surfaced two PLC mode-change events with no corresponding entry in the expected activity sequence, flaggable as anomalies warranting further investigation.
- Recovering both the volatile (RAM) and non-volatile (flash) copies of the running firmware from two independently-located firmware base addresses, and comparing their extracted file sizes, allowed cross-validation of firmware integrity, since a completed, unmodified backup/restore cycle should leave both copies matching.

## Related Objectives

- `DFO-1018` Read data from digital evidence storage formats

## Related Weaknesses

- [[weaknesses/PLC memory-derived event logs lack creation timestamps, limiting timeline reconstruction]]

## References

- [DFCite-1304] Rais, Awad, Lopez and Ahmed, 2022, "Memory forensic analysis of a programmable logic controller in industrial control systems", DFRWS 2022 EU; FSI: Digital Investigation 40, 301339.
