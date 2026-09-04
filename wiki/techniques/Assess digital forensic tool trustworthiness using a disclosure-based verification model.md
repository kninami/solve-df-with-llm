---
id: LWT-1169
type: technique
name: Assess digital forensic tool trustworthiness using a disclosure-based verification model
description: Classify a digital forensic tool's producer along an eight-level scale of verification-evidence disclosure — from no claims at all through published specifications, undisclosed internal testing, third-party group testing, and increasingly deep accredited third-party diligence, up to fully open disclosure — to estimate the tool's trustworthiness and the residual validation effort the end-user must still perform.
objective_ids:
  - DFO-1004
weakness_ids:
  - LWW-1175
aliases:
  - Tool verification disclosure model evaluation
source_refs:
  - LWCite-1170
updated_at: 2026-08-12
status: complete
---

# Assess digital forensic tool trustworthiness using a disclosure-based verification model

## Summary

Forensic examiners and lab quality managers need a structured way to judge how much independent validation effort a given tool still requires before its output can support method validation for accreditation (e.g. ISO 17025), since tool producers vary enormously in how much verification evidence they disclose.

## Details

The eight disclosure models, in increasing order of assurance: Claim-Free (no claims made, software released as-is); Spec-Sheet-Only (functionality claimed but no test results disclosed); Internal Verification (producer tests internally but does not disclose unless forced to); External Verification (a third party tests against its own requirement subset, e.g. NIST's Computer Forensics Tool Testing program, though results may lag releases and some claims go untested); Certified Internal Diligence (a third party certifies the producer's testing and development regime as competent, without inspecting test/implementation detail); Sampled Accredited Internal Diligence, or SAID (as CID, but the third party also samples and directly observes some of the producer's actual work); Full Accredited Internal Diligence (as SAID, but all relevant producer processes are inspected, at significantly higher producer cost); and Open Diligence (producer publicly discloses requirements, test plans, data, and results for peer review and independent adoption). Each model can be mapped to an achievable Trustworthy Software Foundation trust level (0-4) and rated for producer/user liability, effort, and risk; SAID is identified as offering the best balance, redistributing validation cost from (many) end-users to the producer without exposing full implementation detail or commercially sensitive information.

## Examples

- The NIST Computer Forensics Tool Testing (CFTT) program is characterized as External Verification combined with a degree of Open Diligence (via published specifications and test suites), while the related Federated Testing project functions closer to a combination of Internal Verification, External Verification, and Open Diligence since it is executed by volunteers using the same published test materials.
- Under a Claim-Free, Spec-Sheet-Only, or undisclosed-Internal-Verification model, an accredited laboratory bears full responsibility (and cost) for independently validating every claimed tool function itself before it can support method validation for that function.

## Related Objectives

- `DFO-1004` Conduct research

## Related Weaknesses

- [[weaknesses/Forensic tool producers' non-disclosure of verification evidence prevents end-users from establishing tool trustworthiness]]

## References

- [LWCite-1170] Marshall, 2021, "Digital forensic tool verification: An evaluation of options for establishing trustworthiness", FSI: Digital Investigation 38, 301181.
