---
id: DFM-1240
type: mitigation
name: Combine multiple family-specific generic YARA rule-sets and periodically extend coverage to newly identified botnet families
source_refs:
  - DFCite-1254
updated_at: 2026-08-13
status: complete
---

# Combine multiple family-specific generic YARA rule-sets and periodically extend coverage to newly identified botnet families

## Summary

Do not rely on a single IoT botnet family's generic YARA rule-set as coverage against IoT botnets in general; instead, merge rule-sets built from multiple distinct families, and periodically repeat the static-analysis process against newly identified or emerging families to extend coverage over time.

## Addresses

- [[weaknesses/Family-specific generic YARA signatures for IoT botnets fail to detect other unrelated botnet families]]

## How To Apply

Maintain a combined rule-set assembled from the generic patterns of every IoT botnet family that has been statically analyzed, rather than a single family's rule-set, and re-test the combined rule-set's detection rate against each represented family whenever a new family's rules are added, to catch any unintended interference between rules. Track detection-rate results against families outside the analyzed set (as an ongoing gap indicator) and prioritize static analysis of new or fast-growing families for inclusion, since detection rate against an unanalyzed family cannot be assumed from performance against analyzed ones.

## References

- [DFCite-1254] Abbas et al., 2021, "Generic signature development for IoT Botnet families", FSI: Digital Investigation 38, 301224.
