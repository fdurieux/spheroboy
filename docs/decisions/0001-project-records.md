# 0001: Project records and task ownership

Status: Accepted  
Date: 2026-10-19

## Context

Spheroboy combines exploratory hardware research, archived conversations, and future firmware development. The user accepted a workflow using Notion, Git, and Backlog.md.

## Decision

- Use Notion for the overview, informal lab journal, ideas, and progress photographs.
- Keep technical findings, evidence metadata, accepted decisions, conversations, and code in Git.
- Keep actionable work and its status in Backlog.md.
- Link from the notebook to repository documents and tasks. Maintain accepted technical facts in repository documents rather than duplicating them in Notion.
- Preserve imported conversations as historical sources and verify their hardware claims before treating them as established.

## Consequences

Codex can maintain project context and tasks through repository files. ChatGPT remains useful for exploration when supplied with relevant context. Useful results from either assistant should be incorporated with evidence. The local Notion template needs importing manually; no synchronization or external Notion write is configured.
