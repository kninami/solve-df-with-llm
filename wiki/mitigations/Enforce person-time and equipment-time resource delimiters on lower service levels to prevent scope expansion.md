---
id: DFM-1157
type: mitigation
name: Enforce person-time and equipment-time resource delimiters on lower service levels to prevent scope expansion
source_refs:
  - DFCite-1155
updated_at: 2026-08-12
status: complete
---

# Enforce person-time and equipment-time resource delimiters on lower service levels to prevent scope expansion

## Summary

Apply and actively enforce explicit "person time" (practitioner effort) and "equipment engaged time" caps on Service Levels 1-3, and treat any client request to extend a lower service level's investigative remit as requiring a fresh Service Level Allocator consultation and a re-allocation to a higher level, rather than an informal expansion of the original allocation.

## Addresses

- [[weaknesses/Clients expand a resource-delimited digital forensic service level beyond its allocated remit]]

## How To Apply

Define and document, per Service Level, both the practitioner time and the equipment time budget for the tasks it covers, scaling equipment time dynamically to data-source size where fixed limits are impractical. When a client's mid-engagement request would exceed the allocated Service Level's defined remit, route it back through the SLA (or a Level 0 consultation) for re-allocation rather than absorbing the extra work under the original, lower-tier allocation, and periodically review actual practitioner/equipment time spent per Service Level against the defined budgets to detect systematic scope creep.

## References

- [DFCite-1155] Horsman, 2021, "Defining 'service levels' for digital forensic science organisations", FSI: Digital Investigation 38.
