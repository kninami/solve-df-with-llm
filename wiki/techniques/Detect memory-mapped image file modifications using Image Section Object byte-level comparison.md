---
id: LWT-2124
type: technique
name: Detect memory-mapped image file modifications using Image Section Object byte-level comparison
description: Identify malicious code injected into a Windows process's memory-mapped executables and DLLs (API hooks, AMSI/ETW bypasses, module stomping, process hollowing) by comparing each mapped page in process memory byte-by-byte against the corresponding page of the Image Section Object, a memory-resident, unmodified reference copy of the same image file, pinpointing the exact modified bytes rather than only the modified page.
objective_ids:
  - DFO-1019
weakness_ids:
  - LWW-2133
aliases:
  - imgmalfind
  - ISO-based MMIF modification detection
source_refs:
  - LWCite-2155
updated_at: 2026-08-17
status: complete
---

# Detect memory-mapped image file modifications using Image Section Object byte-level comparison

## Summary

A Windows executable or DLL mapped into a process's address space (a memory-mapped image file, MMIF) has a second, normally unmodified representation in memory — the Image Section Object (ISO), a page-aligned, relocated template used to back new mappings of the same file. Comparing each Virtual Address Descriptor (VAD) page of a process's mapped image against the corresponding ISO page byte-by-byte reveals exactly which bytes were modified, letting an investigator distinguish a small API-hook patch (a handful of bytes) from a large-scale module-stomping or process-hollowing overwrite (hundreds to thousands of bytes) without manually reviewing an entire 4096-byte page for a change that could be as small as three bytes.

## Details

Prior page-level detection approaches (testing a page's PrototypePte or Shared field, or the PFN database's Modified field) are all subverted by Windows' automatic memory-combining feature: when two processes are maliciously modified with identical bytes (common for AMSI/ETW bypasses using static patch bytes, or Module Stomping targeting the same victim DLL), the OS later combines the resulting duplicate private pages back into a single shared physical page, causing all three prior approaches to misreport the page as unmodified. Resolving the OriginalPte field's state instead (SUBSEC indicates unmodified, any other state indicates modification) is immune to this effect. Because legitimate software also patches its own MMIF pages for benign reasons (e.g., browser sandboxing hooks, antivirus self-protection hooks, .NET TLS-slot index patches), a companion filtering algorithm checks whether the exact instruction sequence matches a known benign pattern, whether the patch's ultimate jump target lands on an unmodified page, and whether the process-MMIF-target combination is explicitly allow-listed, before excluding a finding as benign — verifying the target page's integrity specifically prevents allow-listing a hook chain that redirects through a benign-looking target into a page that was itself separately modified (e.g., by module stomping).

## Examples

- imgmalfind (Volatility 3 plugin): detected all tested AMSI bypasses, ETW bypasses, and 114 NetRipper API hooks across Edge/Chrome processes that Volatility's `apihooks` plugin missed entirely, correctly reported Module Stomping (270 modified bytes matching the 276-byte injected shellcode) and overwrite-based Process Hollowing (64,627 modified bytes) with byte-level precision, and — after applying its benign-modification filter — reduced 628 identified benign browser/Office/antivirus hooks on a clean Windows 10 system down to a single unexplained modification requiring manual review.

## Related Objectives

- `DFO-1019` Detect anti-forensics and other anomalies

## Related Weaknesses

- [[weaknesses/Byte-level MMIF modification detection degrades to whole-page reporting when the ISO page is not memory-resident]]

## References

- [LWCite-2155] Block, 2023, "Windows memory forensics: Identification of (malicious) modifications in memory-mapped image files", FSI: Digital Investigation 45.
