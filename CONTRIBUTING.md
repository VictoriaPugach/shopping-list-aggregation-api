# Contributing

## Before opening a pull request

1. Keep the public API and the Recipe contract compatible with v1.
2. Add or update tests for changed behavior.
3. Run `make test` and `docker compose config`.
4. Describe a changed normalization rule or synonym in the pull request.

## Review

Victoria Pugach reviews contract compatibility. Lyuba Novokhatskaya reviews security. Both may review the aggregation flow and tests.

One approval is required for an ordinary pull request. Changes to the public API, Recipe mapping, units, or ingredient matching require two approvals. If reviewers differ by more than 10% in evaluation, they revisit the work together.
