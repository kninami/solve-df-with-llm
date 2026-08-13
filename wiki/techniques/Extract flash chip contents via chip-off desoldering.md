---
id: DFT-1023
type: technique
name: Extract flash chip contents via chip-off desoldering
description: Physically desolder a device's data-storage IC from its PCB and read it out directly via a reader board or wire-to-wire adapter, as a last-resort acquisition method for devices where non-destructive methods have failed or are unavailable, using either accessible low-cost hot-air tools or, when the chip exposes no usable test points, X-ray-guided pin tracing beforehand.
objective_ids:
  - DFO-1021
weakness_ids:
  - DFW-1023
  - DFW-1120
aliases:
  - X-ray guided chip-off flash extraction
  - Cheap as chips accessible BGA chip-off methodology
  - Accessible chip-off acquisition
source_refs:
  - DFCite-1016
  - DFCite-1112
updated_at: 2026-08-12
status: complete
---

# Extract flash chip contents via chip-off desoldering

## Summary

When a target flash chip (e.g., an SoC-embedded NAND or a BGA-packaged storage IC) cannot be read non-destructively — either because no usable in-circuit programming interface is exposed, or because less invasive acquisition attempts failed outright — the chip can be physically removed from its board and read directly. A six-stage accessible methodology (deconstruction, identification, removal, restoration, determine, perform) using low-cost hot-air tools covers the general case; where the removed chip's pinout is not already known from a datasheet, X-ray tomography of the multi-layer PCB beforehand allows internal trace routing to be mapped from accessible test points to the chip's pins before removal.

## Details

**General accessible methodology**: after removing the device's outer casing and any EMI shields, the storage IC is visually identified (manufacturer marks, part numbers, and — where these are missing or shortened — internet searches and datasheet lookups) among the other components on the PCB. The chip is then desoldered using a hot-air gun or rework station with continuous thermocouple-monitored temperature control, lifted with a suction tool, scalpel, or tweezers once the solder is fully liquefied, and restored (cleaned of residual solder/adhesive with a soldering iron, solder wick, flux, and isopropyl alcohol, then re-tinned) before being read via a BGA reader adapter, flasher box, and write-blocker on an acquisition PC. This general approach does not require X-ray equipment and uses widely available tools (pry tools, screwdrivers, hot-air gun, thermocouple, soldering iron, vernier callipers), making it accessible to examiners without specialist chip-off training.

**X-ray-guided variant (no exposed test points)**: when a target flash chip exposes no usable in-circuit programming interface — for example, only one of the memory's required I/O lines is accessible from an external test pin, insufficient for standard ONFI-protocol dumping — multi-layer X-ray imaging of the circuit board, taken before removal, maps the internal trace routing from each accessible test point to its corresponding chip pin, so the removed chip's pinout is known before it is wired to a reader. An infrared back-heater reflow process desolders the chip while minimizing thermal differential stress. Once removed, the chip can either be reballed onto a custom adapter PCB, or — where a custom PCB is prohibitively expensive for a one-off extraction — connected via a labor-intensive wire-to-wire method, soldering an individual wire to each pin based on the X-ray-derived pinout. Reduced dumping speed (signal voltage/frequency reduced below the chip's rated maximum) further lowers the error rate during the multi-hour read-out process.

## Examples

- A Google Home smart speaker's Toshiba TC58NVG1S3H NAND flash (256MB, ONFI SDR protocol) was X-rayed across all four PCB layers to trace its seven exposed test points to the chip's seventeen relevant pins, then wire-to-wire connected to a reader after infrared reflow removal, completing a 272MiB raw dump in 4 h.
- In "Operation Stuck On You," a smart home device's storage IC was desoldered at 215-300°C with a hot-air gun and suction tool after commercial and open-source tools failed to acquire it, following visual identification of the IC and datasheet retrieval via web search — no X-ray was required since the datasheet already documented the pinout.

## Related Objectives

- `DFO-1021` Access device data for acquisition

## Related Weaknesses

- [[weaknesses/Chip-off flash extraction is irreversible and precludes non-destructive re-examination]]
- [[weaknesses/Chip-off removal or restoration handling can catastrophically fracture the target IC before it can be read]]

## References

- [DFCite-1016] Barral et al., 2022, "A forensic analysis of the Google Home: repairing compressed data without error correction", FSI: Digital Investigation 42-43.
- [DFCite-1112] Hadgkiss et al., 2022, "Cheap as chips: An accessible chip off acquisition method for ball grid array (BGA) integrated circuits in digital investigations", FSI: Digital Investigation 42-43.
