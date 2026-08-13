---
id: DFT-1219
type: technique
name: Benchmark approximate matching algorithms using an automated test framework
description: Empirically determine which similarity-hashing (approximate matching) algorithm best suits a given forensic use case by running it through a modular, automated test framework covering efficiency (generation, comparison, compression), sensitivity and robustness (single-common-block correlation, fragment detection, alignment robustness), and adversarial resilience (digest generation impediment, digest comparison impediment, finding-the-needle), rather than choosing an algorithm from default tool settings or personal experience.
objective_ids:
  - DFO-1004
weakness_ids:
  - DFW-1105
aliases:
  - FRASHER
  - Automated approximate matching evaluation framework
source_refs:
  - DFCite-1249
updated_at: 2026-08-13
status: complete
---

# Benchmark approximate matching algorithms using an automated test framework

## Summary

No single approximate matching (AM) algorithm performs best across every forensic use case, yet algorithm selection is often made from default tool settings or informal experience rather than systematic testing. FRASHER is an open-source, modular Python framework that automates a comprehensive battery of test cases against a candidate AM algorithm, producing CSV results and visualizations so an investigator or tool developer can pick the algorithm whose strengths (or documented weaknesses) actually match the intended use case.

## Details

A JSON "playbook" configures which algorithms, test files, and test cases to run; the framework then generates or manipulates the required test files, executes each configured algorithm, and appends results back to the playbook for visualization. Test cases fall into three groups: **efficiency** (generation-time, all-vs-all and one-vs-all comparison-time, and compression-ratio measurements); **sensitivity & robustness** (single-common-block correlation as a shrinking fragment is embedded in an otherwise unrelated file; fragment detection as an original file is progressively trimmed; alignment robustness as random bytes are added to a file's head or tail); and **adversarial resilience** (digest generation impediment, testing the minimum input size/diversity an algorithm needs before it can hash at all; digest comparison impediment, testing an algorithm's resistance to content-duplication attacks; and finding-the-needle, testing an algorithm's ability to locate a specifically manipulated file within a large real-world corpus). The framework's modular, well-defined interfaces let new algorithms or test cases be integrated without re-architecting the tool.

## Examples

- Sample evaluation of six algorithms (ssdeep, sdhash, TLSH, MRSH-v2, mrsh-cf, FbHash) found TLSH performed best in both all-vs-all and one-vs-all fingerprint comparison, sdhash was fastest at digest generation, and FbHash — despite comparable accuracy — took roughly 1839 seconds to generate a digest for a 1.9 GB corpus (versus roughly 6 seconds for sdhash) and produced a 19.81 GB digest file, which the authors concluded makes it "unusable in a one-vs-all scenario ... in digital forensics because the comparison takes too long."
- In the finding-the-needle test against a 3.29 GB real-world corpus with ten distinct needle-manipulation types, mrsh-cf and MRSH-v2 consistently found the most needles regardless of file type, ssdeep performed third-best, and sdhash performed worst overall (reliably finding only two of the ten needle types); no algorithm reliably detected a needle created purely by Zlib compression.

## Related Objectives

- `DFO-1004` Conduct research

## Related Weaknesses

- [[weaknesses/Similarity digest algorithms are vulnerable to known reduction and emulation attacks with minimal input modification]]

## References

- [DFCite-1249] Göbel et al., 2022, "FRASHER -- A framework for automated evaluation of similarity hashing", FSI: Digital Investigation 42, 301407.
