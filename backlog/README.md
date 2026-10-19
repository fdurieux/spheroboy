# Project backlog

Backlog.md is the task status record for Spheroboy. Tasks live in `tasks/`; configuration is in `config.yml`. Tasks start unassigned and To Do. Hardware acceptance criteria require physical evidence; creating a task does not verify its premise.

Run from the repository root:

```bash
npx --yes backlog.md@1.54.0 task list --plain
npx --yes backlog.md@1.54.0 task list --ready --plain
npx --yes backlog.md@1.54.0 task view TASK-1 --plain
npx --yes backlog.md@1.54.0 board
```

For task changes, use the CLI to preserve its format:

```bash
npx --yes backlog.md@1.54.0 task create "Investigate a specific question" \
  --description "Context and evidence needed" \
  --ac "An observable completion condition"
npx --yes backlog.md@1.54.0 task edit TASK-1 --status "In Progress"
```

Run `npx --yes backlog.md@1.54.0 instructions overview` before using it as an agent. Tasks should link to research and record observable acceptance criteria. Keep findings in `docs/hardware/`, captures metadata in `captures/`, and accepted choices in `docs/decisions/`. Record evidence and satisfy the criteria before marking Done.

The initial sequence covers evidence recovery, MCU identification, pin mapping, sensor capture, debug access and backup feasibility, display evaluation, and runtime evaluation. Dependencies express prerequisites rather than proof that a hypothesis is true. If a target or interface hypothesis is disproved, update dependent tasks before proceeding.
