---
id: LWT-1199
type: technique
name: Decrypt a banking trojan's C2 communication by extracting its hardcoded encryption keys
description: Statically and dynamically analyze an Android banking trojan's decompiled code to recover its hardcoded (or deterministically derived) command-and-control encryption key/IV, decrypt captured or emulated C2 traffic with it, and enumerate the trojan's full command set and stolen-data categories from the decrypted payloads.
objective_ids:
  - DFO-1019
weakness_ids:
  - LWW-1208
aliases:
  - Static and dynamic reverse engineering of Hook banking trojan C2 protocol
source_refs:
  - LWCite-1219
updated_at: 2026-08-13
status: complete
---

# Decrypt a banking trojan's C2 communication by extracting its hardcoded encryption keys

## Summary

Many Android banking trojans distributed as "malware-as-a-service" reuse simple, fixed encryption schemes to protect their command-and-control traffic; decompiling the trojan and tracing its configuration class reveals the hardcoded key and IV (or the deterministic value they are derived from), letting an analyst decrypt captured traffic and build an emulated C2 client to enumerate every supported command without needing access to the operator's live panel.

## Details

The analysis combined static analysis (decompilation to identify configuration constants, permission declarations, and command-handler methods) with dynamic analysis (running samples in an emulator against a self-hosted emulated C2 server) to recover the full protocol: the trojan's initial configuration class held a hardcoded AES-256-CBC key/IV pair identical across all analyzed samples, letting every subsequent encrypted JSON request/response be decrypted; a Python client emulating the C2 server was then used to issue commands (e.g. `updateInjections`) and harvest the trojan's complete list of webinject targets and command definitions, which are not otherwise documented anywhere outside the malware's own code. Packed samples first required unpacking (identifying and reversing an RC4-encrypted DEX payload, or reversing a multidex-based packer) before the configuration class was reachable for static analysis.

## Examples

- Recovering the hardcoded AES-256-CBC key (`1A1zP1eP5QGefi2DMPTfTL5SLmv7Divf`) and IV (`0123456789abcdef`) shared by all 64 analyzed Hook samples allowed every C2 request/response observed during dynamic analysis to be decrypted without needing to compromise a live C2 server.
- Emulating the `updateInjections`/`downloadInjections` C2 requests with a Python client harvested 774 webinject overlay pages targeting specific banking and wallet apps, revealing the trojan's full target list from the client side alone.

## Related Objectives

- `DFO-1019` Detect anti-forensics and other anomalies

## Related Weaknesses

- [[weaknesses/Banking trojans detect an emulator, USB, or ADB-over-WiFi environment and halt execution to evade dynamic analysis]]

## References

- [LWCite-1219] Schmutz et al., 2024, "Forensic analysis of hook Android malware", FSI: Digital Investigation 49.
