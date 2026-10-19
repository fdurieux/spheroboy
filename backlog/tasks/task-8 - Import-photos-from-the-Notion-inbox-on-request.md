---
id: TASK-8
title: Import photos from the Notion inbox on request
status: Done
assignee:
  - '@codex'
created_date: '2026-10-19 18:55'
updated_date: '2026-10-19 19:21'
labels: []
dependencies: []
documentation:
  - docs/notion-photo-inbox.md
ordinal: 8000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
The user uploads photos from a phone to a dedicated Notion page. A repeatable read-only import should preserve technical evidence in Git without manual downloads or duplicate files.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 The configured Notion inbox can be read using NOTION_TOKEN without exposing credentials or temporary signed URLs.
- [x] #2 The importer follows nested blocks and pagination and stores supported images with source references and SHA-256 checksums.
- [x] #3 Repeated imports and photos already present in the repository do not create duplicate image files; failed downloads remain retryable.
- [x] #4 Documented commands and automated checks cover import behavior, and live access and current inbox contents are verified with limitations stated.
<!-- AC:END -->

## Implementation Plan

<!-- SECTION:PLAN:BEGIN -->
1. Verify live read access to the provided inbox using the existing secure token. 2. Implement a Python standard-library importer with paginated nested block traversal, separate unauthenticated attachment downloads, checksum deduplication, and persistent provenance. 3. Test nested pages, retries after failed downloads, file changes, and repeated imports with fixtures; verify the current inbox twice. 4. Document operation and current limitations without modifying the Notion page.
<!-- SECTION:PLAN:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
Implemented the standard-library importer and configuration for the provided inbox. All 10 automated tests pass, including pagination, nesting, checksum deduplication, retries, revisions, and token isolation. Live page and block read access verified with existing NOTION_TOKEN. Two photos appeared in the inbox during setup; both downloads failed because prod-files-secure.s3.us-west-2.amazonaws.com is not allowed at runtime. Saved a network draft adding only that host while preserving api.notion.com and chatgpt.com. User must save/apply and publish settings before retrying. No successful live photo transfer is claimed; task remains In Progress.

The file-host proxy blocker is resolved. Live import succeeded: found 2, imported 2, failed 0. A second live run reported unchanged 2 and imported 0. All 10 automated tests passed again. Both downloaded photos fully decode and match recorded byte sizes and hashes. Updated docs/notion-photo-inbox.md with the verified current behavior and limitations. No Notion content was modified.
<!-- SECTION:NOTES:END -->

## Final Summary

<!-- SECTION:FINAL_SUMMARY:BEGIN -->
Implemented and documented the read-only Notion photo importer with source records, checksums, pagination, nested traversal, and duplicate prevention. All 10 automated tests pass. Live verification imported two photos successfully and skipped both unchanged on repeat. Import remains on request; no background watcher is configured.
<!-- SECTION:FINAL_SUMMARY:END -->
