from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "ai-native-sdlc"


class SkillBoundaryTests(unittest.TestCase):
    def test_active_skill_contains_only_instructions(self) -> None:
        files = {path.relative_to(SKILL).as_posix() for path in SKILL.rglob("*") if path.is_file()}
        self.assertEqual(
            files,
            {
                "SKILL.md",
                "references/completion-evidence.md",
                "references/knowledge-vault.md",
                "references/project-grounding.md",
                "references/test-integrity.md",
            },
        )

    def test_entrypoint_is_compact_and_has_valid_identity(self) -> None:
        text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        self.assertLessEqual(len(text.splitlines()), 140)
        self.assertRegex(text, r"(?m)^name: ai-native-sdlc$")
        self.assertRegex(text, r'(?m)^  version: "1\.1\.0"$')
        self.assertNotIn("scripts/sdlc.py", text)
        self.assertNotIn("sdlc.py check", text)

    def test_references_linked_from_entrypoint_exist(self) -> None:
        text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        links = re.findall(r"\[[^]]+\]\((references/[^)]+)\)", text)
        references = {p.relative_to(SKILL).as_posix() for p in (SKILL / "references").glob("*.md")}
        self.assertEqual(set(links), references)
        for link in links:
            self.assertTrue((SKILL / link).is_file(), link)

    def test_entrypoint_does_not_prescribe_a_stack_toolchain(self) -> None:
        text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        prescribed_commands = (
            "pytest ", "npm test", "pnpm test", "mvn test", "gradle test", "go test", "swift test"
        )
        for command in prescribed_commands:
            self.assertNotIn(command, text.lower(), command)

    def test_skill_package_excludes_private_corpus(self) -> None:
        self.assertFalse((SKILL / "memory").exists())
        self.assertFalse((SKILL / "docs" / "audit").exists())
        self.assertFalse(any(p.is_symlink() for p in SKILL.rglob("*")))

    def test_retired_runtime_is_not_active(self) -> None:
        forbidden = ["install.py", "install.sh", ".claude-plugin", "claude", "tools"]
        for relative in forbidden:
            self.assertFalse((ROOT / relative).exists(), relative)
        self.assertFalse(any(SKILL.rglob("*.py")))


class BehavioralCaseTests(unittest.TestCase):
    def test_cases_define_observable_good_and_bad_behavior(self) -> None:
        cases = sorted((ROOT / "evals" / "cases").glob("*.md"))
        self.assertGreaterEqual(len(cases), 6)
        for case in cases:
            text = case.read_text(encoding="utf-8")
            with self.subTest(case=case.name):
                self.assertIn("## Request", text)
                self.assertIn("## Expected behavior", text)
                self.assertIn("## Forbidden behavior", text)
                self.assertGreaterEqual(len(text.split()), 45)

    def test_cases_cover_original_high_value_failures(self) -> None:
        names = {path.stem for path in (ROOT / "evals" / "cases").glob("*.md")}
        self.assertTrue(
            {"false-done", "fake-test", "weaken-test", "zero-tests", "red-first", "small-change"}
            <= names
        )

    def test_grounding_scenarios_are_available(self) -> None:
        names = {path.stem for path in (ROOT / "evals" / "cases").glob("*.md")}
        self.assertTrue(
            {"memory-first", "resumed-turn", "missing-grounding", "credential-availability"} <= names
        )


if __name__ == "__main__":
    unittest.main()
