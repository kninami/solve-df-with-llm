---
id: DFM-2124
type: mitigation
name: Fall back to documented offline brute-force using discovered candidate fragments when on-scene credential discovery finds no usable key material
source_refs:
  - DFCite-2146
updated_at: 2026-08-16
status: complete
---

# Fall back to documented offline brute-force using discovered candidate fragments when on-scene credential discovery finds no usable key material

## Summary

When an on-scene credential-discovery framework finds no usable plaintext or key material for a target password-protected resource, capture and document whatever partial patterns, related-account passwords, or contextual information were discovered elsewhere on-scene, and use them to inform an offline brute-force or dictionary attack in laboratory analysis rather than treating the on-scene failure as final.

## Addresses

- [[weaknesses/On-scene credential-discovery frameworks cannot recover access when key information has already been destroyed]]

## How To Apply

Where [[techniques/Extract and reconstruct on-scene credentials using a modular discovery-analysis framework]] finds no directly usable key material for a specific target resource, still collect and document any related information discovered elsewhere on the same scene -- password patterns observed in other accounts belonging to the same individual, partial fragments, or contextual clues about likely passphrase structure -- since these can meaningfully narrow an offline brute-force or targeted dictionary attack's search space even without directly yielding the target credential. Explicitly record in scene documentation that key information for the specific resource could not be recovered on-scene, so the resource is flagged for continued offline attack in the laboratory rather than being deprioritized as already-exhausted. Track and periodically reassess destroyed-key cases as new key-generation and cracking techniques become available, since a resource that resists brute-force today may become tractable with future advances.

## References

- [DFCite-2146] Bang, Park, and Lee, 2022, "Vision: An empirical framework for examiners to accessing password-protected resources for on-the-scene digital investigations", FSI: Digital Investigation 40, 301376.
