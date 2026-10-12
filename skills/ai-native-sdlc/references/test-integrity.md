# Test Integrity

Read this when tests are written, changed, failing, suspicious, or used as completion evidence.

## Core test

A useful test must execute relevant production behavior and be capable of failing when that behavior is wrong. Its expected result must come from an independent oracle: an accepted requirement, standard, policy, captured contract, deliberately simple reference implementation, or a derivation visible in the test.

## Refuse test gaming

Do not obtain green output by:

- deleting, renaming, moving, commenting out, skipping, focusing, quarantining, or making failures expected;
- weakening equality, ranges, tolerances, counts, coverage thresholds, or exception expectations;
- mocking the unit under test or returning the exact value later asserted;
- swallowing exceptions, returning success early, rewriting reports, or allowing zero tests;
- changing expected values only because implementation output changed;
- hard-coding production behavior for known test inputs;
- labeling mocked tests as integration or end-to-end evidence;
- adding retries to conceal deterministic or flaky failures.

If the specification legitimately changed, update tests transparently and explain the new oracle. Keep the test change reviewable; do not hide it inside a broad implementation diff.

## Defect workflow

When feasible:

1. Reproduce the defect with the smallest representative test.
2. Run it before the fix and confirm it fails for the expected reason.
3. Apply the production fix without weakening the reproduction.
4. Run the focused test and the relevant full suite.
5. Inspect collection and skip counts, not only the exit code.

If the original behavior cannot be reproduced, report that limitation. Do not invent a red-first history.

## Adversarial review

Ask:

- Would the test fail if the implementation returned a constant or skipped the critical branch?
- Does it assert externally observable behavior rather than its own mocks?
- Are important negative, boundary, authorization, money, and failure cases covered?
- Can test discovery silently omit the file or case?
- Does the runner configuration permit no-tests success, ignored failures, retries, or exclusions?
- Were tests or test configuration weakened in the diff?

When a test appears incorrect, identify the conflicting requirement or oracle and stop for a decision. A failing honest test is better evidence than a manufactured green suite.

