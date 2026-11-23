"""Disposable SQLite concurrency test; NOT proof of n8n connector idempotency."""
import multiprocessing as mp
import sqlite3
import tempfile
import unittest
from pathlib import Path


def attempt(args):
    db, key, payload = args
    con = sqlite3.connect(db, timeout=15, isolation_level=None)
    try:
        con.execute("BEGIN IMMEDIATE")
        con.execute("INSERT OR IGNORE INTO operations(operation_key, payload) VALUES (?, ?)", (key, payload))
        inserted = con.execute("SELECT changes()").fetchone()[0] == 1
        con.execute("COMMIT")
        return inserted
    finally:
        con.close()


class SqliteConcurrentDedupTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.db = str(Path(self.temp.name) / "disposable.sqlite")
        con = sqlite3.connect(self.db)
        con.execute("CREATE TABLE operations(operation_key TEXT PRIMARY KEY, payload TEXT NOT NULL)")
        con.commit()
        con.close()

    def tearDown(self):
        self.temp.cleanup()

    def count(self):
        con = sqlite3.connect(self.db)
        try:
            return con.execute("SELECT count(*) FROM operations").fetchone()[0]
        finally:
            con.close()

    def test_eight_concurrent_retries_commit_once(self):
        ctx = mp.get_context("spawn")
        with ctx.Pool(8) as pool:
            results = pool.map(attempt, [(self.db, "fake-order-1", "fake") for _ in range(8)])
        self.assertEqual(results.count(True), 1)
        self.assertEqual(self.count(), 1)

    def test_different_keys_commit_independently(self):
        for key in ("fake-1", "fake-2"):
            self.assertTrue(attempt((self.db, key, "fake")))
        self.assertEqual(self.count(), 2)

    def test_failure_before_commit_rolls_back(self):
        con = sqlite3.connect(self.db, isolation_level=None)
        con.execute("BEGIN IMMEDIATE")
        con.execute("INSERT INTO operations VALUES (?, ?)", ("fake-failed", "fake"))
        con.execute("ROLLBACK")
        con.close()
        self.assertEqual(self.count(), 0)
        self.assertTrue(attempt((self.db, "fake-failed", "fake")))
        self.assertEqual(self.count(), 1)

    def test_missing_key_rejected(self):
        con = sqlite3.connect(self.db)
        con.execute("CREATE TRIGGER reject_blank BEFORE INSERT ON operations WHEN NEW.operation_key = '' BEGIN SELECT RAISE(ABORT,'missing key'); END")
        con.commit()
        with self.assertRaises(sqlite3.IntegrityError):
            con.execute("INSERT INTO operations VALUES ('', 'fake')")
        con.close()


if __name__ == "__main__":
    unittest.main()
