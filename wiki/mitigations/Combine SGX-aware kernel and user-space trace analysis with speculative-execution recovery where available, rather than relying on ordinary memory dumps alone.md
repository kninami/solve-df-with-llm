---
id: LWM-2087
type: mitigation
name: Combine SGX-aware kernel and user-space trace analysis with speculative-execution recovery where available, rather than relying on ordinary memory dumps alone
source_refs:
  - LWCite-2102
updated_at: 2026-08-16
status: complete
---

# Combine SGX-aware kernel and user-space trace analysis with speculative-execution recovery where available, rather than relying on ordinary memory dumps alone

## Summary

When investigating a suspected-compromised SGX-enabled machine, use an SGX-aware acquisition tool to detect enclave presence via CPUID and dump debug-mode/vulnerable-microcode content directly, and for release-mode enclaves on patched hardware, rely on kernel- and user-space trace analysis to indirectly characterize enclave presence, structure, and interface, rather than treating an ordinary memory dump's inability to see inside enclave zones as evidence no enclave-related activity occurred.

## Addresses

- [[weaknesses/SGX release-mode enclave memory is hardware-encrypted and unreadable to ordinary memory-dump tools absent a microcode vulnerability]]

## How To Apply

Use an SGX-aware acquisition tool (rather than a generic memory-dump tool) that queries CPU capabilities via CPUID to detect SGX presence, EPC zones, and microcode revision at acquisition time; where the microcode is known-vulnerable to a speculative-execution attack, use that attack path to recover release-mode enclave content directly. Where the microcode is patched (foreclosing direct content recovery), apply [[techniques/Analyze SGX enclave memory using kernel-structure and user-space interface reverse engineering]] to enumerate enclave presence (including "zombie" enclaves) from kernel data structures and to infer memory layout and ecall/ocall interface from user-space traces, and combine this with complementary techniques such as ROP-chain detection in the host process to identify anomalous enclave-interaction patterns that may indicate malicious behavior, even without direct visibility into the enclave's own content.

## References

- [LWCite-2102] Toffalini, Oliveri, Graziano, Zhou, and Balzarotti, 2021, "The evidence beyond the wall: Memory forensics in SGX environments", FSI: Digital Investigation 39, 301313.
