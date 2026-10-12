# v1.1 Implementation Plan

1. Preserve audit evidence, the knowledge vault, adversarial fixtures/evals, and release archives.
2. Remove the active framework implementation under `skills/ai-native-sdlc/`.
3. Create a concise `SKILL.md` with proportional change, verification, review, and claim-reporting behavior.
4. Add focused references for evidence, test integrity, and knowledge-vault use.
5. Replace framework-centric tests with structural and behavioral tests for v1.1.
6. Validate the skill and run its tests.
7. Dogfood it against this change: inspect the diff, challenge test quality, run all authoritative checks after the final edit, and record exact evidence in `VERIFICATION.md`.

## Risks

- Overfitting the skill to the failures already observed.
- Turning concise guidance into another universal framework.
- Mistaking textual conformance tests for behavioral proof.
- Losing unique evidence while removing generated machinery.

## Controls

Keep evidence and knowledge outside the active skill, use outcome-based scenarios, and retain historical release archives for recovery.

## Memory integration update

1. Read the full current product specification and consult vault notes on knowledge use, acceptance criteria, and architecture decisions.
2. Make retrieval mandatory at each development step/turn; define full specification reading, component discovery, and secret-safe configuration consumption.
3. Add one focused project-grounding reference and four realistic evaluation cases. Update resource-contract checks for the intended fifth file.
4. Forward-test with independent agents in temporary projects, including a changed requirement on a later turn. Review actual commands, edits, and results.
5. Run repository and canonical validation after fixes; record sources, evidence, limitations, and conservation hashes. Do not deploy or use real credentials for these evaluations.

## Local end-user documentation follow-up

1. Retrieve vault knowledge on accessible documentation/developer experience and read the full current product specification, references, tooling, and license.
2. Verify host setup conventions against official documentation; write an end-user overview, one focused user guide, and practical use cases. Keep the shipped skill unchanged.
3. Add meaningful checks for missing/broken documentation links and accidental private-corpus link targets; run them before and after writing.
4. Exercise guarded copy instructions in isolated temporary projects, with an existing-destination negative case. Do not install globally or claim host activation from copying.
5. Obtain independent documentation review, run authoritative checks after final edits, and record evidence/limits in `DOCUMENTATION-VERIFICATION.md`. Preserve private evidence and recovery files; leave publishing untouched.

## Linux/macOS native distribution

1. Retrieve reproducibility/configuration knowledge, read current requirements, and check installed CLI capabilities against primary host documentation.
2. Add four native metadata files and a minimal Make/tar recipe generating only an allowlisted clean marketplace. Preserve the canonical skill and historical collections.
3. Add failing distribution-contract tests before the implementation: exact payload/bytes, no private chaff, output overwrite refusal, missing/symlinked source rejection, and manifest identity/path consistency.
4. Validate/build the bundle; forward-test isolated Claude user installation and Codex read-only marketplace discovery without changing HOME/CODEX_HOME or real user settings.
5. Update end-user guidance and record fresh tests, payload hashes, review findings, and unverified Linux/Codex-host behavior. No GitHub publication or custom installer.
