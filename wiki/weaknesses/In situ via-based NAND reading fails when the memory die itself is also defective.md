---
id: DFW-1112
type: weakness
name: In situ via-based NAND reading fails when the memory die itself is also defective
description: The in situ via-interconnection technique only recovers data when the NAND memory die is functional and just the controller has failed; if the memory chip itself is also defective, or the medium must be fully delayered to access transistors directly (passive voltage contrast, scanning capacitance microscopy, or atomic force microscopy), the only remaining options are destructive and risk permanent data loss.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1112
source_refs:
  - DFCite-1106
updated_at: 2026-08-12
status: complete
---

# In situ via-based NAND reading fails when the memory die itself is also defective

## Summary

The paper is explicit that a functioning memory die is a precondition: the method "is designed to assist users in retrieving the contents of the MMC, even in situations where the embedded controller fails, provided that the memory component remains functional." Where both the controller and the memory are faulty, the only remaining options require delayering the chip via SEM, AFM, or passive-voltage-contrast microscopy, and the authors caution that these techniques "involve delayering of the MMC, which can be destructive and should be avoided in legal forensics affairs, as it may result in permanent data loss."

## Why It Matters

An investigator who applies the in situ via-based technique to a medium with a defective memory die (not just a defective controller) will be unable to recover data through this non-destructive path and must decide whether to escalate to a destructive delayering technique — a decision with irreversible consequences for the evidence that should not be made without first confirming the memory die is genuinely at fault, since delayering forecloses any later re-examination.

## Related Mitigations

- [[mitigations/Reserve destructive delayering techniques for confirmed memory-die failure after non-destructive in situ reading fails]]

## Used By

- [[techniques/Read flash memory in situ via reverse-engineered PCB vias]]

## References

- [DFCite-1106] Thomas-Brans et al., 2024, "Case of study for in situ memory reading on damaged MultiMedia Card", FSI: Digital Investigation 48.
