---
id: LWT-2102
type: technique
name: Extract V8 JavaScript engine heap objects from memory using MetaMap-based scanning
description: Recover live JavaScript objects (strings, arrays, closures, and application-specific data) from a memory image of any process embedding Google's V8 JavaScript engine -- not just Chrome, but any Node.js, Electron, or V8-embedding application -- by locating V8's internal Map (hidden class/shape) metadata structures in memory and using them to correctly interpret the type and field layout of every heap object referencing that Map.
objective_ids:
  - DFO-1017
  - DFO-1011
weakness_ids:
  - LWW-2108
aliases:
  - V8MapScan
  - Juicing V8
source_refs:
  - LWCite-2127
updated_at: 2026-08-16
status: complete
---

# Extract V8 JavaScript engine heap objects from memory using MetaMap-based scanning

## Summary

V8, the JavaScript engine underlying Chrome, Node.js, Electron, and many other applications, represents every heap object's type and field layout via an associated internal "Map" (V8's own term for a hidden class/shape descriptor, unrelated to the JavaScript `Map` data type) rather than storing type tags directly on each object. Because V8 heap layouts are undocumented and change across versions, a memory-forensics tool cannot interpret arbitrary V8 heap bytes without first locating the relevant Map structures; scanning specifically for Map objects and following their pointers back to every object referencing them recovers a substantial portion of a process's live JavaScript object graph directly from an acquired memory image.

## Details

V8's heap stores tagged pointers and small integers inline according to a per-object-type layout that only the object's associated Map fully specifies (field count, field types, and whether a field is inline or itself a pointer to another heap object). The technique implements this as a Volatility 3 framework plugin: it scans the target process's heap regions for byte patterns consistent with V8's own internal Map object structure (which itself has a fixed, identifiable layout since Maps are themselves heap objects with their own meta-Map), then, for each located Map, scans the broader heap for objects whose own Map pointer field references that specific Map instance -- correctly interpreting each matched object's fields according to the located Map's layout description rather than needing hard-coded per-application-version offsets. Because V8's Map-based object model is stable across the engine's use in many different embedding applications, the same scanning approach generalizes across any V8-embedding process rather than requiring separate reverse engineering per target application.

## Examples

- Applied to memory images of several V8-embedding applications (including Node.js processes and Electron-based desktop applications), the technique recovered live JavaScript string, array, and object values present in the process's heap at acquisition time, without requiring per-application customization of the underlying Map-scanning logic.
- Because V8 exposes its own JavaScript `Map`/`Set`/object/array types atop the same underlying Map-metadata mechanism, the same scanning approach recovers application-level data structures (e.g. a chat application's in-memory message objects) alongside V8's own internal bookkeeping objects, letting an investigator filter for application-relevant object types once the general recovery mechanism is working.

## Related Objectives

- `DFO-1017` Extract artifacts stored by the operating system
- `DFO-1011` Extract artifacts stored by applications

## Related Weaknesses

- [[weaknesses/V8 garbage collection between memory snapshots reduces the number of recoverable JavaScript heap objects]]

## References

- [LWCite-2127] "uicing V8: A primary account for the memory forensics of the V8 JavaScript engine", FSI: Digital Investigation 48, 2024.
