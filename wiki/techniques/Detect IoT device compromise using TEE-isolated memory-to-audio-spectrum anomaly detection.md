---
id: LWT-1261
type: technique
name: Detect IoT device compromise using TEE-isolated memory-to-audio-spectrum anomaly detection
description: Continuously acquire an IoT microcontroller's flash memory from within a Trusted Execution Environment (isolating the acquisition from the untrusted main firmware), transform each changed-block memory dump into an audio spectrum, and classify it with a remote CNN as benign or anomalous, giving a resource-constrained IoT device a tamper-resistant, hardware-isolated first line of defense for incident response.
objective_ids:
  - DFO-1019
  - DFO-1015
weakness_ids:
  - LWW-1273
aliases:
  - MARS (Memory Anomaly Recognition System)
source_refs:
  - LWCite-1301
updated_at: 2026-08-14
status: complete
---

# Detect IoT device compromise using TEE-isolated memory-to-audio-spectrum anomaly detection

## Summary

Resource-constrained IoT devices rarely have room for a traditional host-based intrusion detection system, and any detection component running in the same untrusted execution context as the device's main firmware risks being disabled by the very malware it is meant to catch; embedding the memory-acquisition component inside a Trusted Execution Environment (TEE) — a hardware-isolated secure region a compromised main firmware cannot access or tamper with — while offloading the computationally expensive anomaly-classification step to a remote server keeps the on-device footprint minimal while remaining tamper-resistant.

## Details

The system splits into a lightweight on-device client and a remote classification server. On the client side, a memory acquisition module inside the TEE hashes each memory block and compares it to its previously stored hash, transferring only changed blocks (rather than a full memory dump each cycle) to minimize network overhead; a watchdog timer, reset only by the memory-acquisition code itself, forces a device reset if the untrusted main firmware fails to trigger a periodic memory check — catching cases where malware disables the detection process outright. On the server side, the received memory blocks are reassembled and transformed from raw binary into an audio spectrum (a format found, through comparison against direct n-gram byte-sequence analysis, to yield the most computationally efficient and informative feature set while remaining a lossless transformation, verified via hash comparison of a round-tripped conversion); a CNN trained on Mel-frequency cepstral coefficients, spectrograms, and chroma features extracted from that spectrum classifies the memory image as benign or anomalous and returns the classification to the device, which resets and reboots if the result indicates compromise.

## Examples

- A proof-of-concept implementation on an STM32L562QEI6QU ARM TrustZone-enabled microcontroller, tested against two hypothetical IoT applications (an infrared motion sensor and a status-indicating blinking LED), achieved 100% test accuracy, F1-score, recall, and precision in distinguishing benign from anomalous memory images, with the full memory-to-classification pipeline completing in about 43 seconds.
- Stress testing via randomly induced bit-flips at varying corruption levels (0.1%, 0.2%, 0.5%, 1.0% of memory bytes changed) found the classifier reliably detected anomalies once changes reached 1.0% of memory bytes, a threshold the authors note is well below the memory footprint of real IoT malware such as Mirai (which occupies roughly 27% of a comparable 256 KB memory), suggesting the approach could detect threats with even smaller footprints than tested.

## Related Objectives

- `DFO-1019` Detect anti-forensics and other anomalies
- `DFO-1015` Prepare for a digital investigation

## Related Weaknesses

- [[weaknesses/TEE-based IoT flash-memory anomaly detection cannot detect malware operating solely in volatile SRAM]]

## References

- [LWCite-1301] Waguespack, Smith, Muliri, Vijayakanthan and Ali-Gombe, 2024, "MARS: The first line of defense for IoT incident response", DFRWS 2024 USA; FSI: Digital Investigation 49, 301754.
