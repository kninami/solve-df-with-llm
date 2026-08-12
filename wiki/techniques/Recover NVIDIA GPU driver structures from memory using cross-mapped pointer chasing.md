---
id: DFT-1052
type: technique
name: Recover NVIDIA GPU driver structures from memory using cross-mapped pointer chasing
description: Locate and parse NVIDIA GPU kernel driver data structures (NVOC — NVIDIA Object Compiler — objects) within a RAM memory dump by exploiting the fact that both the open-source and closed-source flavors of the driver follow the same underlying structural layout, using pointer-chasing lookup methods (recursive descent from a known kernel symbol, or reverse ascent from a known class identifier) to locate structures in either driver flavor and cross-map class definitions between the two, enabling forensic tools that work regardless of which driver variant a target system used.
objective_ids:
  - DFO-1017
weakness_ids:
  - DFW-1054
aliases:
  - Cross-mapped pointer-chasing recovery of NVIDIA GPU driver structures in memory
  - NVOC memory forensics
  - NVSYMMAP
source_refs:
  - DFCite-1044
updated_at: 2026-08-09
status: complete
---

# Recover NVIDIA GPU driver structures from memory using cross-mapped pointer chasing

## Summary

NVIDIA's kernel driver code (both the open-source and closed-source builds) is generated using an internal preprocessor, NVOC, that gives every driver object a consistent structural layout: each NVOC structure's first member is a pointer to an NVOC_RTTI structure, which in turn points to an NVOC_CLASS_DEF structure holding the object's class ID, size, and metadata. Because this layout is identical across both driver flavors even though the closed-source module's own symbol names are scrubbed/obfuscated, an investigator can locate a structure via one driver's own exported kernel symbols (kallsyms) and then use the same pointer-chasing pattern to find and identify the structurally equivalent object in the other flavor's memory, without needing the closed-source driver's original symbol names.

## Details

Recursive descent lookup starts from a known kallsym pointing to an NVOC structure, follows its RTTI pointer to the NVOC_RTTI structure, and follows that to the NVOC_CLASS_DEF structure to recover the structure's class ID, name, and size. Reverse ascent lookup works in the opposite direction: starting from a known class ID, it scans kernel memory for a pointer directed at the corresponding NVOC_CLASS_DEF structure, then for a pointer directed at the corresponding NVOC_RTTI structure, ultimately locating the originating NVOC structure instance itself. Applying both methods across paired open- and closed-source driver installations, and comparing structures by their declared size and (for open-source) name, produces a cross-mapping between the two flavors' otherwise differently-named class definitions, which a standalone tool and Volatility 2 plugins then use to automatically parse GPU-relevant forensic artefacts (e.g., a GPU Accounting structure recording process start/end times, live/dead status, and PID for processes that used the GPU) from a memory dump regardless of which driver flavor produced it.

## Examples

- Testing on NVIDIA driver version 525: 171 known NVOC_CLASS_DEF structures were confirmed via the open-source kallsyms and used as ground truth; applying the mapping method to the closed-source module (whose kallsym names are scrubbed) identified 330 total structures (263 documented via cross-mapping, 67 additional undocumented ones discovered only in the closed-source driver), with 59 of 171 compared structures being byte-for-byte identical in size between the open and closed-source versions.

## Related Objectives

- `DFO-1017` Extract artifacts stored by the operating system

## Related Weaknesses

- [[weaknesses/GPU process-usage history is unavailable unless GPU Accounting was proactively enabled]]

## References

- [DFCite-1044] Bowen et al., 2024, "A step in a new direction: NVIDIA GPU kernel driver memory forensics", FSI: Digital Investigation 49.
