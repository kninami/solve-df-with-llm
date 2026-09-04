---
id: LWT-2126
type: technique
name: Identify a dashcam recording's source model using combined container metadata fingerprinting
description: Determine which dashcam make and model produced an unknown multimedia container file by comparing its chunk sequence, directory/file naming rules, on-screen watermark layout, and video decoding parameters against a reference database of these characteristics collected across known dashcam models, since no single characteristic reliably distinguishes all models on its own.
objective_ids:
  - DFO-1008
weakness_ids:
  - LWW-2136
aliases:
  - Dashcam signature database matching
source_refs:
  - LWCite-2157
updated_at: 2026-08-17
status: complete
---

# Identify a dashcam recording's source model using combined container metadata fingerprinting

## Summary

An unknown dashcam recording found without its originating device (e.g., recovered from a suspect's storage or shared online) can often be attributed to a specific make and model by comparing structural characteristics of its container file — the ordered sequence of internal chunks, the file/directory naming convention used, the layout and content of any burned-in on-screen watermark, and video decoding parameters (resolution, frame rate, codec profile) — against a reference "signature database" built by reverse-engineering known dashcam models, without needing the physical device itself.

## Details

Each of the individual characteristics has limitations in isolation: several models from the same manufacturer (or unrelated manufacturers converging on similar container-authoring libraries) can produce an identical chunk sequence — for example, three unrelated 14-model-study devices (Thepoint, FXD900, and K7) shared the same AVI chunk sequence despite being different products — and directory/file naming rules are sometimes reused verbatim across models from the same vendor. Watermark content is likewise not always device-specific, though only a minority of tested models included the specific model name in their decoded-frame watermark. Because the individual characteristics are inconsistently reliable but are largely independent of one another, combining multiple characteristics — chunk sequence plus watermark content plus decoding parameters (resolution and compression profile) — narrowed source-model identification to a unique match across all 14 models in the reference study, where no single characteristic alone was sufficient.

## Examples

- Combining chunk sequence with watermark layout and decoding-parameter (resolution/compression) fingerprints uniquely distinguished all 14 reference dashcam models, including the three models (Thepoint, FXD900, K7) that shared an identical AVI chunk sequence and so could not be told apart by chunk sequence alone.

## Related Objectives

- `DFO-1008` Establish identities

## Related Weaknesses

- [[weaknesses/Dashcam source-model identification via a single metadata characteristic is ambiguous across sibling models]]

## References

- [LWCite-2157] Lee et al., 2021, "Your car is recording: Metadata-driven dashcam analysis system", FSI: Digital Investigation 38.
