---
id: LWM-1264
type: mitigation
name: Build and verify a JTAG acquisition profile against a test PLC of the same model before acquiring a suspect PLC's memory
source_refs:
  - LWCite-1284
updated_at: 2026-08-14
status: complete
---

# Build and verify a JTAG acquisition profile against a test PLC of the same model before acquiring a suspect PLC's memory

## Summary

Obtain a PLC of the same make and model as the suspect device and use it to iteratively discover safe address ranges and tuned acquisition parameters, verifying the resulting profile's correctness and repeatability, before ever applying JTAG acquisition to the actual suspect controller.

## Addresses

- [[weaknesses/PLC memory acquisition via JTAG risks crashing or hanging the controller when acquisition parameters or address ranges are untested]]

## How To Apply

Before acquiring a suspect PLC, obtain a same-model test unit and perform the full profile-creation process against it: identify the processor and memory ICs, locate and confirm the JTAG pinout, run a full address-space scan to discover unacquirable (crash-inducing) ranges and redundant (don't-care-bit) address blocks, and tune per-block acquisition parameters (block size, clock speed, wait time) to the point where repeated acquisitions succeed without crashing the test unit or its debugger. Verify the finished profile's data by confirming that acquired firmware hashes match vendor-published firmware and that known strings (controller name, project filenames) are correctly recovered, and confirm repeatability by re-running the acquisition multiple times across different sessions. Only once the profile is verified stable on the test unit should it be applied to the suspect PLC, using the same acquisition setup and parameters, minimizing the risk of an untested condition crashing the actual evidence device.

## References

- [LWCite-1284] Rais, Awad, Lopez and Ahmed, 2021, "JTAG-based PLC memory acquisition framework for industrial control systems", DFRWS 2021 USA; FSI: Digital Investigation 37, 301196.
