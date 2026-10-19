---
id: TASK-10
title: Reconcile game planning with the cloud project and open a PR
status: In Progress
assignee:
  - '@codex'
created_date: '2026-10-19 21:08'
labels:
  - documentation
  - repository
dependencies:
  - TASK-9
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
- [ ] #1 The finalized cloud snapshot is retained with its hardware evidence, sanitized source archives, tools, tests, and existing task history; game documentation adds no conflicting hardware claims or duplicate implementation backlog.
- [ ] #2 The accepted standalone-screen direction, game source images and provenance, platform requirements, and three game specifications are linked from current project documentation and the Notion notebook.
- [ ] #3 Relevant importer tests, maintained documentation links, image/provenance checks, and publication review pass for the combined repository.
- [ ] #4 The reconciliation branch is pushed and an unmerged pull request against main is available for review.
<!-- AC:END -->

## Implementation Plan

<!-- SECTION:PLAN:BEGIN -->
1. Fetch and retain the finalized cloud snapshot and read its project guidance, hardware evidence, and backlog. 2. Reconcile game specifications with the verified hardware records, record the accepted standalone-screen choice, and link existing display/runtime tasks. 3. Validate the combined files and publish a review branch. 4. Open and attach the PR, update Notion links to the published branch, and finalize the task with evidence.
<!-- SECTION:PLAN:END -->
