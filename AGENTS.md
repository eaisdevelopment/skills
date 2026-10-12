# Repository Guidelines

## Purpose and Boundaries

This repository contains the compact `ai-native-sdlc` integrity skill. The skill guides coding agents to use a project's existing SDLC honestly; it must not grow into a parallel workflow engine. Preserve `docs/audit/` as private evidence, `memory/architect-master-vault/` as a read-only knowledge base, and `dist/` as historical recovery material.

## Project Structure

- `skills/ai-native-sdlc/`: shipped skill and focused references.
- `evals/cases/`: realistic prompts with observable expected and forbidden behaviors.
- `tests/`: fast repository-contract tests.
- `docs/v1.1/`: product intent, specification, plan, and verification evidence.

Do not add installers, generated scaffolds, vendored engines, project state, framework adapters, or generic CI/deployment orchestration.

## Development and Verification

Run after the final relevant edit:

```sh
python3 -m unittest discover -s tests -t .
uv run --with pyyaml python "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-creator/scripts/quick_validate.py" skills/ai-native-sdlc
```

Tests use the standard-library `unittest` framework. Name files `test_<behavior>.py`, classes `<Area>Tests`, and methods `test_<expected_outcome>`. Test observable contracts such as resource boundaries, valid case structure, and resolvable links; do not pin prose merely by matching headings.

## Writing Style

Keep instructions concise, direct, and platform-neutral. Assume agents already know ordinary coding practices. Add guidance only when evidence shows it changes decisions or protects a real invariant. Put conditional detail in a focused reference and link it from `SKILL.md`.

## Change Quality

Apply `skills/ai-native-sdlc/SKILL.md` to work in this repository. Search the vault at each development step/turn, read the full applicable specification, inspect existing components/configuration, and cite sources before decisions. Use the project's existing loader for credentials and report availability only; never put `.env` values in context or artifacts.

Every change needs a clear outcome, acceptance criteria, proportional risk review, and fresh verification evidence. For defects, add a failing behavioral case or test before the fix when feasible. Never weaken tests to obtain green output. Pull requests should describe the user-visible behavioral change, risks, commands run, exit codes, and remaining unverified work. Use focused Conventional Commit subjects such as `fix(skill): reject stale verification evidence`.
