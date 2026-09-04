---
id: LWT-1283
type: technique
name: Detect software supply chain attack behaviors in binaries using semantic-graph queries and Bayesian malicious-intent scoring
description: Identify a compiled Windows binary as likely compromised by a software supply chain attack (SSCA) by matching its data-flow, control-flow, and AST-annotated semantic graph against queries encoding known SSCA characteristic behaviors, then scoring each match's malicious intent using Bayesian inference calibrated against large ground-truth corpora of malware, benign, and Windows 10 binaries.
objective_ids:
  - DFO-1019
weakness_ids:
  - LWW-1293
aliases:
  - SSCA investigative framework
  - Parametric momentum data-flow metric
source_refs:
  - LWCite-1325
updated_at: 2026-08-15
status: complete
---

# Detect software supply chain attack behaviors in binaries using semantic-graph queries and Bayesian malicious-intent scoring

## Summary

A software supply chain attack delivers malicious code through an otherwise-trusted, digitally-signed vendor binary, bypassing the source-code-level defenses (code review, bug reports) that would normally catch it — leaving the compiled release binary as the last inspectable artifact. Characterizing the code behaviors common to known SSCAs as queries over a binary's semantic graph, then using Bayesian inference over large reference corpora to assess how strongly each matched behavior indicates malicious intent, lets an investigator flag SSCA-consistent behavior in a binary under examination without needing its source code.

## Details

Seven prominent, well-documented SSCAs (including ShadowHammer/ASUS Live Update and CCleaner) were manually dissected to extract their characteristic malicious code behaviors, each expressed as a query over a semantic graph built from a binary's data-flow, control-flow, and abstract-syntax-tree annotations. These queries were then run against a ground-truth corpus of over 10 million functions drawn from three classes — malware, benign software, and Windows 10 system binaries — and three-way Bayesian inference over the resulting match counts assessed how strongly the presence of each behavior indicates malicious intent, rather than treating a match as a binary yes/no signal. Each behavior was further annotated with contextual information (e.g. which specific API calls or code patterns co-occur with it) that, when applied as an additional filter over matched samples, further sharpened the malicious-intent signal. A separate novel data-flow metric, "parametric momentum," was found to be a powerful standalone indicator, flagging a meaningful fraction of malware samples with zero false positives when used alone.

## Examples

- The presence of any single characterized SSCA behavior within a binary was found to indicate malware with 86-100% probability across the tested behaviors.
- Annotating a matched SSCA behavior with contextual co-occurrence information and filtering on it boosted the assessed malicious-intent probability by up to 30% relative to the unfiltered behavior match alone.
- The standalone "parametric momentum" data-flow metric alone flagged 12.71% of the malware corpus with zero false positives, without requiring any of the other characterized SSCA behavior queries.
- A temporal analysis found that the characteristic behaviors used by the seven studied SSCAs had existed in software (in some prior, non-malicious or differently-used form) for 13-21 years before being weaponized in the actual attack — time during which, the authors argue, the behavior could plausibly have been identified and mitigated had this kind of behavior-based detection been applied proactively.

## Related Objectives

- `DFO-1019` Detect anti-forensics and other anomalies

## Related Weaknesses

- [[weaknesses/Software supply chain attack behavior detection depends on previously characterized queries and cannot detect a not-yet-catalogued attack behavior]]

## References

- [LWCite-1325] Andreoli, Lounis, Debbabi, and Hanna, 2023, "On the prevalence of software supply chain attacks: Empirical study and investigative framework", FSI: Digital Investigation 44, 301508.
