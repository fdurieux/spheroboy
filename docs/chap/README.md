# Spheroboy human decisions with CHAP

This is a local, single-operator decision recorder, using **chap-coordinator
0.3.2** (public draft) and the upstream review desk. It records proposals,
explicit human approvals, rejections, edited approvals, reasons and evidence.
It performs no hardware operations and does not change Backlog task status.

## Start on your computer

Requirements: Git and Python 3.10 or newer, with venv and pip. From this repository:

```sh
python3 -m venv .venv-chap
.venv-chap/bin/python -m pip install --require-hashes --only-binary=:all: -r tools/chap/requirements.txt
.venv-chap/bin/python tools/chap/chap.py init
.venv-chap/bin/python tools/chap/chap.py serve
```

On Windows, use `.venv-chap\Scripts\python.exe` instead of
`.venv-chap/bin/python`. The desk opens a private **127.0.0.1** link. Keep its
reviewer token private. Stop with Ctrl-C; pending reviews and decisions survive.
Use `serve --port 0` if the default port 7331 is occupied. Restarting rotates
connection tokens. Never expose this demo server to a network or reverse proxy.

The workspace is `wsp_spheroboy`; the reviewer label is `human:fdurieux`.
API proposals are attributed to `agent:spheroboy-assistant`; browser-pasted
proposals to `agent:manual-submission`. These are declared labels, not verified
identities. Put the actual author/tool and source reference in proposal evidence.
No sample task or historical approval is automatically inserted.

## Record a decision

1. Prepare a JSON proposal using [the example](../../tools/chap/proposal.example.json).
   Replace the example content and commit placeholder. Include the subject,
   exact proposed action, evidence at a specific commit or content hash,
   conditions and the Backlog task ID. Keep essential review context inside
   `draft`, because its digest is what the decision binds.
2. While the desk is stopped, run:

   ```sh
   .venv-chap/bin/python tools/chap/chap.py propose /path/to/proposal.json
   .venv-chap/bin/python tools/chap/chap.py list
   .venv-chap/bin/python tools/chap/chap.py serve
   ```

   Alternatively, paste the draft object into the running desk. Agents may
   submit through the local API below while the desk owns the database.
3. Read the proposal and referenced evidence. Approve, reject, or edit and approve.
   Give a reason for every decision; the upstream desk enforces it for edits
   and rejections. An unanswered review remains pending. To request changes,
   reject with reasons and submit a revised proposal linked to the rejected one.
4. Export evidence and link the CHAP task ID and export in the accepted
   `docs/decisions/` record. Backlog.md remains the project task status record.

For a terminal review, stop the desk and use `review TASK_ID`. It displays the
full record, requires interactive input and a reason, and leaves a blank answer
pending. Agents must never drive this human-review command or use the reviewer
capability. No signature is fabricated on your behalf.

Approval is not proof of a PCB connection, measurement, successful test or safe
flash procedure. Record those facts separately, with their evidence. A decision
about a draft does not approve later edits to that draft or a different commit.
Superseding decisions need a new proposal referring to the earlier task ID;
old decisions remain in the log. Existing ADRs 0001–0003 remain historical
records. Any later import must identify its original source/date and import date,
and must not masquerade as a fresh signed approval.

## Agent integration while the desk runs

The desk writes `.chap/agent.json` with `base_url` and `agent_token`.
Send JSON `{ "draft": {...}, "kind": "project_decision", "context": {...} }`
to `POST /api/proposals` with `Content-Type: application/json` and
`X-CHAP-Agent: <agent_token>`. Read `GET /api/tasks/<task_id>` or
`GET /api/tasks/<task_id>/result` with that same header. Pending/rejected results
return HTTP 409; callers must not fall back to the original draft.

The agent capability cannot decide reviews; those require the separate reviewer
capability. This is the upstream desk's convenience API over real CHAP, not an
MCP server. No automatic ChatGPT connector or cross-chat capture is installed.
A future agent must explicitly submit a proposal from an environment able to
reach the local desk, or prepare a proposal file for the owner to import.

## Export, verify and back up

Stop the desk before CLI access: one process owns the SQLite database.

```sh
.venv-chap/bin/python tools/chap/chap.py verify
.venv-chap/bin/python tools/chap/chap.py export .chap/evidence-001.json
.venv-chap/bin/python tools/chap/chap.py verify-export .chap/evidence-001.json
.venv-chap/bin/python tools/chap/chap.py backup /safe/location/spheroboy-decisions.db
```

Exports contain the whole workspace, not just the selected decision. Review for
private information before committing an export under `docs/decisions/evidence/`.
The database, tokens and raw exports in `.chap/` are ignored by Git. Back up the
SQLite database externally; an export is evidence, **not a restore format**.
To restore, stop the desk, preserve the current database and sidecar files,
then copy the backup to a new path and run `--db /new/path/decisions.db verify`
before starting `--db /new/path/decisions.db serve`. Do not copy a live database.

`verify-export` recomputes the audit chain, including the final entry, without
trusting the embedded verification result. It does not authenticate the snapshot,
arrival timestamps or human identity. Retain the printed `chain_head` outside
the database operator's control and pass `--expected-head sha256:...` when
verifying the corresponding export. Without an independent anchor, someone able
to rewrite the whole log can recompute it. Git history alone is not an immutable
external anchor. No OIDC, signatures or external transparency service is enabled.
The `audit-scitt/1.0` profile is used for local chain verification only.

## Validation and upgrades

```sh
PYTHONPATH=tools/chap/vendor .venv-chap/bin/python -m unittest discover -s tools/chap/vendor -p 'test_upstream.py' -v
.venv-chap/bin/python -m unittest discover -s tools/chap -p 'test_chap.py' -v
```

The dependency is pinned with the published wheel SHA-256. Vendored example
files retain their Apache-2.0 licence and [exact upstream commit](../../tools/chap/vendor/UPSTREAM.md).
Before upgrading, back up the database, review upstream migrations and run these
tests against a copy. The prototype is appropriate for personal decision records;
it is not non-repudiable identity verification or a hardware execution gate.
