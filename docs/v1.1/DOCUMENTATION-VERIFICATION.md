# Local End-user Documentation Verification

## Scope

2026-10-09 follow-up: finish the overview, product description, setup, practical use cases, memory/configuration guidance, troubleshooting, and migration locally. No GitHub publication, release archive, global installation, license change, or shipped-skill change is authorized by this task.

The acceptance criteria are in `SPEC.md`; the proportional plan is in `PLAN.md`. Configuration/credentials are `N/A`: documentation and repository-maintenance checks require no application runtime or integration credentials.

## Grounding and review

Read repository instructions, the full product intent/specification/plan, the skill and all four references, current README/changelog, tests, CI, and license. Search the configured vault directly for documentation, onboarding, accessible knowledge, configuration, acceptance, and verification. Read its guide/index and `Knowledge_Management`, `Configuration_automation`, `Success_Criteria`, `Developer_Experience`, and `Design_Documentation` concepts. Use those concepts to keep the guidance accessible and actionable without reproducing private source text or building another workflow system.

The initial guessed `Documentation.md` vault path was absent (search exit 2); inventory located `Design_Documentation.md` instead. This was not recorded as a successful no-match or full reading. An output-truncated concept batch was completed through subsequent reads.

Current setup conventions were checked against fetched [OpenAI skill documentation](https://learn.chatgpt.com/docs/build-skills) and [Anthropic skill documentation](https://code.claude.com/docs/en/skills), not just search snippets. These establish discovery/invocation conventions, not tested compatibility of this particular skill in either host.

A separate agent drafted eight illustrative use cases. Another agent reviewed the end-user documents for consistency, secret handling, license restrictions, migration, and unsupported effectiveness claims. No blocking findings were reported; its optional read-only smoke-task suggestion was added. The examples are requests and expected behavior, not newly executed behavioral evaluations.

## Verification evidence

Before the user guide existed, `python3 -m unittest tests.test_user_documentation -v` exited 1: 2 tests ran, with 3 failing subtests identifying the missing guide and broken link. No tests were weakened to remove those failures.

Final local documentation verdict: **PASS** for the acceptance criteria within this task's scope. Evidence:

- `python3 -m unittest discover -s tests -t .` — exit 0; 11 tests, `OK`, including 2 new documentation/link checks. Independent review also ran `python3 -m unittest tests.test_user_documentation -v`: exit 0, 2 tests passed.
- `uv run --with pyyaml python "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-creator/scripts/quick_validate.py" skills/ai-native-sdlc` — exit 0; `Skill is valid!`.
- A fresh copy containing only public skill/tests/evals, README/changelog/license, user guides, and v1.1 documents ran the same unittest command: exit 0, 11 tests passed, without the private collections.
- The actual second/third `sh` blocks from `USER-GUIDE.md` were extracted with `awk` and executed in isolated temporary projects with `sdlc_source_dir` pointing to this local skill. Codex-path trial: `/tmp/sdlc-doc-codex.b8Uid2`; Claude-path trial: `/tmp/sdlc-doc-claude.NopToT`. Both initial copies exited 0. `diff -r` against the source exited 0; all five files matched. Re-executing each block against its existing destination exited 1, and another `diff -r` exited 0: no overwrite occurred.
- End-user documentation has resolvable local links and no links to private vault/audit/report/archive collections. Manual and independent review distinguish examples, historical model trials, structural tests, and untested host activation.

The copy trials test the documented shell commands and file layout only. They do not launch either host, configure global skills, or prove runtime activation. Existing-symlink behavior is guarded in the commands but was not a separate executed trial.

## Preservation baseline

Before and after editing, aggregate SHA-256 values matched:

- Shipped skill: `1257d218ca198a28da934c858464b37fa693b764e533a5f7c101d55cd76a4bef`.
- Private vault, `docs/audit/`, and historical `dist/`: `fbf1e5510bc4aa3cad2bfe75e4f7d87900aa277679545eb2e914b0a6a9c08d24`.

Use `find <roots> -type f -print0 | sort -z | xargs -0 shasum -a 256 | shasum -a 256`, with the skill root alone for the first value and the three protected roots for the second. The prior memory-integration evidence in `VERIFICATION.md` remains a dated historical record; it is not rewritten as a new run.

## Limits and publication

- Copy/layout trials do not establish actual Codex/Claude activation, model compliance, or live integrations. Host activation and new cross-model behavior remain `NOT VERIFIED`.
- Structural/link checks do not evaluate business correctness or ensure that no secret can ever be leaked. Independent content review is a separate check.
- Git revision binding and hosted CI are `NOT VERIFIED`: this workspace has no Git metadata. No remote write, push, repository-description update, or release was performed.
- The documentation and skill remain proprietary under the existing license. Permission to prepare local documentation does not publish private material or change licensing.
