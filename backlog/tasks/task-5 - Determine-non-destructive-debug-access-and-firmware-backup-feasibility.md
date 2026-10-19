---
id: TASK-5
title: Determine non-destructive debug access and firmware backup feasibility
status: To Do
assignee: []
created_date: '2026-10-19 18:04'
labels:
  - hardware
  - tooling
dependencies:
  - TASK-3
references:
  - docs/research/conversations/README.md
documentation:
  - docs/project-brief.md
  - docs/hardware/README.md
ordinal: 5000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Atmel-ICE compatibility and target protection are unverified. Establish the access boundary before selecting a flashing workflow; this task does not authorize erase, recovery, or replacement firmware.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 The local probe and software versions and the exact non-destructive connection attempt are recorded with logs.
- [ ] #2 The result establishes readable access or a documented protection or compatibility blocker without erasing or flashing the target.
- [ ] #3 Readable firmware regions have retained backups with sizes and checksums, or the unavailable regions and preservation blocker are explicitly documented.
<!-- AC:END -->
