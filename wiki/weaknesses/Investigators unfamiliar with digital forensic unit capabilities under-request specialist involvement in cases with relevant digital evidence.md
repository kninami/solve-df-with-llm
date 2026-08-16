---
id: DFW-2090
type: weakness
name: Investigators unfamiliar with digital forensic unit capabilities under-request specialist involvement in cases with relevant digital evidence
description: Frontline investigators and case officers decide, largely informally and without a standardized referral process, whether to call in a digital forensic unit (DFU) for a case, and a lack of familiarity with digital traces or with what a DFU can actually recover leads to cases with potentially relevant digital evidence never being referred for specialist digital forensic examination at all.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-2091
source_refs:
  - DFCite-2106
updated_at: 2026-08-16
status: complete
---

# Investigators unfamiliar with digital forensic unit capabilities under-request specialist involvement in cases with relevant digital evidence

## Summary

An ethnographic study of a Swiss cantonal police digital forensic unit (DFU) found the decision to involve the DFU in a case depends heavily on individual investigators' informal knowledge, technical familiarity, and personal working relationships with DFU members, rather than a standardized process: one interviewee explained the DFU is called "as soon as there are suspicions of a link to the Darknet, Bitcoin, or if during the investigation... it is found that they frequently use social media, belong to a geek community, or have an affinity with technology." This same lack of familiarity with the types of digital traces available or with the DFU's actual capabilities was independently identified as a significant obstacle by DFU managers, and DFU members themselves reported frustration at not being called upon for cases where they believed they could have made a meaningful contribution.

## Why It Matters

Because the referral decision is discretionary and dependent on an individual investigator's own technical awareness rather than a systematic case-assessment process, a case handled by an investigator less familiar with digital evidence's potential relevance risks having no digital forensic examination performed at all -- not because the DFU could not have found relevant evidence, but because the referral was never made. This creates an inconsistency in which cases benefit from digital forensic expertise that depends more on which officer happens to be assigned than on the case's actual evidentiary characteristics, and the resulting missed evidence is, by definition, invisible in any statistics based only on cases that were actually referred.

## Related Mitigations

- [[mitigations/Train frontline investigators on digital forensic unit capabilities and let DFU practitioners take a proactive scene-attendance role]]

## Used By

- (No technique page derived from this source; this weakness documents an organizational referral gap identified by ethnographic field observation, per the reuse-first ingestion policy for conceptual/definitional papers.)

## References

- [DFCite-2106] Ryser and Baechler, 2026, "The implementation of digital forensic science in a Swiss police force", FSI: Digital Investigation 56, 302069.
