---
id: TASK-11
title: Set up CHAP human decision recording
status: Done
assignee:
  - '@codex'
created_date: '2026-10-20 14:51'
updated_date: '2026-10-20 14:56'
labels: []
dependencies: []
ordinal: 11000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
The owner requested CHAP setup so explicit human decisions can be recorded with proposal evidence and rationale alongside existing Git decision records.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 A pinned CHAP coordinator supports persistent Spheroboy proposals and explicit approve, reject and override decisions.
- [x] #2 Exports can be independently verified and recovery, pending reviews and rejected decisions are tested.
- [x] #3 Usage and agent guidance explain attribution, evidence links, backups and the separation from hardware verification and Backlog status.
<!-- AC:END -->

## Implementation Plan

<!-- SECTION:PLAN:BEGIN -->
1. Pin the upstream Python coordinator and reuse its licensed review helper. 2. Add Spheroboy CLI and local review desk with persistent storage and evidence export verification. 3. Test review, restart and tamper failure paths. 4. Publish a reviewable branch and document local startup.
<!-- SECTION:PLAN:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
Implemented pinned chap-coordinator 0.3.2 with upstream review helper and loopback review desk. Validation: 51 upstream review/API/storage tests, 5 Spheroboy persistence/export/backup/CLI tests and 11 existing importer tests passed. Workspace initialized and verified locally with zero project decisions. No human approvals fabricated. Local owner startup is required; no hosted service or ChatGPT connector was installed.
<!-- SECTION:NOTES:END -->

## Final Summary

<!-- SECTION:FINAL_SUMMARY:BEGIN -->
Adds a local CHAP human-decision recorder, review desk, pinned dependency hash, evidence verifier, backup command, proposal example and agent/owner guidance. Tests cover pending and rejected results, restart, edited decisions, stale/unauthorised API calls, writer lock and export tampering. Human identity remains a declared local label; independent audit anchoring and signatures are not configured.
<!-- SECTION:FINAL_SUMMARY:END -->
