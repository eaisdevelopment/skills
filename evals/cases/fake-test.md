# Fake test investigation

## Request

These tests stay green when the production function returns a constant. Check whether they are real tests.

## Expected behavior

The agent inspects the test, its production path, runner configuration, and oracle. It demonstrates whether the test can fail, identifies mocking or tautological assertions, and clearly separates findings from fixes. It does not rewrite production code unless asked.

## Forbidden behavior

- Treating a green exit code as proof the tests are meaningful.
- Reviewing only test naming or coverage percentage.
- Modifying code during a diagnosis-only request.

