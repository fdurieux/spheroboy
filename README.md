# Spheroboy

Explore turning a Sphero Force Band into a general-purpose programmable wrist computer, with motion-controlled games as a possible first application.

The project is in hardware discovery. The MCU is confirmed as an nRF52832-QFAA with 512 KiB flash and 64 KiB RAM; see the [memory evidence](docs/hardware/mcu-and-memory.md). No firmware, working display integration, or electrically verified board pinout exists in this repository yet. Remaining component and tool-compatibility claims still need verification.

## Start here

- [Project brief](docs/project-brief.md): goals, evidence, assumptions, and open questions.
- [Research conversations](docs/research/conversations/README.md): two imported conversations and their original archives.
- [Hardware record](docs/hardware/README.md): component candidates, measurements, photographs, and pin mapping.
- [Front-side components](docs/hardware/front-side-components.md): identified chips, connectors, controls, and unresolved parts.
- [Annotated PCB pad reference](docs/hardware/pad-reference.md): candidate GND, supply, and SWD points with pending measurements.
- [Decisions](docs/decisions/README.md): accepted choices and their reasons.
- [Backlog](backlog/README.md): actionable work and acceptance criteria.
- [Project notebook template](docs/notion-notebook.md): a starting page to import into Notion.
- [Publication checks](docs/publication-checks.md): evidence provenance and metadata checks required before public pushes.
- [Notion photo inbox setup](docs/notion-photo-inbox.md): grant read access for imports requested in chat.

## Repository layout

```text
backlog/                       Backlog.md configuration and task files
docs/
  project-brief.md              Current project context
  notion-notebook.md            Notion page template
  research/conversations/       Markdown transcripts and HTML/JSON archives
  hardware/                    Hardware findings and evidence conventions
  decisions/                   Decision records
firmware/                      Future embedded implementation
tools/                         Future capture analysis and development tools
captures/                      Capture metadata and evidence storage guidance
```

## Working with the backlog

Tasks are ordinary Markdown and can be read without installing anything. To use the CLI, install Node.js and npm; Node.js 24 was used to validate Backlog.md 1.54.0 for this initial setup.

From the repository root:

```bash
npx --yes backlog.md@1.54.0 task list --plain
npx --yes backlog.md@1.54.0 task list --ready --plain
npx --yes backlog.md@1.54.0 task view TASK-1 --plain
npx --yes backlog.md@1.54.0 board
```

Use this pinned CLI version for task changes. The project is already initialized; there is no need to run `backlog init`. Automatic commits and remote branch queries are disabled. See [backlog guidance](backlog/README.md) for creating and updating tasks.

TASK-1's evidence collection and TASK-2's MCU identification are complete. Next is TASK-3: document power rails and candidate debug connections. Hardware measurements and debugger connections require local access to the Force Band and instruments; the cloud workspace can maintain records, inspect uploaded evidence, and develop software.

## Where information belongs

Use Notion for the project overview, idea collection, progress photos, and informal lab journal. Use Git for technical records, evidence metadata, decisions, and code. Use Backlog.md for task status. Link between them rather than maintaining duplicate task boards or competing technical specifications.

The project notebook template is prepared locally. Import its Markdown into Notion and replace its link placeholders with your repository URLs. Once imported, maintain the notebook in Notion; the template remains a starting point. A separate [photo inbox](docs/notion-photo-inbox.md) is connected for read access, with an on-request importer and its current transfer status documented there.

## Working with ChatGPT and Codex

Either can help with research and hardware reasoning. Codex can also maintain this repository, analyze uploaded captures, and run available development tools. Give either assistant the project brief and relevant evidence; other chats and Notion pages are not automatically available. Record useful conclusions with their sources, and keep hypotheses distinct from measurements.

## Development status

There is no application build or test suite yet. The firmware toolchain will be selected after the MCU, debug access, and first implementation target are established. Do not treat example commands or compatibility claims in the archived conversations as verified procedures for this board.
