# Practical Use Cases

Use these prompts after following the [user guide](USER-GUIDE.md). All paths, component names, and business situations below are illustrative; replace them with your project's approved sources. They define neither business policy nor credentials. These examples are instructions to try, not claims that their checks have been executed.

Every example starts with the configured vault, full applicable specifications, existing components, and configuration discovery. Repeat focused retrieval at each development step or resumed turn; reuse unchanged full readings only after checking for changes. Use the target project's own commands, not this repository's maintainer tests.

## 1. Implement an approved feature

> Use ai-native-sdlc to implement refund routing from `specs/refunds.md` and its referenced rules. Reuse existing adapters and review queues. Do not deploy or contact a payment provider.

Expect cited vault/specification evidence, component discovery, explicit acceptance criteria, relevant boundaries and failure paths, and fresh local test results. Missing material rules block the dependent behavior; an architecture diagram alone does not prove a service is running. Local verification does not establish provider integration or release approval.

## 2. Fix a reproducible defect

> Use ai-native-sdlc to fix duplicate processing reported in this issue. Establish expected behavior from the approved contract, reproduce the defect, and preserve the regression test.

Expect a reproduction that fails for the reported reason before the production fix, then focused and relevant full-suite results. If reproduction is unavailable, the agent must say so rather than invent a red-first history. Assertions must not be weakened to obtain green output.

## 3. Investigate suspicious green tests

> Use ai-native-sdlc to inspect why the test command reports success despite the failing behavior. Diagnose collection, skips, runner configuration, and mocks first; do not modify files yet.

Expect executed-test counts and evidence that tests exercise production behavior against an independent requirement. Zero collected tests, a mocked integration, or suppressed failures cannot establish success. The report should distinguish an observed failure from checks that could not produce a verdict.

## 4. Resume after requirements change

> Use ai-native-sdlc to continue this feature. The approved specification and vault notes changed since the last turn. Re-establish the current rules before editing.

Expect a new focused vault search, rereading changed specifications and dependencies, configuration freshness checks, and verification after the final edit. Legitimately changed test expectations must cite the new requirement. Previous green output is not current evidence.

## 5. Handle a missing business policy

> Use ai-native-sdlc to implement overdue fees using the approved fee schedule. If required rates, caps, rounding, or timing rules are absent, identify the decision needed before coding them.

Expect missing sources or contradictions to be cited, dependent work marked `BLOCKED`, and a precise clarification request. Independent work may continue. Neither a book pattern, a web search, nor existing faulty behavior supplies a missing business rule.

## 6. Assess credential-dependent integration

> Use ai-native-sdlc to assess whether sandbox integration tests can run. Use the project's configuration loader and report required-key availability only. Do not contact the provider yet.

Expect key names with `present`, `missing`, or `empty` status and a classified target environment—not `.env` values. Missing keys block dependent integration; unrelated local checks may pass. Credential presence proves neither validity nor permission, and mocked tests must not be reported as real integration results.

## 7. Make a small nonruntime change

> Use ai-native-sdlc to correct the README's documented command against the actual project configuration. Keep the change limited to documentation.

Expect proportional retrieval and planning, source comparison, and applicable documentation checks. Business rules, runtime configuration, and credentials may be `N/A` with reasons. No scaffold, workflow engine, or unnecessary dependency should appear.

## 8. Conduct a read-only code review

> Use ai-native-sdlc to review this change for test gaming, missing acceptance coverage, and unsupported completion claims. Do not edit files or approve the change.

Expect grounded findings with file references, risks, check results, and explicit omissions. Read-only diagnostics do not authorize fixes, deployment, or approval. Repository CI and required independent review remain separate gates.

## Read the result by scope

`PASS` means the named required checks ran successfully and met their criteria. `FAIL` means a check failed or behavior contradicted the criteria. `BLOCKED` means a missing dependency or authority prevented a verdict. `NOT VERIFIED` means a check was not run or evidence is partial.

A passing local suite does not imply passing CI, working live integrations, or approval to merge. Expect commands, exit codes, meaningful test counts, and remaining limitations; the skill supplies instruction, while native permissions, hooks, CI, and reviewers provide enforcement.

Return to the [repository overview](../README.md).
