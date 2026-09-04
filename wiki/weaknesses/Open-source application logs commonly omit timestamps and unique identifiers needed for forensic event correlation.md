---
id: LWW-1292
type: weakness
name: Open-source application logs commonly omit timestamps and unique identifiers needed for forensic event correlation
description: A systematic source-code-level review of 60 open-source applications found that roughly half omitted timestamps from at least some relevant log entries and around a third lacked unique identifiers for correlating related events, meaning an investigator cannot assume an arbitrary application's default logging is adequate for timeline reconstruction or event correlation without first checking.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-1293
source_refs:
  - LWCite-1323
updated_at: 2026-08-15
status: complete
---

# Open-source application logs commonly omit timestamps and unique identifiers needed for forensic event correlation

## Summary

Of 60 open-source applications studied, 29 omitted timestamps from at least some security-relevant log entries and 23 did not record unique identifiers (UIDs) that would allow related log entries (belonging to the same user, session, or transaction) to be correlated with one another. More than half of the applications also logged predominantly unstructured, text-only events, and 35 logged exceptions inadequately for detecting attacks or misuse.

## Why It Matters

An investigator who assumes an application's logs will support timeline reconstruction or cross-event correlation, without first verifying that timestamps and UIDs are actually present in the relevant log entries, risks discovering — mid-investigation, when it is too late to remediate — that the necessary data was never recorded in the first place. This is not a rare edge case: in this study, timestamp omission and missing correlation identifiers affected roughly a third to half of the applications examined, suggesting an investigator should treat default application logging as unverified until checked, rather than assuming adequacy.

## Related Mitigations

- [[mitigations/Verify an application's logging completeness against the five-task forensic taxonomy before relying on it as a primary evidence source]]

## Used By

- [[techniques/Assess an application's log adequacy for forensic use against a five-task taxonomy]]

## References

- [LWCite-1323] Azahari and Balzarotti, 2024, "On the inadequacy of open-source application logs for digital forensics", FSI: Digital Investigation 49, 301750.
