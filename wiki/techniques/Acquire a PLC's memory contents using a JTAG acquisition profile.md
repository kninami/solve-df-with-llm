---
id: DFT-1246
type: technique
name: Acquire a PLC's memory contents using a JTAG acquisition profile
description: Recover the complete addressable memory contents of a proprietary, legacy programmable logic controller by locating its JTAG debug port, building a memory map that excludes unacquirable and redundant address ranges, and using an optimized, verified acquisition profile to read the memory over JTAG without crashing the controller.
objective_ids:
  - DFO-1021
  - DFO-1006
weakness_ids:
  - DFW-1263
aliases:
  - Kyros JTAG PLC memory acquisition framework
source_refs:
  - DFCite-1284
updated_at: 2026-08-14
status: complete
---

# Acquire a PLC's memory contents using a JTAG acquisition profile

## Summary

Because PLC vendors use proprietary, often undocumented, heterogeneous hardware architectures and typically do not publish memory maps, acquiring a PLC's complete addressable memory — including firmware, control logic, and volatile process data relevant to a suspected sabotage or intrusion — via its hardware-level JTAG debug interface requires first building a device-specific acquisition profile (JTAG pinout, memory map, and tuned read parameters) rather than attempting a naive full-address-space scan, which risks crashing or hanging the controller.

## Details

Profile creation proceeds through hardware assessment (identifying the PLC's processor and volatile/non-volatile memory ICs from circuit-board inspection and vendor documentation, since full datasheets are often unavailable), JTAG pin identification (locating the JTAG contact pad on the circuit board and confirming its TMS/TDI/TDO/TCK/GND pinout via a connectivity test or an automated pin-finder tool such as JTAGulator when the pins are not clearly labeled or accessible), device memory-map creation (an exhaustive address-space scan on a test unit, since undocumented address ranges may point to peripherals, unused space, or crash-inducing regions), data-redundancy elimination (identifying address ranges where "don't care" bits mean multiple addresses map to the same physical memory, so only one copy needs to be acquired), unacquirable-block removal (excluding address ranges that hang or crash the controller when read), and acquisition-parameter optimization (tuning per-block read block-size, clock speed, and inter-read wait-time, since different memory ICs on the same board tolerate different acquisition speeds and over-aggressive settings can crash the PLC or its debugger). The resulting profile is verified against a test PLC (confirming firmware hash matches the vendor-published firmware, and that known strings such as controller name and project filenames are correctly recovered) before being applied to a suspect PLC of the same model, at which point only the acquisition-and-verification phase (not profile creation) needs to be repeated.

## Examples

- Building a JTAG acquisition profile for an Allen-Bradley ControlLogix 5561 (1756-L61) controller took over two weeks of iterative hardware assessment, pin identification, and crash-driven parameter tuning on a test unit, after which the resulting profile reliably acquired the suspect PLC's full addressable memory (SDRAM, NOR flash, static RAM, NAND flash, and SD card) without further crashes.
- A companion study used a JTAG-based memory-acquisition setup for the same controller family to feed [[techniques/Reverse-engineer a PLC's memory dump to extract control-logic, IO states, and logs using differential analysis]], illustrating that reliable acquisition and structural interpretation of PLC memory are complementary but distinct steps in a complete PLC forensic workflow.
- Attempting to acquire an untested address range on the case-study PLC caused it to immediately halt, while don't-care address bits were found to produce eight identical 16MB copies of the same underlying data at different addresses — both effects that had to be identified and encoded into the acquisition profile before a full, reliable acquisition could proceed.
- Re-running the verified acquisition profile against the same test PLC five times over five days (after restarting the PLC and debugger, and after downloading different programs) produced identical results each time, and modifying a single byte in one address range of a duplicated memory block was correctly observed as changed across every redundant copy of that block.

## Related Objectives

- `DFO-1021` Access device data for acquisition
- `DFO-1006` Acquire data

## Related Weaknesses

- [[weaknesses/PLC memory acquisition via JTAG risks crashing or hanging the controller when acquisition parameters or address ranges are untested]]

## References

- [DFCite-1284] Rais, Awad, Lopez and Ahmed, 2021, "JTAG-based PLC memory acquisition framework for industrial control systems", DFRWS 2021 USA; FSI: Digital Investigation 37, 301196.
