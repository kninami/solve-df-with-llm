---
id: DFT-2061
type: technique
name: Recover a phishing website's captured victim data and server-side artifacts by mirroring its file structure
description: Download a complete, offline copy of a suspect phishing website using a website-copier tool, then inspect its recovered folder structure, index page source, and log/data files to identify how the site captures victim input and to recover the plaintext data it has already collected from victims.
objective_ids:
  - DFO-1006
weakness_ids:
  - DFW-2062
aliases:
  - HTTrack-based phishing website forensic capture
source_refs:
  - DFCite-2064
updated_at: 2026-08-15
status: complete
---

# Recover a phishing website's captured victim data and server-side artifacts by mirroring its file structure

## Summary

Once a suspect URL is identified (e.g., from a victim's browser history), download the entire site to a workstation with a website-copier tool so it can be examined offline without further interacting with the live, potentially attacker-monitored server. The recovered file tree typically exposes the site's underlying content-management system, its form-submission handler, and — critically — a log or data file where submitted victim information is stored server-side.

## Details

The recovered site structure is inspected in stages: the top-level directory listing reveals the platform used to build the fake page (e.g., a WordPress installation, identifiable from its standard `wp-content`/`wp-includes`/`wp-json` folders and an `xmlrpc.php` endpoint); the index page's "view page source" reveals the site's configuration (e.g., a WordPress RSD/service descriptor listing its registered APIs) confirming how it was built; and a log or plaintext data file in the site root is checked for captured form submissions. Because phishing forms typically collect and store every field a visiting victim submits — name, phone number, email, and case-specific fields (e.g., a fake loan-application amount and confirmation choices) — this log file can directly recover the phished data for multiple victims from a single capture, not just the one victim whose complaint triggered the investigation.

## Examples

- Downloading a suspect e-banking phishing site (`isbanh.com`, mimicking a real bank's domain) with HTTrack Website Copier revealed a WordPress-based site with an `index` file, a `log` file, and other data files at the root; the recovered `log` file contained the full-text form submissions (name, national ID/tax number, phone, email, loan-amount selection, and consent checkboxes) of at least two separate victims who had submitted their information to the fake loan-application form.

## Related Objectives

- `DFO-1006` Acquire data

## Related Weaknesses

- [[weaknesses/WHOIS-IP-based attribution of a phishing website identifies its hosting infrastructure, not necessarily the actual attacker]]

## References

- [DFCite-2064] Kara, 2021, "Don't Bite the Bait: Phishing Attack for Internet Banking (E-Banking)", JDFSL 16(5). Source of the HTTrack-based site-mirroring and recovered-log-file case study against a real e-banking phishing site.
