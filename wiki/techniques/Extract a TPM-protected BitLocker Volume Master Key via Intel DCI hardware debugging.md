---
id: DFT-1213
type: technique
name: Extract a TPM-protected BitLocker Volume Master Key via Intel DCI hardware debugging
description: Recover the clear Volume Master Key (VMK) of a TPM-protected BitLocker volume by enabling Intel Direct Connect Interface (DCI) hardware debugging on the target computer's UEFI firmware, reverse-engineering the Windows Boot Manager to locate the exact code point where the TPM's unsealed VMK is held in a CPU register, and halting the CPU with a breakpoint there to dump the register's referenced memory.
objective_ids:
  - DFO-1016
weakness_ids:
  - DFW-1226
aliases:
  - Intel DCI BitLocker VMK extraction
  - DCILeech-style TPM BitLocker key recovery
source_refs:
  - DFCite-1237
updated_at: 2026-08-13
status: complete
---

# Extract a TPM-protected BitLocker Volume Master Key via Intel DCI hardware debugging

## Summary

When a BitLocker volume's Volume Master Key is protected solely by a TPM, the Windows Boot Manager UEFI application must retrieve the key from the TPM into CPU-accessible memory during every boot for the volume to decrypt, and Intel processors from the Skylake generation onward expose a low-cost hardware debug interface (Intel DCI) that — once enabled in firmware — can halt the CPU at that exact moment and read the key straight out of memory, without needing the user's Windows password or the BitLocker recovery key.

## Details

The method proceeds in five steps. First, the target's storage is imaged and `manage-bde` confirms the volume is TPM-protected and identifies its PCR validation profile. Second, Intel DCI is enabled by extracting the UEFI firmware image (via a software tool or a hardware SPI flash programmer), locating the DCI-related settings' NVRAM variable offsets with firmware-analysis tooling (parsing the module containing them, then extracting its Internal Forms Representation to map each setting name to its variable-store offset), and writing the new values back to firmware — critically avoiding any firmware-modification method that triggers a full reset-to-defaults, since that would force BitLocker into recovery mode due to altered PCR measurements. Third, the evidence drive's Windows Boot Manager binary (`bootmgfw.efi`) is disassembled in a reverse-engineering tool with Windows symbol files loaded, to locate the `FvebUnsealCallback` function's return instruction, at which point a specific CPU register holds a pointer to the just-unsealed clear VMK in memory. Fourth, the host computer connects to the powered-off target over an inexpensive USB 3 A-to-A debug cable, halts the CPU as it powers on, sets a breakpoint at the located return-instruction address, releases execution until the breakpoint is hit, and dumps the memory the noted register points to — yielding the 32-byte VMK. Fifth, the VMK is used with a Linux BitLocker-decryption tool to produce a fully decrypted, mountable volume image. The entire method depends on Intel DCI actually being enableable on the target hardware: some systems' firmware settings for DCI have no effect regardless of the values written, and Intel Boot Guard (when it also covers the relevant NVRAM regions) can block firmware modification outright.

## Examples

- On an Acer Aspire 5 laptop with a 7th-generation Intel Kaby Lake CPU, Windows 11 Pro, TPM 2.0, and Secure Boot enabled, the method successfully enabled Intel DCI via software firmware modification (CHIPSEC to dump, `RU.efi` to write), located the VMK-holding register via Ghidra disassembly of `bootmgfw.efi`, and retrieved the 32-byte VMK over a USB 3 debug cable, fully decrypting the volume with Dislocker.
- On a Lenovo T480 laptop with an 8th-generation Intel Kaby Lake R CPU and Intel Boot Guard enabled, firmware write protection required a hardware SPI programmer instead of a software approach, and although the relevant NVRAM regions were not themselves protected by Boot Guard's chain of trust, the DCI-related firmware settings had no effect on enabling the interface, so the method could not be completed on that system.
- On both tested systems, the firmware modifications required to enable Intel DCI did not trigger BitLocker's recovery mode, confirming that the specific settings altered do not affect the PCR measurements BitLocker validates against.

## Related Objectives

- `DFO-1016` Overcome protection mechanisms

## Related Weaknesses

- [[weaknesses/Intel DCI-based BitLocker VMK extraction depends on the target computer's debug interface being enableable]]

## References

- [DFCite-1237] Bichara de Assumpção, dos Reis, Marcondes, da Silva Eleutério and Vieira, 2023, "Forensic method for decrypting TPM-protected BitLocker volumes using Intel DCI", DFRWS 2023 EU; FSI: Digital Investigation 44, 301514.
