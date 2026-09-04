---
id: LWT-2084
type: technique
name: Analyze SGX enclave memory using kernel-structure and user-space interface reverse engineering
description: Investigate an Intel SGX-enabled machine's memory image in three phases -- acquisition-time detection of SGX hardware capabilities via CPUID, kernel-space analysis of the OS's enclave-tracking data structures (Linux sgx_encl / vm_private_data) to enumerate loaded and "zombie" enclaves, and user-space analysis inferring an enclave's memory layout and its secure/outside function interface from the host process's memory -- to recover as much information as possible about SGX enclaves despite SGX's hardware-enforced memory isolation blocking direct content inspection in release mode.
objective_ids:
  - DFO-1017
  - DFO-1019
weakness_ids:
  - LWW-2087
aliases:
  - SGX memory forensics
source_refs:
  - LWCite-2102
updated_at: 2026-08-16
status: complete
---

# Analyze SGX enclave memory using kernel-structure and user-space interface reverse engineering

## Summary

Intel Software Guard Extensions (SGX) create hardware-isolated memory regions called enclaves that shield code and data from the rest of the system -- including the operating system and, from a forensic standpoint, ordinary memory-dump and analysis tools -- meaning an enclave's actual content is normally invisible to an analyst inspecting an acquired memory image. Because an enclave can never be fully self-contained (it always needs some external support code to interact with the rest of the system), an analyst can recover substantial indirect information about an enclave's presence, structure, and interface by examining the traces its supporting kernel and user-space infrastructure leaves in ordinary (non-enclave) memory, without needing to break SGX's isolation itself.

## Details

**Memory acquisition** first determines what level of access is available: an SGX-aware dump tool queries CPU capabilities via the CPUID instruction (a read-only opcode-based query that does not affect RAM content or coherency) to detect SGX hardware presence, EPC (Enclave Page Cache) zone addresses/sizes, and microcode revision; enclaves running in debug mode can then be dumped directly via the EDBGRD opcode, while enclaves in release mode remain unreadable unless the CPU's microcode is known to be vulnerable to a CPU speculative-execution attack (e.g. Foreshadow-SGX, SGAxe), in which case those attacks can also be leveraged to extract release-mode enclave content. **Kernel-space analysis** examines the specific data structures the OS kernel and Intel's own driver (isgx or DCAP on Linux) use to track loaded enclaves -- primarily the `vm_private_data` field of a process's `vm_area_struct`, which for an SGX-hosting process points to an `sgx_encl` structure recording the enclave's load address, allocated EPC pages, debug-mode/capability flags, and a linked list of other enclaves instantiated on the system (letting an analyst also recover "zombie" enclaves detached from their host process but not yet deallocated) -- allowing enumeration of enclave presence and status even when the dump itself carries no direct enclave content. Where the kernel driver in use is unknown to the analyst, heuristics based on the special memory-page flags (VM_PFNMAP, VM_IO) SGX pages carry can still detect likely enclave-hosting processes, at the cost of some false positives from other processes using similarly-flagged special memory pages (e.g. graphics devices). **User-space analysis** infers an enclave's memory layout (by recognizing known page-permission-block patterns for API-like frameworks such as the Intel SGX SDK, or estimating loaded-application size via measuring rwx block size for Container-like frameworks such as Graphene/SGX-LKL) and its interface (the specific `ecall`/`ocall` functions the enclave exposes to interact with the untrusted host process and OS) via static analysis of framework-specific code patterns (e.g. locating the `ocall_table`/`ecall_table` structures each development framework hard-codes in predictable locations), rather than relying on more expensive semantic software-similarity techniques.

## Examples

- Evaluated against 45 SGX applications spanning six development frameworks (Intel SGX SDK, Open Enclave SDK, Asylo, RUST-SDK, SGX-LKL, Graphene) and two Intel drivers (isgx, DCAP), the technique correctly located every sample's `ecall`/`ocall` interface with zero false positives and zero false negatives, and correctly identified the development framework for all but one sample (a RUST-SGX sample misclassified as Intel SGX SDK due to shared code similarities, though its interface information was still correctly extracted).
- Applied to a commercial Conclave-based application, the technique's kernel-space analysis correctly identified three enclaves present in the memory image (a quoting enclave, a provisioning enclave, and the application's main logic enclave), and its user-space analysis -- after being redirected from the JVM host binary to the actual shared library exporting the enclave's `sgx_ecall` symbol -- correctly extracted the enclave's interface and confirmed its single outside function (a debug-only `printf` call) had no other host-process file-write capability.
- Applied to two malware-enclave proof-of-concept samples (SGX-ROP and SnakeGX), the technique's memory-layout and interface analysis, combined with an existing ROP-chain-detection Volatility plugin, identified an unexpected ROP chain in the host process interacting with the enclave via file-write calls (SGX-ROP) and confirmed an enclave whose interface matched a known legitimate application's specification while carrying additional undocumented outside-chain behavior used to exfiltrate cryptographic keys (SnakeGX).

## Related Objectives

- `DFO-1017` Extract artifacts stored by the operating system
- `DFO-1019` Detect anti-forensics and other anomalies

## Related Weaknesses

- [[weaknesses/SGX release-mode enclave memory is hardware-encrypted and unreadable to ordinary memory-dump tools absent a microcode vulnerability]]

## References

- [LWCite-2102] Toffalini, Oliveri, Graziano, Zhou, and Balzarotti, 2021, "The evidence beyond the wall: Memory forensics in SGX environments", FSI: Digital Investigation 39, 301313.
