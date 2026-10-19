---
id: TASK-2
title: Confirm the MCU identity and memory specifications
status: Done
assignee:
  - '@codex'
created_date: '2026-10-19 18:04'
updated_date: '2026-10-19 19:38'
labels:
  - hardware
  - research
dependencies:
  - TASK-1
references:
  - docs/research/conversations/README.md
documentation:
  - docs/project-brief.md
  - docs/hardware/README.md
  - docs/hardware/mcu-and-memory.md
ordinal: 2000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Identify the exact Force Band MCU variant from its package marking and manufacturer documentation, then record its flash, RAM, supply range, and debug interface. The new Notion close-ups provide readable evidence for nRF52832-QFAA.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 The MCU marking is linked to a readable photograph and exact manufacturer part documentation.
- [x] #2 Flash, RAM, supply limits, and debug interface for the confirmed variant are recorded with source references.
- [x] #3 The project brief is updated to distinguish the confirmed identity from earlier hypotheses.
<!-- AC:END -->

## Implementation Plan

<!-- SECTION:PLAN:BEGIN -->
1. Import and inspect the new Notion close-ups, transcribing MCU and external-memory markings separately from interpretations. 2. Retrieve official Nordic and memory-manufacturer documentation and resolve the exact variants, capacities, supply limits, and debug interface. 3. Record photo and documentation evidence and practical memory-budget limits. 4. Update the project brief and check only supported acceptance criteria.
<!-- SECTION:PLAN:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
Imported three new Notion close-ups, verified their sizes and hashes, and fully decoded them. Read U1 as N52832 / QFAAB0 / 1616BB. Retrieved Nordic’s manufacturer-authored Product Specification v1.0 through SparkFun’s pinned archival copy because the manufacturer portal is blocked. Section 52.4 table 129 explicitly maps AA to 512 kB flash and 64 kB RAM; sections 6, 7, and 16 document 1.7–3.6 V VDD, 64 MHz Cortex-M4F, and SWD. Cross-checked FICR memory constants in Nordic nrfx headers. External U9 shows Winbond 25Q40, consistent with 512 KiB SPI flash per flashrom’s database; exact suffix and voltage remain unconfirmed. Recorded evidence and limits in docs/hardware/mcu-and-memory.md and updated the project brief. No hardware measurements or firmware reads performed.
<!-- SECTION:NOTES:END -->

## Final Summary

<!-- SECTION:FINAL_SUMMARY:BEGIN -->
Confirmed nRF52832-QFAA from the new package photograph and Nordic’s marking table: 512 KiB internal flash, 64 KiB RAM, 64 MHz Cortex-M4F, 1.7–3.6 V rated VDD, and SWD. Updated evidence records and project context. External W25Q40-family storage is consistent with 512 KiB, with exact suffix and voltage unresolved. The new photos verify identity, not actual rail voltage or debug access.
<!-- SECTION:FINAL_SUMMARY:END -->
