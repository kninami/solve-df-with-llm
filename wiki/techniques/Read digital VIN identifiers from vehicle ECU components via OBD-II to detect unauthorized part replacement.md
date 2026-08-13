---
id: DFT-1164
type: technique
name: Read digital VIN identifiers from vehicle ECU components via OBD-II to detect unauthorized part replacement
description: Connect a manufacturer-specific reader to a vehicle's OBD-II port to read the "digital VIN" (digiVIN) values stored in individual electronic control unit components, then compare the readout against the vehicle's own VIN and the expected repeatability pattern for that model to identify components that originate from a different, potentially stolen or unauthorizedly-serviced vehicle.
objective_ids:
  - DFO-1008
weakness_ids:
  - DFW-1170
aliases:
  - Digital vehicle identity / digiVIN forensic component authentication
source_refs:
  - DFCite-1175
updated_at: 2026-08-12
status: complete
---

# Read digital VIN identifiers from vehicle ECU components via OBD-II to detect unauthorized part replacement

## Summary

Modern vehicles store a digital form of the VIN (digiVIN) inside many processor-equipped components (airbag control units, engine control modules, gateways, and others), readable via the OBD-II diagnostic port; reading and cross-referencing these values against the vehicle's registered VIN and the manufacturer's known component-repeatability pattern lets an investigator identify individual components that were removed from, or installed onto, a different vehicle without authorization.

## Details

A three-year survey of 250 vehicle models from 43 manufacturers found digital identifiers on every brand studied, in numbers ranging from a single identifier (some Korean/Japanese models) to 37 (Chrysler Grand Voyager), generally increasing with vehicle price tier and being more common in American and European models than Asian ones. Public digiVINs follow the standardized VIN structure and can therefore be validated against reference databases directly; non-public digital identifiers are manufacturer-proprietary in structure, placement, and reading protocol and typically require direct cooperation with the manufacturer to interpret, but their obscurity makes them harder for a thief or unauthorized repairer to locate and alter. Reading requires a manufacturer- (or group-) specific reading device connected through the OBD-II connector, since reading protocols and hardware are not standardized across brands; some manufacturers add "hidden trap" identifiers to unexpected components (e.g. a mirror) specifically to catch unauthorized reproduction attempts.

## Examples

- On a Jeep Gladiator, the digiVIN was read directly from the dashboard display; on other models it required a dedicated OBD-II reader connected to the vehicle's diagnostic port.
- A component bearing a digiVIN value of all-zero ("00000000000000000") indicates the manufacturer supports digital identification for that component type but chose not to populate it for that specific unit, which is distinguishable from a component whose digiVIN was deliberately altered or removed.

## Related Objectives

- `DFO-1008` Establish identities

## Related Weaknesses

- [[weaknesses/Absence of a universal digital-VIN reader across vehicle manufacturers limits bulk component-authenticity inspection]]

## References

- [DFCite-1175] Rak et al., 2021, "Digital vehicle identity - Digital VIN in forensic and technical practice", FSI: Digital Investigation 39, 301307.
