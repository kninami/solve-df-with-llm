---
id: DFW-2123
type: weakness
name: On-scene credential-discovery frameworks cannot recover access when key information has already been destroyed
description: An on-scene credential-discovery framework can only reconstruct or extract key material that is still present somewhere in the target system's live memory, storage, or an installed application's own credential store, so if a suspect has already destroyed, wiped, or never stored the relevant key/passphrase material on any accessible system, the framework has nothing to discover, and the investigation is left with only slower, less certain offline brute-force approaches, without any documented method for handling this scenario effectively on-scene.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-2124
source_refs:
  - DFCite-2146
updated_at: 2026-08-16
status: complete
---

# On-scene credential-discovery frameworks cannot recover access when key information has already been destroyed

## Summary

The framework's own authors explicitly acknowledge this limitation: "the current framework has a limitation because it does not consider scenarios where key information for password-protected resources were destroyed. In that case, it is difficult to respond effectively on-the-scene, but during the analysis stage, brute-force attacks can be attempted using key generation algorithms." Because the framework's discovery stage depends on finding some trace of the credential material still present somewhere in accessible memory or storage, a suspect who successfully destroyed all such traces before the scene was secured leaves the framework with no discovery target at all.

## Why It Matters

An investigator relying on this class of framework as their primary approach to password-protected resources should not treat an unsuccessful discovery run as evidence that no credential material ever existed, or as grounds to abandon the target resource; it may simply mean the specific traces the framework searches for are no longer present, while the resource itself and its significance to the case remain. Because a destroyed-key scenario forecloses the framework's core fast, on-scene approach and pushes the investigation toward slower offline brute-force with no guarantee of success, the practical consequence for case timelines and outcomes can be substantial, and the investigator needs to recognize this scenario is occurring rather than assuming the framework's normal operation will eventually succeed.

## Related Mitigations

- [[mitigations/Fall back to documented offline brute-force using discovered candidate fragments when on-scene credential discovery finds no usable key material]]

## Used By

- [[techniques/Extract and reconstruct on-scene credentials using a modular discovery-analysis framework]]

## References

- [DFCite-2146] Bang, Park, and Lee, 2022, "Vision: An empirical framework for examiners to accessing password-protected resources for on-the-scene digital investigations", FSI: Digital Investigation 40, 301376.
