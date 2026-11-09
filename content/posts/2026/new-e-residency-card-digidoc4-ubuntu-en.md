Title: New e-Residency Card Not Detected by DigiDoc4 on Ubuntu 24.04? Check Your OpenSC
Slug: new-e-residency-card-not-detected-digidoc4-ubuntu
Lang: en
Date: 2026-11-09 15:30
Modified: 2026-11-09 15:30
Tags: estonia; e-residency; ubuntu; digidoc4; opensc; linux;
Status: published
Authors: Iqbal Abdullah
Summary: My new e-Residency card was not detected on Ubuntu because Ubuntu Pro's ESM repository was holding back OpenSC. Here is how to check and fix it.

I just received my replacement Estonian e-Residency card, and when I tried it right away with DigiDoc4 on Ubuntu, the card was not detected. My old card still works fine and DigiDoc4 is fully up to date, so I looked into it. It turned out that the problem was neither the card nor DigiDoc4. Ubuntu Pro's ESM (Expanded Security Maintenance) repository was keeping `opensc` at an old version that doesn't know about the new chip.

If you have Ubuntu Pro enabled and your card was issued from 17 November 2025 onwards, you might hit the same wall, so here is how to check and how to fix it.

## Background

Estonia started issuing a new generation of ID cards on 17 November 2025, and that includes the e-Resident digital ID cards. The chip changed from IDEMIA Cosmo to Thales MultiApp V5.1, and the new cards need ID-software 25.10 or later ([id.ee](https://www.id.ee/en/article/id-card-generations-supported-in-different-versions-of-the-id-software/)).

Separately, e-Residency cards issued between 10 December 2021 and 16 August 2023 (numbers UA0051053 to UA0076261) will have their certificates revoked on 9 December 2026 ([Police and Border Guard Board](https://www.politsei.ee/en/instructions/e-resident-s-digital-id/cards-issued-until-august-2023)). So many e-residents should be getting replacement cards right now, and those replacements are the new Thales cards.

## The Problem

When I inserted the new card, DigiDoc4 showed nothing and the "My eID" view stayed empty. When I inserted the old card, everything worked. The reader LED was blinking and `lsusb` could see the reader.

## Environment

- Ubuntu 24.04.5 LTS (noble), kernel 7.0.0-42-generic
- ID-software 26.7.0 (Ubuntu build), DigiDoc4 4.11.0
- Reader: ACS ACR38U-CCID
- Ubuntu Pro with ESM Apps enabled

## Diagnosis

DigiDoc4 has a diagnostics screen. To open it, first click "Settings" at the top right of the window.

![DigiDoc4 main window with the Settings link at the top right marked in red]({static}/images/estonia/digidoc4-settings.webp)

Then choose "Diagnostics" from the menu on the left. There are two places to look: the `opensc` line under `Libraries:`, and the `Smart Card readers:` section further down when you scroll.

![DigiDoc4 diagnostics screen with the Diagnostics menu item and the opensc 0.27.1-0RIA3 line marked in red]({static}/images/estonia/digidoc4-diagnostics.webp)

I took this screenshot after the fix, which is why it shows `opensc` 0.27.1-0RIA3. Before the fix, it showed this:

```
opensc (0.25.0~rc1-1ubuntu0.2+esm1)
```

With the new card inserted, the `Smart Card readers:` section shows something like this:

```
Smart Card readers:
ACS ACR 38U-CCID 00 00 max APDU size 65536
Reader state: CHANGED, PRESENT
ATR - 3BFF9600008031FE438031B85365494464B085051012233F1D
AID_IDEMIA: 6a82 (Not found)
AID_THALES: 9000 (OK)
ID - XXXXXXXXXXX
```

`AID_THALES: 9000 (OK)` means that the Thales applet on the card answered. So pcscd and the reader do see the card, and DigiDoc4 itself is a version with Thales support. That means the problem had to be in the layer between them.

On Linux, DigiDoc4 uses OpenSC (PKCS#11) to access the card. Thales support was added to RIA's OpenSC in ID-software 25.10 ([release notes](https://www.id.ee/en/article/id-software-versions-info-release-notes/)). RIA is Estonia's Information System Authority, and what I had installed instead was Ubuntu's own OpenSC from early 2024 with ESM patches on top. It predates the Thales card, so it does not know about it.

## The Root Cause

`apt policy opensc` explained why:

```
$ apt policy opensc
opensc:
  Installed: 0.25.0~rc1-1ubuntu0.2+esm1
  Candidate: 0.25.0~rc1-1ubuntu0.2+esm1
  Version table:
     0.27.1-0RIA3 500
        500 https://installer.id.ee/media/ubuntu noble/main amd64 Packages
 *** 0.25.0~rc1-1ubuntu0.2+esm1 510
        510 https://esm.ubuntu.com/apps/ubuntu noble-apps-security/main amd64 Packages
```

[RIA's repository](https://www.id.ee/en/article/install-id-software/) offers `opensc 0.27.1-0RIA3`. But Ubuntu Pro's ESM Apps repository has pin priority 510 against RIA's 500. apt looks at the priority before the version number, so `apt upgrade` will keep the old ESM package no matter how many times you run it. `apt policy opensc-pkcs11` showed the same thing.

This only happens if you have Ubuntu Pro (ESM) enabled. Without ESM, both sources are at priority 500 and apt picks the higher version, which is RIA's.

## The Solution

Install RIA's OpenSC explicitly:

```bash
sudo apt install opensc=0.27.1-0RIA3 opensc-pkcs11=0.27.1-0RIA3
sudo systemctl restart pcscd
```

If RIA has published a newer package by the time you read this, replace the version with the one shown by `apt policy opensc`.

Then pin it so that future upgrades don't go back to the ESM version:

```bash
sudo tee /etc/apt/preferences.d/ria-opensc <<'EOF'
Package: opensc opensc-pkcs11
Pin: origin installer.id.ee
Pin-Priority: 600
EOF
```

Relaunch DigiDoc4 and the new card should show up.

## After It Works

- Change PIN2 in DigiDoc4 under "My eID". New cards cannot sign until PIN2 has been changed once ([id.ee](https://www.id.ee/en/article/thales-id-card/)).
- Cards issued on or after 17 November 2025 cannot be used to authenticate to foreign e-services yet. They should work once the European Commission approves the changes to Estonia's eID scheme ([id.ee](https://www.id.ee/en/article/id-cards-issued-from-17-november-onwards-cannot-be-used-for-e-services-provided-by-foreign-countries/)).
- PUK cannot be changed on Thales cards in the DigiDoc apps ([id.ee](https://www.id.ee/en/article/thales-id-card/)).

## Things That Were Not the Problem

- The ID-software and DigiDoc4 versions (26.7 and 4.11.0 already support Thales)
- The card reader (the ACR38U works)
- pcscd (running, and it detected the card)
- Wayland vs X11

## Quick Checklist

If you see the same symptoms, check these in order:

1. Run `apt policy opensc`. Is the installed version from `installer.id.ee`?
2. In DigiDoc4 Diagnostics, does `AID_THALES` return `9000`?
3. If the answer to 1 is no and the answer to 2 is yes, install RIA's OpenSC and pin it.
