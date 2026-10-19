---
id: TASK-1
title: Recover hardware evidence and select the experiment device
status: Done
assignee:
  - '@codex'
created_date: '2026-10-19 18:04'
updated_date: '2026-10-19 19:21'
labels:
  - hardware
  - research
dependencies: []
references:
  - docs/research/conversations/README.md
documentation:
  - docs/project-brief.md
  - docs/hardware/README.md
  - docs/hardware/photos/README.md
  - docs/hardware/force-band-01.md
  - docs/decisions/0002-modify-existing-force-band.md
ordinal: 1000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Record the selected Sphero Force Band, readable photos of both PCB sides, the owner-confirmed instruments, and the decision to modify the existing unit. Evidence is in docs/hardware/force-band-01.md and the linked photo and decision records.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 A device identifier and readable photographs of both PCB sides are recorded in docs/hardware/.
- [x] #2 Available instruments and their model or firmware versions are recorded.
- [x] #3 The owner decision about preserving the original set and the selected experiment device is recorded.
<!-- AC:END -->

## Implementation Plan

<!-- SECTION:PLAN:BEGIN -->
1. Recover and retain the conversation photos with source references and checksums. 2. Record the existing Force Band as SB-FB-001, the confirmed equipment inventory, and the owner modification decision. 3. Import and visually review the Notion photographs of both PCB sides. 4. Verify file integrity and document the evidence before checking the acceptance criteria.
<!-- SECTION:PLAN:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
Recovered all 16 user image attachments referenced in conversation-1; conversation-2 has no user image attachments. Saved original downloaded bytes in docs/hardware/photos/ with source message and attachment IDs, filenames, dimensions, byte sizes, and SHA-256 checksums in manifest.json. Verified full image decoding, expected dimensions and sizes, and copy integrity. No visual board identification or physical measurements performed. Device selection, instrument inventory, and preservation decision remain outstanding; acceptance criteria remain unchecked.

Owner confirmed modification of the existing Sphero Force Band and ownership of Saleae Logic 8, Atmel-ICE, and Atmel Debug Adapter Shield. Recorded model names and explicitly unknown versions/revisions in docs/hardware/force-band-01.md; accepted modification decision in docs/decisions/0002-modify-existing-force-band.md. Visually reviewed all three message-116 Sphero board photos and message-129 packaging photo: all board views show the same component side, with 00-001000 / REV15 silkscreen. Assigned project identifier SB-FB-001. Acceptance criteria 2 and 3 are satisfied; criterion 1 remains incomplete because the opposite PCB side is not documented. No programming, wiring, or physical measurements performed.

Imported both Notion photos successfully. Visual inspection confirms readable views of both sides of the same Force Band PCB. The reverse side clearly shows SWDIO, SWCLK, GND, 3V3, UART, and SPI silkscreen labels. Both files are 4032 x 3024; full image decoding, byte sizes, and SHA-256 hashes verified. Updated SB-FB-001 with links to both photos. All three acceptance criteria are now satisfied; electrical pin functions and MCU specifications remain for later tasks.
<!-- SECTION:NOTES:END -->

## Final Summary

<!-- SECTION:FINAL_SUMMARY:BEGIN -->
Selected the owner’s existing Sphero Force Band as SB-FB-001, documented the modification decision and three owned instruments, and retained readable photos of both PCB sides with source records and checksums. Verified both new photos by visual inspection and full decoding. All acceptance criteria are complete; no wiring or programming was performed.
<!-- SECTION:FINAL_SUMMARY:END -->
