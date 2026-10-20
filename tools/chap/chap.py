#!/usr/bin/env python3
"""Local Spheroboy decision recording using the pinned CHAP coordinator."""
import argparse
import json
import os
from pathlib import Path
import sqlite3
import sys
import webbrowser

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE / 'vendor'))
from chap_starter import ReviewGate, ChapError, StorageError
from chap_coordinator.audit import entry_is_well_formed, entry_record, link_hash
from chap_coordinator.types import AuditEntry
from chap_coordinator.canonical import ZERO_HASH
import server

WORKSPACE = 'wsp_spheroboy'
REVIEWER = 'human:fdurieux'
AGENTS = ('agent:spheroboy-assistant', 'agent:manual-submission')
server.DEMO_AGENT, server.PASTE_AGENT = AGENTS
server.SCENARIOS = {}  # No sample decisions in the real project log.


def read_json(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def emit(value):
    # Escape invisible/non-ASCII characters in the terminal review surface.
    print(json.dumps(value, indent=2, ensure_ascii=True))


def verify_export(body, expected_head=None):
    """Check CHAP envelopes against the chain head, never trust a stored verdict."""
    if body.get('format') != 'chap-starter-evidence/1':
        raise ValueError('Unsupported export format')
    entries = body.get('entries')
    if not isinstance(entries, list) or not entries:
        raise ValueError('Missing audit entries')
    previous = ZERO_HASH
    for index, item in enumerate(entries):
        entry = AuditEntry(**item)
        if entry.seq != index or not entry_is_well_formed(entry):
            raise ValueError('Invalid entry or sequence')
        if entry.prev_hash != previous:
            raise ValueError('Broken audit chain')
        call = entry.envelope or entry.request
        if call.get('params', {}).get('workspace') != body.get('workspace'):
            raise ValueError('Workspace mismatch')
        previous = link_hash(entry_record(entry), previous)
    head = body.get('verification', {}).get('chain_head')
    if previous != head or (expected_head is not None and previous != expected_head):
        raise ValueError('Chain head mismatch')
    return {'status': 'verified', 'entries': len(entries), 'chain_head': previous,
            'scope': 'envelopes only; snapshot, arrival metadata and identity are not authenticated',
            'external_anchor_checked': expected_head is not None}


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--db', type=Path, default=ROOT / '.chap' / 'decisions.db')
    sub = p.add_subparsers(dest='command', required=True)
    for name in ('init', 'list', 'verify'):
        sub.add_parser(name)
    proposal = sub.add_parser('propose')
    proposal.add_argument('file', type=Path, help='JSON with draft, kind and context')
    review = sub.add_parser('review')
    review.add_argument('task_id')
    show = sub.add_parser('show')
    show.add_argument('task_id')
    export = sub.add_parser('export')
    export.add_argument('file', type=Path)
    check = sub.add_parser('verify-export')
    check.add_argument('file', type=Path)
    check.add_argument('--expected-head')
    backup = sub.add_parser('backup')
    backup.add_argument('file', type=Path)
    desk = sub.add_parser('serve')
    desk.add_argument('--port', type=int, default=7331)
    desk.add_argument('--no-browser', action='store_true')
    a = p.parse_args(argv)
    os.umask(0o077)
    try:
        if a.command == 'verify-export':
            emit(verify_export(read_json(a.file), a.expected_head))
            return
        if a.command != 'init' and not a.db.exists():
            raise ValueError('Database is missing. Run init explicitly first; do not silently replace a lost log.')
        with ReviewGate(db=a.db, workspace=WORKSPACE, reviewer=REVIEWER, agents=AGENTS) as gate:
            if a.command in ('init', 'verify'):
                emit(gate.verify())
            elif a.command == 'list':
                emit(gate.tasks())
            elif a.command == 'show':
                emit(gate.inspect(a.task_id))
            elif a.command == 'propose':
                body = read_json(a.file)
                draft = body['draft']
                for field in ('subject', 'proposal', 'evidence', 'conditions'):
                    if field not in draft:
                        raise ValueError('Draft requires ' + field)
                emit({'task_id': gate.propose(draft, kind=body.get('kind', 'project_decision'),
                                             context=body.get('context', {}))})
            elif a.command == 'review':
                if not sys.stdin.isatty():
                    raise ValueError('Human review requires an interactive terminal; agents must leave proposals pending.')
                view = gate.inspect(a.task_id)
                emit(view)
                action = input('approve / edit / reject / Enter to defer: ').strip()
                if not action:
                    print('Left pending.')
                    return
                edited = read_json(input('Edited JSON file: ').strip()) if action == 'edit' else None
                rationale = input('Reason (required): ').strip()
                if not rationale:
                    raise ValueError('A reason is required')
                emit(gate.decide(a.task_id, action, edited=edited, rationale=rationale,
                                 expected_digest=view['digest']))
            elif a.command == 'export':
                gate.verify()
                if a.file.exists():
                    raise ValueError('Use a new export filename; existing evidence will not be overwritten')
                gate.export(a.file)
                emit(verify_export(read_json(a.file)))
            elif a.command == 'backup':
                if a.file.exists():
                    raise ValueError('Backup destination already exists')
                with sqlite3.connect(str(a.db)) as source, sqlite3.connect(str(a.file)) as target:
                    source.backup(target)
                print('Backup saved: ' + str(a.file))
            elif a.command == 'serve':
                with server.ReviewServer(('127.0.0.1', a.port), gate) as http:
                    connection = a.db.parent / 'agent.json'
                    server.write_connection(http, connection)
                    url = http.base_url + '/#reviewer=' + http.reviewer_token
                    print('Private human review link (do not share with agents):\n' + url, flush=True)
                    print('Agent connection file: ' + str(connection), flush=True)
                    if not a.no_browser:
                        webbrowser.open(url)
                    try:
                        http.serve_forever(poll_interval=0.25)
                    except KeyboardInterrupt:
                        pass
    except (ValueError, KeyError, TypeError, OSError, ChapError, StorageError) as exc:
        p.exit(1, str(exc) + '\n')


if __name__ == '__main__':
    main()
