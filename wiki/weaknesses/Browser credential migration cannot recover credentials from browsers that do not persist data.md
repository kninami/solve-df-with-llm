---
id: DFW-1055
type: weakness
name: Browser credential migration cannot recover credentials from browsers that do not persist data
description: Browser credential migration depends on the source browser having written session credentials to local storage in the first place; browsers that operate only in incognito/private mode by design, or privacy-focused browsers such as Tor that deliberately avoid persisting session data, leave nothing on disk to extract, so this technique cannot recover credentials from them regardless of how the migration and re-encryption steps are executed.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1055
source_refs:
  - DFCite-1045
updated_at: 2026-08-09
status: complete
---

# Browser credential migration cannot recover credentials from browsers that do not persist data

## Summary

Of the 28 browsers tested for migration, three (including Tor, and two others that support only an incognito-equivalent mode) do not save user data at all, and were confirmed unable to support this technique. All other 25 browsers, spanning Chromium-, Firefox-, and Internet Explorer-based lineages, did successfully support credential migration, whether directly (Firefox/IE-based) or after decryption/re-encryption (Chromium-based, using DPAPI).

## Why It Matters

If a suspect used a privacy-focused or incognito-only browser specifically to access cloud services, this technique provides no path to recovering their session credentials from that browser, regardless of investigator skill or effort — the underlying data simply was never written to disk. An investigator should confirm which browser(s) a suspect actually used, and whether that browser persists data at all, before planning a credential-migration-based access strategy, since three of 28 commonly used browsers in the study offered no path to migration.

## Related Mitigations

- [[mitigations/Confirm the target browser persists credential data before planning credential migration]]

## Used By

- [[techniques/Access a cloud account using captured credentials]]

## References

- [DFCite-1045] Hur et al., 2023, "A study on cloud data access through browser credential migration in Windows environment", FSI: Digital Investigation 45.
