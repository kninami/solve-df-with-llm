---
id: DFW-2063
type: weakness
name: Forensic toolkit completeness in recovering iOS vault-app hidden photos varies unpredictably by app and tool
description: The three tested mobile forensic toolkits each recovered a different subset of hidden vault-app photos and artifacts from the same iOS device, so no single toolkit reliably found every hidden photo across every vault app, and which artifacts were missed was not predictable from the app or tool alone.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-2064
source_refs:
  - DFCite-2066
updated_at: 2026-08-15
status: complete
---

# Forensic toolkit completeness in recovering iOS vault-app hidden photos varies unpredictably by app and tool

## Summary

Running the same imaged iPhone through three forensic software packages (UFED Cellebrite, Magnet Axiom, and Black Bag Mobilyze) produced different results per tool: Cellebrite and Axiom found all twenty images in the default iOS photo gallery, but Mobilyze did not recognize the photos assigned to two of the five vault apps and did not detect those apps on the phone at all; Axiom failed to find the twenty images in the camera roll that Cellebrite found; and Mobilyze could only detect three of the five vault apps' twelve associated pictures. Thumbnail-extension-based obfuscation (e.g., a vault app using a non-standard file extension for its thumbnail) was effective against some tools' detection logic but not others.

## Why It Matters

An investigator who runs only one forensic toolkit against a device containing vault applications risks missing hidden photos entirely — not because the photos are unrecoverable, but because that particular tool's parsing logic did not recognize the specific artifact format a given vault app happened to use. Since which artifacts are missed differs unpredictably by app-and-tool combination rather than following a simple pattern, this gap is easy to overlook without deliberately cross-checking results across more than one tool.

## Related Mitigations

- [[mitigations/Cross-validate iOS vault-app hidden-photo recovery using multiple forensic toolkits]]

## Used By

- [[techniques/Recover hidden photos from an iOS vault application's residual artifacts]]

## References

- [DFCite-2066] Gilbert & Seigfried-Spellar, 2022, "Forensic Discoverability of iOS Vault Applications", JDFSL 17(1). Reports differing per-tool detection results across Cellebrite, Axiom, and Mobilyze for the same five vault apps and twenty test images, concluding "using more than one forensic application to analyze the same image of the iPhone provides the most correct and whole picture of what evidence is on the phone."
