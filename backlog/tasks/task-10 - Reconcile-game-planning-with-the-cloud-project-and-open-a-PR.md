---
id: TASK-10
title: Reconcile game planning with the cloud project and open a PR
status: Done
assignee:
  - '@codex'
created_date: '2026-10-19 21:08'
updated_date: '2026-10-19 21:15'
labels:
  - documentation
  - repository
dependencies:
  - TASK-9
references:
  - 'https://github.com/fdurieux/spheroboy/pull/1'
documentation:
  - docs/games/README.md
  - docs/games/reconciliation.md
ordinal: 10000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Hardware records, source archives, tools, and the implementation backlog were maintained in a separate cloud checkout while game specifications and Notion pages were prepared locally. Combine the actual snapshot with the game plans so reviewers see one coherent project and the notebook links to published technical records.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 The finalized cloud snapshot is retained with its hardware evidence, sanitized source archives, tools, tests, and existing task history; game documentation adds no conflicting hardware claims or duplicate implementation backlog.
- [x] #2 The accepted standalone-screen direction, game source images and provenance, platform requirements, and three game specifications are linked from current project documentation and the Notion notebook.
- [x] #3 Relevant importer tests, maintained documentation links, image/provenance checks, and publication review pass for the combined repository.
- [x] #4 The reconciliation branch is pushed and an unmerged pull request against main is available for review.
<!-- AC:END -->

## Implementation Plan

<!-- SECTION:PLAN:BEGIN -->
1. Fetch and retain the finalized cloud snapshot and read its project guidance, hardware evidence, and backlog. 2. Reconcile game specifications with the verified hardware records, record the accepted standalone-screen choice, and link existing display/runtime tasks. 3. Validate the combined files and publish a review branch. 4. Open and attach the PR, update Notion links to the published branch, and finalize the task with evidence.
<!-- SECTION:PLAN:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
Retained finalized cloud snapshot 9538f705a2b79c029eb60feef01582f5586e691b, integrated game records and decision 0003, and linked the existing TASK-6/TASK-7 evaluation work. Published branch codex/reconcile-game-planning and opened/attached PR #1. All 11 importer tests pass locally. An exported staged tree verified 184 maintained Markdown links, JSON syntax, 24 hardware photo records and three game images with matching hashes/full decoding and no GPS EXIF. Annotation/source, manufacturer manual, and six publication-archive hashes match. Credential-pattern and reconciliation whitespace checks pass. Read back the Notion hub and four pages after adding branch-specification/PR links; all game images remain attached. GitHub reports the PR open and mergeable. Concurrent local PCB-layout changes in TASK-3, the hardware index, placement SVG, and layout assessment were excluded and preserved.
<!-- SECTION:NOTES:END -->

## Final Summary

<!-- SECTION:FINAL_SUMMARY:BEGIN -->
Reconciled the actual cloud project with Pong, Breakout, and Pac-Man planning, preserved hardware/source evidence and the existing backlog, recorded the accepted standalone-screen direction, and linked the private Notion notebook to published specifications. PR #1 is open for review. Tests, maintained links, source/photo provenance, publication checks, and Notion readback pass. No game firmware or physical-device validation is claimed; prerequisite hardware/runtime work remains in its existing tasks.
<!-- SECTION:FINAL_SUMMARY:END -->
