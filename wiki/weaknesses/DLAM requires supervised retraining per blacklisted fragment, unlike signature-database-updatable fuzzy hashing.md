---
id: LWW-1125
type: weakness
name: DLAM requires supervised retraining per blacklisted fragment, unlike signature-database-updatable fuzzy hashing
description: Because DLAM is a supervised classifier trained to recognize a specific blacklisted fragment or fragment category, adding a newly discovered blacklisted file requires retraining (or fine-tuning) the model on labeled examples containing it, unlike traditional fuzzy hashing where a new blacklist entry can be added simply by computing and storing its hash.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-1125
source_refs:
  - LWCite-1119
updated_at: 2026-08-12
status: complete
---

# DLAM requires supervised retraining per blacklisted fragment, unlike signature-database-updatable fuzzy hashing

## Summary

The paper's own evaluation is explicitly scoped to supervised fragment detection: models are trained to distinguish between benign files and files containing a specific target fragment, using labeled training data. The authors note extending DLAM to unsupervised fragment and outlier detection is left to future work, meaning the demonstrated capability requires a labeled training set built around each fragment or blacklist category to be detected — a categorically different operational model from traditional fuzzy hashing tools such as ssdeep or TLSH, where an investigator adds a newly identified malware sample or leaked document to a blacklist simply by computing its hash and adding it to a lookup database.

## Why It Matters

In an operational setting where new malware samples or newly leaked documents are identified frequently, DLAM's retraining requirement introduces a delay and computational cost before a newly discovered blacklisted file can be detected in other evidence, compared to the near-instant signature-database update traditional approximate matching supports. An investigator choosing between the two approaches needs to weigh DLAM's higher fragment-detection accuracy against this slower, more resource-intensive update cycle for newly discovered blacklist entries.

## Related Mitigations

- [[mitigations/Pair DLAM with a traditional updatable fuzzy-hash blacklist for newly discovered files pending retraining]]

## Used By

- [[techniques/Detect blacklisted file fragments using transformer-based approximate matching]]

## References

- [LWCite-1119] Uhlig et al., 2023, "Combining AI and AM - Improving approximate matching through transformer networks", FSI: Digital Investigation 45.
