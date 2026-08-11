---
id: DFW-1084
type: weakness
name: Reverse-engineered RTOS-dedicated file system parsers are manufacturer- and model-specific and do not generalize across vehicle platforms
description: The reverse-engineered structure and parsing method developed for one manufacturer's RTOS-dedicated built-in-camera file system (Hyundai/KIA/GENESIS DVRS) does not automatically transfer to other manufacturers' or models' dedicated file systems, since each vehicle manufacturer designs its own proprietary real-time file system, and vehicle operating systems are becoming increasingly manufacturer-specific (e.g. Mercedes-Benz's MB.OS, BMW's Operating System 8, VW's vw.os, Hyundai's ccOS).
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1084
source_refs:
  - DFCite-1074
updated_at: 2026-08-10
status: complete
---

# Reverse-engineered RTOS-dedicated file system parsers are manufacturer- and model-specific and do not generalize across vehicle platforms

## Summary

The paper's own future-work framing makes this scope limitation explicit: "in the future, this method can be applied to analyze various RTOS and dedicated file systems installed in the vehicle" — meaning the reverse-engineering and analysis presented was performed and validated for one specific manufacturer's file system, not a general-purpose method for any RTOS-dedicated automotive file system. Because most RTOSs use their own custom file system for reliability and real-time-performance reasons, and manufacturers are increasingly designing entirely proprietary operating systems, file-system diversity across the industry is expected to keep increasing.

## Why It Matters

An investigator who successfully applies this reverse-engineered parsing method to one vehicle's built-in camera storage should not assume the same tooling or structural assumptions will work on a different manufacturer's or model's built-in camera without independently reverse-engineering that system's specific file system driver and structure first — mainstream forensic tools already fail on these dedicated file systems generally, and a single reverse-engineered solution does not close that gap industry-wide.

## Related Mitigations

- [[mitigations/Reverse-engineer and validate the target RTOS file system per manufacturer and model before applying an existing parser]]

## Used By

- [[techniques/Reverse-engineered RTOS-dedicated vehicle file system analysis with unallocated-space video frame recovery]]

## References

- [DFCite-1074] Lee et al., 2023, "Analysis of real-time operating systems' file systems: Built-in cameras from vehicles", FSI: Digital Investigation 44.
