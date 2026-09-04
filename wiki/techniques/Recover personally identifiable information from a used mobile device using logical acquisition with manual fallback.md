---
id: LWT-2055
type: technique
name: Recover personally identifiable information from a used mobile device using logical acquisition with manual fallback
description: The process of systematically examining a mobile device of uncertain or mixed ownership history (e.g. a secondhand or seized device) for recoverable personally identifiable information, by first attempting a logical acquisition with mobile forensic tools and, where the device is incompatible or acquisition fails, falling back to manual on-device examination and photographic documentation.
objective_ids:
  - DFO-1006
weakness_ids:
  - LWW-2055
aliases:
  - Secondhand mobile device PII recovery survey methodology
source_refs:
  - LWCite-2056
updated_at: 2026-08-14
status: partial
---

# Recover personally identifiable information from a used mobile device using logical acquisition with manual fallback

## Summary

When a mobile device's true ownership or usage history is uncertain - as with a secondhand device, a device recovered from an unknown location, or one that changed hands before an investigation began - an investigator first previews the device to check whether it contains data, then attempts a logical acquisition with standard mobile forensic tools; if the device is incompatible with the available tools (an unrecognized model, a locked device, or a non-functional unit), a manual examination is attempted instead, powering on the device, navigating its interface directly, and photographing the screen as data is revealed.

## Details

LWCite-2056's four-phase procedure (collection, examination, analysis, reporting) begins by previewing each device to classify it as containing data, factory-reset/wiped, password-protected, or unrecognized/non-functional; only the first category proceeds to full analysis. Acquisition uses two complementary mobile forensic tools (XRY Forensics and MobilEdit Forensic Express) for redundancy and broader device-model compatibility, always performing a logical (not physical or manual) acquisition where possible to preserve evidentiary integrity and enable analysis to occur on the resulting image rather than the original device. Where logical acquisition fails due to tool/device incompatibility, a manual examination directly on the powered-on device is used instead, with findings documented via screen photography since no forensic image can be produced this way. Recovered data across all readable device areas (contacts, messages, conversations, images, geolocation data, email, social media data) is then filtered specifically for personally identifiable information before reporting.

## Examples

- LWCite-2056's 100-device UK secondhand-market sample (April-December 2018): 72 devices were successfully logically imaged (via XRY primarily, MobilEdit as a supplementary tool), while manual examination was used for 2 of the 28 non-imageable devices, recovering rich content (a 6,464-email inbox with PayPal transaction details, 344 images, 133 contacts) from one otherwise-unacquirable device.

## Related Objectives

- `DFO-1006` Acquire data

## Related Weaknesses

- [[weaknesses/PII recovered from a used mobile device may belong to a previous owner rather than the current possessor]]

## References

- [LWCite-2056] Angelopoulou et al., "A study of the data remaining on second-hand mobile devices in the UK", Journal of Digital Forensics, Security and Law, 2022 — source of the collection/examination/analysis/reporting methodology and 100-device sample findings described above.
