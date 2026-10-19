# Spheroboy games

Implementation analysis for Pong, Breakout, and Pac-Man on the Sphero Force Band. Prepared 19 October 2026; no game implementation is claimed.

The recovered conversation confirms **Option A: a standalone wrist computer, retaining the Force Band casing and adding a screen**. Wrist gestures are the requested controls. A 128 × 64 monochrome OLED, Lua game logic, C drivers, speaker effects, and the existing button were proposed in the chat; component selection and runtime feasibility remain to be verified.

## Read the analysis

| Record | Purpose |
|---|---|
| [Shared platform](shared-platform.md) | Hardware dependencies, runtime, controls, memory, and verification |
| [Pong](pong.md) | First game: one control axis, ball physics, computer opponent |
| [Breakout](breakout.md) | Reuse Pong foundations; add bricks, lives, and level completion |
| [Pac-Man](pacman.md) | Compact maze, buffered turns, pellets, and ghost behaviour |
| [Implementation plan](implementation-plan.md) | Order, responsibilities, evidence required to proceed |
| [Documentation workflow](documentation-workflow.md) | What belongs in Notion, Git, and Backlog.md |
| [Source inventory](source-inventory.md) | Recovered decisions, proposals, conversation IDs, and image provenance |
| [Image manifest](references/manifest.json) | Original image URLs, downloaded files, sizes, and hashes |
| [Reconciliation record](reconciliation.md) | Cloud snapshot provenance, integrated records, and validation scope |

## Recommended sequence

Establish the shared hardware/runtime platform, then build **Pong → Breakout → Pac-Man**. Desktop game-logic work can proceed while physical hardware access is investigated. A desktop prototype alone does not establish Force Band feasibility.

Pong and Breakout suit the proposed 128 × 64 display. Pac-Man needs a deliberately smaller maze or a different display layout; scaling down the reference screenshot would not produce a readable game.

## Project integration

The actual cloud project snapshot at commit `9538f705a2b79c029eb60feef01582f5586e691b` has been incorporated alongside these game records. The [hardware evidence](../hardware/README.md), [conversation archive](../research/conversations/README.md), importer tools/tests, and [existing backlog](../../backlog/README.md) are retained. The [reconciliation record](reconciliation.md) explains the changes and source boundaries; the game plans do not replace measured hardware evidence or duplicate implementation task status.

Notion navigation and the review branch are recorded in [notion-pages.json](notion-pages.json). The notebook is private and requires the owner's Notion workspace access.
