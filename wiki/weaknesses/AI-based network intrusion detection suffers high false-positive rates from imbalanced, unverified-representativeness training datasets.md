---
id: DFW-2015
type: weakness
name: AI-based network intrusion detection suffers high false-positive rates from imbalanced, unverified-representativeness training datasets
description: AI-based network intrusion detection systems are commonly trained and evaluated on a small set of public benchmark datasets (e.g. CICIDS-2017, CSE-CIC-IDS2018) that remain vulnerable to class imbalance and whose representativeness of real-world network traffic has no universal verification method, contributing to persistently high false-alarm rates in deployed detectors.
categories:
  - ASTM_INAC_EX
mitigation_ids:
  - DFM-2015
source_refs:
  - DFCite-2015
updated_at: 2026-08-14
status: partial
---

# AI-based network intrusion detection suffers high false-positive rates from imbalanced, unverified-representativeness training datasets

## Summary

The source survey's own "Current Challenges and Future Directions" discussion states plainly that "there is no universal way to verify the extent to which these [public] datasets represent real-world network traffic," and that even the most recent widely used datasets (CICIDS-2017, CSE-CIC-IDS2018) "are still vulnerable to excessive class imbalance problems, which can lead to low accuracy and a high false-positive rate." It further notes that despite many surveyed IDS approaches achieving high detection/alert rates, they "often also have high false alarm rates," and that "a high false-positive rate results in a high cost, since considerable resources are used in analyzing the detected activity, which ultimately turns out to be typical network traffic."

## Why It Matters

An investigator or SOC analyst relying on an AI-based NIDS whose training data does not verifiably represent the target network's real traffic risks two compounding problems: wasted investigative effort chasing false alarms (a documented, resource-costly failure mode), and reduced confidence that the detector's alerts (or lack thereof) reliably reflect genuine attack activity on the specific network being monitored, since class-imbalanced public benchmarks may not transfer accurately to a given deployment's actual traffic distribution.

## Related Mitigations

- [[mitigations/Validate AI-based NIDS models against representative private traffic and combine classifiers via meta-learning to cut false positives]]

## Used By

- [[techniques/Detect network intrusions using AI-based traffic classification]]

## References

- [DFCite-2015] Rizvi et al., 2022 — Section III.A.1 and III.B "Current Challenges and Future Directions" discussions explicitly identify dataset-representativeness and class-imbalance-driven false-positive rates as open problems across the surveyed literature.
