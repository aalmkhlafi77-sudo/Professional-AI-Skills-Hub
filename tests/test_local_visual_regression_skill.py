import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "skills/local-visual-regression"


class VisualSkillTests(unittest.TestCase):
    def test_bundle(self):
        for path in ("SKILL.md", "agents/openai.yaml", "references/baselines.md",
                     "references/playwright-example.md"):
            self.assertTrue((ROOT / path).is_file(), path)

    def test_baseline_review_is_mandatory(self):
        content = (ROOT / "SKILL.md").read_text(encoding="utf-8").lower()
        for phrase in ("localhost", "visually", "reduced motion", "rtl", "baselines"):
            self.assertIn(phrase, content)

    def test_fixture_has_responsive_and_negative_checks(self):
        content = (ROOT / "references/playwright-example.md").read_text(encoding="utf-8")
        for phrase in ("1440", "390", "768", "toHaveScreenshot", "scrollWidth", "focus-visible", "rtl"):
            self.assertIn(phrase, content)

    def test_no_automatic_baseline_acceptance(self):
        content = (ROOT / "references/baselines.md").read_text(encoding="utf-8")
        self.assertIn("Never auto-update baseline", content)
        self.assertIn("Human reviewer", content)


if __name__ == "__main__":
    unittest.main()
