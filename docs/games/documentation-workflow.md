# Documentation ownership

## Notion

Use the Spheroboy Games hub and four child pages for the intended player experience, recovered concept references, open product choices, relative scope, and navigation. Each game page includes its recovered image and a source link. The Shared Platform page explains cross-game dependencies in accessible terms.

Keep the game notebook private while drafting. The existing Photo inbox remains a separate upload source and is linked without moving or renaming it.

## Repository

Maintain precise rules, state transitions, acceptance criteria, technical design decisions, build/flash procedures, wiring evidence, measurements, game code, level data, and original reference files in Git. Preserve recovered source message IDs and distinguish owner decisions, assistant proposals, and newly proposed implementation details.

The combined repository retains the cloud structure. Proposed future implementation locations within it are:

```text
docs/games/                 specifications and reference images
docs/hardware/              verified connections and measurements
docs/decisions/             implementation decisions and reasons
docs/research/conversations/ immutable conversation archives
firmware/platform/          sensor, display, button, timing, audio adapters
firmware/games/             Pong, Breakout, and maze-chase game modules
tools/                      desktop harness and reproducible tools
backlog/                    Backlog.md work items
```

Reference screenshots belong under `docs/games/references/`; they are documentation sources. Production runtime assets should be authored or selected separately with their provenance recorded.

## Backlog.md

The actual [Backlog.md files](../../backlog/README.md) from the cloud snapshot are retained as the authoritative implementation backlog. Keep their IDs, dependency graph, and evidence; do not create another independently numbered task set or copy task statuses into Notion. Existing TASK-3 through TASK-7 already cover power/pin mapping, sensor capture, debug access, display evaluation, and runtime evaluation.

The work packages in [implementation-plan.md](implementation-plan.md) map to that existing backlog and describe later game work. They are not a second task board and do not declare hardware tasks complete. TASK-10 tracks this reconciliation and PR publication, rather than game implementation.

## Change workflow

1. Explore a player-facing idea in Notion and link the source evidence.
2. When a choice is adopted, update the affected repository specification or decision record.
3. Create or update one Backlog.md task with acceptance criteria and links.
4. Implement and retain validation evidence in the repository; update task status there.
5. Update Notion only when the experience, scope, decision, or demonstration changes. Link to the specification and task instead of copying their detail/status.

While the PR is under review, Notion links to records on `codex/reconcile-game-planning`. Change those links to `main` after the PR merges. The returned Notion URLs are stored in `notion-pages.json`; a private notebook link does not grant access. No automatic two-way sync is configured.
