---
id: LWT-1107
type: technique
name: Read flash memory in situ via reverse-engineered PCB vias
description: Recover a MultiMedia Card's NAND flash contents while it remains attached to its PCB by using 3D X-ray tomography to reverse-engineer the internal signal routing between the controller and memory chip, then physically interconnecting a logic analyzer or reader to exposed PCB vias via laser-ablated, conductive-glue connections, without desoldering the chip.
objective_ids:
  - DFO-1021
weakness_ids:
  - LWW-1112
aliases:
  - In situ MMC memory reading via PCB vias
  - Via-based interconnection for damaged MMC diagnosis
source_refs:
  - LWCite-1106
updated_at: 2026-08-12
status: complete
---

# Read flash memory in situ via reverse-engineered PCB vias

## Summary

MultiMedia Card (MMC/eMMC/microSD/UFS) media typically expose debugging pads intended for manufacturing test and programming, which In-System Programming extraction relies on. Some media have no usable debugging pads and a failed controller, leaving neither ISP nor normal host communication viable; this technique establishes a physical connection directly to the PCB's internal vias instead, keeping the memory chip attached to the board rather than desoldering it.

## Details

The process has three stages. First, non-invasive preparatory work: 2D/3D X-ray imaging locates the controller and memory dies and traces PCB copper-layer routing to identify which vias correspond to which NAND flash control, data, and power signals (informed by the ONFI standard's defined pin functions), without any physical modification. Second, interconnection: since commercial via-probe solutions (Spiderboard, PCBite, Rusolut adaptors) are mechanically fragile or require intact debug pads, a home-made double-layer PCB is fabricated and thinned at the mounting point; a 1064nm infrared laser (Digit Concept Sesame Laser) ablates the resin/varnish locally over each target via to expose copper without damaging surrounding structures, and medium-viscosity conductive glue — confined to the localized opening — completes the electrical path from via to reader PCB, avoiding the destructive delayering that full chip-off or SEM/AFM-based extraction would require. Third, exploitation: a logic analyzer (e.g. Saleae Logic Pro) captures the RESET and READ_ID command/response frames during host-driven initialization to confirm the reverse-engineered signal order and read the NAND manufacturer/device ID, which is then cross-referenced against the chip manufacturer's datasheet to obtain the page/block size parameters needed to configure a reader (e.g. EASYJTAG) for a full memory dump. A successful case study on a microSD card with a failed controller (no debug pads present) identified the memory as a functional Toshiba TC58NVG2D4CTG00 (4GB) and configured a reader for its 2kB page / 256kB block geometry.

## Examples

- A microSD card that failed initial diagnostics with no visible debug pads was 3D X-rayed to trace controller-to-memory bondings, interconnected via a laser-ablated, conductive-glue-bonded homemade PCB, and its NAND manufacturer ID (98h, Toshiba) and geometry were confirmed via READ_ID frame analysis on a Saleae logic analyzer before full read-out.

## Related Objectives

- `DFO-1021` Access device data for acquisition

## Related Weaknesses

- [[weaknesses/In situ via-based NAND reading fails when the memory die itself is also defective]]

## References

- [LWCite-1106] Thomas-Brans et al., 2024, "Case of study for in situ memory reading on damaged MultiMedia Card", FSI: Digital Investigation 48.
