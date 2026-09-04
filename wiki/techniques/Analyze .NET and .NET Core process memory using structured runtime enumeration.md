---
id: LWT-1264
type: technique
name: Analyze .NET and .NET Core process memory using structured runtime enumeration
description: Recover a .NET or .NET Core process's loaded assemblies (including memory-only, never-written-to-disk assemblies), classes, fields, field values, and both managed (IL) and native (NDirect) methods directly from a memory image by walking the Common Language Runtime's internal data structures, rather than relying on unstructured string search or a live debugger that only works against a running process.
objective_ids:
  - DFO-1019
weakness_ids:
  - LWW-1275
aliases:
  - dotnet_memory_only / dotnet_fields / dotnet_field_values / dotnet_ndirect_methods / dotnet_il_methods / dotnet_class_references Volatility plugins
source_refs:
  - LWCite-1303
updated_at: 2026-08-14
status: complete
---

# Analyze .NET and .NET Core process memory using structured runtime enumeration

## Summary

.NET has become a favored platform for memory-only malware (in-memory-loaded assemblies via the `Assembly.Load` API, used by frameworks such as Cobalt Strike's `execute-assembly` and the Covenant C2 framework) precisely because its abused capabilities leave no trace on the file system when the malware operator so chooses; because generic userland malware detection (VAD inspection, injected-DLL cross-referencing) cannot determine whether a located .NET assembly is malicious or benign without runtime-specific structural analysis, walking the CLR's own internal object model directly from a memory image — locating application domains, then assemblies, modules, classes, fields, field values, and methods — recovers deep, automatically-alertable insight into a .NET process's behavior that generic memory analysis or a live-process-only debugger (such as SOS) cannot provide.

## Details

Starting from a process's application-domain list (`SystemDomain::m_appDomainIdList` for .NET Framework, the single global `AppDomain::m_pTheAppDomain` for .NET Core), each domain's loaded assemblies are enumerated (its `m_Assemblies` ArrayList), and each assembly's on-disk path field (`PEImage.m_path`) is checked: if it points to the CLR's global empty-string buffer rather than a real path, the assembly is memory-only and can be reconstructed and written to disk directly from its in-memory `PEImageLayout` for further static analysis in a tool such as dnSpy. From there, each assembly's modules, and each module's defined classes (via the `TypeDefToMethodTable` metadata-database structure), fields (`FieldDesc` instances, queried for name/offset/type), live field *values* (by scanning the process heap for instances of a known class's method table and reading each field's value at its known offset), and methods can be automatically enumerated and alerted on: native (`NDirect`) methods — the mechanism .NET malware uses to call into unmanaged Windows APIs such as `SetWindowsHookEx` for keylogging — reveal a capability profile analogous to import-address-table analysis for native executables but performed per .NET class, while JIT-compiled managed (IL) method disassembly can be automatically scanned for calls to a configurable set of suspicious functions (e.g. screenshot-capable `GraphicsFromImage`) to flag the specific method and class responsible.

## Examples

- Running the field-value-enumeration plugin against a Covenant-C2-infected memory sample automatically recovered the malware's exact configured C2 server hostname and callback URI directly from the relevant class's `Hostname` and `CovenantURI` string fields, without any manual reverse engineering of the sample's source code.
- Running the native-method-enumeration plugin against a Covenant-infected sample's keylogger module automatically reported every native Windows API import used for keystroke capture (`GetModuleHandle`, `CallNextHookEx`, `GetForegroundWindow`, `GetWindowText`, `SetWindowsHookEx`, `UnhookWindowsHookEx`) along with each import's owning DLL and .NET module.
- Running the managed-IL-method-analysis plugin against a memory sample infected with the SharpStage malware (MoleRats APT group) automatically identified a call to `System.Drawing.Graphics.FromImage` from a specific class and method, immediately indicating screenshot-capture capability and pinpointing the exact function to begin deeper manual analysis from — defeating the sample's string obfuscation, since the function name itself was randomized but its purpose was inferred automatically from the API call it made.

## Related Objectives

- `DFO-1019` Detect anti-forensics and other anomalies

## Related Weaknesses

- [[weaknesses/Structured runtime memory analysis relies on manually reverse-engineered internal offsets that can break across runtime or OS versions]]

## References

- [LWCite-1303] Manna, Case, Ali-Gombe and Richard III, 2022, "Memory analysis of .NET and .Net Core applications", DFRWS 2022 USA; FSI: Digital Investigation 42, 301404.
