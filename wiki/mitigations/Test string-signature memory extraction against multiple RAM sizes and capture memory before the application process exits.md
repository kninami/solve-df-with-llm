---
id: DFM-1224
type: mitigation
name: Test string-signature memory extraction against multiple RAM sizes and capture memory before the application process exits
source_refs:
  - DFCite-1235
updated_at: 2026-08-13
status: complete
---

# Test string-signature memory extraction against multiple RAM sizes and capture memory before the application process exits

## Summary

Validate any keyword-string-search memory-extraction methodology against test devices spanning the range of RAM sizes realistically encountered in casework, and prioritize acquiring memory while the target application's process (or browser tab) is still running rather than after it has been closed.

## Addresses

- [[weaknesses/Unstructured string-search recovery of application memory artifacts is incomplete and its format varies with available RAM]]

## How To Apply

When developing or applying a string-search-based memory extraction method, run identical test scenarios on devices or VMs configured with at least a low, medium, and high RAM size representative of current real-world client devices (e.g. 4 GB, 8 GB, and 12+ GB), and document any differences in artifact persistence or record format observed between them — do not assume results from a single, minimally provisioned test VM generalize. In live casework, prioritize memory acquisition while the target process or browser tab remains open, since testing showed that after closing it some categories of artifact (in particular two-way communication records and correspondent identifiers) became partially or fully unrecoverable even though other artifact categories persisted unaffected.

## References

- [DFCite-1235] Iqbal, Khalid, Marrington, Shah and Hung, 2022, "Forensic investigation of Google Meet for memory and browser artifacts", DFRWS 2022 APAC; FSI: Digital Investigation 43, 301448.
