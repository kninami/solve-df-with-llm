---
id: DFM-1170
type: mitigation
name: Maintain a per-manufacturer digital-VIN reader and protocol library prioritized by component repeatability
source_refs:
  - DFCite-1175
updated_at: 2026-08-12
status: complete
---

# Maintain a per-manufacturer digital-VIN reader and protocol library prioritized by component repeatability

## Summary

Since no single universal reader can decode every manufacturer's proprietary digital-VIN protocol, a forensic laboratory should build and maintain a catalogue of manufacturer-specific readers and known digiVIN component-repeatability patterns so investigations can be prioritized by which vehicle brands are already supported.

## Addresses

- [[weaknesses/Absence of a universal digital-VIN reader across vehicle manufacturers limits bulk component-authenticity inspection]]

## How To Apply

Record, per manufacturer and model line, which components carry a digiVIN, its expected repeatability count, and the reader/protocol required to access it, building on published research and OBD-II tooling as it becomes available. When a case involves a make not yet covered, budget time to acquire or develop the appropriate reader before relying on digital-VIN evidence, and document the coverage gap in the case notes rather than assuming an absence of a reading is equivalent to an absence of tampering.

## References

- [DFCite-1175] Rak et al., 2021, "Digital vehicle identity - Digital VIN in forensic and technical practice", FSI: Digital Investigation 39, 301307.
