import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills/plain-php-mysql-security"


class PlainPhpMysqlSkillTests(unittest.TestCase):
    def test_complete_skill_bundle(self):
        for name in ("SKILL.md", "agents/openai.yaml", "references/security.md",
                     "references/transactions.md", "references/deployment.md"):
            self.assertTrue((SKILL / name).is_file(), name)
            self.assertGreater((SKILL / name).stat().st_size, 100)

    def test_scope_and_review_requirements(self):
        body = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("name: plain-php-mysql-security", body)
        self.assertIn("description:", body)
        for name in ("security.md", "transactions.md", "deployment.md"):
            self.assertIn("references/" + name, body)
        for term in ("PDO", "rollback", "Laravel", "DECIMAL", "production"):
            self.assertIn(term.lower(), body.lower())

    def test_transaction_negative_cases(self):
        body = (SKILL / "references/transactions.md").read_text(encoding="utf-8").lower()
        for term in ("duplicate", "rollback", "deadlock", "concurrent", "idempotency", "implicit"):
            self.assertIn(term, body)

    def test_security_negative_cases(self):
        body = (SKILL / "references/security.md").read_text(encoding="utf-8").lower()
        for term in ("csrf", "authorization", "finfo", "symlink", "session", "injection"):
            self.assertIn(term, body)


if __name__ == "__main__":
    unittest.main()
