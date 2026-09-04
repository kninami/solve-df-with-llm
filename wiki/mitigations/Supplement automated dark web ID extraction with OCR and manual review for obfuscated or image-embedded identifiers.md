---
id: LWM-1273
type: mitigation
name: Supplement automated dark web ID extraction with OCR and manual review for obfuscated or image-embedded identifiers
source_refs:
  - LWCite-1300
updated_at: 2026-08-14
status: complete
---

# Supplement automated dark web ID extraction with OCR and manual review for obfuscated or image-embedded identifiers

## Summary

Supplement text-pattern-based automated identifier extraction with OCR analysis of onion service images and a manual review pass for known obfuscation patterns (such as two-layered ID encoding), rather than treating the automated extraction's output as a complete inventory of a service's external communication channels.

## Addresses

- [[weaknesses/Automated dark web identifier extraction misses obfuscated, image-embedded, or non-standard-format identification forms]]

## How To Apply

Run OCR against onion service page images and screenshots as part of the collection pipeline, in addition to text-pattern extraction, to recover identifiers embedded as images rather than plain text. Maintain and periodically update a catalog of known dark web identifier obfuscation patterns (such as two-layered encoding schemes) and apply targeted decoding rules for each during extraction. For high-priority services or investigations, follow up automated extraction with a manual review pass specifically looking for identifiers the automated pipeline may have missed, and treat the automated extraction's degree-centrality rankings as a lower bound on a given service's or identifier's true connectivity rather than a precise count.

## References

- [LWCite-1300] de-Marcos, Domínguez-Díaz and Stapic, 2026, "Mapping the Tor darkmarket ecosystem: A network analysis of topics, communication channels, and languages", FSI: Digital Investigation 56, 302032.
