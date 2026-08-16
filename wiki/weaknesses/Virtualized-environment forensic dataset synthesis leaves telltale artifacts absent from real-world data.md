---
id: DFW-1071
type: weakness
name: Virtualized-environment forensic dataset synthesis leaves telltale artifacts absent from real-world data
description: Even a simple synthesized scenario run inside a virtualized environment through an automation agent produces virtualization- and agent-specific artifacts (evidence of virtualized hardware, automation-agent traces) that would not be present on a genuine, non-virtualized real-world system, meaning a synthetic dataset built this way is discoverably synthetic rather than an unbiased stand-in for real-world evidence.
categories:
  - ASTM_INAC_EX
mitigation_ids:
  - DFM-1071
source_refs:
  - DFCite-1061
  - DFCite-1247
  - DFCite-1267
updated_at: 2026-08-13
status: complete
---

# Virtualized-environment forensic dataset synthesis leaves telltale artifacts absent from real-world data

## Summary

The authors note directly, discussing even a simple AKF-generated demonstration scenario, that "there are still...many artifacts that would not be present in a real-world dataset," citing prior work reaching similar conclusions that evidence of synthesizer use is easily discoverable, in part because the use of virtualized hardware and an automation agent leaves its own signature. ForTrace's own evaluation independently catalogs three concrete categories of such self-identifying artifacts: file-system traces (the framework's own installation directory, Python runtime directories, and Prefetch entries from modules invoking `regedit`/`psexec`), Registry traces (its `changeUser()` function writes the last active user's username and password in plain text to `HKLM\Microsoft\Windows NT\CurrentVersion\Winlogon`), and Event Log traces (installation and scenario-execution events persist even when the scenario itself later disables logging). A follow-up evaluation on a Linux scenario further attributed most of these traces specifically to the client-side software component (an "Agent") running inside the guest to drive and report on the simulation — not to virtualization itself — finding that removing the agent entirely and controlling the guest purely from the host (see [[techniques/Synthesize digital forensic training and validation datasets]]) eliminated the agent's installation logs, password-less sudo configuration, its own Python library and `__pycache__` directory, and its running process and autostart entry. One trace nonetheless persisted even without any agent present: a shell-history entry from the one-time command needed to make the interactive console's command prompt static and machine-parseable, since that command is itself typed into, and logged by, the guest's shell.

## Why It Matters

A dataset built via virtualized-environment synthesis is well suited for testing whether a forensic tool can correctly parse and interpret a given artifact type, but is a poor stand-in for real-world data in any use case (e.g. training or evaluating anti-forensic/anomaly detection, or research claiming ecological validity for user-behavior modeling) where the presence of virtualization- or synthesizer-specific traces would themselves be a confound. An analyst using such a dataset without accounting for this risks conclusions that do not generalize to genuine, non-synthetic evidence.

## Related Mitigations

- [[mitigations/Disclose and account for virtualization and synthesizer artifacts when using synthetic forensic datasets]]

## Used By

- [[techniques/Synthesize digital forensic training and validation datasets]]

## References

- [DFCite-1061] Gonzales et al., 2025, "AKF: A modern synthesis framework for building datasets in digital forensics", FSI: Digital Investigation 55.
- [DFCite-1247] Göbel et al., 2022, "ForTrace - A holistic forensic data set synthesis framework", FSI: Digital Investigation 40, 301344. Catalogs concrete file-system, Registry, and Event Log traces left by its own synthesis framework, including a plaintext credential leak via the `changeUser()` function.
- [DFCite-1267] Wolf, Göbel, and Baier, 2024, "Hypervisor-based data synthesis: On its potential to tackle the curse of client-side agent remnants in forensic image generation", FSI: Digital Investigation 48, 301690. Attributes most prior catalogued traces to the client-side agent specifically and demonstrates most (but not all) are eliminated by removing it.
- [DFCite-2123] Du, Hargreaves, Sheppard, and Scanlon, 2021, "TraceGen: User activity emulation for digital forensic test image generation", FSI: Digital Investigation 38, 301133. An early documented case of this weakness: a Python `shutil`-based automated file-copy action omitted ShellBag registry-key artifacts that the same action performed manually via GUI copy-paste generated.
