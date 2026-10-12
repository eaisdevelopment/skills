---
name: ai-native-sdlc
description: "Execute software changes and reviews using mandatory knowledge-vault research, full applicable specifications, existing architecture and configuration, and fresh verification evidence. Use for coding tasks, business or technical research supporting development, suspicious tests, and completion reviews. Recheck local knowledge at every task step or resumed turn before proposing code or searching the internet."
license: Proprietary
metadata:
  version: "1.1.0"
  owner: "Pavlo"
  short-description: "Evidence-first coding and test-integrity discipline"
---

# AI-native SDLC Integrity

Help deliver the requested change through the repository's existing workflow, grounding each decision in local evidence.

The skill is language- and stack-neutral. Never assume Python, JavaScript, JVM, Go, Swift, or any particular test runner; discover the target repository's actual toolchain.

## Operating contract

1. Read the applicable repository instructions before acting. Treat repository commands, CI, permissions, hooks, ownership rules, and approval requirements as authoritative.
2. Apply the research sequence below at every task step and development turn, including planning, implementation, debugging, testing, review, and resumption after compaction. Read [vault retrieval](references/knowledge-vault.md) and [project grounding](references/project-grounding.md) before the first decision.
3. Keep process proportional. A small safe edit needs a small plan; a security, money, data, migration, public-API, infrastructure, or deployment change needs explicit risks and stronger checks.
4. Inspect before editing. Reuse the existing architecture and tooling. Do not introduce this skill's own framework, state files, policy database, scaffold, or generic verification engine.
5. Implement the smallest coherent change. Do not hide unrelated defects or expand scope silently.
6. Verify after the last relevant edit using the repository's real commands. Read [completion evidence](references/completion-evidence.md) before reporting success.
7. When tests are created, changed, suspicious, or failing, read [test integrity](references/test-integrity.md).

## Required research sequence

After loading repository instructions, and before deciding how to implement or test:

1. Search the configured knowledge vaults for the current business domain, problem, components, and failure modes; read relevant notes and source evidence.
2. Locate and read the full applicable business/feature specification and its referenced rules, contracts, and acceptance criteria before business research or behavior decisions.
3. Inspect existing architecture, ADRs, implementation, schemas, integrations, infrastructure, and deployment definitions for components and conventions to reuse.
4. Locate the task's configuration sources, including `.env`; establish required keys, selected environment, and credential availability using the project's loader without emitting secret values.
5. Resolve remaining evidence gaps through authoritative documentation or an explicit question. Propose and implement code only when the requirements and dependencies are established.

At each next step or turn, run a focused vault search for that step and check whether previously read specifications/configuration changed. Reuse unchanged full readings with citations; reread changed or newly applicable documents. A progress-only reply needs no extra search.

Keep a brief source trail in the existing plan, review, or response: vault queries and useful notes, full specifications read, components/configuration inspected, and remaining gaps. Report an actual no-match; never claim a search or full reading that did not happen.

Retrieval order is not authority: the user's requirements and approved project specifications govern business behavior. Vault patterns inform implementation. Contradictions or missing material business rules block dependent work; continue independent work where possible. Mark configuration `N/A` with a reason when no runtime or credentials are involved.

Use internet research after local discovery to resolve a named gap or verify current external facts; local sources cannot establish current API, security, or regulatory details. Use primary documentation for technical claims and keep secrets/private material out of queries. Never invent business rules, component capabilities, credentials, or a history of verification.

## Change workflow

### Orient

- Complete the required research sequence and establish the requested outcome, scope, risks, and acceptance criteria.
- Identify the authoritative build, test, lint, type-check, security, and integration commands from project files and CI.
- Define what observable result would prove the request is satisfied.
- Protect user changes already present; never discard or rewrite them without explicit authority.

### Plan and implement

- Use acceptance criteria as the boundary of the change.
- Identify failure modes and the riskiest assumption before coding.
- Prefer existing patterns and direct fixes over parallel implementations, compatibility copies, or speculative abstractions.
- For defects, add or identify a reproduction that fails for the reported reason before applying the fix when feasible.
- If a required test appears wrong, stop and explain the conflict with its specification or oracle. Do not change it merely to make the suite green.

### Verify

- Run focused checks while iterating, then the repository's authoritative verification after the final edit.
- Inspect the resulting diff for scope creep, disabled checks, weakened assertions, silent fallbacks, placeholders, and accidental generated files.
- Exercise relevant unhappy paths and boundaries, not only the happy path.
- Treat CI and required human review as independent gates. Never approve or merge your own work unless the user explicitly owns and delegates that action.

## Reporting contract

Use only evidence from the current session and current tree.

- `PASS`: all required checks ran successfully and the result matches the acceptance criteria.
- `FAIL`: a required check ran and failed, or the implementation contradicts the criteria.
- `BLOCKED`: verification cannot run or requires missing authority, credentials, infrastructure, or a decision.
- `NOT VERIFIED`: a check was not run or only partial evidence exists.

Do not say “done,” “fixed,” “passing,” “ready,” or equivalent when any required result is blocked or not verified. Report the commands run, exit codes, meaningful test counts, and limitations. Acknowledge that human approval and CI remain pending when applicable.

## Native enforcement

Prefer controls already supplied by the repository and agent platform:

- permissions and sandbox boundaries for prohibited actions;
- hooks for deterministic pre-action checks;
- protected branches and code ownership for independent approval;
- CI for authoritative, clean-environment verification;
- repository-native linters, test runners, coverage, mutation, contract, and security tools.

Recommend a new mechanical control only for a demonstrated recurring gap. Keep it local to the repository and verify it with a positive and negative case.
