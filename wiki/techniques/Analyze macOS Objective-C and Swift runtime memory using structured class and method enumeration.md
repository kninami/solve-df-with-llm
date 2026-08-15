---
id: DFT-1270
type: technique
name: Analyze macOS Objective-C and Swift runtime memory using structured class and method enumeration
description: Detect macOS userland malware — keyloggers, and code that abuses microphone, camera, or screen-capture APIs — directly from a memory image by walking the Objective-C and Swift runtimes' internal data structures to enumerate every loaded class, its instances, instance-variable values, and methods, then flagging known-bad classes or method calls to often-abused APIs, rather than relying on manual reverse engineering or malware-sample-specific detection rules.
objective_ids:
  - DFO-1019
weakness_ids:
  - DFW-1275
aliases:
  - mac_analyze_classes Volatility plugin
  - Objective-C and Swift runtime memory forensics
source_refs:
  - DFCite-1309
updated_at: 2026-08-15
status: complete
---

# Analyze macOS Objective-C and Swift runtime memory using structured class and method enumeration

## Summary

Because macOS malware overwhelmingly relies on Objective-C and Swift runtime APIs to interact with hardware (microphones, cameras) and monitor user activity (keystrokes, window focus), walking the Objective-C and Swift runtimes' own internal object model directly from a memory image — enumerating loaded classes, locating their instances on the heap, decoding instance-variable values, and enumerating methods — recovers structured, automatically-alertable evidence of malicious behavior that generic userland memory analysis (broad process/region dumps) cannot provide, and does so without requiring prior knowledge of the specific malware sample.

## Details

**Enumerating loaded classes**: since macOS 10.10, loaded classes are tracked by the `gdb_objc_realized_classes` global (`NXMapTable` type); each class's `objc_class` structure is decoded via its `class_rw_t`/`class_ro_t` data pointers (the `class_rw_t` layout itself changed starting with macOS 10.15, requiring version-aware decoding) to recover the class's name, methods, and instance variables. **Locating class instances**: because Objective-C simply allocates instance storage via `malloc`/`calloc` without separately tracking instances, the process heap must be scanned for `objc_object` structures whose leading `isa` pointer references an already-enumerated class; this scan also recovers de-allocated instances still resident in freed heap regions (validated carefully to avoid memory-smearing artifacts), extending analysis beyond only currently-live objects. **Parsing instance variables and decoding values**: each variable's offset, name, and type-encoding string (from `ivar_t`) is used to decode its value from the object's memory — signed/unsigned integers, floats/doubles, character-pointer strings, booleans, class/type pointers, arrays, and reverse-engineered `NSString`/`NSInteger`/`NSUrl`/`NSArray` encodings (which required binary analysis to document since the Foundation framework's exact in-memory layouts for these types are undocumented). **Enumerating methods**: each class's `method_list_t` array of `method_t` structures yields the method's selector name, parameter type signature, and implementation pointer, which the plugins can then disassemble to check for calls to a configurable list of often-abused APIs (e.g. `CGEventTapCreate`/`IOHIDManagerRegisterInputValueCallback` for keylogging, `NSCreateObjectFileImageFromMemory` for memory-only payload execution, `popen`/`NSTask::launch` for spawning processes). **Swift support**: when Swift/Objective-C interoperability is enabled (the default on Apple platforms), Swift classes register with the Objective-C runtime and can largely be enumerated with the same algorithm, but Swift stores variable type information only in separate `TargetTypeContextDescriptor` metadata records (not in `ivar_t`) and mangles all type/method names, requiring a purpose-built demangler; methods that stay purely within the Swift runtime (not propagated to Objective-C) are instead recovered by parsing the class's vtable (`TargetVTableDescriptorHeader`/`TargetMethodDescriptor`) and cross-referencing each method's implementation pointer against the executable's Mach-O symbol table.

## Examples

- Running the `mac_analyze_classes` plugin against a memory sample infected with FinSpy (a commercial surveillance tool documented by Amnesty International as capable of keylogging, audio/webcam recording, screen recording, and file exfiltration) automatically flagged the process's use of known-bad classes and abused APIs, without any FinSpy-specific detection signature.
- Validated against a malware testbed built from documented real-world macOS threats — Crisis, EvilQuest, Komplex (APT28), MacDownloader, Realtime-Spy, Ventir, and XAgentmacOS — the plugins generically detected each sample's use of runtime-provided APIs for audio/webcam capture, keylogging, screenshot capture, and command execution, based purely on the APIs and classes used rather than sample-specific signatures.

## Related Objectives

- `DFO-1019` Detect anti-forensics and other anomalies

## Related Weaknesses

- [[weaknesses/Structured runtime memory analysis relies on manually reverse-engineered internal offsets that can break across runtime or OS versions]]

## References

- [DFCite-1309] Manna, Case, Ali-Gombe, and Richard III, 2021, "Modern macOS userland runtime analysis", FSI: Digital Investigation 38, 301221.
