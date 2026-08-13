---
id: DFT-1217
type: technique
name: Formulate competing propositions for likelihood-ratio evaluation of Trojan horse defense claims
description: Translate the prosecution's and defense's disputed explanations for the presence of illegal content on a device into a well-formed, mutually exclusive pair of propositions — addressing a disputed actor, disputed activity, or disputed intent — suitable as input to a likelihood-ratio (LR) evaluation, rather than evaluating evidence against loosely stated or overlapping explanations.
objective_ids:
  - DFO-1003
weakness_ids:
  - DFW-1233
aliases:
  - Trojan horse defense proposition formulation
  - Hierarchy-of-propositions method for digital evidence
source_refs:
  - DFCite-1246
updated_at: 2026-08-13
status: complete
---

# Formulate competing propositions for likelihood-ratio evaluation of Trojan horse defense claims

## Summary

The likelihood-ratio framework only produces an informative evaluation if the two competing propositions it compares are relevant, mutually exclusive, and precisely capture what is actually disputed between the parties; translating a defense's alternative explanation directly and loosely into a proposition (e.g. "the traces were left by another person") without this discipline routinely yields an LR of 1.0 — an evaluation that is technically valid but tells the court nothing. This technique provides a structured method, adapted from established physical-evidence proposition-formulation guidance, for building well-formed proposition pairs specifically for Trojan horse defense and similar disputed-possession cases.

## Details

Explanations for the presence of illegal material on a device are first sorted into five categories: intentional activity by the suspect, an unintentional activity by the suspect, activity by someone else (direct perpetration, e.g. a remote intruder or another physical user), activity by something else (indirect perpetration, e.g. malware or an automated sync process — the classic "Trojan horse" claim), and other explanations such as evidence contamination. The first proposition (H1) is built by describing only the specific alleged activity that is actually disputed by the defense, using "the suspect" rather than "the user of the device" when the suspect-to-device link itself is undisputed, and using "knowingly" as an adverb (rather than characterizing the specific nature of intent) to isolate disputes over the presence of awareness from disputes over its exact character. The second proposition (H2) is then built to match, framed around whichever of three dispute types is actually at issue: a disputed actor (someone else performed the activity), a disputed activity (a different or unintentional activity occurred), or — a type specific to digital forensic casework — disputed intent (the same activity occurred, but its knowing/unknowing character is contested). The method also follows the "hierarchy of propositions" (source/activity/offense levels), explicitly permitting offense-level propositions addressing intent when the dispute requires it, and provides guidance for ambiguous or "no comment" scenarios (listing possible explanations collaboratively, evaluating multiple proposition sets, or reporting against a default background-prevalence explanation) and for "package deal" cases where multiple disputed activities should be combined into one proposition pair rather than evaluated separately.

## Examples

- For a case where both the identity of the downloader and the suspect's awareness of the files are disputed, the method arrives at H1: "Mr. X knowingly downloaded the files on the computer" versus H2: "Someone else with remote access downloaded the files on the computer; Mr. X is unaware of the presence of the files" — a disputed-actor-plus-disputed-intent pair — as opposed to a naive H1/H2 pair restating only "the suspect did it" vs. "someone else did it," which the paper shows collapses to an uninformative LR of 1.0 if the parties agree the files' mere presence is undisputed.
- For a bycatch-style Category 4 (unintentional activity) explanation, the method distinguishes an activity-level proposition pair (a different download activity occurred) from an offense-level proposition pair (the same download activity occurred, but its knowing/unknowing character is disputed), since the two require formulating structurally different H1/H2 pairs even though both stem from the same underlying "bycatch" explanation category.

## Related Objectives

- `DFO-1003` Review content for relevance

## Related Weaknesses

- [[weaknesses/Propositions translated directly from disputed explanations can yield an uninformative likelihood ratio]]

## References

- [DFCite-1246] Vink et al., 2025, "Formulating propositions in Trojan horse defense cases", FSI: Digital Investigation 53, 301915.
