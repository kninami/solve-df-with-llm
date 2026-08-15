---
id: DFT-1263
type: technique
name: Transplant a damaged device's electronic components onto a donor board using dental burr lapping
description: Repair a device whose main board is too badly damaged to power on or read by transferring its critical components (memory, processor, or crypto-chip) onto an identical, functional donor board, using a dental control unit's burr and drill (rather than hot-air desoldering) to lap away the damaged board's material layer by layer and free the components without overheating or physically stressing them, then re-soldering them onto the donor board.
objective_ids:
  - DFO-1021
weakness_ids:
  - DFW-1023
aliases:
  - Forensic IT transplantation
  - Donor board preparation by dental burr lapping
source_refs:
  - DFCite-1302
updated_at: 2026-08-14
status: complete
---

# Transplant a damaged device's electronic components onto a donor board using dental burr lapping

## Summary

Analogous to a human organ transplant, this technique replaces a damaged phone or device's non-functional main board with a healthy, identical donor board by physically moving the critical memory/processor/crypto components across: the donor board's own equivalent components are first removed and discarded, then the damaged board's own components are freed using a dental control unit's rotating burr to grind away the surrounding board material in controlled layers (rather than heat-based desoldering, which risks damaging an already-compromised component), and finally re-soldered onto the prepared donor board to produce a single functional assembly that can be powered on and read normally.

## Details

Because small, densely-packed electronic components are not held to the PCB uniformly like a tooth's roots (some are centered, some peripheral, some irregularly patterned), a CNC milling machine cannot apply the required non-uniform, judgment-based force safely, making a manually operated dental burr — offering fine, real-time tactile control the operator can adjust continuously — better suited to this task than automated milling despite its lower geometric precision. Two burr materials are used depending on hardness needs: diamond burrs (very sensitive, prone to rapid wear on hard materials) and tungsten carbide burrs (more robust and aggressive, requiring careful speed/torque control on sensitive board areas), with a flame-shaped tungsten carbide burr (run between 5,000-50,000 rev/min at low torque) offering the most consistent contact area across the varied surface orientations found around a target component. The operator progressively removes material in from the package's periphery toward the component, tracking the component's estimated internal layer count (informed by prior 2D/3D X-ray imaging) to change to progressively finer-grained burrs as the copper layer nearest the component's own PCB is approached, minimizing the risk of damaging the component itself in the final passes; a fine surgical blade removes the last surrounding ring of material once the component's own solder balls become visible. The prepared donor board then receives the freed component: old solder and resin residue is cleaned from both the donor board's now-empty footprint and the freed component's contacts, and the component is re-soldered into place before a final check confirms no short circuits or missing solder balls resulted from the reballing process.

## Examples

- Preparing a donor board for an iPhone's CPU by dental burr lapping proceeded in two visually distinguishable phases (an initial coarse removal phase and a final fine-polish phase immediately around the component), successfully freeing the CPU package intact for transplantation.
- Applying too much downward pressure with the burr, rather than letting the tool's own rotation do the cutting work, was identified as the primary operator error risk — correct technique uses minimal applied pressure and relies on burr rotation speed and material choice to control removal rate, since excessive force risks producing an uneven surface or a trench that damages an adjacent, still-needed component or trace.

## Related Objectives

- `DFO-1021` Access device data for acquisition

## Related Weaknesses

- [[weaknesses/Chip-off flash extraction is irreversible and precludes non-destructive re-examination]]

## References

- [DFCite-1302] Heckmann, Souvignet, Sauveron and Naccache, 2021, "Medical Equipment Used for Forensic Data Extraction: A low-cost solution for forensic laboratories not provided with expensive diagnostic or advanced repair equipment", FSI: Digital Investigation 36, 301092.
