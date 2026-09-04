---
id: LWT-2117
type: technique
name: Extract and reconstruct on-scene credentials using a modular discovery-analysis framework
description: Access password-protected resources (encrypted disks/containers, cryptocurrency wallets, secure messenger accounts) during an on-scene search and seizure by running a four-stage modular framework -- pre-definition (configuring target signatures/patterns), discovery (scanning live memory and storage for credential-related artifacts), analysis (reconstructing plausible passphrases from discovered fragments and verifying them against the target), and post-processing (validating and documenting results) -- rather than relying only on cooperative disclosure or later offline brute-force alone.
objective_ids:
  - DFO-1016
  - DFO-1015
weakness_ids:
  - LWW-2123
aliases:
  - Vision (on-scene credential-access framework)
source_refs:
  - LWCite-2146
updated_at: 2026-08-16
status: complete
---

# Extract and reconstruct on-scene credentials using a modular discovery-analysis framework

## Summary

Password-protected resources -- full/file-based disk encryption, cryptocurrency wallets, and secure messenger accounts -- are increasingly common obstacles at search-and-seizure sites, where a suspect may be uncooperative and a live, running system is often the most realistic opportunity to obtain the key material needed to access them later. A modular four-stage framework (pre-definition, discovery, analysis, post-processing) systematically searches a live system's memory and storage for credential fragments (browser-saved passwords, cryptographic keys, partial passphrases), reconstructs a plausible passphrase or key from what is found, and verifies it against the actual protected target before the scene is left.

## Details

**Pre-definition** configures, in advance, the target applications/services to search for (identified by file name/path/size), the pattern-match definitions for credential extraction (regular expressions and format signatures for cryptocurrency public/private keys, Tor onion domains, messenger key structures), and the similarity-measure functions (cryptographic key search methods) the later stages will use -- all stored in a reusable, extensible JSON configuration, letting the framework's coverage grow as new applications/services are added without changing its core code. **Discovery** operates in three sub-stages: an optional pre-exploration stage identifies installed applications relevant to analysis via file metadata without altering the file system; search and identification then applies either pattern-match actions (regular expressions, code structures, format signatures for known credential types) or similarity-measure actions (high-entropy-region detection, structural-property analysis, key-schedule search) against both memory (including swap/pagefile/hiberfil) and storage; and collection extracts credential information already stored in identified applications (web browsers, email clients, FTP/SSH/VPN clients) using per-application credential-extraction modules. **Analysis** reconstructs a usable credential from whatever the discovery stage found: if a plaintext password fragment or pattern was recovered, pattern generation and word generation build a targeted dictionary of case-specific candidate passphrases (using a Markov-model-based approach for generating realistic variants) rather than relying on a generic wordlist; if only a binary hash value was recovered, a rainbow-table lookup attempts to find a matching plaintext; a verification sub-stage then confirms the reconstructed candidate actually decrypts or authenticates against the specific target (e.g. validating a recovered cryptocurrency private key against its claimed balance, or a recovered password against the specific locked device/service). **Post-processing** validates the overall chain of acquired/decrypted materials and documents the process (source, method, and result for each recovered credential) into a report suitable for continued use both on-scene and in later laboratory analysis.

## Examples

- Case study 1 (cryptocurrency investment fraud): running the framework's discovery process against two powered-on desktop computers recovered 47 web-browser-stored ID/password pairs, 143 cryptocurrency public keys and 28 private keys embedded in the suspect's own source code (hard-coded, covering 64 and 25 balances respectively), plus 3 cryptocurrency recovery keys and 2 wallet application installations from the filesystem -- collectively enabling immediate seizure of over USD 500,000 in identified cryptocurrency to a controlled paper wallet before the scene was left.
- Case study 2 (drug-dealing investigation): discovery on an uncooperative buyer's laptop recovered 32 web-browser ID/password pairs and 4 cryptocurrency public keys; analysis used a recovered fixed-format password pattern (a fixed string component plus service-specific first-letter-uppercase and numeric suffix conventions) to successfully authenticate to the suspect's messenger application installed on the laptop, recovering chat logs and additional cryptocurrency addresses that became the starting point for tracking the seller.
- Case study 3 (obstruction-of-business case): discovery recovered 23 web-browser credential pairs, a Truecrypt trace in Prefetch, a BitLocker-enabled registry entry, 4 BitLocker disk-encryption keys from physical memory, and an installed SSH client (Putty) with a saved server address; analysis used web-browser password patterns to derive a fixed-format passphrase that successfully decrypted a Truecrypt-encrypted USB storage device found at the scene, recovering source code and a development log used to establish the timeline of the underlying obstruction offense.

## Related Objectives

- `DFO-1016` Overcome protection mechanisms
- `DFO-1015` Prepare for a digital investigation

## Related Weaknesses

- [[weaknesses/On-scene credential-discovery frameworks cannot recover access when key information has already been destroyed]]

## References

- [LWCite-2146] Bang, Park, and Lee, 2022, "Vision: An empirical framework for examiners to accessing password-protected resources for on-the-scene digital investigations", FSI: Digital Investigation 40, 301376.
