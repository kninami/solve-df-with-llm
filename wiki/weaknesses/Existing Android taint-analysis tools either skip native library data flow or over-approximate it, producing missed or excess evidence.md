---
id: LWW-1267
type: weakness
name: Existing Android taint-analysis tools either skip native library data flow or over-approximate it, producing missed or excess evidence
description: Mainstream Android static taint-analysis tools either treat a called native method as a black box that produces no taint at all (under-tainting, silently missing evidence a native library actually generates or stores) or assume every output of a native call is tainted by every input (over-tainting, producing false-positive evidence flags), because none tracks actual data-flow logic within the native code itself.
categories:
  - ASTM_INCOMP
  - ASTM_INAC_EX
mitigation_ids:
  - LWM-1268
source_refs:
  - LWCite-1293
updated_at: 2026-08-14
status: complete
---

# Existing Android taint-analysis tools either skip native library data flow or over-approximate it, producing missed or excess evidence

## Summary

Comparing three static analysis tools against 22 benchmark apps specifically designed to test native/inter-language data-flow tracking showed FlowDroid conservatively treats all native method calls as black boxes and fails to detect most data paths through them, while JN-SAF's over-approximation strategy (unioning taint across all inputs and outputs of a native call) produced false positives; separately, evaluating both tools against 2,627 real-world apps found 745 of them (28%) suffered FlowDroid's under-tainting problem with at least one type of evidence left undocumented, and 16.48% suffered JN-SAF's over-approximation-driven false positives.

## Why It Matters

An investigator relying on one of these existing tools to characterize what data an Android app's native code collects, stores, or transmits risks either missing genuinely present evidentiary data flows entirely (under-tainting) — with no indication in the tool's output that anything was skipped — or being misled by spurious evidence flags that do not correspond to real behavior (over-tainting), either of which can distort an investigation's understanding of what a specific app actually does with sensitive data such as location, sensor readings, or user input.

## Related Mitigations

- [[mitigations/Supplement Java-focused Android taint-analysis tools with a native-library-aware data-flow summary before drawing conclusions]]

## Used By

- [[techniques/Summarize Android native library data flow using static taint analysis]]

## References

- [LWCite-1293] Shi, Cheng and Guan, 2022, "LibDroid: Summarizing information flow of android native libraries via static analysis", DFRWS 2022 USA; FSI: Digital Investigation 42, 301405.
