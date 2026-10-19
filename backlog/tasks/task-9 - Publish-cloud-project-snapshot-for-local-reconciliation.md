---
id: TASK-9
title: Publish cloud project snapshot for local reconciliation
status: In Progress
assignee:
  - '@codex'
created_date: '2026-10-19 20:52'
updated_date: '2026-10-19 21:03'
labels:
  - documentation
  - repository
dependencies: []
documentation:
  - docs/publication-checks.md
ordinal: 9000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
The local game-documentation chat needs the actual maintained cloud project files to reconcile with docs/games and open one PR. The owner authorizes a new snapshot branch based on the empty origin/main base, without force-push, merge, or PR creation here.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 The snapshot includes maintained hardware records, original conversation archive, tools and tests, photos and provenance, and backlog, while excluding credentials, temporary downloads, and unrelated session data.
- [ ] #2 The published codex/cloud-project-snapshot branch descends from origin/main commit 94a3e0fd7df129aa5359a2e78e7ef6726236f9f9, and no existing remote history is overwritten.
- [ ] #3 Importer tests, local links, archive and photo integrity, secret review, and remote commit verification are reported with material exclusions or limitations.
<!-- AC:END -->

## Implementation Plan

<!-- SECTION:PLAN:BEGIN -->
1. Finish and record the PCB front-side component review without asserting unresolved identities. 2. Preserve all existing workspace work in a recovery archive outside the checkout; fetch and verify the empty origin/main base and create the requested descendant branch. 3. Review the publication set for credentials and unrelated visitor/session metadata; retain untouched imports outside Git and sanitize only publication archive metadata and signed URLs. 4. Run importer tests, link checks, source/photo checksums, backlog validation, and staged-file review. 5. Commit and push the snapshot without force or PR creation, verify remote SHA and ancestry, then record publication completion.
<!-- SECTION:PLAN:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
Finished front-side inventory in docs/hardware/front-side-components.md; U8 remains unidentified. Preserved private recovery archive outside checkout, based requested branch on verified empty main 94a3e0fd7df129aa5359a2e78e7ef6726236f9f9. Publication review removed anonymous visitor/session bootstrap data, CSP nonces, and signed/auth URL query fields from archival metadata while preserving all 200 message bodies. Removed private metadata from 8 Notion JPEG/MPO files using ExifTool 13.59 without recompression; every decoded frame, orientation, and ICC profile is identical. Updated source vs published hashes and annotation source provenance. Added future publication checklist. Importer now reuses known sanitized publication bytes across caption edits or duplicate original sources; 11 tests pass and live import reports 8 unchanged, 0 failures. Independent text/metadata audit passes. Final staging, commit, push, and remote verification remain.
<!-- SECTION:NOTES:END -->
