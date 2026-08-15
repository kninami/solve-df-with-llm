---
id: DFT-1272
type: technique
name: Detect DLL hijacking by comparing a loaded module's path and size across memory-dump processes
description: Detect DLL search-order hijacking, DLL side-loading, and DLL proxying attacks in a Windows memory dump by listing every process that has a given module loaded, determining the module's most common on-disk path and size across those processes, and flagging any process whose loaded copy of the module differs in path or size from that consensus value as a likely hijacking victim.
objective_ids:
  - DFO-1019
weakness_ids:
  - DFW-1282
aliases:
  - Modex/Intermodex --detect flag
source_refs:
  - DFCite-1310
updated_at: 2026-08-15
status: complete
---

# Detect DLL hijacking by comparing a loaded module's path and size across memory-dump processes

## Summary

DLL hijacking attacks (search-order hijacking, side-loading, proxying) work by getting a victim process to load a malicious DLL with the same filename as a legitimate one. Because the great majority of processes on a system load the genuine, unmodified DLL, comparing the on-disk path and file size of a named module across every process that has it loaded — and treating the most common path/size pair as ground truth — surfaces the minority of processes loading a differently-pathed or differently-sized (and therefore likely malicious) copy, without needing a known-bad signature for the malicious DLL itself.

## Details

Built as a `--detect` flag on the same Modex/Intermodex tools used for module aggregation ([[techniques/Aggregate module pages across single or multiple Windows memory dumps to reconstruct a complete DLL]]), the detection logic lists every process with the named module loaded, computes the most common path and the most common size among them, and flags any process whose module path differs from the most common path, or whose module size differs from the most common size, as a potential hijacking victim. Intermodex extends this comparison across multiple memory dumps — including dumps from different machines, provided those machines have a similar configuration (same Windows version and updates) — and reports both the affected process and the affected memory dump. Because the detection assumes the majority of loaded copies are genuine, it depends on hijacked processes being a minority, an assumption the authors consider reasonable since attackers generally aim for stealth; it also does not rely on ASLR-sensitive base addresses, so it is unaffected by the base-address-matching limitation that constrains Intermodex's module-aggregation (rather than detection) use.

## Examples

- A proof-of-concept DLL-proxying attack against VLC media player, hijacking the Microsoft-signed `cryptbase.dll` by placing a malicious same-named DLL in VLC's own directory, was successfully flagged by both Modex (on a single infected memory dump, identifying the VLC process as suspicious) and Intermodex (across an infected dump and a clean dump, additionally identifying which dump the affected process ran in).

## Related Objectives

- `DFO-1019` Detect anti-forensics and other anomalies

## Related Weaknesses

- [[weaknesses/Path- and size-based DLL hijacking detection misses an attack whose malicious DLL matches the legitimate DLL's path and size]]

## References

- [DFCite-1310] Fernández-Álvarez and Rodríguez, 2023, "Module extraction and DLL hijacking detection via single or multiple memory dumps", FSI: Digital Investigation 44, 301505.
