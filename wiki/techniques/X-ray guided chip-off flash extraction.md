---
id: DFT-1023
type: technique
name: X-ray guided chip-off flash extraction
description: Physically desolder a flash storage chip lacking exposed test-access pins using infrared reflow heating, using X-ray tomography of the multi-layer PCB to trace internal test points to their respective pins beforehand, then read out the chip's raw contents via a wire-to-wire adapter or reballing onto a reader board.
objective_ids:
  - DFO-1021
weakness_ids:
  - DFW-1023
aliases: []
source_refs:
  - DFCite-1016
updated_at: 2026-08-09
status: complete
---

# X-ray guided chip-off flash extraction

## Summary

When a target flash chip (e.g., an SoC-embedded NAND) exposes no usable in-circuit programming interface — for example, only one of the memory's required I/O lines is accessible from an external test pin, insufficient for standard ONFI-protocol dumping — the chip must instead be physically removed and read directly. Multi-layer X-ray imaging of the circuit board, taken before removal, allows the internal trace routing from each accessible test point to be mapped to its corresponding chip pin, so the removed chip's pinout is already known before it is wired to a reader.

## Details

An infrared back-heater reflow process desolders the target chip while minimizing thermal differential stress between the chip and board, reducing (but not eliminating) the risk of fracturing either. Once removed, the chip can either be reballed onto a custom adapter PCB for direct reader-socket use, or — where a custom PCB is prohibitively expensive to source for a one-off extraction — connected via a labor-intensive wire-to-wire method, soldering an individual wire to each of the chip's pins (e.g., seventeen wires: seven control, eight I/O, two VCC/GND) based on the pinout previously derived from X-ray analysis. Reduced dumping speed (signal voltage/frequency reduced below the chip's rated maximum) further lowers the error rate during the multi-hour read-out process.

## Examples

- A Google Home smart speaker's Toshiba TC58NVG1S3H NAND flash (256MB, ONFI SDR protocol) was X-rayed across all four PCB layers to trace its seven exposed test points to the chip's seventeen relevant pins, then wire-to-wire connected to a reader after infrared reflow removal, completing a 272MiB raw dump in 4 h.

## Related Objectives

- `DFO-1021` Access device data for acquisition

## Related Weaknesses

- [[weaknesses/Chip-off flash extraction is irreversible and precludes non-destructive re-examination]]

## References

- [DFCite-1016] Barral et al., 2022, "A forensic analysis of the Google Home: repairing compressed data without error correction", FSI: Digital Investigation 42-43.
