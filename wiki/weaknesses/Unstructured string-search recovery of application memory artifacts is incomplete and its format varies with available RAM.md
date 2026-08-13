---
id: DFW-1224
type: weakness
name: Unstructured string-search recovery of application memory artifacts is incomplete and its format varies with available RAM
description: The presence, persistence, and even the layout of application artifacts recoverable from a process memory dump via keyword string search depends on the amount of RAM installed on the client device, so a signature or extraction script validated on one RAM configuration can miss or misparse artifacts on another.
categories:
  - ASTM_INCOMP
  - ASTM_MISINT
mitigation_ids:
  - DFM-1224
source_refs:
  - DFCite-1235
updated_at: 2026-08-13
status: complete
---

# Unstructured string-search recovery of application memory artifacts is incomplete and its format varies with available RAM

## Summary

Testing the identical Google Meet test scenario across 4 GB, 8 GB, and 12 GB Windows VMs found that received in-call messages were entirely absent from the 4 GB and 8 GB memory dumps but present in the 12 GB dumps, and that sent messages themselves were stored in a different format at 12 GB (a single collective, chained record covering all sent messages) than at 4 GB/8 GB (separate individual records per message) — meaning both the completeness and the parsing logic required change depending on how much memory was available to the client device at capture time.

## Why It Matters

A memory-artifact extraction script or signature developed and validated against a memory dump from one RAM configuration (e.g. a small test VM) can silently under-recover or fail to parse artifacts from a real-world device with a different amount of installed RAM, because higher-RAM systems may retain more data for longer and in a structurally different arrangement rather than merely retaining the same data for a longer or shorter time; an investigator unaware of this can wrongly conclude that content (such as received messages) never existed rather than that it was present but recoverable only under the specific RAM/format combination their tooling assumed.

## Related Mitigations

- [[mitigations/Test string-signature memory extraction against multiple RAM sizes and capture memory before the application process exits]]

## Used By

- [[techniques/Recover application artifacts from process memory using unstructured keyword string search]]

## References

- [DFCite-1235] Iqbal, Khalid, Marrington, Shah and Hung, 2022, "Forensic investigation of Google Meet for memory and browser artifacts", DFRWS 2022 APAC; FSI: Digital Investigation 43, 301448.
