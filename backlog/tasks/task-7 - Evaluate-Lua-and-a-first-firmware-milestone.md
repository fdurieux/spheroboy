---
id: TASK-7
title: Evaluate Lua and a first firmware milestone
status: To Do
assignee: []
created_date: '2026-10-19 18:04'
labels:
  - firmware
  - research
dependencies:
  - TASK-2
  - TASK-4
  - TASK-5
  - TASK-6
references:
  - docs/research/conversations/README.md
documentation:
  - docs/project-brief.md
  - docs/hardware/README.md
ordinal: 7000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
The user expressed interest in Lua for a programmable wrist computer. Imported memory estimates are not target measurements; runtime selection must follow verified hardware and access findings.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 A decision record compares a Lua-capable approach with a minimal native baseline for the confirmed MCU and desired first application.
- [ ] #2 Memory estimates cite the exact target and account for interpreter, stack, drivers, and any Bluetooth or display requirements, with measurements distinguished from estimates.
- [ ] #3 The chosen next build milestone and reproducible toolchain requirements are documented, or an access blocker is identified without implying that firmware has been built.
<!-- AC:END -->
