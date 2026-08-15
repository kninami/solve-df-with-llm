---
id: DFT-1253
type: technique
name: Summarize Android native library data flow using static taint analysis
description: Statically analyze an Android app's compiled native (C/C++, .so) libraries by lifting each to LLVM IR, tracking taint propagation from native source APIs (sensors, timestamps, visited URLs, text input) through to native sink APIs (file writes, network sends) via forward data-flow analysis, and pre-computing a queryable per-method summary database so a forensic investigator or analysis tool no longer has to treat native code as an opaque black box.
objective_ids:
  - DFO-1011
weakness_ids:
  - DFW-1267
aliases:
  - LibDroid
  - Android Native Library Database (ANLD)
source_refs:
  - DFCite-1293
updated_at: 2026-08-14
status: complete
---

# Summarize Android native library data flow using static taint analysis

## Summary

Android apps increasingly implement functionality in native (NDK-compiled C/C++) libraries rather than Java, and existing Android taint-analysis tools either skip native method invocations entirely (treating a native call's output as untainted, an under-tainting problem that misses evidence) or crudely over-approximate it (unioning taint across every input/output of a native call regardless of actual data flow, producing excess false positives) — because none tracks real data-flow *within* native code. Lifting each native library's compiled binary to LLVM intermediate representation and running a dedicated forward taint-propagation analysis against it produces a precise, reusable data-flow summary for each native method, identifying which of its inputs/outputs correspond to sensitive evidentiary data (visited URLs, timestamps, sensor readings, user text input) and where that data is written to the file system or network.

## Details

Given a native library's `.so` file, the library is transformed to LLVM IR (via McSema) and its control-flow graph and entry points are built (via Clang Static Analyzer), against which a `SummarizeNativeMethod` algorithm computes a per-method summary: a `TaintSet` (which categories of evidentiary data a variable carries), a `Path` (the file path evidentiary data is written to, tracked through native file-descriptor writes), and, for branches whose outcome depends on symbolic input, an abstract-syntax-tree condition resolved via an SMT solver. Taint propagation rules are defined per ARM/Thumb instruction (data movement, arithmetic/logic, and control-flow instructions), and a stack-based loop-detection mechanism avoids re-analyzing the same method call repeatedly when it appears inside a loop. Native source and sink APIs are seeded from a combination of existing published lists (FlowDroid, SuSi, DroidSafe) and the authors' own manual analysis, extended with four evidentiary categories specifically relevant to forensic investigation: visited URL, timestamp, sensor, and text input. The resulting per-method summaries are stored in a pre-computed database (the Android Native Library Database, ANLD) that an investigator or an existing Java-focused Android static-analysis tool can query directly by native library name and version, without needing to re-run the (comparatively expensive) native-code analysis for every case that uses the same library.

## Examples

- Analyzing 13,138 native libraries collected from 2,627 real-world Google Play apps found that of the libraries invoking any source/sink API, 45 read and stored the device's Sensor data, 17 stored the user's Time-stamped activity, 14 obtained the user's visited URLs, and many additionally acquired device identifiers (Device ID, UUID, Contact, Mobile Country Code) categorized as "Others."
- A case study on a `com.gooders.pdfscanner.gpmalware` app (Joker malware family) found its native library concealed Command-and-Control communication: LibDroid's data-flow summary showed the native code querying the device's Mobile Country Code and IP address (via `android_getaddrinfofornetwork()`) and writing the result to `/data/data/com.gooders.g pmalware/databases/idata.db`, exposing the covert C2 payload-subscription mechanism that would otherwise have been invisible to Java-only taint analysis.
- Manual best-efforts verification against 34 native libraries used by 10 real installed apps (exercised via automated UI interaction for 2 hours each) found LibDroid achieved 97% average precision identifying files containing evidentiary data.

## Related Objectives

- `DFO-1011` Extract artifacts stored by applications

## Related Weaknesses

- [[weaknesses/Existing Android taint-analysis tools either skip native library data flow or over-approximate it, producing missed or excess evidence]]

## References

- [DFCite-1293] Shi, Cheng and Guan, 2022, "LibDroid: Summarizing information flow of android native libraries via static analysis", DFRWS 2022 USA; FSI: Digital Investigation 42, 301405.
