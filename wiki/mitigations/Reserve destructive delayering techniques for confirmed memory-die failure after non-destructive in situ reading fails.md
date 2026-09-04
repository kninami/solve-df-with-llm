---
id: LWM-1112
type: mitigation
name: Reserve destructive delayering techniques for confirmed memory-die failure after non-destructive in situ reading fails
source_refs:
  - LWCite-1106
updated_at: 2026-08-12
status: complete
---

# Reserve destructive delayering techniques for confirmed memory-die failure after non-destructive in situ reading fails

## Summary

Before resorting to destructive delayering (passive voltage contrast, scanning capacitance microscopy, or atomic force microscopy), confirm via logic-analyzer diagnosis during in situ via interconnection that the memory die itself, not just the controller, is at fault, and document that determination given the irreversible nature of delayering.

## Addresses

- [[weaknesses/In situ via-based NAND reading fails when the memory die itself is also defective]]

## How To Apply

During the in situ interconnection and exploitation phase, use the logic analyzer's captured initialization frames to determine whether the memory chip responds correctly to Reset and Read ID commands. If it does not respond, or responds with values inconsistent with any plausible manufacturer ID, treat this as evidence of memory-die failure and document it specifically before considering a destructive delayering technique. Only proceed to delayering once non-destructive in situ reading has been confirmed non-viable, and record the technical basis for that determination in the case file given that delayering precludes any later re-examination.

## References

- [LWCite-1106] Thomas-Brans et al., 2024, "Case of study for in situ memory reading on damaged MultiMedia Card", FSI: Digital Investigation 48.
