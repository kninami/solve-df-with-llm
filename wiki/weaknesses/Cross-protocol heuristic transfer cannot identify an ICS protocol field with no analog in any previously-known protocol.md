---
id: LWW-1302
type: weakness
name: Cross-protocol heuristic transfer cannot identify an ICS protocol field with no analog in any previously-known protocol
description: Because PREE's field-identification heuristics are built from an analyst's existing knowledge of already-understood ICS protocols, a field type genuinely unique to the protocol under investigation — with no counterpart field, byte-pattern, or usage convention among the protocols the analyst already knows — has no heuristic capable of recognizing it, so the underlying reverse-engineering approach is fundamentally bounded by the analyst's prior protocol knowledge rather than being protocol-agnostic.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-1304
source_refs:
  - LWCite-1337
updated_at: 2026-08-15
status: complete
---

# Cross-protocol heuristic transfer cannot identify an ICS protocol field with no analog in any previously-known protocol

## Summary

PREE's entire premise rests on the hypothesis that "knowledge of one ICS protocol can aid in reverse engineering other proprietary ICS protocols" because of shared, overlapping functionality across the ICS protocol family. This hypothesis, while validated for the common field types tested (function code, length, memory address, session/transaction ID), does not extend to a field type that is genuinely novel to the protocol under examination and shares no structural or behavioral resemblance to fields the analyst has previously encountered.

## Why It Matters

An investigator using PREE-style cross-protocol heuristics against a proprietary protocol with vendor-unique fields (custom status flags, proprietary encoding schemes, vendor-specific extensions) risks silently missing those fields — the analysis will report successfully identified common fields while giving no indication that other, unidentified fields exist and may carry evidentiary significance. Since PREE's own accuracy improvement over prior tools was demonstrated specifically on shared/common field types, an investigator should not extrapolate that improvement to a protocol's full field set without additional manual verification.

## Related Mitigations

- [[mitigations/Manually review unclassified message regions after cross-protocol heuristic field identification]]

## Used By

- [[techniques/Reverse-engineer a proprietary ICS protocol's fields using cross-protocol heuristic pattern transfer]]

## References

- [LWCite-1337] Qasim, Jo, and Ahmed, 2023, "PREE: Heuristic builder for reverse engineering of network protocols in industrial control systems", FSI: Digital Investigation 45, 301565.
