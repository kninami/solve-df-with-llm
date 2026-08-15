---
id: DFM-1268
type: mitigation
name: Supplement Java-focused Android taint-analysis tools with a native-library-aware data-flow summary before drawing conclusions
source_refs:
  - DFCite-1293
updated_at: 2026-08-14
status: complete
---

# Supplement Java-focused Android taint-analysis tools with a native-library-aware data-flow summary before drawing conclusions

## Summary

Before relying on a Java-focused Android static-analysis tool's evidence findings for an app that uses native (NDK-compiled) libraries, cross-check its output against a dedicated native-library data-flow summary — either from a pre-computed database of previously analyzed libraries or a fresh native-code taint analysis — to catch data flows the Java-only tool would silently miss or falsely flag.

## Addresses

- [[weaknesses/Existing Android taint-analysis tools either skip native library data flow or over-approximate it, producing missed or excess evidence]]

## How To Apply

Identify which native libraries (`.so` files) a target app bundles, and check whether each is already present in a native-library data-flow summary database; if not, run a dedicated native-code static taint analysis against it to generate one. Cross-reference the resulting per-method summary (source APIs invoked, sink APIs invoked, and the specific file paths sensitive data is written to) against the Java-focused tool's own reported findings, treating a native library invoking a source/sink API the Java tool did not flag as a signal of missed under-tainted evidence, and treating a native call the Java tool over-broadly flagged as tainted without a corresponding summary-confirmed data path as a likely false positive. Where feasible, corroborate summary-derived findings with a best-efforts manual verification pass (e.g. exercising the app's UI and checking which files are actually created) before relying on the automated result as case evidence.

## References

- [DFCite-1293] Shi, Cheng and Guan, 2022, "LibDroid: Summarizing information flow of android native libraries via static analysis", DFRWS 2022 USA; FSI: Digital Investigation 42, 301405.
