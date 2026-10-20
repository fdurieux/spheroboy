import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

import chap
from chap_starter import ReviewPending, ReviewRejected, StorageError


class SpheroboyTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.db = Path(self.tmp.name) / 'decisions.db'

    def gate(self):
        return chap.ReviewGate(db=self.db, workspace=chap.WORKSPACE,
                               agents=chap.AGENTS, reviewer=chap.REVIEWER)

    def test_restart_edit_reject_and_backup(self):
        with self.gate() as gate:
            first = gate.propose({'proposal': 'candidate pin', 'verified': False})
            second = gate.propose({'proposal': 'erase'})
            with self.assertRaises(ReviewPending):
                gate.result(first)
        with self.gate() as gate:
            self.assertFalse(gate.inspect(first)['allowed'])
            gate.decide(first, 'edit', edited={'proposal': 'measure pin', 'verified': False},
                        rationale='Need electrical evidence first')
            gate.decide(second, 'reject', rationale='No backup evidence')
        backup = Path(self.tmp.name) / 'backup.db'
        chap.main(['--db', str(self.db), 'backup', str(backup)])
        with chap.ReviewGate(db=backup, workspace=chap.WORKSPACE,
                             agents=chap.AGENTS, reviewer=chap.REVIEWER) as gate:
            self.assertEqual(gate.result(first)['proposal'], 'measure pin')
            self.assertFalse(gate.result(first)['verified'])
            with self.assertRaises(ReviewRejected):
                gate.result(second)

    def test_export_tamper_truncation_and_anchor(self):
        path = Path(self.tmp.name) / 'evidence.json'
        with self.gate() as gate:
            task = gate.propose({'proposal': 'inspect'})
            gate.decide(task, 'approve', rationale='Read-only inspection')
            gate.export(path)
        body = chap.read_json(path)
        head = chap.verify_export(body)['chain_head']
        self.assertTrue(chap.verify_export(body, head)['external_anchor_checked'])
        changed = copy.deepcopy(body)
        changed['entries'][-1]['envelope']['params']['comment'] = 'Changed'
        with self.assertRaises(ValueError):
            chap.verify_export(changed)
        changed = copy.deepcopy(body)
        changed['entries'].pop()
        with self.assertRaises(ValueError):
            chap.verify_export(changed)
        with self.assertRaises(ValueError):
            chap.verify_export(body, 'sha256:' + '0' * 64)

    def test_double_writer_refused(self):
        with self.gate():
            with self.assertRaises(StorageError):
                self.gate()

    def test_cli_cannot_approve_from_pipe(self):
        with self.gate() as gate:
            task = gate.propose({'proposal': 'inspect'})
        result = subprocess.run([sys.executable, str(chap.HERE / 'chap.py'),
                                 '--db', str(self.db), 'review', task],
                                input='approve\nYes\n', text=True, capture_output=True)
        self.assertNotEqual(result.returncode, 0)
        with self.gate() as gate:
            self.assertFalse(gate.inspect(task)['allowed'])

    def test_missing_db_not_silently_created(self):
        with self.assertRaises(SystemExit):
            chap.main(['--db', str(self.db), 'list'])
        self.assertFalse(self.db.exists())


if __name__ == '__main__':
    unittest.main()
