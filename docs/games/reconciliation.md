# Cloud and game-planning reconciliation

Date: 2026-10-19. Work record: TASK-10 in the [existing backlog](../../backlog/README.md). Review: [PR #1](https://github.com/fdurieux/spheroboy/pull/1).

## Source snapshot

The maintained cloud project was published on `codex/cloud-project-snapshot` at commit **9538f705a2b79c029eb60feef01582f5586e691b**, descending from the empty initial `main` commit `94a3e0fd7df129aa5359a2e78e7ef6726236f9f9`. The reconciliation branch retains that history and adds the local game records. It does not reconstruct the cloud files from chat summaries.

Retained records include the root guidance, project brief, hardware inventory and measurements-to-do, 24 hardware photo records and annotation, original 179 + 21 conversation message bodies, manufacturer manual, Notion importer and tests, and TASK-1 through TASK-9. Cloud snapshot publication is recorded by TASK-9. No hardware task has been declared complete by this integration.

## Reconciled differences

- The full original conversation import stops before the game discussion. A six-message extract from the newer owner-supplied share supplements it, with all three game reference images and their hashes.
- The newer share includes the owner's Option A selection. [Decision 0003](../decisions/0003-standalone-wrist-display.md) records the standalone wrist-screen direction without selecting an exact module, runtime, or pinout.
- The game documents now link to the actual [MCU evidence](../hardware/mcu-and-memory.md) and [component inventory](../hardware/front-side-components.md). U8 remains unidentified; the audio marking alone does not verify a usable audio driver or wiring.
- TASK-3 through TASK-7 remain the prerequisite work for electrical mapping, motion capture, debug access, display, and Lua/runtime evaluation. The game work packages reference them instead of creating a second backlog.
- The root README and brief now point to the game specifications and private Notion notebook. The notebook links to the review branch while the PR is open.
- Machine-specific paths and internal Notion attachment identifiers were removed from the public game-page index.

## Publication and preservation

The cloud snapshot's [publication record](../publication-checks.md) documents metadata-only sanitation of eight Notion photos, unchanged decoded pixels/orientation/ICC profiles, separate original/published checksums, and removal of visitor/session data and signed query credentials from archive metadata. The original raw cloud files remain in the private recovery archive, outside Git. The published conversation message bodies remain unchanged.

The three game reference images were recovered from the resolved image records in the newer chat and saved without editing their downloaded bytes. Their [manifest](references/manifest.json) records exact source URLs, file sizes, hashes, and decoded dimensions. These are documentation references, not production game assets.

## Verification scope

Verify the combined checkout using the existing importer test suite, maintained Markdown links, JSON parsing, photo hashes/full decoding/GPS checks, and annotation/manual/archive provenance. Review the staged publication set for credentials, session data, and unrelated local files. TASK-10 records the observed results and the PR link after publication.

The combined staged tree passed all 11 importer tests, 184 maintained Markdown-link checks, JSON parsing, and hash/full-decode/GPS checks for 24 hardware photos and three game images. Annotation, manufacturer-manual, and all six archive-publication hashes match their records. The publication credential-pattern scan and reconciliation whitespace checks also passed. The Notion project hub and four game/platform pages were read back after updating their specification and PR links; all three game images remain attached. Separate local PCB-layout edits were excluded from this PR and left untouched.

There is no firmware build, working game, display integration, measured board pinout, or new physical-device validation in this PR. Those remain future work behind the documented prerequisites.
