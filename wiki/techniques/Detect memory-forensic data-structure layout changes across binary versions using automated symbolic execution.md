---
id: LWT-2071
type: technique
name: Detect memory-forensic data-structure layout changes across binary versions using automated symbolic execution
description: Automatically determine which functions within a forensically important binary (e.g. an OS kernel module or userland runtime) access members of a target data structure, and compare that access pattern across different versions of the binary using symbolic execution, to verify whether a memory-analysis framework's known structure-member offsets still hold for a specific target version.
objective_ids:
  - DFO-1004
weakness_ids:
  - LWW-2074
aliases:
  - Seance
source_refs:
  - LWCite-2079
updated_at: 2026-08-16
status: complete
---

# Detect memory-forensic data-structure layout changes across binary versions using automated symbolic execution

## Summary

Memory forensic frameworks (e.g. Volatility, Rekall) rely on knowing the exact offset and type of each member of the data structures they parse out of a memory image, but this layout information is not published for most binary module versions and previously had to be recovered by slow, error-prone manual reverse engineering per version. Seance automates this by using symbolic execution (via the angr binary-analysis platform) to trace every register, memory, and pointer access a target function makes when accessing a structure member, producing a version-specific "fingerprint" that can be directly compared against fingerprints from other versions of the same binary.

## Details

For a function known to access a structure of interest, Seance loads the target binary, generates its control-flow graph bounded by a computed start/end address, and performs symbolic execution across all reachable code paths, recording every register and memory access (address/register, data, access length, condition, and containing basic block) into read and write dictionaries. Post-processing traces pointer values back to their originating register to determine the structure-member offset each access refers to, producing a JSON fingerprint per binary version (file version, list of source/offset-list pairs, and control-flow-graph metadata) that is stored in a results database. Comparing fingerprints across versions of the same module yields one of five outcomes ranging from a full match (no framework changes needed) through offset-only, raw-offset, and partial-access matches (each indicating a different degree of required re-analysis) to no match at all (the module changed enough that the framework needs full re-analysis for that version) — directly telling a memory-forensics developer or investigator whether their tool's existing structure-offset knowledge is still valid for the exact target binary version, rather than assuming it based on the OS/application version alone.

## Examples

- Evaluated against 21 versions of macOS's Objective-C runtime (`libobjc.dylib`, versions corresponding to macOS 10.11.0 through 10.15.6), Seance detected that different structure members changed compatibility groupings independently — e.g. `NXFreeHashTable` formed three distinct compatible groups across the tested versions while `NXEmptyHashTable` formed only one large group spanning 10.14.0-10.15.6 — showing that offset compatibility must be assessed per structure member rather than assumed uniform across an entire binary version.
- Also demonstrated against the Windows networking stack (`tcpip.sys`), reading back memory accesses recorded during symbolic execution of a target function to trace register/pointer offsets used within it.

## Related Objectives

- `DFO-1004` Conduct research

## Related Weaknesses

- [[weaknesses/Memory forensic frameworks silently produce incomplete or incorrect artifacts when a target binary's data structure layout changes between versions]]

## References

- [LWCite-2079] Maggio, Case, Ali-Gombe, and Richard III, 2021, "Seance: Divination of tool-breaking changes in forensically important binaries", FSI: Digital Investigation 37, 301189.
